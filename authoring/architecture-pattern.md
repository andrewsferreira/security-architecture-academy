---
id: AP-000
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
---

<!--
  Template: Architecture Pattern
  Copie para docs/ conforme docs/internal/content-model.md.
  Substitua todos os marcadores {{ … }} — o CI bloqueia a publicação de páginas que ainda os contenham.
-->

# {{ Título }}

## Resumo

{{ O padrão em uma frase }}

## Problema

{{ Situação recorrente e forças em conflito }}

## Contexto de aplicação

- **Use quando:** {{ condição }}
- **Evite quando:** {{ condição }}

## Solução

{{ Descrição da estrutura e do comportamento }}

## Diagramas

<!-- Diagrama da estrutura do padrão, com trust boundaries. -->

## Controles envolvidos

| Controle | Objetivo | Referência |
|:---|:---|:---|
| {{ Controle }} | {{ Objetivo }} | {{ Framework e id }} |

## Trade-offs

| Benefício | Custo ou risco |
|:---|:---|
| {{ Benefício }} | {{ Custo }} |

## Padrões relacionados

- {{ Padrão }}

## Atividades

- {{ Exercício de aplicação }}

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
