---
id: ART-ARC
title: "Modelo: Architecture Review Checklist"
description: Checklist editável para revisão arquitetural de segurança, organizado por contexto, níveis de abstração, fronteiras, identidade, dados, resiliência, operação, decisões e ambientes híbridos.
status: published
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# Modelo: Architecture Review Checklist

Checklist para conduzir uma revisão arquitetural de segurança. Cada item admite três respostas — **Atende**, **Não atende** ou **Não se aplica** — e todo *Não atende* gera um achado com recomendação. O checklist consolida os itens das aulas do Módulo 02; módulos posteriores acrescentam seções específicas.

## Modelo

```markdown
# Revisão arquitetural — <Nome da solução>

**Data:** <AAAA-MM-DD> · **Revisor:** <papel> · **Nível de revisão:** <Leve | Completa>
**Documentos revisados:** <links>

| # | Item | Resultado | Evidência ou achado |
|:---|:---|:---|:---|
| **A. Contexto e requisitos** | | | |
| A1 | Objetivo de negócio, ativos e apetite a risco estão registrados e confirmados | <Atende/Não atende/N.A.> | |
| A2 | Requisitos de segurança são verificáveis e rastreáveis à origem | | |
| A3 | Restrições regulatórias e contratuais estão identificadas | | |
| **B. Representação** | | | |
| B1 | Há visões nos níveis adequados ao risco (conceitual, lógica, física) | | |
| B2 | Há rastreabilidade entre serviços, componentes lógicos e elementos físicos | | |
| B3 | A visão física corresponde ao ambiente real ou ao código de infraestrutura | | |
| **C. Fronteiras e fluxos** | | | |
| C1 | Zonas de confiança estão definidas e nomeadas pelo propósito | | |
| C2 | Todo fluxo que cruza uma fronteira de confiança é autenticado | | |
| C3 | Dados classificados como confidenciais são criptografados em trânsito entre zonas | | |
| C4 | Interfaces administrativas não são expostas a zonas de menor confiança | | |
| **D. Identidade e acesso** | | | |
| D1 | Pessoas e workloads se autenticam por serviços corporativos de identidade | | |
| D2 | Acesso privilegiado é temporário, aprovado e registrado | | |
| D3 | Autorização é verificada no recurso, não apenas na borda | | |
| **E. Dados** | | | |
| E1 | Dados estão classificados e seu fluxo entre zonas é conhecido | | |
| E2 | Retenção e eliminação atendem às obrigações | | |
| **F. Resiliência** | | | |
| F1 | Pontos únicos de falha dos componentes críticos estão identificados e tratados | | |
| F2 | Requisitos de disponibilidade e recuperação estão definidos e são compatíveis com o desenho | | |
| **G. Operação e detecção** | | | |
| G1 | Eventos de segurança relevantes são enviados ao SIEM | | |
| G2 | Há dono operacional para cada componente de segurança | | |
| **H. Padrões e decisões** | | | |
| H1 | A solução usa os serviços de segurança corporativos ou registra exceção | | |
| H2 | Decisões significativas estão em ADRs, com consequências negativas e risco residual | | |
| H3 | Exceções têm prazo, compensatórios e dono do risco | | |
| **I. Ambientes híbridos (quando aplicável)** | | | |
| I1 | Cada ponto de integração entre ambientes tem dono | | |
| I2 | Realizações físicas diferentes atendem aos mesmos requisitos lógicos | | |
| I3 | O comportamento em falha da integração está especificado | | |

## Achados

| ID | Item | Achado | Risco | Recomendação | Prazo |
|:---|:---|:---|:---|:---|:---|
| ACH-01 | <item> | <descrição> | <Alto/Médio/Baixo> | <recomendação> | <data> |

## Parecer

<Aprovado | Aprovado com condições | Não aprovado> — <justificativa>
```

## Como conduzir a revisão

1. **Antes da sessão:** leia os documentos e preencha o que puder com evidências.
2. **Na sessão:** percorra os itens *Não atende* e os duvidosos com a equipe; ouça o contexto antes de registrar o achado.
3. **Depois:** registre achados com risco e recomendação, e um parecer. Condições de aprovação viram itens com prazo.

## Exemplo preenchido

- [Análise do As-Is do Caso A — Meridiana](../case-studies/case-a-meridiana/solution.md#analise-do-as-is)
