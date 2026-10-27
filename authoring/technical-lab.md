---
id: LAB-00
title: "{{ Título }}"
description: "{{ Uma frase, até ~160 caracteres }}"
domain: "{{ id-do-dominio }}"
tier: "{{ fundamental | professional | architect }}"
status: draft
prerequisites: []
objectives:
  - "{{ Objetivo verificável }}"
estimated_time: "{{ 90 min }}"
cost: "{{ Sem custo — execução local | custo estimado e serviços faturáveis }}"
tested: false                     # true somente após execução real registrada na página do laboratório
last_updated: "{{ AAAA-MM-DD }}"
reviewed_by: []
---

<!--
  Template: Technical Lab — 10 elementos obrigatórios
  Laboratórios demonstram aplicação arquitetural, não apenas administração de ferramentas.
  Execução local e gratuita por padrão; cloud apenas como opção, com custos e limpeza descritos.
-->

# {{ Título }}

## Resumo

!!! danger "Ambiente isolado"

    Execute este laboratório apenas em ambiente próprio e isolado, criado para estudo. Use somente dados sintéticos.

| Item | Valor |
|:---|:---|
| Tempo estimado | {{ }} |
| Custo | {{ }} |
| Status de teste | {{ Executado em AAAA-MM-DD / Não executado }} |

## Objetivo

- {{ Objetivo }}

## Cenário empresarial

{{ Organização fictícia e demanda de negócio }}

## Requisitos

| Item | Versão | Observação |
|:---|:---|:---|
| {{ Ferramenta }} | {{ }} | {{ Gratuito/pago }} |

## Arquitetura inicial

{{ Diagrama e descrição do ponto de partida }}

## Passo a passo

### 1. {{ Etapa }}

```bash
{{ comando }}
```

**Resultado esperado:** {{ }}

## Critérios de validação

- [ ] {{ Critério verificável }}

## Evidências esperadas

{{ Saídas, arquivos e artefatos que comprovam a conclusão }}

## Perguntas arquiteturais

1. {{ Pergunta }}

## Explicação do resultado

??? success "Explicação"

    {{ O que o resultado demonstra e como se conecta às decisões de arquitetura }}

## Desmontagem

{{ Como remover tudo o que foi criado }}

## Referências

- {{ Referência }}

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | {{ @github-handle }} |
| Revisão técnica | {{ @github-handle }} — {{ AAAA-MM-DD }} |
| Última execução de teste | {{ AAAA-MM-DD }} |
