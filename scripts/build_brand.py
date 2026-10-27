#!/usr/bin/env python3
"""Gera os assets de identidade visual da Security Architecture Academy.

Todos os SVGs são produzidos programaticamente, com o texto convertido em
curvas (paths). Isso garante renderização idêntica no GitHub, no portal e em
qualquer visualizador, sem depender de fontes instaladas no computador de quem
abre o arquivo.

Uso (apenas mantenedores — requer as fontes Inter em formato OTF/TTF):

    pip install -r requirements-brand.txt
    python scripts/build_brand.py

Variáveis de ambiente:
    BRAND_FONT_DIR  Diretório com Inter-*.otf e InterDisplay-*.otf
                    (padrão: /usr/share/fonts/opentype/inter)

Saídas:
    assets/branding/*.svg, assets/branding/*.png
    docs/assets/branding/*  (cópia sincronizada usada pelo portal)
    docs/assets/images/hero-architecture-{light,dark}.svg
"""

from __future__ import annotations

import os
import shutil
from dataclasses import dataclass
from pathlib import Path

import cairosvg
import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "branding"
DOCS_BRAND = ROOT / "docs" / "assets" / "branding"
DOCS_IMAGES = ROOT / "docs" / "assets" / "images"
FONT_DIR = Path(os.environ.get("BRAND_FONT_DIR", "/usr/share/fonts/opentype/inter"))

# --------------------------------------------------------------------------
# Design tokens (fonte da verdade: docs/internal/design-system.md)
# --------------------------------------------------------------------------
NAVY_950 = "#081426"
NAVY_900 = "#0C1D36"
NAVY_800 = "#132B4F"
NAVY_700 = "#1B3A68"
BLUE_600 = "#1E5EC8"
BLUE_500 = "#2F74E8"
BLUE_400 = "#5B93F0"
BLUE_300 = "#8DB4F5"
CYAN_500 = "#0E9FB8"
CYAN_400 = "#2CC4DA"
SLATE_600 = "#475569"
SLATE_500 = "#64748B"
SLATE_400 = "#94A3B8"
SLATE_300 = "#CBD5E1"
SLATE_200 = "#E2E8F0"
OFF_WHITE = "#F7F9FC"
WHITE = "#FFFFFF"


@dataclass(frozen=True)
class Scheme:
    name: str
    background: str
    title: str
    subtitle: str
    muted: str
    boundary: str
    layer: str
    core: str
    node: str
    grid: str
    zone_fill: str
    zone_stroke: str
    link: str


DARK = Scheme(
    name="dark",
    background=NAVY_900,
    title=WHITE,
    subtitle=SLATE_300,
    muted=SLATE_400,
    boundary=BLUE_400,
    layer=BLUE_500,
    core=CYAN_400,
    node=SLATE_200,
    grid="#1A3157",
    zone_fill="#11264A",
    zone_stroke="#2A4A7C",
    link="#3F6AA8",
)

LIGHT = Scheme(
    name="light",
    background=OFF_WHITE,
    title=NAVY_900,
    subtitle=SLATE_600,
    muted=SLATE_500,
    boundary=BLUE_600,
    layer=BLUE_500,
    core=CYAN_500,
    node=NAVY_700,
    grid="#E3E9F2",
    zone_fill="#EEF3FA",
    zone_stroke="#C3D2E8",
    link="#8EA6C9",
)


