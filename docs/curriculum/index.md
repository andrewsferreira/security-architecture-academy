---
title: Curriculum Roadmap
description: Estrutura curricular completa da Security Architecture Academy — 18 módulos em seis níveis, aulas, atividades e status editorial gerados a partir do manifesto.
---

# Curriculum Roadmap

A formação está organizada em **seis níveis progressivos** (Nível 0 a Nível 5), com **18 módulos** (M00 a M17) e uma seção complementar sobre segurança de IA. Esta página mostra cada módulo, suas aulas e o status editorial real de cada entrega.

!!! note "Como ler esta página"

    - Tudo abaixo é gerado de [`curriculum/manifest.yml`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/curriculum/manifest.yml) e verificado no CI.
    - **Fase** indica a ordem histórica de produção. A publicação segue releases por nível — Fundamentals (M00–M02), Professional (M03–M15) e Architect (M16, M17 e C01) —, descritas no [roadmap](../about/roadmap.md).
    - **Profundidade** indica o nível de exigência de cada aula: *Fundamental* (compreender), *Professional* (aplicar) e *Architect* (decidir e justificar).
    - Títulos de aulas com status **Planned** são provisórios até a produção do módulo.

## Status editoriais

| Status | Significado |
|:---|:---|
| <span class="saa-status saa-status--planned">Planned</span> | Definido no currículo, sem conteúdo produzido. |
| <span class="saa-status saa-status--draft">Draft</span> | Em escrita, fora da navegação. |
| <span class="saa-status saa-status--published">Published</span> | Conteúdo completo, aguardando revisão técnica. |
| <span class="saa-status saa-status--published">Published</span> | Revisado e publicado no site público. |
| <span class="saa-status saa-status--deprecated">Deprecated</span> | Mantido por referência, com indicação do substituto. |

