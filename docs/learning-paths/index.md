---
title: Learning Paths
description: Trilhas transversais (Fundamentals, Professional e Advanced), profundidades de aula e os dois horizontes de estudo da Security Architecture Academy.
---

# Learning Paths

A formação combina três estruturas que se complementam:

| Estrutura | Pergunta que responde | Onde aparece |
|:---|:---|:---|
| **Níveis** (0 a 5) | *Em que ordem os assuntos são estudados?* | Organização dos 18 módulos |
| **Profundidade** (Fundamental, Professional, Architect) | *Quanto esta aula exige de mim?* | Cada aula e cada avaliação |
| **Trilhas** (Fundamentals, Professional, Advanced) | *Que conjunto de aulas atende ao meu objetivo?* | Percursos transversais aos módulos |

```mermaid
--8<-- "assets/diagrams/learning-journey.mmd"
```

## Profundidades

Cada aula declara uma profundidade, e as avaliações ficam progressivamente mais exigentes.

| Profundidade | O estudante… | Exemplo de evidência |
|:---|:---|:---|
| **Fundamental** | compreende conceitos e terminologia. | Explica a diferença entre arquitetura lógica e física com um exemplo. |
| **Professional** | aplica os conceitos na análise e no desenho de soluções. | Desenha o To-Be de um sistema e seleciona controles por camada. |
| **Architect** | justifica decisões, avalia alternativas, gerencia riscos e documenta a arquitetura. | Escreve um ADR com alternativas, riscos residuais e critérios de aceitação. |

## Trilhas transversais

As trilhas atravessam os módulos agrupando aulas pela profundidade. Elas permitem que quem já tem experiência técnica — o perfil para o qual esta formação foi desenhada — concentre esforço onde há mais lacuna.

=== "Fundamentals"

    **Objetivo:** dominar os conceitos necessários para compreender arquitetura.

    - Aulas de profundidade *Fundamental* de todos os módulos (cerca de 27 horas de aulas).
    - Indicada para quem obteve resultado abaixo de 70% em alguma seção da [avaliação diagnóstica](../assessments/diagnostic-fundamentals.md).
    - Conclui com a avaliação diagnóstica refeita, mirando 85% ou mais.

=== "Professional"

    **Objetivo:** aplicar arquitetura em organizações reais.

    - Aulas de profundidade *Professional* (cerca de 82 horas), laboratórios e os estudos de caso A, B e E.
    - Exige domínio dos fundamentos: diagnóstico aprovado ou trilha Fundamentals concluída.
    - Conclui com a avaliação intermediária e ao menos dois estudos de caso avaliados como *Adequado* ou melhor na rubrica.

=== "Advanced"

    **Objetivo:** decisões corporativas, ambientes híbridos complexos, governança e liderança técnica.

    - Aulas de profundidade *Architect* (cerca de 58 horas), estudos de caso C e D e o projeto final.
    - Exige a trilha Professional, ou experiência equivalente comprovada nas avaliações.
    - Conclui com a avaliação final, a avaliação avançada em inglês e o projeto final avaliado como *Excelente* em pelo menos metade dos critérios.

## Dois horizontes de estudo

| | Trilha essencial | Formação completa |
|:---|:---|:---|
| **Objetivo** | Desenvolvimento profissional acelerado nas competências prioritárias | Formação integral e evolução contínua |
| **Duração** | 16 semanas, 6 a 8 horas por semana (cerca de 100 a 130 horas) | Sem prazo rígido; estimativa acima de 300 horas incluindo atividades |
| **Escopo** | M02, M03, M06, M07, M11 e M16 completos; aulas selecionadas de M00, M01, M04, M05, M09 e M10 | Todos os 18 módulos, a seção de IA, os cinco estudos de caso e o projeto final |
| **Plano** | [Plano de 16 semanas](study-plan.md#trilha-essencial-16-semanas) | [Formação completa](study-plan.md#formacao-completa) |

!!! warning "Tempo real de estudo"

    As cargas indicadas cobrem a leitura das aulas. Laboratórios, estudos de caso e revisões costumam dobrar esse tempo. O programa completo pode exigir bem mais do que 16 semanas, conforme o ritmo e a profundidade buscados — a trilha essencial não substitui a formação completa, ela prioriza o que tem maior impacto profissional imediato.

## Disponibilidade

O conteúdo chega ao portal em releases cumulativas por nível:

| Release | Módulos | O que significa para as trilhas |
|:---|:---|:---|
| **1 — Fundamentals** | M00, M01, M02 | Base de toda a formação: infraestrutura, fundamentos de segurança e introdução à arquitetura, com laboratórios e avaliação final integradora. |
| **2 — Professional** | M03 a M15 | Completa as aulas de profundidade *Professional* e as aulas *Fundamental* que abrem esses módulos (por exemplo, M03-L01 e M07-L01). |
| **3 — Architect** | M16, M17, C01 | Completa a trilha Advanced e o projeto final. |

A trilha transversal **Fundamentals** (aulas de profundidade *Fundamental* de todos os módulos) e a **Release 1 — Fundamentals** não são a mesma coisa: a release publica módulos inteiros, para preservar a sequência e os pré-requisitos de cada um; as aulas de profundidade *Fundamental* dos módulos 03 a 13 chegam com a Release 2. O estado real de cada módulo está no [Curriculum Roadmap](../curriculum/index.md).
