"""Utilitários compartilhados pelos scripts de validação.

Sem dependências além de PyYAML e da biblioteca padrão.
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path
from typing import Any, Iterator

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONFIG = ROOT / "zensical.toml"
MANIFEST = ROOT / "curriculum" / "manifest.yml"

STATUSES = ("planned", "draft", "in-review", "published", "deprecated")
FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def read_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    """Retorna (front matter, corpo) de um arquivo Markdown."""
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text
    data = yaml.safe_load(match.group(1)) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: front matter não é um mapeamento YAML")
    return data, text[match.end():]


def load_config(path: Path = CONFIG) -> dict[str, Any]:
    with path.open("rb") as fh:
        return tomllib.load(fh)


def iter_nav_files(nav: Any) -> Iterator[str]:
    """Percorre recursivamente a `nav` do zensical.toml e devolve os caminhos .md."""
    if isinstance(nav, str):
        if not nav.startswith(("http://", "https://")):
            yield nav
    elif isinstance(nav, list):
        for item in nav:
            yield from iter_nav_files(item)
    elif isinstance(nav, dict):
        for value in nav.values():
            yield from iter_nav_files(value)


def nav_files(config: dict[str, Any] | None = None) -> set[str]:
    config = config if config is not None else load_config()
    return set(iter_nav_files(config.get("project", {}).get("nav", [])))


def load_manifest(path: Path = MANIFEST) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


class Report:
    """Acumula erros e avisos e define o código de saída."""

    def __init__(self, title: str) -> None:
        self.title = title
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def finish(self) -> int:
        for w in self.warnings:
            print(f"  aviso: {w}")
        for e in self.errors:
            print(f"  ERRO:  {e}")
        status = "FALHOU" if self.errors else "OK"
        print(f"[{status}] {self.title} — {len(self.errors)} erro(s), {len(self.warnings)} aviso(s)")
        return 1 if self.errors else 0


def exit_with(report: Report) -> None:
    sys.exit(report.finish())
