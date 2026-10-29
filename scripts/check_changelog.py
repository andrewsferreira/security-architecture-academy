#!/usr/bin/env python3
"""Confere se o CHANGELOG.md descreve as publicações registradas no manifesto.

Contrato (desde a v0.2.1):

* ``## [Unreleased]`` é a primeira seção e reúne mudanças ainda sem versão.
* A versão em preparo (status ``in-review`` ou ``approved`` no manifesto) tem a
  própria seção, com o cabeçalho ``## [X.Y.Z] — não publicada``, já no commit
  submetido à aprovação. Nada da versão fica em *Unreleased*.
* A exportação final (``scripts/export_release.py --mode final``) troca esse
  cabeçalho pela data de aprovação (``approved_on``) — a data da release. Assim,
  a árvore pública nunca descreve a versão publicada como "não publicada", e o
  commit aprovado não precisa ser alterado depois.
* A exportação leva à árvore pública só a seção da versão exportada e as já
  publicadas: notas em *Unreleased* e seções pendentes de outras versões (por
  exemplo, de um nível ainda em desenvolvimento) ficam no desenvolvimento.
* Versões publicadas têm cabeçalho ``## [X.Y.Z] — AAAA-MM-DD`` com a data de
  ``approved_on``; versões planejadas não têm seção.
* A abertura de uma versão aprovada ou publicada não usa "em revisão",
  "em preparação" nem "não publicada".
* A seção da versão inicial de cada release informa o total cumulativo de aulas
  do escopo ("37 aulas"), conferido com o manifesto.

O texto das seções já publicadas é protegido por ``tests/test_changelog.py``
(SHA-256 de cada seção): o histórico de uma versão não é reescrito.

Regras (--rules):
    development  repositório de desenvolvimento e árvores candidatas: a versão em
                 preparo aparece como "não publicada".
    release      árvore de publicação: sem "não publicada", *Unreleased* vazio e a
                 versão da release com data. Com --tag, confere a versão.
    auto         (padrão) pela identidade do repositório — GITHUB_REPOSITORY,
                 definida pelo GitHub Actions, ou --repository: fora do repositório
                 de desenvolvimento valem as regras de publicação. Localmente, sem
                 GITHUB_REPOSITORY, valem as de publicação só em árvores exportadas no
                 modo final.

Uso:
    python scripts/check_changelog.py
    python scripts/check_changelog.py --release --tag v0.2.1
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from _common import ROOT, Report, load_manifest, release_publications, repository_role

CHANGELOG = "CHANGELOG.md"
PENDING_LABEL = "não publicada"
HEADER_RE = re.compile(r"^## \[(?P<version>[^\]]+)\](?: — (?P<label>.+?))?\s*$")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
VERSION_RE = re.compile(r"\d+\.\d+\.\d+")
NOT_RELEASED_RE = re.compile(r"em revisão|em preparação|não publicad[ao]", re.IGNORECASE)
REQUIRED_STATUSES = {"in-review", "approved", "published"}
FORBIDDEN_STATUSES = {"planned"}
SCOPE_KEYS = ("modules", "complements")


@dataclass
class Section:
    version: str
    label: str | None
    line: int
    lines: list[str] = field(default_factory=list)

    @property
    def text(self) -> str:
        return "\n".join(self.lines)

    @property
    def intro(self) -> str:
        """Parágrafo de abertura: texto antes da primeira subseção (###)."""
        out = []
        for line in self.lines:
            if line.startswith("### "):
                break
            out.append(line)
        return "\n".join(out).strip()


def parse(text: str) -> list[Section]:
    sections: list[Section] = []
    for number, line in enumerate(text.splitlines(), start=1):
        match = HEADER_RE.match(line.rstrip())
        if match:
            sections.append(Section(match["version"], match["label"], number))
        elif sections:
            sections[-1].lines.append(line)
    return sections


def release_changelog(text: str, version: str, date: dt.date | None = None) -> str:
    """CHANGELOG da árvore exportada para a versão ``version``.

    Esvazia *Unreleased* e remove seções pendentes de outras versões, que descrevem trabalho fora da
    release. Com ``date`` (exportação final), troca o cabeçalho pendente da versão pela data da release.
    Exige exatamente uma seção pendente da versão.
    """
    header = f"## [{version}] — {PENDING_LABEL}"
    if sum(1 for line in text.splitlines() if line.rstrip() == header) != 1:
        raise ValueError(f"CHANGELOG.md: a versão exportada precisa de exatamente uma seção '{header}' "
                         "(registrada antes da aprovação; ver scripts/check_changelog.py)")
    out: list[str] = []
    keep = True
    for line in text.splitlines(keepends=True):
        match = HEADER_RE.match(line.rstrip("\n"))
        if match:
            other_pending = match["label"] == PENDING_LABEL and match["version"] != version
            keep = not other_pending
            if match["version"] == "Unreleased":
                out.append(line)
                out.append("\n")
                keep = False
                continue
            if match["version"] == version and date is not None:
                line = f"## [{version}] — {date.isoformat()}\n"
        if keep:
            out.append(line)
    return "".join(out)


def section_body(text: str, version: str) -> str | None:
    """Corpo (sem o cabeçalho) da seção de uma versão, normalizado — usado na proteção do histórico."""
    for section in parse(text):
        if section.version == version:
            return section.text.strip() + "\n"
    return None


def _key(version: str) -> tuple[int, ...]:
    return tuple(int(x) for x in version.split("."))


def publications(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """Todas as publicações (versão inicial e correções) de todas as releases, com o id da release."""
    out = []
    for release in manifest.get("releases") or []:
        for record in release_publications(release):
            out.append({**record, "release": release})
    return out


def cumulative_lessons(manifest: dict[str, Any], release_id: str) -> int:
    """Total de aulas do escopo cumulativo até a release (inclusive)."""
    ids: set[str] = set()
    for release in manifest.get("releases") or []:
        for key in SCOPE_KEYS:
            ids.update(str(x) for x in release.get(key) or [])
        if str(release.get("id")) == release_id:
            break
    units = [u for key in SCOPE_KEYS for u in manifest.get(key) or [] if str(u.get("id")) in ids]
    return sum(len(u.get("lessons") or []) for u in units)


def _iso(value: Any) -> str | None:
    return value.isoformat() if isinstance(value, dt.date) else (str(value) if value else None)


def check(text: str, manifest: dict[str, Any], release_mode: bool, tag: str | None = None,
          target: str | None = None) -> Report:
    """Confere o CHANGELOG contra o manifesto.

    ``target`` é a versão de uma árvore exportada (a do RELEASE-MANIFEST.yml ou a de --tag). Numa árvore
    exportada só a versão-alvo e as publicadas têm seção: as demais publicações em preparo (outra
    correção, outra release em revisão) ficam no desenvolvimento, e a ausência delas não é erro.
    """
    target = target or (tag.removeprefix("v") if tag else None)
    report = Report(f"CHANGELOG ({'publicação' if release_mode else 'desenvolvimento'})")
    sections = parse(text)
    if not sections or sections[0].version != "Unreleased":
        report.error("a primeira seção deve ser '## [Unreleased]'")
    versioned = [s for s in sections if s.version != "Unreleased"]
    if release_mode:
        for s in sections:
            if s.version == "Unreleased" and s.text.strip():
                report.error(f"linha {s.line}: [Unreleased] precisa estar vazio na árvore de publicação "
                             "(o conteúdo da versão fica na seção própria)")

    seen: dict[str, Section] = {}
    for s in versioned:
        if not VERSION_RE.fullmatch(s.version):
            report.error(f"linha {s.line}: versão inválida [{s.version}]")
            continue
        if s.version in seen:
            report.error(f"linha {s.line}: seção [{s.version}] repetida")
        seen[s.version] = s
    ordered = [s.version for s in versioned if VERSION_RE.fullmatch(s.version)]
    if ordered != sorted(ordered, key=_key, reverse=True):
        report.error("as seções de versão devem estar em ordem decrescente: " + ", ".join(ordered))

    records = {str(r["version"]): r for r in publications(manifest)}
    for version in sorted(set(seen) - set(records), key=_key):
        report.error(f"[{version}]: versão sem publicação correspondente no manifesto")

    for version, record in records.items():
        status = record.get("status")
        section = seen.get(version)
        where = f"[{version}] ({record['release']['id']}, {status})"
        if status in FORBIDDEN_STATUSES:
            if section:
                report.error(f"{where}: versão planejada não pode ter seção no CHANGELOG")
            continue
        if target and status != "published" and version != target:
            # outra publicação em preparo: não faz parte desta árvore
            if section and (release_mode or section.label != PENDING_LABEL):
                report.error(f"{where}: seção de versão que não pertence a esta árvore (alvo: {target})")
            continue
        if status not in REQUIRED_STATUSES:  # in-development: seção opcional, sempre como pendente
            if section and section.label != PENDING_LABEL:
                report.error(f"{where}: versão em desenvolvimento só pode ter o cabeçalho "
                             f"'## [{version}] — {PENDING_LABEL}'")
            continue
        if section is None:
            report.error(f"{where}: seção ausente — a versão em preparo é registrada em '## [{version}] — "
                         f"{PENDING_LABEL}' antes da aprovação")
            continue
        approved_on = _iso(record.get("approved_on"))
        dated = bool(section.label and DATE_RE.fullmatch(section.label))
        if status == "published" or (status == "approved" and release_mode):
            if not dated:
                report.error(f"{where}: cabeçalho deve trazer a data da release (approved_on = {approved_on}), "
                             f"não {section.label!r}")
            elif approved_on and section.label != approved_on:
                report.error(f"{where}: data {section.label} difere de approved_on {approved_on}")
        elif release_mode:
            report.error(f"{where}: a árvore de publicação só contém versões aprovadas ou publicadas")
        elif section.label != PENDING_LABEL:
            report.error(f"{where}: versão ainda não publicada usa o cabeçalho '## [{version}] — {PENDING_LABEL}', "
                         f"não {section.label!r}")
        if status in {"approved", "published"} and NOT_RELEASED_RE.search(section.intro):
            report.error(f"{where}: a abertura descreve a versão como não publicada ou em revisão")
        if record["kind"] == "initial" and status in {"approved", "published"}:
            lessons = cumulative_lessons(manifest, str(record["release"]["id"]))
            if not re.search(rf"\b{lessons} aulas\b", section.text):
                report.error(f"{where}: a seção não informa o escopo cumulativo do manifesto ({lessons} aulas)")

    if release_mode:
        for s in versioned:
            if s.label == PENDING_LABEL:
                report.error(f"linha {s.line}: [{s.version}] marcada como '{PENDING_LABEL}' na árvore de publicação")
    if tag:
        version = tag.removeprefix("v")
        section = seen.get(version)
        if section is None or not (section.label and DATE_RE.fullmatch(section.label)):
            report.error(f"{tag}: a versão publicada precisa de seção datada no CHANGELOG")
    return report


def release_rules(repository: str | None, root: Path) -> bool:
    """Regras de publicação fora do repositório de desenvolvimento.

    No GitHub Actions, a identidade vem de GITHUB_REPOSITORY, definida pelo runner (não pelo conteúdo do
    PR). Fora dele (execução local), valem as regras de publicação apenas numa árvore exportada no
    modo final (RELEASE-MANIFEST.yml com ``mode: final``); candidatas seguem as do desenvolvimento.
    """
    role = repository_role(repository)
    if role == "local":
        path = root / "RELEASE-MANIFEST.yml"
        if not path.is_file():
            return False
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        return isinstance(data, dict) and data.get("mode") == "final"
    return role != "development"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--rules", choices=["auto", "development", "release"], default="auto",
                        help="regras a aplicar (padrão: pela identidade do repositório)")
    parser.add_argument("--release", action="store_true", help="atalho para --rules release")
    parser.add_argument("--tag", help="versão publicada (ex.: v0.2.1): exige seção datada")
    parser.add_argument("--target", help="versão da árvore exportada (padrão: a do RELEASE-MANIFEST.yml)")
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY"),
                        help="owner/repo (padrão: GITHUB_REPOSITORY)")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    rules = "release" if args.release else args.rules
    release_mode = rules == "release" or (rules == "auto" and release_rules(args.repository, root))
    text = (root / CHANGELOG).read_text(encoding="utf-8")
    manifest = load_manifest(root / "curriculum" / "manifest.yml")
    target = args.target or exported_version(root)
    return check(text, manifest, release_mode, args.tag, target).finish()


def exported_version(root: Path) -> str | None:
    """Versão de uma árvore exportada (RELEASE-MANIFEST.yml); None no repositório de desenvolvimento."""
    path = root / "RELEASE-MANIFEST.yml"
    if not path.is_file():
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return str(data["version"]) if isinstance(data, dict) and data.get("version") else None


if __name__ == "__main__":
    sys.exit(main())
