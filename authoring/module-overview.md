---
id: M00
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
module: M00
---

<!--
  Template: Module Overview
  Copie para docs/ conforme docs/internal/content-model.md.
  Substitua todos os marcadores {{ … }} — o CI bloqueia a publicação de páginas que ainda os contenham.
-->

# {{ Título }}

## Resumo

<!-- 2–3 frases: o que o módulo cobre e por que importa para um arquiteto. -->

{{ Resumo }}

## Pré-requisitos

<!-- Módulos ou conhecimentos necessários, com links. -->

- {{ Pré-requisito }}

## Objetivos de aprendizagem

Ao concluir este módulo, você será capaz de:

- {{ Objetivo }}

## Mapa do módulo

<!-- Diagrama Mermaid (assets/diagrams/) mostrando a relação entre as aulas. -->

| Aula | Tema | Tipo |
|:---|:---|:---|
| `M00-L01` | {{ Tema }} | Technical Lesson |

## Conteúdo técnico

<!-- Visão geral dos conceitos centrais; o detalhamento fica nas aulas. -->

{{ Conteúdo }}

## Atividades

- {{ Laboratório, estudo de caso ou avaliação associados }}

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
