---
id: M00-L00
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
  Template: Concept Explanation
  Copie para docs/ conforme docs/internal/content-model.md.
  Substitua todos os marcadores {{ … }} — o CI bloqueia a publicação de páginas que ainda os contenham.
-->

# {{ Título }}

## Resumo

{{ Definição em uma frase }}

## Definição

{{ Definição precisa, com fonte normativa quando existir }}

## Por que importa

{{ Impacto em decisões de arquitetura }}

## Conteúdo técnico

{{ Explicação aprofundada }}

## Exemplo

!!! example "Cenário"

    {{ Exemplo fictício e realista }}

## Diagramas

<!-- Opcional, quando o conceito tiver estrutura espacial ou sequencial. -->

## Conceitos relacionados

- [{{ Conceito }}]({{ link-relativo.md }})

## Atividades

- {{ Pergunta de verificação }}

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
