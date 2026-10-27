#!/usr/bin/env python3
"""netplan — revisão de um plano de endereçamento e segmentação (Laboratório 00).

Ferramenta educacional da Security Architecture Academy. Lê um plano de rede em
JSON (ambientes, zonas, sub-redes e fluxos permitidos) e aponta problemas que
um arquiteto encontraria em uma revisão: sobreposição de endereços entre
ambientes, faixas fora do bloco reservado, zonas grandes demais, fluxos amplos
("any") e caminhos diretos de zonas não confiáveis para zonas restritas.

Uso:
    python netplan.py models/meridiana-as-is.json
    python netplan.py models/meridiana-as-is.json --markdown relatorio.md

Somente biblioteca padrão. Dados fictícios — não use com planos reais sem revisão.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import sys
from dataclasses import dataclass, field
from itertools import combinations
from pathlib import Path

TRUST_LEVELS = {"untrusted": 0, "dmz": 1, "internal": 2, "restricted": 3, "management": 3}
SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2}


@dataclass
class Finding:
    rule: str
    severity: str
    message: str


@dataclass
class Plan:
    name: str
    allocations: dict[str, ipaddress.IPv4Network]
    zones: dict[str, dict]
    flows: list[dict]
    errors: list[str] = field(default_factory=list)


def load(path: str | Path) -> Plan:
    """Carrega e valida a estrutura do plano. Erros de estrutura vão para Plan.errors."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    errors: list[str] = []
    allocations: dict[str, ipaddress.IPv4Network] = {}
    for env, cidr in data.get("allocations", {}).items():
        try:
            allocations[env] = ipaddress.ip_network(cidr, strict=True)
        except ValueError as exc:
            errors.append(f"alocação {env}: {exc}")
    zones: dict[str, dict] = {}
    for zone in data.get("zones", []):
        name = zone.get("name")
        if not name:
            errors.append("zona sem nome")
            continue
        if zone.get("trust") not in TRUST_LEVELS:
            errors.append(f"zona {name}: trust deve ser um de {sorted(TRUST_LEVELS)}")
        if zone.get("environment") not in allocations and zone.get("trust") != "untrusted":
            errors.append(f"zona {name}: ambiente '{zone.get('environment')}' sem alocação")
        if zone.get("cidr"):
            try:
                zone["network"] = ipaddress.ip_network(zone["cidr"], strict=True)
            except ValueError as exc:
                errors.append(f"zona {name}: {exc}")
        elif zone.get("trust") != "untrusted":
            errors.append(f"zona {name}: sem cidr")
        zones[name] = zone
    flows = data.get("flows", [])
    for i, flow in enumerate(flows, start=1):
        for end in ("from", "to"):
            if flow.get(end) not in zones:
                errors.append(f"fluxo {i}: zona '{flow.get(end)}' não existe")
        if not flow.get("ports"):
            errors.append(f"fluxo {i}: sem portas (use \"any\" explicitamente, se for o caso)")
    return Plan(data.get("name", Path(path).stem), allocations, zones, flows, errors)


