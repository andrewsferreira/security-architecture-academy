---
title: Frameworks oficiais
description: Normas, frameworks e white papers oficiais de NIST, SABSA, The Open Group, ISO, CIS, OWASP, CISA e MITRE, com versão conferida e localização dos conceitos.
---

# Frameworks oficiais

Fontes institucionais por categoria. **Localizado** indica que a seção foi identificada no sumário oficial; **Lido**, que o texto foi efetivamente consultado.

<!-- frameworks:start -->

## Security Engineering

### SP 800-125 — Guide to Security for Full Virtualization Technologies

`NIST-SP800-125` · NIST · Final (28/01/2011); partes 800-125A Rev. 1 e 800-125B · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/125/final)

Página oficial conferida. Documento de 2011 — útil para conceitos de isolamento por hipervisor; não reflete tecnologias recentes.

Módulos: M00, M08 · Leitura: Consulta (prioridade 3).

### SP 800-160 Vol. 1 Rev. 1 — Engineering Trustworthy Secure Systems

`NIST-SP800-160-V1R1` · NIST · Rev. 1, final (16/11/2022) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final)

**Conceitos:** Systems security engineering; Trustworthiness; Security requirements; Architecture definition; Verification and validation; Assurance.

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| §3.2 (p. 13) | The Concept of an Adequately Secure System (stakeholder needs, minimum tolerable levels, ASARP, evidence-based determination) | M01, M02 | **Lido** |
| §3.8 (p. 27) | System Security Viewpoints (system function, security function, life cycle assets) | M00, M04 | **Lido** |
| Cap. 2 (p. 10) | Trust and Trustworthiness (confiança como crença; confiabilidade como capacidade demonstrada por evidência) | M01, M02 | **Lido** |
| Cap. 2 (p. 7) | Systems Engineering Overview (inclui Trust and Trustworthiness, p. 10) | M02, M04 | Localizado |
| Cap. 3 (p. 12) | System Security Concepts (Adequately Secure System; Assets; Loss; Protection Needs; System Security Viewpoints) | M01, M02 | Localizado |
| Cap. 4 (p. 32) | Systems Security Engineering Framework (Problem, Solution e Trustworthiness Contexts) | M02, M16 | Localizado |
| Apêndice C (p. 64) | Security Policy and Requirements (C.3 Distinguishing Requirements, Policy, and Mechanisms, p. 68) | M02 | Localizado |
| Apêndice D (p. 70) | Trustworthy Secure Design (D.3 Security Design Order of Precedence, p. 74) | M02, M04 | Localizado |
| Apêndice E (p. 82) | Principles for Trustworthy Secure Design (E.1–E.30, inclui E.9 Defense In Depth, E.16 Least Privilege, E.19 Mediated Access, E.20 Minimal Trusted Elements) | M01, M02, M04 | Localizado |
| Apêndice F (p. 102) | Trustworthiness and Assurance | M02, M16 | Localizado |
| Apêndice H (p. 115) | Technical Processes (H.1 Business or Mission Analysis; H.2 Stakeholder Needs and Requirements Definition; H.3 System Requirements Definition; H.4 System Architecture Definition; H.9 Verification; H.11 Validation) | M02, M04, M16 | Localizado |
| Apêndice I (p. 149) | Technical Management Processes (I.3 Decision Management, p. 153; I.4 Risk Management, p. 154) | M02, M03 | Localizado |

Página oficial conferida: final de 16/11/2022, substitui a versão de 21/03/2018; sem Rev. 2 mencionada. Sumário do PDF conferido (capítulos, apêndices C–L e páginas impressas); conteúdo das seções ainda não lido. Em 2026-10-23 foram lidos no PDF o §3.2, o §3.8 e a seção Trust and Trustworthiness do Cap. 2; os apêndices (C–L) não são extraídos pela ferramenta de leitura e permanecem localizados apenas pelo sumário.

Módulos: M01, M02, M04, M16, M17 · Leitura: Essencial (prioridade 1).

### RFC 1918 — Address Allocation for Private Internets (BCP 5)

`RFC-1918` · IETF · Fevereiro de 1996; atualizado pelo RFC 6761 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.rfc-editor.org/info/rfc1918)

Página do RFC Editor conferida: BCP 5; obsoleta os RFCs 1597 e 1627.

Módulos: M00, M05 · Leitura: Consulta (prioridade 3).

### RFC 2104 — HMAC: Keyed-Hashing for Message Authentication

`RFC-2104` · IETF · Fevereiro de 1997; Informational; atualizado pelo RFC 6151 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.rfc-editor.org/rfc/rfc2104)

Página lida em 2026-10-23 (título, autores, data, status, resumo). Usado no LAB-01.

Módulos: M01 · Leitura: Consulta (prioridade 3).

### RFC 7914 — The scrypt Password-Based Key Derivation Function

`RFC-7914` · IETF · Agosto de 2016; Informational · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.rfc-editor.org/rfc/rfc7914)

Página lida em 2026-10-23 (título, autores, data, status, resumo). Usado no LAB-01.

Módulos: M01 · Leitura: Consulta (prioridade 3).

### RFC 8996 — Deprecating TLS 1.0 and TLS 1.1 (BCP 195)

`RFC-8996` · IETF · Março de 2021 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.rfc-editor.org/rfc/rfc8996.html)

RFC lida em 2026-10-23: TLS 1.0 e 1.1 não devem ser usados; razões incluem dependência de SHA-1 e cifras legadas. Autores registrados por conhecimento prévio.

Módulos: M01, M08 · Leitura: Consulta (prioridade 3).

### RFC 9846 — The Transport Layer Security (TLS) Protocol Version 1.3

`RFC-9846` · IETF · Julho de 2026 — obsoleta o RFC 8446 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-27 · [abrir fonte oficial](https://www.rfc-editor.org/rfc/rfc9846.html)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| §1.2 | Major Differences from TLS 1.2 / resumo das mudanças em relação ao RFC 8446 | M01 | **Lido** |
| §2 | Protocol Overview — autenticação do servidor e, opcionalmente, do cliente; CertificateVerify como assinatura de todo o handshake | M01 | **Lido** |
| §2.2 | Resumption and Pre-Shared Key (PSK) — PSK sozinha perde a forward secrecy para os dados da aplicação | M01 | **Lido** |
| §2.3 | 0-RTT Data — sem garantia de forward secrecy e sem proteção contra replay entre conexões | M01 | **Lido** |
| §4.3.9 | Pre-Shared Key Exchange Modes | M01 | Localizado |

Página conferida: julho de 2026, Standards Track; obsoleta os RFCs 8446, 5246, 5077, 6961, 7627 e 8422. Segundo a seção 1.2, é uma atualização menor que mantém o número de versão e a compatibilidade, endurece alguns requisitos e esclarece o texto. O RFC 8446 deixa de ser a referência vigente. Em 2026-10-27 foram lidas as seções 2, 2.2 e 2.3 (modos de troca de chaves, forward secrecy e 0-RTT); a §4.3.9 foi localizada apenas pelo sumário.

Módulos: M00, M01, M13 · Leitura: Consulta (prioridade 2).

### The Protection of Information in Computer Systems

`SALTZER-SCHROEDER-1975` · Proceedings of the IEEE · Vol. 63, n. 9, pp. 1278–1308 · Não confirmado · redistribuição: não verificada · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://en.wikipedia.org/wiki/The_Protection_of_Information_in_Computer_Systems)

**Conceitos:** Economy of mechanism; Fail-safe defaults; Complete mediation; Open design; Separation of privilege; Least privilege; Least common mechanism; Psychological acceptability; Work factor; Compromise recording.

Dados bibliográficos e a lista dos princípios conferidos em fonte secundária (Wikipedia). O artigo original não foi aberto nesta revisão; a URL registrada é a da fonte secundária.

Módulos: M01, M02 · Leitura: Consulta (prioridade 2).

## Enterprise Security Architecture

### ISO/IEC/IEEE 42010:2022 — Architecture Description (resumo no arc42 Quality Model)

`ARC42-ISO42010-SUMMARY` · arc42 Quality Model · Página online; licença CC BY-SA 4.0 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://quality.arc42.org/standards/iso-42010)

Página lida em 2026-10-23: arquitetura como 'the fundamental concepts or properties of an entity', distinta da descrição de arquitetura. Fonte secundária; o texto da norma (paga) não foi consultado.

Módulos: M02 · Leitura: Consulta (prioridade 3).

### Cloud Adoption Framework for Azure — overview

`AZURE-CAF-OVERVIEW` · Microsoft · Atualizado em 04/09/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/overview)

Página lida em 2026-10-23.

Módulos: M10 · Leitura: Consulta (prioridade 3).

### Strangler Fig

`FOWLER-STRANGLER-FIG` · martinfowler.com · 22/08/2024 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.martinfowler.com/bliki/StranglerFigApplication.html)

Artigo lido em 2026-10-23: quatro atividades (entender resultados, dividir o problema, entregar as partes, mudar a organização); riscos de substituições completas.

Módulos: M08, M11 · Leitura: Consulta (prioridade 2).

### ISO/IEC/IEEE 42010:2022 — Software, systems and enterprise — Architecture description

`ISO-42010-2022` · ISO/IEC/IEEE · Edição 2 (novembro de 2022) · Pago · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://committee.iso.org/standard/74393.html)

Edição 2 (2022-11), substitui a de 2011.

Módulos: M02 · Leitura: Consulta (prioridade 3).

### Integrating Risk and Security within a TOGAF Enterprise Architecture

`SABSA-G152` · The Open Group / SABSA Institute · Janeiro de 2016 (Open Group Guide) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://sabsa.org/white-paper-requests/)

