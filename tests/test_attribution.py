"""Testes da verificação de atribuição de autoria e do manifesto de release."""

from __future__ import annotations

import hashlib
import subprocess

import yaml

import check_attribution as ca
import export_release as ex
from _common import Report
from verify_release_manifest import verify


def scan(text: str, rel: str = "docs/x.md", allowlist=None) -> tuple[Report, list[str]]:
    report, mentions = Report("t"), []
    ca.scan_text(rel, text, report, allowlist or [], mentions)
    return report, mentions


def test_credit_expressions_are_errors():
    for line in ("Co-Authored-By: Assistant <noreply@anthropic.com>",
                 "Generated with Claude Code",
                 "Conteúdo gerado por IA",
                 "Este material foi escrito com o ChatGPT.",
                 "Built with AI",
                 "Powered by OpenAI",
                 "Elaborado com auxílio de inteligência artificial"):
        report, _ = scan(line)
        assert report.errors, line


def test_academic_mentions_are_only_listed_for_review():
    report, mentions = scan("| Microsoft 365 e Copilot | — | controles do Microsoft 365 Copilot |")
    assert not report.errors and len(mentions) == 1
    report, mentions = scan("O malware precursor usa credenciais roubadas.")
    assert not report.errors and not mentions


def test_allowlist_requires_path_and_excerpt():
    allow = [{"path": "docs/x.md", "contains": "código gerado por IA", "reason": "tema da aula"}]
    report, _ = scan("Riscos do código gerado por IA em produção.", allowlist=allow)
    assert not report.errors
    report, _ = scan("Riscos do código gerado por IA em produção.", rel="docs/y.md", allowlist=allow)
    assert report.errors


def test_agent_instruction_files_are_blocked(tmp_path):
    for name in ("CLAUDE.md", "AGENTS.md", ".claude/settings.json", ".github/copilot-instructions.md", "a/.cursor/x"):
        assert ca.AGENT_PATH_RE.search(name), name
    assert not ca.AGENT_PATH_RE.search("docs/agents/overview.md")
    (tmp_path / "AGENTS.md").write_text("x", encoding="utf-8")
    report = Report("t")
    ca.scan_tree(tmp_path, report, tracked=False, allowlist=[])
    assert report.errors


def test_commit_messages_and_authors(tmp_path):
    def run(*args):
        subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True)
    run("init", "-q")
    run("-c", "user.name=Pessoa", "-c", "user.email=pessoa@example.com", "commit", "-q", "--allow-empty", "-m", "docs: ok")
    run("-c", "user.name=Pessoa", "-c", "user.email=pessoa@example.com", "commit", "-q", "--allow-empty",
        "-m", "feat: x\n\nCo-Authored-By: Bot <noreply@anthropic.com>")
    report = Report("t")
    monkey_root = ca.ROOT
    try:
        ca.ROOT = tmp_path
        assert ca.scan_commits(tmp_path, "HEAD", report) == 2
    finally:
        ca.ROOT = monkey_root
    assert len(report.errors) == 1 and "Co-Authored-By" in report.errors[0]


def write_tree(root, files: dict[str, str], **overrides) -> None:
    for rel, text in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8")
    data = {"release": "R1", "version": "0.1.0", "tag": "v0.1.0", "mode": "final", "status": "approved",
            "scope": {}, "source": {"dirty": False},
            "approval": {"approved_by": ["Mantenedor"], "approved_on": "2026-11-01", "approved_source_commit": "a" * 40},
            "files": {rel: hashlib.sha256(text.encode()).hexdigest() for rel, text in files.items()}}
    data.update(overrides)
    (root / "RELEASE-MANIFEST.yml").write_text(yaml.safe_dump(data), encoding="utf-8")


def test_release_manifest_integrity(tmp_path):
    write_tree(tmp_path, {"README.md": "a", "docs/index.md": "b"})
    assert not verify(tmp_path, require_approval=True, tag="v0.1.0").errors
    (tmp_path / "site").mkdir()
    (tmp_path / "site" / "index.html").write_text("gerado", encoding="utf-8")
    assert not verify(tmp_path).errors, "artefatos de build são ignorados"
    (tmp_path / "docs" / "index.md").write_text("alterado", encoding="utf-8")
    (tmp_path / "extra.md").write_text("x", encoding="utf-8")
    errors = verify(tmp_path, tag="v0.2.0").errors
    assert any("conteúdo diferente" in e for e in errors)
    assert any("fora da release" in e for e in errors)
    assert any("tag solicitada" in e for e in errors)


def test_release_manifest_requires_approval(tmp_path):
    write_tree(tmp_path, {"README.md": "a"}, mode="candidate", status="in-review",
               approval={"approved_by": [], "approved_on": None, "approved_source_commit": None})
    assert not verify(tmp_path).errors
    errors = verify(tmp_path, require_approval=True).errors
    assert len(errors) == 4


def test_public_allowlist_excludes_process_reports():
    allow = ex.load_allowlist()
    for rel in ("PROGRESS.md", "RELEASE-PLAN.md", "RELEASE-1-REVIEW-PACKAGE.md", "FINAL-CONSOLIDATION-REPORT.md",
                "ACADEMIC-COMPLETENESS-REPORT.md", "FUNDAMENTALS-PUBLICATION-READINESS.md", "CLAUDE.md"):
        assert not ex.is_public(rel, allow), rel
    for rel in ("README.md", "docs/index.md", "scripts/check_attribution.py", "LICENSE", "CONTRIBUTING.md",
                "research/bibliography.yml", "research/notes/BOOK-ANDERSON-SE3.md", ".github/workflows/pages.yml"):
        assert ex.is_public(rel, allow), rel
    # Documentação operacional e configurações de manutenção ficam só no desenvolvimento.
    for rel in ("scripts/export_landing.py", "docs/internal/index.md", "docs/internal/design-system.md",
                "docs/internal/fundamentals-final-editorial-review.md", "docs/internal/fundamentals-v0.1.1-stabilization.md",
                "docs/getting-started/local-development.md", "authoring/technical-lesson.md", "PROJECT-STANDARDS.md",
                "private-research/README.md", ".github/dependabot.yml"):
        assert not ex.is_public(rel, allow), rel


def test_landing_export_publishes_no_lessons():
    import pytest

    el = pytest.importorskip("export_landing", reason="exportador da página institucional só existe no desenvolvimento")

    chosen = el.selection()
    assert {"README.md", "zensical.toml", "docs/index.md", ".github/workflows/pages.yml"} <= set(chosen)
    assert not any(p.startswith(("docs/modules/", "docs/labs/", "docs/assessments/", "docs/case-studies/",
                                 "examples/", "research/", "curriculum/")) for p in chosen)
    assert all(p.startswith("docs/assets/") or p in el.SHARED_FILES or p in el.OVERLAY.values() for p in chosen)
