#!/usr/bin/env python3
"""Verifica links e recursos internos do site gerado (site/).

Analisa todo HTML produzido pelo build e confirma que cada href/src interno
aponta para um arquivo existente e, quando houver âncora (#id), que o id
exista na página de destino. Links externos são verificados separadamente
pelo workflow agendado (lychee), para não bloquear PRs por indisponibilidades
de terceiros.

Uso:
    zensical build --clean && python scripts/check_links.py [--site site]
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from _common import ROOT, Report, exit_with, load_config

SKIP_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class Collector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.refs: list[tuple[str, str]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        for attr in ("href", "src"):
            value = a.get(attr)
            if value and tag in {"a", "img", "script", "link", "source", "iframe"}:
                self.refs.append((tag, value))
        if tag == "source" and a.get("srcset"):
            self.refs.append((tag, a["srcset"].split()[0]))


@lru_cache(maxsize=None)
def parse(path: Path) -> Collector:
    c = Collector()
    c.feed(path.read_text(encoding="utf-8", errors="replace"))
    return c


def base_path() -> str:
    """Prefixo de caminho do site publicado (ex.: /security-architecture-academy/)."""
    site_url = load_config().get("project", {}).get("site_url", "/")
    path = urlsplit(site_url).path or "/"
    return path if path.endswith("/") else path + "/"


BASE = base_path()


def resolve(site: Path, page: Path, url: str) -> Path | None:
    parts = urlsplit(url)
    target = unquote(parts.path)
    if not target:
        return page
    if target.startswith("/"):
        # URLs absolutas (ex.: 404.html) incluem o caminho base do GitHub Pages
        if not target.startswith(BASE):
            return None
        target = "/" + target[len(BASE):]
    base = site if target.startswith("/") else page.parent
    candidate = (base / target.lstrip("/")).resolve()
    if candidate.is_dir():
        candidate = candidate / "index.html"
    return candidate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default=str(ROOT / "site"), help="diretório do build")
    args = parser.parse_args()
    site = Path(args.site).resolve()
    report = Report("Links internos do site")
    if not (site / "index.html").is_file():
        report.error(f"build não encontrado em {site} — execute `make build` antes")
        exit_with(report)

    pages = sorted(site.rglob("*.html"))
    checked = 0
    for page in pages:
        for tag, url in parse(page).refs:
            parts = urlsplit(url)
            if parts.scheme in SKIP_SCHEMES or url.startswith("//"):
                continue
            checked += 1
            target = resolve(site, page, url)
            rel_page = page.relative_to(site)
            if target is None or not target.exists():
                report.error(f"{rel_page}: <{tag}> aponta para recurso inexistente: {url}")
                continue
            if site not in target.parents and target != site:
                report.error(f"{rel_page}: link sai do diretório do site: {url}")
                continue
            if parts.fragment and target.suffix == ".html":
                if unquote(parts.fragment) not in parse(target).ids:
                    report.error(f"{rel_page}: âncora inexistente: {url}")
    print(f"  {len(pages)} páginas, {checked} referências internas verificadas")
    exit_with(report)


if __name__ == "__main__":
    main()
