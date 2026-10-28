---
id: M02
title: "Módulo 2 — Introdução à Arquitetura de Segurança"
description: O ofício do arquiteto de segurança, níveis de abstração, princípios e padrões, arquiteturas de referência, frameworks, requisitos orientados ao negócio e ADRs.
stage: n1
status: published
prerequisites: [M00, M01]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
---

# Módulo 2 — Introdução à Arquitetura de Segurança { #modulo-02-introducao-a-arquitetura-de-seguranca }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 1 — Fundamentos de Arquitetura</span>
<span class="saa-meta">8 aulas · cerca de 10 h de aulas</span>
<span class="saa-status saa-status--published">Published</span>
</div>

## Resumo

!!! abstract "Sobre este módulo"

    Este é o módulo que transforma o especialista técnico em alguém que **pensa como arquiteto**. Ele não ensina uma tecnologia: ensina a perguntar *para quê*, *contra quê*, *em que nível de abstração* e *com que custo* — e a registrar as respostas de modo que outras pessoas possam entender, reutilizar e contestar a decisão.

Ao concluir o módulo, você será capaz de:

- Descrever o papel, as entregas e os limites de responsabilidade de um Security Architect.
- Situar a arquitetura de segurança em relação à arquitetura corporativa e à arquitetura de soluções.
- Representar uma solução nas visões conceitual, lógica e física, sem misturar os níveis.
- Organizar princípios, padrões, baselines, controles e exceções em uma hierarquia coerente.
- Usar arquiteturas de referência e blueprints sem copiá-los cegamente.
- Escolher entre NIST, SABSA e TOGAF conforme o propósito, e entender o que CISSP e ISSAP avaliam.
- Derivar requisitos de segurança verificáveis a partir de objetivos de negócio.
- Documentar decisões em Architecture Decision Records com alternativas e consequências.

## Pré-requisitos

| Pré-requisito | Por quê | Como validar |
|:---|:---|:---|
| Módulo Inicial — Fundamentos de infraestrutura | As aulas usam diagramas com redes, cloud, APIs e identidade. | Seção A da [avaliação diagnóstica](../../assessments/diagnostic-fundamentals.md) |
| Módulo 1 — Fundamentos de segurança | Princípios, trust boundaries, risco e tipos de controle são o vocabulário do módulo. | Seções B e C da avaliação diagnóstica |

Profissionais com experiência em Vulnerability Management, pentest, AppSec ou infraestrutura geralmente dominam esses fundamentos na prática. A avaliação diagnóstica serve para confirmar isso e apontar lacunas pontuais antes do módulo.

## Aulas

<!-- lessons:start -->

| Aula | Tema | Profundidade | Duração |
|:---|:---|:---|:---|
| [Aula 01](01-security-architect-role.md) | O papel do Security Architect | Fundamental | 60 min |
| [Aula 02](02-enterprise-solution-security-architecture.md) | Enterprise, Solution e Security Architecture | Fundamental | 60 min |
| [Aula 03](03-conceptual-logical-physical.md) | Arquitetura conceitual, lógica e física | Professional | 75 min |
| [Aula 04](04-principles-standards-baselines-exceptions.md) | Princípios, padrões, baselines e exceções | Professional | 75 min |
| [Aula 05](05-reference-architectures-blueprints.md) | Arquiteturas de referência e blueprints | Professional | 60 min |
| [Aula 06](06-frameworks.md) | Frameworks, padrões e certificações: NIST, SABSA, TOGAF, CISSP e ISSAP | Professional | 90 min |
| [Aula 07](07-business-driven-requirements.md) | Business-driven Security Architecture: de requisitos de negócio a requisitos de segurança | Architect | 90 min |
| [Aula 08](08-architecture-decision-records.md) | Architecture Decision Records | Architect | 75 min |

<!-- lessons:end -->

## Atividades do módulo

| Atividade | Competências | Tempo estimado |
|:---|:---|:---|
| [Laboratório 02 — Modelagem arquitetural como código](../../labs/lab-02-architecture-modeling.md) | C3, C4, C6, C8 | 2 a 3 h |
| [Caso A — Meridiana Distribuidora](../../case-studies/case-a-meridiana/index.md) | C1 a C10 | 4 a 6 h |
| [Avaliação do Módulo 2](../../assessments/m02-security-architecture.md) | C1, C2, C5, C6, C8 | 90 min |
| [Avaliação integradora do Módulo Inicial ao Módulo 2 — Livraria Ipê](../../assessments/fundamentals-final.md) | Integra Módulo Inicial, Módulo 1 e Módulo 2 | 3 a 4 h |

## Mapa do módulo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-module-map.mmd"
```

<figcaption>Figura 1 — Mapa do Módulo 2.</figcaption>
</figure>

## Organizações fictícias usadas no módulo

As aulas usam as mesmas organizações para que os exemplos se acumulem em vez de recomeçar a cada aula. Todas são fictícias.

| Organização | Perfil | Onde aparece |
|:---|:---|:---|
| **Aurora Pagamentos** | Instituição de pagamento de médio porte; datacenter próprio, workloads em AWS, identidade em Active Directory sincronizado com Microsoft Entra ID; sujeita a PCI DSS e LGPD. | Aulas 01, 03, 04, 07 e 08 |
| **Grupo Horizonte** | Holding com quatro subsidiárias (varejo, logística, saúde ocupacional e serviços financeiros), cada uma com tecnologia própria. | Aulas 02, 05 e 06 |
| **Meridiana Distribuidora** | Distribuidora com datacenter tradicional, Active Directory, servidores Windows e Linux e acesso remoto por VPN. | Laboratório 02 e Caso A |

## Referências principais do módulo

- ISO/IEC/IEEE. *42010:2022 — Architecture description*. <https://committee.iso.org/standard/74393.html> — norma paga, não consultada na íntegra; a descrição usada nesta aula se apoia na página oficial da norma e em resumos públicos.
- NIST. *SP 800-160 Vol. 1 Rev. 1 — Engineering Trustworthy Secure Systems*. 2022. <https://csrc.nist.gov/news/2022/guidance-on-engineering-trustworthy-secure-systems> — gratuito.
- NIST. *Cybersecurity Framework 2.0 (CSWP 29)*. 2024. <https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final> — gratuito.
- The Open Group. *TOGAF Series Guide: Integrating Risk and Security within a TOGAF Enterprise Architecture*. <https://pubs.opengroup.org/togaf-standard/integrating-risk-and-security/index.html> — leitura online gratuita.
- M. Nygard. *Documenting Architecture Decisions*. 2011. <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions> — gratuito.

Registro completo em [Fontes e recursos](../../resources/index.md).
