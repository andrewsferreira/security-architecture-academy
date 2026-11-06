"""Contrato de publicação: o que entra na árvore e no site públicos e como cada item é representado.

Cobre os cenários da auditoria de integridade da R3 (docs/internal/r3-publication-integrity-audit.md):
conteúdo publicado, em revisão, planejado e rascunho; isolamento de releases futuras e do Handbook;
arquivo sem classificação; preservação do que já foi publicado; Research Library; acesso por URL,
busca e sitemap; reprodutibilidade; falha fechada; e autorização da release.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

import check_site_scope as css
import export_release as ex
from _common import ROOT, load_manifest
from validate_references import coverage

# Repositório de desenvolvimento: tem histórico Git e não é uma árvore exportada. O repositório público também
# tem .git, mas traz o RELEASE-MANIFEST.yml, e nele a exportação não se aplica.
DEV_REPOSITORY = (ROOT / ".git").exists() and not (ROOT / "RELEASE-MANIFEST.yml").is_file()


@pytest.fixture()
def manifest() -> dict:
    return load_manifest()


def empty_scope() -> dict[str, set[str]]:
    return {key: set() for key in ex.SCOPES}


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


# ------------------------------------------------------------ classificação (G, F, E)
def minimal_tree(tmp_path: Path) -> tuple[Path, dict, dict]:
    write(tmp_path / "zensical.toml", '[project]\nnav = [\n  { "Início" = "index.md" },\n]\n')
    write(tmp_path / "docs" / "index.md", "# Início\n")
    write(tmp_path / "README.md", "# Projeto\n")
    allow = {"files": ["README.md", "zensical.toml"], "directories": [], "exclude": [], "shared_diagrams": []}
    manifest = {"modules": [{"id": "M05", "slug": "network-security", "status": "in-review",
                             "lessons": [{"id": "M05-L01", "file": "01-a.md", "status": "in-review"}]}],
                "complements": [], "case_studies": [], "labs": [], "assessments": [], "artifacts": []}
    return tmp_path, manifest, allow


def test_tree_with_only_eligible_files_is_fully_classified(tmp_path):
    out, manifest, allow = minimal_tree(tmp_path)
    write(out / "docs" / "modules" / "05-network-security" / "01-a.md", "# Aula\n")
    write(out / "assets" / "diagrams" / "m05-l01-x.mmd", "flowchart LR\n")
    scope = empty_scope()
    scope["modules"] = {"M05"}
    inventory, unclassified = ex.classify_tree(out, manifest, scope, allow)
    assert unclassified == []
    lesson = next(e for e in inventory if e["path"].endswith("01-a.md"))
    assert (lesson["item"], lesson["status"]) == ("M05-L01", "in-review")


def test_unclassified_document_is_rejected(tmp_path):
    """Teste G: página com cara de conteúdo, fora do currículo e da navegação, não tem razão para ser pública."""
    out, manifest, allow = minimal_tree(tmp_path)
    write(out / "docs" / "new-topic" / "draft-notes.md", "# Notas\n")
    write(out / "unknown-dir" / "file.txt", "x")
    _, unclassified = ex.classify_tree(out, manifest, empty_scope(), allow)
    assert unclassified == ["docs/new-topic/draft-notes.md", "unknown-dir/file.txt"]


def test_out_of_scope_module_files_are_unclassified(tmp_path):
    """Teste E: arquivo de módulo fora do escopo que escape do filtro de cópia não passa pela classificação."""
    out, manifest, allow = minimal_tree(tmp_path)
    write(out / "docs" / "modules" / "05-network-security" / "01-a.md", "# Aula\n")
    write(out / "assets" / "diagrams" / "m05-l01-x.mmd", "flowchart LR\n")
    _, unclassified = ex.classify_tree(out, manifest, empty_scope(), allow)  # M05 fora do escopo
    assert unclassified == ["assets/diagrams/m05-l01-x.mmd", "docs/modules/05-network-security/01-a.md"]


@pytest.mark.parametrize("path", ["docs/internal/new-report.md", "docs/internal/sub/deep/page.md",
                                  "docs/getting-started/local-development.md", "authoring/template.md",
                                  "PROJECT-STANDARDS.md", "PROGRESS.md", "RELEASE-PLAN.md", "notes-local.md"])
def test_internal_and_unlisted_paths_never_reach_the_public_repository(path):
    """Teste F: o Handbook, os templates e os relatórios de processo ficam só no desenvolvimento."""
    assert not ex.is_public(path, ex.load_allowlist(ROOT))


def test_future_module_and_activity_paths_are_excluded_for_r3(manifest):
    scope = ex.cumulative_scope(manifest, "R3")
    prefixes, out_modules = ex.excluded_paths(manifest, scope)
    for unit in manifest["modules"]:
        inside = unit["id"] in scope["modules"]
        new_page = ex.unit_dir(unit) + "/99-new-lesson.md"
        assert ex.is_excluded(new_page, prefixes, out_modules) is (not inside)
        diagram = f"assets/diagrams/m{unit['id'][1:]}-l99-new.mmd"
        assert ex.is_excluded(diagram, prefixes, out_modules) is (not inside)
    for key in ex.COLLECTIONS:
        for item in manifest[key]:
            if item.get("path") and item["id"] not in scope[key]:
                assert ex.is_excluded(f"docs/{item['path']}", prefixes, out_modules)


def test_unreferenced_activity_diagram_stays_out(tmp_path):
    out, _, allow = minimal_tree(tmp_path)
    write(out / "docs" / "case-studies" / "case-a" / "index.md", '--8<-- "assets/diagrams/case-a-to-be.mmd"\n')
    for name in ("case-a-to-be", "case-b-to-be", "shared-flow", "m05-l01-x"):
        write(out / "assets" / "diagrams" / f"{name}.mmd", "flowchart LR\n")
    allow["shared_diagrams"] = ["assets/diagrams/shared-flow.mmd"]
    assert ex.unreferenced_shared_diagrams(out, allow) == ["assets/diagrams/case-b-to-be.mmd"]


# ------------------------------------------------------------ status (B, D, N, O)
def test_draft_page_in_tree_is_a_finding(tmp_path):
    """Teste D: rascunho nunca entra na árvore pública."""
    write(tmp_path / "docs" / "x.md", "---\ntitle: X\nstatus: draft\n---\n")
    assert ex.scope_findings(tmp_path, "candidate") == ["docs/x.md: rascunho na árvore pública"]


def test_in_review_is_allowed_in_candidate_and_blocked_in_final(tmp_path):
    """Teste B: em revisão só na candidata; a árvore final não pode conter 'in-review'."""
    write(tmp_path / "docs" / "x.md", "---\ntitle: X\nstatus: in-review\n---\n")
    assert ex.scope_findings(tmp_path, "candidate") == []
    assert ex.scope_findings(tmp_path, "final") == ["docs/x.md: 'in-review' na árvore de publicação"]


def test_final_transform_never_promotes_draft_or_planned(manifest):
    data = copy.deepcopy(manifest)
    r3 = next(r for r in data["releases"] if r["id"] == "R3")
    r3.update(approved_by=["Mantenedor"], approved_on=__import__("datetime").date(2026, 1, 1))
    m05 = next(m for m in data["modules"] if m["id"] == "M05")
    m05["lessons"][0]["status"] = "draft"
    scope = ex.cumulative_scope(data, "R3")
    out = ex.transform_manifest(data, scope, "final", r3)
    lesson = next(m for m in out["modules"] if m["id"] == "M05")["lessons"][0]
    assert lesson["status"] == "draft"  # fica 'draft' e a validação --release da árvore bloqueia


def test_unknown_release_fails_closed(manifest):
    with pytest.raises(ex.ExportError):
        ex.cumulative_scope(manifest, "R99")


def test_candidate_and_final_have_different_authorization_requirements(manifest, tmp_path):
    """Teste O: a candidata não exige aprovação; a final exige status e campos preenchidos pelo mantenedor."""
    r3 = next(r for r in manifest["releases"] if r["id"] == "R3")
    if r3["status"] in {"approved", "published"}:
        pytest.skip("R3 já aprovada neste manifesto")
    with pytest.raises(ex.ExportError, match="modo final exige"):
        ex.export("R3", "final", tmp_path / "out")


# ------------------------------------------------------------ preservação (H)
def test_published_content_stays_in_every_later_release(manifest):
    releases = manifest["releases"]
    previous: dict[str, set[str]] = empty_scope()
    for rel in releases:
        scope = ex.cumulative_scope(manifest, rel["id"])
        for key in ex.SCOPES:
            assert previous[key] <= scope[key], f"{rel['id']} remove {key} de releases anteriores"
        previous = scope
    published = [r["id"] for r in releases if r["status"] in {"approved", "published"}]
    last = ex.cumulative_scope(manifest, published[-1])
    for unit in manifest["modules"]:
        if unit["status"] == "published":
            assert unit["id"] in last["modules"]


# ------------------------------------------------------------ Research Library (J)
def test_coverage_reports_only_modules_with_content(manifest):
    bib = yaml.safe_load((ROOT / "research" / "bibliography.yml").read_text(encoding="utf-8"))
    kmap = yaml.safe_load((ROOT / "research" / "knowledge-map.yml").read_text(encoding="utf-8"))
    public = ex.transform_manifest(copy.deepcopy(manifest), ex.cumulative_scope(manifest, "R3"), "candidate",
                                   next(r for r in manifest["releases"] if r["id"] == "R3"))
    cov = coverage(bib, kmap, public, {})
    rows = [r["id"] for r in cov["modules"]]
    assert rows == sorted(ex.cumulative_scope(manifest, "R3")["modules"])
    assert set(cov["planned"]) == {m["id"] for m in manifest["modules"]} - set(rows)


def test_knowledge_map_drops_relations_to_future_modules(tmp_path):
    kmap = {"concepts": [
        {"id": "KC-1", "modules": ["M05", "M09"], "lessons": ["M05-L01", "M09-L01"]},
        {"id": "KC-2", "modules": ["M09"], "lessons": []},     # orientação só de módulo futuro
        {"id": "KC-3", "modules": ["M05"], "lessons": []},
        {"id": "KC-4", "lessons": []},                          # sem módulo: orientação geral
    ]}
    scope = empty_scope()
    scope["modules"] = {"M05"}
    result = ex.transform_knowledge_map(kmap, scope, tmp_path)
    assert [c["id"] for c in result["concepts"]] == ["KC-1", "KC-3", "KC-4"]
    assert result["concepts"][0]["modules"] == ["M05"]
    assert result["concepts"][0]["lessons"] == ["M05-L01"]


def test_bibliography_filter_keeps_every_reference_and_the_comments():
    text = ("# cabeçalho\nreferences:\n- id: A\n  modules:\n  - M05\n  - M09\n  chapters:\n  - locator: Cap. 1\n"
            "    modules:\n    - M09\n    pages: '3'\n- id: B\n  modules:\n  - M11\n  notes: x\n- id: C\n  modules: []\n")
    scope = empty_scope()
    scope["modules"] = {"M05"}
    result = ex.transform_bibliography(text, scope)
    data = yaml.safe_load(result)
    assert result.startswith("# cabeçalho\n")
    assert [r["id"] for r in data["references"]] == ["A", "B", "C"]
    assert data["references"][0]["modules"] == ["M05"]
    assert data["references"][0]["chapters"][0]["modules"] == []
    assert data["references"][1]["modules"] == [] and data["references"][1]["notes"] == "x"


# ------------------------------------------------------------ site, busca e sitemap (A, C, K, L)
SITE_URL = "https://example.org/academy/"


def fake_site(tmp_path: Path, pages: list[str]) -> tuple[Path, Path]:
    docs, site = tmp_path / "docs", tmp_path / "site"
    for page in pages:
        write(docs / page, "# p\n")
        url = page[:-3]
        url = "" if url == "index" else (url[:-5] if url.endswith("/index") else url + "/")
        write(site / url / "index.html", "<html></html>")
    write(site / "404.html", "<html></html>")
    items = [{"location": (p[:-3] + "/").replace("index/", "") if p != "index.md" else ""} for p in pages]
    write(site / "search.json", json.dumps({"items": items}))
    locs = "".join(f"<url><loc>{SITE_URL}{i['location']}</loc></url>" for i in items)
    write(site / "sitemap.xml", f"<urlset>{locs}</urlset>")
    return site, docs


PLANNED = {"modules": [{"id": "M09", "slug": "aws", "status": "planned"}], "complements": []}


def test_site_scope_accepts_a_consistent_site(tmp_path):
    site, docs = fake_site(tmp_path, ["index.md", "modules/05-net/index.md", "modules/05-net/01-a.md"])
    assert css.check(site, docs, PLANNED, SITE_URL, public=True).errors == []


def test_planned_module_is_not_reachable_by_direct_url(tmp_path):
    """Testes C e K: HTML de módulo planejado no site, mesmo sem link, é erro."""
    site, docs = fake_site(tmp_path, ["index.md"])
    write(site / "modules" / "09-aws" / "01-lesson" / "index.html", "<html></html>")
    errors = css.check(site, docs, PLANNED, SITE_URL, public=True).errors
    assert "página compilada sem Markdown na árvore: modules/09-aws/01-lesson/" in errors
    assert "endereço proibido acessível no site: modules/09-aws/01-lesson/" in errors


def test_search_and_sitemap_cannot_point_to_excluded_pages(tmp_path):
    """Teste L: busca e sitemap só apontam para páginas da árvore."""
    site, docs = fake_site(tmp_path, ["index.md"])
    write(site / "search.json", json.dumps({"items": [{"location": ""}, {"location": "internal/workflow/#x"}]}))
    write(site / "sitemap.xml", f"<urlset><url><loc>{SITE_URL}</loc></url><url><loc>{SITE_URL}modules/09-aws/</loc></url></urlset>")
    errors = css.check(site, docs, PLANNED, SITE_URL, public=True).errors
    assert "índice de busca aponta para página inexistente ou excluída: internal/workflow/" in errors
    assert "sitemap aponta para página inexistente ou excluída: modules/09-aws/" in errors


def test_handbook_pages_are_forbidden_only_in_the_public_tree(tmp_path):
    site, docs = fake_site(tmp_path, ["index.md", "internal/workflow.md"])
    assert css.check(site, docs, PLANNED, SITE_URL, public=False).errors == []
    assert "endereço proibido acessível no site: internal/workflow/" in css.check(site, docs, PLANNED, SITE_URL,
                                                                                 public=True).errors


# ------------------------------------------------------------ exportação real (A, M)
@pytest.mark.skipif(not DEV_REPOSITORY, reason="exportação: só no repositório de desenvolvimento")
def test_export_is_reproducible_and_fully_classified(tmp_path):
    """Teste M: duas exportações do mesmo commit geram o mesmo inventário e os mesmos SHA-256."""
    runs = []
    for name in ("a", "b"):
        result = ex.export("R3", "candidate", tmp_path / name)
        files = yaml.safe_load((tmp_path / name / ex.RELEASE_MANIFEST).read_text(encoding="utf-8"))["files"]
        runs.append((files, result["inventory"]))
    assert runs[0][0] == runs[1][0]
    assert runs[0][1] == runs[1][1]
    paths = {e["path"] for e in runs[0][1]}
    assert "docs/modules/05-network-security/index.md" in paths            # Teste A: módulo do escopo presente
    assert not any(p.startswith(("docs/internal/", "docs/modules/09-")) for p in paths)
    digest = hashlib.sha256(json.dumps(sorted(runs[0][0].items())).encode()).hexdigest()
    assert len(digest) == 64


# ------------------------------------------------------------ página inicial (I)
def homepage_for(manifest: dict, release_id: str, mode: str) -> str:
    import render_curriculum as rc

    data = copy.deepcopy(manifest)
    rel = next(r for r in data["releases"] if r["id"] == release_id)
    # Estado de candidata da release, também na árvore final (onde ela já aparece publicada).
    rel.update(status="in-review", approved_by=[], approved_on=None)
    for unit in data["modules"]:
        if unit["id"] in rel["modules"]:
            for item in [unit] + list(unit.get("lessons") or []):
                if item.get("status") == "published":
                    item["status"] = "in-review"
    if mode == "final":
        rel.update(status="approved", approved_by=["Mantenedor"], approved_on=__import__("datetime").date(2026, 1, 1))
    public = ex.transform_manifest(data, ex.cumulative_scope(data, release_id), mode, rel)
    return rc.render_release_status(public)


def test_homepage_follows_the_exported_manifest(manifest):
    """Teste I: versões, rótulos e links da página inicial vêm do manifesto público da exportação."""
    candidate = homepage_for(manifest, "R3", "candidate")
    final = homepage_for(manifest, "R3", "final")
    r3 = next(r for r in manifest["releases"] if r["id"] == "R3")
    assert f"v{r3['version']} —" not in candidate.split("Publicado:", 1)[1].split("**.", 1)[0]
    assert "Continuar no Professional" not in candidate
    assert f"v{r3['version']} — Nível 2" in final.split("Publicado:", 1)[1].split("**.", 1)[0]
    assert "[Continuar no Professional](modules/05-network-security/index.md)" in final
    step = final.split("### Nível 2: Arquiteturas de Infraestrutura", 1)[1].split("</div>", 1)[0]
    assert "saa-status--published" in step
    for later in ("### Nível 3", "### Nível 4", "### Nível 5"):
        block = final.split(later, 1)[1].split("</div>", 1)[0]
        assert "saa-status--published" not in block and "Disponível" not in block


# ------------------------------------------------------------ selos escritos à mão (B, G)
def badge(status: str) -> str:
    return f'<span class="saa-status saa-status--{status}">X</span>'


BADGE_MANIFEST = {
    "modules": [{"id": "M05", "slug": "network-security", "status": "in-review", "lessons": []}],
    "complements": [], "labs": [], "assessments": [],
    "case_studies": [{"id": "CS-B", "title": "Caso B — Migração para AWS", "status": "planned"}],
    "artifacts": [{"id": "ART-TM", "title": "Threat Model", "status": "in-review", "path": "artifacts/threat-model.md"}],
}


def badge_errors(tmp_path: Path, page: str, text: str) -> list[str]:
    import check_status_badges as csb

    write(tmp_path / page, text)
    return csb.check(tmp_path / "docs", BADGE_MANIFEST, tmp_path).errors


def test_manual_badges_match_the_manifest(tmp_path):
    text = (f"| [Threat Model](threat-model.md) | x | {badge('in-review')} |\n"
            f"| **B — Migração para AWS** | x | {badge('planned')} |\n"
            f"| {badge('published')} | legenda |\n")
    assert badge_errors(tmp_path, "docs/artifacts/index.md", text) == []


def test_manual_badge_cannot_claim_publication(tmp_path):
    """Selo 'published' para item em revisão ou planejado é erro, inclusive na árvore final."""
    text = f"| [Threat Model](threat-model.md) | x | {badge('published')} |\n| `CS-B` | {badge('in-review')} |\n"
    errors = badge_errors(tmp_path, "docs/artifacts/index.md", text)
    assert any("ART-TM com selo 'published'" in e for e in errors)
    assert any("CS-B com selo 'in-review'" in e for e in errors)


def test_unidentified_badge_may_only_say_planned(tmp_path):
    text = f"| Avaliações futuras | {badge('planned')} |\n| Algo sem item | {badge('published')} |\n"
    errors = badge_errors(tmp_path, "docs/assessments/index.md", text)
    assert errors == ["docs/assessments/index.md:2: selo 'published' sem item identificável no manifesto"]


def test_module_page_badge_follows_the_module(tmp_path):
    errors = badge_errors(tmp_path, "docs/modules/05-network-security/index.md", badge("published") + "\n")
    assert errors == ["docs/modules/05-network-security/index.md:1: M05 com selo 'published', mas o manifesto diz 'in-review'"]


# ------------------------------------------------------------ "Como usar a Academy" na árvore final
def test_available_block_has_a_card_for_every_module_of_a_published_release():
    """Quando uma release é publicada, cada módulo dela tem card com descrição em "Como usar a Academy".

    Sem a descrição, o card sai vazio na árvore pública (e o markdownlint do repositório público falha).
    """
    import render_curriculum as rc

    manifest = copy.deepcopy(load_manifest())
    ids = {str(mid) for rel in manifest["releases"] if rel.get("status") in ("published", "approved", "in-review")
           for mid in rel.get("modules") or []}
    for unit in manifest["modules"]:
        if str(unit["id"]) in ids and unit.get("path"):
            unit["status"] = "published"
    for item in manifest.get("assessments") or []:
        if item.get("status") == "in-review":
            item["status"] = "published"
    out = rc.render_available(manifest)
    assert "    ---\n\n    \n" not in out, "card sem descrição em 'Como usar a Academy'"
    assert "\n\n\n" not in out
    for mid in sorted(ids):
        assert mid in rc.MODULE_CARDS, f"{mid} sem card em MODULE_CARDS"
    assert "a avaliação intermediária dos Níveis 1 e 2" in out
