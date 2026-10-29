"""Verificação do RELEASE-MANIFEST.yml: obrigatório no repositório público, opcional no de desenvolvimento.

Até a v0.2.0, o CI usava ``--if-present``: sem o manifesto, a verificação passava — inclusive no
repositório público. A presença agora depende da identidade do repositório (GITHUB_REPOSITORY,
definida pelo runner), não de arquivos que um PR poderia remover.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest
import yaml

import verify_release_manifest as vr

PUBLIC = "andrewsferreira/security-architecture-academy"
DEV = "andrewsferreira/security-architecture-academy-dev"


def _tree(root: Path, **overrides) -> dict:
    files = {"README.md": "# Academy\n", "docs/index.md": "Início\n"}
    curriculum = {"releases": [{"id": "R2", "version": "0.2.0", "patches": [{"version": "0.2.1"}]}]}
    files["curriculum/manifest.yml"] = yaml.safe_dump(curriculum)
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8")
    data = {
        "schema_version": 1, "release": "R2", "version": "0.2.1", "tag": "v0.2.1", "kind": "patch",
        "mode": "final", "status": "approved", "scope": {},
        "approval": {"approved_by": ["Mantenedor"], "approved_on": "2026-10-29",
                     "approved_source_commit": "a" * 40},
        "source": {"repository": DEV, "commit": "b" * 40, "dirty": False},
        "files": {rel: hashlib.sha256((root / rel).read_bytes()).hexdigest() for rel in files},
    }
    data.update(overrides)
    (root / vr.MANIFEST_NAME).write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return data


def run(root: Path, *args: str) -> int:
    return vr.main(["--root", str(root), *args])


def test_valid_manifest_passes_in_every_repository(tmp_path):
    _tree(tmp_path)
    for repo in (PUBLIC, DEV, ""):
        assert run(tmp_path, "--repository", repo) == 0
    assert run(tmp_path, "--repository", PUBLIC, "--require-approval", "--tag", "v0.2.1") == 0


def test_missing_manifest_fails_in_public_repository_and_forks(tmp_path):
    (tmp_path / "README.md").write_text("x", encoding="utf-8")
    assert run(tmp_path, "--repository", PUBLIC) == 1
    assert run(tmp_path, "--repository", "someone/security-architecture-academy") == 1


def test_development_repository_runs_without_public_manifest(tmp_path):
    (tmp_path / "README.md").write_text("x", encoding="utf-8")
    assert run(tmp_path, "--repository", DEV) == 0
    assert run(tmp_path, "--repository", "") == 0  # execução local
    # deploy nunca dispensa o manifesto, em nenhum repositório
    assert run(tmp_path, "--repository", DEV, "--require-approval") == 1


def test_identity_comes_from_the_runner_environment(tmp_path, monkeypatch):
    (tmp_path / "README.md").write_text("x", encoding="utf-8")
    monkeypatch.setenv("GITHUB_REPOSITORY", PUBLIC)
    assert vr.main(["--root", str(tmp_path)]) == 1
    monkeypatch.setenv("GITHUB_REPOSITORY", DEV)
    assert vr.main(["--root", str(tmp_path)]) == 0


def test_changed_hash_is_rejected(tmp_path):
    _tree(tmp_path)
    (tmp_path / "docs" / "index.md").write_text("Início alterado\n", encoding="utf-8")
    report = vr.verify(tmp_path)
    assert any("conteúdo diferente" in e for e in report.errors)


def test_extra_and_removed_files_are_rejected(tmp_path):
    _tree(tmp_path)
    (tmp_path / "docs" / "extra.md").write_text("x", encoding="utf-8")
    (tmp_path / "README.md").unlink()
    errors = vr.verify(tmp_path).errors
    assert any("fora da release: docs/extra.md" in e for e in errors)
    assert any("ausente: README.md" in e for e in errors)


@pytest.mark.parametrize("overrides, message", [
    ({"tag": "v0.2.0"}, "não corresponde à versão"),
    ({"version": "0.2", "tag": "v0.2"}, "versão inválida"),
    ({"version": "0.2.2", "tag": "v0.2.2"}, "difere da publicação registrada"),
    ({"release": "R9"}, "ausente de curriculum/manifest.yml"),
    ({"files": {}}, "files"),
])
def test_inconsistent_version_or_metadata_is_rejected(tmp_path, overrides, message):
    _tree(tmp_path, **overrides)
    assert any(message in e for e in vr.verify(tmp_path).errors)


def test_requested_tag_must_match(tmp_path):
    _tree(tmp_path)
    assert any("difere da release exportada" in e for e in vr.verify(tmp_path, tag="v0.2.0").errors)


@pytest.mark.parametrize("overrides, message", [
    ({"approval": {"approved_by": [], "approved_on": None, "approved_source_commit": "a" * 40}}, "aprovação"),
    ({"approval": {"approved_by": ["M"], "approved_on": "2026-10-29", "approved_source_commit": None}},
     "commit de origem"),
    ({"mode": "candidate"}, "modo final"),
    ({"status": "in-review"}, "exige 'approved'"),
    ({"source": {"dirty": True}}, "não commitadas"),
])
def test_final_mode_requires_approval_fields(tmp_path, overrides, message):
    _tree(tmp_path, **overrides)
    assert vr.verify(tmp_path).errors == []  # integridade sozinha não exige aprovação
    assert any(message in e for e in vr.verify(tmp_path, require_approval=True).errors)


def test_missing_required_field_is_rejected(tmp_path):
    data = _tree(tmp_path)
    data.pop("approval")
    (tmp_path / vr.MANIFEST_NAME).write_text(yaml.safe_dump(data), encoding="utf-8")
    assert any("campo obrigatório ausente: approval" in e for e in vr.verify(tmp_path).errors)


def test_ci_does_not_skip_the_manifest():
    root = Path(__file__).resolve().parent.parent
    ci = (root / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "--if-present" not in ci
    assert "python scripts/verify_release_manifest.py" in ci
    pages = (root / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")
    assert "verify_release_manifest.py --require-approval --tag" in pages
