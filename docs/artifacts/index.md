---
title: Modelos de artefatos
description: Modelos editáveis de artefatos de arquitetura de segurança — ADR, especificação de requisitos, checklist de revisão, avaliação de arquitetura, threat model, matriz de controles, risk register e os demais previstos no currículo — com exemplos preenchidos.
---

# Modelos de artefatos

Modelos editáveis para os artefatos que um arquiteto de segurança produz. Cada modelo explica o propósito de cada campo e aponta um **exemplo preenchido** com organizações fictícias.

!!! tip "Como usar"

    Copie o bloco do modelo para o repositório da sua solução (por exemplo, `docs/adr/0001-titulo.md`) e substitua os textos entre `< >`. Os modelos funcionam em qualquer editor Markdown e são renderizados no GitHub.

| Modelo | Quando usar | Exemplo preenchido | Status |
|:---|:---|:---|:---|
| [Architecture Decision Record](architecture-decision-record.md) | Registrar uma decisão arquitetural significativa | [ADRs do Caso A](../case-studies/case-a-meridiana/adr-001-remote-access.md) | <span class="saa-status saa-status--published">Published</span> |
| [Security Requirements Specification](security-requirements-specification.md) | Especificar requisitos de segurança de uma solução | [Solução do Caso A](../case-studies/case-a-meridiana/solution.md#requisitos-de-seguranca) | <span class="saa-status saa-status--published">Published</span> |
| [Architecture Review Checklist](architecture-review-checklist.md) | Revisar uma arquitetura antes da aprovação | [Avaliação do As-Is do Caso A](../case-studies/case-a-meridiana/solution.md#analise-do-as-is) | <span class="saa-status saa-status--published">Published</span> |
| [Security Architecture Assessment](security-architecture-assessment.md) | Avaliar a arquitetura de segurança de uma organização ou ambiente | [Meridiana — avaliação parcial](security-architecture-assessment.md#exemplo-preenchido) | <span class="saa-status saa-status--published">Published</span> |
| [Threat Model](threat-model.md) | Documentar ameaças, mitigações e riscos de um sistema | [Integração de laudos da Lumen](threat-model.md#exemplo-preenchido) | <span class="saa-status saa-status--published">Published</span> |
| [Security Control Matrix](security-control-matrix.md) | Mapear controles a requisitos, riscos e frameworks | [Meridiana — RSK-007](security-control-matrix.md#exemplo-preenchido) | <span class="saa-status saa-status--published">Published</span> |
| [Risk Register](risk-register.md) | Registrar riscos, tratamento e donos | [Meridiana — RSK-007](risk-register.md#exemplo-preenchido) | <span class="saa-status saa-status--published">Published</span> |
| Hybrid Security Architecture Blueprint | Descrever o contrato de segurança entre ambientes | — | <span class="saa-status saa-status--planned">Planned</span> |
| Security Maturity Assessment | Avaliar maturidade de capacidades de segurança | — | <span class="saa-status saa-status--planned">Planned</span> |
| Vulnerability Management Program | Estruturar um programa corporativo de VM | — | <span class="saa-status saa-status--planned">Planned</span> |
| Security Architecture Roadmap | Planejar a evolução em 90 dias, 6 e 12 meses | — | <span class="saa-status saa-status--planned">Planned</span> |
| Executive Architecture Summary | Apresentar uma proposta para CISO e executivos | — | <span class="saa-status saa-status--planned">Planned</span> |
| Matriz RACI | Definir responsabilidades por atividade | — | <span class="saa-status saa-status--planned">Planned</span> |

Os modelos planejados serão produzidos junto com os módulos que os utilizam (Fases 2 e 3).
