---
id: M08
title: "Módulo 8 — On-Premises e Sistemas Legados"
description: Segurança de ambientes on-premises e legados — datacenters, hardening e baselines, arquitetura de servidores Windows, Linux e Active Directory, backup e resiliência contra ransomware, sistemas sem suporte e controles compensatórios, protocolos inseguros e modernização gradual.
stage: n2
status: published
prerequisites: [M05, M06, M07]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
---

# Módulo 8 — On-Premises e Sistemas Legados { #modulo-08-on-premises-e-sistemas-legados }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 2 — Arquiteturas de Infraestrutura</span>
<span class="saa-meta">7 aulas · cerca de 8 h de aulas</span>
<span class="saa-status saa-status--published">Published</span>
</div>

## Resumo

!!! abstract "Sobre este módulo"

    A maior parte das organizações não começa do zero: tem datacenter, servidores configurados ao longo de anos, Active Directory com histórico, sistemas sem suporte e protocolos que ninguém ousa desligar. É nesse ambiente que o ransomware costuma ter sucesso. Este módulo trata o legado como realidade a ser governada — com hardening verificável, separação administrativa, backup que sobrevive a um administrador comprometido, exceções com prazo e uma modernização em que cada etapa deixa o ambiente mais seguro.

Ao concluir o módulo, você será capaz de:

- Organizar a segurança física e o gerenciamento fora de banda de datacenters.
- Definir baselines a partir de benchmarks e mantê-las por automação.
- Aplicar a separação por planos a servidores Windows, Linux e ao Active Directory.
- Projetar backup isolado, imutável e testado contra ransomware.
- Tratar sistemas sem suporte com decisões explícitas e compensatórios verificáveis.
- Remover protocolos inseguros pelo ciclo auditar, corrigir, desabilitar e monitorar.
- Modernizar legados com strangler fig, fachadas e marcos de segurança.

## Aulas

<!-- lessons:start -->

| Aula | Tema | Profundidade | Duração |
|:---|:---|:---|:---|
| [Aula 01](01-datacenter-security.md) | Segurança de datacenters | Fundamental | 60 min |
| [Aula 02](02-hardening-baselines.md) | Hardening e baselines de configuração | Professional | 75 min |
| [Aula 03](03-windows-linux-ad.md) | Arquitetura para Windows Server, Linux e Active Directory | Professional | 90 min |
| [Aula 04](04-backup-ransomware-resilience.md) | Backup, recuperação e resiliência contra ransomware | Professional | 75 min |
| [Aula 05](05-unsupported-systems.md) | Sistemas sem suporte e controles compensatórios | Architect | 60 min |
| [Aula 06](06-insecure-protocols.md) | Protocolos inseguros e dependências legadas | Professional | 60 min |
| [Aula 07](07-modernization.md) | Integração com ambientes modernos e modernização gradual | Architect | 75 min |

<!-- lessons:end -->

## Mapa do módulo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m08-module-map.mmd"
```

<figcaption>Figura 1 — Mapa do Módulo 8.</figcaption>
</figure>

## Pré-requisitos

| Pré-requisito | Por quê | Como validar |
|:---|:---|:---|
| [Módulo 5](../05-network-security/index.md) | Segmentação, zona de gestão e bastion são usados em todas as aulas | Exercícios das Aulas 01 e 04 do Módulo 5 |
| [Módulo 6](../06-iam/index.md) | Active Directory, contas privilegiadas e recuperação de identidade | Exercícios das Aulas 03, 06 e 09 do Módulo 6 |
| [Módulo 7](../07-zero-trust/index.md) | A implantação progressiva de Zero Trust sustenta a modernização gradual da Aula 07 | Exercício da Aula 07 do Módulo 7 |
| [Módulo 3 — Aula 05](../03-governance-risk/05-bia-rto-rpo.md) | Objetivos de recuperação orientam backup e datacenter | Questões da aula |
| [Módulo 3 — Aula 03](../03-governance-risk/03-control-selection-tailoring.md) | Controles compensatórios tratam o mesmo risco do controle original (Aula 05) | Questões da aula |

## Atividades

- Exercício de decisão ao final de cada aula, com matriz de decisão ponderada, pesos justificados, risco residual e as condições que mudariam a escolha. A matriz organiza a comparação; a decisão continua dependendo do julgamento profissional e da análise de riscos — uma obrigação legal ou um limite de tolerância elimina uma opção antes de qualquer soma.
- O [Caso A — Meridiana](../../case-studies/case-a-meridiana/index.md) aplica hardening, backup e tratamento de legados ao datacenter tradicional.

## Organizações fictícias usadas no módulo

| Organização | Perfil |
|:---|:---|
| **Meridiana Distribuidora** | Sala de servidores, baseline de 80 servidores Windows, backup integrado ao domínio, servidor de etiquetas sem suporte, ERP antigo. |
| **Lumen Saúde** | Racks nas clínicas, 140 servidores Linux com chave compartilhada, equipamento de imagem sem suporte. |
| **Aurora Pagamentos** | Baseline Linux, servidores Linux e identidade, desativação de TLS antigo com parceiros. |

## Referências principais do módulo

- NIST. *SP 800-128 — Security-Focused Configuration Management*. <https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-128.pdf>.
- NIST. *SP 800-70 Rev. 5 — National Checklist Program*. 2026. <https://csrc.nist.gov/pubs/sp/800/70/r5/final>.
- CIS. *CIS Benchmarks*. <https://www.cisecurity.org/cis-benchmarks>.
- CISA, FBI, NSA, MS-ISAC. *#StopRansomware Guide*. 2023. <https://www.cisa.gov/stopransomware/ransomware-guide>.
- NIST NCCoE. *SP 1800-11 — Data Integrity: Recovering from Ransomware*. <https://www.nccoe.nist.gov/projects/building-blocks/data-integrity/recover>.
- IETF. *RFC 8996 — Deprecating TLS 1.0 and TLS 1.1*. 2021.
- M. Fowler. *Strangler Fig*. 2024. <https://www.martinfowler.com/bliki/StranglerFigApplication.html>.
