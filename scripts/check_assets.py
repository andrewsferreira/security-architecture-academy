#!/usr/bin/env python3
"""Verifica a integridade dos assets de marca e diagramas.

- Presença de todos os assets obrigatórios de assets/branding/.
- SVGs bem formados, com viewBox e <title> (acessibilidade).
- Dimensões e tamanho dos PNGs (Social Preview do GitHub: 1280×640, < 1 MB).
- Cópia em docs/assets/branding/ idêntica à fonte em assets/branding/.
- Fontes de diagramas (assets/diagrams/*.mmd) não vazias e com cabeçalho de descrição.

Uso:
    python scripts/check_assets.py
"""

from __future__ import annotations

import hashlib
import struct
import xml.etree.ElementTree as ET
from pathlib import Path

from _common import ROOT, Report, exit_with

BRANDING = ROOT / "assets" / "branding"
DOCS_BRANDING = ROOT / "docs" / "assets" / "branding"
DIAGRAMS = ROOT / "assets" / "diagrams"
SVG_NS = "{http://www.w3.org/2000/svg}"

REQUIRED = [
    "logo.svg", "logo-dark.svg", "logo-light.svg", "icon.svg", "banner.svg", "banner-dark.svg",
    "banner-light.svg", "social-preview.png", "favicon.png",
]
PNG_RULES = {  # nome: (largura, altura, bytes máximos)
    "social-preview.png": (1280, 640, 1_000_000),
    "favicon.png": (64, 64, 50_000),
    "apple-touch-icon.png": (180, 180, 100_000),
}
MAX_SVG_BYTES = 200_000


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        raise ValueError("não é um PNG válido")
    return struct.unpack(">II", head[16:24])


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    report = Report("Assets")

    for name in REQUIRED:
        if not (BRANDING / name).is_file():
            report.error(f"asset obrigatório ausente: assets/branding/{name}")

    svgs = sorted(BRANDING.glob("*.svg")) + sorted((ROOT / "docs" / "assets" / "images").glob("*.svg"))
    for svg in svgs:
        rel = svg.relative_to(ROOT)
        try:
            root = ET.parse(svg).getroot()
        except ET.ParseError as exc:
            report.error(f"{rel}: SVG malformado ({exc})")
            continue
        if root.tag != f"{SVG_NS}svg":
            report.error(f"{rel}: elemento raiz não é <svg>")
        if "viewBox" not in root.attrib:
            report.error(f"{rel}: sem viewBox (não escala corretamente)")
        if root.find(f"{SVG_NS}title") is None:
            report.error(f"{rel}: sem <title> (texto alternativo para leitores de tela)")
        if svg.stat().st_size > MAX_SVG_BYTES:
            report.warn(f"{rel}: {svg.stat().st_size // 1024} KiB — considere simplificar")
        if root.find(f".//{SVG_NS}text") is not None:
            report.warn(f"{rel}: contém <text>; a renderização depende de fontes do visualizador")

    for name, (w, h, max_bytes) in PNG_RULES.items():
        path = BRANDING / name
        if not path.is_file():
            continue
        try:
            size = png_size(path)
        except ValueError as exc:
            report.error(f"assets/branding/{name}: {exc}")
            continue
        if size != (w, h):
            report.error(f"assets/branding/{name}: {size[0]}×{size[1]} (esperado {w}×{h})")
        if path.stat().st_size > max_bytes:
            report.error(f"assets/branding/{name}: {path.stat().st_size} bytes (máximo {max_bytes})")

    for src in sorted(BRANDING.iterdir()):
        if src.suffix not in {".svg", ".png"}:
            continue
        copy = DOCS_BRANDING / src.name
        if not copy.is_file():
            report.error(f"docs/assets/branding/{src.name} ausente — execute `make brand-sync`")
        elif sha256(copy) != sha256(src):
            report.error(f"docs/assets/branding/{src.name} diverge da fonte — execute `make brand-sync`")
    for copy in sorted(DOCS_BRANDING.glob("*")):
        if not (BRANDING / copy.name).exists():
            report.error(f"docs/assets/branding/{copy.name} não existe em assets/branding (fonte única)")

    sources = sorted(DIAGRAMS.glob("*.mmd"))
    if not sources:
        report.error("nenhuma fonte de diagrama em assets/diagrams/")
    for src in sources:
        text = src.read_text(encoding="utf-8").strip()
        if not text:
            report.error(f"{src.relative_to(ROOT)}: arquivo vazio")
        elif "accDescr" not in text:
            report.error(f"{src.relative_to(ROOT)}: sem accDescr (descrição acessível obrigatória)")

    print(f"  {len(svgs)} SVGs, {len(PNG_RULES)} PNGs, {len(sources)} fontes de diagrama verificados")
    exit_with(report)


if __name__ == "__main__":
    main()
