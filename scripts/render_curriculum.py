#!/usr/bin/env python3
"""Gera as páginas derivadas de curriculum/manifest.yml e da Research Library (research/).

Saídas (blocos entre marcadores <!-- nome:start --> / <!-- nome:end -->):
    docs/curriculum/index.md                → blocos "curriculum" e "activities"
    docs/curriculum/dependencies.md         → bloco "dependencies" (grafo Mermaid)
    docs/resources/index.md                 → blocos "library-summary" e "sources"
    docs/resources/books.md                 → bloco "books"
    docs/resources/official-frameworks.md   → bloco "frameworks"
    docs/resources/cloud-security.md        → bloco "cloud"
    docs/resources/reference-matrix.md      → bloco "reference-matrix"
    docs/resources/coverage.md              → bloco "coverage"
    docs/index.md                           → bloco "release-status" (disponibilidade por nível)
    CURRICULUM.md                           → arquivo inteiro (visão para o GitHub)

Uso:
    python scripts/render_curriculum.py           # atualiza os arquivos
    python scripts/render_curriculum.py --check   # falha se algum estiver desatualizado (CI)
"""

from __future__ import annotations

import argparse
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Any

import yaml

from _common import DOCS, ROOT, load_manifest

BIBLIOGRAPHY = ROOT / "research" / "bibliography.yml"
KNOWLEDGE_MAP = ROOT / "research" / "knowledge-map.yml"
REPO_BLOB = "https://github.com/andrewsferreira/security-architecture-academy/blob/main/"
LABELS = {
    "planned": "Planned",
    "draft": "Draft",
    "in-review": "In Review",
    "published": "Published",
    "deprecated": "Deprecated",
}
ACCESS = {
    "public": "Público",
    "free-registration": "Gratuito com cadastro",
    "free-restricted": "Gratuito com restrições",
    "paid": "Pago",
    "unconfirmed": "Não confirmado",
}
TYPES = {
    "documentation": "Documentação",
    "course": "Curso",
    "lab": "Laboratório",
    "guide": "Guia",
    "video": "Vídeo",
    "reference": "Referência",
}
SITE = "https://andrewsferreira.github.io/security-architecture-academy/"


# ---------------------------------------------------------------- utilidades
def badge(status: str) -> str:
    return f'<span class="saa-status saa-status--{status}">{LABELS.get(status, status)}</span>'


def hours(minutes: int) -> str:
    h, m = divmod(minutes, 60)
    return f"{h} h {m:02d} min" if m else f"{h} h"


def module_number(mid: str) -> str:
    return mid[1:]


def unit_base(unit: dict[str, Any]) -> str:
    if unit["id"].startswith("M"):
        return f"modules/{module_number(unit['id'])}-{unit['slug']}"
    return f"complements/{unit['slug']}"


def splice(page: str, name: str, block: str) -> str:
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    if start not in page or end not in page:
        raise SystemExit(f"Marcadores {start} / {end} não encontrados")
    head, rest = page.split(start, 1)
    _, tail = rest.split(end, 1)
    return f"{head}{start}\n\n{block.rstrip()}\n\n{end}{tail}"


