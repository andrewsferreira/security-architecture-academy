"""CHANGELOG coerente com o manifesto e histórico de versões publicadas protegido.

Regressão da v0.2.0: a árvore pública publicada trazia a versão em *Unreleased*, descrita como
"em revisão; não publicada" — a seção datada só foi escrita no registro pós-publicação, depois do
commit aprovado. O mesmo ocorreu na v0.1.0 e na v0.1.1.
"""

from __future__ import annotations

import copy
import datetime as dt
import hashlib

import pytest

import check_changelog as cc
import export_release as ex
from _common import ROOT, load_manifest, release_publications, repository_role

MANIFEST = load_manifest()
TEXT = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

# SHA-256 do corpo de cada seção já publicada (cabeçalho excluído). Uma seção publicada não é reescrita:
# correções posteriores entram na seção da versão seguinte. Ao registrar uma nova publicação, acrescente
# aqui o hash da seção da versão (mesma alteração que preenche published_on no manifesto).
PUBLISHED_SECTIONS = {
    "0.1.0": "9e2e942ce8080736ff93a9b015e2ff2361819199b52a9d1c1a8c812152b9ff01",
    "0.1.1": "2cfdd5b00cd3f046ed456d1aa128e917856c7ce1ee6f91ae17ad930a6f44fe53",
    "0.2.0": "984fecc4fb3fc0f7cf5e6f120ef6f3469aa73ac821f11b6dbbc91583871dc731",
}


def errors(text: str, manifest: dict, release: bool, tag: str | None = None, target: str | None = None) -> list[str]:
    return cc.check(text, manifest, release, tag, target).errors


def r2(manifest: dict) -> dict:
    return next(r for r in manifest["releases"] if r["id"] == "R2")


# Os cenários usam uma base sintética, independente do que estiver em preparo no momento (outra correção,
# outra release em revisão) e válida tanto no desenvolvimento quanto na árvore pública: só as publicações
# já feitas, R3 em desenvolvimento, R4–R6 planejadas e uma correção fictícia 0.2.99 em revisão.
SYN = "0.2.99"


def _published_text(text: str) -> str:
    out, keep = [], True
    for line in text.splitlines(keepends=True):
        match = cc.HEADER_RE.match(line.rstrip())
        if match:
            keep = match["version"] in PUBLISHED_SECTIONS
            if match["version"] == "Unreleased":
                out.append(line + "\n")
                keep = False
                continue
        if keep:
            out.append(line)
    return "".join(out)


BASE_TEXT = _published_text(TEXT)
BASE_MANIFEST = copy.deepcopy(MANIFEST)
for _rel in BASE_MANIFEST["releases"]:
    _rel["patches"] = [p for p in _rel.get("patches") or [] if p.get("status") == "published"] or None
    if _rel["patches"] is None:
        _rel.pop("patches")
    if _rel.get("status") != "published":
        _rel["status"] = "in-development" if _rel["id"] == "R3" else "planned"
r2(BASE_MANIFEST).setdefault("patches", []).append(
    {"version": SYN, "title": "Correção sintética", "status": "in-review", "approved_by": [], "approved_on": None,
     "approved_source_commit": None, "public_commit": None, "published_on": None})
DEV_TEXT = BASE_TEXT.replace("## [Unreleased]\n\n", f"## [Unreleased]\n\n## [{SYN}] — {cc.PENDING_LABEL}\n\n"
                             "Correção sintética da Release 2.\n\n### Fixed\n\n- Item.\n\n", 1)


def approved(manifest: dict, version: str, on: dt.date) -> dict:
    data = copy.deepcopy(manifest)
    for rel in data["releases"]:
        for record in [rel] + list(rel.get("patches") or []):
            if str(record["version"]) == version:
                record.update(status="approved", approved_by=["Mantenedor"], approved_on=on,
                              approved_source_commit="0" * 40)
    return data


def test_repository_changelog_follows_the_contract():
    rules = cc.release_rules(None, ROOT)  # local: regras de publicação só em árvore exportada no modo final
    assert errors(TEXT, MANIFEST, rules, target=cc.exported_version(ROOT)) == []


