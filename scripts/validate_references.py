#!/usr/bin/env python3
"""Valida a Research Library (research/) e sua integração com o conteúdo.

Verificações:
  - esquema de research/bibliography.yml (campos, valores permitidos, datas);
  - IDs únicos e estáveis;
  - fontes sem metadados mínimos (aviso);
  - referências citadas em `sources` e `further_reading` das páginas existem,
    e `sources` não aponta para fonte Pending/Unavailable;
  - research/knowledge-map.yml: referência existente, módulos válidos e
    `consulted: true` coerente com o capítulo na bibliografia;
  - IDs citados nas notas de leitura existem;
  - referências não utilizadas e módulos sem fontes associadas (aviso);
  - nenhum arquivo privado (private-research/, PDF, EPUB) versionado.

Uso:
    python scripts/validate_references.py            # validação
    python scripts/validate_references.py --report   # imprime o relatório de cobertura (Markdown)
    python scripts/validate_references.py --links    # também verifica as URLs (rede; uso no workflow semanal)
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

from _common import DOCS, ROOT, Report, load_manifest, read_front_matter

RESEARCH = ROOT / "research"
BIBLIOGRAPHY = RESEARCH / "bibliography.yml"
KNOWLEDGE_MAP = RESEARCH / "knowledge-map.yml"
NOTES = RESEARCH / "notes"

ID_RE = re.compile(r"^[A-Z0-9]+(?:-[A-Z0-9]+)*$")
NOTE_ID_RE = re.compile(r"`([A-Z0-9]+(?:-[A-Z0-9]+)+)`")
CHAPTER_RE = re.compile(r"^Cap\.\s*(\d+)")

AVAILABILITY = {"Free Download", "Free Online Reading", "Free With Registration", "Paid", "Restricted", "Unknown"}
REDISTRIBUTION = {"Explicitly Permitted", "Restricted", "Prohibited", "Not Verified"}
VERIFICATION = {"Verified", "Partially Verified", "Unavailable", "Pending"}
READING_ROLES = {"essential", "deep-dive", "reference", "exercises", "projects"}
PAGE_BASIS = {"printed", "pdf"}
TIERS = {"fundamental", "professional", "architect"}
REQUIRED = ("id", "title", "publisher", "url", "type", "language", "category", "availability",
            "redistribution", "verification", "verified_on", "modules", "reading_role", "priority")
CITABLE = {"Verified", "Partially Verified"}
PRIVATE_PATTERNS = (re.compile(r"^private-research/(?!README\.md$)"), re.compile(r"\.(pdf|epub)$", re.IGNORECASE))


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def module_ids() -> list[str]:
    return [m["id"] for m in load_manifest()["modules"]]


def page_citations() -> dict[str, dict[str, list[str]]]:
    """{arquivo relativo: {"sources": [...], "further_reading": [...]}} para páginas com citações."""
    out: dict[str, dict[str, list[str]]] = {}
    for page in sorted(DOCS.rglob("*.md")):
        try:
            meta, _ = read_front_matter(page)
        except Exception:  # noqa: BLE001 — front matter inválido é tratado por check_structure.py
            continue
        cites = {k: list(meta.get(k) or []) for k in ("sources", "further_reading")}
        if any(cites.values()):
            out[page.relative_to(ROOT).as_posix()] = cites
    return out


def note_citations() -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    if NOTES.is_dir():
        for note in sorted(NOTES.glob("*.md")):
            out[note.relative_to(ROOT).as_posix()] = set(NOTE_ID_RE.findall(note.read_text(encoding="utf-8")))
    return out


def tracked_files() -> list[str] | None:
    try:
        result = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.splitlines()


# ------------------------------------------------------------------ validação
def validate(bib: dict[str, Any], kmap: dict[str, Any], modules: list[str],
             pages: dict[str, dict[str, list[str]]], notes: dict[str, set[str]],
             tracked: list[str] | None) -> Report:
    report = Report("Research Library")
    refs = bib.get("references") or []
    categories = set((bib.get("categories") or {}).keys())
    by_id: dict[str, dict[str, Any]] = {}

    for idx, ref in enumerate(refs):
        rid = ref.get("id", f"#{idx}")
        for field in REQUIRED:
            if ref.get(field) in (None, "", []) and field != "modules":
                report.error(f"{rid}: campo obrigatório ausente: {field}")
        if not ID_RE.match(str(rid)):
            report.error(f"{rid}: ID fora do padrão (maiúsculas, dígitos e hífens)")
        if rid in by_id:
            report.error(f"{rid}: ID duplicado")
        by_id[rid] = ref
        for field, allowed in (("availability", AVAILABILITY), ("redistribution", REDISTRIBUTION),
                               ("verification", VERIFICATION), ("reading_role", READING_ROLES)):
            if ref.get(field) is not None and ref.get(field) not in allowed:
                report.error(f"{rid}: {field} inválido: {ref.get(field)!r}")
        if categories and ref.get("category") not in categories:
            report.error(f"{rid}: categoria desconhecida: {ref.get('category')!r}")
        if ref.get("priority") not in (1, 2, 3):
            report.error(f"{rid}: priority deve ser 1, 2 ou 3")
        try:
            dt.date.fromisoformat(str(ref.get("verified_on")))
        except ValueError:
            report.error(f"{rid}: verified_on não é uma data AAAA-MM-DD")
        if not str(ref.get("url", "")).startswith("https://"):
            report.error(f"{rid}: url deve usar https://")
        for mod in ref.get("modules") or []:
            if mod not in modules:
                report.error(f"{rid}: módulo inexistente: {mod}")
        for ch in ref.get("chapters") or []:
            loc = ch.get("locator", "?")
            if not ch.get("locator") or not ch.get("title") or not isinstance(ch.get("consulted"), bool):
                report.error(f"{rid}: capítulo {loc!r} precisa de locator, title e consulted (booleano)")
            if "pages" in ch and ch.get("page_basis") not in PAGE_BASIS:
                report.error(f"{rid}: capítulo {loc!r} com pages exige page_basis printed ou pdf")
            if ch.get("consulted") and ref.get("verification") not in CITABLE:
                report.error(f"{rid}: capítulo {loc!r} marcado como consultado em fonte não verificada")
            for mod in ch.get("modules") or []:
                if mod not in modules:
                    report.error(f"{rid}: capítulo {loc!r} com módulo inexistente: {mod}")
        if ref.get("verification") == "Verified" and not (ref.get("year") or ref.get("edition")):
            report.warn(f"{rid}: fonte verificada sem ano nem edição/versão registrados")
        if ref.get("availability") in ("Free Download", "Free Online Reading") and ref.get("redistribution") == "Explicitly Permitted" \
                and "licen" not in str(ref.get("notes", "")).lower():
            report.warn(f"{rid}: redistribuição marcada como permitida sem citar a licença nas notas")

    # -- páginas
    used: set[str] = set()
    for page, cites in pages.items():
        for field, ids in cites.items():
            for rid in ids:
                used.add(rid)
                ref = by_id.get(rid)
                if ref is None:
                    report.error(f"{page}: {field} cita referência inexistente: {rid}")
                elif field == "sources" and ref.get("verification") not in CITABLE:
                    report.error(f"{page}: sources cita fonte não verificada ({ref.get('verification')}): {rid}")

    # -- mapa de conhecimento
    for idx, entry in enumerate(kmap.get("concepts") or []):
        label = entry.get("concept", f"#{idx}")
        rid = entry.get("ref")
        ref = by_id.get(rid)
        used.add(rid)
        if ref is None:
            report.error(f"knowledge-map: '{label}' cita referência inexistente: {rid}")
            continue
        for field in ("locator", "modules", "tier", "application", "limitations"):
            if not entry.get(field):
                report.error(f"knowledge-map: '{label}' sem {field}")
        if entry.get("tier") and entry["tier"] not in TIERS:
            report.error(f"knowledge-map: '{label}' com tier inválido: {entry['tier']}")
        for mod in entry.get("modules") or []:
            if mod not in modules:
                report.error(f"knowledge-map: '{label}' com módulo inexistente: {mod}")
        if not isinstance(entry.get("consulted"), bool):
            report.error(f"knowledge-map: '{label}' precisa de consulted (booleano)")
        elif entry["consulted"]:
            if ref.get("verification") not in CITABLE:
                report.error(f"knowledge-map: '{label}' consultado em fonte não verificada: {rid}")
            match = CHAPTER_RE.match(str(entry.get("locator", "")))
            if match:
                chapter = next((c for c in ref.get("chapters") or []
                                if CHAPTER_RE.match(c.get("locator", "")) and CHAPTER_RE.match(c["locator"]).group(1) == match.group(1)), None)
                if chapter is None or not chapter.get("consulted"):
                    report.error(f"knowledge-map: '{label}' marcado como consultado, mas {rid} Cap. {match.group(1)} não está consultado na bibliografia")

    # -- notas
    for note, ids in notes.items():
        for rid in ids:
            if rid in by_id:
                used.add(rid)
            elif ID_RE.match(rid) and "-" in rid and not rid.startswith(("M0", "M1", "C0")):
                report.error(f"{note}: cita referência inexistente: {rid}")

    # -- não utilizadas e cobertura
    for rid in by_id:
        if rid not in used:
            report.warn(f"{rid}: referência não utilizada em aulas, mapa de conhecimento ou notas")
    covered = {m for r in refs if r.get("verification") in CITABLE for m in r.get("modules") or []}
    for mod in modules:
        if mod not in covered:
            report.warn(f"{mod}: módulo sem fonte verificada associada")

    # -- arquivos privados
    if tracked is None:
        report.warn("git indisponível — verificação de arquivos privados ignorada")
    else:
        for path in tracked:
            if any(p.search(path) for p in PRIVATE_PATTERNS):
                report.error(f"arquivo privado ou obra de terceiros versionado: {path}")
    for path in list(DOCS.rglob("*.pdf")) + list(DOCS.rglob("*.epub")):
        report.error(f"PDF/EPUB dentro de docs/ seria publicado no portal: {path.relative_to(ROOT)}")
    return report


# ------------------------------------------------------------------ cobertura
def coverage(bib: dict[str, Any], kmap: dict[str, Any], manifest: dict[str, Any],
             pages: dict[str, dict[str, list[str]]]) -> dict[str, Any]:
    """Estatísticas de cobertura usadas pelo relatório e pela página do portal."""
    refs = bib.get("references") or []
    rows = []
    for mod in manifest["modules"]:
        mid = mod["id"]
        mrefs = [r for r in refs if mid in (r.get("modules") or [])]
        verified = [r for r in mrefs if r.get("verification") in CITABLE]
        essential = [r for r in verified if r.get("reading_role") == "essential"]
        chapters = [c for r in refs for c in r.get("chapters") or [] if mid in (c.get("modules") or [])]
        consulted = [c for c in chapters if c.get("consulted")]
        concepts = [c for c in kmap.get("concepts") or [] if mid in (c.get("modules") or [])]
        lesson_cites = sorted({rid for page, cites in pages.items() if page.startswith(f"docs/modules/{mid[1:]}-")
                               for rid in cites["sources"] + cites["further_reading"]})
        if not verified:
            level = "Sem fontes"
        elif len(verified) < 3 or not essential or not concepts:
            level = "Parcial"
        elif consulted and len(concepts) >= 3:
            level = "Boa"
        else:
            level = "Localizada"
        rows.append({"id": mid, "title": mod["title"], "status": mod["status"], "refs": len(mrefs),
                     "verified": len(verified), "essential": [r["id"] for r in essential],
                     "chapters": len(chapters), "consulted": len(consulted), "concepts": len(concepts),
                     "cited": lesson_cites, "level": level})
    by_cat: dict[str, int] = defaultdict(int)
    for r in refs:
        by_cat[r["category"]] += 1
    states = {k: defaultdict(int) for k in ("verification", "availability", "redistribution")}
    for r in refs:
        for k in states:
            states[k][r[k]] += 1
    return {"modules": rows, "by_category": dict(by_cat), "states": {k: dict(v) for k, v in states.items()},
            "total": len(refs), "concepts": len(kmap.get("concepts") or []),
            "chapters": sum(len(r.get("chapters") or []) for r in refs),
            "consulted": sum(1 for r in refs for c in r.get("chapters") or [] if c.get("consulted"))}


def render_report(cov: dict[str, Any], categories: dict[str, str]) -> str:
    out = [f"**{cov['total']} referências** · {cov['chapters']} capítulos ou seções localizados, "
           f"{cov['consulted']} efetivamente lidos · {cov['concepts']} conceitos no mapa de conhecimento.", ""]
    out += ["| Verificação | Qtde. |", "|:---|---:|"]
    names = {"Verified": "Verificada", "Partially Verified": "Parcialmente verificada", "Unavailable": "Indisponível", "Pending": "Pendente"}
    out += [f"| {names.get(k, k)} | {cov['states']['verification'][k]} |" for k in names if k in cov["states"]["verification"]]
    out += ["", "**Critério de cobertura:** *Boa* — pelo menos 3 fontes verificadas, leitura essencial, 3 conceitos mapeados e algum trecho efetivamente lido · "
            "*Localizada* — fontes e conceitos existem, mas os trechos foram só localizados ou são poucos · *Parcial* — menos de 3 fontes verificadas, "
            "sem leitura essencial ou sem conceitos mapeados · *Sem fontes*.",
            "", "| Módulo | Status | Fontes verificadas | Leitura essencial | Capítulos localizados (lidos) | Conceitos mapeados | Cobertura |",
            "|:---|:---|---:|:---|---:|---:|:---|"]
    for row in cov["modules"]:
        ess = ", ".join(f"`{e}`" for e in row["essential"]) or "—"
        out.append(f"| {row['id']} — {row['title']} | {row['status']} | {row['verified']} | {ess} | "
                   f"{row['chapters']} ({row['consulted']}) | {row['concepts']} | {row['level']} |")
    gaps = [r for r in cov["modules"] if r["level"] in ("Sem fontes", "Parcial")]
    out += ["", "**Lacunas:** " + (", ".join(f"{r['id']} ({r['level'].lower()})" for r in gaps) if gaps else "nenhuma.")]
    empty = [label for key, label in categories.items() if not cov["by_category"].get(key)]
    if empty:
        out.append("")
        out.append("**Categorias sem fontes registradas:** " + ", ".join(empty) + ".")
    return "\n".join(out)


# ------------------------------------------------------------------ links
def check_links(refs: list[dict[str, Any]], report: Report) -> None:
    headers = {"User-Agent": "security-architecture-academy-link-check/1.0 (+https://github.com/andrewsferreira/security-architecture-academy)"}
    for ref in refs:
        url = ref["url"]
        for method in ("HEAD", "GET"):
            try:
                req = urllib.request.Request(url, method=method, headers=headers)
                with urllib.request.urlopen(req, timeout=20) as resp:  # noqa: S310 — URLs do registro, apenas https
                    if resp.status < 400:
                        break
            except urllib.error.HTTPError as exc:
                if method == "GET":
                    report.warn(f"{ref['id']}: {url} respondeu {exc.code}")
            except (urllib.error.URLError, TimeoutError) as exc:
                if method == "GET":
                    report.warn(f"{ref['id']}: {url} inacessível ({exc})")
        time.sleep(1)  # sem varredura agressiva: uma requisição por segundo


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--report", action="store_true", help="imprime o relatório de cobertura em Markdown")
    parser.add_argument("--links", action="store_true", help="verifica as URLs das referências (requer rede)")
    args = parser.parse_args()

    bib, kmap, manifest = load_yaml(BIBLIOGRAPHY), load_yaml(KNOWLEDGE_MAP), load_manifest()
    pages = page_citations()
    if args.report:
        print(render_report(coverage(bib, kmap, manifest, pages), bib.get("categories") or {}))
        return
    report = validate(bib, kmap, module_ids(), pages, note_citations(), tracked_files())
    if args.links:
        check_links(bib.get("references") or [], report)
    sys.exit(report.finish())


if __name__ == "__main__":
    main()
