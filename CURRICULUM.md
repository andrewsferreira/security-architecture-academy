# Currículo

<!-- Arquivo gerado por scripts/render_curriculum.py a partir de curriculum/manifest.yml. Não edite à mão. -->

Visão completa da formação. Versão navegável: [Curriculum Roadmap](https://andrewsferreira.github.io/security-architecture-academy/curriculum/). Manifesto atualizado em 2026-10-23.

**Legenda de status:** Planned (planejado) · Draft (em escrita) · In Review (em revisão) · Published (publicado) · Deprecated (descontinuado).

## Fases do projeto

| Fase | Status |
|:---|:---|
| Fase 0 — Planejamento acadêmico e técnico | In Review |
| Fase 1 — MVP educacional (Módulo 02) | In Review |
| Fase 2 — Formação profissional prioritária | Planned |
| Fase 3 — Expansão curricular | Planned |

## Nível 0 — Fundamentos de Tecnologia e Segurança

Infraestrutura, redes, cloud e fundamentos de segurança como linguagem comum.

### M00 — Fundamentos de Infraestrutura e Computação

Status: **Published** · Fase 3 · Pré-requisitos: nenhum

- `M00-L01` [Computação, sistemas operacionais e virtualização](docs/modules/00-foundations/01-computing-os-virtualization.md) — Fundamental, 60 min — Published
- `M00-L02` [Redes TCP/IP: modelo OSI, endereçamento, DNS, DHCP e NAT](docs/modules/00-foundations/02-tcp-ip-networking.md) — Fundamental, 75 min — Published
- `M00-L03` [Segmentação e conectividade: VLAN, roteamento, VPN, TLS e firewalls](docs/modules/00-foundations/03-segmentation-connectivity.md) — Fundamental, 75 min — Published
- `M00-L04` [Datacenters, armazenamento, clusters e alta disponibilidade](docs/modules/00-foundations/04-datacenter-high-availability.md) — Fundamental, 60 min — Published
- `M00-L05` [Containers, Kubernetes, APIs, microsserviços e serverless](docs/modules/00-foundations/05-containers-apis-serverless.md) — Fundamental, 75 min — Published
- `M00-L06` [Cloud computing: modelos de serviço e de implantação](docs/modules/00-foundations/06-cloud-computing-models.md) — Fundamental, 60 min — Published
- `M00-L07` [Lendo diagramas arquiteturais: componentes, fluxos e fronteiras](docs/modules/00-foundations/07-reading-architecture-diagrams.md) — Fundamental, 60 min — Published

### M01 — Fundamentos de Segurança

Status: **Published** · Fase 3 · Pré-requisitos: M00

- `M01-L01` [Propriedades de segurança: CIA, autenticidade, autorização e não repúdio](docs/modules/01-security-fundamentals/01-security-properties.md) — Fundamental, 60 min — Published
- `M01-L02` [Princípios de design seguro](docs/modules/01-security-fundamentals/02-secure-design-principles.md) — Fundamental, 75 min — Published
- `M01-L03` [Trust boundaries, attack surface e responsabilidade compartilhada](docs/modules/01-security-fundamentals/03-trust-boundaries-attack-surface.md) — Fundamental, 60 min — Published
- `M01-L04` [Criptografia aplicada: simétrica, assimétrica, hashing e assinaturas](docs/modules/01-security-fundamentals/04-applied-cryptography.md) — Fundamental, 75 min — Published
- `M01-L05` [PKI, certificados, TLS e gerenciamento de chaves](docs/modules/01-security-fundamentals/05-pki-tls-key-management.md) — Fundamental, 75 min — Published
- `M01-L06` [Ameaça, vulnerabilidade, risco, exposição e controle](docs/modules/01-security-fundamentals/06-threat-vulnerability-risk.md) — Fundamental, 60 min — Published
- `M01-L07` [Modelos formais: Bell-LaPadula, Biba, Clark-Wilson e Brewer-Nash](docs/modules/01-security-fundamentals/07-formal-security-models.md) — Professional, 60 min — Published

## Nível 1 — Fundamentos de Arquitetura

O ofício do arquiteto, governança e riscos, e métodos de design e threat modeling.

### M02 — Introdução à Arquitetura de Segurança

Status: **Published** · Fase 1 · Pré-requisitos: M00, M01

- `M02-L01` [O papel do Security Architect](docs/modules/02-security-architecture/01-security-architect-role.md) — Fundamental, 60 min — Published
- `M02-L02` [Enterprise, Solution e Security Architecture](docs/modules/02-security-architecture/02-enterprise-solution-security-architecture.md) — Fundamental, 60 min — Published
- `M02-L03` [Arquitetura conceitual, lógica e física](docs/modules/02-security-architecture/03-conceptual-logical-physical.md) — Professional, 75 min — Published
- `M02-L04` [Princípios, padrões, baselines e exceções](docs/modules/02-security-architecture/04-principles-standards-baselines-exceptions.md) — Professional, 75 min — Published
- `M02-L05` [Arquiteturas de referência e blueprints](docs/modules/02-security-architecture/05-reference-architectures-blueprints.md) — Professional, 60 min — Published
- `M02-L06` [Frameworks, padrões e certificações: NIST, SABSA, TOGAF, CISSP e ISSAP](docs/modules/02-security-architecture/06-frameworks.md) — Professional, 90 min — Published
- `M02-L07` [Business-driven Security Architecture: de requisitos de negócio a requisitos de segurança](docs/modules/02-security-architecture/07-business-driven-requirements.md) — Architect, 90 min — Published
- `M02-L08` [Architecture Decision Records](docs/modules/02-security-architecture/08-architecture-decision-records.md) — Architect, 75 min — Published

### M03 — Governança, Riscos e Controles

Status: **Planned** · Fase 2 · Pré-requisitos: M02

- `M03-L01` Governança de segurança e o NIST CSF 2.0 — Fundamental, 75 min — Planned
- `M03-L02` NIST Risk Management Framework (SP 800-37) — Professional, 75 min — Planned
- `M03-L03` Seleção e tailoring de controles: SP 800-53 e CIS Controls — Professional, 90 min — Planned
- `M03-L04` ISO/IEC 27001/27002, LGPD e PCI DSS: propósito e escopo — Fundamental, 75 min — Planned
- `M03-L05` Business Impact Analysis, RTO e RPO — Professional, 60 min — Planned
- `M03-L06` Risk assessment, risk register e tratamento de riscos — Professional, 90 min — Planned
- `M03-L07` Catálogo de controles e arquitetura baseada em risco — Architect, 75 min — Planned
- `M03-L08` Indicadores, maturidade e reporte à governança — Architect, 60 min — Planned

### M04 — Métodos de Design e Threat Modeling

Status: **Planned** · Fase 3 · Pré-requisitos: M02

- `M04-L01` Data Flow Diagrams e fluxos de confiança — Fundamental, 60 min — Planned
- `M04-L02` STRIDE aplicado à arquitetura — Professional, 75 min — Planned
- `M04-L03` Attack trees e abuse cases — Professional, 60 min — Planned
- `M04-L04` MITRE ATT&CK para cenários de ataque — Professional, 75 min — Planned
- `M04-L05` Pontos únicos de falha e análise de dependências — Professional, 60 min — Planned
- `M04-L06` De ameaças a requisitos de segurança — Architect, 75 min — Planned
- `M04-L07` Revisão arquitetural, As-Is/To-Be e validação de controles — Architect, 75 min — Planned

## Nível 2 — Arquiteturas de Infraestrutura

Rede, identidade, Zero Trust e ambientes on-premises e legados.

### M05 — Network Security Architecture

Status: **Planned** · Fase 3 · Pré-requisitos: M00, M02

- `M05-L01` Zonas de confiança, segmentação e microsegmentação — Fundamental, 75 min — Planned
- `M05-L02` Perímetro e inspeção: DMZ, WAF, NGFW, IDS/IPS e proxies — Professional, 75 min — Planned
- `M05-L03` Tráfego North-South e East-West — Professional, 60 min — Planned
- `M05-L04` Acesso remoto: VPN, ZTNA e bastion hosts — Professional, 75 min — Planned
- `M05-L05` SD-WAN, SASE e SSE — Professional, 60 min — Planned
- `M05-L06` Network Access Control — Professional, 45 min — Planned
- `M05-L07` Desenho de uma rede corporativa segura — Architect, 90 min — Planned

### M06 — Identity & Access Management

Status: **Planned** · Fase 2 · Pré-requisitos: M01, M02

- `M06-L01` Disciplinas de identidade: IAM, IGA, PAM e PIM — Fundamental, 60 min — Planned
- `M06-L02` Modelos de autorização: RBAC, ABAC e acesso contextual — Professional, 75 min — Planned
- `M06-L03` Diretórios e autenticação corporativa: Active Directory, LDAP e Kerberos — Professional, 90 min — Planned
- `M06-L04` Federação: SAML 2.0, OAuth 2.0 e OpenID Connect — Professional, 90 min — Planned
- `M06-L05` Identidade híbrida: Active Directory, Microsoft Entra ID e provedores cloud — Architect, 90 min — Planned
- `M06-L06` Contas privilegiadas e identidades de máquina — Professional, 75 min — Planned
- `M06-L07` Workload Identity Federation — Architect, 60 min — Planned
- `M06-L08` Ciclo de vida de identidades e segregação de funções — Professional, 60 min — Planned
- `M06-L09` Recuperação de identidade em incidentes — Architect, 75 min — Planned

### M07 — Zero Trust Architecture

Status: **Planned** · Fase 2 · Pré-requisitos: M05, M06

- `M07-L01` Fundamentos de Zero Trust e o NIST SP 800-207 — Fundamental, 75 min — Planned
- `M07-L02` Componentes lógicos: Policy Engine, Policy Administrator e PEP — Professional, 60 min — Planned
- `M07-L03` Abordagens identity-centric, resource-centric e de rede — Professional, 60 min — Planned
- `M07-L04` Verificação contínua, postura de dispositivo e acesso adaptativo — Professional, 75 min — Planned
- `M07-L05` Segmentação e proteção de workloads — Professional, 60 min — Planned
- `M07-L06` CISA Zero Trust Maturity Model — Architect, 60 min — Planned
- `M07-L07` Implantação progressiva com sistemas legados e restrições — Architect, 90 min — Planned

### M08 — On-Premises e Sistemas Legados

Status: **Planned** · Fase 3 · Pré-requisitos: M05, M06

- `M08-L01` Segurança de datacenters — Fundamental, 60 min — Planned
- `M08-L02` Hardening e baselines de configuração — Professional, 75 min — Planned
- `M08-L03` Arquitetura para Windows Server, Linux e Active Directory — Professional, 90 min — Planned
- `M08-L04` Backup, recuperação e resiliência contra ransomware — Professional, 75 min — Planned
- `M08-L05` Sistemas sem suporte e controles compensatórios — Architect, 60 min — Planned
- `M08-L06` Protocolos inseguros e dependências legadas — Professional, 60 min — Planned
- `M08-L07` Integração com ambientes modernos e modernização gradual — Architect, 75 min — Planned

## Nível 3 — Arquitetura Cloud e Híbrida

AWS, Azure, Google Cloud e a integração segura entre ambientes.

### M09 — AWS Security Architecture

Status: **Planned** · Fase 3 · Pré-requisitos: M05, M06

- `M09-L01` Security Pillar do Well-Architected e responsabilidade compartilhada — Fundamental, 60 min — Planned
- `M09-L02` AWS Organizations, multi-account, landing zones e Control Tower — Professional, 90 min — Planned
- `M09-L03` IAM e IAM Identity Center — Professional, 90 min — Planned
- `M09-L04` Rede: VPC, Security Groups, NACLs, roteamento e endpoints — Professional, 75 min — Planned
- `M09-L05` Dados e segredos: AWS KMS e Secrets Manager — Professional, 60 min — Planned
- `M09-L06` Detecção e governança: CloudTrail, Config, GuardDuty, Security Hub, Inspector e Macie — Professional, 90 min — Planned
- `M09-L07` AWS Security Reference Architecture e integração com on-premises — Architect, 90 min — Planned

### M10 — Azure e Google Cloud

Status: **Planned** · Fase 3 · Pré-requisitos: M05, M06

- `M10-L01` Azure Well-Architected, Cloud Adoption Framework e Azure Landing Zones — Professional, 75 min — Planned
- `M10-L02` Microsoft Entra ID e identidade híbrida — Professional, 75 min — Planned
- `M10-L03` Defender for Cloud, Azure Policy e Azure Arc — Professional, 75 min — Planned
- `M10-L04` Google Cloud: Architecture Framework e hierarquia de recursos — Professional, 60 min — Planned
- `M10-L05` Google Cloud IAM, Organization Policy e Security Command Center — Professional, 75 min — Planned
- `M10-L06` Equivalências e particularidades entre AWS, Azure e Google Cloud — Architect, 60 min — Planned
- `M10-L07` Mapeamento para o Microsoft SC-100 — Architect, 45 min — Planned

### M11 — Hybrid & Multicloud Security Architecture

Status: **Planned** · Fase 2 · Pré-requisitos: M06, M07

- `M11-L01` Conectividade híbrida: VPN site-to-site, AWS Direct Connect e Azure ExpressRoute — Professional, 90 min — Planned
- `M11-L02` Arquitetura de DNS híbrido — Professional, 60 min — Planned
- `M11-L03` Identidade e federação entre Active Directory e provedores cloud — Architect, 90 min — Planned
- `M11-L04` Logs, observabilidade, SIEM e SOC multiambiente — Professional, 75 min — Planned
- `M11-L05` Segredos, certificados, criptografia e chaves distribuídos — Professional, 75 min — Planned
- `M11-L06` Políticas consistentes e postura: CSPM, CNAPP, CWPP, CIEM e DSPM — Architect, 90 min — Planned
- `M11-L07` Asset discovery e inventário corporativo — Professional, 60 min — Planned
- `M11-L08` Backup, disaster recovery e continuidade em ambientes híbridos — Architect, 75 min — Planned
- `M11-L09` Comunicação segura entre workloads — Professional, 60 min — Planned
- `M11-L10` Responsabilidade compartilhada, soberania, latência e vendor lock-in — Architect, 75 min — Planned
- `M11-L11` Três modelos de referência híbridos: As-Is e To-Be — Architect, 120 min — Planned

## Nível 4 — Arquitetura de Segurança Aplicada

Aplicações, dados, gestão de vulnerabilidades e exposição, operações e resiliência.

### M12 — Application Security Architecture

Status: **Planned** · Fase 3 · Pré-requisitos: M04, M06

- `M12-L01` Secure SDLC e DevSecOps — Fundamental, 60 min — Planned
- `M12-L02` OWASP ASVS como especificação de requisitos — Professional, 60 min — Planned
- `M12-L03` Arquitetura de API Security — Professional, 75 min — Planned
- `M12-L04` Autenticação e autorização distribuídas — Professional, 75 min — Planned
- `M12-L05` API Gateway, service mesh e mTLS — Professional, 60 min — Planned
- `M12-L06` Segurança de microsserviços e containers — Professional, 75 min — Planned
- `M12-L07` CI/CD, IaC e software supply chain — Architect, 75 min — Planned
- `M12-L08` SAST, DAST, SCA, secrets scanning e SBOM na arquitetura — Professional, 60 min — Planned

### M13 — Data Security Architecture

Status: **Planned** · Fase 3 · Pré-requisitos: M01, M03

- `M13-L01` Classificação e ciclo de vida de dados — Fundamental, 60 min — Planned
- `M13-L02` Criptografia at rest, in transit e in use — Professional, 75 min — Planned
- `M13-L03` Tokenização, hashing e mascaramento — Professional, 60 min — Planned
- `M13-L04` KMS, HSM e rotação de chaves — Professional, 75 min — Planned
- `M13-L05` Data Loss Prevention e segurança de bancos de dados — Professional, 75 min — Planned
- `M13-L06` Governança de dados distribuídos, privacidade, retenção e LGPD — Architect, 75 min — Planned
- `M13-L07` Zero Trust aplicado a dados — Architect, 60 min — Planned

### M14 — Vulnerability & Exposure Management Architecture

Status: **Planned** · Fase 3 · Pré-requisitos: M03

- `M14-L01` Arquitetura de um programa corporativo de gestão de vulnerabilidades — Professional, 75 min — Planned
- `M14-L02` Descoberta e cobertura de ativos — Professional, 60 min — Planned
- `M14-L03` Cobertura por superfície: infraestrutura, web, APIs, cloud, AD e containers — Professional, 75 min — Planned
- `M14-L04` Vulnerability Management versus Exposure Management — Professional, 60 min — Planned
- `M14-L05` Priorização: CVSS, EPSS, CISA KEV e contexto de negócio — Architect, 75 min — Planned
- `M14-L06` Ownership, SLA, remediação e exceções — Professional, 60 min — Planned
- `M14-L07` Automação, integrações, KPIs, KRIs e dashboards — Professional, 60 min — Planned
- `M14-L08` Programa centralizado para múltiplas organizações — Architect, 75 min — Planned

### M15 — Security Operations & Resilience Architecture

Status: **Planned** · Fase 3 · Pré-requisitos: M05, M06

- `M15-L01` Arquitetura de logging e telemetria — Professional, 75 min — Planned
- `M15-L02` SIEM, SOAR, XDR e EDR — Professional, 75 min — Planned
- `M15-L03` Detecção em ambientes híbridos — Architect, 60 min — Planned
- `M15-L04` Incident response e gestão de crises — Professional, 75 min — Planned
- `M15-L05` Resiliência contra ransomware, backup imutável e disaster recovery — Architect, 75 min — Planned
- `M15-L06` Validação de controles e exercícios tabletop — Professional, 60 min — Planned
- `M15-L07` Segurança da cadeia de suprimentos — Architect, 60 min — Planned

## Nível 5 — Arquitetura Corporativa Avançada

Arquitetura corporativa, governança entre empresas e projeto final.

### M16 — Enterprise Security Architecture

Status: **Planned** · Fase 2 · Pré-requisitos: M03, M11

- `M16-L01` Arquitetura orientada ao negócio com SABSA — Architect, 90 min — Planned
- `M16-L02` SABSA e TOGAF integrados — Architect, 75 min — Planned
- `M16-L03` Modelos centralizado, federado e descentralizado — Architect, 60 min — Planned
- `M16-L04` Arquitetura corporativa de referência e shared security services — Architect, 75 min — Planned
- `M16-L05` Governança de segurança entre empresas de um grupo — Architect, 75 min — Planned
- `M16-L06` Architecture Review Boards, padrões, exceções e technical debt — Architect, 75 min — Planned
- `M16-L07` Gestão de stakeholders e negociação de riscos — Architect, 60 min — Planned
- `M16-L08` Estratégia, roadmaps, orçamento, TCO e priorização de investimentos — Architect, 90 min — Planned

### M17 — Estudos de Caso e Projeto Final

Status: **Planned** · Fase 3 · Pré-requisitos: M16

- `M17-L01` Avaliação de maturidade e levantamento de requisitos — Architect, 90 min — Planned
- `M17-L02` Arquitetura base, identificação de lacunas e seleção de controles — Architect, 120 min — Planned
- `M17-L03` Desenho da arquitetura híbrida e da governança de segurança — Architect, 120 min — Planned
- `M17-L04` Roadmap de 90 dias, 6 meses e 12 meses — Architect, 90 min — Planned
- `M17-L05` Apresentação executiva e documentação para engenharia — Architect, 90 min — Planned

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
- `AS-M00` [Avaliação do Módulo 00](docs/assessments/m00-foundations.md) — Published
- `AS-M01` [Avaliação do Módulo 01](docs/assessments/m01-security-fundamentals.md) — Published
- `AS-FUND` [Avaliação final de Fundamentals (integradora)](docs/assessments/fundamentals-final.md) — Published
- `AS-M02` [Avaliação do Módulo 02](docs/assessments/m02-security-architecture.md) — Published
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