@pytest.mark.parametrize("version", sorted(PUBLISHED_SECTIONS))
def test_published_sections_are_not_rewritten(version):
    body = cc.section_body(TEXT, version)
    assert body is not None, f"seção [{version}] ausente"
    assert hashlib.sha256(body.encode("utf-8")).hexdigest() == PUBLISHED_SECTIONS[version], (
        f"a seção [{version}] já publicada foi alterada")


def test_every_published_version_is_protected():
    published = {str(r["version"]) for rel in MANIFEST["releases"] for r in release_publications(rel)
                 if r.get("status") == "published"}
    assert published == set(PUBLISHED_SECTIONS)


def test_v020_public_tree_regression_is_rejected():
    """Árvore como a publicada na v0.2.0: versão em Unreleased, 'em revisão; não publicada'."""
    data = copy.deepcopy(BASE_MANIFEST)
    rel = r2(data)
    rel.pop("patches", None)
    rel.update(status="approved", public_commit=None, published_on=None)
    body = cc.section_body(BASE_TEXT, "0.2.0")
    rest = body.split("\n### ", 1)[1]
    stale = BASE_TEXT.replace(f"## [0.2.0] — 2026-10-28\n\n{body}", "").replace(
        "## [Unreleased]\n", "## [Unreleased]\n\nRelease 2 — Fundamentals: conclusão do Nível 1 "
        "(v0.2.0, em revisão; não publicada).\n\n### " + rest)
    errs = errors(stale, data, release=True, tag="v0.2.0")
    assert any("[Unreleased] precisa estar vazio" in e for e in errs)
    assert any("[0.2.0]" in e and "seção ausente" in e for e in errs)
    assert any("v0.2.0: a versão publicada precisa de seção datada" in e for e in errs)


def test_pending_version_needs_its_own_section():
    assert errors(DEV_TEXT, BASE_MANIFEST, release=False) == []
    without = DEV_TEXT.replace(f"## [{SYN}] — {cc.PENDING_LABEL}", "### Versão em preparo")
    assert any("seção ausente" in e for e in errors(without, BASE_MANIFEST, release=False))
    spaced = DEV_TEXT.replace(f"## [{SYN}] — {cc.PENDING_LABEL}", f"## [{SYN}] — {cc.PENDING_LABEL}  ")
    assert ex.publish_changelog(spaced, SYN, None)  # espaço no fim não impede a exportação


def test_final_export_dates_the_approved_version_and_passes_release_rules():
    on = dt.date(2026, 10, 29)
    data = approved(BASE_MANIFEST, SYN, on)
    final = ex.publish_changelog(DEV_TEXT, SYN, on)
    assert f"## [{SYN}] — 2026-10-29" in final
    assert cc.PENDING_LABEL not in "\n".join(l for l in final.splitlines() if l.startswith("## ["))
    assert errors(final, data, release=True, tag=f"v{SYN}") == []
    # o commit aprovado continua válido nas regras do desenvolvimento
    assert errors(DEV_TEXT, data, release=False) == []
    # sem a transformação, a árvore de publicação é rejeitada
    assert any("não publicada" in e for e in errors(DEV_TEXT, data, release=True))


def test_export_keeps_only_the_release_and_published_history():
    """Notas de Unreleased e seções pendentes de outro nível não vão à árvore pública."""
    work = DEV_TEXT.replace("## [Unreleased]\n", "## [Unreleased]\n\n- nota interna\n\n## [0.3.0] — não publicada\n\n"
                            "Release 3 em desenvolvimento.\n\n", 1)
    assert errors(work, BASE_MANIFEST, release=False) == []
    candidate = ex.publish_changelog(work, SYN, None)
    assert "nota interna" not in candidate and "[0.3.0]" not in candidate
    assert f"## [{SYN}] — {cc.PENDING_LABEL}" in candidate
    for version in PUBLISHED_SECTIONS:
        assert cc.section_body(candidate, version) == cc.section_body(TEXT, version)


