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
| **Escopo** | Módulos 2, 3, 6, 7, 11 e 16 completos; aulas selecionadas do Módulo Inicial, do Módulo 1, do Módulo 4, do Módulo 5, do Módulo 9 e do Módulo 10 | Todos os 18 módulos, a seção de IA, os cinco estudos de caso e o projeto final |
| **Plano** | [Plano de 16 semanas](study-plan.md#trilha-essencial-16-semanas) | [Formação completa](study-plan.md#formacao-completa) |

!!! warning "Tempo real de estudo"

    As cargas indicadas cobrem a leitura das aulas. Laboratórios, estudos de caso e revisões costumam dobrar esse tempo. O programa completo pode exigir bem mais do que 16 semanas, conforme o ritmo e a profundidade buscados — a trilha essencial não substitui a formação completa, ela prioriza o que tem maior impacto profissional imediato.

## Disponibilidade

O conteúdo chega ao portal em releases cumulativas, uma por nível — a Release 1 publicou o Nível 0 e o Módulo 2; a Release 2 completa o Nível 1:

<!-- release-table:start -->

| Release | Níveis | Módulos | Estado |
|:---|:---|:---|:---|
| **1 — Fundamentals Base** | Nível 0; Nível 1 | Módulo Inicial, Módulo 1 e Módulo 2 | Disponível (v0.1.1) |
| **2 — Fundamentals: conclusão do Nível 1** | Nível 1 | Módulos 3 e 4 | Disponível (v0.2.1) |
| **3 — Nível 2: Arquiteturas de Infraestrutura** | Nível 2 | Módulos 5 a 8 | Em desenvolvimento (v0.3.0) |
| **4 — Nível 3: Arquitetura Cloud e Híbrida** | Nível 3 | Módulos 9 a 11 | Em desenvolvimento (v0.4.0) |
| **5 — Nível 4: Arquitetura de Segurança Aplicada** | Nível 4 | Módulos 12 a 15 | Planejado (v0.5.0) |
| **6 — Nível 5: Arquitetura Corporativa Avançada** | Nível 5 | Módulos 16 e 17 e complemento de IA | Planejado (v0.6.0) |

<!-- release-table:end -->

A trilha transversal **Fundamentals** (aulas de profundidade *Fundamental* de todos os módulos) e as releases não são a mesma coisa: cada release publica módulos inteiros, para preservar a sequência e os pré-requisitos de cada um; as aulas de profundidade *Fundamental* dos módulos dos Níveis 2 a 5 chegam com a release do respectivo nível. O estado real de cada módulo está no [Curriculum Roadmap](../curriculum/index.md).