# ------------------------------------------------------- Curriculum Roadmap
def render_curriculum(m: dict[str, Any]) -> str:
    domains = {d["id"]: d["title"] for d in m["domains"]}
    tiers = {t["id"]: t["title"] for t in m["tiers"]}
    modules = m["modules"]
    lessons = [lesson for mod in modules for lesson in mod["lessons"]]
    counts = OrderedDict((s, 0) for s in LABELS)
    for lesson in lessons:
        counts[lesson["status"]] += 1
    total = sum(lesson["minutes"] for lesson in lessons)
    out = [
        f"**{len(modules)} módulos · {len(lessons)} aulas · cerca de {total // 60} horas de aulas** "
        "(sem laboratórios, estudos de caso e avaliações). "
        "Status das aulas: " + " · ".join(f"{LABELS[s]} **{n}**" for s, n in counts.items() if n) + ".",
        "",
    ]
    for stage in m["stages"]:
        items = [mod for mod in modules if mod["stage"] == stage["id"]]
        out += [f"### {stage['title']}", "", stage["summary"], "",
                "| ID | Módulo | Aulas | Carga | Fase | Status |", "|:---|:---|:---|:---|:---|:---|"]
        for mod in items:
            title = mod["title"]
            if mod.get("path") and mod["status"] != "planned":
                title = f"[{title}](../{mod['path']})"
            minutes = sum(lesson["minutes"] for lesson in mod["lessons"])
            out.append(f"| `{mod['id']}` | {title} | {len(mod['lessons'])} | {hours(minutes)} | "
                       f"{mod['phase']} | {badge(mod['status'])} |")
        out.append("")
        for mod in items:
            doms = ", ".join(domains[d] for d in mod["domains"])
            prereq = ", ".join(f"`{p}`" for p in mod["prerequisites"]) or "nenhum"
            out += [f'??? abstract "{mod["id"]} — {mod["title"]}"', "",
                    f"    **Domínios:** {doms} · **Pré-requisitos:** {prereq}", "",
                    "    | Aula | Título | Profundidade | Tempo | Status |", "    |:---|:---|:---|:---|:---|"]
            for lesson in mod["lessons"]:
                ltitle = lesson["title"]
                if lesson.get("file") and lesson["status"] != "planned":
                    ltitle = f"[{ltitle}](../{unit_base(mod)}/{lesson['file']})"
                out.append(f"    | `{lesson['id']}` | {ltitle} | {tiers[lesson['tier']]} | "
                           f"{lesson['minutes']} min | {badge(lesson['status'])} |")
            out.append("")
    for comp in m.get("complements") or []:
        out += ["### Seção complementar", "",
                f"| ID | Conteúdo | Aulas | Fase | Status |", "|:---|:---|:---|:---|:---|",
                f"| `{comp['id']}` | {comp['title']} | {len(comp['lessons'])} | {comp['phase']} | {badge(comp['status'])} |", ""]
    out.append("<small>Títulos de aulas com status Planned são provisórios até a produção do módulo.</small>")
    return "\n".join(out)


def render_activities(m: dict[str, Any]) -> str:
    titles = {
        "case_studies": "Estudos de caso",
        "labs": "Laboratórios",
        "assessments": "Avaliações",
        "artifacts": "Modelos de artefatos",
    }
    out: list[str] = []
    for key, heading in titles.items():
        out += [f"### {heading}", "", "| ID | Título | Módulos | Fase | Status |", "|:---|:---|:---|:---|:---|"]
        for item in m.get(key) or []:
            title = item["title"]
            if item.get("path") and item["status"] != "planned":
                title = f"[{title}](../{item['path']})"
            if item.get("tested"):
                title += " · *executado e testado*"
            mods = ", ".join(f"`{x}`" for x in item.get("modules") or []) or "—"
            out.append(f"| `{item['id']}` | {title} | {mods} | {item['phase']} | {badge(item['status'])} |")
        out.append("")
    return "\n".join(out)


# -------------------------------------------------------- Grafo Mermaid
def render_dependencies(m: dict[str, Any]) -> str:
    out = ["```mermaid", "flowchart TB",
           "  accTitle: Dependências entre os módulos",
           "  accDescr: Grafo de pré-requisitos gerado a partir do manifesto do currículo. Cada seta liga um "
           "módulo pré-requisito ao módulo que depende dele; os módulos estão agrupados pelos seis níveis do currículo.",
           ""]
    for stage in m["stages"]:
        sid = stage["id"].upper()
        out.append(f'  subgraph {sid}["{stage["title"]}"]')
        out.append("    direction LR")
        for mod in (x for x in m["modules"] if x["stage"] == stage["id"]):
            out.append(f'    {mod["id"]}["{mod["id"]} · {mod["title"]}"]')
        out.append("  end")
    for comp in m.get("complements") or []:
        out.append(f'  {comp["id"]}["{comp["id"]} · {comp["title"].replace("Complemento: ", "")}"]')
    out.append("")
    for unit in list(m["modules"]) + list(m.get("complements") or []):
        for dep in unit["prerequisites"]:
            out.append(f"  {dep} --> {unit['id']}")
    out.append("")
    out.append("  classDef zone fill:transparent,stroke:#64748b,stroke-width:1px,stroke-dasharray:4 3")
    out.append("  classDef active stroke:#0e9fb8,stroke-width:3px")
    out.append("  class " + ",".join(s["id"].upper() for s in m["stages"]) + " zone")
    active = [u["id"] for u in m["modules"] if u["status"] != "planned"]
    if active:
        out.append("  class " + ",".join(active) + " active")
    out.append("```")
    return "\n".join(out)


