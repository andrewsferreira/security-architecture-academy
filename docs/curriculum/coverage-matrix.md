---
title: Matriz de cobertura
description: Rastreabilidade entre os tópicos obrigatórios do currículo e as aulas planejadas ou produzidas, incluindo as distinções conceituais e os temas transversais.
---

# Matriz de cobertura

Esta matriz garante que **cada tópico obrigatório do currículo tenha uma aula responsável** e evita duplicações: quando um tema aparece em mais de um módulo, a matriz indica qual aula o aprofunda e quais apenas o aplicam.

!!! info "Estado da matriz"

    As aulas do **M02** estão produzidas (<span class="saa-status saa-status--published">Published</span>). Para os demais módulos, os IDs de aula são **planejados** e podem ser ajustados quando o módulo for produzido; qualquer ajuste atualiza esta matriz no mesmo Pull Request.

## Distinções conceituais obrigatórias

O currículo exige que algumas diferenças sejam ensinadas explicitamente. Cada uma tem uma aula principal e reforços posteriores.

| Distinção | Aula principal | Reforços |
|:---|:---|:---|
| Arquitetura × implementação | M02-L03 | M04-L07, M17-L05 |
| Estratégia × operação | M02-L01 | M16-L08 |
| Princípios × padrões × controles | M02-L04 | M03-L07, M16-L06 |
| Requisitos funcionais × não funcionais | M02-L07 | M04-L06, M12-L02 |
| Risco técnico × risco de negócio | M02-L07 | M03-L06, M14-L05, M16-L07 |
| Segurança necessária × complexidade desnecessária | M02-L04, M02-L08 | M07-L07, M16-L06 |
| Controles preventivos, detectivos, corretivos e compensatórios | M01-L06 | M02-L04, M03-L07, M08-L05 |
| Conformidade normativa × segurança efetiva | M02-L06 | M03-L04, M16-L05 |

## Tópicos por módulo

### Nível 0 e Nível 1

| Módulo | Tópico obrigatório | Aula |
|:---|:---|:---|
| M00 | Hardware, sistemas operacionais, virtualização e hipervisores | M00-L01 |
| M00 | TCP/IP, OSI, DNS, DHCP e NAT | M00-L02 |
| M00 | VLAN, routing, VPN, TLS e firewalls | M00-L03 |
| M00 | Datacenters, clusters, armazenamento e alta disponibilidade | M00-L04 |
| M00 | Containers, Kubernetes, APIs, microsserviços e serverless | M00-L05 |
| M00 | IaaS, PaaS, SaaS; public, private e hybrid cloud | M00-L06 |
| M00 | Identificar componentes e fluxos em diagramas | M00-L07 |
| M01 | CIA, autenticidade, autorização e não repúdio | M01-L01 |
| M01 | Defense in Depth, Least Privilege, Secure by Design/Default, Fail Secure, Separation of Duties | M01-L02 |
| M01 | Trust Boundaries, Attack Surface e Shared Responsibility | M01-L03 |
| M01 | Criptografia, PKI, TLS, certificados, assinaturas e chaves | M01-L04, M01-L05 |
| M01 | Threat, vulnerability, risk, exposure e control | M01-L06 |
| M01 | Bell-LaPadula, Biba e modelos formais | M01-L07 |
| M02 | O que faz um Security Architect | M02-L01 |
| M02 | Enterprise × Solution × Security Architecture | M02-L02 |
| M02 | Arquitetura conceitual, lógica e física | M02-L03 |
| M02 | Arquiteturas de referência e blueprints | M02-L05 |
| M02 | Baselines, padrões, princípios e exceções | M02-L04 |
| M02 | NIST, SABSA, TOGAF, CISSP e ISSAP | M02-L06 |
| M02 | Business-driven Security Architecture | M02-L07 |
| M02 | Requisitos de negócio → requisitos de segurança | M02-L07 |
| M02 | Architecture Decision Records | M02-L08 |
| M03 | NIST CSF 2.0 e suas seis funções | M03-L01 |
| M03 | NIST RMF | M03-L02 |
| M03 | SP 800-53, seleção de controles e CIS Controls | M03-L03 |
| M03 | ISO 27001/27002, LGPD e PCI DSS (conceitual) | M03-L04 |
| M03 | BIA, RTO e RPO | M03-L05 |
| M03 | Risk Assessment, Risk Register e Risk Treatment | M03-L06 |
| M03 | Security Control Catalogue e Risk-based Security Architecture | M03-L07 |
| M03 | Indicadores, maturidade e governança | M03-L08 |
| M04 | DFD e modelagem de fluxos de confiança | M04-L01 |
| M04 | STRIDE | M04-L02 |
| M04 | Attack trees e abuse cases | M04-L03 |
| M04 | MITRE ATT&CK | M04-L04 |
| M04 | Pontos únicos de falha | M04-L05 |
| M04 | Requisitos derivados de ameaças | M04-L06 |
| M04 | Revisão arquitetural, validação de controles, As-Is e To-Be | M04-L07 |