Critérios de cada transição: [Modelo de conteúdo](../internal/content-model.md#criterios-de-publicacao).

## Módulos e aulas

<!-- curriculum:start -->

**18 módulos · 135 aulas · cerca de 162 horas de aulas** (sem laboratórios, estudos de caso e avaliações). Status das aulas: Planned **113** · Published **22**.

### Nível 0 — Fundamentos de Tecnologia e Segurança

Infraestrutura, redes, cloud e fundamentos de segurança como linguagem comum.

| ID | Módulo | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| `M00` | [Fundamentos de Infraestrutura e Computação](../modules/00-foundations/index.md) | 7 | 7 h 45 min | 3 | <span class="saa-status saa-status--published">Published</span> |
| `M01` | [Fundamentos de Segurança](../modules/01-security-fundamentals/index.md) | 7 | 7 h 45 min | 3 | <span class="saa-status saa-status--published">Published</span> |

??? abstract "M00 — Fundamentos de Infraestrutura e Computação"

    **Domínios:** Infrastructure Foundations · **Pré-requisitos:** nenhum

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M00-L01` | [Computação, sistemas operacionais e virtualização](../modules/00-foundations/01-computing-os-virtualization.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | `M00-L02` | [Redes TCP/IP: modelo OSI, endereçamento, DNS, DHCP e NAT](../modules/00-foundations/02-tcp-ip-networking.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | `M00-L03` | [Segmentação e conectividade: VLAN, roteamento, VPN, TLS e firewalls](../modules/00-foundations/03-segmentation-connectivity.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | `M00-L04` | [Datacenters, armazenamento, clusters e alta disponibilidade](../modules/00-foundations/04-datacenter-high-availability.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | `M00-L05` | [Containers, Kubernetes, APIs, microsserviços e serverless](../modules/00-foundations/05-containers-apis-serverless.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | `M00-L06` | [Cloud computing: modelos de serviço e de implantação](../modules/00-foundations/06-cloud-computing-models.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | `M00-L07` | [Lendo diagramas arquiteturais: componentes, fluxos e fronteiras](../modules/00-foundations/07-reading-architecture-diagrams.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |

??? abstract "M01 — Fundamentos de Segurança"

    **Domínios:** Security Foundations · **Pré-requisitos:** `M00`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M01-L01` | [Propriedades de segurança: CIA, autenticidade, autorização e não repúdio](../modules/01-security-fundamentals/01-security-properties.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | `M01-L02` | [Princípios de design seguro](../modules/01-security-fundamentals/02-secure-design-principles.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | `M01-L03` | [Trust boundaries, attack surface e responsabilidade compartilhada](../modules/01-security-fundamentals/03-trust-boundaries-attack-surface.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | `M01-L04` | [Criptografia aplicada: simétrica, assimétrica, hashing e assinaturas](../modules/01-security-fundamentals/04-applied-cryptography.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | `M01-L05` | [PKI, certificados, TLS e gerenciamento de chaves](../modules/01-security-fundamentals/05-pki-tls-key-management.md) | Fundamental | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | `M01-L06` | [Ameaça, vulnerabilidade, risco, exposição e controle](../modules/01-security-fundamentals/06-threat-vulnerability-risk.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | `M01-L07` | [Modelos formais: Bell-LaPadula, Biba, Clark-Wilson e Brewer-Nash](../modules/01-security-fundamentals/07-formal-security-models.md) | Professional | 60 min | <span class="saa-status saa-status--published">Published</span> |

### Nível 1 — Fundamentos de Arquitetura

O ofício do arquiteto, governança e riscos, e métodos de design e threat modeling.

| ID | Módulo | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| `M02` | [Introdução à Arquitetura de Segurança](../modules/02-security-architecture/index.md) | 8 | 9 h 45 min | 1 | <span class="saa-status saa-status--published">Published</span> |
| `M03` | Governança, Riscos e Controles | 8 | 10 h | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `M04` | Métodos de Design e Threat Modeling | 7 | 8 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M02 — Introdução à Arquitetura de Segurança"

    **Domínios:** Enterprise Security Architecture, Security Foundations · **Pré-requisitos:** `M00`, `M01`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M02-L01` | [O papel do Security Architect](../modules/02-security-architecture/01-security-architect-role.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | `M02-L02` | [Enterprise, Solution e Security Architecture](../modules/02-security-architecture/02-enterprise-solution-security-architecture.md) | Fundamental | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | `M02-L03` | [Arquitetura conceitual, lógica e física](../modules/02-security-architecture/03-conceptual-logical-physical.md) | Professional | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | `M02-L04` | [Princípios, padrões, baselines e exceções](../modules/02-security-architecture/04-principles-standards-baselines-exceptions.md) | Professional | 75 min | <span class="saa-status saa-status--published">Published</span> |
    | `M02-L05` | [Arquiteturas de referência e blueprints](../modules/02-security-architecture/05-reference-architectures-blueprints.md) | Professional | 60 min | <span class="saa-status saa-status--published">Published</span> |
    | `M02-L06` | [Frameworks, padrões e certificações: NIST, SABSA, TOGAF, CISSP e ISSAP](../modules/02-security-architecture/06-frameworks.md) | Professional | 90 min | <span class="saa-status saa-status--published">Published</span> |
    | `M02-L07` | [Business-driven Security Architecture: de requisitos de negócio a requisitos de segurança](../modules/02-security-architecture/07-business-driven-requirements.md) | Architect | 90 min | <span class="saa-status saa-status--published">Published</span> |
    | `M02-L08` | [Architecture Decision Records](../modules/02-security-architecture/08-architecture-decision-records.md) | Architect | 75 min | <span class="saa-status saa-status--published">Published</span> |

??? abstract "M03 — Governança, Riscos e Controles"

    **Domínios:** Governance, Risk & Compliance · **Pré-requisitos:** `M02`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M03-L01` | Governança de segurança e o NIST CSF 2.0 | Fundamental | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M03-L02` | NIST Risk Management Framework (SP 800-37) | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M03-L03` | Seleção e tailoring de controles: SP 800-53 e CIS Controls | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M03-L04` | ISO/IEC 27001/27002, LGPD e PCI DSS: propósito e escopo | Fundamental | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M03-L05` | Business Impact Analysis, RTO e RPO | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M03-L06` | Risk assessment, risk register e tratamento de riscos | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M03-L07` | Catálogo de controles e arquitetura baseada em risco | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M03-L08` | Indicadores, maturidade e reporte à governança | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M04 — Métodos de Design e Threat Modeling"

    **Domínios:** Application Security, Enterprise Security Architecture · **Pré-requisitos:** `M02`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M04-L01` | Data Flow Diagrams e fluxos de confiança | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M04-L02` | STRIDE aplicado à arquitetura | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M04-L03` | Attack trees e abuse cases | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M04-L04` | MITRE ATT&CK para cenários de ataque | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M04-L05` | Pontos únicos de falha e análise de dependências | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M04-L06` | De ameaças a requisitos de segurança | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M04-L07` | Revisão arquitetural, As-Is/To-Be e validação de controles | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |

### Nível 2 — Arquiteturas de Infraestrutura

Rede, identidade, Zero Trust e ambientes on-premises e legados.

| ID | Módulo | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| `M05` | Network Security Architecture | 7 | 8 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `M06` | Identity & Access Management | 9 | 11 h 15 min | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `M07` | Zero Trust Architecture | 7 | 8 h | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `M08` | On-Premises e Sistemas Legados | 7 | 8 h 15 min | 3 | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M05 — Network Security Architecture"

    **Domínios:** Network Security · **Pré-requisitos:** `M00`, `M02`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M05-L01` | Zonas de confiança, segmentação e microsegmentação | Fundamental | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M05-L02` | Perímetro e inspeção: DMZ, WAF, NGFW, IDS/IPS e proxies | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M05-L03` | Tráfego North-South e East-West | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M05-L04` | Acesso remoto: VPN, ZTNA e bastion hosts | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M05-L05` | SD-WAN, SASE e SSE | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M05-L06` | Network Access Control | Professional | 45 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M05-L07` | Desenho de uma rede corporativa segura | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M06 — Identity & Access Management"

    **Domínios:** Identity & Access Management · **Pré-requisitos:** `M01`, `M02`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M06-L01` | Disciplinas de identidade: IAM, IGA, PAM e PIM | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M06-L02` | Modelos de autorização: RBAC, ABAC e acesso contextual | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M06-L03` | Diretórios e autenticação corporativa: Active Directory, LDAP e Kerberos | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M06-L04` | Federação: SAML 2.0, OAuth 2.0 e OpenID Connect | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M06-L05` | Identidade híbrida: Active Directory, Microsoft Entra ID e provedores cloud | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M06-L06` | Contas privilegiadas e identidades de máquina | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M06-L07` | Workload Identity Federation | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M06-L08` | Ciclo de vida de identidades e segregação de funções | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M06-L09` | Recuperação de identidade em incidentes | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M07 — Zero Trust Architecture"

    **Domínios:** Zero Trust Architecture, Identity & Access Management, Network Security · **Pré-requisitos:** `M05`, `M06`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M07-L01` | Fundamentos de Zero Trust e o NIST SP 800-207 | Fundamental | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M07-L02` | Componentes lógicos: Policy Engine, Policy Administrator e PEP | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M07-L03` | Abordagens identity-centric, resource-centric e de rede | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M07-L04` | Verificação contínua, postura de dispositivo e acesso adaptativo | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M07-L05` | Segmentação e proteção de workloads | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M07-L06` | CISA Zero Trust Maturity Model | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M07-L07` | Implantação progressiva com sistemas legados e restrições | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M08 — On-Premises e Sistemas Legados"

    **Domínios:** Infrastructure Foundations, Security Operations & Resilience · **Pré-requisitos:** `M05`, `M06`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M08-L01` | Segurança de datacenters | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M08-L02` | Hardening e baselines de configuração | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M08-L03` | Arquitetura para Windows Server, Linux e Active Directory | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M08-L04` | Backup, recuperação e resiliência contra ransomware | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M08-L05` | Sistemas sem suporte e controles compensatórios | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M08-L06` | Protocolos inseguros e dependências legadas | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M08-L07` | Integração com ambientes modernos e modernização gradual | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |

### Nível 3 — Arquitetura Cloud e Híbrida

AWS, Azure, Google Cloud e a integração segura entre ambientes.

| ID | Módulo | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| `M09` | AWS Security Architecture | 7 | 9 h 15 min | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `M10` | Azure e Google Cloud | 7 | 7 h 45 min | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `M11` | Hybrid & Multicloud Security Architecture | 11 | 14 h 30 min | 2 | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M09 — AWS Security Architecture"

    **Domínios:** Cloud Security · **Pré-requisitos:** `M05`, `M06`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M09-L01` | Security Pillar do Well-Architected e responsabilidade compartilhada | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M09-L02` | AWS Organizations, multi-account, landing zones e Control Tower | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M09-L03` | IAM e IAM Identity Center | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M09-L04` | Rede: VPC, Security Groups, NACLs, roteamento e endpoints | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M09-L05` | Dados e segredos: AWS KMS e Secrets Manager | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M09-L06` | Detecção e governança: CloudTrail, Config, GuardDuty, Security Hub, Inspector e Macie | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M09-L07` | AWS Security Reference Architecture e integração com on-premises | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M10 — Azure e Google Cloud"

    **Domínios:** Cloud Security, Identity & Access Management · **Pré-requisitos:** `M05`, `M06`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M10-L01` | Azure Well-Architected, Cloud Adoption Framework e Azure Landing Zones | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M10-L02` | Microsoft Entra ID e identidade híbrida | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M10-L03` | Defender for Cloud, Azure Policy e Azure Arc | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M10-L04` | Google Cloud: Architecture Framework e hierarquia de recursos | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M10-L05` | Google Cloud IAM, Organization Policy e Security Command Center | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M10-L06` | Equivalências e particularidades entre AWS, Azure e Google Cloud | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M10-L07` | Mapeamento para o Microsoft SC-100 | Architect | 45 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M11 — Hybrid & Multicloud Security Architecture"

    **Domínios:** Hybrid & Multicloud Security, Cloud Security, Network Security, Identity & Access Management · **Pré-requisitos:** `M06`, `M07`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M11-L01` | Conectividade híbrida: VPN site-to-site, AWS Direct Connect e Azure ExpressRoute | Professional | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M11-L02` | Arquitetura de DNS híbrido | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M11-L03` | Identidade e federação entre Active Directory e provedores cloud | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M11-L04` | Logs, observabilidade, SIEM e SOC multiambiente | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M11-L05` | Segredos, certificados, criptografia e chaves distribuídos | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M11-L06` | Políticas consistentes e postura: CSPM, CNAPP, CWPP, CIEM e DSPM | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M11-L07` | Asset discovery e inventário corporativo | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M11-L08` | Backup, disaster recovery e continuidade em ambientes híbridos | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M11-L09` | Comunicação segura entre workloads | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M11-L10` | Responsabilidade compartilhada, soberania, latência e vendor lock-in | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M11-L11` | Três modelos de referência híbridos: As-Is e To-Be | Architect | 120 min | <span class="saa-status saa-status--planned">Planned</span> |

### Nível 4 — Arquitetura de Segurança Aplicada

Aplicações, dados, gestão de vulnerabilidades e exposição, operações e resiliência.

| ID | Módulo | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| `M12` | Application Security Architecture | 8 | 9 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `M13` | Data Security Architecture | 7 | 8 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `M14` | Vulnerability & Exposure Management Architecture | 8 | 9 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `M15` | Security Operations & Resilience Architecture | 7 | 8 h | 3 | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M12 — Application Security Architecture"

    **Domínios:** Application Security · **Pré-requisitos:** `M04`, `M06`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M12-L01` | Secure SDLC e DevSecOps | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M12-L02` | OWASP ASVS como especificação de requisitos | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M12-L03` | Arquitetura de API Security | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M12-L04` | Autenticação e autorização distribuídas | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M12-L05` | API Gateway, service mesh e mTLS | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M12-L06` | Segurança de microsserviços e containers | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M12-L07` | CI/CD, IaC e software supply chain | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M12-L08` | SAST, DAST, SCA, secrets scanning e SBOM na arquitetura | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M13 — Data Security Architecture"

    **Domínios:** Data Security · **Pré-requisitos:** `M01`, `M03`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M13-L01` | Classificação e ciclo de vida de dados | Fundamental | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M13-L02` | Criptografia at rest, in transit e in use | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M13-L03` | Tokenização, hashing e mascaramento | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M13-L04` | KMS, HSM e rotação de chaves | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M13-L05` | Data Loss Prevention e segurança de bancos de dados | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M13-L06` | Governança de dados distribuídos, privacidade, retenção e LGPD | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M13-L07` | Zero Trust aplicado a dados | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M14 — Vulnerability & Exposure Management Architecture"

    **Domínios:** Vulnerability Management · **Pré-requisitos:** `M03`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M14-L01` | Arquitetura de um programa corporativo de gestão de vulnerabilidades | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M14-L02` | Descoberta e cobertura de ativos | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M14-L03` | Cobertura por superfície: infraestrutura, web, APIs, cloud, AD e containers | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M14-L04` | Vulnerability Management versus Exposure Management | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M14-L05` | Priorização: CVSS, EPSS, CISA KEV e contexto de negócio | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M14-L06` | Ownership, SLA, remediação e exceções | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M14-L07` | Automação, integrações, KPIs, KRIs e dashboards | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M14-L08` | Programa centralizado para múltiplas organizações | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M15 — Security Operations & Resilience Architecture"

    **Domínios:** Security Operations & Resilience · **Pré-requisitos:** `M05`, `M06`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M15-L01` | Arquitetura de logging e telemetria | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M15-L02` | SIEM, SOAR, XDR e EDR | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M15-L03` | Detecção em ambientes híbridos | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M15-L04` | Incident response e gestão de crises | Professional | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M15-L05` | Resiliência contra ransomware, backup imutável e disaster recovery | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M15-L06` | Validação de controles e exercícios tabletop | Professional | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M15-L07` | Segurança da cadeia de suprimentos | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |

### Nível 5 — Arquitetura Corporativa Avançada

Arquitetura corporativa, governança entre empresas e projeto final.

| ID | Módulo | Aulas | Carga | Fase | Status |
|:---|:---|:---|:---|:---|:---|
| `M16` | Enterprise Security Architecture | 8 | 10 h | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `M17` | Estudos de Caso e Projeto Final | 5 | 8 h 30 min | 3 | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M16 — Enterprise Security Architecture"

    **Domínios:** Enterprise Security Architecture, Governance, Risk & Compliance · **Pré-requisitos:** `M03`, `M11`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M16-L01` | Arquitetura orientada ao negócio com SABSA | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M16-L02` | SABSA e TOGAF integrados | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M16-L03` | Modelos centralizado, federado e descentralizado | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M16-L04` | Arquitetura corporativa de referência e shared security services | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M16-L05` | Governança de segurança entre empresas de um grupo | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M16-L06` | Architecture Review Boards, padrões, exceções e technical debt | Architect | 75 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M16-L07` | Gestão de stakeholders e negociação de riscos | Architect | 60 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M16-L08` | Estratégia, roadmaps, orçamento, TCO e priorização de investimentos | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |

??? abstract "M17 — Estudos de Caso e Projeto Final"

    **Domínios:** Enterprise Security Architecture, Hybrid & Multicloud Security · **Pré-requisitos:** `M16`

    | Aula | Título | Profundidade | Tempo | Status |
    |:---|:---|:---|:---|:---|
    | `M17-L01` | Avaliação de maturidade e levantamento de requisitos | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M17-L02` | Arquitetura base, identificação de lacunas e seleção de controles | Architect | 120 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M17-L03` | Desenho da arquitetura híbrida e da governança de segurança | Architect | 120 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M17-L04` | Roadmap de 90 dias, 6 meses e 12 meses | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |
    | `M17-L05` | Apresentação executiva e documentação para engenharia | Architect | 90 min | <span class="saa-status saa-status--planned">Planned</span> |

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
| `CS-A` | [Caso A — Datacenter tradicional (Meridiana Distribuidora)](../case-studies/case-a-meridiana/index.md) | `M02`, `M05`, `M06`, `M08` | 1 | <span class="saa-status saa-status--published">Published</span> |
| `CS-B` | Caso B — Migração para AWS | `M09`, `M11` | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `CS-C` | Caso C — Arquitetura híbrida com Azure e AWS | `M10`, `M11` | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `CS-D` | Caso D — Grupo empresarial com subsidiárias | `M16` | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `CS-E` | Caso E — Programa corporativo de Vulnerability Management | `M14` | 3 | <span class="saa-status saa-status--planned">Planned</span> |

### Laboratórios

| ID | Título | Módulos | Fase | Status |
|:---|:---|:---|:---|:---|
| `LAB-00` | [Laboratório 00 — Plano de endereçamento e segmentação](../labs/lab-00-network-plan.md) · *executado e testado* | `M00` | 1 | <span class="saa-status saa-status--published">Published</span> |
| `LAB-01` | [Laboratório 01 — Mecanismos de segurança na prática](../labs/lab-01-security-mechanisms.md) · *executado e testado* | `M01` | 1 | <span class="saa-status saa-status--published">Published</span> |
| `LAB-02` | [Laboratório 02 — Modelagem arquitetural como código](../labs/lab-02-architecture-modeling.md) · *executado e testado* | `M02` | 1 | <span class="saa-status saa-status--published">Published</span> |

### Avaliações

| ID | Título | Módulos | Fase | Status |
|:---|:---|:---|:---|:---|
| `AS-DIAG` | [Avaliação diagnóstica de fundamentos](../assessments/diagnostic-fundamentals.md) | `M00`, `M01` | 1 | <span class="saa-status saa-status--published">Published</span> |
| `AS-M00` | [Avaliação do Módulo 00](../assessments/m00-foundations.md) | `M00` | 1 | <span class="saa-status saa-status--published">Published</span> |
| `AS-M01` | [Avaliação do Módulo 01](../assessments/m01-security-fundamentals.md) | `M01` | 1 | <span class="saa-status saa-status--published">Published</span> |
| `AS-FUND` | [Avaliação final de Fundamentals (integradora)](../assessments/fundamentals-final.md) | `M00`, `M01`, `M02` | 1 | <span class="saa-status saa-status--published">Published</span> |
| `AS-M02` | [Avaliação do Módulo 02](../assessments/m02-security-architecture.md) | `M02` | 1 | <span class="saa-status saa-status--published">Published</span> |
| `AS-MID` | Avaliação intermediária (Níveis 1 e 2) | `M03`, `M04`, `M05`, `M06`, `M07`, `M08` | 2 | <span class="saa-status saa-status--planned">Planned</span> |
| `AS-FINAL` | Avaliação final | `M09`, `M10`, `M11`, `M12`, `M13`, `M14`, `M15`, `M16` | 3 | <span class="saa-status saa-status--planned">Planned</span> |
| `AS-ADV-EN` | Advanced assessment (English, CISSP/ISSAP reasoning style) | `M02`, `M03`, `M06`, `M07`, `M11`, `M16` | 3 | <span class="saa-status saa-status--planned">Planned</span> |

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