# -------------------------------------------------------- Research Library
AVAILABILITY_PT = {
    "Free Download": "Download gratuito", "Free Online Reading": "Leitura online gratuita",
    "Free With Registration": "Gratuito com cadastro", "Paid": "Pago", "Restricted": "Restrito", "Unknown": "Não confirmado",
}
REDISTRIBUTION_PT = {
    "Explicitly Permitted": "Permitida pela licença", "Restricted": "Restrita", "Prohibited": "Proibida", "Not Verified": "Não verificada",
}
VERIFICATION_PT = {
    "Verified": "Verificada", "Partially Verified": "Parcialmente verificada", "Unavailable": "Indisponível", "Pending": "Pendente",
}
ROLE_PT = {"essential": "Essencial", "deep-dive": "Aprofundada", "reference": "Consulta", "exercises": "Exercícios", "projects": "Projetos"}


def _cite(ref: dict[str, Any]) -> str:
    """Linha bibliográfica curta: autores/instituição, título, edição."""
    who = ", ".join(ref.get("authors") or []) or ref["publisher"]
    edition = f" — {ref['edition']}" if ref.get("edition") else ""
    return f"{who}. [*{ref['title']}*]({ref['url']}){edition}"


def _status(ref: dict[str, Any]) -> str:
    ver = VERIFICATION_PT[ref["verification"]]
    if ref["verification"] in ("Verified", "Partially Verified"):
        ver += f" em {ref['verified_on']}"
    else:
        ver = f"**{ver}**"
    return ver


def _ref_table(refs: list[dict[str, Any]]) -> list[str]:
    out = ["| Referência | Acesso | Redistribuição | Módulos | Leitura | Verificação |",
           "|:---|:---|:---|:---|:---|:---|"]
    for ref in refs:
        mods = ", ".join(ref.get("modules") or []) or "—"
        desc = _cite(ref) + f"<br><small>`{ref['id']}` · {ref.get('type', '')}"
        if ref.get("identifiers"):
            desc += " · " + " · ".join(f"{k.upper()} {v}" for k, v in ref["identifiers"].items())
        desc += "</small>"
        role = f"{ROLE_PT[ref['reading_role']]} · P{ref['priority']}"
        out.append(f"| {desc} | {AVAILABILITY_PT[ref['availability']]} | {REDISTRIBUTION_PT[ref['redistribution']]} | "
                   f"{mods} | {role} | {_status(ref)} |")
    return out


def render_library_summary(bib: dict[str, Any]) -> str:
    refs = bib["references"]
    count = OrderedDict((k, 0) for k in VERIFICATION_PT)
    for ref in refs:
        count[ref["verification"]] += 1
    plural = {"Verified": ("verificada", "verificadas"), "Partially Verified": ("parcialmente verificada", "parcialmente verificadas"),
              "Unavailable": ("indisponível", "indisponíveis"), "Pending": ("pendente", "pendentes")}
    parts = [f"{n} {plural[k][0] if n == 1 else plural[k][1]}" for k, n in count.items() if n]
    essential = [r for r in refs if r["reading_role"] == "essential" and r["verification"] in ("Verified", "Partially Verified")]
    lines = [f"**{len(refs)} referências registradas** — " + ", ".join(parts) + ".", "",
             "**Leitura essencial:** " + ", ".join(f"[{r['title'].split(':')[0]}]({r['url']})" for r in essential) + "."]
    return "\n".join(lines)


def render_sources(bib: dict[str, Any]) -> str:
    out: list[str] = []
    for key, label in bib["categories"].items():
        refs = [r for r in bib["references"] if r["category"] == key]
        if not refs:
            out += [f"### {label}", "", "*Nenhuma fonte registrada nesta categoria — lacuna registrada no relatório de cobertura.*", ""]
            continue
        out += [f"### {label}", ""] + _ref_table(refs) + [""]
    return "\n".join(out).rstrip()


