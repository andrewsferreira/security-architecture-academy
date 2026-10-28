---
title: Matriz de cobertura
description: Rastreabilidade entre os tópicos obrigatórios do currículo e as aulas planejadas ou produzidas, incluindo as distinções conceituais e os temas transversais.
---

# Matriz de cobertura

Esta matriz garante que **cada tópico obrigatório do currículo tenha uma aula responsável** e evita duplicações: quando um tema aparece em mais de um módulo, a matriz indica qual aula o aprofunda e quais apenas o aplicam.

!!! info "Estado da matriz"

    O estado de publicação de cada módulo está no [Curriculum Roadmap](index.md). Para módulos ainda não publicados, os IDs de aula são **planejados** e podem ser ajustados quando o módulo for produzido; qualquer ajuste atualiza esta matriz no mesmo Pull Request.

## Distinções conceituais obrigatórias

O currículo exige que algumas diferenças sejam ensinadas explicitamente. Cada uma tem uma aula principal e reforços posteriores.

| Distinção | Aula principal | Reforços |
|:---|:---|:---|
| Arquitetura × implementação | Módulo 2 — Aula 03 | Módulo 4 — Aula 07, Módulo 17 — Aula 05 |
| Estratégia × operação | Módulo 2 — Aula 01 | Módulo 16 — Aula 08 |
| Princípios × padrões × controles | Módulo 2 — Aula 04 | Módulo 3 — Aula 07, Módulo 16 — Aula 06 |
| Requisitos funcionais × não funcionais | Módulo 2 — Aula 07 | Módulo 4 — Aula 06, Módulo 12 — Aula 02 |
| Risco técnico × risco de negócio | Módulo 2 — Aula 07 | Módulo 3 — Aula 06, Módulo 14 — Aula 05, Módulo 16 — Aula 07 |
| Segurança necessária × complexidade desnecessária | Módulo 2 — Aulas 04 e 08 | Módulo 7 — Aula 07, Módulo 16 — Aula 06 |
| Controles preventivos, detectivos, corretivos e compensatórios | Módulo 1 — Aula 06 | Módulo 2 — Aula 04, Módulo 3 — Aula 07, Módulo 8 — Aula 05 |
| Conformidade normativa × segurança efetiva | Módulo 2 — Aula 06 | Módulo 3 — Aula 04, Módulo 16 — Aula 05 |

## Tópicos por módulo

### Nível 0 e Nível 1

