#!/usr/bin/env python3
"""archcheck — análise de arquitetura como código (Laboratório 02).

Lê um modelo de arquitetura em YAML (zonas, componentes e fluxos), valida a
estrutura, gera um diagrama Mermaid com as fronteiras de confiança e aplica
regras de revisão arquitetural derivadas do Módulo 02.

Uso:
    python archcheck.py models/meridiana-as-is.yaml
    python archcheck.py MODELO.yaml --mermaid diagrama.mmd --report relatorio.md --fail-on high

Ferramenta educacional: as regras ilustram raciocínio de revisão e NÃO
substituem uma revisão arquitetural completa.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

SEVERITIES = ("high", "medium", "low")
AUTHN = {"none", "password", "shared", "mfa", "mtls", "token", "certificate"}
STRONG_AUTHN = {"mfa", "mtls", "token", "certificate"}
DATA_CLASSES = ("public", "internal", "confidential")
COMPONENT_TYPES = {
    "actor", "workstation", "admin-workstation", "server", "application", "database", "directory", "backup",
    "remote-access", "firewall", "gateway", "siem", "saas", "device", "identity-provider",
}
CROWN_JEWELS = {"database", "directory", "backup"}


@dataclass
class Finding:
    rule: str
    severity: str
    target: str
    message: str
    recommendation: str
    lesson: str


@dataclass
class Model:
    name: str
    zones: dict[str, dict[str, Any]]
    components: dict[str, dict[str, Any]]
    flows: list[dict[str, Any]]
    errors: list[str] = field(default_factory=list)


# ---------------------------------------------------------------- carga
def load(path: Path) -> Model:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    model = Model(
        name=str(data.get("name", path.stem)),
        zones={z["id"]: z for z in data.get("zones") or [] if "id" in z},
        components={c["id"]: c for c in data.get("components") or [] if "id" in c},
        flows=list(data.get("flows") or []),
    )
    validate(model, data)
    return model


def validate(model: Model, raw: dict[str, Any]) -> None:
    err = model.errors.append
    if not model.zones:
        err("o modelo precisa de ao menos uma zona")
    for zone in raw.get("zones") or []:
        if "id" not in zone or "trust" not in zone:
            err(f"zona sem id ou trust: {zone}")
        elif not isinstance(zone["trust"], int) or not 0 <= zone["trust"] <= 4:
            err(f"zona {zone['id']}: trust deve ser inteiro de 0 (nenhuma confiança) a 4")
    for comp in raw.get("components") or []:
        cid = comp.get("id", "?")
        if comp.get("zone") not in model.zones:
            err(f"componente {cid}: zona desconhecida {comp.get('zone')!r}")
        if comp.get("type") not in COMPONENT_TYPES:
            err(f"componente {cid}: tipo inválido {comp.get('type')!r}")
    for index, flow in enumerate(model.flows, start=1):
        where = f"fluxo #{index}"
        for end in ("from", "to"):
            if flow.get(end) not in model.components:
                err(f"{where}: componente desconhecido em '{end}': {flow.get(end)!r}")
        if flow.get("authn") not in AUTHN:
            err(f"{where}: authn deve ser um de {sorted(AUTHN)}")
        if flow.get("data", "internal") not in DATA_CLASSES:
            err(f"{where}: data deve ser um de {DATA_CLASSES}")
        if not isinstance(flow.get("encrypted", False), bool):
            err(f"{where}: encrypted deve ser true ou false")


# ---------------------------------------------------------------- regras
def zone_of(model: Model, cid: str) -> dict[str, Any]:
    return model.zones[model.components[cid]["zone"]]


def label(model: Model, cid: str) -> str:
    return model.components[cid].get("name", cid)


def analyze(model: Model) -> list[Finding]:
    findings: list[Finding] = []
    add = findings.append

    # Regras por fluxo
    for flow in model.flows:
        src, dst = flow["from"], flow["to"]
        z_src, z_dst = zone_of(model, src), zone_of(model, dst)
        crosses = z_src["id"] != z_dst["id"]
        upward = z_dst["trust"] > z_src["trust"]
        target = f"{label(model, src)} → {label(model, dst)}"
        authn = flow["authn"]
        data_class = flow.get("data", "internal")
        purpose = flow.get("purpose", "")

        if crosses and upward and authn == "none":
            add(Finding("AC-01", "high", target,
                        "Fluxo entra em zona de maior confiança sem autenticação.",
                        "Autenticar o fluxo na fronteira e no destino.", "M02-L03"))
        reaches_inside = z_dst["trust"] >= 2 or model.components[dst]["type"] == "remote-access"
        if crosses and z_src["trust"] == 0 and reaches_inside and authn in {"password", "shared"}:
            add(Finding("AC-02", "high", target,
                        "Acesso a partir da internet à rede interna protegido apenas por senha.",
                        "Exigir MFA e restringir o acesso a aplicações específicas.", "M02-L07"))
        if authn == "shared":
            add(Finding("AC-03", "high", target,
                        "Credencial compartilhada impede identificar quem executou cada ação.",
                        "Usar identidades individuais, com aprovação e registro.", "M02-L04"))
        if crosses and data_class == "confidential" and not flow.get("encrypted", False):
            add(Finding("DP-01", "high", target,
                        "Dados confidenciais cruzam uma fronteira de confiança sem criptografia.",
                        "Criptografar o fluxo em trânsito.", "M02-L03"))
        if (crosses and z_src["trust"] <= 1
                and model.components[dst]["type"] in {"database", "directory"}):
            add(Finding("SG-01", "high", target,
                        "Componente de zona de baixa confiança acessa diretamente um repositório crítico.",
                        "Intermediar o acesso por uma API ou serviço na zona de aplicações, com permissões mínimas.",
                        "M02-L05"))
        if purpose == "admin" and not z_src.get("management", False):
            add(Finding("AC-04", "medium", target,
                        "Acesso administrativo originado fora de uma zona de gestão.",
                        "Administrar apenas a partir de zona de gestão com estações dedicadas.", "M02-L03"))

    # Regras por zona
    for zone in model.zones.values():
        members = [c for c in model.components.values() if c["zone"] == zone["id"]]
        types = {c["type"] for c in members}
        if "workstation" in types and types & CROWN_JEWELS:
            jewels = ", ".join(sorted(types & CROWN_JEWELS))
            add(Finding("SG-02", "high", zone.get("name", zone["id"]),
                        f"Estações de usuários compartilham a zona com ativos críticos ({jewels}).",
                        "Separar usuários, dados, gestão e backup em zonas com política entre elas.", "M02-L04"))
        unsupported = [c for c in members if c.get("supported") is False]
        critical = [c for c in members if c.get("critical") and c.get("supported") is not False]
        for comp in unsupported:
            sev = "high" if critical else "medium"
            add(Finding("LG-01", sev, comp.get("name", comp["id"]),
                        "Componente sem suporte de segurança"
                        + (" na mesma zona de componentes críticos." if critical else "."),
                        "Isolar em zona própria, registrar exceção com prazo e planejar a substituição.",
                        "M02-L04"))

    # Regras por componente
    for comp in model.components.values():
        name = comp.get("name", comp["id"])
        if comp.get("critical") and comp.get("redundancy", 1) < 2:
            add(Finding("RS-01", "medium", name,
                        "Componente crítico sem redundância (ponto único de falha).",
                        "Prever redundância ou aceitar formalmente o risco com plano de recuperação.", "M02-L07"))
        if comp.get("critical") and comp.get("logging", "local") != "central":
            add(Finding("DT-01", "medium", name,
                        "Componente crítico sem envio de eventos ao monitoramento central.",
                        "Enviar eventos de segurança ao SIEM com retenção definida.", "M02-L07"))
        if comp["type"] == "backup":
            if comp.get("identity") == "corporate-domain":
                add(Finding("RS-02", "high", name,
                            "Backup administrado com credenciais do domínio corporativo.",
                            "Isolar a administração do backup do domínio e manter cópia imutável.", "M02-L07"))
            if not comp.get("immutable", False) and not comp.get("offsite", False):
                add(Finding("RS-03", "high", name,
                            "Backup sem imutabilidade nem cópia isolada fora do site.",
                            "Adicionar imutabilidade e cópia isolada, com testes de restauração.", "M02-L07"))

    order = {s: i for i, s in enumerate(SEVERITIES)}
    findings.sort(key=lambda f: (order[f.severity], f.rule, f.target))
    return findings


# ---------------------------------------------------------------- saídas
def to_mermaid(model: Model, findings: list[Finding]) -> str:
    flagged = {part for f in findings for part in f.target.split(" → ")}
    names = {c["id"]: c.get("name", c["id"]) for c in model.components.values()}
    lines = [
        "flowchart LR",
        f"  accTitle: {model.name}",
        "  accDescr: Diagrama gerado pelo archcheck a partir do modelo YAML. Cada subgraph é uma zona de "
        "confiança; as setas são fluxos rotulados com protocolo e autenticação; componentes com achados "
        "aparecem destacados.",
        "",
    ]
    for zone in sorted(model.zones.values(), key=lambda z: z["trust"]):
        lines.append(f'  subgraph {zone["id"].replace("-", "_")}["{zone.get("name", zone["id"])} · confiança {zone["trust"]}"]')
        for comp in (c for c in model.components.values() if c["zone"] == zone["id"]):
            nid = comp["id"].replace("-", "_")
            shape = ('(["', '"])') if comp["type"] == "actor" else ('["', '"]')
            lines.append(f'    {nid}{shape[0]}{names[comp["id"]]}{shape[1]}')
        lines.append("  end")
    lines.append("")
    for flow in model.flows:
        src, dst = flow["from"].replace("-", "_"), flow["to"].replace("-", "_")
        text = f'{flow.get("protocol", "?")} · {flow["authn"]}'
        lines.append(f'  {src} -- "{text}" --> {dst}')
    lines.append("")
    lines.append("  classDef zone fill:transparent,stroke:#64748b,stroke-width:1px,stroke-dasharray:4 3")
    lines.append("  classDef finding stroke:#dc2626,stroke-width:2px")
    lines.append("  class " + ",".join(z.replace("-", "_") for z in model.zones) + " zone")
    marked = [c["id"].replace("-", "_") for c in model.components.values() if c.get("name", c["id"]) in flagged]
    if marked:
        lines.append("  class " + ",".join(marked) + " finding")
    return "\n".join(lines) + "\n"


def to_report(model: Model, findings: list[Finding]) -> str:
    counts = {s: sum(1 for f in findings if f.severity == s) for s in SEVERITIES}
    out = [
        f"# Relatório archcheck — {model.name}",
        "",
        f"Zonas: {len(model.zones)} · Componentes: {len(model.components)} · Fluxos: {len(model.flows)}",
        "",
        f"**Achados:** {counts['high']} alto(s), {counts['medium']} médio(s), {counts['low']} baixo(s).",
        "",
    ]
    if findings:
        out += ["| Regra | Severidade | Alvo | Achado | Recomendação | Aula |",
                "|:---|:---|:---|:---|:---|:---|"]
        for f in findings:
            out.append(f"| {f.rule} | {f.severity} | {f.target} | {f.message} | {f.recommendation} | {f.lesson} |")
    else:
        out.append("Nenhum achado pelas regras do laboratório.")
    out += ["", "_Ferramenta educacional: as regras não substituem uma revisão arquitetural completa._", ""]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Análise de arquitetura como código (Laboratório 02)")
    parser.add_argument("model", type=Path, help="arquivo YAML do modelo")
    parser.add_argument("--mermaid", type=Path, help="grava o diagrama Mermaid neste arquivo")
    parser.add_argument("--report", type=Path, help="grava o relatório Markdown neste arquivo")
    parser.add_argument("--fail-on", choices=SEVERITIES, help="código de saída 1 se houver achado nesta severidade ou maior")
    args = parser.parse_args(argv)

    model = load(args.model)
    if model.errors:
        for error in model.errors:
            print(f"ERRO de modelo: {error}", file=sys.stderr)
        return 2

    findings = analyze(model)
    report = to_report(model, findings)
    print(report)
    if args.mermaid:
        args.mermaid.write_text(to_mermaid(model, findings), encoding="utf-8")
        print(f"Diagrama gravado em {args.mermaid}")
    if args.report:
        args.report.write_text(report, encoding="utf-8")
        print(f"Relatório gravado em {args.report}")
    if args.fail_on:
        limit = SEVERITIES.index(args.fail_on)
        if any(SEVERITIES.index(f.severity) <= limit for f in findings):
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
