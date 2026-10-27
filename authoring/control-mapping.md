---
id: M00-CM00
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
frameworks: ["{{ NIST SP 800-53 Rev. 5 }}", "{{ ISO/IEC 27001:2022 }}"]
---

<!--
  Template: Control Mapping
  Copie para docs/ conforme docs/internal/content-model.md.
  Substitua todos os marcadores {{ … }} — o CI bloqueia a publicação de páginas que ainda os contenham.
-->

# {{ Título }}

## Resumo

{{ Objetivo do mapeamento e frameworks/versões comparados }}

## Metodologia

{{ Critério de equivalência: total, parcial, relacionado }}

## Mapeamento

| Objetivo de controle | {{ Framework A }} | {{ Framework B }} | Equivalência | Observações |
|:---|:---|:---|:---|:---|
| {{ Objetivo }} | {{ id }} | {{ id }} | {{ total/parcial }} | {{ }} |

## Lacunas

- {{ Lacuna identificada }}

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
