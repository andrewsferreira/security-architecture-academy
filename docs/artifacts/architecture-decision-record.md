---
id: ART-ADR
title: "Modelo: Architecture Decision Record"
description: Modelo editável de ADR com extensões para segurança — decisores, requisitos relacionados, alternativas, risco residual com dono, verificação e data de revisão.
status: published
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# Modelo: Architecture Decision Record

Baseado no formato de Michael Nygard (título, contexto, decisão, status e consequências), com extensões para decisões de segurança. Fundamentos e exemplos comentados na [Aula 08 do Módulo 2](../modules/02-security-architecture/08-architecture-decision-records.md).

## Modelo

```markdown
# ADR-<NNN> — <Frase curta que nomeia a decisão, não o produto>

**Status:** <Proposta | Aceita | Depreciada | Substituída por ADR-NNN>
**Data:** <AAAA-MM-DD>
**Decisores:** <papéis ou nomes>
**Consultados:** <papéis ou áreas ouvidas>

## Contexto

<Forças em jogo — técnicas, de negócio, regulatórias, de equipe e de prazo —
descritas de forma factual, inclusive quando conflitam. Cite ADRs anteriores
que formam o contexto.>

## Requisitos e riscos relacionados

- <REQ-ID: requisito que a decisão atende>
- <Ameaça ou risco tratado>

## Alternativas consideradas

| Critério | Peso | <Alternativa A> | <Alternativa B> | <Alternativa C> |
|:---|:---|:---|:---|:---|
| <critério> | <1–3> | <1–3> | <1–3> | <1–3> |

<Resumo de por que cada alternativa foi ou não escolhida.>

## Decisão

<Em voz ativa: "Vamos…". Específica o suficiente para ser verificada.>

## Consequências

- **Positivas:** <efeitos desejados>
- **Negativas:** <custos, limitações e novos riscos — obrigatório>
- **Neutras:** <efeitos sem valoração clara>

## Risco residual

<O que permanece após a decisão.> **Dono do risco:** <papel com autoridade para aceitá-lo>

## Verificação

<Como confirmar que a decisão foi implementada como decidida: testes,
regras de política, revisões.>

## Revisão

<Data ou gatilho para revisitar a decisão.>

## Relacionamentos

- <Substitui / é substituída por / complementa ADR-NNN>
- <Exceção EXC-NNN associada, se houver>
```

## Orientação por campo

| Campo | Pergunta que responde | Erro comum |
|:---|:---|:---|
| Título | Que decisão foi tomada? | Nomear um produto em vez da decisão |
| Contexto | Por que foi preciso decidir, e sob quais restrições? | Contexto de uma linha, sem forças em conflito |
| Requisitos e riscos | O que a decisão precisa atender? | Decisão sem rastreabilidade |
| Alternativas | Que outras opções existiam e como foram comparadas? | Uma alternativa só, ou alternativas de fachada |
| Decisão | O que exatamente será feito? | Texto vago, impossível de verificar |
| Consequências | O que muda — inclusive para pior? | Só consequências positivas |
| Risco residual | O que fica, e quem aceitou? | "Risco aceito" sem dono |
| Verificação | Como saber se foi feito? | Ausente |
| Revisão | Quando revisitar? | Decisões temporárias tratadas como permanentes |

## Regras do registro

- Numere sequencialmente e nunca reutilize números.
- ADRs aceitos não são editados no conteúdo; mudanças geram um novo ADR que substitui o anterior.
- Mantenha cada ADR com uma ou duas páginas, em frases completas.
- Guarde os ADRs junto do código ou da infraestrutura que implementam a decisão.

## Exemplos preenchidos

- [ADR-001 — Acesso remoto da Meridiana Distribuidora](../case-studies/case-a-meridiana/adr-001-remote-access.md)
- [ADR-002 — Segmentação do datacenter da Meridiana](../case-studies/case-a-meridiana/adr-002-segmentation.md)
- [ADR-003 — Centralização de logs da Meridiana](../case-studies/case-a-meridiana/adr-003-logging.md)
- [ADR-012 da Aurora Pagamentos](../modules/02-security-architecture/08-architecture-decision-records.md#exemplo-empresarial), na Aula 08 do Módulo 2