Título, código e data conferidos no catálogo oficial; download direto com hash SHA256. Conteúdo não lido nesta revisão. Termos de redistribuição não verificados — manter cópia apenas em private-research/. Relação com a versão atual do TOGAF Series Guide (TOG-RISK-SECURITY) a confirmar.

Módulos: M02, M03, M16 · Leitura: Aprofundada (prioridade 2).

### Modelling SABSA with ArchiMate

`SABSA-T100` · SABSA Institute · Outubro de 2019; v2.5 de fevereiro de 2026 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://sabsa.org/white-paper-requests/)

Título, código e data conferidos no catálogo oficial; download direto com hash SHA256. Conteúdo não lido nesta revisão. Termos de redistribuição não verificados — manter cópia apenas em private-research/.

Módulos: M16 · Leitura: Aprofundada (prioridade 3).

### SABSA White Paper

`SABSA-W100` · SABSA Institute · Publicado em 2009 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://sabsa.org/white-paper-requests/)

**Conceitos:** Seis camadas e visões (Business, Architect, Designer, Builder, Tradesman, Service Manager); Matriz 6 × 6 com as perguntas What, Why, How, Who, Where, When; Business Attributes Profile; Relação com o framework de Zachman.

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Figure 1 e Table 1 (p. 8–9) | Camadas e visões do modelo SABSA | M02, M16 | **Lido** |
| Table 3 (p. 15–16) | Matriz SABSA 6 × 6 (Assets, Motivation, Process, People, Location, Time) | M02, M16 | **Lido** |
| Business Attributes Profile (p. 18–20) | Engenharia de requisitos com atributos de negócio, taxonomia e métricas | M02, M16 | **Lido** |

Catálogo oficial conferido. Texto lido em 2026-10-23 numa cópia hospedada no SlideShare (© 1995–2009 SABSA Limited), pois o link direto do catálogo não é exposto ao ambiente de verificação: camadas e visões (Table 1, p. 9), matriz (Table 3, p. 16), Business Attributes Profile (pp. 19–20) e relação com Zachman (p. 8). Recomendável confirmar no PDF baixado do catálogo oficial.

Módulos: M02, M16 · Leitura: Aprofundada (prioridade 2).

### White Paper W101 — Architecting a Secure Digital World

`SABSA-W101` · SABSA Institute · Agosto de 2018 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://sabsa.org/white-paper-w101-architecting-a-secure-digital-world/)

**Conceitos:** Business-driven security architecture; Business attributes; SABSA layers.

Listado no catálogo oficial com link de download direto e hash SHA256; nenhum formulário visível na página do catálogo em 2026-10-23. A página do W101 o descreve como introdução ao SABSA para iniciantes, com visão geral e benefícios; acesso inicialmente restrito a membros, hoje listado no catálogo.

Módulos: M02, M16 · Leitura: Essencial (prioridade 1).

### SABSA Risk Management Part One – The Meaning of Risk

`SABSA-W102` · SABSA Institute · Outubro de 2018 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://sabsa.org/white-paper-requests/)

Título, código e data conferidos no catálogo oficial; download direto com hash SHA256. Conteúdo não lido nesta revisão. Termos de redistribuição não verificados — manter cópia apenas em private-research/.

Módulos: M03, M16 · Leitura: Aprofundada (prioridade 2).

### SABSA Responsibility Assignment Modelling

`SABSA-W103` · SABSA Institute · Junho de 2023 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://sabsa.org/white-paper-requests/)

Título, código e data conferidos no catálogo oficial; download direto com hash SHA256. Conteúdo não lido nesta revisão. Termos de redistribuição não verificados — manter cópia apenas em private-research/.

Módulos: M03, M16 · Leitura: Aprofundada (prioridade 3).

### SABSA Enterprise Security Architecture Principles

`SABSA-W105` · SABSA Institute · Janeiro de 2026 · Restrito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://sabsa.org/white-paper-requests/)

**Conceitos:** Framework Principles, Advantages and Benefits (PAB).

Catálogo oficial lista o documento (janeiro de 2026). A página do W105 (<https://sabsa.org/w105-sabsa-enterprise-security-architecture-principles/>) informa que ele está inicialmente disponível apenas para membros do instituto antes da liberação pública, e descreve o framework PAB — ligar direcionadores de negócio a princípios, e princípios a vantagens e benefícios mensuráveis. Conteúdo não lido.

Módulos: M02, M16 · Leitura: Essencial (prioridade 1).

### SABSA–TOGAF Integration White Paper

`SABSA-W117` · The Open Group / SABSA Institute · Outubro de 2011 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://sabsa.org/white-paper-requests/)

Título, código e data conferidos no catálogo oficial; download direto com hash SHA256. Conteúdo não lido nesta revisão. Termos de redistribuição não verificados — manter cópia apenas em private-research/. Provavelmente corresponde ao white paper anunciado pela The Open Group em 07/11/2011 (TOG-SABSA-2011) — relação a confirmar.

Módulos: M02, M16 · Leitura: Aprofundada (prioridade 2).

### TOGAF Series Guide: Integrating Risk and Security within a TOGAF Enterprise Architecture

`TOG-RISK-SECURITY` · The Open Group · Página viva — data de atualização não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://pubs.opengroup.org/togaf-standard/integrating-risk-and-security/index.html)

Introdução conferida; número e data do documento não visíveis na página.

Módulos: M02, M16 · Leitura: Consulta (prioridade 3).

### TOGAF Standard, 10th Edition (anúncio oficial)

`TOG-TOGAF-10` · The Open Group · 10ª edição (lançada em 25/04/2022) · Não confirmado · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.opengroup.org/open-group-announces-launch-togaf-standard-10th-edition)

Lançado em 25/04/2022.

Módulos: M02, M16 · Leitura: Consulta (prioridade 3).

### TOGAF — Architecture Principles (documentação online da série TOGAF 9)

`TOG-TOGAF9-PRINCIPLES` · The Open Group · Documentação online da série TOGAF 9; versão exata não indicada na página · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap20.html)

Página lida em 2026-10-23: componentes Name, Statement, Rationale e Implications; critérios de um bom conjunto — compreensível, robusto, completo, consistente e estável. O capítulo equivalente da 10ª edição não foi consultado.

Módulos: M02 · Leitura: Consulta (prioridade 3).

## Zero Trust

### Zero Trust Maturity Model, Version 2.0

`CISA-ZTMM-2` · CISA · 2.0 (abril de 2023) · Leitura online gratuita · redistribuição: não verificada · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://www.cisa.gov/zero-trust-maturity-model)

**Conceitos:** Cinco pilares: Identity, Devices, Networks, Applications and Workloads, Data; Capacidades transversais: Visibility and Analytics, Automation and Orchestration, Governance; Estágios: Traditional, Initial, Advanced, Optimal.

Página da CISA aberta, mas sem versão e data visíveis no trecho; pilares, capacidades e data (abril de 2023) confirmados por fonte secundária da Microsoft (learn.microsoft.com, cisa-zero-trust-maturity-model-intro). O PDF oficial não pôde ser aberto pela ferramenta (erro do site). Funções por pilar e descrições de estágios para Identity/Authentication e Networks/Network Segmentation conferidas em reprodução da Thales (ebook) e definição de estágios e capacidades transversais no Microsoft Learn (cisa-zero-trust-maturity-model-intro).

Módulos: M07 · Leitura: Consulta (prioridade 3).

### SP 1800-35 — Implementing a Zero Trust Architecture

`NIST-SP1800-35` · NIST National Cybersecurity Center of Excellence (NCCoE) · Final (10/06/2025) · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://pages.nist.gov/zero-trust-architecture/)

Notícia oficial do CSRC conferida em 2026-10-23: final de 10/06/2025, 19 implementações de exemplo com 24 fornecedores; o documento mapeia as capacidades ao CSF, à SP 800-53 Rev. 5 e às medidas de segurança de software crítico. Conteúdo das implementações não lido.

Módulos: M07, M11 · Leitura: Consulta (prioridade 2).

### SP 800-207 — Zero Trust Architecture

`NIST-SP800-207` · NIST · Final (11/08/2020) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/207/final)

**Conceitos:** Sete tenets (§2.1); Policy Decision Point e Policy Enforcement Point (§3); Trust algorithm (§3.3); Modelos de implantação (§3.2); Migração e arquitetura híbrida com perímetro (§7.2).

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| §2.1 (p. 6) | Tenets of Zero Trust | M07, M02 | **Lido** |
| §2.2 (p. 8) | A Zero Trust View of a Network | M07 | Localizado |
| §3 (p. 9) | Logical Components of Zero Trust Architecture | M06, M07 | **Lido** |
| §3.1 (p. 11–12) | Variations of Zero Trust Architecture Approaches (identity governance, micro-segmentation, SDP) | M05, M07 | **Lido** |
| §3.2 (p. 13–16) | Deployed Variations of the Abstract Architecture | M07 | **Lido** |
| §3.3 (p. 17–19) | Trust Algorithm | M07 | **Lido** |
| §4 (p. 23) | Deployment Scenarios/Use Cases (inclui §4.2 Multi-cloud/Cloud-to-Cloud Enterprise) | M07, M11 | Localizado |
| §5 (p. 28–30) | Threats Associated with Zero Trust Architecture | M04, M07 | **Lido** |
| §7 (p. 36–41) | Migrating to a Zero Trust Architecture (inclui §7.2 Hybrid ZTA and Perimeter-Based Architecture) | M07, M11, M16 | **Lido** |
| Apêndice B (p. 46) | Identified Gaps in the Current State-of-the-Art in ZTA | M07 | Localizado |