def test_patch_can_ship_while_another_release_is_in_review():
    """Correção da R2 exportada com a R3 em revisão (e o inverso): só a versão-alvo tem seção na árvore."""
    data = copy.deepcopy(BASE_MANIFEST)
    next(r for r in data["releases"] if r["id"] == "R3")["status"] = "in-review"
    work = DEV_TEXT.replace("## [Unreleased]\n", "## [Unreleased]\n\n## [0.3.0] — não publicada\n\n"
                            "Release 3: Nível 2 (37 aulas).\n\n", 1)
    assert errors(work, data, release=False) == []
    on = dt.date(2026, 11, 2)
    final = ex.publish_changelog(work, SYN, on)
    assert errors(final, approved(data, SYN, on), release=True, tag=f"v{SYN}") == []
    candidate_r3 = ex.publish_changelog(work, "0.3.0", None)
    assert errors(candidate_r3, data, release=False, target="0.3.0") == []
    assert any("não pertence a esta árvore" in e for e in errors(work, data, release=True, tag=f"v{SYN}"))


def test_export_refuses_changelog_without_pending_section():
    with pytest.raises(ex.ExportError, match="exatamente uma seção"):
        ex.publish_changelog("# Changelog\n\n## [Unreleased]\n", "9.9.9", dt.date(2026, 1, 1))


def test_dates_order_scope_and_planned_versions():
    data = BASE_MANIFEST
    wrong_date = BASE_TEXT.replace("## [0.1.1] — 2026-10-27", "## [0.1.1] — 2026-10-26")
    assert any("difere de approved_on" in e for e in errors(wrong_date, data, release=False))
    planned = BASE_TEXT.replace("## [Unreleased]\n", "## [Unreleased]\n\n## [0.5.0] — não publicada\n")
    assert any("versão planejada" in e for e in errors(planned, data, release=False))
    developing = BASE_TEXT.replace("## [Unreleased]\n", "## [Unreleased]\n\n## [0.3.0] — 2026-12-01\n")
    assert any("em desenvolvimento" in e for e in errors(developing, data, release=False))
    unknown = BASE_TEXT.replace("## [Unreleased]\n", "## [Unreleased]\n\n## [9.9.9] — 2026-01-01\n")
    assert any("sem publicação correspondente" in e for e in errors(unknown, data, release=False))
    a, b = cc.section_body(BASE_TEXT, "0.1.1"), cc.section_body(BASE_TEXT, "0.1.0")
    swapped = BASE_TEXT.replace(f"## [0.1.1] — 2026-10-27\n\n{a}", "@@A@@").replace(
        f"## [0.1.0] — 2026-10-27\n\n{b}", f"## [0.1.1] — 2026-10-27\n\n{a}").replace(
        "@@A@@", f"## [0.1.0] — 2026-10-27\n\n{b}")
    assert any("ordem decrescente" in e for e in errors(swapped, data, release=False))
    no_scope = BASE_TEXT.replace("(37 aulas)", "").replace("— 37 aulas", "")
    assert any("37 aulas" in e for e in errors(no_scope, data, release=False))
    stale_intro = BASE_TEXT.replace("Estabilização da Release 1 — Fundamentals, publicada",
                                    "Estabilização da Release 1 — Fundamentals, em revisão,")
    assert any("abertura" in e for e in errors(stale_intro, data, release=False))


def test_cumulative_lessons_follow_the_manifest():
    assert cc.cumulative_lessons(MANIFEST, "R1") == 22
    assert cc.cumulative_lessons(MANIFEST, "R2") == 37


def test_repository_role_is_taken_from_the_runner_identity():
    assert repository_role(None) == "local"
    assert repository_role("") == "local"
    assert repository_role("andrewsferreira/security-architecture-academy-dev") == "development"
    assert repository_role("AndrewsFerreira/Security-Architecture-Academy-Dev") == "development"
    assert repository_role("andrewsferreira/security-architecture-academy") == "public"
    assert repository_role("someone/security-architecture-academy") == "public"  # fork: regras estritas


def test_rules_follow_repository_identity_and_exported_tree(tmp_path):
    assert cc.release_rules(None, tmp_path) is False  # local, sem árvore exportada
    (tmp_path / "RELEASE-MANIFEST.yml").write_text("mode: candidate\n", encoding="utf-8")
    assert cc.release_rules(None, tmp_path) is False  # candidata: regras do desenvolvimento
    (tmp_path / "RELEASE-MANIFEST.yml").write_text("mode: final\n", encoding="utf-8")
    assert cc.release_rules(None, tmp_path) is True
    assert cc.release_rules("andrewsferreira/security-architecture-academy-dev", tmp_path) is False
    assert cc.release_rules("andrewsferreira/security-architecture-academy", tmp_path) is True
