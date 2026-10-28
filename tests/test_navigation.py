"""Navegação pública: sete grupos, níveis dentro de Fundamentals e Research Library separada da Prática."""

from __future__ import annotations

from typing import Any

import export_release as ex
from _common import ROOT, load_config, load_manifest

PUBLIC_GROUPS = ["Início", "Começar", "Fundamentals", "Prática", "Research Library", "Currículo e Roadmap", "Sobre"]
DEV_ONLY_GROUPS = {"Professional", "Handbook"}  # removidos da árvore pública pela exportação

MANIFEST = load_manifest()
NAV = load_config()["project"]["nav"]
PUBLIC_TREE = (ROOT / "RELEASE-MANIFEST.yml").is_file()


def label(entry: dict[str, Any]) -> str:
    return next(iter(entry))


def paths(node: Any) -> list[str]:
    if isinstance(node, str):
        return [] if node.startswith(("http://", "https://")) else [node]
    if isinstance(node, list):
        return [p for item in node for p in paths(item)]
    if isinstance(node, dict):
        return [p for value in node.values() for p in paths(value)]
    return []


def public_release() -> str:
    """Release cujo escopo a árvore pública contém (a última com publicação aprovada ou publicada)."""
    rid = "R1"
    for rel in MANIFEST["releases"]:
        if rel.get("status") in {"approved", "published"}:
            rid = rel["id"]
    return rid


def is_public_doc(path: str) -> bool:
    scope = ex.cumulative_scope(MANIFEST, public_release())
    prefixes, out_modules = ex.excluded_paths(MANIFEST, scope)
    rel = f"docs/{path}"
    return ex.is_public(rel, ex.load_allowlist(ROOT)) and not ex.is_excluded(rel, prefixes, out_modules) \
        and (ROOT / rel).is_file()


def prune(node: Any) -> Any:
    """Navegação como fica na árvore pública (mesma regra de export_release.transform_nav)."""
    if isinstance(node, str):
        return node if node.startswith(("http://", "https://")) or is_public_doc(node) else None
    if isinstance(node, list):
        kept = [x for x in (prune(item) for item in node) if x not in (None, [], {})]
        return kept
    if isinstance(node, dict):
        key, value = next(iter(node.items()))
        value = prune(value)
        return {key: value} if value not in (None, []) else None
    return node


def test_no_duplicate_paths():
    all_paths = paths(NAV)
    assert len(all_paths) == len(set(all_paths))


def test_public_navigation_has_exactly_seven_groups():
    public = prune(NAV)
    assert [label(e) for e in public] == PUBLIC_GROUPS
    if not PUBLIC_TREE:
        assert [label(e) for e in NAV if label(e) not in DEV_ONLY_GROUPS] == PUBLIC_GROUPS
        for entry in NAV:
            if label(entry) in DEV_ONLY_GROUPS:
                assert not any(is_public_doc(p) for p in paths(entry)), f"{label(entry)} contém página pública"


def test_research_library_is_its_own_group():
    groups = {label(e): e for e in NAV}
    assert "resources/index.md" in paths(groups["Research Library"])
    assert not any(p.startswith("resources/") for p in paths(groups["Prática"]))
    assert "Handbook" not in [label(e) for e in prune(NAV)]


def test_fundamentals_groups_modules_by_level():
    stages = {s["id"]: s["title"] for s in MANIFEST["stages"]}
    modules = [m for m in MANIFEST["modules"] if m.get("path") and m["status"] not in ("planned", "draft")]
    fundamentals = next(e for e in NAV if label(e) == "Fundamentals")["Fundamentals"]
    seen = []
    for level in fundamentals:
        title = label(level)
        assert title in stages.values(), title
        stage = next(k for k, v in stages.items() if v == title)
        for module_entry in level[title]:
            index = paths(module_entry)[0]
            mod = next(m for m in modules if m["path"] == index)
            assert mod["stage"] == stage, f"{mod['id']} fora do {title}"
            seen.append(mod["id"])
    order = [m["id"] for m in MANIFEST["modules"]]
    assert seen == sorted(seen, key=order.index)
    assert {"n0", "n1"} == {next(k for k, v in stages.items() if v == label(level)) for level in fundamentals}


def test_public_fundamentals_shows_only_released_modules():
    fundamentals = next(e for e in prune(NAV) if label(e) == "Fundamentals")
    indexes = [p for p in paths(fundamentals) if p.endswith("/index.md")]
    scope = ex.cumulative_scope(MANIFEST, public_release())["modules"]
    expected = [m["path"] for m in MANIFEST["modules"] if m["id"] in scope]
    assert indexes == expected
