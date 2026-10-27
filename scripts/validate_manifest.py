#!/usr/bin/env python3
"""Valida curriculum/manifest.yml (schema v2) e sua coerência com docs/ e a navegação.

Regras completas: docs/internal/content-model.md

Uso:
    python scripts/validate_manifest.py            # branches e Pull Requests
    python scripts/validate_manifest.py --release  # publicação: bloqueia draft/in-review
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from typing import Any

from _common import ROOT, STATUSES, Report, exit_with, load_config, load_manifest, nav_files, read_front_matter

MODULE_ID_RE = re.compile(r"^M(\d{2})$")
COMPLEMENT_ID_RE = re.compile(r"^C(\d{2})$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PLACEHOLDER_RE = re.compile(r"\{\{[^}]*\}\}|\bTODO\b|\bTBD\b|<PLACEHOLDER>")  # sensível a maiúsculas: "todo" é português
UNIT_FIELDS = ("id", "title", "description", "status", "last_updated")
COLLECTIONS = ("case_studies", "labs", "assessments", "artifacts")
ACTIVE = {"draft", "in-review"}
RELEASE_STATUSES = ("planned", "in-development", "in-review", "approved", "published")
RELEASE_SCOPES = ("modules", "complements") + COLLECTIONS


def unit_dir(unit: dict[str, Any], kind: str) -> str:
    """Diretório esperado (relativo a docs/) de um módulo ou complemento."""
    if kind == "module":
        number = MODULE_ID_RE.match(str(unit.get("id", ""))).group(1)  # type: ignore[union-attr]
        return f"modules/{number}-{unit.get('slug')}"
    return f"complements/{unit.get('slug')}"


class Validator:
    def __init__(self, manifest: dict[str, Any], root: Path, nav: set[str], release: bool) -> None:
        self.m = manifest
        self.root = root
        self.docs = root / "docs"
        self.nav = nav
        self.release = release
        self.report = Report("Curriculum manifest" + (" (release)" if release else ""))
        self.ids: set[str] = set()

    # -- utilitários -------------------------------------------------------
    def err(self, msg: str) -> None:
        self.report.error(msg)

    def ids_of(self, key: str) -> list[Any]:
        return [item.get("id") for item in self.m.get(key) or []]

    def unique(self, ident: str, where: str) -> None:
        if ident in self.ids:
            self.err(f"{where}: id duplicado: {ident}")
        self.ids.add(ident)

    def check_status_and_nav(self, where: str, status: str, rel: str | None) -> None:
        """Regras comuns de status × navegação × publicação."""
        if status not in STATUSES:
            self.err(f"{where}: status inválido: {status!r}")
            return
        if status == "planned":
            if rel:
                self.err(f"{where}: item 'planned' não pode ter path")
            return
        if not rel:
            self.err(f"{where}: status '{status}' exige path")
            return
        in_nav = rel in self.nav
        if status == "draft" and in_nav:
            self.err(f"{where}: conteúdo 'draft' não pode estar na navegação")
        if status == "published" and not in_nav:
            self.err(f"{where}: conteúdo publicado precisa estar em nav (zensical.toml)")
        if self.release and status in ACTIVE:
            self.err(f"{where}: status '{status}' não pode ser publicado — conclua a revisão antes do merge")

    def check_page(self, where: str, rel: str, ident: str, status: str, required: tuple[str, ...]) -> None:
        page = self.docs / rel
        if not page.is_file():
            self.err(f"{where}: arquivo não encontrado: docs/{rel}")
            return
        meta, body = read_front_matter(page)
        for field in required:
            if field not in meta:
                self.err(f"{where}: front matter de docs/{rel} sem o campo {field}")
        if "id" in meta and meta["id"] != ident:
            self.err(f"{where}: front matter id={meta['id']!r} difere do manifesto ({ident})")
        if "status" in meta and meta["status"] != status:
            self.err(f"{where}: front matter status={meta['status']!r} difere do manifesto ({status})")
        if status in {"in-review", "published"} and PLACEHOLDER_RE.search(body):
            self.err(f"{where}: docs/{rel} contém marcadores de rascunho (TODO/TBD/{{{{…}}}})")

    def check_published_meta(self, where: str, item: dict[str, Any]) -> None:
        if item.get("status") != "published":
            return
        if not item.get("reviewed_by"):
            self.err(f"{where}: item publicado exige reviewed_by")
        if not isinstance(item.get("published_on"), dt.date):
            self.err(f"{where}: item publicado exige published_on (AAAA-MM-DD)")

    # -- seções ------------------------------------------------------------
    def check_header(self) -> None:
        if self.m.get("schema_version") != 2:
            self.err("schema_version deve ser 2")
        if tuple(self.m.get("statuses") or {}) != STATUSES:
            self.err(f"statuses deve conter exatamente, nesta ordem: {', '.join(STATUSES)}")
        for key in ("tiers", "tracks", "stages", "phases", "domains"):
            if not self.m.get(key):
                self.err(f"seção obrigatória ausente ou vazia: {key}")
        tiers = set(self.ids_of("tiers"))
        for track in self.m.get("tracks") or []:
            if track.get("tier") not in tiers:
                self.err(f"trilha {track.get('id')}: tier desconhecido {track.get('tier')!r}")
        for phase in self.m.get("phases") or []:
            if phase.get("status") not in STATUSES:
                self.err(f"fase {phase.get('id')}: status inválido")

    def check_units(self, key: str, kind: str) -> dict[str, list[str]]:
        id_re = MODULE_ID_RE if kind == "module" else COMPLEMENT_ID_RE
        prefix = "módulo" if kind == "module" else "complemento"
        stages = self.ids_of("stages")
        phases = set(self.ids_of("phases"))
        domains = set(self.ids_of("domains"))
        tiers = set(self.ids_of("tiers"))
        graph: dict[str, list[str]] = {}
        slugs: set[str] = set()
        last_stage = 0
        units = self.m.get(key) or []
        if kind == "module" and not units:
            self.err("nenhum módulo definido")

        for index, unit in enumerate(units):
            uid = str(unit.get("id", f"#{index}"))
            where = f"{prefix} {uid}"
            for field in ("id", "slug", "title", "phase", "domains", "prerequisites", "status", "lessons"):
                if field not in unit:
                    self.err(f"{where}: campo obrigatório ausente: {field}")
            match = id_re.match(uid)
            expected = f"M{index:02d}" if kind == "module" else f"C{index + 1:02d}"
            if not match:
                self.err(f"{where}: id fora do padrão")
                continue
            if uid != expected:
                self.err(f"{where}: ids devem ser sequenciais (esperado {expected})")
            self.unique(uid, where)

            slug = str(unit.get("slug", ""))
            if not SLUG_RE.match(slug) or slug in slugs:
                self.err(f"{where}: slug inválido ou duplicado: {slug!r}")
            slugs.add(slug)

            if kind == "module":
                stage = unit.get("stage")
                if stage not in stages:
                    self.err(f"{where}: stage desconhecido: {stage!r}")
                else:
                    if stages.index(stage) < last_stage:
                        self.err(f"{where}: módulos devem estar ordenados por stage")
                    last_stage = stages.index(stage)
            if unit.get("phase") not in phases:
                self.err(f"{where}: fase desconhecida: {unit.get('phase')!r}")
            for dom in unit.get("domains") or []:
                if dom not in domains:
                    self.err(f"{where}: domínio desconhecido: {dom!r}")
            if not unit.get("domains"):
                self.err(f"{where}: ao menos um domínio é obrigatório")
            graph[uid] = list(unit.get("prerequisites") or [])

            status = unit.get("status")
            rel = unit.get("path")
            base = unit_dir(unit, kind)
            self.check_status_and_nav(where, status, rel)
            self.check_published_meta(where, unit)
            if status == "planned" and (self.docs / base).exists():
                self.err(f"{where}: 'planned', mas docs/{base} existe — atualize o status")
            if rel and status != "planned":
                if rel != f"{base}/index.md":
                    self.err(f"{where}: path deve ser {base}/index.md")
                self.check_page(where, rel, uid, status, UNIT_FIELDS)

            lessons = unit.get("lessons") or []
            if not lessons:
                self.err(f"{where}: nenhuma aula definida")
            for n, lesson in enumerate(lessons, start=1):
                lid = str(lesson.get("id"))
                lwhere = f"aula {lid}"
                if lid != f"{uid}-L{n:02d}":
                    self.err(f"{lwhere}: esperado {uid}-L{n:02d}")
                self.unique(lid, lwhere)
                if lesson.get("tier") not in tiers:
                    self.err(f"{lwhere}: tier desconhecido: {lesson.get('tier')!r}")
                minutes = lesson.get("minutes")
                if not isinstance(minutes, int) or minutes <= 0:
                    self.err(f"{lwhere}: minutes deve ser inteiro positivo")
                lstatus = lesson.get("status")
                lrel = f"{base}/{lesson['file']}" if lesson.get("file") else None
                self.check_status_and_nav(lwhere, lstatus, lrel)
                self.check_published_meta(lwhere, lesson)
                if lrel and lstatus != "planned":
                    self.check_page(lwhere, lrel, lid, lstatus, UNIT_FIELDS + ("tier", "prerequisites", "objectives"))
                if status in {"in-review", "published"} and lstatus in {"planned", "draft"}:
                    self.err(f"{lwhere}: módulo '{status}' não pode ter aula '{lstatus}'")
        return graph

    def check_graph(self, graph: dict[str, list[str]]) -> None:
        known = set(graph)
        for uid, deps in graph.items():
            for dep in deps:
                if dep not in known:
                    self.err(f"{uid}: pré-requisito desconhecido: {dep}")
                if dep == uid:
                    self.err(f"{uid}: não pode depender de si mesmo")
        state: dict[str, int] = {}

        def visit(node: str, trail: list[str]) -> None:
            if state.get(node) == 1:
                self.err("dependência circular: " + " → ".join(trail + [node]))
                return
            if state.get(node) == 2:
                return
            state[node] = 1
            for dep in graph.get(node, []):
                if dep in graph:
                    visit(dep, trail + [node])
            state[node] = 2

        for node in graph:
            visit(node, [])

    def check_collections(self) -> None:
        modules = set(self.ids_of("modules"))
        phases = set(self.ids_of("phases"))
        for key in COLLECTIONS:
            for item in self.m.get(key) or []:
                iid = str(item.get("id"))
                where = f"{key} {iid}"
                self.unique(iid, where)
                if not item.get("title"):
                    self.err(f"{where}: título obrigatório")
                if item.get("phase") not in phases:
                    self.err(f"{where}: fase desconhecida: {item.get('phase')!r}")
                for mod in item.get("modules") or []:
                    if mod not in modules:
                        self.err(f"{where}: módulo desconhecido: {mod}")
                status = item.get("status")
                rel = item.get("path")
                self.check_status_and_nav(where, status, rel)
                self.check_published_meta(where, item)
                if rel and status != "planned":
                    self.check_page(where, rel, iid, status, ("title", "description"))
                answers = item.get("answers")
                if key == "assessments" and status != "planned":
                    if not answers:
                        self.err(f"{where}: avaliação exige arquivo de gabarito separado (answers)")
                    elif not (self.docs / answers).is_file():
                        self.err(f"{where}: gabarito não encontrado: docs/{answers}")
                if key == "labs" and item.get("tested") and status == "planned":
                    self.err(f"{where}: laboratório planejado não pode estar marcado como testado")

    def check_releases(self) -> None:
        """Seção opcional `releases`: escopos válidos, sem sobreposição, e coerência de status.

        Uma release `published` exige aprovação registrada pelo mantenedor, datas, URL e
        todo o seu escopo publicado. Uma release `approved` exige aprovação registrada.
        """
        releases = self.m.get("releases")
        if releases is None:
            return
        known = {key: {str(i.get("id")) for i in self.m.get(key) or []} for key in RELEASE_SCOPES}
        status_of = {str(i.get("id")): i.get("status") for key in RELEASE_SCOPES for i in self.m.get(key) or []}
        seen: dict[str, str] = {}
        for rel in releases:
            rid = str(rel.get("id"))
            where = f"release {rid}"
            self.unique(rid, where)
            status = rel.get("status")
            if status not in RELEASE_STATUSES:
                self.err(f"{where}: status inválido {status!r} (use {', '.join(RELEASE_STATUSES)})")
            if not re.fullmatch(r"\d+\.\d+\.\d+", str(rel.get("version", ""))):
                self.err(f"{where}: version deve seguir MAJOR.MINOR.PATCH")
            items = []
            for key in RELEASE_SCOPES:
                for iid in rel.get(key) or []:
                    iid = str(iid)
                    if iid not in known[key]:
                        self.err(f"{where}: {key} desconhecido: {iid}")
                    if iid in seen:
                        self.err(f"{where}: {iid} já pertence à release {seen[iid]}")
                    seen[iid] = rid
                    items.append(iid)
            if not rel.get("modules") and not rel.get("complements"):
                self.err(f"{where}: escopo sem módulos")
            candidate = rel.get("candidate")
            if candidate and not str(candidate).startswith(f"v{rel.get('version')}-"):
                self.err(f"{where}: candidate deve ser uma pré-versão de v{rel.get('version')} (ex.: v{rel.get('version')}-rc1)")
            source = rel.get("approved_source_commit")
            if source and not re.fullmatch(r"[0-9a-f]{40}", str(source)):
                self.err(f"{where}: approved_source_commit deve ser o SHA completo (40 caracteres) do commit aprovado")
            if status in {"approved", "published"}:
                if not source:
                    self.err(f"{where}: status '{status}' exige approved_source_commit (commit exato revisado pelo mantenedor)")
                if not rel.get("approved_by"):
                    self.err(f"{where}: status '{status}' exige approved_by (registrado pelo mantenedor)")
                if not isinstance(rel.get("approved_on"), dt.date):
                    self.err(f"{where}: status '{status}' exige approved_on (AAAA-MM-DD)")
            if status == "published":
                if not isinstance(rel.get("published_on"), dt.date):
                    self.err(f"{where}: release publicada exige published_on (AAAA-MM-DD)")
                if not str(rel.get("url") or "").startswith("https://"):
                    self.err(f"{where}: release publicada exige a URL pública confirmada")
                for iid in items:
                    if status_of.get(iid) != "published":
                        self.err(f"{where}: {iid} não está 'published' no manifesto")
            elif rel.get("published_on") or rel.get("url") or rel.get("public_commit"):
                self.err(f"{where}: published_on, url e public_commit só podem ser preenchidos após a publicação")

    def run(self) -> Report:
        self.check_header()
        graph = self.check_units("modules", "module")
        graph.update(self.check_units("complements", "complement"))
        self.check_graph(graph)
        self.check_collections()
        self.check_releases()
        domains = set(self.ids_of("domains"))
        used = {d for key in ("modules", "complements") for u in self.m.get(key) or [] for d in u.get("domains") or []}
        for dom in sorted(domains - used):
            self.report.warn(f"domínio sem módulos: {dom}")
        return self.report


def validate(manifest: dict[str, Any], root: Path = ROOT, nav: set[str] | None = None, release: bool = False) -> Report:
    return Validator(manifest, root, nav or set(), release).run()


def summary(manifest: dict[str, Any]) -> str:
    counts: dict[str, int] = {}
    lessons = 0
    for mod in manifest.get("modules") or []:
        counts[mod.get("status", "?")] = counts.get(mod.get("status", "?"), 0) + 1
        lessons += len(mod.get("lessons") or [])
    return f"  módulos: {', '.join(f'{k}={v}' for k, v in sorted(counts.items()))}; aulas planejadas: {lessons}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", action="store_true", help="regras de publicação (bloqueia draft/in-review)")
    args = parser.parse_args()
    manifest = load_manifest()
    report = validate(manifest, ROOT, nav_files(load_config()), args.release)
    print(summary(manifest))
    exit_with(report)


if __name__ == "__main__":
    main()
