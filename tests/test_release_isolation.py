"""Isolamento entre releases do Professional: o que cada release exporta não depende de releases futuras.

O Professional é escrito inteiro no desenvolvimento, mas publicado em partes: R3 (Módulos 5 a 8), R4 (9 a 11)
e R5 (12 a 15). Para cada release, simula o filtro de scripts/export_release.py (allowlist e escopo cumulativo)
sobre as páginas e verifica que nenhuma página exportada:

- tem link relativo para uma página que fica fora da árvore dessa release;
- inclui, por snippet, um diagrama que a exportação remove.

Blocos gerados dentro das páginas (por exemplo, "Próximos passos") também são regenerados e ficam de fora.
Menções em texto a módulos futuros ("aprofundado no Módulo 11") são permitidas: não quebram links. As páginas
geradas do manifesto (export_release.GENERATED) ficam de fora: a exportação as regenera a partir do manifesto
público, que já não contém o que está fora do escopo. A verificação completa continua sendo a da árvore
candidata (check_links.py no site compilado).
"""

from __future__ import annotations

import posixpath
import re
from pathlib import Path

import pytest

import export_release as ex
from _common import ROOT

# A simulação usa os arquivos rastreados pelo Git do repositório de desenvolvimento. Na árvore exportada
# (sem .git), a verificação equivalente é a de links do site compilado, feita pela própria exportação.
if not (ROOT / ".git").exists():
    pytest.skip("simulação de exportação: só no repositório de desenvolvimento", allow_module_level=True)

MANIFEST = ex.load_manifest(ROOT)
ALLOW = ex.load_allowlist(ROOT)
FILES = [f for f in ex.tracked_files(ROOT) if f.startswith(("docs/", "assets/diagrams/"))]
LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)\s]*)?\)")
SNIPPET_RE = re.compile(r'--8<-- "(assets/diagrams/[^"]+)"')
# Blocos gerados por render_curriculum.py (próximos passos, listas de aulas…), regenerados na exportação.
GENERATED_BLOCK_RE = re.compile(r"<!-- ([\w-]+):start -->.*?<!-- \1:end -->", re.S)


def exported(release_id: str) -> set[str]:
    scope = ex.cumulative_scope(MANIFEST, release_id)
    prefixes, out_modules = ex.excluded_paths(MANIFEST, scope)
    return {f for f in FILES if ex.is_public(f, ALLOW) and not ex.is_excluded(f, prefixes, out_modules)}


@pytest.mark.parametrize("release_id", ["R3", "R4", "R5"])
def test_exported_pages_do_not_link_to_later_releases(release_id):
    tree = exported(release_id)
    broken = []
    for page in sorted(f for f in tree if f.endswith(".md") and f not in ex.GENERATED):
        text = GENERATED_BLOCK_RE.sub("", (ROOT / page).read_text(encoding="utf-8"))
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://")):
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(page), target))
            if (ROOT / resolved).exists() and resolved not in tree:
                broken.append(f"{page} → {target}")
    assert not broken, f"{release_id}: links para conteúdo fora da release:\n" + "\n".join(broken[:20])


@pytest.mark.parametrize("release_id", ["R3", "R4", "R5"])
def test_exported_pages_include_only_exported_diagrams(release_id):
    tree = exported(release_id)
    missing = []
    for page in sorted(f for f in tree if f.endswith(".md")):
        for diagram in SNIPPET_RE.findall((ROOT / page).read_text(encoding="utf-8")):
            if diagram not in tree:
                missing.append(f"{page} → {diagram}")
    assert not missing, f"{release_id}: diagramas removidos pela exportação:\n" + "\n".join(missing[:20])


def test_release_scopes_follow_the_level_model():
    r3, r4, r5 = (ex.cumulative_scope(MANIFEST, r)["modules"] for r in ("R3", "R4", "R5"))
    assert {"M05", "M06", "M07", "M08"} <= r3 and not r3 & {"M09", "M10", "M11"}
    assert {"M09", "M10", "M11"} <= r4 and not r4 & {"M12", "M13", "M14", "M15"}
    assert {"M12", "M13", "M14", "M15"} <= r5 and not r5 & {"M16", "M17"}
    for path in (Path("docs/modules/05-network-security/index.md"),):
        assert str(path) in exported("R3")
