---
title: Curriculum Roadmap
description: Estrutura curricular completa da Security Architecture Academy — 18 módulos em seis níveis, aulas, atividades e status editorial gerados a partir do manifesto.
---

# Curriculum Roadmap

A formação está organizada em **seis níveis progressivos** (Nível 0 a Nível 5), com **18 módulos** (Módulo Inicial ao Módulo 17) e uma seção complementar sobre segurança de IA. Esta página mostra cada módulo, suas aulas e o status editorial real de cada entrega.

!!! note "Como ler esta página"

    - Tudo abaixo é gerado de [`curriculum/manifest.yml`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/curriculum/manifest.yml) e verificado no CI.
    - **Fase** indica a ordem histórica de produção. A publicação segue releases cumulativas por nível — Fundamentals, com os Níveis 0 e 1 (Módulo Inicial ao Módulo 4, nas Releases 1 e 2), e uma release para cada um dos Níveis 2 a 5 (Módulos 5 a 17 e C01) —, descritas no [roadmap](../about/roadmap.md).
    - **Profundidade** indica o nível de exigência de cada aula: *Fundamental* (compreender), *Professional* (aplicar) e *Architect* (decidir e justificar).
    - Títulos de aulas com status **Planned** são provisórios até a produção do módulo.

## Status editoriais

| Status | Significado |
|:---|:---|
| <span class="saa-status saa-status--planned">Planned</span> | Definido no currículo, sem conteúdo produzido. |
| <span class="saa-status saa-status--draft">Draft</span> | Em escrita, fora da navegação. |
| <span class="saa-status saa-status--in-review">In Review</span> | Conteúdo completo, aguardando revisão técnica. |
| <span class="saa-status saa-status--published">Published</span> | Revisado e publicado no site público. |
| <span class="saa-status saa-status--deprecated">Deprecated</span> | Mantido por referência, com indicação do substituto. |

Só conteúdo *Published* aparece no portal; a publicação acontece por release, depois da revisão do mantenedor.

## Módulos e aulas

<!-- curriculum:start -->

**18 módulos · 135 aulas · cerca de 162 horas de aulas** (sem laboratórios, estudos de caso e avaliações). Status das aulas: Planned **98** · Published **37**.

### Nível 0 — Fundamentos de Tecnologia e Segurança

Infraestrutura, redes, cloud e fundamentos de segurança como linguagem comum.

| Módulo | Título | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| Módulo Inicial<br><small>`M00`</small> | [Fundamentos de Infraestrutura e Computação](../modules/00-foundations/index.md) | 7 | 7 h 45 min | 3 | <span class="saa-status saa-status--published">Published</span> |
| Módulo 1<br><small>`M01`</small> | [Fundamentos de Segurança](../modules/01-security-fundamentals/index.md) | 7 | 7 h 45 min | 3 | <span class="saa-status saa-status--published">Published</span> |