Página oficial conferida: final de 11/08/2020; relacionados SP 800-207A e CSWP 20. Sumário do PDF conferido (seções e páginas impressas) e §2.1 lida: sete princípios (tenets). Demais seções identificadas pelo sumário. Em 2026-10-23 foram lidos no PDF o §3 (componentes lógicos e fontes de dados), §3.1 (abordagens), §3.2 (modelos de implantação), §3.3 (algoritmo de confiança), §5 (ameaças) e §7 (migração).

Módulos: M02, M05, M06, M07, M11, M16 · Leitura: Essencial (prioridade 1).

### SP 800-207A — A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Location Environments

`NIST-SP800-207A` · NIST · Final (13/09/2023) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/207/a/final)

Notícia oficial do CSRC conferida em 2026-10-23: políticas de nível de identidade e de rede; gateways e infraestrutura de identidade de serviço; monitoração e telemetria para ajustar acessos e exigir autenticação adicional; service mesh como infraestrutura de apoio. Texto integral não lido.

Módulos: M07, M09, M12 · Leitura: Consulta (prioridade 2).

## Governance & Risk

### CIS Critical Security Controls v8.1

`CIS-CONTROLS-V8-1` · Center for Internet Security · v8.1 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.cisecurity.org/controls/v8-1)

Página oficial conferida: v8.1 descrita como atualização iterativa da v8, com mapeamentos realinhados ao CSF 2.0, inclusão da função Govern, glossário ampliado e classes de ativos revisadas. Página de Implementation Groups: 153 safeguards nas versões 8 e 8.1; IG1 é 'essential cyber hygiene' e todo ambiente deveria começar por ele; IG3 inclui todos os safeguards. Contagem por IG não conferida (está em imagem). Licença não exibida — redistribuição não verificada.

Módulos: M02, M03, M08 · Leitura: Consulta (prioridade 3).

### BOD 23-01: Improving Asset Visibility and Vulnerability Detection on Federal Networks

`CISA-BOD-23-01` · CISA · Diretiva de outubro de 2022; ações exigidas até 03/04/2023 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://cisa.gov/binding-operational-directive-23-01)

Página lida em 2026-10-23: obrigatória apenas para agências civis federais dos EUA; usada no curso como referência de prática, não como obrigação.

Módulos: M11, M14 · Leitura: Consulta (prioridade 3).

### Navigating the ISO/IEC 27001:2022 Transition: A 90-Day Challenge

`ISACA-ISO27001-TRANSITION-2024` · ISACA Journal · ISACA Journal, vol. 3, 2024 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.isaca.org/resources/isaca-journal/issues/2024/volume-3/navigating-the-iso-iec-27001-2022-transition-a-90-day-challenge)

Artigo lido em 2026-10-23 (fonte secundária confiável, associação profissional): publicação da 27001:2022 em 25/10/2022; período de transição encerrado em 31/10/2025; cláusulas 4 a 10 não podem ser excluídas por quem declara conformidade; a Declaração de Aplicabilidade registra os controles do Anexo A incluídos ou excluídos, com justificativa, e liga a avaliação ao tratamento de riscos; a ISO/IEC 27002 detalha propósito e orientação de cada controle.

Módulos: M03 · Leitura: Aprofundada (prioridade 3).

### ISO/IEC 27001:2022 — Information security, cybersecurity and privacy protection — Information security management systems — Requirements

`ISO-27001-2022` · ISO/IEC · 3ª edição (25/10/2022) · Pago · redistribuição: proibida · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://www.iso.org/standard/27001)

**Conceitos:** Anexo A com 93 controles em quatro temas: organizacionais (37), pessoas (8), físicos (14), tecnológicos (34).

Norma paga; página da ISO exigiu permissão não concedida ao ambiente. A existência da edição 2022 está confirmada nos mapeamentos oficiais do NIST (NIST-CSF-INFORMATIVE-REFS); a estrutura do Anexo A foi conferida em fonte secundária (scrut.io). Data de publicação, encerramento da transição (31/10/2025), cláusulas 4–10 e Declaração de Aplicabilidade conferidos no ISACA Journal (ISACA-ISO27001-TRANSITION-2024).

Módulos: M03, M16 · Leitura: Consulta (prioridade 2).

### ISO/IEC 27002:2022 — Information security, cybersecurity and privacy protection — Information security controls

`ISO-27002-2022` · ISO/IEC · 3ª edição (15/02/2022) · Pago · redistribuição: proibida · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://www.iso.org/standard/75652.html)

**Conceitos:** 93 controles em quatro temas (cláusulas 5 a 8); 11 controles novos, entre eles 5.23 uso de serviços de cloud e 8.28 secure coding; Atributos de controle: tipo, propriedade, conceito de cibersegurança, capacidade operacional, domínio de segurança.

Norma paga, não lida. Estrutura conferida em fonte secundária (EY, alerta sobre a ISO/IEC 27002:2022): publicação em 15/02/2022; de 114 controles em 14 domínios para 93 em 4 temas (58 atualizados, 24 consolidados, 11 novos); cinco tipos de atributo, com exemplos de valores.

Módulos: M03, M16 · Leitura: Consulta (prioridade 3).

### The NIST Cybersecurity Framework (CSF) 2.0 — NIST CSWP 29

`NIST-CSF-2` · NIST · 2.0 (CSWP 29, 26/02/2024) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final)

**Conceitos:** Functions: Govern, Identify, Protect, Detect, Respond, Recover; Organizational Profiles (atual e alvo); Tiers.

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Sec. 2 (p. 3–4) | CSF Core — seis Functions (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) | M01, M03 | **Lido** |
| Sec. 3.1 (p. 6–7) | Organizational Profiles — Current e Target, cinco etapas | M03, M16 | **Lido** |
| Sec. 3.2 e App. B (p. 7–8, 24–26) | Tiers — Partial, Risk Informed, Repeatable, Adaptive | M03 | **Lido** |
| App. A — GOVERN (p. 16–18) | Categorias GV.OC, GV.RM, GV.RR, GV.PO, GV.OV, GV.SC | M03, M16 | **Lido** |

Publicado em 26/02/2024. DOI 10.6028/NIST.CSWP.29. PDF lido em 2026-10-23 (Sec. 1–3 e Apêndices A–B): o CSF descreve resultados e declara que não prescreve como alcançá-los (Sec. 1, p. 1).

Módulos: M02, M03, M16 · Leitura: Essencial (prioridade 1).

### Cybersecurity Framework — FAQs

`NIST-CSF-FAQ` · NIST · Página viva — data de atualização não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://nist.gov/cyberframework/faqs)

Functions: Govern, Identify, Protect, Detect, Respond, Recover. Tiers: Partial, Risk Informed, Repeatable, Adaptive.

Módulos: M02, M03 · Leitura: Consulta (prioridade 3).

### Cybersecurity Framework (página principal e recursos)

`NIST-CSF-HOME` · NIST · Leitura online gratuita · redistribuição: não verificada · **Indisponível** · [abrir fonte oficial](https://www.nist.gov/cyberframework)

Domínio `www.nist.gov/cyberframework` fora da lista de acesso do ambiente de verificação em 2026-10-23. Usar NIST-CSF-2 e NIST-CSF-INFORMATIVE-REFS.

Módulos: M03 · Leitura: Consulta (prioridade 3).

### CSF 2.0 Informative References

`NIST-CSF-INFORMATIVE-REFS` · NIST · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.nist.gov/cyberframework/csf-20-informative-references)

**Conceitos:** Mapeamento CSF 2.0 ↔ SP 800-53 Rev. 5.2.0, ISO/IEC 27001:2022, CIS Controls 8.1, CCM v4.0, PCI DSS 4.0.1.

Página conferida (criada em 15/02/2024, atualizada em 15/10/2026): download integral em .xlsx, traduções em 11 idiomas (inclui português), catálogo e relatórios de comparação. Mapeamentos de terceiros não têm correção testada pelo NIST.

Módulos: M03, M16 · Leitura: Consulta (prioridade 2).

### Risk Management Framework (projeto no CSRC)

`NIST-RMF` · NIST · Página viva — data de atualização não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/projects/risk-management)

Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor.

Módulos: M02, M03 · Leitura: Consulta (prioridade 3).

### SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments

`NIST-SP800-30-R1` · NIST · Rev. 1, final (17/09/2012) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/30/r1/final)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Sec. 2.1 (p. 4) | Componentes da gestão de riscos: frame, assess, respond, monitor (Figura 1) | M03 | **Lido** |
| Sec. 2.3.1 (p. 8–12) | Modelo genérico de risco: fonte e evento de ameaça, vulnerabilidade, condição predisponente, probabilidade, impacto, risco (Figura 3) | M01, M03 | **Lido** |
| Sec. 2.3.2–2.3.3 (p. 14–16) | Abordagens de avaliação (quantitativa, qualitativa, semiquantitativa) e de análise (ameaça, ativo/impacto, vulnerabilidade) | M03 | **Lido** |
| Sec. 2.4 (p. 17) | Três níveis de gestão de riscos: organização, processo de negócio, sistema (Figura 4) | M03 | **Lido** |
| Cap. 3 (p. 23–38) | Processo de avaliação: preparar, conduzir, comunicar, manter | M03 | Localizado |

Página oficial conferida; sem revisão mais nova. PDF lido em 2026-10-23 até a Sec. 2.4 (Cap. 2); do Cap. 3 só o sumário foi conferido (etapas preparar, conduzir, comunicar e manter).

Módulos: M01, M03, M14 · Leitura: Essencial (prioridade 1).

### SP 800-37 Rev. 2 — Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy

`NIST-SP800-37-R2` · NIST · Rev. 2, final (20/12/2018) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/37/r2/final)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Sec. 2.2 (p. 9–10) | Etapas do RMF: Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor | M03 | **Lido** |
| Sec. 3.1 (Tabela 1) (p. 12–13) | Prepare — tarefas no nível da organização (P-1 a P-7) | M03 | **Lido** |
| Apêndice F | Decisões de autorização | M03 | Localizado |

Página oficial conferida: final de 20/12/2018, substitui a Rev. 1 (2014); nenhuma Rev. 3 mencionada. O resumo cita categorização, seleção, implementação e avaliação de controles, autorização e monitoramento contínuo, além das atividades de preparação. As sete etapas (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) foram conferidas na página do projeto RMF (NIST-RMF). PDF lido em 2026-10-23 até a Sec. 3.1: autorização para operar ou para usar, autorização de controles comuns para herança, fronteira de autorização (nota 36, p. 16) e prioridade para a autorização contínua (Sumário Executivo, p. viii). Tarefas do nível de sistema e Apêndice F não lidos.

Módulos: M03, M16 · Leitura: Essencial (prioridade 1).

### SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations

`NIST-SP800-53` · NIST · Rev. 5 (atualização de 10/12/2020); Release 5.2.0 de 27/08/2025 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

**Conceitos:** Control families; Control enhancements; Catálogo versus baseline; OSCAL.

Página oficial conferida: Release 5.2.0 em 27/08/2025; materiais suplementares em OSCAL (JSON, XML, YAML), planilhas e crosswalk ISO/IEC 27001:2022. Partes: SP 800-53A Rev. 5 e SP 800-53B. Catálogo — não é uma lista de obrigações para toda organização. A página lista 20 famílias de controles, inclusive Supply Chain Risk Management. Texto do controle AC-5 (Separation of Duties) conferido em réplica do catálogo (stigviewer.com, 2026-10-23): identificar e documentar deveres que exigem separação e definir autorizações de acesso que a suportem; discussão inclui dividir funções de negócio e de suporte entre pessoas diferentes e evitar que quem administra controle de acesso também administre funções de auditoria; baselines moderada e alta. Texto do controle SA-22 (Unsupported System Components) conferido em réplica (stigviewer.com): substituir componentes sem suporte do fornecedor ou prover fontes alternativas de suporte; discussão admite isolamento como redução de risco; baselines baixa, moderada e alta.

Módulos: M01, M02, M03, M05, M06, M08, M14, M15 · Leitura: Consulta (prioridade 2).

### SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations

`NIST-SP800-53A-R5` · NIST · Rev. 5, final (25/01/2022) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final)

**Conceitos:** Métodos de avaliação: examinar, entrevistar e testar.

Página oficial conferida: metodologia e procedimentos de avaliação alinhados à SP 800-53 Rev. 5, adaptáveis ao risco e executáveis em várias fases do ciclo de vida. Definições de examine, interview e test conferidas no glossário do CSRC, com origem na SP 800-53A Rev. 5.

Módulos: M03, M04 · Leitura: Consulta (prioridade 2).

### SP 800-53B — Control Baselines for Information Systems and Organizations

`NIST-SP800-53B` · NIST · Final (10/12/2020); Release 5.2.0 de 27/08/2025, sem mudanças nas baselines · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final)

**Conceitos:** Baselines low, moderate e high; Baseline de privacidade; Tailoring; Overlays.

Página oficial conferida: baselines por nível de impacto, baseline de privacidade independente do nível, orientação de tailoring e de overlays. A Release 5.2.0 não alterou as baselines.

Módulos: M03 · Leitura: Consulta (prioridade 2).

### SP 800-55 Vol. 1 — Measurement Guide for Information Security: Identifying and Selecting Measures

`NIST-SP800-55-V1` · NIST · Final (04/12/2024); Vol. 2 — Developing an Information Security Measurement Program · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/55/v1/final)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Sec. 1.4 e 2.4 (p. 2, 9–11) | Medidas versus métricas | M03 | **Lido** |
| Sec. 2.2 (p. 7–8) | Avaliação qualitativa, semiquantitativa e quantitativa | M03 | **Lido** |
| Sec. 3.1–3.2 (p. 12–17) | Documentação de medidas, coleta e qualidade dos dados; características de boas medidas | M03, M14 | **Lido** |
| Sec. 3.3 (p. 17–18) | Tipos de medida: implementação, eficácia, eficiência e impacto | M03, M14 | **Lido** |
| Sec. 3.4 (p. 20–22) | Priorização de medidas | M03 | **Lido** |

Páginas oficiais dos volumes 1 e 2 conferidas (04/12/2024); substituem a SP 800-55 Rev. 1 (2008). Vol. 1 lido em 2026-10-23 (Sec. 1–3); Vol. 2 não lido.

Módulos: M03, M14, M16 · Leitura: Consulta (prioridade 2).

### Documenting Architecture Decisions (2011)

`NYGARD-ADR-2011` · Cognitect (Michael Nygard) · 15/11/2011 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

Seções Title, Context, Decision, Status e Consequences.

Módulos: M02, M16 · Leitura: Consulta (prioridade 3).

### PCI DSS v4.0.1 — Payment Card Industry Data Security Standard

`PCI-DSS-401` · PCI Security Standards Council · v4.0.1 (11/06/2024); substituiu a v4.0 em 31/12/2024 · Gratuito com cadastro · redistribuição: restrita · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://www.pcisecuritystandards.org/document_library/)

Data e natureza da revisão (menor, sem requisitos novos) conferidas em fonte secundária (usd.de); a biblioteca oficial não foi aberta. O download oficial exige aceite de licença do PCI SSC (conhecimento geral, não conferido). Estrutura de 12 requisitos em 6 objetivos e aplicação a quem armazena, processa ou transmite dados de portadores de cartão conferidas em fonte secundária (opensecurityarchitecture.org).

Módulos: M03, M13 · Leitura: Consulta (prioridade 2).

### SABSA — White Paper Requests (catálogo de white papers)

`SABSA-CATALOG` · The SABSA Institute · Página viva — data de atualização não exibida · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://sabsa.org/white-paper-requests/)

Catálogo oficial com W100, W101, W102, W103, W105, W117, SW104, R101, T100 e G152, cada um com link de download e hash SHA256. A página não exibe formulário nem termos; termos de redistribuição não verificados.

Módulos: M16 · Leitura: Consulta (prioridade 3).

### TOGAF and SABSA Integration (white paper, 2011)

`TOG-SABSA-2011` · The Open Group / The SABSA Institute · Comunicado de 07/11/2011 · Não confirmado · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.opengroup.org/open-group-issues-guide-integrating-togaf%C2%AE-sabsa%C2%AE-secure-architecture-methodology)

Comunicado de 07/11/2011.

Módulos: M02, M16 · Leitura: Consulta (prioridade 3).

## Identity Security

### Security best practices in IAM — IAM User Guide

`AWS-IAM-BEST-PRACTICES` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

Página lida em 2026-10-23: 14 práticas — federação com credenciais temporárias para humanos, papéis para workloads, MFA (resistente a phishing quando possível), proteção do root, privilégio mínimo, Access Analyzer, revisão de não usados, condições, verificação de acesso público e entre contas, guardrails com SCPs e RCPs, permissions boundaries.

Módulos: M09 · Leitura: Essencial (prioridade 1).

### What is IAM Identity Center?

`AWS-IAM-IDENTITY-CENTER` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)

Página lida em 2026-10-23: conectar o IdP existente ou criar usuários; permission sets para funções comuns em várias contas; instância de organização como boa prática e única que gerencia acesso a contas.

Módulos: M09, M11 · Leitura: Consulta (prioridade 2).

### Create a role for OpenID Connect federation (console) — AWS IAM User Guide

`AWS-IAM-OIDC-ROLE` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html)

Página lida em 2026-10-23: condições de aud e sub na política de confiança; aviso de que sem limitar o sub ao repositório, ações do GitHub de organizações fora do controle da conta podem assumir o papel; o IAM rejeita políticas sem sub ou com curinga para o provedor do GitHub.

Módulos: M06, M09, M11 · Leitura: Consulta (prioridade 2).

### Policy evaluation logic e Cross-account policy evaluation logic — IAM User Guide

`AWS-IAM-POLICY-EVALUATION` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)

Páginas lidas em 2026-10-23: na mesma conta, identidade e recurso formam união; boundaries, SCPs e RCPs formam interseção; negação explícita prevalece; entre contas, a requisição só é permitida se a avaliação nas duas contas permitir (reference_policies_evaluation-logic-cross-account.html).

Módulos: M09 · Leitura: Consulta (prioridade 2).

### What is AWS Identity and Access Management Roles Anywhere?

`AWS-IAM-ROLES-ANYWHERE` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)

Página lida em 2026-10-23: trust anchors (AWS Private CA ou CA externa), perfis com session policy, papéis que confiam no serviço; fronteira de confiança é a conta, salvo condições na política de confiança.

Módulos: M09, M11 · Leitura: Consulta (prioridade 3).

### Configure SAML and SCIM with Microsoft Entra ID and IAM Identity Center

`AWS-IDC-ENTRA` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/singlesignon/latest/userguide/idp-microsoft-entra.html)

Página lida em 2026-10-23: SAML 2.0 para entrada e SCIM 2.0 para provisionamento; atributos para controle de acesso; limitações: remoção de atributo não sincroniza, grupos aninhados não são provisionados, atributos multivalorados rejeitados, convidados exigem mapeamento de claims.

Módulos: M11 · Leitura: Consulta (prioridade 3).

### What is Azure role-based access control (Azure RBAC)?

