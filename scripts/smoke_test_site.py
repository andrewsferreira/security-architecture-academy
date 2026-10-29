#!/usr/bin/env python3
"""Smoke tests do portal publicado: confere o site real depois do deploy do GitHub Pages.

Os endereços vêm da árvore (zensical.toml e curriculum/manifest.yml), não de uma lista fixa:

* Páginas principais — início, Começar, índices dos módulos publicados, laboratórios,
  avaliações (inclusive AS-FUND e AS-N1, quando no escopo), Research Library,
  Currículo e Roadmap, Sobre: HTTP 200 sem redirecionamento, gerador Zensical e
  ``<link rel="canonical">`` igual ao endereço pedido (uma página de erro servida com
  200 não passa).
* Versão: a página inicial mostra a versão publicada (``--expect-version``, padrão: a
  tag do RELEASE-MANIFEST.yml).
* sitemap.xml: contém todas as páginas da navegação e nenhuma página proibida.
* Assets essenciais: CSS e JavaScript do tema e do projeto, ícone e índice de busca.
* Endereços proibidos: Handbook (``internal/``), guia de ambiente local e módulos fora do
  escopo publicado precisam responder 404 — um 200, mesmo com aparência de erro, falha.

Propagação do Pages: cada verificação tem tentativas limitadas, com espera crescente
(``--attempts``, ``--backoff``) e prazo total (``--deadline``); as requisições levam
``?smoke=<valor>`` para não receber do CDN a versão anterior em cache. Uma falha só é declarada
depois de esgotadas as tentativas; o relatório separa indisponibilidade (rede, 5xx) de
conteúdo divergente. Requisições sequenciais, com intervalo mínimo entre elas.

Uso:
    python scripts/smoke_test_site.py                                  # site_url do zensical.toml
    python scripts/smoke_test_site.py --base-url https://…/ --expect-version v0.2.1
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import yaml

from _common import ROOT, iter_nav_files, load_config

USER_AGENT = "security-architecture-academy-smoke-test/1"
CANONICAL_RE = re.compile(r'<link rel="canonical" href="([^"]+)"')
GENERATOR_RE = re.compile(r'<meta name="generator" content="zensical')
ASSET_RE = re.compile(r'(?:href|src)="\./(assets/[^"]+\.(?:css|js))"')
CORE_PAGES = (
    "index.md", "getting-started/index.md", "labs/index.md", "assessments/index.md",
    "resources/index.md", "curriculum/index.md", "about/roadmap.md", "about/index.md",
)
CORE_ASSESSMENTS = ("AS-FUND", "AS-N1")
STATIC_ASSETS = ("assets/stylesheets/extra.css", "assets/javascripts/a11y.js",
                 "assets/branding/favicon.png", "search.json")
FORBIDDEN_PAGES = ("internal/", "getting-started/local-development/")


# --------------------------------------------------------------------- HTTP
@dataclass
class Response:
    status: int | None          # None: falha de rede ou timeout
    url: str                    # endereço final (após redirecionamento, se houver)
    body: str
    error: str = ""


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: D401 - API do urllib
        return None  # o 3xx volta como HTTPError e é tratado como redirecionamento inesperado


def fetch(url: str, timeout: float) -> Response:
    opener = urllib.request.build_opener(_NoRedirect)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache"})
    try:
        with opener.open(request, timeout=timeout) as resp:
            return Response(resp.status, resp.geturl(), resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as exc:
        location = exc.headers.get("Location", "") if exc.headers else ""
        return Response(exc.code, location or url, "", f"HTTP {exc.code}")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return Response(None, url, "", f"{type(exc).__name__}: {exc}")


# ------------------------------------------------------------- expectativas
def page_url(base: str, doc: str) -> str:
    """URL publicada de um arquivo de docs/ (diretórios com barra final, como no Zensical)."""
    if doc == "index.md":
        return base
    if doc.endswith("/index.md"):
        return base + doc[: -len("index.md")]
    return base + doc[: -len(".md")] + "/"


def expectations(root: Path) -> dict:
    config = load_config(root / "zensical.toml")
    project = config["project"]
    nav = [doc for doc in iter_nav_files(project.get("nav", [])) if (root / "docs" / doc).is_file()]
    manifest = yaml.safe_load((root / "curriculum" / "manifest.yml").read_text(encoding="utf-8"))
    modules = manifest.get("modules") or []
    published = [m for m in modules if m.get("status") == "published"]
    out_of_scope = [m for m in modules if m.get("status") != "published"]
    module_pages = [f"modules/{str(m['id'])[1:]}-{m['slug']}/index.md" for m in published]
    assessments = {a["id"]: a for a in manifest.get("assessments") or []}
    core = [p for p in CORE_PAGES if p in nav] + [p for p in module_pages if p in nav]
    core += [assessments[i]["path"] for i in CORE_ASSESSMENTS
             if i in assessments and assessments[i].get("path") in nav]
    forbidden = list(FORBIDDEN_PAGES) + [f"modules/{str(m['id'])[1:]}-{m['slug']}/" for m in out_of_scope]
    forbidden += [f"complements/{c['slug']}/" for c in manifest.get("complements") or [] if c.get("status") != "published"]
    version = None
    release_manifest = root / "RELEASE-MANIFEST.yml"
    if release_manifest.is_file():
        version = (yaml.safe_load(release_manifest.read_text(encoding="utf-8")) or {}).get("tag")
    return {"site_url": project.get("site_url"), "nav": nav, "core": core, "forbidden": forbidden,
            "version": version}


# --------------------------------------------------------------- verificações
@dataclass
class Result:
    name: str
    ok: bool
    detail: str
    transient: bool = False


def check_page(resp: Response, url: str, canonical_url: str | None = None) -> Result:
    """Página do portal servida no endereço pedido. ``canonical_url``: endereço com o site_url do projeto
    (difere de ``url`` quando o teste roda contra outro host, por exemplo um servidor local)."""
    if resp.status is None or (resp.status and resp.status >= 500):
        return Result(url, False, f"indisponível ({resp.error or resp.status})", transient=True)
    if 300 <= resp.status < 400:
        return Result(url, False, f"redirecionamento inesperado para {resp.url}")
    if resp.status != 200:
        return Result(url, False, f"HTTP {resp.status}", transient=resp.status == 404)  # propagação
    canonical = CANONICAL_RE.search(resp.body)
    if not GENERATOR_RE.search(resp.body) or not canonical:
        return Result(url, False, "conteúdo não é uma página do portal")
    if canonical.group(1) != (canonical_url or url):
        return Result(url, False, f"canonical {canonical.group(1)} difere do endereço esperado")
    return Result(url, True, "200, página do portal")


def check_version(resp: Response, url: str, version: str, canonical_url: str | None = None) -> Result:
    page = check_page(resp, url, canonical_url)
    if not page.ok:
        return page
    if not re.search(rf"{re.escape(version)}(?![\d.])", resp.body):
        # um deploy recém-concluído pode ainda servir a versão anterior em cache
        return Result(f"versão {version}", False, "página inicial sem a versão publicada", transient=True)
    return Result(f"versão {version}", True, "exibida na página inicial")


def check_asset(resp: Response, url: str) -> Result:
    if resp.status is None or (resp.status and resp.status >= 500):
        return Result(url, False, f"indisponível ({resp.error or resp.status})", transient=True)
    if resp.status != 200 or not resp.body:
        return Result(url, False, f"HTTP {resp.status}", transient=resp.status == 404)
    return Result(url, True, f"200, {len(resp.body)} bytes")


def check_absent(resp: Response, url: str) -> Result:
    if resp.status == 404:
        return Result(url, True, "404, como esperado")
    if resp.status is None or resp.status >= 500:
        return Result(url, False, f"indisponível ({resp.error or resp.status}) — ausência não confirmada",
                      transient=True)
    # 200 (mesmo com texto de erro) ou redirecionamento: o endereço existe. Pode ser cache de uma página
    # removida nesta versão, então também é reavaliado até o fim das tentativas.
    return Result(url, False, f"HTTP {resp.status}: endereço deveria estar indisponível", transient=True)


def check_sitemap(resp: Response, url: str, expected: set[str], forbidden: list[str], canon: str) -> Result:
    """Sitemap com as URLs canônicas (site_url): todas as páginas da navegação e nenhuma proibida."""
    if resp.status != 200:
        return Result(url, False, f"HTTP {resp.status or resp.error}", transient=True)
    try:
        locs = {el.text.strip() for el in ET.fromstring(resp.body).iter() if el.tag.endswith("loc") and el.text}
    except ET.ParseError as exc:
        return Result(url, False, f"XML inválido: {exc}")
    missing = sorted(expected - locs)
    blocked = sorted(loc for loc in locs if any(loc.startswith(canon + f) for f in forbidden))
    if missing or blocked:
        detail = "; ".join(filter(None, [
            f"{len(missing)} página(s) da navegação ausente(s): {', '.join(missing[:5])}" if missing else "",
            f"página(s) proibida(s): {', '.join(blocked[:5])}" if blocked else ""]))
        return Result(url, False, detail, transient=bool(missing) and not blocked)
    return Result(url, True, f"{len(locs)} URLs, todas as {len(expected)} páginas da navegação presentes")


# ------------------------------------------------------------------ execução
class Runner:
    def __init__(self, fetcher: Callable[[str], Response], attempts: int, backoff: float, deadline: float,
                 interval: float, sleep: Callable[[float], None] = time.sleep,
                 clock: Callable[[], float] = time.monotonic) -> None:
        self.fetcher, self.attempts, self.backoff = fetcher, attempts, backoff
        self.interval, self.sleep, self.clock = interval, sleep, clock
        self.end = clock() + deadline
        self.last: dict[str, Response] = {}

    def run(self, url: str, evaluate: Callable[[Response], Result]) -> Result:
        """Avalia ``url`` até passar, falhar de forma definitiva ou esgotar tentativas/prazo.

        Esgotado o prazo total, as verificações restantes não fazem requisição: ficam "não
        confirmadas", e o tempo do job continua limitado por --deadline mais um timeout.
        """
        wait = self.backoff
        for attempt in range(1, self.attempts + 1):
            if self.clock() >= self.end:
                return Result(url, False, "não verificada: prazo total esgotado", transient=True)
            self.sleep(self.interval)
            response = self.fetcher(url)
            self.last[url] = response
            result = evaluate(response)
            if result.ok or not result.transient:
                return result
            if attempt == self.attempts or self.clock() + wait > self.end:
                result.detail += f" (após {attempt} tentativa(s))"
                return result
            print(f"  … {result.name}: {result.detail}; nova tentativa em {wait:.0f}s ({attempt}/{self.attempts})")
            self.sleep(wait)
            wait = min(wait * 2, 60.0)
        raise AssertionError("inalcançável")


def smoke(base: str, exp: dict, runner: Runner, version: str | None) -> list[Result]:
    results: list[Result] = []
    canon = (exp["site_url"] or base).rstrip("/") + "/"

    def record(result: Result) -> None:
        print(f"  [{'OK' if result.ok else 'FALHOU'}] {result.name}: {result.detail}")
        results.append(result)

    print("Páginas principais")
    for doc in exp["core"]:
        url = page_url(base, doc)
        record(runner.run(url, lambda r, u=url, c=page_url(canon, doc): check_page(r, u, c)))
    if version:
        print("Versão publicada")
        record(runner.run(base, lambda r: check_version(r, base, version, canon)))
    print("sitemap.xml")
    expected = {page_url(canon, doc) for doc in exp["nav"]}
    record(runner.run(base + "sitemap.xml",
                      lambda r: check_sitemap(r, base + "sitemap.xml", expected, exp["forbidden"], canon)))
    print("Assets essenciais")
    home = runner.last.get(base)  # obtida (com novas tentativas) na verificação da página inicial
    assets = sorted(set(ASSET_RE.findall(home.body if home else "")) | set(STATIC_ASSETS))
    for asset in assets:
        url = base + asset
        record(runner.run(url, lambda r, u=url: check_asset(r, u)))
    print("Endereços que não podem existir")
    for path in exp["forbidden"]:
        url = base + path
        record(runner.run(url, lambda r, u=url: check_absent(r, u)))
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--base-url", help="endereço do portal (padrão: site_url do zensical.toml)")
    parser.add_argument("--expect-version", help="versão exibida na página inicial (padrão: tag do RELEASE-MANIFEST.yml)")
    parser.add_argument("--attempts", type=int, default=6, help="tentativas por verificação (padrão: 6)")
    parser.add_argument("--backoff", type=float, default=10.0, help="espera inicial entre tentativas, em s (dobra até 60)")
    parser.add_argument("--deadline", type=float, default=600.0, help="prazo total, em s (padrão: 600)")
    parser.add_argument("--timeout", type=float, default=20.0, help="timeout de cada requisição, em s")
    parser.add_argument("--interval", type=float, default=0.3, help="intervalo mínimo entre requisições, em s")
    parser.add_argument("--cache-bust", default=str(int(time.time())),
                        help="valor do parâmetro ?smoke= acrescentado às requisições, para não receber do CDN "
                             "uma versão anterior em cache (padrão: horário atual; vazio desativa)")
    args = parser.parse_args(argv)
    if args.attempts < 1 or args.deadline <= 0 or args.timeout <= 0:
        parser.error("--attempts, --deadline e --timeout precisam ser positivos")
    exp = expectations(args.root.resolve())
    base = (args.base_url or exp["site_url"] or "").rstrip("/") + "/"
    if not base.startswith(("https://", "http://")):
        parser.error("informe --base-url ou site_url no zensical.toml")
    version = args.expect_version or exp["version"]
    print(f"Smoke tests em {base} — {len(exp['core'])} páginas principais, {len(exp['nav'])} na navegação, "
          f"versão esperada: {version or 'não verificada'}")
    def fetcher(url: str) -> Response:
        return fetch(f"{url}?smoke={args.cache_bust}" if args.cache_bust else url, args.timeout)

    runner = Runner(fetcher, args.attempts, args.backoff, args.deadline, args.interval)
    results = smoke(base, exp, runner, version)
    failed = [r for r in results if not r.ok]
    unavailable = [r for r in failed if r.transient]
    print(f"[{'FALHOU' if failed else 'OK'}] Smoke tests — {len(results) - len(failed)}/{len(results)} verificações; "
          f"{len(failed) - len(unavailable)} divergência(s) de conteúdo, {len(unavailable)} sem confirmação "
          "depois das tentativas (indisponibilidade ou propagação)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
