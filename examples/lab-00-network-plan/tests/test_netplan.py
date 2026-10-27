"""Testes do netplan (Laboratório 00). Executados no CI junto com os testes do projeto."""

from __future__ import annotations

import json
import sys
from pathlib import Path

LAB = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(LAB))

import netplan  # noqa: E402

AS_IS = LAB / "models" / "meridiana-as-is.json"
TO_BE = LAB / "solutions" / "meridiana-to-be.json"


def rules(path: Path, severity: str | None = None) -> set[str]:
    return {f.rule for f in netplan.analyze(netplan.load(path)) if severity is None or f.severity == severity}


def test_models_are_valid():
    assert netplan.load(AS_IS).errors == []
    assert netplan.load(TO_BE).errors == []


def test_as_is_reveals_expected_findings():
    high = rules(AS_IS, "high")
    # sobreposição datacenter × VPC, rede plana com gestão, RDP da internet, fluxos "any"
    assert {"AD-01", "AD-03", "SG-02", "FL-01", "FL-02", "FL-04"} <= high
    assert "FL-03" in rules(AS_IS, "low")
    assert "SG-01" in rules(AS_IS, "medium")


def test_as_is_counts_match_lab_page():
    """O enunciado (docs/labs/lab-00-network-plan.md) informa 8 altos, 2 médios e 1 baixo."""
    from collections import Counter
    findings = netplan.analyze(netplan.load(AS_IS))
    assert Counter(f.severity for f in findings) == Counter({"high": 8, "medium": 2, "low": 1})


def test_to_be_has_no_findings():
    assert rules(TO_BE) == set()


def test_cli_exit_codes(tmp_path):
    assert netplan.main([str(AS_IS), "--markdown", str(tmp_path / "r.md")]) == 1
    assert "Revisão do plano de rede" in (tmp_path / "r.md").read_text(encoding="utf-8")
    assert netplan.main([str(TO_BE)]) == 0


def test_structural_errors_are_reported(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({
        "allocations": {"dc": "10.0.0.1/16"},
        "zones": [{"name": "z", "trust": "weird", "environment": "dc", "cidr": "10.0.0.0/24"}],
        "flows": [{"from": "z", "to": "nada"}],
    }), encoding="utf-8")
    plan = netplan.load(bad)
    assert any("alocação dc" in e for e in plan.errors)
    assert any("trust deve ser" in e for e in plan.errors)
    assert any("não existe" in e for e in plan.errors)
    assert any("sem portas" in e for e in plan.errors)
    assert netplan.main([str(bad)]) == 2


def test_subnet_outside_environment_block():
    plan = netplan.load(TO_BE)
    plan.zones["dc-usuarios"]["network"] = netplan.ipaddress.ip_network("10.99.0.0/24")
    assert "AD-02" in {f.rule for f in netplan.analyze(plan)}
