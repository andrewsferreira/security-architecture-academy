#!/usr/bin/env python3
"""Verifica o contraste WCAG 2.x dos pares de cores do Design System.

Os tokens são lidos de docs/assets/stylesheets/extra.css (fonte da verdade),
de modo que uma mudança de cor que reduza o contraste abaixo de AA (4.5:1)
falha no CI.

Uso:
    python scripts/check_contrast.py [--markdown]
"""

from __future__ import annotations

import argparse
import re

from _common import DOCS, Report, exit_with

CSS = DOCS / "assets" / "stylesheets" / "extra.css"
AA = 4.5

# (contexto, descrição, token de texto, token de fundo)
PAIRS = [
    ("Light", "Texto", "default:--saa-text", "default:--saa-bg"),
    ("Light", "Texto secundário", "default:--saa-text-muted", "default:--saa-bg"),
    ("Light", "Link / Primary", "default:--saa-primary", "default:--saa-bg"),
    ("Light", "Accent", "default:--saa-accent", "default:--saa-bg"),
    ("Light", "Success", "default:--saa-success", "default:--saa-bg"),
    ("Light", "Warning", "default:--saa-warning", "default:--saa-bg"),
    ("Light", "Error", "default:--saa-error", "default:--saa-bg"),
    ("Light", "Texto secundário sobre surface", "default:--saa-text-muted", "default:--saa-surface"),
    ("Light", "Texto sobre Navy 900 (botão primário)", "#ffffff", "root:--saa-navy-900"),
    # Item ativo da navegação: accent sobre --md-accent-fg-color--transparent (accent a 10% sobre branco)
    ("Light", "Accent sobre item ativo da navegação", "default:--saa-accent", "#e6f1f3"),
    ("Dark", "Texto", "slate:--saa-text", "slate:--saa-bg"),
    ("Dark", "Texto secundário", "slate:--saa-text-muted", "slate:--saa-bg"),
    ("Dark", "Link / Primary", "slate:--saa-primary", "slate:--saa-bg"),
    ("Dark", "Accent", "slate:--saa-accent", "slate:--saa-bg"),
    ("Dark", "Success", "slate:--saa-success", "slate:--saa-bg"),
    ("Dark", "Warning", "slate:--saa-warning", "slate:--saa-bg"),
    ("Dark", "Error", "slate:--saa-error", "slate:--saa-bg"),
    ("Dark", "Texto secundário sobre surface", "slate:--saa-text-muted", "slate:--saa-surface-raised"),
]


def parse_tokens() -> dict[str, dict[str, str]]:
    css = CSS.read_text(encoding="utf-8")
    scopes = {
        "root": r":root\s*\{(.*?)\}",
        "default": r'\[data-md-color-scheme="default"\]\s*\{(.*?)\}',
        "slate": r'\[data-md-color-scheme="slate"\]\s*\{(.*?)\}',
    }
    tokens: dict[str, dict[str, str]] = {}
    for scope, pattern in scopes.items():
        block = re.search(pattern, css, re.DOTALL)
        tokens[scope] = dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", block.group(1))) if block else {}
    return tokens


def resolve(ref: str, tokens: dict[str, dict[str, str]]) -> str:
    if ref.startswith("#"):
        return ref
    scope, name = ref.split(":", 1)
    value = tokens[scope].get(name) or tokens["root"].get(name)
    if value is None:
        raise KeyError(ref)
    value = value.strip()
    var = re.fullmatch(r"var\((--[\w-]+)\)", value)
    return resolve(f"{scope}:{var.group(1)}", tokens) if var else value


def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    channels = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(fg: str, bg: str) -> float:
    a, b = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--markdown", action="store_true", help="imprime a tabela em Markdown")
    args = parser.parse_args()
    tokens = parse_tokens()
    report = Report("Contraste WCAG (mínimo AA 4.5:1)")
    rows = []
    for ctx, label, fg_ref, bg_ref in PAIRS:
        try:
            fg, bg = resolve(fg_ref, tokens), resolve(bg_ref, tokens)
        except KeyError as exc:
            report.error(f"token não encontrado em extra.css: {exc}")
            continue
        r = ratio(fg, bg)
        level = "AAA" if r >= 7 else "AA" if r >= AA else "insuficiente"
        rows.append(f"| {ctx} | {label} | `{fg}` / `{bg}` | {r:.1f}:1 | {level} |")
        if r < AA:
            report.error(f"{ctx} · {label}: {r:.2f}:1 ({fg} sobre {bg})")
    if args.markdown:
        print("| Modo | Par | Cores | Contraste | Nível |\n|:---|:---|:---|:---|:---|")
        print("\n".join(rows))
    exit_with(report)


if __name__ == "__main__":
    main()
