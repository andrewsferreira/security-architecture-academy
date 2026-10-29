#!/usr/bin/env python3
"""Gera a árvore pública de uma release — somente o conteúdo do escopo aprovado.

O repositório de desenvolvimento contém todo o trabalho (inclusive módulos em
revisão e rascunhos). O repositório público recebe apenas a árvore gerada por
este script, que contém o escopo **cumulativo** das releases até a indicada
(R1; R1+R2; …), as páginas institucionais e a infraestrutura do portal.

Modos:
    --mode candidate  Árvore para revisão do mantenedor. Status permanecem
                      'in-review'; valida com as regras de branch.
    --mode final      Árvore de publicação. Exige release 'approved' com
                      approved_by/approved_on preenchidos pelo mantenedor; marca o
                      escopo como 'published' e valida com --release.

Uso:
    python scripts/export_release.py --release R1 --mode candidate --out build/public
    python scripts/export_release.py --release R1 --mode final --out build/public

Seleção dos arquivos (nesta ordem):
    1. Somente arquivos versionados (git ls-files) — nunca a pasta .git.
    2. Allowlist explícita (curriculum/public-allowlist.yml): o que não está nela
       fica só no desenvolvimento (relatórios de processo, arquivos locais).
    3. Escopo cumulativo da release, pelo manifesto: módulos, atividades,
       diagramas e conceitos de releases futuras são removidos.

A árvore recebe RELEASE-MANIFEST.yml: versão, escopo (aulas, laboratórios,
avaliações, diagramas, referências), aprovação, commit privado de origem e o
SHA-256 de cada arquivo — verificado por scripts/verify_release_manifest.py no
CI e no deploy do repositório público.

O CHANGELOG exportado traz só a versão da release e as já publicadas: notas em
*Unreleased* e seções pendentes de outras versões ficam no desenvolvimento. No
modo final, o cabeçalho "## [X.Y.Z] — não publicada" da versão recebe a data de
aprovação (contrato em scripts/check_changelog.py).

No modo final, o commit aprovado (approved_source_commit) é conferido: entre
ele e o HEAD só podem mudar o manifesto e as páginas geradas a partir dele, e
os arquivos exportados não podem ter alterações não commitadas.

O script nunca altera o repositório de desenvolvimento: escreve apenas em
--out, que precisa estar vazio ou não existir. Ao final, executa as validações
dentro da árvore gerada (--no-validate para pular), incluindo a verificação de
atribuição de autoria na árvore e no site compilado.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

from _common import DEVELOPMENT_REPOSITORY, PUBLIC_REPOSITORY, publication_target, release_publications
from check_changelog import release_changelog

ROOT = Path(__file__).resolve().parent.parent
SCOPES = ("modules", "complements", "case_studies", "labs", "assessments", "artifacts")
COLLECTIONS = ("case_studies", "labs", "assessments", "artifacts")
NAV_ITEM_RE = re.compile(r'^\s*(?:\{ "[^"]+" = )?"([^"]+\.md)"(?: \})?,?\s*$')
EMPTY_GROUP_RE = re.compile(r'^[ \t]*\{ "[^"]+" = \[\n[ \t]*\] \},\n', re.MULTILINE)
DIAGRAM_MODULE_RE = re.compile(r"^m(\d{2})-")
STATUS_LINE_RE = re.compile(r"^status: in-review$", re.MULTILINE)
REVIEWED_RE = re.compile(r"^reviewed_by: \[\]$", re.MULTILINE)
REVIEW_ROW = "| Revisão técnica | Pendente — aguardando revisão do mantenedor |"
BADGE_IN_REVIEW = '<span class="saa-status saa-status--in-review">In Review</span>'
BADGE_PUBLISHED = '<span class="saa-status saa-status--published">Published</span>'


ALLOWLIST = Path("curriculum") / "public-allowlist.yml"
RELEASE_MANIFEST = "RELEASE-MANIFEST.yml"
GENERATED = {
    "CURRICULUM.md", "docs/index.md", "docs/curriculum/index.md", "docs/curriculum/dependencies.md",
    "docs/resources/index.md", "docs/resources/books.md", "docs/resources/official-frameworks.md",
    "docs/resources/cloud-security.md", "docs/resources/reference-matrix.md", "docs/resources/coverage.md",
}
CHANGEABLE_AFTER_APPROVAL = GENERATED | {"curriculum/manifest.yml"}
PRIVATE_REPOSITORY = DEVELOPMENT_REPOSITORY
PUBLIC_TREE = PUBLIC_REPOSITORY  # a árvore exportada é verificada com as regras do repositório público


class ExportError(Exception):
    pass


def load_allowlist(root: Path = ROOT) -> dict[str, list[str]]:
    data = yaml.safe_load((root / ALLOWLIST).read_text(encoding="utf-8")) or {}
    return {"files": list(data.get("files") or []), "directories": list(data.get("directories") or []),
            "exclude": list(data.get("exclude") or [])}


def is_public(rel: str, allow: dict[str, list[str]]) -> bool:
    """Arquivo pode ir ao repositório público? ``exclude`` aceita caminhos exatos e diretórios (terminados em /)."""
    for item in allow.get("exclude", []):
        if rel == item or (item.endswith("/") and rel.startswith(item)):
            return False
    return rel in allow["files"] or any(rel.startswith(d) for d in allow["directories"])


def git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    if result.returncode != 0:
        raise ExportError(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout.strip()


def check_approved_commit(root: Path, release: dict[str, Any], exported: list[str]) -> str:
    """Garante que a árvore final corresponde ao commit revisado pelo mantenedor."""
    approved = str(release.get("approved_source_commit") or "")
    if not re.fullmatch(r"[0-9a-f]{40}", approved):
        raise ExportError("modo final exige approved_source_commit (SHA completo do commit revisado pelo mantenedor)")
    git(root, "cat-file", "-e", f"{approved}^{{commit}}")
    changed = set(filter(None, git(root, "diff", "--name-only", approved, "HEAD").splitlines()))
    unexpected = sorted((changed & set(exported)) - CHANGEABLE_AFTER_APPROVAL)
    if unexpected:
        raise ExportError("arquivos exportados mudaram depois do commit aprovado: " + ", ".join(unexpected[:10]))
    dirty_paths = set(filter(None, git(root, "diff", "--name-only", "HEAD").splitlines()))
    if dirty_paths & set(exported):
        raise ExportError("há alterações não commitadas em arquivos exportados: "
                          + ", ".join(sorted(dirty_paths & set(exported))[:10]))
    return approved


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def release_manifest(manifest: dict[str, Any], release: dict[str, Any], scope: dict[str, set[str]],
                     mode: str, out: Path, source: dict[str, Any]) -> dict[str, Any]:
    """Manifesto da publicação gerada — a versão inicial da release ou a versão de correção em preparo.

    ``history`` lista as publicações anteriores da mesma release (versão, datas e commits), sem alterá-las.
    """
    records = release_publications(release)
    target = records[-1]
    """Manifesto de publicação gravado na raiz da árvore exportada."""
    units = [u for key in ("modules", "complements") for u in manifest.get(key) or [] if str(u["id"]) in scope[key]]
    lessons, refs = [], set()
    for unit in units:
        for lesson in unit.get("lessons") or []:
            lessons.append({"id": lesson["id"], "title": lesson.get("title"), "status": lesson.get("status")})
            if lesson.get("file"):
                page = out / unit_dir(unit) / lesson["file"]
                if page.is_file():
                    front = page.read_text(encoding="utf-8").split("---", 2)[1]
                    data = yaml.safe_load(front) or {}
                    refs.update(str(r) for r in (data.get("sources") or []) + (data.get("further_reading") or []))
    collections = {key: [{"id": i["id"], "title": i.get("title"), "status": i.get("status")}
                         for i in manifest.get(key) or [] if str(i["id"]) in scope[key]] for key in COLLECTIONS}
    files = {}
    for path in sorted(out.rglob("*")):
        rel = path.relative_to(out).as_posix()
        if path.is_file() and rel != RELEASE_MANIFEST:
            files[rel] = sha256(path)
    approved = mode == "final"
    history = [{"version": str(r["version"]), "kind": r["kind"], "published_on": _iso(r.get("published_on")),
                "approved_source_commit": r.get("approved_source_commit"), "public_commit": r.get("public_commit")}
               for r in records[:-1]]
    return {
        "schema_version": 1,
        "release": release["id"],
        "version": str(target["version"]),
        "tag": f"v{target['version']}",
        "kind": target["kind"],
        "candidate": target.get("candidate"),
        "title": target.get("title") or release.get("title"),
        "mode": mode,
        "status": target.get("status"),
        "levels": sorted({str(u.get("stage")) for u in units}),
        "scope": {
            "modules": [{"id": u["id"], "title": u.get("title"), "status": u.get("status"),
                         "prerequisites": u.get("prerequisites") or []} for u in units],
            "lessons": lessons,
            **collections,
        },
        "diagrams": sorted(p.stem for p in (out / "assets" / "diagrams").glob("*.mmd")),
        "references": sorted(refs),
        "editorial_state": "approved" if approved else "in-review — aguardando revisão do mantenedor",
        "technical_state": "validado pela exportação (ver validações na árvore)",
        "approval": {
            "approved_by": list(target.get("approved_by") or []),
            "approved_on": _iso(target.get("approved_on")),
            "approved_source_commit": target.get("approved_source_commit"),
        },
        "source": source,
        "public_commit": target.get("public_commit"),
        "publication": {"published_on": _iso(target.get("published_on")), "url": target.get("url")},
        # Campos que só existem depois desta árvore: não são preenchidos aqui nem alterados depois
        # (o commit público é imutável e os hashes não mudam).
        "post_export": {
            "fields": [name for name, value in (("public_commit", target.get("public_commit")),
                                                ("publication.published_on", target.get("published_on")),
                                                ("publication.url", target.get("url"))) if not value],
            "note": ("Conhecidos só depois do commit público e do deploy desta árvore. Ficam registrados no "
                     "manifesto do repositório de desenvolvimento e chegam às árvores exportadas depois "
                     "desta: em curriculum/manifest.yml e, nas correções seguintes da mesma release, em "
                     "'history'."),
        },
        "history": history,
        "files": files,
    }


def _iso(value: Any) -> Any:
    return value.isoformat() if isinstance(value, dt.date) else value


# ----------------------------------------------------------------- escopo
def load_manifest(root: Path = ROOT) -> dict[str, Any]:
    return yaml.safe_load((root / "curriculum" / "manifest.yml").read_text(encoding="utf-8"))


def cumulative_scope(manifest: dict[str, Any], release_id: str) -> dict[str, set[str]]:
    """Escopo acumulado das releases da primeira até `release_id`, inclusive."""
    releases = manifest.get("releases") or []
    ids = [str(r.get("id")) for r in releases]
    if release_id not in ids:
        raise ExportError(f"release desconhecida: {release_id} (disponíveis: {', '.join(ids)})")
    scope: dict[str, set[str]] = {key: set() for key in SCOPES}
    for rel in releases[: ids.index(release_id) + 1]:
        for key in SCOPES:
            scope[key].update(str(x) for x in rel.get(key) or [])
    return scope


def unit_dir(unit: dict[str, Any]) -> str:
    uid = str(unit["id"])
    if uid.startswith("M"):
        return f"docs/modules/{uid[1:]}-{unit['slug']}"
    return f"docs/complements/{unit['slug']}"


def excluded_paths(manifest: dict[str, Any], scope: dict[str, set[str]]) -> tuple[list[str], set[str]]:
    """Retorna (prefixos de caminho a excluir, números de módulo fora do escopo)."""
    prefixes: list[str] = []
    out_modules: set[str] = set()
    for key in ("modules", "complements"):
        for unit in manifest.get(key) or []:
            if str(unit["id"]) not in scope[key]:
                prefixes.append(unit_dir(unit) + "/")
                if key == "modules":
                    out_modules.add(str(unit["id"])[1:])
    for key in COLLECTIONS:
        for item in manifest.get(key) or []:
            if str(item["id"]) in scope[key] or not item.get("path"):
                continue
            path = f"docs/{item['path']}"
            prefixes.append(path.rsplit("/", 1)[0] + "/" if path.endswith("/index.md") else path)
            if item.get("answers"):
                prefixes.append(f"docs/{item['answers']}")
            if key == "labs":
                prefixes.append(f"examples/{Path(item['path']).stem}/")
    return prefixes, out_modules


def tracked_files(root: Path) -> list[str]:
    result = subprocess.run(["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True)
    return [p for p in result.stdout.decode("utf-8").split("\0") if p]


def is_excluded(rel: str, prefixes: list[str], out_modules: set[str]) -> bool:
    if any(rel == p or rel.startswith(p) for p in prefixes if p.endswith("/")) or rel in prefixes:
        return True
    if rel.startswith("assets/diagrams/"):
        match = DIAGRAM_MODULE_RE.match(Path(rel).name)
        return bool(match and match.group(1) in out_modules)
    return False


# ------------------------------------------------------------- transformações
def transform_manifest(manifest: dict[str, Any], scope: dict[str, set[str]], mode: str,
                       release: dict[str, Any]) -> dict[str, Any]:
    """Manifesto público. No modo final, itens do escopo passam a ``published``.

    Itens já publicados conservam a data e os revisores da publicação original; só itens publicados
    pela primeira vez recebem a data e os aprovadores desta publicação (inicial ou de correção).
    """
    target = publication_target(release)
    approvers = list(target.get("approved_by") or [])
    date = target.get("approved_on")

    def publish(item: dict[str, Any]) -> None:
        first = item.get("status") != "published" or not item.get("published_on")
        item["status"] = "published"
        if first:
            item["published_on"] = date
            item["reviewed_by"] = approvers

    for key in ("modules", "complements"):
        for unit in manifest.get(key) or []:
            inside = str(unit["id"]) in scope[key]
            if not inside:
                unit["status"] = "planned"
                for field in ("path", "published_on", "reviewed_by"):
                    unit.pop(field, None)
                for lesson in unit.get("lessons") or []:
                    lesson["status"] = "planned"
                    for field in ("file", "published_on", "reviewed_by"):
                        lesson.pop(field, None)
            elif mode == "final":
                for item in [unit] + list(unit.get("lessons") or []):
                    if item.get("status") in {"in-review", "published"}:
                        publish(item)
    for key in COLLECTIONS:
        for item in manifest.get(key) or []:
            if str(item["id"]) not in scope[key]:
                item["status"] = "planned"
                for field in ("path", "answers", "tested", "published_on", "reviewed_by"):
                    item.pop(field, None)
            elif mode == "final" and item.get("status") in {"in-review", "published"}:
                publish(item)
    return manifest


def transform_knowledge_map(kmap: dict[str, Any], scope: dict[str, set[str]], out: Path) -> dict[str, Any]:
    """Remove do mapa de conhecimento os conceitos ligados só a aulas fora do escopo.

    Conceitos sem aula associada (orientação de pesquisa) permanecem. Nos demais,
    ficam apenas as aulas do escopo e os diagramas presentes na árvore pública.
    """
    units = scope["modules"] | scope["complements"]
    kept = []
    for original in kmap.get("concepts") or []:
        concept = dict(original)
        lessons = list(concept.get("lessons") or [])
        if lessons:
            inside = [lid for lid in lessons if str(lid).split("-", 1)[0] in units]
            if not inside:
                continue
            concept["lessons"] = inside
        if concept.get("diagrams"):
            concept["diagrams"] = [d for d in concept["diagrams"]
                                   if (out / "assets" / "diagrams" / f"{d}.mmd").is_file()]
        kept.append(concept)
    return {**kmap, "concepts": kept}


def transform_nav(config_text: str, out: Path) -> str:
    lines = []
    for line in config_text.splitlines(keepends=True):
        match = NAV_ITEM_RE.match(line)
        if match and not match.group(1).startswith(("http://", "https://")) and not (out / "docs" / match.group(1)).is_file():
            continue
        lines.append(line)
    text = "".join(lines)
    while True:
        new = EMPTY_GROUP_RE.sub("", text)
        if new == text:
            return text
        text = new


def publish_changelog(text: str, version: str, date: dt.date | None) -> str:
    """CHANGELOG exportado: só a versão da release e as já publicadas (ver check_changelog.release_changelog).

    No desenvolvimento, a versão em preparo tem o cabeçalho ``## [X.Y.Z] — não publicada`` desde o
    commit submetido à aprovação; a árvore final recebe a data da release (``approved_on``). O commit
    aprovado não é alterado, e a árvore pública nunca descreve a versão publicada como pendente.
    """
    try:
        return release_changelog(text, version, date)
    except ValueError as exc:
        raise ExportError(str(exc)) from exc


def publish_page(text: str, approvers: list[str], date: dt.date, rel: str = "") -> str:
    """Marca como publicada uma página do escopo aprovado.

    Não altera o Handbook (``docs/internal/``), que documenta os status, nem as linhas de
    tabela em que o selo é a primeira célula: são definições de status (legendas), não o
    estado de um item.
    """
    if rel.startswith("docs/internal/"):
        return text
    text = STATUS_LINE_RE.sub("status: published", text, count=1)
    names = ", ".join(approvers)
    text = REVIEWED_RE.sub(f"reviewed_by: [{names}]", text, count=1)
    text = text.replace(REVIEW_ROW, f"| Revisão técnica | {names} — {date.isoformat()} |")
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if BADGE_IN_REVIEW in line and not line.lstrip().startswith("| " + BADGE_IN_REVIEW):
            lines[i] = line.replace(BADGE_IN_REVIEW, BADGE_PUBLISHED)
    return "\n".join(lines)


# ---------------------------------------------------------------- execução
def export(release_id: str, mode: str, out: Path, root: Path = ROOT) -> dict[str, Any]:
    if mode not in {"candidate", "final"}:
        raise ExportError("mode deve ser 'candidate' ou 'final'")
    manifest = load_manifest(root)
    release = next((r for r in manifest.get("releases") or [] if str(r.get("id")) == release_id), None)
    scope = cumulative_scope(manifest, release_id)
    pub = publication_target(release)
    label = f"{release_id} v{pub['version']}"
    if mode == "final":
        if pub.get("status") not in {"approved", "published"}:
            raise ExportError(f"{label}: modo final exige publicação 'approved' (atual: {pub.get('status')!r}) — "
                              "a aprovação é registrada pelo mantenedor no manifesto")
        if not pub.get("approved_by") or not isinstance(pub.get("approved_on"), dt.date):
            raise ExportError(f"{label}: approved_by e approved_on precisam estar preenchidos pelo mantenedor")
    if out.exists() and any(out.iterdir()):
        raise ExportError(f"{out} não está vazio — escolha um diretório novo")

    prefixes, out_modules = excluded_paths(manifest, scope)
    allow = load_allowlist(root)
    copied, skipped, not_allowed = [], [], []
    for rel in tracked_files(root):
        source = root / rel
        if not source.is_file():
            continue
        if not is_public(rel, allow):
            not_allowed.append(rel)
            continue
        if rel.startswith(("private-research/", "site/")) and rel != "private-research/README.md":
            skipped.append(rel)
            continue
        if is_excluded(rel, prefixes, out_modules):
            skipped.append(rel)
            continue
        target = out / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        copied.append(rel)

    public_manifest = transform_manifest(yaml.safe_load((root / "curriculum" / "manifest.yml").read_text(encoding="utf-8")),
                                         scope, mode, release)
    header = ("# Manifesto público gerado por scripts/export_release.py — "
              f"escopo cumulativo até {release_id} ({mode}). Não editar: a fonte é o repositório de desenvolvimento.\n")
    (out / "curriculum" / "manifest.yml").write_text(
        header + yaml.safe_dump(public_manifest, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    kmap_path = root / "research" / "knowledge-map.yml"
    if kmap_path.is_file():
        public_kmap = transform_knowledge_map(yaml.safe_load(kmap_path.read_text(encoding="utf-8")), scope, out)
        (out / "research" / "knowledge-map.yml").write_text(
            f"# Mapa de conhecimento público gerado por scripts/export_release.py — escopo até {release_id}.\n"
            + yaml.safe_dump(public_kmap, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    (out / "zensical.toml").write_text(transform_nav((root / "zensical.toml").read_text(encoding="utf-8"), out),
                                       encoding="utf-8")
    if mode == "final":
        approvers = list(pub["approved_by"])
        for page in (out / "docs").rglob("*.md"):
            text = page.read_text(encoding="utf-8")
            new = publish_page(text, approvers, pub["approved_on"], page.relative_to(out).as_posix())
            if new != text:
                page.write_text(new, encoding="utf-8")

    changelog = out / "CHANGELOG.md"
    changelog.write_text(publish_changelog(changelog.read_text(encoding="utf-8"), str(pub["version"]),
                                           pub["approved_on"] if mode == "final" else None), encoding="utf-8")

    # Páginas geradas refletem o manifesto público antes do cálculo dos hashes.
    render = subprocess.run([sys.executable, "scripts/render_curriculum.py"], cwd=out, capture_output=True, text=True)
    if render.returncode != 0:
        raise ExportError(f"render_curriculum.py na árvore exportada: {render.stdout[-500:]}{render.stderr[-500:]}")
    for cache in out.rglob("__pycache__"):
        shutil.rmtree(cache)

    approved_commit = check_approved_commit(root, pub, copied) if mode == "final" else None
    head = git(root, "rev-parse", "HEAD")
    dirty = bool(git(root, "status", "--porcelain", "--untracked-files=no"))
    source = {"repository": PRIVATE_REPOSITORY, "commit": head, "dirty": dirty,
              "approved_source_commit": approved_commit}
    data = release_manifest(yaml.safe_load((out / "curriculum" / "manifest.yml").read_text(encoding="utf-8")),
                            release, scope, mode, out, source)
    (out / RELEASE_MANIFEST).write_text(
        "# Gerado por scripts/export_release.py — não editar. Verificado por scripts/verify_release_manifest.py.\n"
        + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    return {"copied": copied, "skipped": skipped, "not_allowed": not_allowed, "scope": scope, "source": source}


def scope_findings(out: Path, mode: str) -> list[str]:
    """Verificações próprias da árvore exportada, além dos validadores do portal."""
    findings: list[str] = []
    for page in (out / "docs").rglob("*.md"):
        text = page.read_text(encoding="utf-8")
        rel = page.relative_to(out).as_posix()
        if re.search(r"^status: draft$", text, re.MULTILINE):
            findings.append(f"{rel}: rascunho na árvore pública")
        if mode == "final" and re.search(r"^status: in-review$", text, re.MULTILINE):
            findings.append(f"{rel}: 'in-review' na árvore de publicação")
    for pattern in ("*.pdf", "*.epub"):
        findings += [f"{p.relative_to(out)}: obra de terceiros não pode ser publicada" for p in out.rglob(pattern)]
    return findings


def run_validations(out: Path, mode: str, python: str) -> list[tuple[str, int]]:
    release_flag = ["--release"] if mode == "final" else []
    steps = [
        ["scripts/verify_release_manifest.py", "--repository", PUBLIC_TREE,
         *(["--require-approval"] if mode == "final" else [])],
        # versão-alvo: a do RELEASE-MANIFEST.yml da árvore
        ["scripts/check_changelog.py", "--rules", "release" if mode == "final" else "development"],
        ["scripts/check_attribution.py", "--path", "."],
        ["scripts/check_structure.py", *release_flag],
        ["scripts/validate_manifest.py", *release_flag],
        ["scripts/render_curriculum.py", "--check"],
        ["scripts/check_assets.py"],
        ["scripts/check_contrast.py"],
        ["scripts/check_decision_matrices.py"],
        ["scripts/validate_references.py"],
        ["-m", "zensical", "build", "--clean"],
        ["scripts/check_links.py"],
        ["scripts/check_attribution.py", "--path", "site"],
        ["-m", "pytest", "-q", "-p", "no:cacheprovider", "tests", "examples"],
    ]
    results = []
    for step in steps:
        proc = subprocess.run([python, *step], cwd=out, capture_output=True, text=True)
        results.append((" ".join(step), proc.returncode))
        if proc.returncode != 0:
            sys.stdout.write(proc.stdout[-3000:] + proc.stderr[-3000:])
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--release", required=True, help="id da release (R1 a R6)")
    parser.add_argument("--mode", choices=["candidate", "final"], default="candidate")
    parser.add_argument("--out", required=True, type=Path, help="diretório de saída (novo ou vazio)")
    parser.add_argument("--no-validate", action="store_true", help="não executa as validações na árvore gerada")
    args = parser.parse_args(argv)
    try:
        result = export(args.release, args.mode, args.out.resolve())
    except ExportError as exc:
        print(f"[FALHOU] {exc}")
        return 2
    print(f"Árvore {args.mode} de {args.release} em {args.out}: {len(result['copied'])} arquivos copiados, "
          f"{len(result['skipped'])} fora do escopo da release, {len(result['not_allowed'])} fora da allowlist pública.")
    for rel in result["not_allowed"]:
        print(f"  só no desenvolvimento: {rel}")
    src = result["source"]
    print(f"  commit de origem: {src['commit']}{' (com alterações não commitadas)' if src['dirty'] else ''}")
    for key in SCOPES:
        if result["scope"][key]:
            print(f"  {key}: {', '.join(sorted(result['scope'][key]))}")
    findings = scope_findings(args.out.resolve(), args.mode)
    for finding in findings:
        print("  ERRO:", finding)
    failed = bool(findings)
    if not args.no_validate:
        for step, code in run_validations(args.out.resolve(), args.mode, sys.executable):
            print(f"  [{'OK' if code == 0 else 'FALHOU'}] {step}")
            failed |= code != 0
    print("[FALHOU] Árvore de release inválida" if failed else "[OK] Árvore de release válida")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
