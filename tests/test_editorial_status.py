"""Coerência entre o estado real das releases e o que as páginas públicas dizem sobre ele."""

from __future__ import annotations

import re

import pytest

import render_curriculum as rc
from _common import DOCS, ROOT, load_manifest

MANIFEST = load_manifest()
MODULES = {m["id"]: m for m in MANIFEST["modules"]}
R1 = next(r for r in MANIFEST["releases"] if r["id"] == "R1")
R1_PUBLISHED = all(MODULES[m]["status"] == "published" for m in R1["modules"])

# Frases que contradizem uma Release 1 publicada (encontradas na v0.1.0 e corrigidas na v0.1.1).
STALE = [
    r"n[ãa]o estiverem publicados",
    r"Nenhum n[íi]vel est[áa] publicado",
    r"aguardando a revis[ãa]o do mantenedor para publica[çc][ãa]o",
    r"primeiro conjunto de conte[úu]do [ée] o \*\*M[óo]dulo 0?2",
    r"dispon[íi]vel para revis[ãa]o o material",
    r"As aulas do \*\*M02\*\* est[ãa]o produzidas",
]


def student_pages():
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if not rel.startswith(("docs/internal/", "docs/resources/")):
            yield path
    for name in ("README.md", "GETTING-STARTED.md", "ROADMAP.md"):
        yield ROOT / name


@pytest.mark.skipif(not R1_PUBLISHED, reason="Release 1 ainda não publicada")
def test_no_stale_unpublished_statements():
    found = []
    for path in student_pages():
        text = path.read_text(encoding="utf-8")
        for pattern in STALE:
            if re.search(pattern, text):
                found.append(f"{path.relative_to(ROOT)}: {pattern}")
    assert not found, "\n".join(found)


@pytest.mark.skipif(not R1_PUBLISHED, reason="Release 1 ainda não publicada")
def test_roadmap_shows_release_1_published():
    text = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    section = text.split("## Release 1", 1)[1].split("\n## ", 1)[0]
    assert "Published" in section and "publicada" in section
    assert "em revisão" not in section and "aguardando" not in section
    assert "## Release 2 — Professional 🔄" in text and "## Release 3 — Architect ⏳" in text


@pytest.mark.skipif(not R1_PUBLISHED, reason="Release 1 ainda não publicada")
def test_getting_started_starts_at_initial_module():
    text = (DOCS / "getting-started" / "index.md").read_text(encoding="utf-8")
    available = text.split("## O que está disponível", 1)[1].split("\n## ", 1)[0]
    first = re.search(r"\]\(\.\./modules/([\w-]+)/index\.md\)", available).group(1)
    assert first == "00-foundations"
    assert "Release 1 — Fundamentals" in available


def test_homepage_availability_follows_manifest():
    block = rc.render_release_status(MANIFEST)
    if R1_PUBLISHED:
        assert '!!! success "Disponível agora"' in block and "Nenhum nível está publicado" not in block
    else:
        assert "Nenhum nível está publicado" in block


def test_status_legend_keeps_definitions():
    """A legenda descreve cada status; não é o estado de um item e não pode ser reescrita."""
    text = (DOCS / "curriculum" / "index.md").read_text(encoding="utf-8")
    for status, label in (("in-review", "In Review"), ("published", "Published"), ("draft", "Draft")):
        assert f'| <span class="saa-status saa-status--{status}">{label}</span> |' in text


@pytest.mark.skipif(not (ROOT / "authoring").is_dir(), reason="templates de autoria só no desenvolvimento")
def test_lesson_templates_start_at_l01():
    for name in ("technical-lesson.md", "concept-explanation.md"):
        text = (ROOT / "authoring" / name).read_text(encoding="utf-8")
        assert re.search(r"^id: M\d{2}-L01$", text, re.M), name
        assert not re.search(r"M\d{2}-L00", text), name
