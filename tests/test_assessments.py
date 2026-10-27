"""Coerência entre enunciados de avaliações e gabaritos (questões objetivas)."""

from __future__ import annotations

import re

import pytest

from _common import DOCS

QUESTION_RE = re.compile(r"^\*\*([A-C]?\d+)\.\*\*[^\n]*\n\n((?:- \([a-d]\) [^\n]*\n)+)", re.MULTILINE)
DETAIL_RE = re.compile(r"^\*\*([A-C]?\d+) — \(([a-d])\)", re.MULTILINE)
TABLE_RE = re.compile(r"^\| ([A-C]?\d+) \| \*\*([a-d])\*\* \|", re.MULTILINE)
INLINE_RE = re.compile(r"([A-C]\d) \*\*([a-d])\*\*")

OBJECTIVE = ["diagnostic-fundamentals", "m00-foundations", "m01-security-fundamentals", "m02-security-architecture"]


def available() -> list[str]:
    return [name for name in OBJECTIVE if (DOCS / "assessments" / f"{name}.md").is_file()]


@pytest.mark.parametrize("name", available())
def test_answer_keys_match_questions(name):
    questions = QUESTION_RE.findall((DOCS / "assessments" / f"{name}.md").read_text(encoding="utf-8"))
    key = (DOCS / "assessments" / "answers" / f"{name}.md").read_text(encoding="utf-8")
    detail = dict(DETAIL_RE.findall(key))
    summary = dict(TABLE_RE.findall(key)) or dict(INLINE_RE.findall(key))
    assert questions, "nenhuma questão objetiva encontrada"
    for qid, options in questions:
        letters = re.findall(r"^- \(([a-d])\)", options, re.MULTILINE)
        assert letters == ["a", "b", "c", "d"], f"{qid}: alternativas incompletas"
        assert qid in detail, f"{qid}: sem resposta comentada"
        assert summary.get(qid) == detail[qid], f"{qid}: resumo e resposta comentada divergem"
    assert set(detail) == {q for q, _ in questions}
    counts = {letter: list(detail.values()).count(letter) for letter in "abcd"}
    assert min(counts.values()) >= 2, f"respostas corretas mal distribuídas: {counts}"
