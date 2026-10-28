"""Publicação progressiva por nível: R1 (Fundamentals Base), R2 (conclusão do Nível 1) e R3–R6 (Níveis 2 a 5)."""

from __future__ import annotations

import copy

import pytest

import export_release as ex
from _common import load_manifest
from validate_manifest import validate


@pytest.fixture()
def manifest() -> dict:
    return load_manifest()


def stage_modules(manifest: dict, stage: str) -> set[str]:
    return {m["id"] for m in manifest["modules"] if m["stage"] == stage}


def release_errors(data: dict, tmp_path) -> list[str]:
    return [e for e in validate(data, tmp_path).errors if e.startswith("release")]


def test_release_ids_and_versions(manifest):
    releases = manifest["releases"]
    assert [r["id"] for r in releases] == ["R1", "R2", "R3", "R4", "R5", "R6"]
    assert [r["version"] for r in releases] == ["0.1.0", "0.2.0", "0.3.0", "0.4.0", "0.5.0", "0.6.0"]


def test_r1_history_is_preserved(manifest):
    r1 = manifest["releases"][0]
    assert r1["status"] == "published" and r1["modules"] == ["M00", "M01", "M02"]
    assert r1["approved_source_commit"] == "94c6cb4d67519737760ba63912a921cb6681e8bb"
    assert r1["public_commit"] == "7bc0237e90c4a0e742fdb0429864765491cb9511"
    assert [p["version"] for p in r1["patches"]] == ["0.1.1"]
    assert r1["patches"][0]["public_commit"] == "bfd4eb3aa99d2ec94fedeaf664af9516493a6c9b"


def test_r2_completes_levels_0_and_1(manifest):
    r2 = next(r for r in manifest["releases"] if r["id"] == "R2")
    assert r2["modules"] == ["M03", "M04"]
    assert "AS-N1" in r2["assessments"] and "AS-MID" not in r2["assessments"]
    scope = ex.cumulative_scope(manifest, "R2")
    assert scope["modules"] == stage_modules(manifest, "n0") | stage_modules(manifest, "n1")
    lessons = {m["id"]: len(m["lessons"]) for m in manifest["modules"]}
    assert sum(lessons[i] for i in stage_modules(manifest, "n0")) == 14
    assert sum(lessons[i] for i in stage_modules(manifest, "n1")) == 23
    assert sum(lessons[i] for i in scope["modules"]) == 37


@pytest.mark.parametrize("rid,stage", [("R3", "n2"), ("R4", "n3"), ("R5", "n4"), ("R6", "n5")])
def test_future_releases_publish_one_level_each(manifest, rid, stage):
    rel = next(r for r in manifest["releases"] if r["id"] == rid)
    assert set(rel["modules"]) == stage_modules(manifest, stage)
    assert rel["status"] in {"planned", "in-development"}
    assert not rel.get("approved_by") and not rel.get("published_on") and not rel.get("public_commit")


def test_released_assessments_exist_only_once(manifest):
    owners = [r["id"] for r in manifest["releases"] for a in r.get("assessments") or [] if a == "AS-FUND"]
    assert owners == ["R1"], "AS-FUND continua na R1; a avaliação do Nível 1 é a AS-N1"


def test_repository_release_model_is_valid(manifest, tmp_path):
    assert release_errors(manifest, tmp_path) == []


def test_module_out_of_curriculum_order_is_rejected(manifest, tmp_path):
    data = copy.deepcopy(manifest)
    data["releases"][1]["modules"] = ["M03", "M05"]  # pula M04
    data["releases"][2]["modules"] = ["M04", "M06", "M07", "M08"]
    errs = release_errors(data, tmp_path)
    assert any("fora da ordem do currículo" in e and "M04" in e for e in errs)


def test_version_must_grow_with_releases(manifest, tmp_path):
    data = copy.deepcopy(manifest)
    data["releases"][2]["version"] = "0.2.0"
    assert any("deve ser maior" in e for e in release_errors(data, tmp_path))


def test_future_release_cannot_be_marked_published(manifest, tmp_path):
    data = copy.deepcopy(manifest)
    data["releases"][2].update(status="published", published_on=None, url=None)
    errs = release_errors(data, tmp_path)
    assert any("R3" in e and "approved_by" in e for e in errs)
    assert any("R3" in e and "não está 'published'" in e for e in errs)


def test_r2_export_scope_excludes_levels_2_to_5(manifest):
    scope = ex.cumulative_scope(manifest, "R2")
    prefixes, out_modules = ex.excluded_paths(manifest, scope)
    assert not any(p.startswith(("docs/modules/03-", "docs/modules/04-")) for p in prefixes)
    for folder in ("05-", "08-", "09-", "12-", "16-", "17-"):
        assert any(p.startswith(f"docs/modules/{folder}") for p in prefixes), folder
    assert "03" not in out_modules and "04" not in out_modules and "05" in out_modules


def test_availability_follows_published_scope(manifest):
    """Páginas de disponibilidade são geradas do manifesto: refletem o escopo publicado, não o planejado."""
    import render_curriculum as rc

    data = copy.deepcopy(manifest)
    for mod in data["modules"]:
        if mod["id"] in {"M03", "M04"}:
            mod["status"] = "in-review"
    before = rc.render_available(data)
    assert "03-governance-risk" not in before and "Nível 1 completo" not in before
    for mod in data["modules"]:
        if mod["id"] in {"M03", "M04"}:
            mod["status"] = "published"
    after = rc.render_available(data)
    assert "Nível 0 e Nível 1 completos" in after and "37 aulas" in after
    assert "../modules/03-governance-risk/index.md" in after and "../modules/04-threat-modeling/index.md" in after
    assert "05-network-security" not in after
    for exam in data["assessments"]:
        if exam["id"] == "AS-N1":
            exam["status"] = "published"
    assert ("Diagnóstica, uma por módulo, a avaliação integradora do Módulo Inicial ao Módulo 2 e a avaliação "
            "integradora do Nível 1") in rc.render_available(data)
    study = rc.render_study_availability(data)
    assert "Nível 0 e Nível 1 completos" in study and "37 aulas" in study and "22 aulas" not in study
    table = rc.render_release_table(data)
    assert "| **2 — Fundamentals: conclusão do Nível 1** | Nível 1 | Módulos 3 e 4 | Disponível" in table