### Nível 2 e Nível 3

| Módulo | Tópico obrigatório | Aula |
|:---|:---|:---|
| M05 | Segmentação e microsegmentação; zonas de confiança | M05-L01 |
| M05 | DMZ, WAF, NGFW, IDS/IPS e proxies | M05-L02 |
| M05 | North-South e East-West | M05-L03 |
| M05 | Remote Access, VPN, ZTNA e bastion hosts | M05-L04 |
| M05 | SD-WAN, SASE e SSE | M05-L05 |
| M05 | Network Access Control | M05-L06 |
| M05 | Desenho de redes corporativas seguras | M05-L07 |
| M06 | IAM, PAM, PIM e IGA | M06-L01 |
| M06 | RBAC, ABAC e autenticação contextual | M06-L02 |
| M06 | Active Directory, LDAP e Kerberos | M06-L03 |
| M06 | SAML, OAuth 2.0 e OpenID Connect | M06-L04 |
| M06 | Federação cloud/on-premises e Microsoft Entra ID | M06-L05 |
| M06 | Contas privilegiadas e machine identities | M06-L06 |
| M06 | Workload Identity Federation | M06-L07 |
| M06 | Segregação de funções e ciclo de vida | M06-L08 |
| M06 | Identidade híbrida e recuperação em incidentes | M06-L05, M06-L09 |
| M07 | NIST SP 800-207 | M07-L01 |
| M07 | Policy Engine, Policy Administrator e PEP | M07-L02 |
| M07 | Identity-centric e resource-centric | M07-L03 |
| M07 | Continuous Verification, device posture e adaptive access | M07-L04 |
| M07 | Segmentação e proteção de workloads | M07-L05 |
| M07 | CISA Zero Trust Maturity Model | M07-L06 |
| M07 | Implantação progressiva, legados e restrições | M07-L07 |
| M08 | Segurança de datacenters | M08-L01 |
| M08 | Hardening e configurações de referência | M08-L02 |
| M08 | Windows Server, Linux e Active Directory | M08-L03 |
| M08 | Backup, recuperação e resiliência a ransomware | M08-L04 |
| M08 | Sistemas sem suporte e controles compensatórios | M08-L05 |
| M08 | Dependências legadas e protocolos inseguros | M08-L06 |
| M08 | Integração e modernização gradual | M08-L07 |
| M09 | Well-Architected Security Pillar | M09-L01 |
| M09 | Organizations, multi-account, Landing Zones e Control Tower | M09-L02 |
| M09 | IAM e IAM Identity Center | M09-L03 |
| M09 | VPC, Security Groups, NACLs, routing e endpoints | M09-L04 |
| M09 | KMS, Secrets Manager | M09-L05 |
| M09 | CloudTrail, Config, GuardDuty, Security Hub, Inspector e Macie | M09-L06 |
| M09 | Arquiteturas de referência, híbrido AWS/on-premises, governança | M09-L07 |
| M10 | Azure Well-Architected, CAF e Landing Zones | M10-L01 |
| M10 | Microsoft Entra ID e integração híbrida | M10-L02 |
| M10 | Defender for Cloud, Azure Policy e Azure Arc | M10-L03 |
| M10 | Google Cloud Architecture Framework | M10-L04 |
| M10 | Google Cloud IAM, Organization Policy e Security Command Center | M10-L05 |
| M10 | Equivalências entre provedores | M10-L06 |
| M10 | Microsoft SC-100 | M10-L07 |
| M11 | Integração datacenter/cloud; VPN, Direct Connect e ExpressRoute | M11-L01 |
| M11 | DNS híbrido | M11-L02 |
| M11 | Integração AD/provedores cloud e federação | M11-L03 |
| M11 | Logs, observabilidade, SIEM e SOC multiambiente | M11-L04 |
| M11 | Segredos, certificados, criptografia e chaves | M11-L05 |
| M11 | Políticas consistentes; CSPM, CNAPP, CWPP, CIEM e DSPM | M11-L06 |
| M11 | Asset discovery e inventário | M11-L07 |
| M11 | Backup, DR e continuidade | M11-L08 |
| M11 | Comunicação segura entre workloads | M11-L09 |
| M11 | Responsabilidade compartilhada, latência, soberania, disponibilidade e lock-in | M11-L10 |
| M11 | Três modelos As-Is/To-Be obrigatórios | M11-L11 |

