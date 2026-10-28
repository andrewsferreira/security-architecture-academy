"""Exercícios de decisão do Nível 1 (Módulos 3 e 4): matriz ponderada completa e coerente com a recomendação.

A aritmética de todas as matrizes é conferida por scripts/check_decision_matrices.py; aqui se verifica a
estrutura pedagógica exigida pelo modelo de conteúdo — alternativas, critérios, pesos justificados,
recomendação, risco residual e condições que mudariam a escolha — e que a recomendação não contradiz a
matriz sem explicação.
"""

from __future__ import annotations

import re

import pytest

from _common import DOCS, load_manifest

MANIFEST = load_manifest()
MODULES = {m["id"]: m for m in MANIFEST["modules"]}
LEVEL1_NEW = ["M03", "M04"]


def lesson_files():
    for mid in LEVEL1_NEW:
        mod = MODULES[mid]
        folder = DOCS / mod["path"].rsplit("/", 1)[0]
        for lesson in mod["lessons"]:
            if lesson.get("file"):
                yield lesson["id"], folder / lesson["file"]


LESSONS = list(lesson_files())


def exercise(text: str) -> str:
    return text.split("## Exercício de tomada de decisão", 1)[1].split("\n## ", 1)[0]


def matrices(section: str) -> list[tuple[list[str], list[list[str]]]]:
    found, block = [], []
    for line in section.splitlines() + [""]:
        if line.strip().startswith("|"):
            block.append([c.strip().replace("*", "") for c in line.strip().strip("|").split("|")])
        elif block:
            header = block[0]
            if "Peso" in header and block[-1][0].startswith("Total ponderado"):
                found.append((header, block[2:]))
            block = []
    return found


def letter(option: str) -> str:
    match = re.match(r"([A-D]) —", option)
    assert match, f"coluna de alternativa sem letra: {option!r}"
    return match.group(1)


def test_all_level1_lessons_present():
    assert len(LESSONS) == 15


@pytest.mark.parametrize("lid,path", LESSONS, ids=[lid for lid, _ in LESSONS])
def test_exercise_has_complete_weighted_matrix(lid, path):
    section = exercise(path.read_text(encoding="utf-8"))
    found = matrices(section)
    assert found, f"{lid}: exercício sem matriz ponderada"
    header, rows = found[0]
    options = header[header.index("Peso") + 1:]
    criteria = rows[:-1]
    assert len(options) >= 2, f"{lid}: menos de duas alternativas"
    assert len(criteria) >= 3, f"{lid}: menos de três critérios"
    assert all(float(r[header.index("Peso")]) > 0 for r in criteria)
    for required in ("Pesos", "O que mudaria a decisão"):
        assert required in section, f"{lid}: falta '{required}'"
    assert re.search(r"[Rr]isco residual|[Rr]esidual", section), f"{lid}: falta o risco residual"


@pytest.mark.parametrize("lid,path", LESSONS, ids=[lid for lid, _ in LESSONS])
def test_recommendation_matches_matrix_or_explains(lid, path):
    section = exercise(path.read_text(encoding="utf-8"))
    header, rows = matrices(section)[0]
    weight = header.index("Peso")
    letters = [letter(o) for o in header[weight + 1:]]
    totals = dict(zip(letters, (float(c) for c in rows[-1][weight + 1:])))
    best = {k for k, v in totals.items() if v == max(totals.values())}
    match = re.search(r"[Rr]ecomend\w*[^\n]{0,40}?\b([A-D])\b(?:\s+e\s+([A-D])\b)?", section)
    assert match, f"{lid}: recomendação sem alternativa identificada"
    chosen = {g for g in match.groups() if g}
    if len(best) > 1:
        assert "empate" in section.lower() or best <= chosen, f"{lid}: empate sem explicação"
    assert best & chosen, f"{lid}: recomenda {chosen}, mas a matriz favorece {best} sem explicação"


def test_matrix_judgment_note_in_module_indexes():
    for mid in LEVEL1_NEW:
        text = (DOCS / MODULES[mid]["path"]).read_text(encoding="utf-8")
        assert "matriz de decisão ponderada" in text and "julgamento profissional" in text, mid
