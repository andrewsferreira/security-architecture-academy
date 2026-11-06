---
id: M05
title: "Módulo 5 — Network Security Architecture"
description: Arquitetura de segurança de redes corporativas — zonas, segmentação e microsegmentação, perímetro e inspeção, tráfego north-south e east-west, acesso remoto com VPN, ZTNA e bastion, SD-WAN, SASE e SSE, Network Access Control e o desenho integrado de uma rede corporativa segura.
stage: n2
status: published
prerequisites: [M00, M02, M04]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
---

# Módulo 5 — Network Security Architecture { #modulo-05-network-security-architecture }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 2 — Arquiteturas de Infraestrutura</span>
<span class="saa-meta">7 aulas · cerca de 8 h de aulas</span>
<span class="saa-status saa-status--published">Published</span>
</div>

## Resumo

!!! abstract "Sobre este módulo"

    A rede deixou de ser o perímetro único da segurança, mas continua sendo a camada que define quem alcança o quê. Este módulo trata a rede como instrumento de **limitação do raio de impacto** e de **visibilidade**: zonas e fluxos explícitos, perímetro como uma camada entre várias, controle do tráfego interno, acesso remoto por aplicação, serviços de borda em nuvem e controle de quem entra na rede local. A última aula integra tudo em um caso híbrido com estado atual, estado-alvo e transição.

Ao concluir o módulo, você será capaz de:

- Definir zonas de confiança e matrizes de fluxos com negar por padrão, e decidir quando microsegmentar.
- Posicionar DMZ, NGFW, WAF/WAAP, IPS e proxies e definir política de saída.
- Controlar e monitorar tráfego east-west e restringir caminhos de movimento lateral.
- Escolher entre VPN, ZTNA e bastion e planejar a migração para acesso por aplicação.
- Avaliar SD-WAN, SASE e SSE, inclusive modo de falha e dependência de provedor.
- Desenhar NAC com 802.1X e tratar dispositivos sem suporte.
- Propor uma arquitetura de rede-alvo defensável, com transição priorizada e critérios de aceite.

## Aulas

<!-- lessons:start -->

| Aula | Tema | Profundidade | Duração |
|:---|:---|:---|:---|
| [Aula 01](01-zones-segmentation.md) | Zonas de confiança, segmentação e microsegmentação | Fundamental | 75 min |
| [Aula 02](02-perimeter-inspection.md) | Perímetro e inspeção: DMZ, WAF, NGFW, IDS/IPS e proxies | Professional | 75 min |
| [Aula 03](03-north-south-east-west.md) | Tráfego North-South e East-West | Professional | 60 min |
| [Aula 04](04-remote-access.md) | Acesso remoto: VPN, ZTNA e bastion hosts | Professional | 75 min |
| [Aula 05](05-sdwan-sase-sse.md) | SD-WAN, SASE e SSE | Professional | 60 min |
| [Aula 06](06-network-access-control.md) | Network Access Control | Professional | 45 min |
| [Aula 07](07-secure-enterprise-network.md) | Desenho de uma rede corporativa segura | Architect | 90 min |

<!-- lessons:end -->

## Mapa do módulo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m05-module-map.mmd"
```

<figcaption>Figura 1 — Mapa do Módulo 5.</figcaption>
</figure>

## Pré-requisitos

| Pré-requisito | Por quê | Como validar |
|:---|:---|:---|
| [Módulo Inicial](../00-foundations/index.md) | Redes TCP/IP, segmentação e conectividade | Seção A da [avaliação diagnóstica](../../assessments/diagnostic-fundamentals.md) |
| [Módulo 2](../02-security-architecture/index.md) | Princípios, padrões e decisões registradas | [Avaliação do Módulo 2](../../assessments/m02-security-architecture.md) |
| [Módulo 4](../04-threat-modeling/index.md) | Cenários ATT&CK e revisão As-Is/To-Be são usados nas Aulas 03, 04 e 07; a Aula 07 tem a Aula 07 do Módulo 4 como pré-requisito | Questões das Aulas 04 e 07 do Módulo 4 |

## Atividades

- Exercício de decisão ao final de cada aula, com matriz de decisão ponderada, pesos justificados, risco residual e as condições que mudariam a escolha. A matriz organiza a comparação; a decisão continua dependendo do julgamento profissional e da análise de riscos — uma obrigação legal ou um limite de tolerância elimina uma opção antes de qualquer soma.
- A Aula 07 é um estudo de caso integrado com As-Is, To-Be, transição e critérios de aceite.
- O [Caso A — Meridiana](../../case-studies/case-a-meridiana/index.md) aplica segmentação e acesso remoto a um datacenter tradicional.

## Organizações fictícias usadas no módulo

| Organização | Perfil |
|:---|:---|
| **Meridiana Distribuidora** | Rede plana, VPN só com senha, centros de distribuição com coletores (Caso A). |
| **Lumen Saúde** | Clínicas com equipamentos médicos sem 802.1X e portal em containers. |
| **Aurora Pagamentos** | Rede híbrida com sede, filiais, datacenter com CDE e nuvem (caso da Aula 07). |

## Referências principais do módulo

- NIST. *SP 800-215 — Guide to a Secure Enterprise Network Landscape*. 2022. <https://csrc.nist.gov/pubs/sp/800/215/final>.
- NIST. *SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy*. 2009. <https://csrc.nist.gov/pubs/sp/800/41/r1/final>.
- NIST. *SP 800-46 Rev. 2 — Guide to Enterprise Telework, Remote Access, and BYOD Security*. 2016. <https://csrc.nist.gov/pubs/sp/800/46/r2/final>.
- NIST. *SP 800-94 — Guide to Intrusion Detection and Prevention Systems*. 2007. <https://csrc.nist.gov/pubs/sp/800/94/final>.
- NSA. *Network Infrastructure Security Guidance* (PP-22-0266). 2022.
- IETF. *RFC 9190 — EAP-TLS 1.3*. 2022. <https://www.rfc-editor.org/rfc/rfc9190.html>.
- NIST. *SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations*, Release 5.2.0. <https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final> — catálogo usado nas seções de controles das aulas.
