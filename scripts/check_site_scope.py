#!/usr/bin/env python3
"""Verifica que o site compilado (site/) expõe só as páginas da árvore — sem vazamento por URL, busca ou sitemap.

Regras:
  - cada ``index.html`` do site corresponde a uma página Markdown de ``docs/`` (além de ``404.html``);
    não há outro arquivo HTML;
  - cada entrada do índice de busca (``search.json``) e do ``sitemap.xml`` aponta para uma dessas páginas,
    e toda página da árvore está no sitemap e na busca;
  - nenhum endereço proibido existe no site, na busca ou no sitemap: pastas de módulos e complementos
    planejados (fora do escopo) segundo o manifesto e, na árvore pública (com ``RELEASE-MANIFEST.yml``),
    ``internal/`` e ``getting-started/local-development/`` — que no desenvolvimento são o Handbook.

Uso:
    zensical build --clean && python scripts/check_site_scope.py [--site site]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from _common import ROOT, Report, exit_with, load_config, load_manifest

PUBLIC_ONLY_FORBIDDEN = ("internal/", "getting-started/local-development/")
PUBLIC_TREE = (ROOT / "RELEASE-MANIFEST.yml").is_file()


def page_urls(docs: Path) -> set[str]:
    """URLs relativas (diretório) das páginas Markdown: ``a/b.md`` → ``a/b/``; ``a/index.md`` → ``a/``."""
    urls = set()
    for page in docs.rglob("*.md"):
        rel = page.relative_to(docs).as_posix()[:-3]
        urls.add("" if rel == "index" else (rel[: -len("index")] if rel.endswith("/index") else rel + "/"))
    return urls


def forbidden_prefixes(manifest: dict, public: bool = PUBLIC_TREE) -> list[str]:
    prefixes = list(PUBLIC_ONLY_FORBIDDEN) if public else []
    for unit in manifest.get("modules") or []:
        if unit.get("status") == "planned" and unit.get("slug"):
            prefixes.append(f"modules/{str(unit['id'])[1:]}-{unit['slug']}/")
    for unit in manifest.get("complements") or []:
        if unit.get("status") == "planned" and unit.get("slug"):
            prefixes.append(f"complements/{unit['slug']}/")
    return prefixes


def check(site: Path, docs: Path, manifest: dict, site_url: str, public: bool = PUBLIC_TREE) -> Report:
    report = Report("Escopo do site compilado (páginas, busca e sitemap)")
    pages = page_urls(docs)
    forbidden = forbidden_prefixes(manifest, public)
    blocked = [p for p in pages if p.startswith(tuple(forbidden))]
    for url in sorted(blocked):
        report.error(f"página fora do escopo na árvore: docs/{url}")

    built = set()
    for html in site.rglob("*.html"):
        rel = html.relative_to(site).as_posix()
        if rel == "404.html":
            continue
        if not rel.endswith("index.html"):
            report.error(f"HTML sem página de origem: {rel}")
            continue
        built.add(rel[: -len("index.html")])
    for url in sorted(built - pages):
        report.error(f"página compilada sem Markdown na árvore: {url or '/'}")
    for url in sorted(pages - built):
        report.error(f"página da árvore não compilada: {url or '/'}")
    for url in sorted(u for u in built if u.startswith(tuple(forbidden))):
        report.error(f"endereço proibido acessível no site: {url}")

    search = site / "search.json"
    if search.is_file():
        items = json.loads(search.read_text(encoding="utf-8")).get("items") or []
        found = {str(i.get("location", "")).split("#", 1)[0] for i in items}
        for url in sorted(found - pages):
            report.error(f"índice de busca aponta para página inexistente ou excluída: {url or '/'}")
        for url in sorted(pages - found):
            report.error(f"página ausente do índice de busca: {url or '/'}")
    else:
        report.error("search.json ausente no site compilado")

    sitemap = site / "sitemap.xml"
    if sitemap.is_file():
        locs = re.findall(r"<loc>(.*?)</loc>", sitemap.read_text(encoding="utf-8"))
        urls = set()
        for loc in locs:
            if not loc.startswith(site_url):
                report.error(f"sitemap com URL fora do site: {loc}")
                continue
            urls.add(loc[len(site_url):])
        for url in sorted(urls - pages):
            report.error(f"sitemap aponta para página inexistente ou excluída: {url or '/'}")
        for url in sorted(pages - urls):
            report.error(f"página ausente do sitemap: {url or '/'}")
    else:
        report.error("sitemap.xml ausente no site compilado")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--site", type=Path, default=ROOT / "site")
    args = parser.parse_args()
    config = load_config()
    site_url = str(config.get("project", {}).get("site_url", "")).rstrip("/") + "/"
    report = check(args.site, ROOT / "docs", load_manifest(), site_url)
    print(f"{len(page_urls(ROOT / 'docs'))} páginas; {len(forbidden_prefixes(load_manifest()))} prefixos proibidos verificados")
    exit_with(report)


if __name__ == "__main__":
    main()
