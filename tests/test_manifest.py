"""Testes do validador do curriculum manifest (schema v2) e dos geradores de páginas."""

from __future__ import annotations

import copy
import datetime as dt
from pathlib import Path

import pytest
import yaml

from _common import ROOT, load_config, load_manifest, nav_files
from render_curriculum import render_activities, render_curriculum, render_dependencies, render_sources, splice
from validate_manifest import validate

M02_DIR = "modules/02-security-architecture"


@pytest.fixture()
def manifest() -> dict:
    return load_manifest()


def minimal(manifest: dict) -> dict:
    """Manifesto com todos os itens em 'planned', independente dos arquivos do repositório."""
    data = copy.deepcopy(manifest)
    for key in ("modules", "complements"):
        for unit in data[key]:
            unit["status"] = "planned"
            unit.pop("path", None)
            for field in ("reviewed_by", "published_on"):
                unit.pop(field, None)
            for lesson in unit["lessons"]:
                lesson["status"] = "planned"
                for field in ("file", "reviewed_by", "published_on"):
                    lesson.pop(field, None)
    for key in ("case_studies", "labs", "assessments", "artifacts"):
        for item in data[key]:
            item["status"] = "planned"
            item.pop("path", None)
            item.pop("answers", None)
            item.pop("tested", None)
            item.pop("reviewed_by", None)
            item.pop("published_on", None)
    # Releases já aprovadas ou publicadas voltam a 'in-review': os itens acima deixaram de estar publicados.
    for rel in data.get("releases") or []:
        if rel.get("status") in {"approved", "published"}:
            rel.update(status="in-review", approved_by=[], approved_on=None, approved_source_commit=None,
                       public_commit=None, published_on=None, url=None)
            rel.pop("patches", None)
    return data


def write_page(root: Path, rel: str, ident: str, status: str, body: str = "Conteúdo revisado.\n", lesson=False) -> None:
    page = root / "docs" / rel
    page.parent.mkdir(parents=True, exist_ok=True)
    extra = "tier: fundamental\nprerequisites: []\nobjectives: [x]\n" if lesson else ""
    page.write_text(
        f"---\nid: {ident}\ntitle: Teste\ndescription: Página de teste.\nstatus: {status}\n"
        f"last_updated: 2026-10-23\n{extra}---\n\n# Teste\n\n{body}",
        encoding="utf-8",
    )


def activate_m02(data: dict, root: Path, status: str, lesson_status: str | None = None) -> dict:
    mod = data["modules"][2]
    mod["status"] = status
    mod["path"] = f"{M02_DIR}/index.md"
    write_page(root, mod["path"], "M02", status)
    for n, lesson in enumerate(mod["lessons"], start=1):
        lesson["status"] = lesson_status or status
        lesson["file"] = f"{n:02d}-aula.md"
        write_page(root, f"{M02_DIR}/{lesson['file']}", lesson["id"], lesson["status"], lesson=True)
    return mod


# ------------------------------------------------------------- repositório
def test_repository_manifest_is_valid(manifest):
    report = validate(manifest, ROOT, nav_files(load_config()))
    assert report.errors == []


def test_release_blocks_items_in_review(manifest, tmp_path):
    # Independente do estado do repositório: um módulo em revisão, mesmo na navegação,
    # bloqueia a validação de publicação (--release).
    data = minimal(manifest)
    mod = activate_m02(data, tmp_path, "in-review")
    nav = {mod["path"]} | {f"{M02_DIR}/{lesson['file']}" for lesson in mod["lessons"]}
    assert validate(data, tmp_path, nav).errors == []
    errors = validate(data, tmp_path, nav, release=True).errors
    assert errors, "itens em revisão devem bloquear a publicação"
    assert all("não pode ser publicado" in e for e in errors)


def test_curriculum_shape(manifest):
    ids = [m["id"] for m in manifest["modules"]]
    assert ids == [f"M{i:02d}" for i in range(18)]
    assert sum(len(m["lessons"]) for m in manifest["modules"]) >= 130
    assert [s["id"] for s in manifest["stages"]] == ["n0", "n1", "n2", "n3", "n4", "n5"]
    assert {t["id"] for t in manifest["tracks"]} == {"fundamentals", "professional", "advanced"}
    assert len(manifest["artifacts"]) == 13
    assert {c["id"] for c in manifest["case_studies"]} == {"CS-A", "CS-B", "CS-C", "CS-D", "CS-E"}


# ------------------------------------------------------------- regras
def test_minimal_manifest_is_valid(manifest, tmp_path):
    assert validate(minimal(manifest), tmp_path).errors == []


def test_non_sequential_module_ids(manifest, tmp_path):
    data = minimal(manifest)
    data["modules"][1]["id"] = "M05"
    errors = validate(data, tmp_path).errors
    assert any("sequenciais" in e for e in errors)


def test_unknown_stage_domain_and_tier(manifest, tmp_path):
    data = minimal(manifest)
    data["modules"][0]["stage"] = "n9"
    data["modules"][0]["domains"] = ["quantum"]
    data["modules"][0]["lessons"][0]["tier"] = "guru"
    errors = validate(data, tmp_path).errors
    assert any("stage desconhecido" in e for e in errors)
    assert any("domínio desconhecido" in e for e in errors)
    assert any("tier desconhecido" in e for e in errors)


