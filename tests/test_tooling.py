"""Testes dos utilitários de navegação, contraste e estrutura."""

from __future__ import annotations

from check_contrast import PAIRS, parse_tokens, ratio, resolve
from _common import iter_nav_files, load_config, nav_files


def test_contrast_reference_values():
    assert round(ratio("#000000", "#ffffff"), 1) == 21.0
    assert round(ratio("#ffffff", "#ffffff"), 1) == 1.0


def test_all_design_tokens_meet_wcag_aa():
    tokens = parse_tokens()
    for _, label, fg, bg in PAIRS:
        assert ratio(resolve(fg, tokens), resolve(bg, tokens)) >= 4.5, label


def test_nav_iteration_handles_nested_sections():
    nav = [{"A": "a.md"}, {"B": ["b/index.md", {"C": "b/c.md"}, {"Ext": "https://example.com"}]}]
    assert list(iter_nav_files(nav)) == ["a.md", "b/index.md", "b/c.md"]


def test_repository_nav_contains_homepage_and_handbook():
    nav = nav_files(load_config())
    assert "index.md" in nav
    assert "internal/design-system.md" in nav


def test_every_module_page_in_nav_is_declared_in_manifest():
    """Páginas de módulo só entram em nav se o manifesto as declarar com status ativo."""
    import yaml

    from _common import ROOT

    manifest = yaml.safe_load((ROOT / "curriculum" / "manifest.yml").read_text(encoding="utf-8"))
    declared = set()
    for module in manifest["modules"]:
        if module.get("status") in {"in-review", "published"} and module.get("path"):
            base = module["path"].rsplit("/", 1)[0]
            declared.add(base)
    for path in nav_files(load_config()):
        if path.startswith("modules/"):
            assert path.rsplit("/", 1)[0] in declared, f"{path} está em nav sem módulo ativo no manifesto"


def test_smartsymbols_keeps_option_letters():
    """"(c)" identifica alternativas de questões e não pode virar "©"."""
    import tomllib

    from _common import ROOT

    config = tomllib.loads((ROOT / "zensical.toml").read_text(encoding="utf-8"))
    smartsymbols = config["project"]["markdown_extensions"]["pymdownx"]["smartsymbols"]
    assert smartsymbols.get("copyright") is False