`AZURE-RBAC-OVERVIEW` · Microsoft · Atualizado em 12/03/2024 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)

Página lida em 2026-10-23: quatro níveis de escopo (management group, assinatura, grupo de recursos, recurso); modelo aditivo; deny assignment aplicável bloqueia o acesso antes do cálculo das permissões; condições em atribuições.

Módulos: M10 · Leitura: Consulta (prioridade 2).

### Guidance on Phishing-Resistant and Numbers Matching Multifactor Authentication

`CISA-MFA-GUIDANCE-2022` · CISA (via alerta TLP:WHITE do Health-ISAC) · Fact sheets de 31/10/2022; alerta de 01/11/2022 · Leitura online gratuita · redistribuição: não verificada · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://www.aha.org/system/files/media/file/2022/11/cisa-tlp-white-guidance-on-phishing-resistant-and-numbers-matching-multifactor-authentication-11-1-22.pdf)

Lido o alerta que resume os fact sheets da CISA: adoção de MFA resistente a phishing por todas as organizações; number matching como mitigação intermediária para MFA por push. O fact sheet original não pôde ser aberto pela ferramenta.

Módulos: M06 · Leitura: Aprofundada (prioridade 3).

### Federating Google Cloud with Microsoft Entra ID

`GCP-FEDERATION-ENTRA` · Google Cloud · Revisado em 26/06/2024 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory)

Página lida em 2026-10-23 (primeiros 100 mil caracteres): sincronização unidirecional sem senhas; SSO por SAML aplicando MFA e políticas do Entra; mapeamento por UPN com domínio personalizado; limitações com convidados B2B; um Cloud Identity por tenant; exclusão de grupo no Entra não exclui no Google Cloud.

Módulos: M11 · Leitura: Consulta (prioridade 3).

### IAM overview — Google Cloud

`GCP-IAM-OVERVIEW` · Google Cloud · Atualizado em 20/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/iam/docs/overview)

Página lida em 2026-10-23: não se concedem permissões diretamente; papéis básicos não devem ser usados em produção; política de permissão efetiva é a união com as dos ancestrais; deny policies bloqueiam permissões mesmo concedidas; PAB define recursos elegíveis; Privileged Access Manager para acesso temporário; API eventualmente consistente.

Módulos: M10 · Leitura: Essencial (prioridade 2).

### Best practices for using service accounts securely

`GCP-SA-BEST-PRACTICES` · Google Cloud · Atualizado em 20/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)

Página lida em 2026-10-23: evitar chaves sempre que possível; contas de serviço anexadas e workload identity federation; contas padrão podem receber Editor automaticamente — desabilitar com restrição organizacional; restrições de criação de chaves aplicadas por padrão em organizações criadas a partir de 03/05/2024.

Módulos: M10, M11 · Leitura: Consulta (prioridade 3).

### Workforce Identity Federation — Google Cloud IAM

`GCP-WORKFORCE-IDF` · Google Cloud · Atualizado em 20/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/iam/docs/workforce-identity-federation)

Página lida em 2026-10-23: não armazena contas no Google Cloud; IdPs OIDC ou SAML (Entra ID, AD FS, Okta); mapeamento de atributos em CEL; condições de atributo; limite de 400 grupos por usuário; lista própria de produtos suportados.

Módulos: M11 · Leitura: Consulta (prioridade 3).

### Workload Identity Federation — Google Cloud IAM

`GCP-WORKLOAD-IDENTITY-FED` · Google Cloud · Atualizada em 20/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/iam/docs/workload-identity-federation)

Página lida em 2026-10-23: troca de credenciais pelo STS (RFC 8693) por tokens de curta duração; pools e provedores; mapeamento e condições de atributos; um pool por ambiente; risco de conceder acesso a todo o pool.

Módulos: M06, M09, M10, M11 · Leitura: Consulta (prioridade 2).

### What is cloud infrastructure entitlement management (CIEM)?

`IBM-WHAT-IS-CIEM` · IBM Think · 17/06/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.ibm.com/think/topics/ciem)

Página lida em 2026-10-23: CIEM como módulo frequentemente entregue dentro de uma CNAPP; comparação entre permissões concedidas e usadas.

Módulos: M11 · Leitura: Consulta (prioridade 3).

### Active Directory Forest Recovery Guide

`MS-AD-FOREST-RECOVERY` · Microsoft Learn · Atualizado em 16/08/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-guide)

Página de entrada lida em 2026-10-23 (versão localizada): recuperação de floresta como último recurso quando todos os DCs deixam de funcionar normalmente, por corrupção ou comprometimento; estrutura do guia em etapas. Detalhes de planejamento não lidos. Página 'Steps for restoring the forest' lida: cinco etapas — identificar o problema; determinar como recuperar; recuperação inicial isolada de um DC por domínio, limpeza, redefinição de contas privilegiadas e correção de problemas da violação; reimplantar os demais DCs; limpeza final (resolução de nomes e aplicações). Procedimentos detalhados (subpáginas) não lidos.

Módulos: M06, M08, M15 · Leitura: Consulta (prioridade 2).

### The enterprise access model (módulo de treinamento SC-100)

`MS-ENTERPRISE-ACCESS-MODEL` · Microsoft Learn · Atualizado em 2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/training/modules/design-solutions-secure-privileged-access/2-enterprise-access-model)

Página lida em 2026-10-23: planos de dados/workload, gestão e controle; caminhos de acesso de usuários, aplicações e privilegiados; separação de funções entre planos, ativação just-in-time, aprovação, escopo mínimo e contas de emergência. Não compara explicitamente com o modelo de tiers legado.

Módulos: M06, M07 · Leitura: Consulta (prioridade 2).

### What is Microsoft Entra Cloud Sync?

`MS-ENTRA-CLOUD-SYNC` · Microsoft · Atualizado em 21/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync)

Página lida em 2026-10-23: agente de provisionamento com conexões apenas de saída; serviço de provisionamento na nuvem; múltiplos agentes para alta disponibilidade; florestas desconectadas; não é substituto direto de todas as implantações do Connect Sync — usar o guia de decisão.

Módulos: M10, M11 · Leitura: Consulta (prioridade 3).

### What is Conditional Access in Microsoft Entra ID?

`MS-ENTRA-CONDITIONAL-ACCESS` · Microsoft · Atualizado em 27/04/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)

Página lida em 2026-10-23: sinais de usuário, grupo, agente, localização IP, dispositivo, aplicação, risco e Defender for Cloud Apps; decisões de bloqueio ou concessão com requisitos (MFA, força de autenticação, dispositivo compatível, etc.); aplicado após o primeiro fator; exige Entra ID P1; políticas de risco exigem ID Protection (P2).

Módulos: M10, M07 · Leitura: Consulta (prioridade 2).

### Authentication for Microsoft Entra hybrid identity solutions

`MS-ENTRA-HYBRID-AUTHN` · Microsoft Learn · Atualizada em 09/04/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn)

Página lida em 2026-10-23 (versão localizada, conteúdo em inglês): recomendação de habilitar PHS em qualquer cenário, como contingência e para detecção de credenciais vazadas; PTA e federação dependem do ambiente local; failover manual.

Módulos: M06, M11 · Leitura: Consulta (prioridade 2).

### What are managed identities for Azure resources?

`MS-ENTRA-MANAGED-IDENTITIES` · Microsoft · Atualizado em 19/08/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)

Página lida em 2026-10-23: eliminam a gestão de credenciais; credenciais não acessíveis ao desenvolvedor; system-assigned vinculada ao ciclo de vida do recurso; user-assigned compartilhável e recomendada para serviços Microsoft; tokens obtidos pelo SDK sem segredos.

Módulos: M10, M11 · Leitura: Consulta (prioridade 2).

### What is Microsoft Entra Privileged Identity Management?

`MS-ENTRA-PIM` · Microsoft · Atualizado em 23/04/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)

Página lida em 2026-10-23: papéis do Entra, papéis de recursos do Azure e PIM for Groups; atribuições elegíveis versus ativas.

Módulos: M10, M06 · Leitura: Consulta (prioridade 2).

### Workload identity federation — Microsoft Entra Workload ID

`MS-ENTRA-WORKLOAD-ID-FED` · Microsoft Learn · Atualizada em 09/04/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation)

Página lida em 2026-10-23: elimina segredos e certificados de workloads externos; correspondência exata (sensível a maiúsculas) de issuer, subject e audience; cenários GitHub Actions, Kubernetes, Google Cloud, AWS e SPIFFE; o escopo da confiança depende da precisão do sujeito e do emissor.

Módulos: M06, M10, M11 · Leitura: Consulta (prioridade 2).

### Microsoft's guidance to help mitigate Kerberoasting

`MS-KERBEROASTING-2024` · Microsoft Security Blog · 11/10/2024 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.microsoft.com/security/blog/2024/10/11/microsofts-guidance-to-help-mitigate-kerberoasting)

Artigo lido em 2026-10-23: contas com SPN; quebra offline; gMSA/dMSA; senhas longas e aleatórias; AES; auditoria de SPNs; detecção por tipo de cifra incomum e volume de pedidos.

Módulos: M06, M08 · Leitura: Consulta (prioridade 2).

### SP 800-162 — Guide to Attribute Based Access Control (ABAC) Definition and Considerations

`NIST-SP800-162` · NIST · Janeiro de 2014, atualizações de 02/08/2019 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-162.pdf)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Sec. 2 (p. 4–17) | ABAC — conceitos, comparação com ACL e RBAC, componentes da empresa | M06, M07 | **Lido** |
| Sec. 3 (p. 17–26) | Considerações de implantação (custo, governança, atributos, auditoria) | M06 | **Lido** |

