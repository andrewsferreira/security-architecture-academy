#!/usr/bin/env python3
"""Verifica a estrutura do repositório, o front matter das páginas e a navegação.

Uso:
    python scripts/check_structure.py            # validação de Pull Request
    python scripts/check_structure.py --release  # validação de publicação (main)

Regras de status das páginas:
    draft      — nunca na navegação.
    in-review  — permitido em branches (inclusive na navegação, para revisão);
                 bloqueado em --release.
    published / sem status — páginas públicas; precisam estar na navegação.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from _common import DOCS, ROOT, Report, exit_with, load_config, nav_files, read_front_matter
from export_release import is_public, load_allowlist

# Na árvore pública (com RELEASE-MANIFEST.yml na raiz) não se exigem os arquivos que a allowlist
# mantém só no desenvolvimento (Handbook, templates de autoria, padrões internos, Dependabot).
PUBLIC_TREE = (ROOT / "RELEASE-MANIFEST.yml").is_file()

REQUIRED_FILES = [
    "README.md", "GETTING-STARTED.md", "CURRICULUM.md", "CHANGELOG.md", "ROADMAP.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
    "PROJECT-STANDARDS.md", "LICENSING.md", "LICENSE", "LICENSE-CODE", ".editorconfig", ".gitignore", ".gitattributes", "requirements.txt",
    "zensical.toml", "Makefile", "curriculum/manifest.yml", "research/bibliography.yml", "research/knowledge-map.yml",
    "private-research/README.md", "includes/abbreviations.md", "authoring/technical-lesson.md",
    "docs/index.md", "docs/internal/design-system.md", "docs/internal/style-guide.md",
    "docs/assets/stylesheets/extra.css", ".github/PULL_REQUEST_TEMPLATE.md", ".github/dependabot.yml",
    ".github/workflows/ci.yml", ".github/workflows/pages.yml",
]
TEMPLATE_FIELDS = ("id", "title", "description", "domain", "tier", "status", "prerequisites", "objectives",
                   "last_updated", "reviewed_by")
TEMPLATE_SECTIONS = ("Resumo", "Referências", "Revisão")
DRAFT_STATUSES = {"draft", "in-review"}
LINK_RE = re.compile(r'(?:\]\(|src=")([^)"#\s]+)')
MERMAID_SOURCE_RE = re.compile(r"<!--\s*source:\s*(\S+)\s*-->\s*```mermaid\n(.*?)```", re.DOTALL)


def check(release: bool) -> Report:
    report = Report("Estrutura do repositório" + (" (release)" if release else ""))

    allow = load_allowlist(ROOT) if PUBLIC_TREE else None
    for rel in REQUIRED_FILES:
        if allow and not is_public(rel, allow):
            if (ROOT / rel).exists():
                report.error(f"{rel}: arquivo exclusivo do desenvolvimento presente na árvore pública")
            continue
        if not (ROOT / rel).is_file():
            report.error(f"arquivo obrigatório ausente: {rel}")

    # O Zensical ignora silenciosamente docs/templates/ (nome reservado do tema).
    if (ROOT / "docs" / "templates").exists():
        report.error("docs/templates/ é ignorado pelo Zensical — use docs/artifacts/ para modelos do estudante")

    # --- Navegação ---------------------------------------------------------
    nav = nav_files(load_config())
    for rel in sorted(nav):
        if not (DOCS / rel).is_file():
            report.error(f"nav aponta para arquivo inexistente: docs/{rel}")

    # --- Páginas -----------------------------------------------------------
    for page in sorted(DOCS.rglob("*.md")):
        rel = page.relative_to(DOCS).as_posix()
        try:
            meta, body = read_front_matter(page)
        except Exception as exc:  # noqa: BLE001 — reportar YAML inválido
            report.error(f"docs/{rel}: front matter inválido ({exc})")
            continue
        if not body.strip():
            report.error(f"docs/{rel}: página vazia")
        if not meta.get("description"):
            report.error(f"docs/{rel}: front matter sem 'description' (usada em SEO e compartilhamento)")
        status = meta.get("status")
        if status == "draft" and rel in nav:
            report.error(f"docs/{rel}: status 'draft' não pode estar na navegação")
        elif status in DRAFT_STATUSES:
            if release:
                report.error(f"docs/{rel}: status '{status}' não pode ser publicado em main")
            else:
                report.warn(f"docs/{rel}: '{status}' — bloqueado na publicação até a aprovação")
        elif rel not in nav:
            report.error(f"docs/{rel}: página pública fora da navegação — adicione em nav ou marque como draft")

    # --- Templates educacionais ------------------------------------------
    templates = sorted((ROOT / "authoring").glob("*.md"))
    if not templates and not (allow and not is_public("authoring/technical-lesson.md", allow)):
        report.error("nenhum template encontrado em authoring/")
    for tpl in templates:
        if tpl.name == "README.md":
            continue
        meta, body = read_front_matter(tpl)
        for field in TEMPLATE_FIELDS:
            if field not in meta:
                report.error(f"authoring/{tpl.name}: campo de front matter ausente: {field}")
        if meta.get("status") != "draft":
            report.error(f"authoring/{tpl.name}: templates devem iniciar com status: draft")
        for section in TEMPLATE_SECTIONS:
            if not re.search(rf"^## .*{section}", body, re.MULTILINE):
                report.error(f"authoring/{tpl.name}: seção obrigatória ausente: {section}")

    # --- YAML do GitHub (issue forms, workflows, Dependabot) -----------
    import yaml  # noqa: PLC0415 — dependência já exigida por _common

    for yml in sorted((ROOT / ".github").rglob("*.yml")):
        try:
            yaml.safe_load(yml.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            report.error(f"{yml.relative_to(ROOT)}: YAML inválido ({exc.__class__.__name__})")

    # --- Arquivos da raiz: links locais e diagramas sincronizados -------
    # Relatórios de processo (PROGRESS, RELEASE-PLAN…) existem só no repositório de desenvolvimento;
    # os ausentes são ignorados.
    for name in ("README.md", "GETTING-STARTED.md", "CURRICULUM.md", "ROADMAP.md", "LICENSING.md", "PROJECT-STANDARDS.md",
                 "CONTRIBUTING.md", "SECURITY.md", "CODE_OF_CONDUCT.md",
                 "CHANGELOG.md", "PROGRESS.md", "RELEASE-PLAN.md", "FINAL-CONSOLIDATION-REPORT.md",
                 "PUBLICATION-READINESS-CHECKLIST.md", "ACADEMIC-COMPLETENESS-REPORT.md",
                 "FUNDAMENTALS-PUBLICATION-READINESS.md", "research/README.md"):
        path = ROOT / name
        if not path.is_file():
            continue
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (path.parent / target).exists():
                report.error(f"{name}: referência local inexistente: {target}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for source, block in MERMAID_SOURCE_RE.findall(readme):
        src = ROOT / source
        if not src.is_file():
            report.error(f"README.md: fonte de diagrama inexistente: {source}")
        elif src.read_text(encoding="utf-8").strip() != block.strip():
            report.error(f"README.md: diagrama divergente da fonte {source} — copie o conteúdo atualizado")

    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", action="store_true", help="regras de publicação (bloqueia rascunhos)")
    exit_with(check(parser.parse_args().release))


if __name__ == "__main__":
    main()