| Módulo | Tópico obrigatório | Aula |
|:---|:---|:---|
| Módulo Inicial | Hardware, sistemas operacionais, virtualização e hipervisores | Módulo Inicial — Aula 01 |
| Módulo Inicial | TCP/IP, OSI, DNS, DHCP e NAT | Módulo Inicial — Aula 02 |
| Módulo Inicial | VLAN, routing, VPN, TLS e firewalls | Módulo Inicial — Aula 03 |
| Módulo Inicial | Datacenters, clusters, armazenamento e alta disponibilidade | Módulo Inicial — Aula 04 |
| Módulo Inicial | Containers, Kubernetes, APIs, microsserviços e serverless | Módulo Inicial — Aula 05 |
| Módulo Inicial | IaaS, PaaS, SaaS; public, private e hybrid cloud | Módulo Inicial — Aula 06 |
| Módulo Inicial | Identificar componentes e fluxos em diagramas | Módulo Inicial — Aula 07 |
| Módulo 1 | CIA, autenticidade, autorização e não repúdio | Módulo 1 — Aula 01 |
| Módulo 1 | Defense in Depth, Least Privilege, Secure by Design/Default, Fail Secure, Separation of Duties | Módulo 1 — Aula 02 |
| Módulo 1 | Trust Boundaries, Attack Surface e Shared Responsibility | Módulo 1 — Aula 03 |
| Módulo 1 | Criptografia, PKI, TLS, certificados, assinaturas e chaves | Módulo 1 — Aulas 04 e 05 |
| Módulo 1 | Threat, vulnerability, risk, exposure e control | Módulo 1 — Aula 06 |
| Módulo 1 | Bell-LaPadula, Biba e modelos formais | Módulo 1 — Aula 07 |
| Módulo 2 | O que faz um Security Architect | Módulo 2 — Aula 01 |
| Módulo 2 | Enterprise × Solution × Security Architecture | Módulo 2 — Aula 02 |
| Módulo 2 | Arquitetura conceitual, lógica e física | Módulo 2 — Aula 03 |
| Módulo 2 | Arquiteturas de referência e blueprints | Módulo 2 — Aula 05 |
| Módulo 2 | Baselines, padrões, princípios e exceções | Módulo 2 — Aula 04 |
| Módulo 2 | NIST, SABSA, TOGAF, CISSP e ISSAP | Módulo 2 — Aula 06 |
| Módulo 2 | Business-driven Security Architecture | Módulo 2 — Aula 07 |
| Módulo 2 | Requisitos de negócio → requisitos de segurança | Módulo 2 — Aula 07 |
| Módulo 2 | Architecture Decision Records | Módulo 2 — Aula 08 |
| Módulo 3 | NIST CSF 2.0 e suas seis funções | Módulo 3 — Aula 01 |
| Módulo 3 | NIST RMF | Módulo 3 — Aula 02 |
| Módulo 3 | SP 800-53, seleção de controles e CIS Controls | Módulo 3 — Aula 03 |
| Módulo 3 | ISO 27001/27002, LGPD e PCI DSS (conceitual) | Módulo 3 — Aula 04 |
| Módulo 3 | BIA, RTO e RPO | Módulo 3 — Aula 05 |
| Módulo 3 | Risk Assessment, Risk Register e Risk Treatment | Módulo 3 — Aula 06 |
| Módulo 3 | Security Control Catalogue e Risk-based Security Architecture | Módulo 3 — Aula 07 |
| Módulo 3 | Indicadores, maturidade e governança | Módulo 3 — Aula 08 |
| Módulo 4 | DFD e modelagem de fluxos de confiança | Módulo 4 — Aula 01 |
| Módulo 4 | STRIDE | Módulo 4 — Aula 02 |
| Módulo 4 | Attack trees e abuse cases | Módulo 4 — Aula 03 |
| Módulo 4 | MITRE ATT&CK | Módulo 4 — Aula 04 |
| Módulo 4 | Pontos únicos de falha | Módulo 4 — Aula 05 |
| Módulo 4 | Requisitos derivados de ameaças | Módulo 4 — Aula 06 |
| Módulo 4 | Revisão arquitetural, validação de controles, As-Is e To-Be | Módulo 4 — Aula 07 |

### Nível 2 e Nível 3