PDF lido em 2026-10-23 (Sec. 2–3, parcialmente): ABAC concede ou nega acesso por atributos do sujeito, do objeto e condições de ambiente; ACL e RBAC são casos especiais de ABAC; risco de explosão de papéis no RBAC; responder 'quem pode acessar este objeto' é mais difícil em ABAC.

Módulos: M06, M07 · Leitura: Consulta (prioridade 2).

### SP 800-63-4 — Digital Identity Guidelines (com SP 800-63A-4, 63B-4 e 63C-4)

`NIST-SP800-63-4` · NIST · Rev. 4, final (31/07/2025); substitui a SP 800-63-3 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/63/4/final)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| SP 800-63B-4, Sec. 2 | Authentication Assurance Levels (AAL1, AAL2, AAL3) e resistência a phishing | M06 | **Lido** |
| SP 800-63B-4, Sec. 3.1.1 | Senhas: comprimento, composição, troca periódica, lista de bloqueio | M06 | **Lido** |
| SP 800-63B-4, Sec. 3.1.3 | Autenticadores fora de banda; PSTN/SMS restrito; e-mail proibido | M06 | **Lido** |

Página oficial conferida em 2026-10-23 (final de 31/07/2025, substitui a 63-3 de 02/03/2020). Versão HTML da 63B-4 lida até a Sec. 3.2: AAL3 exige autenticador resistente a phishing; AAL2 deve oferecer ao menos uma opção resistente a phishing; autenticadores sincronizáveis (passkeys sincronizadas) não podem ser usados em AAL3; senhas de fator único com no mínimo 15 caracteres; sem regras de composição nem troca periódica; PSTN restrito; e-mail proibido para fora de banda. Escrito para sistemas do governo federal dos EUA.

Módulos: M06, M07, M17 · Leitura: Essencial (prioridade 1).

### Security Assertion Markup Language (SAML) V2.0 Technical Overview

`OASIS-SAML2-TECH-OVERVIEW` · OASIS · Committee Draft 02, 25/03/2008 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)

Documento lido em 2026-10-23 (Sec. 3–5). É uma visão geral não normativa (Committee Draft); a especificação normativa é o conjunto SAML V2.0 da OASIS.

Módulos: M06 · Leitura: Consulta (prioridade 2).

### OpenID Connect Core 1.0 incorporating errata set 2

`OIDC-CORE-1` · OpenID Foundation · Final, errata set 2 (15/12/2023) · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://openid.net/specs/openid-connect-core-1_0.html)

Especificação lida em 2026-10-23 (resumo, ID Token e fluxos): iss, sub, aud, exp e iat obrigatórios; fluxos Authorization Code, Implicit e Hybrid.

Módulos: M06, M12 · Leitura: Consulta (prioridade 2).

### Microsoft Details NTLM Phase-Out Plan in Windows: How IT Teams Can Prepare

`PETRI-NTLM-2026` · Petri · 02/02/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://petri.com/?p=773920)

Artigo lido em 2026-10-23 (fonte secundária de imprensa especializada): auditoria aprimorada de NTLM, Local KDC e IAKerb, NTLM de rede bloqueado por padrão em versões futuras, com reabilitação possível por política; citação da Microsoft de que desabilitar por padrão não significa remover.

Módulos: M06, M08 · Leitura: Aprofundada (prioridade 3).

### RFC 4120 — The Kerberos Network Authentication Service (V5)

`RFC-4120` · IETF · Julho de 2005 (Standards Track); torna obsoleta a RFC 1510 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://rfc-editor.org/rfc/rfc4120.html)

RFC lida em 2026-10-23 (Sec. 1 e 3, parcialmente). Autores registrados por conhecimento prévio, não conferidos.

Módulos: M06 · Leitura: Consulta (prioridade 3).

### RFC 9700 — Best Current Practice for OAuth 2.0 Security (BCP 240)

`RFC-9700` · IETF · Janeiro de 2025; atualiza RFC 6749, 6750 e 6819 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.rfc-editor.org/rfc/rfc9700.html)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Sec. 2 | Best Practices (redirect exato, PKCE, implicit, password grant, tokens restritos ao remetente, refresh tokens, audiência) | M06, M12 | **Lido** |

RFC lida em 2026-10-23 (Sec. 2). Autores além de Lodderstedt registrados por conhecimento prévio, não conferidos.

Módulos: M06, M12 · Leitura: Essencial (prioridade 1).

### SPIFFE Concepts

`SPIFFE-CONCEPTS` · SPIFFE project (CNCF) · Documentação online (latest) · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/)

Página lida em 2026-10-23.

Módulos: M05, M06, M07 · Leitura: Consulta (prioridade 3).

## Application Security

### Using Abuse Case Models for Security Requirements Analysis

`MCDERMOTT-FOX-ABUSE-1999` · Annual Computer Security Applications Conference (ACSAC) · ACSAC 1999 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.ida.liu.se/~TDDC90/literature/papers/mcdermott_acsac99.pdf)

Artigo lido em 2026-10-23 em cópia hospedada por disciplina da Universidade de Linköping (o PDF não exibe o local de publicação; ACSAC 1999 conforme o nome do arquivo e índices bibliográficos). Redistribuição não verificada.

Módulos: M04 · Leitura: Aprofundada (prioridade 3).

### CAPEC — Common Attack Pattern Enumeration and Classification

`MITRE-CAPEC` · MITRE · Catálogo online, lançado em 2007; versão atual não exibida na página Sobre · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://capec.mitre.org/about)

Página Sobre lida em 2026-10-23: catálogo público de padrões de ataque derivados de exploits reais, com mitigações sugeridas. Termos de uso não exibidos nessa página.

Módulos: M04, M12 · Leitura: Consulta (prioridade 3).

### Threats — Microsoft Threat Modeling Tool

`MS-TMT-STRIDE` · Microsoft Learn · Atualizada em 25/08/2022 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)

Página lida em 2026-10-23 (versão localizada vi-vn, mesmo conteúdo em inglês): definições de Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service e Elevation of Privilege.

Módulos: M04 · Leitura: Consulta (prioridade 2).

### SP 800-190 — Application Container Security Guide

`NIST-SP800-190` · NIST · Final (25/09/2017) · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/190/final)

Página oficial conferida; sem revisão mais nova. O boletim ITL de outubro de 2017 (<https://csrc.nist.gov/files/pubs/shared/itlb/itlbul2017-10.pdf>) confirma que a publicação recomenda contramedidas em seis níveis: imagem, registry, orquestrador, container, SO do host e hardware. Texto integral não lido.

Módulos: M00, M12 · Leitura: Consulta (prioridade 3).

### SP 800-204 — Security Strategies for Microservices-based Application Systems

`NIST-SP800-204` · NIST · Final (07/08/2019); partes 800-204A, B, C e D · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/204/final)

**Conceitos:** Service mesh (204A); ABAC para microsserviços (204B); DevSecOps (204C); Supply chain em CI/CD (204D).

Página oficial conferida. Partes conferidas: 800-204A (maio de 2020, service mesh), 800-204B (agosto de 2021, ABAC com service mesh), 800-204C (março de 2022, DevSecOps com service mesh), 800-204D (fevereiro de 2024, segurança da cadeia de suprimentos em pipelines CI/CD). Conteúdo interno não lido.

Módulos: M00, M12 · Leitura: Consulta (prioridade 3).

### Threat Modeling Again, STRIDE per Element

`OSTERMAN-STRIDE-PER-ELEMENT-2007` · Microsoft (blog arquivado no Microsoft Learn) · 10/09/2007 · Leitura online gratuita · redistribuição: não verificada · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://learn.microsoft.com/ru-ru/archive/blogs/larryosterman/threat-modeling-again-stride-per-element)

Texto lido em 2026-10-23: para cada tipo de elemento há um conjunto limitado de categorias STRIDE; todo fluxo de dados está sujeito a Tampering, Information Disclosure e Denial of Service. A tabela completa por elemento está em imagem não legível pela ferramenta — o restante do mapeamento na M04-L02 é apresentado como mapeamento usual, não como citação.

Módulos: M04 · Leitura: Aprofundada (prioridade 3).

### OWASP Application Security Verification Standard (ASVS) 5.0.0

