"""Testes do archcheck (Laboratório 02). Executados no CI junto com os testes do projeto."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

LAB = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(LAB))

import archcheck  # noqa: E402

AS_IS = LAB / "models" / "meridiana-as-is.yaml"
TO_BE = LAB / "solutions" / "meridiana-to-be.yaml"


def rules(path: Path, severity: str | None = None) -> set[str]:
    findings = archcheck.analyze(archcheck.load(path))
    return {f.rule for f in findings if severity is None or f.severity == severity}


def test_models_are_valid():
    assert archcheck.load(AS_IS).errors == []
    assert archcheck.load(TO_BE).errors == []


def test_as_is_reveals_case_a_findings():
    high = rules(AS_IS, "high")
    # acesso remoto só com senha, credencial compartilhada, banco acessado da DMZ,
    # rede plana, legado junto de ativos críticos e backup vulnerável
    assert {"AC-02", "AC-03", "SG-01", "SG-02", "LG-01", "RS-02", "RS-03", "DP-01"} <= high


def test_to_be_has_no_high_findings():
    assert rules(TO_BE, "high") == set()
    # o legado continua como achado médio: exceção consciente até a substituição
    assert "LG-01" in rules(TO_BE, "medium")


def test_invalid_model_is_rejected(tmp_path):
    bad = tmp_path / "bad.yaml"
    bad.write_text(
        "zones: [{id: z, trust: 9}]\n"
        "components: [{id: a, type: unknown, zone: missing}]\n"
        "flows: [{from: a, to: b, authn: maybe}]\n",
        encoding="utf-8",
    )
    errors = archcheck.load(bad).errors
    assert any("trust" in e for e in errors)
    assert any("tipo inválido" in e for e in errors)
    assert any("zona desconhecida" in e for e in errors)
    assert any("authn" in e for e in errors)
    assert archcheck.main([str(bad)]) == 2


def test_mermaid_has_zones_and_accessibility():
    model = archcheck.load(AS_IS)
    output = archcheck.to_mermaid(model, archcheck.analyze(model))
    assert output.startswith("flowchart LR")
    assert "accTitle:" in output and "accDescr:" in output
    for zone in model.zones:
        assert f"subgraph {zone.replace('-', '_')}" in output
    assert "class " in output and " finding" in output


@pytest.mark.parametrize("model,expected", [(AS_IS, 1), (TO_BE, 0)])
def test_fail_on_high_exit_code(model, expected, capsys):
    assert archcheck.main([str(model), "--fail-on", "high"]) == expected
