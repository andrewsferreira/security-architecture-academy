#!/usr/bin/env python3
"""Verifica a ausência de créditos de autoria atribuídos a ferramentas de IA.

Política do projeto (PROJECT-STANDARDS.md, "Autoria e créditos"): nenhum
arquivo, página compilada ou metadado sob controle do projeto apresenta
assistentes ou ferramentas de IA como autores, coautores, colaboradores ou
geradores do conteúdo, e arquivos de instrução de agentes não são versionados.

O que é verificado:

* **Arquivos de instrução de agentes** (CLAUDE.md, AGENTS.md, GEMINI.md,
  .claude/, .cursor/, .github/copilot-instructions.md…) — erro.
* **Expressões de crédito**: "Co-authored-by" de ferramenta, "Generated with",
  "gerado por IA", "AI-assisted", "Powered by <ferramenta>" e equivalentes,
  em português e inglês — erro.
* **Mensagens e autores de commits** (``--commits``): trailers de coautoria,
  links de sessão e autores que não são pessoas — erro.
* **Menções simples** a nomes de ferramentas (por exemplo, um produto citado
  em uma aula) — apenas listadas para revisão manual, sem erro: o ensino de
  segurança de IA e a citação de produtos são legítimos.

Ocorrências legítimas que casem com uma expressão de crédito (por exemplo, uma
aula sobre código gerado por IA) são registradas em
``scripts/attribution_allowlist.yml`` com caminho, trecho e justificativa.

Uso:
    python scripts/check_attribution.py                      # arquivos versionados
    python scripts/check_attribution.py --path site          # árvore qualquer (ex.: site compilado)
    python scripts/check_attribution.py --commits main..HEAD # mensagens e autores de commits
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

from _common import ROOT, Report

TOOLS = (r"claude(?:[ -]code)?|anthropic|chat-?gpt|openai|gpt-?\d[\w.-]*|copilot|gemini|cursor(?: ai)?"
         r"|codeium|windsurf|tabnine|devin|grok|deepseek|perplexity")
AI_WORDS = rf"(?:{TOOLS}|\bia\b|\bai\b|intelig[êe]ncia artificial|artificial intelligence|\bllms?\b|um assistente|an assistant)"
CREDIT_VERBS = (r"co-?authored-by|generated (?:with|by|using)|created (?:with|by|using)|written (?:with|by)"
                r"|built with|powered by|assisted by|made with|developed with|authored by"
                r"|gerad[oa]s? (?:com|por|pel[oa])|criad[oa]s? (?:com|por|pel[oa])|escrit[oa]s? (?:com|por|pel[oa])"
                r"|produzid[oa]s? (?:com|por|pel[oa])|revisad[oa]s? (?:com|por|pel[oa])|elaborad[oa]s? (?:com|por|pel[oa])"
                r"|com (?:o |a )?(?:aux[íi]lio|ajuda|apoio|assist[êe]ncia) d[eoa]s?")

CREDIT_PATTERNS = [
    re.compile(rf"(?:{CREDIT_VERBS})\W+(?:\S+\W+){{0,3}}?{AI_WORDS}", re.IGNORECASE),
    re.compile(r"\bai[- ](?:assisted|generated|powered)\b|assistid[oa]s? por ia|gerad[oa]s? por ia", re.IGNORECASE),
    re.compile(r"claude\.ai/code|claude-session|noreply@anthropic\.com|🤖", re.IGNORECASE),
]
MENTION_RE = re.compile(rf"\b(?:{TOOLS})\b", re.IGNORECASE)
AGENT_PATH_RE = re.compile(
    r"(?:^|/)(?:CLAUDE\.md|CLAUDE\.local\.md|AGENTS\.md|GEMINI\.md|\.cursorrules|\.windsurfrules|copilot-instructions\.md)$"
    r"|(?:^|/)\.(?:claude|cursor|aider[^/]*|continue|codeium)(?:/|$)",
    re.IGNORECASE)
BOT_AUTHOR_RE = re.compile(rf"{TOOLS}|\[bot\]|noreply@anthropic", re.IGNORECASE)

TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml", ".toml", ".json", ".py", ".js", ".css", ".html", ".htm",
                 ".xml", ".svg", ".mmd", ".cfg", ".ini", ".jsonc", ".sh", ".gitignore", ".gitattributes",
                 ".editorconfig", ""}
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", ".cache", "__pycache__", ".pytest_cache"}
ALLOWLIST = ROOT / "scripts" / "attribution_allowlist.yml"
# A própria verificação contém as expressões que procura.
SELF_FILES = {"scripts/check_attribution.py", "scripts/attribution_allowlist.yml", "tests/test_attribution.py"}


def load_allowlist(path: Path = ALLOWLIST) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return list(data.get("allow") or [])


def allowed(rel: str, line: str, allowlist: list[dict[str, str]]) -> bool:
    return any(rel == item.get("path") and item.get("contains", "") in line for item in allowlist)


def iter_files(root: Path, tracked: bool) -> list[str]:
    if tracked and (root / ".git").exists():
        out = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True)
        return [p for p in out.stdout.decode("utf-8").split("\0") if p]
    files = []
    for path in root.rglob("*"):
        if path.is_file() and not SKIP_DIRS.intersection(path.relative_to(root).parts):
            files.append(path.relative_to(root).as_posix())
    return sorted(files)


def scan_text(rel: str, text: str, report: Report, allowlist: list[dict[str, str]], mentions: list[str]) -> None:
    for number, line in enumerate(text.splitlines(), start=1):
        if any(p.search(line) for p in CREDIT_PATTERNS):
            if allowed(rel, line, allowlist):
                continue
            report.error(f"{rel}:{number}: expressão de crédito a ferramenta de IA: {line.strip()[:160]}")
        elif MENTION_RE.search(line):
            mentions.append(f"{rel}:{number}: {line.strip()[:120]}")


def scan_tree(root: Path, report: Report, tracked: bool, allowlist: list[dict[str, str]]) -> list[str]:
    mentions: list[str] = []
    for rel in iter_files(root, tracked):
        if AGENT_PATH_RE.search(rel):
            report.error(f"{rel}: arquivo de instrução de agente não pode ser versionado nem publicado")
            continue
        if rel in SELF_FILES:
            continue
        path = root / rel
        if path.suffix.lower() not in TEXT_SUFFIXES or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        scan_text(rel, text, report, allowlist, mentions)
    return mentions


def scan_commits(root: Path, rev_range: str, report: Report) -> int:
    fmt = "%H%x1f%an%x1f%ae%x1f%cn%x1f%ce%x1f%B%x1e"
    out = subprocess.run(["git", "log", f"--format={fmt}", rev_range], cwd=root, capture_output=True, text=True)
    if out.returncode != 0:
        report.error(f"git log {rev_range}: {out.stderr.strip()}")
        return 0
    count = 0
    for record in filter(None, (r.strip("\n") for r in out.stdout.split("\x1e"))):
        sha, an, ae, cn, ce, body = record.split("\x1f", 5)
        count += 1
        for who in (f"{an} <{ae}>", f"{cn} <{ce}>"):
            if BOT_AUTHOR_RE.search(who):
                report.error(f"commit {sha[:10]}: autor ou committer não é uma pessoa: {who}")
        for line in body.splitlines():
            if any(p.search(line) for p in CREDIT_PATTERNS):
                report.error(f"commit {sha[:10]}: crédito a ferramenta de IA na mensagem: {line.strip()[:160]}")
    return count


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--path", type=Path, help="árvore a verificar (padrão: arquivos versionados do repositório)")
    parser.add_argument("--commits", help="intervalo de commits a verificar (ex.: main..HEAD, ou HEAD para todo o histórico)")
    parser.add_argument("--show-mentions", action="store_true", help="lista as menções simples para revisão manual")
    args = parser.parse_args(argv)

    report = Report("Atribuição de autoria")
    allowlist = load_allowlist()
    root = (args.path or ROOT).resolve()
    mentions = scan_tree(root, report, tracked=args.path is None, allowlist=allowlist)
    if args.commits:
        total = scan_commits(ROOT, args.commits, report)
        print(f"  {total} commits verificados ({args.commits})")
    print(f"  {len(mentions)} menções simples a nomes de ferramentas para revisão manual")
    if args.show_mentions:
        for item in mentions:
            print("    revisar:", item)
    return report.finish()


if __name__ == "__main__":
    sys.exit(main())