### Nível 4 e Nível 5

| Módulo | Tópico obrigatório | Aula |
|:---|:---|:---|
| M12 | Secure SDLC e DevSecOps | M12-L01 |
| M12 | OWASP ASVS | M12-L02 |
| M12 | API Security | M12-L03 |
| M12 | Autenticação e autorização distribuídas | M12-L04 |
| M12 | API Gateway, Service Mesh e mTLS | M12-L05 |
| M12 | Microsserviços e containers | M12-L06 |
| M12 | CI/CD, IaC e software supply chain | M12-L07 |
| M12 | SAST, DAST, SCA, secrets scanning e SBOM | M12-L08 |
| M12 | Threat modeling de aplicações | M12-L03, M04-L02 |
| M13 | Classificação e ciclo de vida | M13-L01 |
| M13 | Encryption at Rest, in Transit e in Use | M13-L02 |
| M13 | Tokenização, hashing e mascaramento | M13-L03 |
| M13 | KMS, HSM e rotação de chaves | M13-L04 |
| M13 | DLP e segurança de bancos de dados | M13-L05 |
| M13 | Governança, privacidade, retenção e LGPD | M13-L06 |
| M13 | Zero Trust Data Security | M13-L07 |
| M14 | Arquitetura de programa corporativo de VM | M14-L01 |
| M14 | Descoberta e cobertura de ativos | M14-L02 |
| M14 | Infraestrutura, Web, APIs, Cloud, AD e containers | M14-L03 |
| M14 | Vulnerability × Exposure Management | M14-L04 |
| M14 | CVSS, EPSS, CISA KEV e contexto de negócio | M14-L05 |
| M14 | Ownership, SLA, remediação e exceções | M14-L06 |
| M14 | Automação, integrações, KRIs, KPIs e dashboards | M14-L07 |
| M14 | Programa para múltiplas organizações | M14-L08 |
| M15 | Logging e telemetria | M15-L01 |
| M15 | SIEM, SOAR, XDR e EDR | M15-L02 |
| M15 | Integração de ambientes híbridos | M15-L03 |
| M15 | Incident Response e Crisis Management | M15-L04 |
| M15 | Ransomware, alta disponibilidade, backup imutável e DR | M15-L05 |
| M15 | Validação de controles e tabletop | M15-L06 |
| M15 | Cadeia de suprimentos | M15-L07 |
| M16 | Arquitetura orientada ao negócio; SABSA | M16-L01 |
| M16 | SABSA e TOGAF | M16-L02 |
| M16 | Modelos centralizado, federado e descentralizado | M16-L03 |
| M16 | Arquitetura de referência e Shared Security Services | M16-L04 |
| M16 | Governança entre empresas; controles universais e adaptações | M16-L05 |
| M16 | Architecture Review Boards, padrões, exceções e technical debt | M16-L06 |
| M16 | Stakeholders e negociação de riscos | M16-L07 |
| M16 | Estratégia, roadmaps, orçamento, TCO e priorização | M16-L08 |
| M17 | Maturidade e requisitos corporativos | M17-L01 |
| M17 | Arquitetura base, lacunas e controles | M17-L02 |
| M17 | Arquitetura híbrida e governança | M17-L03 |
| M17 | Roadmap de 90 dias, 6 e 12 meses | M17-L04 |
| M17 | Apresentação executiva e arquitetura detalhada | M17-L05 |
| C01 | Segurança de IA/LLM, identidades não humanas e riscos emergentes | C01-L01 a C01-L04 |

## Temas transversais

### Ambientes híbridos

A diretriz de qualidade determina que o tema híbrido não se limite ao M11. Toda aula aplicável tem a seção **Aplicabilidade: on-premises, cloud e híbrido**, com cenário de cada ambiente, dependências de conectividade e identidade, responsabilidades, riscos e trade-offs.

| Onde o híbrido é aprofundado | Foco |
|:---|:---|
| M02 (todas as aulas) | Como o raciocínio arquitetural muda entre ambientes |
| M06-L05, M06-L07 | Identidade híbrida e federação de workloads |
| M07-L07 | Zero Trust com legados |
| M08-L07 | Integração do legado com ambientes modernos |
| M09-L07, M10-L02, M10-L03 | Integração específica de cada provedor |
| M11 (módulo inteiro) | Arquitetura híbrida e multicloud |
| M15-L03 | Detecção multiambiente |
| M16-L04, M16-L05 | Serviços compartilhados e governança entre ambientes |

### Decisões arquiteturais

Cada módulo tem ao menos um **exercício de tomada de decisão** com matriz de alternativas; ADRs são introduzidos no M02-L08 e exigidos nos estudos de caso, laboratórios de desenho e no projeto final.

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
