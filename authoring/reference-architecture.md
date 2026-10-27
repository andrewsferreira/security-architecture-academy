---
id: RA-000
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
  Template: Reference Architecture
  Copie para docs/ conforme docs/internal/content-model.md.
  Substitua todos os marcadores {{ … }} — o CI bloqueia a publicação de páginas que ainda os contenham.
-->

# {{ Título }}

## Resumo

{{ Escopo e objetivo da arquitetura }}

## Requisitos

### Negócio

- {{ Requisito }}

### Segurança e conformidade

- {{ Requisito }}

## Premissas e restrições

- {{ Premissa }}

## Visão geral

<!-- Diagrama de contexto e diagrama de componentes. -->

## Componentes

| Componente | Responsabilidade | Zona de confiança |
|:---|:---|:---|
| {{ Componente }} | {{ Responsabilidade }} | {{ Zona }} |

## Fluxos de dados e trust boundaries

{{ Descrição dos fluxos críticos }}

## Controles por camada

| Camada | Controles |
|:---|:---|
| Identidade | {{ Controles }} |

## Decisões arquiteturais

- [ADR-000 — {{ Título }}]({{ link }})

## Riscos residuais

| Risco | Tratamento | Owner |
|:---|:---|:---|
| {{ Risco }} | {{ Tratamento }} | {{ Papel }} |

## Atividades

- {{ Exercício de adaptação a outro contexto }}

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