`OWASP-ASVS-5` · OWASP Foundation · 5.0.0 (estável; maio de 2025) · Download gratuito · redistribuição: permitida pela licença · Verificada em 2026-10-23 · [abrir fonte oficial](https://owasp.org/www-project-ASVS/)

Página do projeto conferida: versão 5.0.0 estável; licença Creative Commons Attribution-ShareAlike 4.0 International; fonte oficial no GitHub OWASP/ASVS e site asvs.owasp.org. Data de lançamento não exibida. Estrutura conferida em fonte secundária (quality.arc42.org, 2026-10-23): 17 capítulos (V1 Encoding and Sanitization a V17 WebRTC, incluindo V2 Validation and Business Logic, V6 Authentication, V8 Authorization, V15 Secure Coding and Architecture, V16 Security Logging and Error Handling); níveis cumulativos L1, L2 e L3; identificadores <capítulo>.<seção>.<requisito>, citados com a versão (ex.: v5.0.0-6.2.1); lançamento em maio de 2025.

Módulos: M04, M12 · Leitura: Consulta (prioridade 2).

### OWASP Developer Guide — Threat Modeling Project

`OWASP-TM-PROJECT` · OWASP Foundation · Página online (Developer Guide) · Leitura online gratuita · redistribuição: permitida pela licença · Verificada em 2026-10-23 · [abrir fonte oficial](https://devguide.owasp.org/en/04-design/01-threat-modeling/01-threat-modeling-project/)

Página lida em 2026-10-23: projeto em status Incubator; pytm e Cornucopia como projetos Production; Threat Dragon como Lab. Licença do Developer Guide: Creative Commons Attribution-ShareAlike 4.0 International.

Módulos: M04 · Leitura: Consulta (prioridade 3).

### Attack Trees

`SCHNEIER-ATTACK-TREES-1999` · Dr. Dobb's Journal · Dr. Dobb's Journal, dezembro de 1999 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.schneier.com/academic/archives/1999/12/attack_trees.html)

Artigo lido em 2026-10-23: objetivo na raiz, formas de alcançá-lo nas folhas; nós OR são alternativas, nós AND são passos necessários; valores booleanos ou contínuos propagados (OR = filho mais barato; AND = soma); bibliotecas de árvores reutilizáveis.

Módulos: M04 · Leitura: Essencial (prioridade 2).

### Threat Modeling Manifesto

`TM-MANIFESTO` · Threat Modeling Manifesto Working Group · Página online; data não exibida · Leitura online gratuita · redistribuição: permitida pela licença · Verificada em 2026-10-23 · [abrir fonte oficial](https://threatmodelingmanifesto.org/)

**Conceitos:** Quatro perguntas: o que estamos construindo, o que pode dar errado, o que faremos a respeito, fizemos um bom trabalho; Valores: cultura de encontrar e corrigir problemas de design acima de conformidade de checklist; Análise cedo e frequente, em iterações.

Página lida em 2026-10-23. Licença declarada: Creative Commons Attribution 4.0 International (CC BY 4.0).

Módulos: M04, M12 · Leitura: Essencial (prioridade 1).

## Data Security

### Resolução CD/ANPD nº 15, de abril de 2024 — Regulamento de Comunicação de Incidente de Segurança

`ANPD-RES-15-2024` · ANPD · Abril de 2024 · Leitura online gratuita · redistribuição: não verificada · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://www.mattosfilho.com.br/unico/regulamento-incidente-seguranca/)

**Conceitos:** Comunicação à ANPD e ao titular em três dias úteis; Critérios de risco ou dano relevante; Registro de incidentes por no mínimo cinco anos.

Conteúdo conferido em resumo de escritório de advocacia (Mattos Filho), não no texto oficial: três dias úteis para comunicar a ANPD e os titulares, contados do conhecimento de que o incidente afetou dados pessoais; complementação em até 20 dias úteis; prazos em dobro para agentes de pequeno porte; critérios cumulativos de relevância; registro de todos os incidentes por pelo menos cinco anos. Conferir no texto oficial antes de citar literalmente.

Módulos: M03, M13, M15 · Leitura: Consulta (prioridade 2).

### Resolução CD/ANPD nº 19, de 23 de agosto de 2024 — Regulamento de Transferência Internacional de Dados

`ANPD-RES-19-2024` · ANPD · Agosto de 2024 · Leitura online gratuita · redistribuição: não verificada · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://lefosse.com/noticias/alerta/transferencia-internacional-de-dados-prazo-para-adocao-das-clausulas-padrao-da-anpd-se-encerra-em-23-de-agosto/)

Conteúdo conferido em alerta de escritório de advocacia (Lefosse), não no texto oficial: prazo para adoção das cláusulas-padrão encerrado em 23/08/2025; mecanismos de adequação, cláusulas-padrão, cláusulas específicas e normas corporativas globais; cláusulas próprias ou estrangeiras precisam ser substituídas ou aprovadas. Conferir no texto oficial antes de citar literalmente.

Módulos: M11, M13 · Leitura: Consulta (prioridade 2).

### AWS Key Management Service — Developer Guide (overview e concepts)

`AWS-KMS` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)

Páginas overview e concepts lidas em 2026-10-23: chaves protegidas por HSMs validados FIPS 140-3 nível 3, nunca saem do KMS sem cifragem; chaves gerenciadas pelo cliente (política exclusiva do cliente, rotação opcional), gerenciadas pela AWS (rotação anual) e de propriedade da AWS. Também lidas em 2026-10-23: key-policies.html (política de chave como forma principal de controle; exatamente uma por chave; sem permissão na política de chave, políticas IAM que permitem não têm efeito; política padrão habilita IAM; políticas de chave são regionais), kms-cryptography.html (cifragem envelope, root key) e a referência da API GenerateDataKey (retorna cópia em claro e cópia cifrada; apagar a cópia em claro da memória após o uso; guardar a cifrada com os dados). rotate-keys.html lida em 2026-10-23: o KMS retém todo o material de chave anterior e escolhe a versão correta ao decifrar; rotação automática só para chaves simétricas gerenciadas pelo cliente com material gerado pelo KMS; período padrão de 365 dias, configurável; chaves gerenciadas pela AWS rotacionam anualmente.

Módulos: M09, M11, M13 · Leitura: Consulta (prioridade 2).

### External key stores — AWS KMS Developer Guide

`AWS-KMS-XKS` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html)

Página lida em 2026-10-23: cifragem dupla; cliente responde por disponibilidade, durabilidade e latência; revogação torna o texto cifrado irrecuperável; a AWS afirma que, para a maioria dos clientes, o risco de disponibilidade e latência supera o benefício percebido; RTT recomendado de até 35 ms.

Módulos: M11, M13 · Leitura: Consulta (prioridade 3).

### What is Amazon Macie?

`AWS-MACIE` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)

Página lida em 2026-10-23: identificadores gerenciados e personalizados; achados de dados sensíveis e de política.

Módulos: M09, M13 · Leitura: Consulta (prioridade 3).

### What is AWS Secrets Manager?

`AWS-SECRETS-MANAGER` · AWS · Documentação online; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

Página lida em 2026-10-23: substitui credenciais embutidas por chamada em tempo de execução; rotação automática (gerenciada ou por Lambda); cifragem com KMS. Página rotating-secrets.html lida em 2026-10-23: rotação gerenciada sem Lambda para a maioria dos segredos gerenciados; rotação externa gerenciada para parceiros; rotação por função Lambda para os demais.

Módulos: M09, M11 · Leitura: Consulta (prioridade 3).

### CA/Browser Forum — Ballot SC081v3: Introduce Schedule of Reducing Validity and Data Reuse Periods

`CABF-SC081` · CA/Browser Forum · Aprovada; votação encerrada em 11/04/2025 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/)

Página oficial conferida: aprovada (emissores 25 sim, 0 não, 5 abstenções; consumidores 4 sim); validade máxima de 398 dias para 47 dias, com reduções de março de 2026 a março de 2029. Etapas intermediárias não exibidas na página; conferidas na base de conhecimento da DigiCert (fonte secundária): 200 dias a partir de 15/03/2026, 100 dias a partir de 15/03/2027 e 47 dias a partir de 15/03/2029.

Módulos: M01, M13 · Leitura: Consulta (prioridade 2).

### Cloud External Key Manager

`GCP-CLOUD-EKM` · Google Cloud · Atualizado em 22/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/kms/docs/ekm)

Página lida em 2026-10-23: chave nunca enviada ao Google; perda de acesso à chave pode tornar dados irrecuperáveis; preferir EKM via VPC para disponibilidade; parceiros Fortanix, Futurex e Thales.

Módulos: M11, M13 · Leitura: Consulta (prioridade 3).

### Overview of VPC Service Controls

`GCP-VPC-SC` · Google Cloud · Atualizado em 22/10/2026 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.cloud.google.com/vpc-service-controls/docs/overview)

Página lida em 2026-10-23: perímetros em torno de recursos; níveis de acesso; regras de entrada e saída; modo dry-run; complementa o IAM, com recomendação de usar ambos.

Módulos: M10, M13 · Leitura: Consulta (prioridade 3).

### Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD), texto compilado

`LGPD-L13709` · Presidência da República (Planalto) · Texto compilado com alterações até a Lei nº 15.352, de 2026 · Leitura online gratuita · redistribuição: permitida pela licença · Verificada em 2026-10-23 · [abrir fonte oficial](https://planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Art. 5º, II | Definição de dado pessoal sensível | M13 | **Lido** |
| Art. 6º | Princípios (finalidade, adequação, necessidade, livre acesso, qualidade, transparência, segurança, prevenção, não discriminação, responsabilização) | M03, M13 | **Lido** |
| Art. 7º | Bases legais para tratamento | M13 | **Lido** |
| Art. 46 | Medidas de segurança técnicas e administrativas | M03, M13 | **Lido** |
| Art. 48 | Comunicação de incidente de segurança à ANPD e ao titular | M03, M13, M15 | **Lido** |
| Art. 50 | Boas práticas e programa de governança em privacidade | M03, M13 | **Lido** |

Texto oficial do Planalto conferido. Sem licença aplicável: a Lei nº 9.610/1998, art. 8º, IV (texto do Planalto conferido em 2026-10-23), exclui da proteção autoral 'os textos de tratados ou convenções, leis, decretos, regulamentos, decisões judiciais e demais atos oficiais'.

Módulos: M03, M13, M16 · Leitura: Essencial (prioridade 1).

### What is data security posture management (DSPM)?

`MS-WHAT-IS-DSPM` · Microsoft · Página Security 101; data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.microsoft.com/en-us/security/business/security-101/what-is-data-security-posture-management-dspm)

Página lida em 2026-10-23. Texto de fornecedor.

Módulos: M11, M13 · Leitura: Consulta (prioridade 3).

### FIPS 203 — Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM)

`NIST-FIPS-203` · NIST · Final (13/08/2024); relacionados FIPS 204, FIPS 205 e SP 800-227 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/fips/203/final)

**Conceitos:** FIPS 203 (ML-KEM, encapsulamento de chaves); FIPS 204 (Module-Lattice-Based Digital Signature Standard); FIPS 205 (Stateless Hash-Based Digital Signature Standard).

