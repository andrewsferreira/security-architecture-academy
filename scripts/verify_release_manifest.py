#!/usr/bin/env python3
"""Confere a árvore pública contra o RELEASE-MANIFEST.yml gerado na exportação.

Garante que o repositório público contém exatamente os arquivos da release
exportada (mesmo conjunto, mesmo SHA-256), sem arquivos extras, sem obras de
terceiros (PDF/EPUB) e — com --require-approval — que a release foi aprovada
pelo mantenedor, com o commit de origem registrado.

Presença do manifesto, pela identidade do repositório (GITHUB_REPOSITORY, definida
pelo runner do GitHub Actions, ou --repository):
    público (e qualquer outro, inclusive forks)  RELEASE-MANIFEST.yml obrigatório.
    desenvolvimento                               ausência permitida: o manifesto só
                                                  existe nas árvores exportadas.
    local (sem GITHUB_REPOSITORY)                 ausência permitida, com aviso.
Quando o manifesto existe, é sempre verificado por inteiro. A decisão não depende de
arquivos da árvore, que um PR poderia alterar.

Uso:
    python scripts/verify_release_manifest.py                       # CI e validação local
    python scripts/verify_release_manifest.py --require-approval     # deploy
    python scripts/verify_release_manifest.py --require-approval --tag v0.1.0
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

import yaml

from _common import ROOT, Report, publication_target, repository_role

MANIFEST_NAME = "RELEASE-MANIFEST.yml"
# Gerados pelo build, testes ou pelo próprio Git — não fazem parte da release.
IGNORED_PREFIXES = (".git/", "site/", ".cache/", ".pytest_cache/", "node_modules/", ".venv/", "venv/")
IGNORED_PARTS = {"__pycache__"}
FORBIDDEN_SUFFIXES = {".pdf", ".epub"}


def ignored(rel: str) -> bool:
    return rel.startswith(IGNORED_PREFIXES) or bool(IGNORED_PARTS.intersection(rel.split("/")))


REQUIRED_FIELDS = ("release", "version", "tag", "mode", "status", "scope", "approval", "source", "files")


def verify(root: Path, require_approval: bool = False, tag: str | None = None) -> Report:
    report = Report("Manifesto de release")
    path = root / MANIFEST_NAME
    if not path.is_file():
        report.error(f"{MANIFEST_NAME} ausente — a árvore pública só é gerada por scripts/export_release.py")
        return report
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        report.error(f"{MANIFEST_NAME}: conteúdo não é um mapeamento YAML")
        return report
    for key in REQUIRED_FIELDS:
        if key not in data:
            report.error(f"{MANIFEST_NAME}: campo obrigatório ausente: {key}")
    if report.errors:
        return report
    version = str(data["version"])
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        report.error(f"versão inválida: {version!r}")
    elif data["tag"] != f"v{version}":
        report.error(f"tag {data['tag']!r} não corresponde à versão {version}")
    if not isinstance(data["files"], dict) or not data["files"]:
        report.error("lista de arquivos (files) vazia ou inválida")
        return report
    curriculum = root / "curriculum" / "manifest.yml"
    if curriculum.is_file():
        releases = {str(r.get("id")): r for r in (yaml.safe_load(curriculum.read_text(encoding="utf-8")) or {})
                    .get("releases") or []}
        release = releases.get(str(data["release"]))
        if release is None:
            report.error(f"release {data['release']} ausente de curriculum/manifest.yml")
        elif str(publication_target(release)["version"]) != version:
            report.error(f"versão {version} difere da publicação registrada em curriculum/manifest.yml "
                         f"({publication_target(release)['version']})")

    files: dict[str, str] = data["files"] or {}
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    actual = {rel for rel in actual if rel != MANIFEST_NAME and not ignored(rel)}
    for rel in sorted(set(files) - actual):
        report.error(f"arquivo da release ausente: {rel}")
    for rel in sorted(actual - set(files)):
        report.error(f"arquivo fora da release: {rel}")
    for rel in sorted(set(files) & actual):
        if hashlib.sha256((root / rel).read_bytes()).hexdigest() != files[rel]:
            report.error(f"conteúdo diferente do exportado: {rel}")
    for rel in sorted(actual):
        if Path(rel).suffix.lower() in FORBIDDEN_SUFFIXES:
            report.error(f"{rel}: obra de terceiros não pode ser publicada")

    if tag and tag != data["tag"]:
        report.error(f"tag solicitada {tag} difere da release exportada {data['tag']}")
    if require_approval:
        approval = data["approval"] or {}
        if data["mode"] != "final":
            report.error("a árvore não foi gerada no modo final (exportação de publicação)")
        if data["status"] not in {"approved", "published"}:
            report.error(f"release com status {data['status']!r}: publicação exige 'approved'")
        if not approval.get("approved_by") or not approval.get("approved_on"):
            report.error("aprovação do mantenedor não registrada (approved_by, approved_on)")
        if not re.fullmatch(r"[0-9a-f]{40}", str(approval.get("approved_source_commit") or "")):
            report.error("commit de origem aprovado não registrado (approved_source_commit)")
        if (data["source"] or {}).get("dirty"):
            report.error("a exportação partiu de uma cópia com alterações não commitadas")
    print(f"  {data['release']} {data['tag']} ({data['mode']}): {len(files)} arquivos registrados")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--require-approval", action="store_true")
    parser.add_argument("--tag", help="tag da release a publicar (ex.: v0.1.0)")
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY"),
                        help="owner/repo em que a verificação roda (padrão: GITHUB_REPOSITORY)")
    args = parser.parse_args(argv)
    role = repository_role(args.repository)
    if not (args.root / MANIFEST_NAME).is_file() and role != "public" and not (args.require_approval or args.tag):
        where = "repositório de desenvolvimento" if role == "development" else "execução local"
        print(f"[OK] Manifesto de release — {MANIFEST_NAME} ausente ({where}; obrigatório no repositório público)")
        return 0
    return verify(args.root.resolve(), args.require_approval, args.tag).finish()


if __name__ == "__main__":
    sys.exit(main())
