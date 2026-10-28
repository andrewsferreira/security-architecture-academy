"""Rubricas das avaliações integradoras: coerentes com a rubrica padrão e com a regra de aprovação."""

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
