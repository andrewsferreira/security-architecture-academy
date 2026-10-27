---
id: M00-L00
title: "{{ Título }}"
description: "{{ Uma frase, até ~160 caracteres, usada em SEO e compartilhamento }}"
domain: "{{ id-do-dominio }}"        # ver curriculum/manifest.yml → domains
tier: "{{ fundamental | professional | architect }}"
status: draft                     # planned | draft | in-review | published | deprecated
prerequisites: []                 # ids, ex.: [M01-L02]
objectives:
  - "{{ Verbo observável + conteúdo, ex.: Explicar o papel do PEP em uma arquitetura Zero Trust }}"
minutes: 60
sources: []                       # IDs de research/bibliography.yml que sustentam o texto (somente Verified)
further_reading: []               # IDs de leituras complementares
last_updated: "{{ AAAA-MM-DD }}"
reviewed_by: []                   # GitHub handles; obrigatório para publicar
module: M00
---

<!--
  Template: Technical Lesson — padrão obrigatório de aula (14 elementos)
  Copie para docs/modules/<NN>-<slug>/ conforme docs/internal/content-model.md.
  Substitua todos os marcadores {{ … }} — o CI bloqueia a revisão e a publicação de páginas que os contenham.

  Sequência pedagógica obrigatória para cada conceito central:
   1 O que é? · 2 Por que existe? · 3 Qual problema resolve? · 4 Como funciona? · 5 Como se relaciona?
   6 Onde se aplica? · 7 Como especificar? · 8 Trade-offs? · 9 Como validar? · 10 Como justificar?
-->

# {{ Título }}

<div class="saa-lesson-meta" markdown>
<span class="saa-level">{{ Nível N }}</span>
<span class="saa-tier saa-tier--{{ tier }}">{{ Profundidade }}</span>
<span class="saa-meta">{{ 60 }} min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    {{ 2–3 frases: o problema que a aula resolve e o que o estudante será capaz de fazer. }}

**Pré-requisitos:** {{ links para aulas anteriores }}

**Objetivos de aprendizagem** — ao final, você será capaz de:

- {{ Objetivo }}

## Conceito

<!-- 1 O que é? 2 Por que existe? 3 Qual problema resolve? Explicação progressiva. -->

{{ Conteúdo }}

## Fundamentos técnicos

<!-- 4 Como funciona? 5 Como se relaciona com outros conceitos? -->

{{ Conteúdo }}

## Exemplo empresarial

!!! example "{{ Organização fictícia }}"

    {{ Cenário concreto }}

## Arquitetura tradicional versus recomendada

{{ Comparação, idealmente com diagrama As-Is/To-Be }}

## Controles e padrões relevantes

| Controle ou padrão | Objetivo | Referência |
|:---|:---|:---|
| {{ }} | {{ }} | {{ }} |

## Aplicabilidade: on-premises, cloud e híbrido

<!-- Diretriz transversal: cenário on-premises, cloud e híbrido; integração, dependências de conectividade e identidade, responsabilidades, riscos específicos e trade-offs. -->

| Aspecto | On-premises | Cloud | Híbrido |
|:---|:---|:---|:---|
| {{ }} | {{ }} | {{ }} | {{ }} |

## Como especificar e implementar

<!-- 7 Como implementar ou especificar arquiteturalmente? Exemplos de configuração quando apropriado. -->

{{ Conteúdo }}

## Trade-offs, limitações e antipadrões

<!-- 8 Trade-offs, custos, limitações. -->

{{ Conteúdo }}

## Como validar

<!-- 9 Como validar a implementação? -->

{{ Conteúdo }}

## Como apresentar e justificar

<!-- 10 Como apresentar a decisão para áreas técnicas e executivas? -->

{{ Conteúdo }}

## Checklist de revisão arquitetural

- [ ] {{ Item verificável }}

## Questões de compreensão

**1.** {{ Pergunta }}

??? success "Resposta comentada"

    {{ Resposta e explicação }}

## Exercício de tomada de decisão

!!! question "Cenário"

    {{ Situação com restrições e pelo menos duas alternativas viáveis }}

??? success "Resolução de referência"

    {{ Matriz de decisão, decisão justificada e riscos residuais }}

## Pontos-chave

- {{ Ponto-chave }}

## Referências

<!-- Formato: Organização. *Título*. Versão/ano. <link> — gratuito | pago. Ver docs/internal/style-guide.md -->

- {{ Referência }}

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | {{ @github-handle }} |
| Revisão técnica | {{ @github-handle }} — {{ AAAA-MM-DD }} |
| Última atualização | {{ AAAA-MM-DD }} |