def analyze(plan: Plan) -> list[Finding]:
    """Aplica as regras de revisão e devolve os achados ordenados por severidade."""
    findings: list[Finding] = []
    nets = {n: z["network"] for n, z in plan.zones.items() if "network" in z}

    # AD-01: alocações de ambientes não podem se sobrepor (datacenter × nuvem × filiais)
    for (a, na), (b, nb) in combinations(plan.allocations.items(), 2):
        if na.overlaps(nb):
            findings.append(Finding("AD-01", "high",
                f"blocos dos ambientes '{a}' ({na}) e '{b}' ({nb}) se sobrepõem — "
                "a interconexão exigiria NAT e tornaria endereços ambíguos"))

    # AD-02: zonas precisam estar dentro do bloco do seu ambiente
    for name, z in plan.zones.items():
        env = plan.allocations.get(z.get("environment"))
        if env and "network" in z and not z["network"].subnet_of(env):
            findings.append(Finding("AD-02", "medium",
                f"zona '{name}' ({z['network']}) está fora do bloco do ambiente '{z['environment']}' ({env})"))

    # AD-03: zonas não podem se sobrepor entre si
    for (a, na), (b, nb) in combinations(nets.items(), 2):
        if na.overlaps(nb):
            findings.append(Finding("AD-03", "high", f"zonas '{a}' ({na}) e '{b}' ({nb}) se sobrepõem"))

    # AD-04: endereços internos devem ser privados (RFC 1918)
    for name, n in nets.items():
        if plan.zones[name].get("trust") != "untrusted" and not n.is_private:
            findings.append(Finding("AD-04", "medium", f"zona '{name}' usa faixa não privada ({n})"))

    # SG-01: zona muito grande para o que hospeda (rede plana)
    for name, z in plan.zones.items():
        if "network" in z and z.get("hosts"):
            capacity = z["network"].num_addresses - 2
            if capacity > 8 * z["hosts"] and z["network"].prefixlen < 22:
                findings.append(Finding("SG-01", "medium",
                    f"zona '{name}' ({z['network']}, {capacity} endereços) para {z['hosts']} hosts — "
                    "zona ampla sugere rede plana; segmente por função"))

    # SG-02: mistura de funções em uma mesma zona
    for name, z in plan.zones.items():
        roles = set(z.get("roles", []))
        if len(roles) > 1 and ({"users", "servers"} <= roles or "management" in roles):
            findings.append(Finding("SG-02", "high",
                f"zona '{name}' mistura funções {sorted(roles)} — usuários, servidores e gestão "
                "precisam de zonas separadas"))

    for i, f in enumerate(plan.flows, start=1):
        src, dst = plan.zones.get(f.get("from"), {}), plan.zones.get(f.get("to"), {})
        label = f"fluxo {i} ({f.get('from')} → {f.get('to')})"
        ports = f.get("ports")
        # FL-01: fluxo com portas "any"
        if ports == "any" or ports == ["any"]:
            sensitive = dst.get("trust") in ("restricted", "management") or "management" in dst.get("roles", [])
            findings.append(Finding("FL-01", "high" if sensitive else "medium",
                f"{label} permite qualquer porta — documente só os serviços necessários"))
        # FL-02: zona não confiável direto para zona restrita ou de gestão
        if src.get("trust") == "untrusted" and dst.get("trust") in ("restricted", "management", "internal"):
            findings.append(Finding("FL-02", "high",
                f"{label}: origem não confiável alcança zona '{dst.get('trust')}' diretamente — "
                "passe por uma zona intermediária (DMZ, proxy, bastion)"))
        # FL-03: fluxo sem justificativa
        if not f.get("purpose"):
            findings.append(Finding("FL-03", "low", f"{label} sem finalidade documentada"))
        # FL-04: administração fora da zona de gestão
        if any(str(p) in {"22", "3389", "5985", "5986"} for p in (ports if isinstance(ports, list) else [])) \
                and src.get("trust") != "management":
            findings.append(Finding("FL-04", "high",
                f"{label}: portas administrativas a partir de zona que não é de gestão — "
                "administração deve partir de bastion ou estação dedicada"))

    return sorted(findings, key=lambda x: (SEVERITY_ORDER[x.severity], x.rule, x.message))


def to_markdown(plan: Plan, findings: list[Finding]) -> str:
    lines = [f"# Revisão do plano de rede — {plan.name}", "",
             "| Regra | Severidade | Achado |", "|:---|:---|:---|"]
    lines += [f"| {f.rule} | {f.severity} | {f.message} |" for f in findings]
    if not findings:
        lines.append("| — | — | Nenhum achado |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("plan", help="arquivo JSON do plano de rede")
    parser.add_argument("--markdown", help="grava o relatório em Markdown")
    args = parser.parse_args(argv)
    plan = load(args.plan)
    if plan.errors:
        for e in plan.errors:
            print("ERRO:", e, file=sys.stderr)
        return 2
    findings = analyze(plan)
    for f in findings:
        print(f"[{f.severity.upper():6}] {f.rule}  {f.message}")
    counts = {s: sum(f.severity == s for f in findings) for s in SEVERITY_ORDER}
    print(f"\n{len(findings)} achado(s): {counts['high']} alto(s), {counts['medium']} médio(s), {counts['low']} baixo(s)")
    if args.markdown:
        Path(args.markdown).write_text(to_markdown(plan, findings), encoding="utf-8")
    return 1 if counts["high"] else 0


if __name__ == "__main__":
    sys.exit(main())