| Módulo | Tópico obrigatório | Aula |
|:---|:---|:---|
| Módulo 5 | Segmentação e microsegmentação; zonas de confiança | Módulo 5 — Aula 01 |
| Módulo 5 | DMZ, WAF, NGFW, IDS/IPS e proxies | Módulo 5 — Aula 02 |
| Módulo 5 | North-South e East-West | Módulo 5 — Aula 03 |
| Módulo 5 | Remote Access, VPN, ZTNA e bastion hosts | Módulo 5 — Aula 04 |
| Módulo 5 | SD-WAN, SASE e SSE | Módulo 5 — Aula 05 |
| Módulo 5 | Network Access Control | Módulo 5 — Aula 06 |
| Módulo 5 | Desenho de redes corporativas seguras | Módulo 5 — Aula 07 |
| Módulo 6 | IAM, PAM, PIM e IGA | Módulo 6 — Aula 01 |
| Módulo 6 | RBAC, ABAC e autenticação contextual | Módulo 6 — Aula 02 |
| Módulo 6 | Active Directory, LDAP e Kerberos | Módulo 6 — Aula 03 |
| Módulo 6 | SAML, OAuth 2.0 e OpenID Connect | Módulo 6 — Aula 04 |
| Módulo 6 | Federação cloud/on-premises e Microsoft Entra ID | Módulo 6 — Aula 05 |
| Módulo 6 | Contas privilegiadas e machine identities | Módulo 6 — Aula 06 |
| Módulo 6 | Workload Identity Federation | Módulo 6 — Aula 07 |
| Módulo 6 | Segregação de funções e ciclo de vida | Módulo 6 — Aula 08 |
| Módulo 6 | Identidade híbrida e recuperação em incidentes | Módulo 6 — Aulas 05 e 09 |
| Módulo 7 | NIST SP 800-207 | Módulo 7 — Aula 01 |
| Módulo 7 | Policy Engine, Policy Administrator e PEP | Módulo 7 — Aula 02 |
| Módulo 7 | Identity-centric e resource-centric | Módulo 7 — Aula 03 |
| Módulo 7 | Continuous Verification, device posture e adaptive access | Módulo 7 — Aula 04 |
| Módulo 7 | Segmentação e proteção de workloads | Módulo 7 — Aula 05 |
| Módulo 7 | CISA Zero Trust Maturity Model | Módulo 7 — Aula 06 |
| Módulo 7 | Implantação progressiva, legados e restrições | Módulo 7 — Aula 07 |
| Módulo 8 | Segurança de datacenters | Módulo 8 — Aula 01 |
| Módulo 8 | Hardening e configurações de referência | Módulo 8 — Aula 02 |
| Módulo 8 | Windows Server, Linux e Active Directory | Módulo 8 — Aula 03 |
| Módulo 8 | Backup, recuperação e resiliência a ransomware | Módulo 8 — Aula 04 |
| Módulo 8 | Sistemas sem suporte e controles compensatórios | Módulo 8 — Aula 05 |
| Módulo 8 | Dependências legadas e protocolos inseguros | Módulo 8 — Aula 06 |
| Módulo 8 | Integração e modernização gradual | Módulo 8 — Aula 07 |
| Módulo 9 | Well-Architected Security Pillar | Módulo 9 — Aula 01 |
| Módulo 9 | Organizations, multi-account, Landing Zones e Control Tower | Módulo 9 — Aula 02 |
| Módulo 9 | IAM e IAM Identity Center | Módulo 9 — Aula 03 |
| Módulo 9 | VPC, Security Groups, NACLs, routing e endpoints | Módulo 9 — Aula 04 |
| Módulo 9 | KMS, Secrets Manager | Módulo 9 — Aula 05 |
| Módulo 9 | CloudTrail, Config, GuardDuty, Security Hub, Inspector e Macie | Módulo 9 — Aula 06 |
| Módulo 9 | Arquiteturas de referência, híbrido AWS/on-premises, governança | Módulo 9 — Aula 07 |
| Módulo 10 | Azure Well-Architected, CAF e Landing Zones | Módulo 10 — Aula 01 |
| Módulo 10 | Microsoft Entra ID e integração híbrida | Módulo 10 — Aula 02 |
| Módulo 10 | Defender for Cloud, Azure Policy e Azure Arc | Módulo 10 — Aula 03 |
| Módulo 10 | Google Cloud Architecture Framework | Módulo 10 — Aula 04 |
| Módulo 10 | Google Cloud IAM, Organization Policy e Security Command Center | Módulo 10 — Aula 05 |
| Módulo 10 | Equivalências entre provedores | Módulo 10 — Aula 06 |
| Módulo 10 | Microsoft SC-100 | Módulo 10 — Aula 07 |
| Módulo 11 | Integração datacenter/cloud; VPN, Direct Connect e ExpressRoute | Módulo 11 — Aula 01 |
| Módulo 11 | DNS híbrido | Módulo 11 — Aula 02 |
| Módulo 11 | Integração AD/provedores cloud e federação | Módulo 11 — Aula 03 |
| Módulo 11 | Logs, observabilidade, SIEM e SOC multiambiente | Módulo 11 — Aula 04 |
| Módulo 11 | Segredos, certificados, criptografia e chaves | Módulo 11 — Aula 05 |
| Módulo 11 | Políticas consistentes; CSPM, CNAPP, CWPP, CIEM e DSPM | Módulo 11 — Aula 06 |
| Módulo 11 | Asset discovery e inventário | Módulo 11 — Aula 07 |
| Módulo 11 | Backup, DR e continuidade | Módulo 11 — Aula 08 |
| Módulo 11 | Comunicação segura entre workloads | Módulo 11 — Aula 09 |
| Módulo 11 | Responsabilidade compartilhada, latência, soberania, disponibilidade e lock-in | Módulo 11 — Aula 10 |
| Módulo 11 | Três modelos As-Is/To-Be obrigatórios | Módulo 11 — Aula 11 |

