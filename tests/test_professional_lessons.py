"""Aulas do Professional (Módulos 5 a 15) revisadas: modelo de 14 elementos e exercício de decisão completo.

A aritmética das matrizes é conferida por scripts/check_decision_matrices.py. Aqui se verifica, nas aulas já
revisadas, a estrutura exigida pelo modelo de conteúdo: as seções do padrão (inclusive "Controles e padrões
relevantes"), critérios de aceite em "Como validar" e um exercício de decisão com matriz ponderada,
alternativas, critérios, pesos justificados, recomendação coerente com a matriz, risco residual e condições
que mudariam a escolha.

``REVIEWED`` cresce à medida que cada módulo termina a revisão (ver docs/internal/professional-worklog.md);
ao fim do Professional, contém M05 a M15.
"""

from __future__ import annotations

import re

import pytest

from _common import DOCS, load_manifest
from test_level1_matrices import exercise, letter, matrices

MANIFEST = load_manifest()
MODULES = {m["id"]: m for m in MANIFEST["modules"]}
REVIEWED = ["M05", "M06", "M07", "M08"]
SECTIONS = (
    "Resumo", "Conceito", "Fundamentos técnicos", "Exemplo empresarial", "Arquitetura tradicional",
    "Controles e padrões relevantes", "Aplicabilidade", "Como especificar", "Trade-offs", "Como validar",
    "Como apresentar", "Checklist", "Questões de compreensão", "Exercício de tomada de decisão",
    "Pontos-chave", "Referências", "Revisão",
)


def lesson_files():
    for mid in REVIEWED:
        mod = MODULES[mid]
        if mod.get("status") == "planned" and not mod.get("path"):
            continue  # árvore pública de uma release anterior: o módulo ainda não foi exportado
        folder = DOCS / mod["path"].rsplit("/", 1)[0]
        for lesson in mod["lessons"]:
            assert lesson.get("file"), f"{lesson['id']} sem arquivo em módulo revisado"
            yield lesson["id"], folder / lesson["file"]


LESSONS = list(lesson_files())
IDS = [lid for lid, _ in LESSONS]


@pytest.mark.parametrize("lid,path", LESSONS, ids=IDS)
def test_lesson_follows_the_fourteen_element_model(lid, path):
    headings = re.findall(r"^## (.+)$", path.read_text(encoding="utf-8"), re.M)
    missing = [s for s in SECTIONS if not any(h.startswith(s) for h in headings)]
    assert not missing, f"{lid}: seções ausentes {missing}"
    order = [next(i for i, h in enumerate(headings) if h.startswith(s)) for s in SECTIONS]
    assert order == sorted(order), f"{lid}: seções fora da ordem do modelo"


@pytest.mark.parametrize("lid,path", LESSONS, ids=IDS)
def test_controls_section_cites_verifiable_references(lid, path):
    text = path.read_text(encoding="utf-8")
    section = text.split("## Controles e padrões relevantes", 1)[1].split("\n## ", 1)[0]
    rows = [r for r in section.splitlines() if r.startswith("| ") and not r.startswith("|:")][1:]
    assert len(rows) >= 3, f"{lid}: menos de três controles"
    for row in rows:
        assert row.rstrip().endswith("|") and row.count("|") >= 4, f"{lid}: linha de controle malformada"


@pytest.mark.parametrize("lid,path", LESSONS, ids=IDS)
def test_validation_has_acceptance_criteria(lid, path):
    text = path.read_text(encoding="utf-8")
    section = text.split("## Como validar", 1)[1].split("\n## ", 1)[0]
    assert re.search(r"[Cc]ritérios de aceite", section), f"{lid}: 'Como validar' sem critérios de aceite"


@pytest.mark.parametrize("lid,path", LESSONS, ids=IDS)
def test_exercise_has_complete_weighted_matrix(lid, path):
    section = exercise(path.read_text(encoding="utf-8"))
    found = matrices(section)
    assert found, f"{lid}: exercício sem matriz ponderada"
    header, rows = found[0]
    weight = header.index("Peso")
    assert len(header[weight + 1:]) >= 2, f"{lid}: menos de duas alternativas"
    assert len(rows[:-1]) >= 3, f"{lid}: menos de três critérios"
    for required in ("Pesos", "O que mudaria a decisão"):
        assert required in section, f"{lid}: falta '{required}'"
    assert re.search(r"[Rr]isco residual|[Rr]esidual", section), f"{lid}: falta o risco residual"


@pytest.mark.parametrize("lid,path", LESSONS, ids=IDS)
def test_recommendation_matches_matrix(lid, path):
    section = exercise(path.read_text(encoding="utf-8"))
    header, rows = matrices(section)[0]
    weight = header.index("Peso")
    letters = [letter(o) for o in header[weight + 1:]]
    totals = dict(zip(letters, (float(c) for c in rows[-1][weight + 1:])))
    best = {k for k, v in totals.items() if v == max(totals.values())}
    match = re.search(r"[Rr]ecomendação: ([A-D])\b", section)
    assert match, f"{lid}: recomendação sem alternativa identificada"
    assert match.group(1) in best or "empate" in section.lower(), (
        f"{lid}: recomenda {match.group(1)}, mas a matriz favorece {best}")


def test_matrix_judgment_note_in_module_indexes():
    for mid in REVIEWED:
        if not MODULES[mid].get("path"):
            continue
        text = (DOCS / MODULES[mid]["path"]).read_text(encoding="utf-8")
        assert "matriz de decisão ponderada" in text and "julgamento profissional" in text, mid
