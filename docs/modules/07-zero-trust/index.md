---
id: M07
title: "Módulo 7 — Zero Trust Architecture"
description: Zero Trust como estratégia de arquitetura — princípios da NIST SP 800-207, componentes de decisão e aplicação de política, abordagens e modelos de implantação, verificação contínua e postura, proteção de workloads, CISA Zero Trust Maturity Model e implantação progressiva com sistemas legados.
stage: n2
status: published
prerequisites: [M05, M06]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
---

# Módulo 7 — Zero Trust Architecture { #modulo-07-zero-trust-architecture }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 2 — Arquiteturas de Infraestrutura</span>
<span class="saa-meta">7 aulas · cerca de 8 h de aulas</span>
<span class="saa-status saa-status--published">Published</span>
</div>

## Resumo

!!! abstract "Sobre este módulo"

    Os módulos de rede (Módulo 5) e de identidade (Módulo 6) construíram as peças; este módulo as integra na estratégia que dá nome à arquitetura moderna: **Zero Trust**. O foco é o que torna Zero Trust real — princípios precisos, componentes de decisão com disponibilidade e integridade, escolha do modelo de implantação por classe de recurso, verificação contínua com sinais confiáveis, proteção da comunicação entre serviços, avaliação de maturidade com evidências e uma migração em ondas que trata os legados com honestidade.

Ao concluir o módulo, você será capaz de:

- Explicar os sete princípios da SP 800-207 e o que Zero Trust não resolve.
- Mapear produtos reais aos papéis de PE, PA e PEP e especificar seus requisitos.
- Escolher abordagens e modelos de implantação por classe de recurso e de dispositivo.
- Desenhar acesso adaptativo com sinais atestados e respostas graduais.
- Proteger a comunicação entre workloads com identidade, mTLS e políticas.
- Avaliar maturidade com o ZTMM 2.0 e definir alvos ligados a riscos.
- Planejar a migração em ondas, com enclaves para legados e critérios de aceite.

## Aulas

<!-- lessons:start -->

| Aula | Tema | Profundidade | Duração |
|:---|:---|:---|:---|
| [Aula 01](01-zero-trust-fundamentals.md) | Fundamentos de Zero Trust e o NIST SP 800-207 | Fundamental | 75 min |
| [Aula 02](02-logical-components.md) | Componentes lógicos: Policy Engine, Policy Administrator e PEP | Professional | 60 min |
| [Aula 03](03-approaches-deployment.md) | Abordagens identity-centric, resource-centric e de rede | Professional | 60 min |
| [Aula 04](04-continuous-verification.md) | Verificação contínua, postura de dispositivo e acesso adaptativo | Professional | 75 min |
| [Aula 05](05-workload-protection.md) | Segmentação e proteção de workloads | Professional | 60 min |
| [Aula 06](06-cisa-ztmm.md) | CISA Zero Trust Maturity Model | Architect | 60 min |
| [Aula 07](07-progressive-deployment.md) | Implantação progressiva com sistemas legados e restrições | Architect | 90 min |

<!-- lessons:end -->

## Mapa do módulo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m07-module-map.mmd"
```

<figcaption>Figura 1 — Mapa do Módulo 7.</figcaption>
</figure>

## Pré-requisitos

| Pré-requisito | Por quê | Como validar |
|:---|:---|:---|
| [Módulo 5](../05-network-security/index.md) | Segmentação, acesso remoto e NAC são componentes da arquitetura | Exercícios das Aulas 01 e 04 do Módulo 5 |
| [Módulo 6](../06-iam/index.md) | Identidade, autorização e identidade de workload são o centro da decisão | Exercícios das Aulas 02 e 07 do Módulo 6 |
| [Módulo 3 — Aula 08](../03-governance-risk/08-metrics-maturity-reporting.md) | Diferença entre nota de maturidade e medida, usada na Aula 06 | Questões da aula |

## Atividades

- Exercício de decisão ao final de cada aula, com matriz de decisão ponderada, pesos justificados, risco residual e as condições que mudariam a escolha. A matriz organiza a comparação; a decisão continua dependendo do julgamento profissional e da análise de riscos — uma obrigação legal ou um limite de tolerância elimina uma opção antes de qualquer soma.
- A Aula 07 integra o módulo em um plano de migração em ondas para a Meridiana, com critérios de aceite.

## Organizações fictícias usadas no módulo

| Organização | Perfil |
|:---|:---|
| **Meridiana Distribuidora** | Plano de Zero Trust em ondas a partir do cenário de ransomware, com legados em enclave. |
| **Lumen Saúde** | Objetivos de Zero Trust para prontuários, médicos parceiros e modo de falha do PDP. |
| **Aurora Pagamentos** | Vários PDPs com políticas incoerentes, classes de aplicações e proteção de workloads do CDE. |

## Referências principais do módulo

- NIST. *SP 800-207 — Zero Trust Architecture*. 2020. <https://csrc.nist.gov/pubs/sp/800/207/final>.
- NIST. *SP 800-207A — Zero Trust for Cloud-Native Applications in Multi-Location Environments*. 2023. <https://csrc.nist.gov/pubs/sp/800/207/a/final>.
- NIST. *SP 1800-35 — Implementing a Zero Trust Architecture*. 2025. <https://pages.nist.gov/zero-trust-architecture/>.
- NIST. *SP 800-215 — Guide to a Secure Enterprise Network Landscape*. 2022. <https://csrc.nist.gov/pubs/sp/800/215/final>.
- CISA. *Zero Trust Maturity Model, Version 2.0*. 2023. <https://www.cisa.gov/zero-trust-maturity-model>.
