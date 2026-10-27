"""Testes da gestão de releases: validação da seção `releases` e exportação da árvore pública."""

from __future__ import annotations

import copy
import subprocess
import datetime as dt

import pytest

import export_release as ex
from _common import load_manifest
from validate_manifest import validate


@pytest.fixture()
def manifest() -> dict:
    return load_manifest()


def errors_for(manifest: dict, tmp_path) -> list[str]:
    return [e for e in validate(manifest, tmp_path).errors if e.startswith("release")]


def test_repository_releases_are_cumulative_and_disjoint(manifest):
    r1 = ex.cumulative_scope(manifest, "R1")
    r2 = ex.cumulative_scope(manifest, "R2")
    assert r1["modules"] == {"M00", "M01", "M02"}
    assert r1["modules"] < r2["modules"]
    seen: dict[str, str] = {}
    for rel in manifest["releases"]:
        for key in ex.SCOPES:
            for iid in rel.get(key) or []:
                assert iid not in seen, f"{iid} em {seen.get(iid)} e {rel['id']}"
                seen[iid] = rel["id"]
    every_module = {m["id"] for m in manifest["modules"]} | {c["id"] for c in manifest["complements"]}
    assert every_module <= set(seen), "todo módulo pertence a alguma release"


def test_release_validation_rules(manifest, tmp_path):
    data = copy.deepcopy(manifest)
    rel = data["releases"][0]
    rel.update(status="approved", approved_by=[], approved_on=None, published_on=None, url=None)
    assert any("approved_by" in e for e in errors_for(data, tmp_path))
    rel.update(approved_by=["mantenedor"], approved_on=dt.date(2026, 11, 1))
    assert not any("approved_by" in e or "approved_on" in e for e in errors_for(data, tmp_path))
    rel["status"] = "published"
    data["modules"][0]["status"] = "in-review"  # um item do escopo ainda não publicado
    errs = errors_for(data, tmp_path)
    assert any("published_on" in e for e in errs)
    assert any("URL" in e for e in errs)
    assert any("não está 'published'" in e for e in errs)
    data["releases"][1]["modules"].append("M00")
    assert any("já pertence" in e for e in errors_for(data, tmp_path))
    data["releases"][1]["status"] = "launched"
    assert any("status inválido" in e for e in errors_for(data, tmp_path))
    data["releases"][2].update(status="planned", url="https://example.com")
    assert any("só podem ser preenchidos" in e for e in errors_for(data, tmp_path))


def test_excluded_paths_cover_out_of_scope_content(manifest):
    scope = ex.cumulative_scope(manifest, "R1")
    prefixes, out_modules = ex.excluded_paths(manifest, scope)
    assert "docs/modules/03-governance-risk/" in prefixes
    assert not any(p.startswith("docs/modules/0" + n) for p in prefixes for n in "012")
    assert "05" in out_modules and "02" not in out_modules
    assert ex.is_excluded("assets/diagrams/m09-l01-shared-responsibility.mmd", prefixes, out_modules)
    assert not ex.is_excluded("assets/diagrams/m02-l03-logical.mmd", prefixes, out_modules)
    assert not ex.is_excluded("assets/diagrams/learning-journey.mmd", prefixes, out_modules)
    assert ex.is_excluded("docs/modules/11-hybrid-multicloud/index.md", prefixes, out_modules)


def test_transform_manifest_final_publishes_only_scope(manifest):
    data = copy.deepcopy(manifest)
    rel = {"approved_by": ["mantenedor"], "approved_on": dt.date(2026, 11, 1)}
    scope = ex.cumulative_scope(data, "R1")
    out = ex.transform_manifest(data, scope, "final", rel)
    mods = {m["id"]: m for m in out["modules"]}
    assert mods["M00"]["status"] == "published" and mods["M00"]["reviewed_by"] == ["mantenedor"]
    assert all(lesson["status"] == "published" for lesson in mods["M01"]["lessons"])
    assert mods["M05"]["status"] == "planned" and "path" not in mods["M05"]
    assert all("file" not in lesson for lesson in mods["M05"]["lessons"])
    labs = {lab["id"]: lab for lab in out["labs"]}
    assert labs["LAB-00"]["status"] == "published"


