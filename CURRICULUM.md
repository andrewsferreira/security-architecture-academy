# Currículo

<!-- Arquivo gerado por scripts/render_curriculum.py a partir de curriculum/manifest.yml. Não edite à mão. -->

Visão completa da formação. Versão navegável: [Curriculum Roadmap](https://andrewsferreira.github.io/security-architecture-academy/curriculum/). Manifesto atualizado em 2026-10-23.

**Legenda de status:** Planned (planejado) · Draft (em escrita) · In Review (em revisão) · Published (publicado) · Deprecated (descontinuado).

## Fases do projeto

| Fase | Status |
|:---|:---|
| Fase 0 — Planejamento acadêmico e técnico | In Review |
| Fase 1 — MVP educacional (Módulo 2) | In Review |
| Fase 2 — Formação profissional prioritária | Planned |
| Fase 3 — Expansão curricular | Planned |

## Nível 0 — Fundamentos de Tecnologia e Segurança

Infraestrutura, redes, cloud e fundamentos de segurança como linguagem comum.

### Módulo Inicial — Fundamentos de Infraestrutura e Computação

ID técnico: `M00` · Status: **Published** · Fase 3 · Pré-requisitos: nenhum

- **Aula 01** — [Computação, sistemas operacionais e virtualização](docs/modules/00-foundations/01-computing-os-virtualization.md) — `M00-L01` · Fundamental, 60 min — Published
- **Aula 02** — [Redes TCP/IP: modelo OSI, endereçamento, DNS, DHCP e NAT](docs/modules/00-foundations/02-tcp-ip-networking.md) — `M00-L02` · Fundamental, 75 min — Published
- **Aula 03** — [Segmentação e conectividade: VLAN, roteamento, VPN, TLS e firewalls](docs/modules/00-foundations/03-segmentation-connectivity.md) — `M00-L03` · Fundamental, 75 min — Published
- **Aula 04** — [Datacenters, armazenamento, clusters e alta disponibilidade](docs/modules/00-foundations/04-datacenter-high-availability.md) — `M00-L04` · Fundamental, 60 min — Published
- **Aula 05** — [Containers, Kubernetes, APIs, microsserviços e serverless](docs/modules/00-foundations/05-containers-apis-serverless.md) — `M00-L05` · Fundamental, 75 min — Published
- **Aula 06** — [Cloud computing: modelos de serviço e de implantação](docs/modules/00-foundations/06-cloud-computing-models.md) — `M00-L06` · Fundamental, 60 min — Published
- **Aula 07** — [Lendo diagramas arquiteturais: componentes, fluxos e fronteiras](docs/modules/00-foundations/07-reading-architecture-diagrams.md) — `M00-L07` · Fundamental, 60 min — Published

### Módulo 1 — Fundamentos de Segurança

ID técnico: `M01` · Status: **Published** · Fase 3 · Pré-requisitos: Módulo Inicial

- **Aula 01** — [Propriedades de segurança: CIA, autenticidade, autorização e não repúdio](docs/modules/01-security-fundamentals/01-security-properties.md) — `M01-L01` · Fundamental, 60 min — Published
- **Aula 02** — [Princípios de design seguro](docs/modules/01-security-fundamentals/02-secure-design-principles.md) — `M01-L02` · Fundamental, 75 min — Published
- **Aula 03** — [Trust boundaries, attack surface e responsabilidade compartilhada](docs/modules/01-security-fundamentals/03-trust-boundaries-attack-surface.md) — `M01-L03` · Fundamental, 60 min — Published
- **Aula 04** — [Criptografia aplicada: simétrica, assimétrica, hashing e assinaturas](docs/modules/01-security-fundamentals/04-applied-cryptography.md) — `M01-L04` · Fundamental, 75 min — Published
- **Aula 05** — [PKI, certificados, TLS e gerenciamento de chaves](docs/modules/01-security-fundamentals/05-pki-tls-key-management.md) — `M01-L05` · Fundamental, 75 min — Published
- **Aula 06** — [Ameaça, vulnerabilidade, risco, exposição e controle](docs/modules/01-security-fundamentals/06-threat-vulnerability-risk.md) — `M01-L06` · Fundamental, 60 min — Published
- **Aula 07** — [Modelos formais: Bell-LaPadula, Biba, Clark-Wilson e Brewer-Nash](docs/modules/01-security-fundamentals/07-formal-security-models.md) — `M01-L07` · Professional, 60 min — Published

## Nível 1 — Fundamentos de Arquitetura

O ofício do arquiteto, governança e riscos, e métodos de design e threat modeling.

### Módulo 2 — Introdução à Arquitetura de Segurança

ID técnico: `M02` · Status: **Published** · Fase 1 · Pré-requisitos: Módulo Inicial, Módulo 1

- **Aula 01** — [O papel do Security Architect](docs/modules/02-security-architecture/01-security-architect-role.md) — `M02-L01` · Fundamental, 60 min — Published
- **Aula 02** — [Enterprise, Solution e Security Architecture](docs/modules/02-security-architecture/02-enterprise-solution-security-architecture.md) — `M02-L02` · Fundamental, 60 min — Published
- **Aula 03** — [Arquitetura conceitual, lógica e física](docs/modules/02-security-architecture/03-conceptual-logical-physical.md) — `M02-L03` · Professional, 75 min — Published
- **Aula 04** — [Princípios, padrões, baselines e exceções](docs/modules/02-security-architecture/04-principles-standards-baselines-exceptions.md) — `M02-L04` · Professional, 75 min — Published
- **Aula 05** — [Arquiteturas de referência e blueprints](docs/modules/02-security-architecture/05-reference-architectures-blueprints.md) — `M02-L05` · Professional, 60 min — Published
- **Aula 06** — [Frameworks, padrões e certificações: NIST, SABSA, TOGAF, CISSP e ISSAP](docs/modules/02-security-architecture/06-frameworks.md) — `M02-L06` · Professional, 90 min — Published
- **Aula 07** — [Business-driven Security Architecture: de requisitos de negócio a requisitos de segurança](docs/modules/02-security-architecture/07-business-driven-requirements.md) — `M02-L07` · Architect, 90 min — Published
- **Aula 08** — [Architecture Decision Records](docs/modules/02-security-architecture/08-architecture-decision-records.md) — `M02-L08` · Architect, 75 min — Published

### Módulo 3 — Governança, Riscos e Controles

ID técnico: `M03` · Status: **Planned** · Fase 2 · Pré-requisitos: Módulo 2

- **Aula 01** — Governança de segurança e o NIST CSF 2.0 — `M03-L01` · Fundamental, 75 min — Planned
- **Aula 02** — NIST Risk Management Framework (SP 800-37) — `M03-L02` · Professional, 75 min — Planned
- **Aula 03** — Seleção e tailoring de controles: SP 800-53 e CIS Controls — `M03-L03` · Professional, 90 min — Planned
- **Aula 04** — ISO/IEC 27001/27002, LGPD e PCI DSS: propósito e escopo — `M03-L04` · Fundamental, 75 min — Planned
- **Aula 05** — Business Impact Analysis, RTO e RPO — `M03-L05` · Professional, 60 min — Planned
- **Aula 06** — Risk assessment, risk register e tratamento de riscos — `M03-L06` · Professional, 90 min — Planned
- **Aula 07** — Catálogo de controles e arquitetura baseada em risco — `M03-L07` · Architect, 75 min — Planned
- **Aula 08** — Indicadores, maturidade e reporte à governança — `M03-L08` · Architect, 60 min — Planned

### Módulo 4 — Métodos de Design e Threat Modeling

ID técnico: `M04` · Status: **Planned** · Fase 3 · Pré-requisitos: Módulo 2

- **Aula 01** — Data Flow Diagrams e fluxos de confiança — `M04-L01` · Fundamental, 60 min — Planned
- **Aula 02** — STRIDE aplicado à arquitetura — `M04-L02` · Professional, 75 min — Planned
- **Aula 03** — Attack trees e abuse cases — `M04-L03` · Professional, 60 min — Planned
- **Aula 04** — MITRE ATT&CK para cenários de ataque — `M04-L04` · Professional, 75 min — Planned
- **Aula 05** — Pontos únicos de falha e análise de dependências — `M04-L05` · Professional, 60 min — Planned
- **Aula 06** — De ameaças a requisitos de segurança — `M04-L06` · Architect, 75 min — Planned
- **Aula 07** — Revisão arquitetural, As-Is/To-Be e validação de controles — `M04-L07` · Architect, 75 min — Planned

## Nível 2 — Arquiteturas de Infraestrutura

Rede, identidade, Zero Trust e ambientes on-premises e legados.

### Módulo 5 — Network Security Architecture

ID técnico: `M05` · Status: **Planned** · Fase 3 · Pré-requisitos: Módulo Inicial, Módulo 2

- **Aula 01** — Zonas de confiança, segmentação e microsegmentação — `M05-L01` · Fundamental, 75 min — Planned
- **Aula 02** — Perímetro e inspeção: DMZ, WAF, NGFW, IDS/IPS e proxies — `M05-L02` · Professional, 75 min — Planned
- **Aula 03** — Tráfego North-South e East-West — `M05-L03` · Professional, 60 min — Planned
- **Aula 04** — Acesso remoto: VPN, ZTNA e bastion hosts — `M05-L04` · Professional, 75 min — Planned
- **Aula 05** — SD-WAN, SASE e SSE — `M05-L05` · Professional, 60 min — Planned
- **Aula 06** — Network Access Control — `M05-L06` · Professional, 45 min — Planned
- **Aula 07** — Desenho de uma rede corporativa segura — `M05-L07` · Architect, 90 min — Planned

### Módulo 6 — Identity & Access Management

ID técnico: `M06` · Status: **Planned** · Fase 2 · Pré-requisitos: Módulo 1, Módulo 2

- **Aula 01** — Disciplinas de identidade: IAM, IGA, PAM e PIM — `M06-L01` · Fundamental, 60 min — Planned
- **Aula 02** — Modelos de autorização: RBAC, ABAC e acesso contextual — `M06-L02` · Professional, 75 min — Planned
- **Aula 03** — Diretórios e autenticação corporativa: Active Directory, LDAP e Kerberos — `M06-L03` · Professional, 90 min — Planned
- **Aula 04** — Federação: SAML 2.0, OAuth 2.0 e OpenID Connect — `M06-L04` · Professional, 90 min — Planned
- **Aula 05** — Identidade híbrida: Active Directory, Microsoft Entra ID e provedores cloud — `M06-L05` · Architect, 90 min — Planned
- **Aula 06** — Contas privilegiadas e identidades de máquina — `M06-L06` · Professional, 75 min — Planned
- **Aula 07** — Workload Identity Federation — `M06-L07` · Architect, 60 min — Planned
- **Aula 08** — Ciclo de vida de identidades e segregação de funções — `M06-L08` · Professional, 60 min — Planned
- **Aula 09** — Recuperação de identidade em incidentes — `M06-L09` · Architect, 75 min — Planned

### Módulo 7 — Zero Trust Architecture

ID técnico: `M07` · Status: **Planned** · Fase 2 · Pré-requisitos: Módulo 5, Módulo 6

- **Aula 01** — Fundamentos de Zero Trust e o NIST SP 800-207 — `M07-L01` · Fundamental, 75 min — Planned
- **Aula 02** — Componentes lógicos: Policy Engine, Policy Administrator e PEP — `M07-L02` · Professional, 60 min — Planned
- **Aula 03** — Abordagens identity-centric, resource-centric e de rede — `M07-L03` · Professional, 60 min — Planned
- **Aula 04** — Verificação contínua, postura de dispositivo e acesso adaptativo — `M07-L04` · Professional, 75 min — Planned
- **Aula 05** — Segmentação e proteção de workloads — `M07-L05` · Professional, 60 min — Planned
- **Aula 06** — CISA Zero Trust Maturity Model — `M07-L06` · Architect, 60 min — Planned
- **Aula 07** — Implantação progressiva com sistemas legados e restrições — `M07-L07` · Architect, 90 min — Planned

### Módulo 8 — On-Premises e Sistemas Legados

ID técnico: `M08` · Status: **Planned** · Fase 3 · Pré-requisitos: Módulo 5, Módulo 6

- **Aula 01** — Segurança de datacenters — `M08-L01` · Fundamental, 60 min — Planned
- **Aula 02** — Hardening e baselines de configuração — `M08-L02` · Professional, 75 min — Planned
- **Aula 03** — Arquitetura para Windows Server, Linux e Active Directory — `M08-L03` · Professional, 90 min — Planned
- **Aula 04** — Backup, recuperação e resiliência contra ransomware — `M08-L04` · Professional, 75 min — Planned
- **Aula 05** — Sistemas sem suporte e controles compensatórios — `M08-L05` · Architect, 60 min — Planned
- **Aula 06** — Protocolos inseguros e dependências legadas — `M08-L06` · Professional, 60 min — Planned
- **Aula 07** — Integração com ambientes modernos e modernização gradual — `M08-L07` · Architect, 75 min — Planned

## Nível 3 — Arquitetura Cloud e Híbrida

AWS, Azure, Google Cloud e a integração segura entre ambientes.

### Módulo 9 — AWS Security Architecture

ID técnico: `M09` · Status: **Planned** · Fase 3 · Pré-requisitos: Módulo 5, Módulo 6

- **Aula 01** — Security Pillar do Well-Architected e responsabilidade compartilhada — `M09-L01` · Fundamental, 60 min — Planned
- **Aula 02** — AWS Organizations, multi-account, landing zones e Control Tower — `M09-L02` · Professional, 90 min — Planned
- **Aula 03** — IAM e IAM Identity Center — `M09-L03` · Professional, 90 min — Planned
- **Aula 04** — Rede: VPC, Security Groups, NACLs, roteamento e endpoints — `M09-L04` · Professional, 75 min — Planned
- **Aula 05** — Dados e segredos: AWS KMS e Secrets Manager — `M09-L05` · Professional, 60 min — Planned
- **Aula 06** — Detecção e governança: CloudTrail, Config, GuardDuty, Security Hub, Inspector e Macie — `M09-L06` · Professional, 90 min — Planned
- **Aula 07** — AWS Security Reference Architecture e integração com on-premises — `M09-L07` · Architect, 90 min — Planned

### Módulo 10 — Azure e Google Cloud

ID técnico: `M10` · Status: **Planned** · Fase 3 · Pré-requisitos: Módulo 5, Módulo 6

- **Aula 01** — Azure Well-Architected, Cloud Adoption Framework e Azure Landing Zones — `M10-L01` · Professional, 75 min — Planned
- **Aula 02** — Microsoft Entra ID e identidade híbrida — `M10-L02` · Professional, 75 min — Planned
- **Aula 03** — Defender for Cloud, Azure Policy e Azure Arc — `M10-L03` · Professional, 75 min — Planned
- **Aula 04** — Google Cloud: Architecture Framework e hierarquia de recursos — `M10-L04` · Professional, 60 min — Planned
- **Aula 05** — Google Cloud IAM, Organization Policy e Security Command Center — `M10-L05` · Professional, 75 min — Planned
- **Aula 06** — Equivalências e particularidades entre AWS, Azure e Google Cloud — `M10-L06` · Architect, 60 min — Planned
- **Aula 07** — Mapeamento para o Microsoft SC-100 — `M10-L07` · Architect, 45 min — Planned

### Módulo 11 — Hybrid & Multicloud Security Architecture

ID técnico: `M11` · Status: **Planned** · Fase 2 · Pré-requisitos: Módulo 6, Módulo 7

- **Aula 01** — Conectividade híbrida: VPN site-to-site, AWS Direct Connect e Azure ExpressRoute — `M11-L01` · Professional, 90 min — Planned
- **Aula 02** — Arquitetura de DNS híbrido — `M11-L02` · Professional, 60 min — Planned
- **Aula 03** — Identidade e federação entre Active Directory e provedores cloud — `M11-L03` · Architect, 90 min — Planned
- **Aula 04** — Logs, observabilidade, SIEM e SOC multiambiente — `M11-L04` · Professional, 75 min — Planned
- **Aula 05** — Segredos, certificados, criptografia e chaves distribuídos — `M11-L05` · Professional, 75 min — Planned
- **Aula 06** — Políticas consistentes e postura: CSPM, CNAPP, CWPP, CIEM e DSPM — `M11-L06` · Architect, 90 min — Planned
- **Aula 07** — Asset discovery e inventário corporativo — `M11-L07` · Professional, 60 min — Planned
- **Aula 08** — Backup, disaster recovery e continuidade em ambientes híbridos — `M11-L08` · Architect, 75 min — Planned
- **Aula 09** — Comunicação segura entre workloads — `M11-L09` · Professional, 60 min — Planned
- **Aula 10** — Responsabilidade compartilhada, soberania, latência e vendor lock-in — `M11-L10` · Architect, 75 min — Planned
- **Aula 11** — Três modelos de referência híbridos: As-Is e To-Be — `M11-L11` · Architect, 120 min — Planned

## Nível 4 — Arquitetura de Segurança Aplicada

Aplicações, dados, gestão de vulnerabilidades e exposição, operações e resiliência.

### Módulo 12 — Application Security Architecture

ID técnico: `M12` · Status: **Planned** · Fase 3 · Pré-requisitos: Módulo 4, Módulo 6

- **Aula 01** — Secure SDLC e DevSecOps — `M12-L01` · Fundamental, 60 min — Planned
- **Aula 02** — OWASP ASVS como especificação de requisitos — `M12-L02` · Professional, 60 min — Planned
- **Aula 03** — Arquitetura de API Security — `M12-L03` · Professional, 75 min — Planned
- **Aula 04** — Autenticação e autorização distribuídas — `M12-L04` · Professional, 75 min — Planned
- **Aula 05** — API Gateway, service mesh e mTLS — `M12-L05` · Professional, 60 min — Planned
- **Aula 06** — Segurança de microsserviços e containers — `M12-L06` · Professional, 75 min — Planned
- **Aula 07** — CI/CD, IaC e software supply chain — `M12-L07` · Architect, 75 min — Planned
- **Aula 08** — SAST, DAST, SCA, secrets scanning e SBOM na arquitetura — `M12-L08` · Professional, 60 min — Planned

### Módulo 13 — Data Security Architecture

ID técnico: `M13` · Status: **Planned** · Fase 3 · Pré-requisitos: Módulo 1, Módulo 3

- **Aula 01** — Classificação e ciclo de vida de dados — `M13-L01` · Fundamental, 60 min — Planned
- **Aula 02** — Criptografia at rest, in transit e in use — `M13-L02` · Professional, 75 min — Planned
- **Aula 03** — Tokenização, hashing e mascaramento — `M13-L03` · Professional, 60 min — Planned
- **Aula 04** — KMS, HSM e rotação de chaves — `M13-L04` · Professional, 75 min — Planned
- **Aula 05** — Data Loss Prevention e segurança de bancos de dados — `M13-L05` · Professional, 75 min — Planned
- **Aula 06** — Governança de dados distribuídos, privacidade, retenção e LGPD — `M13-L06` · Architect, 75 min — Planned
- **Aula 07** — Zero Trust aplicado a dados — `M13-L07` · Architect, 60 min — Planned

### Módulo 14 — Vulnerability & Exposure Management Architecture

ID técnico: `M14` · Status: **Planned** · Fase 3 · Pré-requisitos: Módulo 3

- **Aula 01** — Arquitetura de um programa corporativo de gestão de vulnerabilidades — `M14-L01` · Professional, 75 min — Planned
- **Aula 02** — Descoberta e cobertura de ativos — `M14-L02` · Professional, 60 min — Planned
- **Aula 03** — Cobertura por superfície: infraestrutura, web, APIs, cloud, AD e containers — `M14-L03` · Professional, 75 min — Planned
- **Aula 04** — Vulnerability Management versus Exposure Management — `M14-L04` · Professional, 60 min — Planned
- **Aula 05** — Priorização: CVSS, EPSS, CISA KEV e contexto de negócio — `M14-L05` · Architect, 75 min — Planned
- **Aula 06** — Ownership, SLA, remediação e exceções — `M14-L06` · Professional, 60 min — Planned
- **Aula 07** — Automação, integrações, KPIs, KRIs e dashboards — `M14-L07` · Professional, 60 min — Planned
- **Aula 08** — Programa centralizado para múltiplas organizações — `M14-L08` · Architect, 75 min — Planned

### Módulo 15 — Security Operations & Resilience Architecture

ID técnico: `M15` · Status: **Planned** · Fase 3 · Pré-requisitos: Módulo 5, Módulo 6

- **Aula 01** — Arquitetura de logging e telemetria — `M15-L01` · Professional, 75 min — Planned
- **Aula 02** — SIEM, SOAR, XDR e EDR — `M15-L02` · Professional, 75 min — Planned
- **Aula 03** — Detecção em ambientes híbridos — `M15-L03` · Architect, 60 min — Planned
- **Aula 04** — Incident response e gestão de crises — `M15-L04` · Professional, 75 min — Planned
- **Aula 05** — Resiliência contra ransomware, backup imutável e disaster recovery — `M15-L05` · Architect, 75 min — Planned
- **Aula 06** — Validação de controles e exercícios tabletop — `M15-L06` · Professional, 60 min — Planned
- **Aula 07** — Segurança da cadeia de suprimentos — `M15-L07` · Architect, 60 min — Planned

## Nível 5 — Arquitetura Corporativa Avançada

Arquitetura corporativa, governança entre empresas e projeto final.

### Módulo 16 — Enterprise Security Architecture

ID técnico: `M16` · Status: **Planned** · Fase 2 · Pré-requisitos: Módulo 3, Módulo 11

- **Aula 01** — Arquitetura orientada ao negócio com SABSA — `M16-L01` · Architect, 90 min — Planned
- **Aula 02** — SABSA e TOGAF integrados — `M16-L02` · Architect, 75 min — Planned
- **Aula 03** — Modelos centralizado, federado e descentralizado — `M16-L03` · Architect, 60 min — Planned
- **Aula 04** — Arquitetura corporativa de referência e shared security services — `M16-L04` · Architect, 75 min — Planned
- **Aula 05** — Governança de segurança entre empresas de um grupo — `M16-L05` · Architect, 75 min — Planned
- **Aula 06** — Architecture Review Boards, padrões, exceções e technical debt — `M16-L06` · Architect, 75 min — Planned
- **Aula 07** — Gestão de stakeholders e negociação de riscos — `M16-L07` · Architect, 60 min — Planned
- **Aula 08** — Estratégia, roadmaps, orçamento, TCO e priorização de investimentos — `M16-L08` · Architect, 90 min — Planned

### Módulo 17 — Estudos de Caso e Projeto Final

ID técnico: `M17` · Status: **Planned** · Fase 3 · Pré-requisitos: Módulo 16

- **Aula 01** — Avaliação de maturidade e levantamento de requisitos — `M17-L01` · Architect, 90 min — Planned
- **Aula 02** — Arquitetura base, identificação de lacunas e seleção de controles — `M17-L02` · Architect, 120 min — Planned
- **Aula 03** — Desenho da arquitetura híbrida e da governança de segurança — `M17-L03` · Architect, 120 min — Planned
- **Aula 04** — Roadmap de 90 dias, 6 meses e 12 meses — `M17-L04` · Architect, 90 min — Planned
- **Aula 05** — Apresentação executiva e documentação para engenharia — `M17-L05` · Architect, 90 min — Planned

## Complemento: Segurança de IA/LLM e identidades não humanas

Status: **Planned** · Fase 3

- `C01-L01` Arquitetura de aplicações com IA e LLM — Planned
- `C01-L02` Ameaças a sistemas de IA: OWASP Top 10 for LLM e MITRE ATLAS — Planned
- `C01-L03` Identidades não humanas e agentes de IA — Planned
- `C01-L04` Riscos emergentes e governança de IA — Planned

## Atividades e artefatos

### Estudos de caso

- `CS-A` [Caso A — Datacenter tradicional (Meridiana Distribuidora)](docs/case-studies/case-a-meridiana/index.md) — Published
- `CS-B` Caso B — Migração para AWS — Planned
- `CS-C` Caso C — Arquitetura híbrida com Azure e AWS — Planned
- `CS-D` Caso D — Grupo empresarial com subsidiárias — Planned
- `CS-E` Caso E — Programa corporativo de Vulnerability Management — Planned

### Laboratórios

- `LAB-00` [Laboratório 00 — Plano de endereçamento e segmentação](docs/labs/lab-00-network-plan.md) — Published
- `LAB-01` [Laboratório 01 — Mecanismos de segurança na prática](docs/labs/lab-01-security-mechanisms.md) — Published
- `LAB-02` [Laboratório 02 — Modelagem arquitetural como código](docs/labs/lab-02-architecture-modeling.md) — Published

### Avaliações

- `AS-DIAG` [Avaliação diagnóstica de fundamentos](docs/assessments/diagnostic-fundamentals.md) — Published
- `AS-M00` [Avaliação do Módulo Inicial](docs/assessments/m00-foundations.md) — Published
- `AS-M01` [Avaliação do Módulo 1](docs/assessments/m01-security-fundamentals.md) — Published
- `AS-FUND` [Avaliação final de Fundamentals (integradora)](docs/assessments/fundamentals-final.md) — Published
- `AS-M02` [Avaliação do Módulo 2](docs/assessments/m02-security-architecture.md) — Published
- `AS-MID` Avaliação intermediária (Níveis 1 e 2) — Planned
- `AS-FINAL` Avaliação final — Planned
- `AS-ADV-EN` Advanced assessment (English, CISSP/ISSAP reasoning style) — Planned

### Modelos de artefatos

- `ART-ADR` [Architecture Decision Record](docs/artifacts/architecture-decision-record.md) — Published
- `ART-SRS` [Security Requirements Specification](docs/artifacts/security-requirements-specification.md) — Published
- `ART-ARC` [Architecture Review Checklist](docs/artifacts/architecture-review-checklist.md) — Published
- `ART-SAA` Security Architecture Assessment — Planned
- `ART-TM` Threat Model — Planned
- `ART-SCM` Security Control Matrix — Planned
- `ART-RR` Risk Register — Planned
- `ART-HSAB` Hybrid Security Architecture Blueprint — Planned
- `ART-SMA` Security Maturity Assessment — Planned
- `ART-VMP` Vulnerability Management Program — Planned
- `ART-ROAD` Security Architecture Roadmap — Planned
- `ART-EXEC` Executive Architecture Summary — Planned
- `ART-RACI` Matriz RACI — Planned