def render_books(bib: dict[str, Any]) -> str:
    out: list[str] = []
    for ref in [r for r in bib["references"] if r.get("type") == "Book"]:
        out += [f"## {ref['title']}", "",
                "| Campo | Valor |", "|:---|:---|",
                f"| Autores | {', '.join(ref.get('authors') or [])} |",
                f"| Editora, edição | {ref['publisher']} — {ref.get('edition', '—')} |"]
        if ref.get("identifiers"):
            out.append("| Identificadores | " + " · ".join(f"{k.upper()} {v}" for k, v in ref["identifiers"].items()) + " |")
        out += [f"| Acesso | [{AVAILABILITY_PT[ref['availability']]}]({ref['url']}) |",
                f"| Redistribuição | {REDISTRIBUTION_PT[ref['redistribution']]} |",
                f"| Verificação | {_status(ref)} |", "",
                f"{ref['notes']}", "",
                "| Capítulo | Título | Páginas | Módulos | Situação |", "|:---|:---|:---|:---|:---|"]
        for ch in ref.get("chapters") or []:
            pages = f"{ch['pages']} ({'impressa' if ch.get('page_basis') == 'printed' else 'PDF'})" if ch.get("pages") else "—"
            state = "**Lido**" if ch["consulted"] else "Sumário"
            out.append(f"| {ch['locator']} | {ch['title']} | {pages} | {', '.join(ch.get('modules') or []) or '—'} | {state} |")
        out.append("")
    return "\n".join(out).rstrip()


def render_category_pages(bib: dict[str, Any], categories: tuple[str, ...]) -> str:
    out: list[str] = []
    for key in categories:
        refs = [r for r in bib["references"] if r["category"] == key and r.get("type") != "Book"]
        if not refs:
            continue
        out += [f"## {bib['categories'][key]}", ""]
        for ref in refs:
            out += [f"### {ref['title']}", "",
                    f"`{ref['id']}` · {ref['publisher']}" + (f" · {ref['edition']}" if ref.get("edition") else "") +
                    f" · {AVAILABILITY_PT[ref['availability']]} · redistribuição: {REDISTRIBUTION_PT[ref['redistribution']].lower()} · "
                    f"{_status(ref)} · [abrir fonte oficial]({ref['url']})", ""]
            if ref.get("concepts"):
                out.append("**Conceitos:** " + "; ".join(ref["concepts"]) + ".")
                out.append("")
            located = [c for c in ref.get("chapters") or []]
            if located:
                out += ["| Localização | Título | Módulos | Situação |", "|:---|:---|:---|:---|"]
                for ch in located:
                    page = f" (p. {ch['pages']})" if ch.get("pages") else ""
                    out.append(f"| {ch['locator']}{page} | {ch['title']} | {', '.join(ch.get('modules') or []) or '—'} | "
                               f"{'**Lido**' if ch['consulted'] else 'Localizado'} |")
                out.append("")
            out += [f"{ref['notes']}", "", f"Módulos: {', '.join(ref.get('modules') or []) or '—'} · "
                    f"Leitura: {ROLE_PT[ref['reading_role']]} (prioridade {ref['priority']}).", ""]
    return "\n".join(out).rstrip()


def render_reference_matrix(bib: dict[str, Any], kmap: dict[str, Any], m: dict[str, Any] | None = None) -> str:
    """Rastreabilidade conceito → fonte e localização → aulas → diagramas → aplicação.

    Aulas com página disponível (status diferente de planned) viram links; as demais aparecem só pelo ID.
    """
    titles = {r["id"]: r["title"].split(":")[0] for r in bib["references"]}
    urls = {r["id"]: r["url"] for r in bib["references"]}
    pages: dict[str, str] = {}
    for unit in (m or {}).get("modules", []) + (m or {}).get("complements", []):
        for lesson in unit.get("lessons") or []:
            if lesson.get("file") and lesson.get("status") != "planned":
                pages[lesson["id"]] = f"../{unit_base(unit)}/{lesson['file']}"
    out = ["| Conceito | Fonte e localização | Aulas | Diagramas | Nível | Aplicação arquitetural | Limitações | Situação |",
           "|:---|:---|:---|:---|:---|:---|:---|:---|"]
    for c in kmap["concepts"]:
        src = f"[{titles[c['ref']]}]({urls[c['ref']]}) — {c['locator']}<br><small>`{c['ref']}`</small>"
        state = "**Lido**" if c["consulted"] else "Localizado"
        lessons = ", ".join(f"[{lid}]({pages[lid]})" if lid in pages else f"`{lid}`" for lid in c.get("lessons") or [])
        lessons = lessons or f"<small>Módulos {', '.join(c['modules'])}</small>"
        diagrams = "<br>".join(f"`{d}`" for d in c.get("diagrams") or []) or "—"
        out.append(f"| {c['concept']} | {src} | {lessons} | {diagrams} | {c['tier']} | {c['application']} | "
                   f"{c['limitations']} | {state} |")
    return "\n".join(out)


