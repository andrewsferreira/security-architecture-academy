---
id: ADR-000
title: "{{ Título }}"
description: "{{ Uma frase, até ~160 caracteres, usada em SEO e compartilhamento }}"
domain: "{{ id-do-dominio }}"        # ver curriculum/manifest.yml → domains
tier: "{{ fundamental | professional | architect }}"
status: draft                     # planned | draft | in-review | published | deprecated
prerequisites: []                 # ids, ex.: [M01-L01]
objectives:
  - "{{ Verbo observável + conteúdo, ex.: Explicar o papel do PEP em uma arquitetura Zero Trust }}"
last_updated: "{{ AAAA-MM-DD }}"
reviewed_by: []                   # GitHub handles; obrigatório para publicar
decision_status: "{{ proposed | accepted | superseded | rejected }}"
decided_on: "{{ AAAA-MM-DD }}"
---

<!--
  Template: Architecture Decision Record
  Copie para docs/ conforme docs/internal/content-model.md.
  Substitua todos os marcadores {{ … }} — o CI bloqueia a publicação de páginas que ainda os contenham.
-->

# {{ Título }}

## Resumo

{{ Decisão em uma frase }}

## Contexto

{{ Forças, requisitos e restrições que motivam a decisão }}

## Opções consideradas

1. {{ Opção A }}
2. {{ Opção B }}

## Decisão

{{ Opção escolhida e justificativa }}

## Consequências

- **Positivas:** {{ }}
- **Negativas:** {{ }}
- **Riscos aceitos:** {{ }}

## Diagramas

<!-- Opcional. -->

## Conformidade

{{ Como verificar que a decisão está sendo seguida }}

## Referências

<!-- Formato: Organização. *Título*. Versão/ano. <link> — gratuito | pago. Ver docs/internal/style-guide.md -->

- {{ Referência }}

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | {{ @github-handle }} |
| Revisão técnica | {{ @github-handle }} — {{ AAAA-MM-DD }} |
| Última atualização | {{ AAAA-MM-DD }} |
| Próxima revisão prevista | {{ AAAA-MM-DD }} |
