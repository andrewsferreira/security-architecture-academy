"""Links das configurações do GitHub e dos documentos públicos apontam para conteúdo publicado.

Regressão da v0.2.0: o contato "Guia editorial e modelo de conteúdo" das issues apontava para
``/internal/`` no portal — o Handbook, retirado da árvore pública na v0.1.1.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

import export_release as ex
from _common import ROOT, load_config

SITE = "https://andrewsferreira.github.io/security-architecture-academy/"
REPO = "https://github.com/andrewsferreira/security-architecture-academy/"
URL_RE = re.compile(r"https?://[^\s)\"'<>`\]]+")
ALLOW = ex.load_allowlist(ROOT)

# Arquivos que o estudante ou o colaborador vê no GitHub, fora do portal.
GITHUB_FILES = sorted(p for p in (ROOT / ".github").rglob("*") if p.is_file() and ex.is_public(
    p.relative_to(ROOT).as_posix(), ALLOW))
ROOT_DOCS = sorted(ROOT / f for f in ALLOW["files"] if f.endswith(".md") and (ROOT / f).is_file())


def site_page(url: str) -> str | None:
    """Arquivo em docs/ que gera a URL do portal (None se nenhum)."""
    path = url[len(SITE):].split("#", 1)[0].split("?", 1)[0]
    if path in {"", "sitemap.xml"} or path.startswith("assets/"):
        return "docs/index.md" if path == "" else path
    candidates = [f"docs/{path}index.md", f"docs/{path.rstrip('/')}.md"] if path.endswith("/") else [f"docs/{path}"]
    return next((c for c in candidates if (ROOT / c).is_file()), candidates[0])


def links(paths: list[Path]) -> list[tuple[str, str]]:
    found = []
    for path in paths:
        for url in URL_RE.findall(path.read_text(encoding="utf-8")):
            found.append((path.relative_to(ROOT).as_posix(), url.rstrip(".,;")))
    return found


@pytest.mark.parametrize("source, url", links(GITHUB_FILES + ROOT_DOCS))
def test_site_and_repository_links_point_to_public_content(source, url):
    if url.startswith(SITE):
        page = site_page(url)
        assert ex.is_public(page, ALLOW), f"{source}: {url} aponta para conteúdo retirado da árvore pública"
        assert (ROOT / page).exists() or page == "sitemap.xml", f"{source}: {url} sem página correspondente"
    elif url.startswith(REPO + "blob/main/") or url.startswith(REPO + "tree/main/"):
        rel = url.split("/main/", 1)[1].split("#", 1)[0]
        assert ex.is_public(rel, ALLOW) or any(rel.rstrip("/") + "/" == d for d in ALLOW["directories"]), (
            f"{source}: {url} aponta para arquivo que não vai ao repositório público")
        assert (ROOT / rel).exists(), f"{source}: {url} aponta para arquivo inexistente"
    assert "security-architecture-academy-dev" not in url, f"{source}: link para o repositório privado"


def test_issue_contacts_keep_private_vulnerability_report_and_contribution_guide():
    text = (ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml").read_text(encoding="utf-8")
    assert REPO + "security/advisories/new" in text
    assert REPO + "blob/main/CONTRIBUTING.md" in text
    assert "/internal/" not in text and "Handbook" not in text


def test_github_files_do_not_reference_internal_material():
    for path in GITHUB_FILES:
        text = path.read_text(encoding="utf-8")
        for term in ("docs/internal/", "Guia editorial", "Handbook", "authoring/", "PROJECT-STANDARDS"):
            assert term not in text, f"{path.relative_to(ROOT)} cita material interno: {term}"


def test_portal_offers_view_source_without_direct_edit():
    """O repositório público recebe só árvores exportadas: editar nele não chega ao portal."""
    features = load_config()["project"]["theme"]["features"]
    assert "content.action.edit" not in features
    assert "content.action.view" in features


def test_notification_instructions_match_available_features():
    text = (ROOT / "docs" / "getting-started" / "index.md").read_text(encoding="utf-8")
    assert "Watch → Custom → Releases" not in text  # o repositório público ainda não tem GitHub Releases
    assert "commits/main.atom" in text
