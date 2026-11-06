#!/usr/bin/env python3
"""Confere os selos de status escritos à mão nas páginas com o status do item no manifesto.

Os índices de atividades (avaliações, casos, laboratórios, modelos), a matriz de cobertura e os índices de
módulo têm selos ``<span class="saa-status saa-status--…">`` fora dos blocos gerados. Cada selo precisa
corresponder ao status do item no manifesto da árvore — no desenvolvimento, o manifesto de trabalho; na
árvore pública, o manifesto transformado pela exportação, em que tudo fora do escopo da release é
``planned``. Assim, nenhuma página anuncia como publicado (ou em revisão) algo que a release não publica.

O item de cada linha é identificado, nesta ordem, pelo link para a página do item, pelo ID técnico
(`` `CS-B` `` ou ``| CS-B |``), pelo título do item na primeira coluna ou, nas páginas de módulo, pelo
próprio módulo. Linhas de legenda (selo na primeira coluna) ficam de fora. Linha sem item identificado
só pode ter selo ``planned``: não afirma disponibilidade.

Uso:
    python scripts/check_status_badges.py
"""

from __future__ import annotations

import posixpath
import re
from pathlib import Path
from typing import Any

from _common import ROOT, Report, exit_with, load_manifest

BADGE_RE = re.compile(r'saa-status--(planned|draft|in-review|published|deprecated)')
GENERATED_BLOCK_RE = re.compile(r"<!-- ([\w-]+):start -->.*?<!-- \1:end -->", re.S)
LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)\s]*)?\)")
ID_RE = re.compile(r"`([A-Z]{1,4}\d{0,2}(?:-[A-Z0-9]+)*(?:-L\d{2})?)`|\|\s*([A-Z]{2,4}-[A-Z0-9-]+)\s*\|")
COLLECTIONS = ("case_studies", "labs", "assessments", "artifacts")


def unit_dir(unit: dict[str, Any]) -> str:
    uid = str(unit["id"])
    return f"docs/modules/{uid[1:]}-{unit['slug']}" if uid.startswith("M") else f"docs/complements/{unit['slug']}"


def item_maps(manifest: dict[str, Any]) -> tuple[dict[str, str], dict[str, str], dict[str, str], dict[str, str]]:
    """(caminho → id, id → status, título normalizado → id, pasta do módulo → id)."""
    by_path, status, by_title, by_dir = {}, {}, {}, {}
    for key in ("modules", "complements"):
        for unit in manifest.get(key) or []:
            uid = str(unit["id"])
            status[uid] = str(unit.get("status"))
            base = unit_dir(unit)
            by_dir[base + "/"] = uid
            by_path[base + "/index.md"] = uid
            for lesson in unit.get("lessons") or []:
                status[str(lesson["id"])] = str(lesson.get("status"))
                if lesson.get("file"):
                    by_path[f"{base}/{lesson['file']}"] = str(lesson["id"])
    for key in COLLECTIONS:
        for item in manifest.get(key) or []:
            iid = str(item["id"])
            status[iid] = str(item.get("status"))
            by_title[normalize(item.get("title") or "")] = iid
            for field in ("path", "answers"):
                if item.get(field):
                    by_path[f"docs/{item[field]}"] = iid
    return by_path, status, by_title, by_dir


def normalize(text: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"^Caso\s+", "", text.strip())
    return re.sub(r"\s+", " ", text).split(" (")[0].strip().lower()


def resolve(page: str, line: str, maps: tuple) -> str | None:
    by_path, status, by_title, by_dir = maps
    for target in LINK_RE.findall(line):
        if target.startswith(("http://", "https://")):
            continue
        path = posixpath.normpath(posixpath.join(posixpath.dirname(page), target))
        if path in by_path:
            return by_path[path]
    for a, b in ID_RE.findall(line):
        if (a or b) in status:
            return a or b
    cells = [c for c in line.split("|") if c.strip()]
    if cells:
        title = normalize(cells[0])
        for known, iid in by_title.items():
            if title and (known == title or known.startswith(title) or title.startswith(known)):
                return iid
    return next((uid for base, uid in by_dir.items() if page == base + "index.md"), None)


def check(docs: Path, manifest: dict[str, Any], root: Path = ROOT) -> Report:
    report = Report("Selos de status escritos nas páginas × manifesto")
    maps = item_maps(manifest)
    for page in sorted(docs.rglob("*.md")):
        rel = page.relative_to(root).as_posix()
        if rel.startswith("docs/internal/"):
            continue
        text = GENERATED_BLOCK_RE.sub(lambda m: "\n" * m.group(0).count("\n"), page.read_text(encoding="utf-8"))
        for number, line in enumerate(text.splitlines(), 1):
            badges = BADGE_RE.findall(line)
            if not badges or line.lstrip().startswith("| <span class=\"saa-status"):
                continue  # sem selo, ou legenda de status (selo na primeira coluna)
            item = resolve(rel, line, maps)
            if item is None:
                if any(b != "planned" for b in badges):
                    report.error(f"{rel}:{number}: selo {badges[0]!r} sem item identificável no manifesto")
                continue
            expected = maps[1][item]
            if badges[0] != expected:
                report.error(f"{rel}:{number}: {item} com selo {badges[0]!r}, mas o manifesto diz {expected!r}")
    return report


def main() -> None:
    exit_with(check(ROOT / "docs", load_manifest()))


if __name__ == "__main__":
    main()
