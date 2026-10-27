"""Testes do validador da Research Library."""

from __future__ import annotations


import pytest

from validate_references import (BIBLIOGRAPHY, KNOWLEDGE_MAP, coverage, load_yaml, module_ids, note_citations,
                                 page_citations, render_report, tracked_files, validate)
from _common import load_manifest

MODULES = [f"M{i:02d}" for i in range(18)]


def ref(**over):
    base = {"id": "TEST-REF", "title": "Título", "publisher": "Instituição", "year": 2024, "url": "https://example.com/doc",
            "type": "Documentation", "language": "en", "category": "governance-risk", "availability": "Free Online Reading",
            "redistribution": "Not Verified", "verification": "Verified", "verified_on": "2026-10-23", "modules": ["M02"],
            "reading_role": "reference", "priority": 3, "notes": ""}
    base.update(over)
    return base


def bib(*refs):
    return {"categories": {"governance-risk": "Governance & Risk"}, "references": list(refs)}


def run(b, kmap=None, pages=None, notes=None, tracked=None):
    return validate(b, kmap or {"concepts": []}, MODULES, pages or {}, notes or {}, tracked if tracked is not None else [])


def test_repository_library_is_valid():
    report = validate(load_yaml(BIBLIOGRAPHY), load_yaml(KNOWLEDGE_MAP), module_ids(), page_citations(),
                      note_citations(), tracked_files())
    assert report.errors == []


def test_minimal_reference_passes():
    assert run(bib(ref())).errors == []


@pytest.mark.parametrize("field,value,fragment", [
    ("availability", "Free", "availability inválido"),
    ("redistribution", "Yes", "redistribution inválido"),
    ("verification", "OK", "verification inválido"),
    ("verified_on", "23/10/2026", "verified_on"),
    ("url", "http://example.com", "https://"),
    ("id", "lower-case", "ID fora do padrão"),
    ("modules", ["M99"], "módulo inexistente"),
    ("priority", 5, "priority"),
])
def test_invalid_fields_are_rejected(field, value, fragment):
    errors = run(bib(ref(**{field: value}))).errors
    assert any(fragment in e for e in errors), errors


def test_duplicate_ids_are_rejected():
    assert any("duplicado" in e for e in run(bib(ref(), ref())).errors)


def test_lesson_cannot_be_based_on_pending_source():
    pages = {"docs/modules/02-x/01-a.md": {"sources": ["TEST-REF"], "further_reading": []}}
    errors = run(bib(ref(verification="Pending")), pages=pages).errors
    assert any("não verificada" in e for e in errors)


def test_further_reading_may_point_to_pending_but_must_exist():
    pages = {"docs/modules/02-x/01-a.md": {"sources": [], "further_reading": ["TEST-REF", "MISSING-REF"]}}
    errors = run(bib(ref(verification="Pending")), pages=pages).errors
    assert errors == ["docs/modules/02-x/01-a.md: further_reading cita referência inexistente: MISSING-REF"]


def test_consulted_concept_requires_consulted_chapter():
    chapters = [{"locator": "Cap. 3", "title": "X", "consulted": False}]
    kmap = {"concepts": [{"concept": "C", "ref": "TEST-REF", "locator": "Cap. 3, §3.1", "consulted": True, "modules": ["M02"],
                          "tier": "fundamental", "application": "a", "limitations": "l"}]}
    errors = run(bib(ref(chapters=chapters)), kmap=kmap).errors
    assert any("não está consultado" in e for e in errors)
    chapters[0]["consulted"] = True
    assert run(bib(ref(chapters=chapters)), kmap=kmap).errors == []


def test_pages_require_page_basis():
    chapters = [{"locator": "Cap. 1", "title": "X", "consulted": False, "pages": "10"}]
    assert any("page_basis" in e for e in run(bib(ref(chapters=chapters))).errors)


@pytest.mark.parametrize("path", ["private-research/book.pdf", "docs/assets/book.PDF", "research/notes/livro.epub"])
def test_private_files_cannot_be_tracked(path):
    assert any("versionado" in e for e in run(bib(ref()), tracked=[path]).errors)


def test_private_research_readme_is_allowed():
    assert run(bib(ref()), tracked=["private-research/README.md"]).errors == []


def test_unused_reference_and_uncovered_modules_are_warnings():
    report = run(bib(ref()))
    assert any("não utilizada" in w for w in report.warnings)
    assert any(w.startswith("M00:") for w in report.warnings)


def test_coverage_report_lists_every_module():
    manifest = load_manifest()
    cov = coverage(load_yaml(BIBLIOGRAPHY), load_yaml(KNOWLEDGE_MAP), manifest, page_citations())
    text = render_report(cov, load_yaml(BIBLIOGRAPHY)["categories"])
    for mod in manifest["modules"]:
        assert f"| {mod['id']} — " in text
    m02 = next(r for r in cov["modules"] if r["id"] == "M02")
    assert m02["verified"] >= 3 and m02["cited"]
