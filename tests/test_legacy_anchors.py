"""Âncoras publicadas nas versões 0.1.x continuam existindo depois da migração para releases por nível."""

from __future__ import annotations

import re

import render_curriculum as rc
from _common import DOCS, ROOT, load_manifest

MANIFEST = load_manifest()


def test_homepage_keeps_published_journey_anchors():
    block = rc.render_release_status(MANIFEST)
    for anchor in ("fundamentals", "professional", "architect"):
        assert f"{{ #{anchor} }}" in block, anchor
    assert set(rc.JOURNEY_ANCHORS) <= {r["id"] for r in MANIFEST["releases"]}


def test_roadmap_keeps_published_release_anchors():
    text = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    for anchor in ("release-1-fundamentals", "release-2-professional", "release-3-architect"):
        assert f'<a id="{anchor}"></a>' in text, anchor


def test_reference_pages_keep_anchors_of_renamed_sources():
    text = (DOCS / "resources" / "official-frameworks.md").read_text(encoding="utf-8")
    for anchors in rc.LEGACY_REF_ANCHORS.values():
        for anchor in anchors:
            assert f'<a id="{anchor}"></a>' in text, anchor
    assert len(re.findall(r'<a id="[^"]+"></a>\n\n### Resolução CD/ANPD nº 15', text)) == 1
