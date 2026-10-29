"""Rubricas das avaliações (integradoras e AS-M02): coerentes com a rubrica padrão e com a regra de aprovação."""

from __future__ import annotations

import math
import re

import pytest

from _common import DOCS

TABLE = re.compile(r"^\| Tarefa \| Pontos \| Excelente \| Adequado \| Insuficiente \|.*?\n\|[-:| ]+\|\n((?:\|.*\|\n)+)", re.M)
APPROVAL = re.compile(r"\*\*Aprovação:\*\* (\d+) pontos ou mais")


def rubric_pages():
    pages = []
    for path in sorted((DOCS / "assessments").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if TABLE.search(text):
            pages.append(path)
    return pages


def parse(path):
    text = path.read_text(encoding="utf-8")
    rows = []
    for line in TABLE.search(text).group(1).strip().splitlines():
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(tuple(int(c) for c in cells[1:5]))
    return rows, int(APPROVAL.search(text).group(1))


def test_integrative_assessments_have_rubric_tables():
    names = {p.name for p in rubric_pages()}
    assert {"fundamentals-final.md", "level-1-integrative.md"} <= names


@pytest.mark.parametrize("path", rubric_pages(), ids=lambda p: p.name)
def test_rubric_is_consistent_with_standard_and_approval(path):
    rows, approval = parse(path)
    assert sum(points for points, *_ in rows) == 100
    for points, excellent, adequate, insufficient in rows:
        assert excellent == points
        # Rubrica padrão: Adequado = 70% do critério (arredondado para cima em pontos inteiros).
        assert adequate >= math.ceil(0.7 * points), (path.name, points, adequate)
        assert insufficient < adequate < excellent
    # Quem é Adequado em todas as tarefas precisa alcançar a nota de aprovação.
    assert sum(adequate for _, _, adequate, _ in rows) >= approval, path.name


def test_regression_as_fund_adequate_everywhere_passes():
    rows, approval = parse(DOCS / "assessments" / "fundamentals-final.md")
    assert sum(r[2] for r in rows) == 71 and approval == 70


# ------------------------------------------------------------------ AS-M02 (avaliação do Módulo 2)
M02_ROW = re.compile(r"^\| \*\*(\d+) \((\d+) pt\)\*\* \|[^|]*\((\d+)\) \|[^|]*\((\d+)\) \|[^|]*\((\d+)\) \|$", re.M)
PART1 = re.compile(r"\*\*Parte 1\*\* — (\w+) questões .*? Vale (\d+) pontos \((\d+) cada\)")


def m02_rubric():
    rows = [tuple(int(x) for x in m) for m in
            M02_ROW.findall((DOCS / "assessments" / "answers" / "m02-security-architecture.md").read_text(encoding="utf-8"))]
    page = (DOCS / "assessments" / "m02-security-architecture.md").read_text(encoding="utf-8")
    part1 = PART1.search(page)
    return rows, int(part1.group(2)), int(part1.group(3)), int(APPROVAL.search(page).group(1))


def test_as_m02_rubric_follows_standard_rubric():
    rows, part1_points, per_question, approval = m02_rubric()
    assert [r[0] for r in rows] == [1, 2, 3, 4]
    assert sum(r[1] for r in rows) + part1_points == 100 and approval == 70
    for _, points, excellent, adequate, insufficient in rows:
        assert excellent == points
        assert adequate >= math.ceil(0.7 * points), (points, adequate)
        assert insufficient < adequate < excellent


def test_regression_as_m02_seven_correct_and_adequate_everywhere_passes():
    """Antes da v0.2.1: 7 acertos na Parte 1 (35) + Adequado nas quatro tarefas (34) = 69, reprovado."""
    rows, part1_points, per_question, approval = m02_rubric()
    assert [r[3] for r in rows] == [9, 7, 9, 12]
    assert [r[1] for r in rows] == [12, 10, 12, 16]  # pontuação máxima preservada
    total = 7 * per_question + sum(r[3] for r in rows)
    assert total == 72 and total >= approval