### Nível 4 e Nível 5

| Módulo | Tópico obrigatório | Aula |
|:---|:---|:---|
| Módulo 12 | Secure SDLC e DevSecOps | Módulo 12 — Aula 01 |
| Módulo 12 | OWASP ASVS | Módulo 12 — Aula 02 |
| Módulo 12 | API Security | Módulo 12 — Aula 03 |
| Módulo 12 | Autenticação e autorização distribuídas | Módulo 12 — Aula 04 |
| Módulo 12 | API Gateway, Service Mesh e mTLS | Módulo 12 — Aula 05 |
| Módulo 12 | Microsserviços e containers | Módulo 12 — Aula 06 |
| Módulo 12 | CI/CD, IaC e software supply chain | Módulo 12 — Aula 07 |
| Módulo 12 | SAST, DAST, SCA, secrets scanning e SBOM | Módulo 12 — Aula 08 |
| Módulo 12 | Threat modeling de aplicações | Módulo 12 — Aula 03, Módulo 4 — Aula 02 |
| Módulo 13 | Classificação e ciclo de vida | Módulo 13 — Aula 01 |
| Módulo 13 | Encryption at Rest, in Transit e in Use | Módulo 13 — Aula 02 |
| Módulo 13 | Tokenização, hashing e mascaramento | Módulo 13 — Aula 03 |
| Módulo 13 | KMS, HSM e rotação de chaves | Módulo 13 — Aula 04 |
| Módulo 13 | DLP e segurança de bancos de dados | Módulo 13 — Aula 05 |
| Módulo 13 | Governança, privacidade, retenção e LGPD | Módulo 13 — Aula 06 |
| Módulo 13 | Zero Trust Data Security | Módulo 13 — Aula 07 |
| Módulo 14 | Arquitetura de programa corporativo de VM | Módulo 14 — Aula 01 |
| Módulo 14 | Descoberta e cobertura de ativos | Módulo 14 — Aula 02 |
| Módulo 14 | Infraestrutura, Web, APIs, Cloud, AD e containers | Módulo 14 — Aula 03 |
| Módulo 14 | Vulnerability × Exposure Management | Módulo 14 — Aula 04 |
| Módulo 14 | CVSS, EPSS, CISA KEV e contexto de negócio | Módulo 14 — Aula 05 |
| Módulo 14 | Ownership, SLA, remediação e exceções | Módulo 14 — Aula 06 |
| Módulo 14 | Automação, integrações, KRIs, KPIs e dashboards | Módulo 14 — Aula 07 |
| Módulo 14 | Programa para múltiplas organizações | Módulo 14 — Aula 08 |
| Módulo 15 | Logging e telemetria | Módulo 15 — Aula 01 |
| Módulo 15 | SIEM, SOAR, XDR e EDR | Módulo 15 — Aula 02 |
| Módulo 15 | Integração de ambientes híbridos | Módulo 15 — Aula 03 |
| Módulo 15 | Incident Response e Crisis Management | Módulo 15 — Aula 04 |
| Módulo 15 | Ransomware, alta disponibilidade, backup imutável e DR | Módulo 15 — Aula 05 |
| Módulo 15 | Validação de controles e tabletop | Módulo 15 — Aula 06 |
| Módulo 15 | Cadeia de suprimentos | Módulo 15 — Aula 07 |
| Módulo 16 | Arquitetura orientada ao negócio; SABSA | Módulo 16 — Aula 01 |
| Módulo 16 | SABSA e TOGAF | Módulo 16 — Aula 02 |
| Módulo 16 | Modelos centralizado, federado e descentralizado | Módulo 16 — Aula 03 |
| Módulo 16 | Arquitetura de referência e Shared Security Services | Módulo 16 — Aula 04 |
| Módulo 16 | Governança entre empresas; controles universais e adaptações | Módulo 16 — Aula 05 |
| Módulo 16 | Architecture Review Boards, padrões, exceções e technical debt | Módulo 16 — Aula 06 |
| Módulo 16 | Stakeholders e negociação de riscos | Módulo 16 — Aula 07 |
| Módulo 16 | Estratégia, roadmaps, orçamento, TCO e priorização | Módulo 16 — Aula 08 |
| Módulo 17 | Maturidade e requisitos corporativos | Módulo 17 — Aula 01 |
| Módulo 17 | Arquitetura base, lacunas e controles | Módulo 17 — Aula 02 |
| Módulo 17 | Arquitetura híbrida e governança | Módulo 17 — Aula 03 |
| Módulo 17 | Roadmap de 90 dias, 6 e 12 meses | Módulo 17 — Aula 04 |
| Módulo 17 | Apresentação executiva e arquitetura detalhada | Módulo 17 — Aula 05 |
| C01 | Segurança de IA/LLM, identidades não humanas e riscos emergentes | C01-L01 a C01-L04 |

