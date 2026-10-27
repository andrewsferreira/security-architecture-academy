#!/usr/bin/env python3
"""Confere a aritmética das matrizes de decisão publicadas no conteúdo.

Uma matriz de decisão é uma tabela Markdown cujo cabeçalho tem a coluna
"Peso" e cuja última linha começa com "Total ponderado". Para cada
alternativa (colunas após "Peso"), o script recalcula Σ(peso × nota) e
compara com o total declarado. Matrizes com notas não numéricas são ignoradas.

Uso:
    python scripts/check_decision_matrices.py
"""

from __future__ import annotations

import re

from _common import DOCS, Report, exit_with

ROW_RE = re.compile(r"^\s*\|(.+)\|\s*$")
NUMBER_RE = re.compile(r"-?\d+(?:[.,]\d+)?")


def cells(line: str) -> list[str]:
    match = ROW_RE.match(line)
    return [c.strip() for c in match.group(1).split("|")] if match else []


def number(text: str) -> float | None:
    clean = text.replace("*", "").strip()
    match = NUMBER_RE.fullmatch(clean)
    return float(clean.replace(",", ".")) if match else None


def tables(lines: list[str]):
    block: list[tuple[int, list[str]]] = []
    for idx, line in enumerate(lines, start=1):
        row = cells(line)
        if row:
            block.append((idx, row))
        elif block:
            yield block
            block = []
    if block:
        yield block


def main() -> None:
    report = Report("Matrizes de decisão")
    checked = 0
    for page in sorted(DOCS.rglob("*.md")):
        rel = page.relative_to(DOCS.parent).as_posix()
        for block in tables(page.read_text(encoding="utf-8").splitlines()):
            header = [h.replace("*", "") for h in block[0][1]]
            if "Peso" not in header or not block[-1][1][0].replace("*", "").startswith("Total ponderado"):
                continue
            weight_col = header.index("Peso")
            options = header[weight_col + 1:]
            totals = [0.0] * len(options)
            valid = True
            for _, row in block[2:-1]:
                weight = number(row[weight_col])
                scores = [number(c) for c in row[weight_col + 1:]]
                if weight is None or any(s is None for s in scores) or len(scores) != len(options):
                    valid = False
                    break
                totals = [t + weight * s for t, s in zip(totals, scores)]  # type: ignore[operator]
            if not valid:
                continue
            checked += 1
            line_no, total_row = block[-1]
            declared = [number(c) for c in total_row[weight_col + 1:]]
            for name, expected, got in zip(options, totals, declared):
                if got is None or abs(expected - got) > 0.01:
                    report.error(f"{rel}:{line_no}: total de '{name}' declarado {got}, calculado {expected:g}")
    print(f"  {checked} matrizes verificadas")
    exit_with(report)


if __name__ == "__main__":
    main()