??? abstract "Módulo Inicial — Fundamentos de Infraestrutura e Computação"

    **ID técnico:** `M00` · **Domínios:** Infrastructure Foundations · **Pré-requisitos:** nenhum

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M00-L01`</small> | [Computação, sistemas operacionais e virtualização](../modules/00-foundations/01-computing-os-virtualization.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 02<br><small>`M00-L02`</small> | [Redes TCP/IP: modelo OSI, endereçamento, DNS, DHCP e NAT](../modules/00-foundations/02-tcp-ip-networking.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 03<br><small>`M00-L03`</small> | [Segmentação e conectividade: VLAN, roteamento, VPN, TLS e firewalls](../modules/00-foundations/03-segmentation-connectivity.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 04<br><small>`M00-L04`</small> | [Datacenters, armazenamento, clusters e alta disponibilidade](../modules/00-foundations/04-datacenter-high-availability.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 05<br><small>`M00-L05`</small> | [Containers, Kubernetes, APIs, microsserviços e serverless](../modules/00-foundations/05-containers-apis-serverless.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 06<br><small>`M00-L06`</small> | [Cloud computing: modelos de serviço e de implantação](../modules/00-foundations/06-cloud-computing-models.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 07<br><small>`M00-L07`</small> | [Lendo diagramas arquiteturais: componentes, fluxos e fronteiras](../modules/00-foundations/07-reading-architecture-diagrams.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |

??? abstract "Módulo 1 — Fundamentos de Segurança"

    **ID técnico:** `M01` · **Domínios:** Security Foundations · **Pré-requisitos:** Módulo Inicial

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M01-L01`</small> | [Propriedades de segurança: CIA, autenticidade, autorização e não repúdio](../modules/01-security-fundamentals/01-security-properties.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 02<br><small>`M01-L02`</small> | [Princípios de design seguro](../modules/01-security-fundamentals/02-secure-design-principles.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 03<br><small>`M01-L03`</small> | [Trust boundaries, attack surface e responsabilidade compartilhada](../modules/01-security-fundamentals/03-trust-boundaries-attack-surface.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 04<br><small>`M01-L04`</small> | [Criptografia aplicada: simétrica, assimétrica, hashing e assinaturas](../modules/01-security-fundamentals/04-applied-cryptography.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 05<br><small>`M01-L05`</small> | [PKI, certificados, TLS e gerenciamento de chaves](../modules/01-security-fundamentals/05-pki-tls-key-management.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 06<br><small>`M01-L06`</small> | [Ameaça, vulnerabilidade, risco, exposição e controle](../modules/01-security-fundamentals/06-threat-vulnerability-risk.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 07<br><small>`M01-L07`</small> | [Modelos formais: Bell-LaPadula, Biba, Clark-Wilson e Brewer-Nash](../modules/01-security-fundamentals/07-formal-security-models.md) | Professional | 60 min | <span class="saa-status saa-status--published">Published</span> |

### Nível 1 — Fundamentos de Arquitetura

O ofício do arquiteto, governança e riscos, e métodos de design e threat modeling.

| Módulo | Título | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| Módulo 2<br><small>`M02`</small> | [Introdução à Arquitetura de Segurança](../modules/02-security-architecture/index.md) | 8 | 9 h 45 min | 1 | <span class="saa-status saa-status--published">Published</span> |
| Módulo 3<br><small>`M03`</small> | [Governança, Riscos e Controles](../modules/03-governance-risk/index.md) | 8 | 10 h | 2 | <span class="saa-status saa-status--published">Published</span> |
| Módulo 4<br><small>`M04`</small> | [Métodos de Design e Threat Modeling](../modules/04-threat-modeling/index.md) | 7 | 8 h | 3 | <span class="saa-status saa-status--published">Published</span> |

??? abstract "Módulo 2 — Introdução à Arquitetura de Segurança"

    **ID técnico:** `M02` · **Domínios:** Enterprise Security Architecture, Security Foundations · **Pré-requisitos:** Módulo Inicial, Módulo 1

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M02-L01`</small> | [O papel do Security Architect](../modules/02-security-architecture/01-security-architect-role.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 02<br><small>`M02-L02`</small> | [Enterprise, Solution e Security Architecture](../modules/02-security-architecture/02-enterprise-solution-security-architecture.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 03<br><small>`M02-L03`</small> | [Arquitetura conceitual, lógica e física](../modules/02-security-architecture/03-conceptual-logical-physical.md) | Professional | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 04<br><small>`M02-L04`</small> | [Princípios, padrões, baselines e exceções](../modules/02-security-architecture/04-principles-standards-baselines-exceptions.md) | Professional | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 05<br><small>`M02-L05`</small> | [Arquiteturas de referência e blueprints](../modules/02-security-architecture/05-reference-architectures-blueprints.md) | Professional | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 06<br><small>`M02-L06`</small> | [Frameworks, padrões e certificações: NIST, SABSA, TOGAF, CISSP e ISSAP](../modules/02-security-architecture/06-frameworks.md) | Professional | 90 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 07<br><small>`M02-L07`</small> | [Business-driven Security Architecture: de requisitos de negócio a requisitos de segurança](../modules/02-security-architecture/07-business-driven-requirements.md) | Architect | 90 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 08<br><small>`M02-L08`</small> | [Architecture Decision Records](../modules/02-security-architecture/08-architecture-decision-records.md) | Architect | 75 min | <span class="saa-status saa-status--published">Published</span> |

??? abstract "Módulo 3 — Governança, Riscos e Controles"

    **ID técnico:** `M03` · **Domínios:** Governance, Risk & Compliance · **Pré-requisitos:** Módulo 2

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M03-L01`</small> | [Governança de segurança e o NIST CSF 2.0](../modules/03-governance-risk/01-governance-csf.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 02<br><small>`M03-L02`</small> | [NIST Risk Management Framework (SP 800-37)](../modules/03-governance-risk/02-nist-rmf.md) | Professional | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 03<br><small>`M03-L03`</small> | [Seleção e tailoring de controles: SP 800-53 e CIS Controls](../modules/03-governance-risk/03-control-selection-tailoring.md) | Professional | 90 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 04<br><small>`M03-L04`</small> | [ISO/IEC 27001/27002, LGPD e PCI DSS: propósito e escopo](../modules/03-governance-risk/04-iso-lgpd-pci.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 05<br><small>`M03-L05`</small> | [Business Impact Analysis, RTO e RPO](../modules/03-governance-risk/05-bia-rto-rpo.md) | Professional | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 06<br><small>`M03-L06`</small> | [Risk assessment, risk register e tratamento de riscos](../modules/03-governance-risk/06-risk-assessment-register.md) | Professional | 90 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 07<br><small>`M03-L07`</small> | [Catálogo de controles e arquitetura baseada em risco](../modules/03-governance-risk/07-control-catalog-risk-architecture.md) | Architect | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 08<br><small>`M03-L08`</small> | [Indicadores, maturidade e reporte à governança](../modules/03-governance-risk/08-metrics-maturity-reporting.md) | Architect | 60 min | <span class="saa-status saa-status--published">Published</span> |

??? abstract "Módulo 4 — Métodos de Design e Threat Modeling"

    **ID técnico:** `M04` · **Domínios:** Application Security, Enterprise Security Architecture · **Pré-requisitos:** Módulo 2

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M04-L01`</small> | [Data Flow Diagrams e fluxos de confiança](../modules/04-threat-modeling/01-data-flow-diagrams.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 02<br><small>`M04-L02`</small> | [STRIDE aplicado à arquitetura](../modules/04-threat-modeling/02-stride.md) | Professional | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 03<br><small>`M04-L03`</small> | [Attack trees e abuse cases](../modules/04-threat-modeling/03-attack-trees-abuse-cases.md) | Professional | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 04<br><small>`M04-L04`</small> | [MITRE ATT&CK para cenários de ataque](../modules/04-threat-modeling/04-mitre-attack-scenarios.md) | Professional | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 05<br><small>`M04-L05`</small> | [Pontos únicos de falha e análise de dependências](../modules/04-threat-modeling/05-single-points-of-failure.md) | Professional | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 06<br><small>`M04-L06`</small> | [De ameaças a requisitos de segurança](../modules/04-threat-modeling/06-threats-to-requirements.md) | Architect | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | Aula 07<br><small>`M04-L07`</small> | [Revisão arquitetural, As-Is/To-Be e validação de controles](../modules/04-threat-modeling/07-architecture-review-validation.md) | Architect | 75 min | <span class="saa-status saa-status--published">Published</span> |

### Nível 2 — Arquiteturas de Infraestrutura

Rede, identidade, Zero Trust e ambientes on-premises e legados.

| Módulo | Título | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| Módulo 5<br><small>`M05`</small> | Network Security Architecture | 7 | 8 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| Módulo 6<br><small>`M06`</small> | Identity & Access Management | 9 | 11 h 15 min | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| Módulo 7<br><small>`M07`</small> | Zero Trust Architecture | 7 | 8 h | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| Módulo 8<br><small>`M08`</small> | On-Premises e Sistemas Legados | 7 | 8 h 15 min | 3 | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 5 — Network Security Architecture"

    **ID técnico:** `M05` · **Domínios:** Network Security · **Pré-requisitos:** Módulo Inicial, Módulo 2

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M05-L01`</small> | Zonas de confiança, segmentação e microsegmentação | Fundamental | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M05-L02`</small> | Perímetro e inspeção: DMZ, WAF, NGFW, IDS/IPS e proxies | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M05-L03`</small> | Tráfego North-South e East-West | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M05-L04`</small> | Acesso remoto: VPN, ZTNA e bastion hosts | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M05-L05`</small> | SD-WAN, SASE e SSE | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M05-L06`</small> | Network Access Control | Professional | 45 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M05-L07`</small> | Desenho de uma rede corporativa segura | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 6 — Identity & Access Management"

    **ID técnico:** `M06` · **Domínios:** Identity & Access Management · **Pré-requisitos:** Módulo 1, Módulo 2

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M06-L01`</small> | Disciplinas de identidade: IAM, IGA, PAM e PIM | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M06-L02`</small> | Modelos de autorização: RBAC, ABAC e acesso contextual | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M06-L03`</small> | Diretórios e autenticação corporativa: Active Directory, LDAP e Kerberos | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M06-L04`</small> | Federação: SAML 2.0, OAuth 2.0 e OpenID Connect | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M06-L05`</small> | Identidade híbrida: Active Directory, Microsoft Entra ID e provedores cloud | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M06-L06`</small> | Contas privilegiadas e identidades de máquina | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M06-L07`</small> | Workload Identity Federation | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 08<br><small>`M06-L08`</small> | Ciclo de vida de identidades e segregação de funções | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 09<br><small>`M06-L09`</small> | Recuperação de identidade em incidentes | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 7 — Zero Trust Architecture"

    **ID técnico:** `M07` · **Domínios:** Zero Trust Architecture, Identity & Access Management, Network Security · **Pré-requisitos:** Módulo 5, Módulo 6

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M07-L01`</small> | Fundamentos de Zero Trust e o NIST SP 800-207 | Fundamental | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M07-L02`</small> | Componentes lógicos: Policy Engine, Policy Administrator e PEP | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M07-L03`</small> | Abordagens identity-centric, resource-centric e de rede | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M07-L04`</small> | Verificação contínua, postura de dispositivo e acesso adaptativo | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M07-L05`</small> | Segmentação e proteção de workloads | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M07-L06`</small> | CISA Zero Trust Maturity Model | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M07-L07`</small> | Implantação progressiva com sistemas legados e restrições | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 8 — On-Premises e Sistemas Legados"

    **ID técnico:** `M08` · **Domínios:** Infrastructure Foundations, Security Operations & Resilience · **Pré-requisitos:** Módulo 5, Módulo 6

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M08-L01`</small> | Segurança de datacenters | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M08-L02`</small> | Hardening e baselines de configuração | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M08-L03`</small> | Arquitetura para Windows Server, Linux e Active Directory | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M08-L04`</small> | Backup, recuperação e resiliência contra ransomware | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M08-L05`</small> | Sistemas sem suporte e controles compensatórios | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M08-L06`</small> | Protocolos inseguros e dependências legadas | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M08-L07`</small> | Integração com ambientes modernos e modernização gradual | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |

### Nível 3 — Arquitetura Cloud e Híbrida

AWS, Azure, Google Cloud e a integração segura entre ambientes.

| Módulo | Título | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| Módulo 9<br><small>`M09`</small> | AWS Security Architecture | 7 | 9 h 15 min | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| Módulo 10<br><small>`M10`</small> | Azure e Google Cloud | 7 | 7 h 45 min | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| Módulo 11<br><small>`M11`</small> | Hybrid & Multicloud Security Architecture | 11 | 14 h 30 min | 2 | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 9 — AWS Security Architecture"

    **ID técnico:** `M09` · **Domínios:** Cloud Security · **Pré-requisitos:** Módulo 5, Módulo 6

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M09-L01`</small> | Security Pillar do Well-Architected e responsabilidade compartilhada | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M09-L02`</small> | AWS Organizations, multi-account, landing zones e Control Tower | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M09-L03`</small> | IAM e IAM Identity Center | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M09-L04`</small> | Rede: VPC, Security Groups, NACLs, roteamento e endpoints | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M09-L05`</small> | Dados e segredos: AWS KMS e Secrets Manager | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M09-L06`</small> | Detecção e governança: CloudTrail, Config, GuardDuty, Security Hub, Inspector e Macie | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M09-L07`</small> | AWS Security Reference Architecture e integração com on-premises | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 10 — Azure e Google Cloud"

    **ID técnico:** `M10` · **Domínios:** Cloud Security, Identity & Access Management · **Pré-requisitos:** Módulo 5, Módulo 6

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M10-L01`</small> | Azure Well-Architected, Cloud Adoption Framework e Azure Landing Zones | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M10-L02`</small> | Microsoft Entra ID e identidade híbrida | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M10-L03`</small> | Defender for Cloud, Azure Policy e Azure Arc | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M10-L04`</small> | Google Cloud: Architecture Framework e hierarquia de recursos | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M10-L05`</small> | Google Cloud IAM, Organization Policy e Security Command Center | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M10-L06`</small> | Equivalências e particularidades entre AWS, Azure e Google Cloud | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M10-L07`</small> | Mapeamento para o Microsoft SC-100 | Architect | 45 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 11 — Hybrid & Multicloud Security Architecture"

    **ID técnico:** `M11` · **Domínios:** Hybrid & Multicloud Security, Cloud Security, Network Security, Identity & Access Management · **Pré-requisitos:** Módulo 6, Módulo 7

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M11-L01`</small> | Conectividade híbrida: VPN site-to-site, AWS Direct Connect e Azure ExpressRoute | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M11-L02`</small> | Arquitetura de DNS híbrido | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M11-L03`</small> | Identidade e federação entre Active Directory e provedores cloud | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M11-L04`</small> | Logs, observabilidade, SIEM e SOC multiambiente | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M11-L05`</small> | Segredos, certificados, criptografia e chaves distribuídos | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M11-L06`</small> | Políticas consistentes e postura: CSPM, CNAPP, CWPP, CIEM e DSPM | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M11-L07`</small> | Asset discovery e inventário corporativo | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 08<br><small>`M11-L08`</small> | Backup, disaster recovery e continuidade em ambientes híbridos | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 09<br><small>`M11-L09`</small> | Comunicação segura entre workloads | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 10<br><small>`M11-L10`</small> | Responsabilidade compartilhada, soberania, latência e vendor lock-in | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 11<br><small>`M11-L11`</small> | Três modelos de referência híbridos: As-Is e To-Be | Architect | 120 min | <span class="saa-status saa-status--planned">Planned</span> |

### Nível 4 — Arquitetura de Segurança Aplicada

Aplicações, dados, gestão de vulnerabilidades e exposição, operações e resiliência.

| Módulo | Título | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| Módulo 12<br><small>`M12`</small> | Application Security Architecture | 8 | 9 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| Módulo 13<br><small>`M13`</small> | Data Security Architecture | 7 | 8 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| Módulo 14<br><small>`M14`</small> | Vulnerability & Exposure Management Architecture | 8 | 9 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| Módulo 15<br><small>`M15`</small> | Security Operations & Resilience Architecture | 7 | 8 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 12 — Application Security Architecture"

    **ID técnico:** `M12` · **Domínios:** Application Security · **Pré-requisitos:** Módulo 4, Módulo 6

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M12-L01`</small> | Secure SDLC e DevSecOps | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M12-L02`</small> | OWASP ASVS como especificação de requisitos | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M12-L03`</small> | Arquitetura de API Security | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M12-L04`</small> | Autenticação e autorização distribuídas | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M12-L05`</small> | API Gateway, service mesh e mTLS | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M12-L06`</small> | Segurança de microsserviços e containers | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M12-L07`</small> | CI/CD, IaC e software supply chain | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 08<br><small>`M12-L08`</small> | SAST, DAST, SCA, secrets scanning e SBOM na arquitetura | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 13 — Data Security Architecture"

    **ID técnico:** `M13` · **Domínios:** Data Security · **Pré-requisitos:** Módulo 1, Módulo 3

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M13-L01`</small> | Classificação e ciclo de vida de dados | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M13-L02`</small> | Criptografia at rest, in transit e in use | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M13-L03`</small> | Tokenização, hashing e mascaramento | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M13-L04`</small> | KMS, HSM e rotação de chaves | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M13-L05`</small> | Data Loss Prevention e segurança de bancos de dados | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M13-L06`</small> | Governança de dados distribuídos, privacidade, retenção e LGPD | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M13-L07`</small> | Zero Trust aplicado a dados | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 14 — Vulnerability & Exposure Management Architecture"

    **ID técnico:** `M14` · **Domínios:** Vulnerability Management · **Pré-requisitos:** Módulo 3

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M14-L01`</small> | Arquitetura de um programa corporativo de gestão de vulnerabilidades | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M14-L02`</small> | Descoberta e cobertura de ativos | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M14-L03`</small> | Cobertura por superfície: infraestrutura, web, APIs, cloud, AD e containers | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M14-L04`</small> | Vulnerability Management versus Exposure Management | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M14-L05`</small> | Priorização: CVSS, EPSS, CISA KEV e contexto de negócio | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M14-L06`</small> | Ownership, SLA, remediação e exceções | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M14-L07`</small> | Automação, integrações, KPIs, KRIs e dashboards | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 08<br><small>`M14-L08`</small> | Programa centralizado para múltiplas organizações | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 15 — Security Operations & Resilience Architecture"

    **ID técnico:** `M15` · **Domínios:** Security Operations & Resilience · **Pré-requisitos:** Módulo 5, Módulo 6

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M15-L01`</small> | Arquitetura de logging e telemetria | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M15-L02`</small> | SIEM, SOAR, XDR e EDR | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M15-L03`</small> | Detecção em ambientes híbridos | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M15-L04`</small> | Incident response e gestão de crises | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M15-L05`</small> | Resiliência contra ransomware, backup imutável e disaster recovery | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M15-L06`</small> | Validação de controles e exercícios tabletop | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M15-L07`</small> | Segurança da cadeia de suprimentos | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |

### Nível 5 — Arquitetura Corporativa Avançada

Arquitetura corporativa, governança entre empresas e projeto final.

| Módulo | Título | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| Módulo 16<br><small>`M16`</small> | Enterprise Security Architecture | 8 | 10 h | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| Módulo 17<br><small>`M17`</small> | Estudos de Caso e Projeto Final | 5 | 8 h 30 min | 3 | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 16 — Enterprise Security Architecture"

    **ID técnico:** `M16` · **Domínios:** Enterprise Security Architecture, Governance, Risk & Compliance · **Pré-requisitos:** Módulo 3, Módulo 11

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M16-L01`</small> | Arquitetura orientada ao negócio com SABSA | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M16-L02`</small> | SABSA e TOGAF integrados | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M16-L03`</small> | Modelos centralizado, federado e descentralizado | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M16-L04`</small> | Arquitetura corporativa de referência e shared security services | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M16-L05`</small> | Governança de segurança entre empresas de um grupo | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 06<br><small>`M16-L06`</small> | Architecture Review Boards, padrões, exceções e technical debt | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 07<br><small>`M16-L07`</small> | Gestão de stakeholders e negociação de riscos | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 08<br><small>`M16-L08`</small> | Estratégia, roadmaps, orçamento, TCO e priorização de investimentos | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "Módulo 17 — Estudos de Caso e Projeto Final"

    **ID técnico:** `M17` · **Domínios:** Enterprise Security Architecture, Hybrid & Multicloud Security · **Pré-requisitos:** Módulo 16

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | Aula 01<br><small>`M17-L01`</small> | Avaliação de maturidade e levantamento de requisitos | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 02<br><small>`M17-L02`</small> | Arquitetura base, identificação de lacunas e seleção de controles | Architect | 120 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 03<br><small>`M17-L03`</small> | Desenho da arquitetura híbrida e da governança de segurança | Architect | 120 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 04<br><small>`M17-L04`</small> | Roadmap de 90 dias, 6 meses e 12 meses | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | Aula 05<br><small>`M17-L05`</small> | Apresentação executiva e documentação para engenharia | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |

### Seção complementar

| ID | Conteúdo | Aulas | Fase | Status |
|:---|:---|:---|:---|:---|
| `C01` | Complemento: Segurança de IA/LLM e identidades não humanas | 4 | 3 | <span class="saa-status saa-status--planned">Planned</span> |

<small>Títulos de aulas com status Planned são provisórios até a produção do módulo.</small>

<!-- curriculum:end -->

## Atividades e artefatos

<!-- activities:start -->

### Estudos de caso

| ID | Título | Módulos | Fase | Status |
|:---|:---|:---|:---|:---|
| `CS-A` | [Caso A — Datacenter tradicional (Meridiana Distribuidora)](../case-studies/case-a-meridiana/index.md) | Módulo 2, Módulo 5, Módulo 6, Módulo 8 | 1 | <span class="saa-status saa-status--published">Published</span> |
| `CS-B` | Caso B — Migração para AWS | Módulo 9, Módulo 11 | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `CS-C` | Caso C — Arquitetura híbrida com Azure e AWS | Módulo 10, Módulo 11 | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `CS-D` | Caso D — Grupo empresarial com subsidiárias | Módulo 16 | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `CS-E` | Caso E — Programa corporativo de Vulnerability Management | Módulo 14 | 3 | <span class="saa-status saa-status--planned">Planned</span> |

### Laboratórios

| ID | Título | Módulos | Fase | Status |
|:---|:---|:---|:---|:---|
| `LAB-00` | [Laboratório 00 — Plano de endereçamento e segmentação](../labs/lab-00-network-plan.md) · *executado e testado* | Módulo Inicial | 1 | <span class="saa-status saa-status--published">Published</span> |
| `LAB-01` | [Laboratório 01 — Mecanismos de segurança na prática](../labs/lab-01-security-mechanisms.md) · *executado e testado* | Módulo 1 | 1 | <span class="saa-status saa-status--published">Published</span> |
| `LAB-02` | [Laboratório 02 — Modelagem arquitetural como código](../labs/lab-02-architecture-modeling.md) · *executado e testado* | Módulo 2 | 1 | <span class="saa-status saa-status--published">Published</span> |

### Avaliações

| ID | Título | Módulos | Fase | Status |
|:---|:---|:---|:---|:---|
| `AS-DIAG` | [Avaliação diagnóstica de fundamentos](../assessments/diagnostic-fundamentals.md) | Módulo Inicial, Módulo 1 | 1 | <span class="saa-status saa-status--published">Published</span> |
| `AS-M00` | [Avaliação do Módulo Inicial](../assessments/m00-foundations.md) | Módulo Inicial | 1 | <span class="saa-status saa-status--published">Published</span> |
| `AS-M01` | [Avaliação do Módulo 1](../assessments/m01-security-fundamentals.md) | Módulo 1 | 1 | <span class="saa-status saa-status--published">Published</span> |
| `AS-FUND` | [Avaliação integradora do Módulo Inicial ao Módulo 2](../assessments/fundamentals-final.md) | Módulo Inicial, Módulo 1, Módulo 2 | 1 | <span class="saa-status saa-status--published">Published</span> |
| `AS-M02` | [Avaliação do Módulo 2](../assessments/m02-security-architecture.md) | Módulo 2 | 1 | <span class="saa-status saa-status--published">Published</span> |
| `AS-N1` | [Avaliação integradora do Nível 1](../assessments/level-1-integrative.md) | Módulo 2, Módulo 3, Módulo 4 | 2 | <span class="saa-status saa-status--published">Published</span> |
| `AS-MID` | Avaliação intermediária (Níveis 1 e 2) | Módulo 3, Módulo 4, Módulo 5, Módulo 6, Módulo 7, Módulo 8 | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `AS-FINAL` | Avaliação final | Módulo 9, Módulo 10, Módulo 11, Módulo 12, Módulo 13, Módulo 14, Módulo 15, Módulo 16 | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `AS-ADV-EN` | Advanced assessment (English, CISSP/ISSAP reasoning style) | Módulo 2, Módulo 3, Módulo 6, Módulo 7, Módulo 11, Módulo 16 | 3 | <span class="saa-status saa-status--planned">Planned</span> |

### Modelos de artefatos

| ID | Título | Módulos | Fase | Status |
|:---|:---|:---|:---|:---|
| `ART-ADR` | [Architecture Decision Record](../artifacts/architecture-decision-record.md) | — | 1 | <span class="saa-status saa-status--published">Published</span> |
| `ART-SRS` | [Security Requirements Specification](../artifacts/security-requirements-specification.md) | — | 1 | <span class="saa-status saa-status--published">Published</span> |
| `ART-ARC` | [Architecture Review Checklist](../artifacts/architecture-review-checklist.md) | — | 1 | <span class="saa-status saa-status--published">Published</span> |
| `ART-SAA` | Security Architecture Assessment | — | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `ART-TM` | Threat Model | — | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `ART-SCM` | Security Control Matrix | — | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `ART-RR` | Risk Register | — | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `ART-HSAB` | Hybrid Security Architecture Blueprint | — | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `ART-SMA` | Security Maturity Assessment | — | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `ART-VMP` | Vulnerability Management Program | — | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `ART-ROAD` | Security Architecture Roadmap | — | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `ART-EXEC` | Executive Architecture Summary | — | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `ART-RACI` | Matriz RACI | — | 2 | <span class="saa-status saa-status--planned">Planned</span> |

<!-- activities:end -->

## Veja também

- [Dependências entre módulos](dependencies.md)
- [Mapa de competências](competencies.md) e [matriz de cobertura](coverage-matrix.md)
- [Learning Paths](../learning-paths/index.md) e [plano de estudo](../learning-paths/study-plan.md)