def test_planned_item_cannot_have_path(manifest, tmp_path):
    data = minimal(manifest)
    data["modules"][2]["path"] = f"{M02_DIR}/index.md"
    assert any("não pode ter path" in e for e in validate(data, tmp_path).errors)


def test_prerequisite_cycle_is_detected(manifest, tmp_path):
    data = minimal(manifest)
    data["modules"][0]["prerequisites"] = ["M17"]
    assert any("circular" in e for e in validate(data, tmp_path).errors)


def test_in_review_module_requires_complete_lessons(manifest, tmp_path):
    data = minimal(manifest)
    activate_m02(data, tmp_path, "in-review")
    data["modules"][2]["lessons"][7]["status"] = "planned"
    data["modules"][2]["lessons"][7].pop("file")
    errors = validate(data, tmp_path).errors
    assert any("não pode ter aula 'planned'" in e for e in errors)


def test_in_review_module_is_valid_in_branch(manifest, tmp_path):
    data = minimal(manifest)
    activate_m02(data, tmp_path, "in-review")
    assert validate(data, tmp_path).errors == []


def test_draft_cannot_be_in_nav(manifest, tmp_path):
    data = minimal(manifest)
    mod = activate_m02(data, tmp_path, "draft")
    errors = validate(data, tmp_path, {mod["path"]}).errors
    assert any("'draft' não pode estar na navegação" in e for e in errors)


def test_status_mismatch_between_page_and_manifest(manifest, tmp_path):
    data = minimal(manifest)
    mod = activate_m02(data, tmp_path, "in-review")
    write_page(tmp_path, mod["path"], "M02", "draft")
    assert any("difere do manifesto" in e for e in validate(data, tmp_path).errors)


def test_published_requires_nav_review_and_no_placeholders(manifest, tmp_path):
    data = minimal(manifest)
    mod = activate_m02(data, tmp_path, "published")
    write_page(tmp_path, mod["path"], "M02", "published", body="Texto com {{ placeholder }}.\n")
    errors = validate(data, tmp_path).errors
    assert any("precisa estar em nav" in e for e in errors)
    assert any("reviewed_by" in e for e in errors)
    assert any("published_on" in e for e in errors)
    assert any("marcadores de rascunho" in e for e in errors)

    write_page(tmp_path, mod["path"], "M02", "published")
    nav = {mod["path"]} | {f"{M02_DIR}/{lesson['file']}" for lesson in mod["lessons"]}
    for item in [mod, *mod["lessons"]]:
        item.update(reviewed_by=["revisor"], published_on=dt.date(2026, 11, 1))
    assert validate(data, tmp_path, nav).errors == []


def test_assessment_requires_separate_answers(manifest, tmp_path):
    data = minimal(manifest)
    item = data["assessments"][0]
    item.update(status="in-review", path="assessments/x.md")
    page = tmp_path / "docs" / "assessments" / "x.md"
    page.parent.mkdir(parents=True)
    page.write_text("---\nid: AS-DIAG\ntitle: T\ndescription: D\nstatus: in-review\n---\n\nTexto\n", encoding="utf-8")
    assert any("gabarito separado" in e for e in validate(data, tmp_path).errors)


# ------------------------------------------------------------- geradores
def test_render_curriculum_lists_every_module_and_lesson(manifest):
    output = render_curriculum(manifest)
    for mod in manifest["modules"]:
        assert f"`{mod['id']}`" in output
        for lesson in mod["lessons"]:
            assert f"`{lesson['id']}`" in output


def test_render_links_only_non_planned(manifest):
    output = render_curriculum(manifest)
    assert f"](../{M02_DIR}/index.md)" in output
    for mod in manifest["modules"]:
        folder = f"modules/{mod['id'][1:]}-{mod['slug']}/"
        if mod["status"] == "planned":
            assert f"](../{folder}" not in output, f"{mod['id']} planejado não deveria ter link"
        else:
            assert f"](../{folder}index.md)" in output


def test_dependencies_graph_has_every_edge(manifest):
    output = render_dependencies(manifest)
    assert "accTitle" in output and "accDescr" in output
    for mod in manifest["modules"]:
        for dep in mod["prerequisites"]:
            assert f"{dep} --> {mod['id']}" in output


def test_render_activities_and_sources():
    manifest = load_manifest()
    assert "CS-A" in render_activities(manifest)
    bib = yaml.safe_load((ROOT / "research" / "bibliography.yml").read_text(encoding="utf-8"))
    output = render_sources(bib)
    assert "Pendente" in output and "Proibida" in output
    for ref in bib["references"]:
        assert ref["url"] in output


def test_splice_replaces_only_marked_block():
    page = "antes\n<!-- x:start -->\nvelho\n<!-- x:end -->\ndepois\n"
    result = splice(page, "x", "novo")
    assert result.startswith("antes\n") and result.endswith("depois\n")
    assert "novo" in result and "velho" not in result