def test_transform_nav_drops_missing_pages_and_empty_groups(tmp_path):
    (tmp_path / "docs" / "a").mkdir(parents=True)
    (tmp_path / "docs" / "a" / "x.md").write_text("x", encoding="utf-8")
    config = (
        'nav = [\n  { "Início" = "index.md" },\n  { "Módulos" = [\n'
        '    { "A" = [\n      "a/x.md",\n    ] },\n'
        '    { "B" = [\n      "b/y.md",\n      "b/z.md",\n    ] },\n  ] },\n]\n'
    )
    out = ex.transform_nav(config, tmp_path)
    assert '"a/x.md"' in out
    assert '"b/y.md"' not in out and '{ "B" = [' not in out
    assert '"index.md"' not in out  # docs/index.md não existe neste diretório de teste


def test_publish_page_marks_review():
    text = ("---\nstatus: in-review\nreviewed_by: []\n---\n\n"
            "| Revisão técnica | Pendente — aguardando revisão do mantenedor |\n"
            '<span class="saa-status saa-status--in-review">In Review</span>\n')
    out = ex.publish_page(text, ["Mantenedor"], dt.date(2026, 11, 1))
    assert "status: published" in out and "reviewed_by: [Mantenedor]" in out
    assert "| Revisão técnica | Mantenedor — 2026-11-01 |" in out
    assert "saa-status--published" in out


def test_final_mode_requires_maintainer_approval(manifest, tmp_path, monkeypatch):
    data = copy.deepcopy(manifest)
    data["releases"][0].update(status="in-review", approved_by=[], approved_on=None)
    monkeypatch.setattr(ex, "load_manifest", lambda root=None: data)
    with pytest.raises(ex.ExportError, match="approved"):
        ex.export("R1", "final", tmp_path / "out")
    data["releases"][0].update(status="approved")
    with pytest.raises(ex.ExportError, match="mantenedor"):
        ex.export("R1", "final", tmp_path / "out")
    with pytest.raises(ex.ExportError, match="desconhecida"):
        ex.cumulative_scope(manifest, "R9")


def test_transform_knowledge_map_keeps_only_scope_lessons(tmp_path):
    (tmp_path / "assets" / "diagrams").mkdir(parents=True)
    (tmp_path / "assets" / "diagrams" / "m01-a.mmd").write_text("x", encoding="utf-8")
    kmap = {"schema_version": 1, "concepts": [
        {"id": "KC-1", "lessons": ["M01-L01", "M05-L02"], "diagrams": ["m01-a", "m05-b"]},
        {"id": "KC-2", "lessons": ["M05-L01"]},
        {"concept": "orientação sem aula", "lessons": []},
    ]}
    scope = {key: set() for key in ex.SCOPES}
    scope["modules"] = {"M00", "M01", "M02"}
    result = ex.transform_knowledge_map(kmap, scope, tmp_path)
    assert [c.get("id") for c in result["concepts"]] == ["KC-1", None]
    assert result["concepts"][0]["lessons"] == ["M01-L01"]
    assert result["concepts"][0]["diagrams"] == ["m01-a"]
    assert kmap["concepts"][0]["lessons"] == ["M01-L01", "M05-L02"]  # entrada original intacta


def test_final_export_is_bound_to_the_approved_commit(tmp_path):
    def git(*args):
        return subprocess.run(["git", "-c", "user.name=P", "-c", "user.email=p@example.com", *args], cwd=tmp_path,
                              check=True, capture_output=True, text=True).stdout.strip()
    git("init", "-q")
    (tmp_path / "curriculum").mkdir()
    (tmp_path / "docs").mkdir()
    (tmp_path / "curriculum" / "manifest.yml").write_text("a", encoding="utf-8")
    (tmp_path / "docs" / "aula.md").write_text("conteúdo revisado", encoding="utf-8")
    git("add", "-A")
    git("commit", "-q", "-m", "conteúdo revisado")
    approved = git("rev-parse", "HEAD")
    exported = ["curriculum/manifest.yml", "docs/aula.md"]
    rel = {"approved_source_commit": approved}
    (tmp_path / "curriculum" / "manifest.yml").write_text("aprovação registrada", encoding="utf-8")
    git("commit", "-q", "-am", "registro da aprovação")
    assert ex.check_approved_commit(tmp_path, rel, exported) == approved
    (tmp_path / "docs" / "aula.md").write_text("mudança não revisada", encoding="utf-8")
    with pytest.raises(ex.ExportError, match="não commitadas"):
        ex.check_approved_commit(tmp_path, rel, exported)
    git("commit", "-q", "-am", "mudança depois da aprovação")
    with pytest.raises(ex.ExportError, match="mudaram depois do commit aprovado"):
        ex.check_approved_commit(tmp_path, rel, exported)
    with pytest.raises(ex.ExportError, match="SHA completo"):
        ex.check_approved_commit(tmp_path, {"approved_source_commit": None}, exported)