## Temas transversais

### Ambientes híbridos

A diretriz de qualidade determina que o tema híbrido não se limite ao Módulo 11. Toda aula aplicável tem a seção **Aplicabilidade: on-premises, cloud e híbrido**, com cenário de cada ambiente, dependências de conectividade e identidade, responsabilidades, riscos e trade-offs.

| Onde o híbrido é aprofundado | Foco |
|:---|:---|
| Módulo 2 (todas as aulas) | Como o raciocínio arquitetural muda entre ambientes |
| Módulo 6 — Aulas 05 e 07 | Identidade híbrida e federação de workloads |
| Módulo 7 — Aula 07 | Zero Trust com legados |
| Módulo 8 — Aula 07 | Integração do legado com ambientes modernos |
| Módulo 9 — Aula 07, Módulo 10 — Aula 02, Módulo 10 — Aula 03 | Integração específica de cada provedor |
| Módulo 11 (módulo inteiro) | Arquitetura híbrida e multicloud |
| Módulo 15 — Aula 03 | Detecção multiambiente |
| Módulo 16 — Aulas 04 e 05 | Serviços compartilhados e governança entre ambientes |

### Decisões arquiteturais

Cada módulo tem ao menos um **exercício de tomada de decisão** com matriz de alternativas; ADRs são introduzidos no Módulo 2 — Aula 08 e exigidos nos estudos de caso, laboratórios de desenho e no projeto final.

## Estudos de caso, laboratórios e artefatos

| Exigência do currículo | Entrega | Status |
|:---|:---|:---|
| Caso A — Datacenter tradicional | CS-A | <span class="saa-status saa-status--published">Published</span> |
| Caso B — Migração para AWS | CS-B | <span class="saa-status saa-status--planned">Planned</span> |
| Caso C — Arquitetura híbrida | CS-C | <span class="saa-status saa-status--planned">Planned</span> |
| Caso D — Grupo empresarial | CS-D | <span class="saa-status saa-status--planned">Planned</span> |
| Caso E — Programa de Vulnerability Management | CS-E | <span class="saa-status saa-status--planned">Planned</span> |
| Laboratório de desenho arquitetural | LAB-02 | <span class="saa-status saa-status--published">Published</span> |
| 13 modelos de artefatos | 3 produzidos, 10 planejados | ver [Modelos](../artifacts/index.md) |
| Avaliações diagnóstica, intermediária, final e avançada em inglês | 2 produzidas, 3 planejadas | ver [Avaliações](../assessments/index.md) |