# --------------------------------------------------------------------------
# Texto → curvas (HarfBuzz para shaping/kerning, fontTools para contornos)
# --------------------------------------------------------------------------
class Font:
    def __init__(self, filename: str) -> None:
        path = FONT_DIR / filename
        if not path.exists():
            raise SystemExit(f"Fonte não encontrada: {path} (defina BRAND_FONT_DIR)")
        self.tt = TTFont(path)
        self.glyphset = self.tt.getGlyphSet()
        self.upem = self.tt["head"].unitsPerEm
        blob = hb.Blob.from_file_path(str(path))
        self.hb_font = hb.Font(hb.Face(blob))
        self.glyph_order = self.tt.getGlyphOrder()

    def shape(self, text: str, tracking: float = 0.0):
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hb_font, buf, {"kern": True, "liga": False})
        glyphs = []
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            glyphs.append((self.glyph_order[info.codepoint], pos.x_advance + tracking * self.upem, pos.x_offset))
        return glyphs

    def width(self, text: str, size: float, tracking: float = 0.0) -> float:
        total = sum(adv for _, adv, _ in self.shape(text, tracking))
        if text:
            total -= tracking * self.upem  # sem tracking após o último glifo
        return total * size / self.upem

    def path(self, text: str, size: float, x: float, y: float, tracking: float = 0.0) -> str:
        scale = size / self.upem
        cursor = 0.0
        parts = []
        for name, adv, xoff in self.shape(text, tracking):
            pen = SVGPathPen(self.glyphset, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
            tpen = TransformPen(pen, (scale, 0, 0, -scale, x + (cursor + xoff) * scale, y))
            self.glyphset[name].draw(tpen)
            cmds = pen.getCommands()
            if cmds:
                parts.append(cmds)
            cursor += adv
        return "".join(parts)


DISPLAY_BOLD = Font("InterDisplay-Bold.otf")
DISPLAY_SEMI = Font("InterDisplay-SemiBold.otf")
TEXT_MEDIUM = Font("Inter-Medium.otf")
TEXT_SEMI = Font("Inter-SemiBold.otf")
TEXT_REGULAR = Font("Inter-Regular.otf")


def text(font: Font, value: str, size: float, x: float, y: float, fill: str, tracking: float = 0.0,
         anchor: str = "start") -> str:
    if anchor != "start":
        w = font.width(value, size, tracking)
        x = x - (w if anchor == "end" else w / 2)
    return f'<path fill="{fill}" d="{font.path(value, size, x, y, tracking)}"/>'


# --------------------------------------------------------------------------
# Símbolo (isotipo): camadas de defesa + trust boundary com travessias
# controladas. Desenhado em um grid de 64×64.
# --------------------------------------------------------------------------
def diamond(cx: float, cy: float, r: float) -> str:
    return f"M{cx} {cy - r}L{cx + r} {cy}L{cx} {cy + r}L{cx - r} {cy}Z"


def symbol(s: Scheme, x: float = 0, y: float = 0, size: float = 64) -> str:
    k = size / 64
    cx = cy = 32
    r_out, gap = 27, 6.5
    # Fronteira externa interrompida nos vértices: os pontos de travessia
    # (gateways) são explícitos e controlados.
    segs = []
    vertices = [(cx, cy - r_out), (cx + r_out, cy), (cx, cy + r_out), (cx - r_out, cy)]
    for i in range(4):
        (x1, y1), (x2, y2) = vertices[i], vertices[(i + 1) % 4]
        dx, dy = x2 - x1, y2 - y1
        length = (dx * dx + dy * dy) ** 0.5
        ux, uy = dx / length, dy / length
        segs.append(f"M{x1 + ux * gap:.2f} {y1 + uy * gap:.2f}L{x2 - ux * gap:.2f} {y2 - uy * gap:.2f}")
    nodes = "".join(f'<circle cx="{vx}" cy="{vy}" r="2.9" fill="{s.node}"/>' for vx, vy in vertices)
    flows = "".join(
        f'<path d="M{cx + (vx - cx) * 0.36:.2f} {cy + (vy - cy) * 0.36:.2f}L{cx + (vx - cx) * 0.86:.2f} '
        f'{cy + (vy - cy) * 0.86:.2f}" stroke="{s.node}" stroke-width="1.6" stroke-linecap="round" opacity=".55"/>'
        for vx, vy in vertices
    )
    return (
        f'<g transform="translate({x} {y}) scale({k})">'
        f'<path d="{"".join(segs)}" fill="none" stroke="{s.boundary}" stroke-width="3.2" stroke-linecap="round"/>'
        f"{flows}"
        f'<path d="{diamond(cx, cy, 17.5)}" fill="none" stroke="{s.layer}" stroke-width="3.2" stroke-linejoin="round"/>'
        f'<path d="{diamond(cx, cy, 8)}" fill="{s.core}"/>'
        f"{nodes}"
        "</g>"
    )


def svg(width: float, height: float, body: str, title: str, desc: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="t d">'
        f'<title id="t">{title}</title><desc id="d">{desc}</desc>{body}</svg>\n'
    )


# --------------------------------------------------------------------------
# Logos
# --------------------------------------------------------------------------
def logo(s: Scheme) -> str:
    h = 64
    sym = symbol(s, 0, 0, 64)
    line1 = text(DISPLAY_SEMI, "Security Architecture", 25, 80, 29, s.title, tracking=-0.01)
    line2 = text(TEXT_SEMI, "ACADEMY", 12.5, 81, 50, s.core if s is DARK else BLUE_600, tracking=0.32)
    w = 80 + DISPLAY_SEMI.width("Security Architecture", 25, -0.01) + 4
    return svg(round(w), h, sym + line1 + line2, "Security Architecture Academy",
               "Logotipo: símbolo de camadas de defesa com fronteira de confiança e o nome do projeto.")


def icon() -> str:
    body = f'<rect width="64" height="64" rx="14" fill="{NAVY_900}"/>' + symbol(DARK, 6, 6, 52)
    return svg(64, 64, body, "Security Architecture Academy",
               "Ícone: camadas de defesa concêntricas com pontos de travessia controlados.")


# --------------------------------------------------------------------------
# Ilustração: zonas de confiança aninhadas (enterprise, cloud, on-premises)
# --------------------------------------------------------------------------
def architecture_illustration(s: Scheme, ox: float, oy: float, labels: bool = True) -> str:
    """Ilustração conceitual 520×300 desenhada a partir de (ox, oy)."""
    out = []

    def zone(x, y, w, h, label, dashed=False, label_bottom=False):
        dash = ' stroke-dasharray="6 5"' if dashed else ""
        out.append(f'<rect x="{ox + x}" y="{oy + y}" width="{w}" height="{h}" rx="12" fill="{s.zone_fill}" '
                   f'stroke="{s.zone_stroke}" stroke-width="1.5"{dash}/>')
        if labels:
            ly = oy + y + h - 14 if label_bottom else oy + y + 22
            out.append(text(TEXT_SEMI, label, 10.5, ox + x + 14, ly, s.muted, tracking=0.12))

    def link(x1, y1, x2, y2, strong=False):
        color = s.core if strong else s.link
        width = 2 if strong else 1.5
        out.append(f'<path d="M{ox + x1} {oy + y1}L{ox + x2} {oy + y2}" stroke="{color}" stroke-width="{width}" '
                   'stroke-linecap="round"/>')

    def node(x, y, kind="workload"):
        if kind == "gateway":
            out.append(f'<path d="{diamond(ox + x, oy + y, 9)}" fill="{s.background}" stroke="{s.core}" stroke-width="2.4"/>')
        elif kind == "identity":
            out.append(f'<circle cx="{ox + x}" cy="{oy + y}" r="9" fill="{s.background}" stroke="{s.boundary}" stroke-width="2.4"/>'
                       f'<circle cx="{ox + x}" cy="{oy + y}" r="3.2" fill="{s.boundary}"/>')
        else:
            out.append(f'<rect x="{ox + x - 8}" y="{oy + y - 8}" width="16" height="16" rx="4" fill="{s.background}" '
                       f'stroke="{s.layer}" stroke-width="2.2"/>')

    # Enterprise boundary (toda a ilustração)
    out.append(f'<rect x="{ox}" y="{oy}" width="520" height="300" rx="18" fill="none" stroke="{s.boundary}" '
               'stroke-width="1.8" stroke-dasharray="2 6" stroke-linecap="round"/>')
    if labels:
        out.append(text(TEXT_SEMI, "ENTERPRISE TRUST BOUNDARY", 10.5, ox + 18, oy + 26, s.boundary, tracking=0.12))
    zone(28, 48, 210, 224, "ON-PREMISES")
    zone(282, 48, 210, 102, "CLOUD · REGION A")
    zone(282, 170, 210, 102, "CLOUD · REGION B", dashed=True, label_bottom=True)

    # Fluxos
    link(80, 120, 186, 120)
    link(80, 120, 80, 210)
    link(80, 210, 186, 210)
    link(186, 120, 186, 210)
    link(186, 165, 260, 165, strong=True)   # on-prem → gateway
    link(260, 165, 330, 104, strong=True)   # gateway → cloud A
    link(260, 165, 330, 222, strong=True)   # gateway → cloud B
    link(330, 104, 440, 104)
    link(330, 222, 440, 222)
    link(440, 104, 440, 222)
    link(133, 165, 186, 165)

    # Nós
    node(80, 120, "identity")
    node(186, 120)
    node(80, 210)
    node(186, 210)
    node(133, 165)
    node(186, 165)
    node(260, 165, "gateway")
    node(330, 104)
    node(440, 104, "identity")
    node(330, 222)
    node(440, 222)
    return "".join(out)


def dot_grid(s: Scheme, w: float, h: float, step: int = 24) -> str:
    pattern = (f'<defs><pattern id="g-{s.name}" width="{step}" height="{step}" patternUnits="userSpaceOnUse">'
               f'<circle cx="1.5" cy="1.5" r="1.1" fill="{s.grid}"/></pattern></defs>')
    return pattern + f'<rect width="{w}" height="{h}" fill="url(#g-{s.name})"/>'


def banner(s: Scheme) -> str:
    w, h = 1280, 400
    body = [f'<rect width="{w}" height="{h}" fill="{s.background}"/>', dot_grid(s, w, h)]
    # Painel textual com fundo sólido para legibilidade sobre o grid
    body.append(f'<rect x="0" y="0" width="660" height="{h}" fill="{s.background}" opacity=".88"/>')
    body.append(symbol(s, 72, 92, 72))
    body.append(text(TEXT_SEMI, "OPEN-SOURCE LEARNING PLATFORM", 13, 168, 120, s.core if s is DARK else BLUE_600,
                     tracking=0.16))
    body.append(text(DISPLAY_BOLD, "Security Architecture", 46, 166, 166, s.title, tracking=-0.015))
    body.append(text(DISPLAY_BOLD, "Academy", 46, 166, 218, s.title, tracking=-0.015))
    body.append(text(TEXT_REGULAR, "From Security Fundamentals to Enterprise & Hybrid Architecture.", 16.5, 168, 266,
                     s.subtitle))
    # Trilha de níveis
    x = 168
    for i, label in enumerate(["Fundamentals", "Professional", "Architect"]):
        tw = TEXT_MEDIUM.width(label, 13.5)
        body.append(f'<rect x="{x}" y="300" width="{tw + 28}" height="30" rx="15" fill="none" '
                    f'stroke="{s.zone_stroke}" stroke-width="1.4"/>')
        body.append(text(TEXT_MEDIUM, label, 13.5, x + 14, 320, s.subtitle))
        x += tw + 28
        if i < 2:
            body.append(f'<path d="M{x + 8} 315H{x + 24}M{x + 19} 310l5 5-5 5" fill="none" stroke="{s.muted}" '
                        'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')
            x += 32
    body.append(architecture_illustration(s, 724, 50))
    return svg(w, h, "".join(body), "Security Architecture Academy",
               "Banner: nome do projeto, trilha Fundamentals → Professional → Architect e ilustração de zonas de "
               "confiança on-premises e cloud conectadas por um gateway controlado.")


def social_preview() -> str:
    s = DARK
    w, h = 1280, 640
    body = [f'<rect width="{w}" height="{h}" fill="{s.background}"/>', dot_grid(s, w, h, 28)]
    body.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="{s.background}" opacity=".55"/>')
    body.append(symbol(s, 96, 120, 96))
    body.append(text(TEXT_SEMI, "OPEN-SOURCE LEARNING PLATFORM", 18, 96, 290, s.core, tracking=0.16))
    body.append(text(DISPLAY_BOLD, "Security Architecture", 72, 92, 368, s.title, tracking=-0.02))
    body.append(text(DISPLAY_BOLD, "Academy", 72, 92, 446, s.title, tracking=-0.02))
    body.append(text(TEXT_REGULAR, "Enterprise · Cloud · Hybrid Security Architecture", 26, 96, 506, s.subtitle))
    body.append(f'<path d="M96 556H1184" stroke="{s.zone_stroke}" stroke-width="1.5"/>')
    body.append(text(TEXT_MEDIUM, "github.com/andrewsferreira/security-architecture-academy", 19, 96, 594, s.muted))
    body.append(text(TEXT_MEDIUM, "Fundamentals  →  Professional  →  Architect", 19, 1184, 594, s.subtitle,
                     anchor="end"))
    body.append(f'<g opacity=".9" transform="translate(774 64) scale(.78)">'
                f'{architecture_illustration(s, 0, 0, labels=False)}</g>')
    return svg(w, h, "".join(body), "Security Architecture Academy — Social Preview",
               "Imagem de compartilhamento com o nome do projeto e a trilha de aprendizagem.")


def hero(s: Scheme) -> str:
    """Ilustração do portal (fundo transparente)."""
    body = architecture_illustration(s, 10, 10)
    return svg(540, 320, body, "Arquitetura conceitual de zonas de confiança",
               "Zonas on-premises e cloud dentro de uma fronteira de confiança corporativa; identidades, workloads e "
               "um gateway que controla as travessias entre ambientes.")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  {path.relative_to(ROOT)}  ({path.stat().st_size / 1024:.1f} KiB)")


def main() -> None:
    print("Gerando assets de marca…")
    write(OUT / "logo.svg", logo(LIGHT))           # padrão: fundos claros (GitHub light, documentos)
    write(OUT / "logo-light.svg", logo(LIGHT))     # para fundos claros
    write(OUT / "logo-dark.svg", logo(DARK))       # para fundos escuros
    write(OUT / "icon.svg", icon())
    write(OUT / "banner.svg", banner(DARK))
    write(OUT / "banner-dark.svg", banner(DARK))
    write(OUT / "banner-light.svg", banner(LIGHT))
    write(OUT / "symbol-dark.svg", svg(64, 64, symbol(DARK), "Security Architecture Academy", "Símbolo para fundos escuros."))
    write(OUT / "symbol-light.svg", svg(64, 64, symbol(LIGHT), "Security Architecture Academy", "Símbolo para fundos claros."))
    write(OUT / "social-preview.svg", social_preview())

    cairosvg.svg2png(url=str(OUT / "social-preview.svg"), write_to=str(OUT / "social-preview.png"),
                     output_width=1280, output_height=640)
    cairosvg.svg2png(url=str(OUT / "icon.svg"), write_to=str(OUT / "favicon.png"), output_width=64, output_height=64)
    cairosvg.svg2png(url=str(OUT / "icon.svg"), write_to=str(OUT / "apple-touch-icon.png"),
                     output_width=180, output_height=180)
    for p in ("social-preview.png", "favicon.png", "apple-touch-icon.png"):
        print(f"  assets/branding/{p}  ({(OUT / p).stat().st_size / 1024:.1f} KiB)")

    write(DOCS_IMAGES / "hero-architecture-light.svg", hero(LIGHT))
    write(DOCS_IMAGES / "hero-architecture-dark.svg", hero(DARK))

    # Sincroniza a cópia usada pelo portal (o Zensical só publica docs/)
    DOCS_BRAND.mkdir(parents=True, exist_ok=True)
    for f in sorted(OUT.iterdir()):
        if f.suffix in {".svg", ".png"}:
            shutil.copy2(f, DOCS_BRAND / f.name)
    print("Cópia sincronizada em docs/assets/branding/")


if __name__ == "__main__":
    main()
