---
id: M00-TM00
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
methodology: "{{ STRIDE | LINDDUN | PASTA | outra }}"
---

<!--
  Template: Threat Model
  Copie para docs/ conforme docs/internal/content-model.md.
  Substitua todos os marcadores {{ … }} — o CI bloqueia a publicação de páginas que ainda os contenham.
-->

# {{ Título }}

## Resumo

{{ Sistema modelado e escopo }}

## Escopo e premissas

- **Dentro do escopo:** {{ }}
- **Fora do escopo:** {{ }}
- **Premissas:** {{ }}

## Diagrama de fluxo de dados

<!-- DFD com trust boundaries explícitos (subgraphs). -->

## Ativos

| Ativo | Classificação | Responsável |
|:---|:---|:---|
| {{ Ativo }} | {{ Classificação }} | {{ Papel }} |

## Ameaças

| ID | Ameaça | Categoria | Componente | Probabilidade | Impacto |
|:---|:---|:---|:---|:---|:---|
| T1 | {{ Ameaça }} | {{ }} | {{ }} | {{ }} | {{ }} |

## Mitigações

| Ameaça | Controle | Status |
|:---|:---|:---|
| T1 | {{ Controle }} | {{ Proposto/Implementado }} |

## Riscos residuais

- {{ Risco e decisão de tratamento }}

## Atividades

- {{ Exercício }}

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