def render_coverage(bib: dict[str, Any], kmap: dict[str, Any], m: dict[str, Any]) -> str:
    from validate_references import coverage, page_citations, render_report  # import tardio: evita ciclo
    return render_report(coverage(bib, kmap, m, page_citations()), bib["categories"])



# -------------------------------------------------------- disponibilidade por nível (homepage)
LEVEL_TEXT = {
    "R1": "**Módulos 00 a 02.** Infraestrutura, fundamentos de segurança e introdução à arquitetura de segurança, "
          "com laboratórios, estudo de caso e avaliação final integradora.",
    "R2": "**Módulos 03 a 15.** Governança, threat modeling, rede, identidade, Zero Trust, legados, AWS, Azure, "
          "Google Cloud, híbrido, aplicações, dados, vulnerabilidades e operações.",
    "R3": "**Módulos 16 e 17 e complemento de IA.** Arquitetura corporativa, governança entre unidades, "
          "estudos de caso integradores e projeto final.",
}


def release_availability(m: dict[str, Any], rel: dict[str, Any]) -> tuple[str, str]:
    """Retorna (classe de status, rótulo) de uma release a partir do estado real do manifesto."""
    mods = {u["id"]: u for u in m["modules"] + m.get("complements", [])}
    scope = [mods[i] for i in (rel.get("modules") or []) + (rel.get("complements") or [])]
    if scope and all(u["status"] == "published" for u in scope):
        return "published", "Disponível"
    if rel.get("status") in {"in-review", "approved"}:
        return "in-review", "Em revisão"
    if rel.get("status") == "in-development" or any(u["status"] != "planned" for u in scope):
        return "draft", "Em desenvolvimento"
    return "planned", "Planejado"


def render_release_status(m: dict[str, Any]) -> str:
    releases = m.get("releases") or []
    mods = {u["id"]: u for u in m["modules"]}
    available = [r for r in releases if release_availability(m, r)[0] == "published"]
    out: list[str] = []
    if available:
        first = mods[available[0]["modules"][0]]
        lesson = next(x for x in first["lessons"] if x.get("file"))
        versions = ", ".join(f"v{r['version']} — {r['title'].split(' — ')[-1]}" for r in available)
        out += ['!!! success "Disponível agora"', "",
                f"    A Academy é disponibilizada progressivamente, por nível. Publicado: **{versions}**. "
                "Os níveis seguintes entram no portal somente depois de concluídos e revisados.", "",
                f"[Começar pelos Fundamentals]({unit_base(first)}/{lesson['file']}){{ .md-button .md-button--primary }}",
                "[Ver o currículo](curriculum/index.md){ .md-button }", ""]
    else:
        out += ['!!! info "Publicação progressiva por nível"', "",
                "    A Academy será disponibilizada por níveis — Fundamentals, Professional e Architect. "
                "Nenhum nível está publicado ainda: a Release 1 (Fundamentals) está em revisão. "
                "O [currículo](curriculum/index.md) mostra o estado real de cada módulo.", ""]
    out += ['<div class="saa-journey" markdown>', ""]
    for rel in releases:
        cls, label = release_availability(m, rel)
        name = rel["title"].split(" — ")[-1]
        out += ['<div class="saa-journey__step" markdown>', "", f"### {name}", "",
                LEVEL_TEXT.get(rel["id"], ""), "",
                f'<span class="saa-status saa-status--{cls}">{label}</span> <span class="saa-meta">v{rel["version"]}</span>', "",
                "</div>", ""]
    out += ["</div>"]
    return "\n".join(out)