Páginas oficiais conferidas: FIPS 203, 204 (Module-Lattice-Based Digital Signature Standard) e 205 (Stateless Hash-Based Digital Signature Standard), todos de 13/08/2024. Nota de planejamento de 17/11/2025 sobre errata do FIPS 203.

Módulos: M01, M13 · Leitura: Consulta (prioridade 2).

### NIST IR 8547 — Transition to Post-Quantum Cryptography Standards (Initial Public Draft)

`NIST-IR-8547` · NIST · Initial Public Draft (12/11/2024); sem versão final mencionada · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/ir/8547/ipd)

Página conferida: rascunho público; comentários encerrados em 10/01/2025. Datas propostas de descontinuação não foram lidas. Tratar como proposta, não como requisito.

Módulos: M01, M13 · Leitura: Consulta (prioridade 3).

### SP 1800-16 — Securing Web Transactions: TLS Server Certificate Management

`NIST-SP1800-16` · NIST NCCoE · Final (16/06/2020), volumes A–D · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/1800/16/final)

Página oficial conferida: volumes A (resumo executivo), B (riscos e boas práticas), C (arquitetura) e D (guias). Conteúdo não lido.

Módulos: M01, M13 · Leitura: Aprofundada (prioridade 2).

### SP 800-57 Part 1 Rev. 5 — Recommendation for Key Management: Part 1 – General

`NIST-SP800-57-PT1-R5` · NIST · Rev. 5, final (04/05/2020) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)

Página oficial conferida; sem revisão mais nova mencionada; substitui a Rev. 4 (2016). Conteúdo interno não lido nesta revisão.

Módulos: M01, M13 · Leitura: Essencial (prioridade 1).

## Operational Resilience

### Reliability Pillar — AWS Well-Architected Framework (design principles)

`AWS-WA-RELIABILITY` · AWS · Página viva — data não exibida · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html)

**Conceitos:** Automatically recover from failure; Test recovery procedures; Scale horizontally; Stop guessing capacity; Manage change through automation.

Cinco princípios de design conferidos na página.

Módulos: M00, M09, M15 · Leitura: Consulta (prioridade 3).

### CIS Benchmarks

`CIS-BENCHMARKS` · Center for Internet Security · Catálogo vivo; FAQ consultado em 2026-10-23 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.cisecurity.org/cis-benchmarks)

FAQ oficial lido: processo de consenso; mais de 100 benchmarks em mais de 25 famílias de produtos (o próprio site cita mais de 140 tecnologias em outro trecho); Level 1 de baixo impacto, Level 2 para defesa em profundidade, perfil STIG substitui o antigo Level 3; PDFs gratuitos, outros formatos para membros. Termos de uso não verificados.

Módulos: M08, M09, M10 · Leitura: Consulta (prioridade 2).

### #StopRansomware Guide

`CISA-STOPRANSOMWARE-GUIDE` · CISA, FBI, NSA e MS-ISAC · Setembro de 2023 (atualiza o guia CISA/MS-ISAC de setembro de 2020) · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://www.cisa.gov/stopransomware/ransomware-guide)

Página lida em 2026-10-23: backups offline e cifrados, testados; golden images; IaC versionado; armazenamento imutável com cautela; vetores iniciais (serviços expostos, credenciais, phishing, malware precursor, terceiros); checklist de resposta em quatro fases. Documento do governo dos EUA; contatos de notificação são dos EUA.

Módulos: M08, M15 · Leitura: Essencial (prioridade 1).

### MITRE ATT&CK

`MITRE-ATTACK` · MITRE · v20 (outubro de 2026) · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://attack.mitre.org/)

Página de atualizações conferida: versão atual v20, de 13/10/2026. Página de táticas Enterprise lida em 2026-10-23 (conteúdo v20.0): 15 táticas — Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Stealth (TA0005), Defense Impairment (TA0112), Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact. Termos de uso (página Legal & Branding) não verificados. Técnicas conferidas nas páginas da v20: T1133 External Remote Services (Persistence, Initial Access), T1078 Valid Accounts (Stealth, Persistence, Privilege Escalation, Initial Access), T1003 OS Credential Dumping, T1087 Account Discovery, T1021 Remote Services, T1685 Disable or Modify Tools (Defense Impairment, 18 técnicas), T1490 Inhibit System Recovery e T1486 Data Encrypted for Impact (Impact). T1558 Steal or Forge Kerberos Tickets (Credential Access) conferida, com subtécnicas .001 Golden Ticket, .002 Silver Ticket, .003 Kerberoasting, .004 AS-REP Roasting e .005 Ccache Files.

Módulos: M03, M04, M06, M14, M15 · Leitura: Consulta (prioridade 3).

### NIST IR 8374 Rev. 1 — Ransomware Risk Management: A Cybersecurity Framework 2.0 Community Profile

`NIST-IR-8374-R1` · NIST · Rev. 1, final (11/06/2026); substitui a IR 8374 (2022) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/ir/8374/r1/final)

Página oficial conferida em 2026-10-23. Conteúdo do perfil não lido.

Módulos: M03, M08, M15 · Leitura: Consulta (prioridade 2).

### SP 1800-11 — Data Integrity: Recovering from Ransomware and Other Destructive Events

`NIST-SP1800-11` · NIST NCCoE · Final · Download gratuito · redistribuição: não verificada · Parcialmente verificada em 2026-10-23 · [abrir fonte oficial](https://www.nccoe.nist.gov/projects/building-blocks/data-integrity/recover)

Página do projeto conferida em 2026-10-23: recuperação de sistemas operacionais, bancos, arquivos, aplicações e configurações com dados precisos, completos e livres de malware; projetos irmãos de identificar/proteger e detectar/responder. Ano registrado por conhecimento prévio — a página não exibe a data.

Módulos: M08 · Leitura: Consulta (prioridade 3).

### SP 800-128 — Guide for Security-Focused Configuration Management of Information Systems

`NIST-SP800-128` · NIST · Agosto de 2011, atualizações de 10/10/2019 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-128.pdf)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Sec. 2 (p. 7–12) | Fundamentos de SecCM: definição, quatro fases, baseline, comitê de controle de configuração | M08 | **Lido** |

PDF lido em 2026-10-23 (Sec. 2 e início da Sec. 3). Autores registrados por conhecimento prévio, não conferidos.

Módulos: M08, M14 · Leitura: Consulta (prioridade 2).

### SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems

`NIST-SP800-34-R1` · NIST · Rev. 1, maio de 2010, atualizada em 11/11/2010 · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final)

| Localização | Título | Módulos | Situação |
|:---|:---|:---|:---|
| Cap. 3 (p. 13) | Processo de planejamento de contingência em sete etapas | M03 | **Lido** |
| Sec. 3.2 (p. 15–19) | Business Impact Analysis — processos e criticidade, requisitos de recursos, prioridades de recuperação; definições de MTD, RTO e RPO | M03, M12 | **Lido** |
| Sec. 2.2 (p. 8–11) | Tipos de plano (BCP, COOP, comunicação de crise, CIP, resposta a incidentes, DRP, ISCP, OEP) | M03, M12, M15 | **Lido** |

Página oficial conferida; nenhuma revisão mais nova mencionada. Escrito para sistemas federais dos EUA; conceitos de BIA, RTO e RPO são amplamente reutilizados. PDF lido em 2026-10-23 (Cap. 2–3): o RTO normalmente precisa ser menor que o MTD, e o RPO não faz parte do MTD (Sec. 3.2.1, p. 17).

Módulos: M00, M03, M08, M15 · Leitura: Consulta (prioridade 2).

### SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile

`NIST-SP800-61-R3` · NIST · Final, 03/04/2025; substitui a Rev. 2 (2012) · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

Página da publicação conferida em 2026-10-23 (título, data, autores, resumo, substituição da Rev. 2). Conteúdo do documento não lido.

Módulos: M09, M15 · Leitura: Consulta (prioridade 2).

### SP 800-70 Rev. 5 — National Checklist Program for IT Products: Guidelines for Checklist Users and Developers

`NIST-SP800-70-R5` · NIST · Rev. 5, final (08/05/2026); substitui a Rev. 4 (2018) · Download gratuito · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/70/r5/final)

Página oficial conferida em 2026-10-23: checklists com instruções, procedimentos ou conteúdo executável para configurar, verificar, detectar mudanças não autorizadas e produzir evidência de postura. Mudanças em relação à Rev. 4 não descritas na página.

Módulos: M08 · Leitura: Consulta (prioridade 3).

### SP 800-92 — Guide to Computer Security Log Management

`NIST-SP800-92` · NIST · Final, 13/09/2006 · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://csrc.nist.gov/pubs/sp/800/92/final)

Página da publicação conferida em 2026-10-23 (título, data, autores, resumo). Documento de 2006; verificar status de revisão antes de citar como prática atual. Conteúdo não lido.

Módulos: M09, M15 · Leitura: Consulta (prioridade 3).

### Understanding the Open Cybersecurity Schema Framework

`OCSF-UNDERSTANDING` · OCSF Project · Documento no repositório ocsf-docs (branch main) · Leitura online gratuita · redistribuição: não verificada · Verificada em 2026-10-23 · [abrir fonte oficial](https://github.com/ocsf/ocsf-docs/blob/main/overview/understanding-ocsf.md)

Documento lido em 2026-10-23: categorias System Activity, Network Activity, Identity & Access Management, Findings, Discovery e Application Activity; agnóstico a formato de armazenamento e ETL.

Módulos: M11, M15 · Leitura: Consulta (prioridade 3).

<!-- frameworks:end -->
