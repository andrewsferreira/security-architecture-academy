---
id: CS-X
title: "{{ Título }}"
description: "{{ Uma frase, até ~160 caracteres }}"
domain: "{{ id-do-dominio }}"
tier: architect
status: draft
prerequisites: []
objectives:
  - "{{ Objetivo }}"
last_updated: "{{ AAAA-MM-DD }}"
reviewed_by: []
---

<!--
  Template: Case Study
  Estrutura em dois arquivos:
    index.md     — enunciado: contexto, restrições, As-Is, problemas e tarefas do estudante
    solution.md  — solução de referência: riscos, requisitos, alternativas, trade-offs, To-Be,
                   controles, plano, indicadores, decisões (ADRs), riscos residuais e rubrica
  Organizações, pessoas e dados são fictícios.
-->

# {{ Título }}

## Resumo

!!! note "Cenário fictício"

    Organizações, pessoas e dados deste estudo são fictícios.

{{ Resumo do caso }}

## Contexto e objetivos de negócio

{{ Setor, porte, ambiente tecnológico e objetivos }}

## Restrições técnicas, financeiras e operacionais

- {{ Restrição }}

## Arquitetura As-Is

{{ Diagrama e descrição }}

## Problemas e ameaças

- {{ Problema }}

## Tarefas do estudante

1. {{ Tarefa e artefato esperado }}

## Rubrica de avaliação

| Critério | Peso | Excelente | Adequado | Insuficiente |
|:---|:---|:---|:---|:---|
| {{ }} | {{ }} | {{ }} | {{ }} | {{ }} |

## Referências

- {{ Referência }}

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | {{ @github-handle }} |
| Revisão técnica | {{ @github-handle }} — {{ AAAA-MM-DD }} |
| Última atualização | {{ AAAA-MM-DD }} |