# -------------------------------------------------------- CURRICULUM.md
def render_root(m: dict[str, Any]) -> str:
    tiers = {t["id"]: t["title"] for t in m["tiers"]}
    lines = [
        "# Currículo",
        "",
        "<!-- Arquivo gerado por scripts/render_curriculum.py a partir de curriculum/manifest.yml. Não edite à mão. -->",
        "",
        f"Visão completa da formação. Versão navegável: [Curriculum Roadmap]({SITE}curriculum/). "
        f"Manifesto atualizado em {m['updated']}.",
        "",
        "**Legenda de status:** Planned (planejado) · Draft (em escrita) · In Review (em revisão) · "
        "Published (publicado) · Deprecated (descontinuado).",
        "",
        "## Fases do projeto",
        "",
        "| Fase | Status |",
        "|:---|:---|",
    ]
    lines += [f"| {p['title']} | {LABELS[p['status']]} |" for p in m["phases"]]
    lines.append("")
    for stage in m["stages"]:
        lines += [f"## {stage['title']}", "", stage["summary"], ""]
        for mod in (x for x in m["modules"] if x["stage"] == stage["id"]):
            prereq = ", ".join(mod["prerequisites"]) or "nenhum"
            lines += [f"### {mod['id']} — {mod['title']}", "",
                      f"Status: **{LABELS[mod['status']]}** · Fase {mod['phase']} · Pré-requisitos: {prereq}", ""]
            for lesson in mod["lessons"]:
                title = lesson["title"]
                if lesson.get("file") and lesson["status"] != "planned":
                    title = f"[{title}](docs/{unit_base(mod)}/{lesson['file']})"
                lines.append(f"- `{lesson['id']}` {title} — {tiers[lesson['tier']]}, "
                             f"{lesson['minutes']} min — {LABELS[lesson['status']]}")
            lines.append("")
    for comp in m.get("complements") or []:
        lines += [f"## {comp['title']}", "", f"Status: **{LABELS[comp['status']]}** · Fase {comp['phase']}", ""]
        lines += [f"- `{x['id']}` {x['title']} — {LABELS[x['status']]}" for x in comp["lessons"]]
        lines.append("")
    lines += ["## Atividades e artefatos", ""]
    for key, heading in (("case_studies", "Estudos de caso"), ("labs", "Laboratórios"),
                         ("assessments", "Avaliações"), ("artifacts", "Modelos de artefatos")):
        lines += [f"### {heading}", ""]
        for item in m.get(key) or []:
            title = item["title"]
            if item.get("path") and item["status"] != "planned":
                title = f"[{title}](docs/{item['path']})"
            lines.append(f"- `{item['id']}` {title} — {LABELS[item['status']]}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


# -------------------------------------------------------- execução
def targets() -> list[tuple[Path, str]]:
    m = load_manifest()
    with BIBLIOGRAPHY.open(encoding="utf-8") as fh:
        bib = yaml.safe_load(fh)
    with KNOWLEDGE_MAP.open(encoding="utf-8") as fh:
        kmap = yaml.safe_load(fh)
    results: list[tuple[Path, str]] = []

    page = DOCS / "curriculum" / "index.md"
    text = page.read_text(encoding="utf-8")
    text = splice(text, "curriculum", render_curriculum(m))
    text = splice(text, "activities", render_activities(m))
    results.append((page, text))

    page = DOCS / "curriculum" / "dependencies.md"
    results.append((page, splice(page.read_text(encoding="utf-8"), "dependencies", render_dependencies(m))))

    res = DOCS / "resources"
    text = (res / "index.md").read_text(encoding="utf-8")
    text = splice(text, "library-summary", render_library_summary(bib))
    text = splice(text, "sources", render_sources(bib))
    results.append((res / "index.md", text))
    for name, block, content in (
        ("books.md", "books", render_books(bib)),
        ("official-frameworks.md", "frameworks", render_category_pages(
            bib, ("security-engineering", "enterprise-architecture", "zero-trust", "governance-risk", "identity",
                  "application-security", "data-security", "operational-resilience"))),
        ("cloud-security.md", "cloud", render_category_pages(bib, ("cloud-security", "hybrid-multicloud"))),
        ("reference-matrix.md", "reference-matrix", render_reference_matrix(bib, kmap, m)),
        ("coverage.md", "coverage", render_coverage(bib, kmap, m)),
    ):
        page = res / name
        results.append((page, splice(page.read_text(encoding="utf-8"), block, content)))

    page = DOCS / "index.md"
    results.append((page, splice(page.read_text(encoding="utf-8"), "release-status", render_release_status(m))))

    results.append((ROOT / "CURRICULUM.md", render_root(m)))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="não escreve; falha se houver divergência")
    args = parser.parse_args()
    stale = []
    for path, content in targets():
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current != content:
            stale.append(path)
            if not args.check:
                path.write_text(content, encoding="utf-8")
                print(f"Atualizado: {path.relative_to(ROOT)}")
    if args.check:
        if stale:
            for path in stale:
                print(f"  desatualizado: {path.relative_to(ROOT)}")
            print("[FALHOU] Páginas geradas divergem do manifesto. Execute: make curriculum")
            sys.exit(1)
        print("[OK] Páginas geradas sincronizadas com o manifesto e a Research Library")


if __name__ == "__main__":
    main()
