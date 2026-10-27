---
title: Mapa de competências
description: As dez competências que a Security Architecture Academy desenvolve, com evidências observáveis por profundidade (Fundamental, Professional e Architect) e os módulos que as trabalham.
---

# Mapa de competências

O objetivo da formação não é concluir um currículo: é tornar o estudante capaz de **receber uma demanda de negócio e entregar uma arquitetura segura, viável, documentada e defensável**. As dez competências abaixo descrevem essa capacidade. Cada módulo, atividade e avaliação existe para desenvolver ou verificar pelo menos uma delas.

## As dez competências

| # | Competência | Pergunta que o profissional consegue responder |
|:---|:---|:---|
| C1 | Compreender uma demanda empresarial | *Qual resultado de negócio esta iniciativa precisa entregar, e o que está em risco?* |
| C2 | Traduzir necessidades em requisitos de segurança | *Quais requisitos verificáveis protegem esse resultado?* |
| C3 | Avaliar a arquitetura existente | *Como o ambiente funciona hoje, e onde estão suas fronteiras e dependências?* |
| C4 | Identificar ameaças, dependências e riscos | *O que pode dar errado, com que probabilidade e qual impacto?* |
| C5 | Comparar alternativas técnicas | *Quais opções atendem aos requisitos e o que cada uma custa?* |
| C6 | Desenhar uma arquitetura To-Be | *Como deve ser o ambiente-alvo, em visões conceitual, lógica e física?* |
| C7 | Selecionar controles adequados | *Quais controles, em que camada, tratam quais riscos?* |
| C8 | Documentar decisões e riscos residuais | *O que foi decidido, por quê, e que risco permanece aceito por quem?* |
| C9 | Elaborar um roadmap de implementação | *Em que ordem, com que dependências e com que marcos a mudança acontece?* |
| C10 | Defender técnica e executivamente a solução | *Como explicar a proposta a um CISO, à engenharia e ao negócio?* |

## Evidências por profundidade

Cada competência evolui em três profundidades. As evidências são **observáveis**: descrevem o que o estudante produz ou faz, e são a base das [rubricas de avaliação](../assessments/rubrics.md).

| # | Fundamental — compreende | Professional — aplica | Architect — decide e justifica |
|:---|:---|:---|:---|
| C1 | Distingue objetivos de negócio, requisitos funcionais e requisitos de qualidade em um enunciado. | Entrevista stakeholders e registra objetivos, restrições e critérios de sucesso de uma iniciativa. | Concilia objetivos conflitantes entre áreas e explicita o apetite a risco que orienta a arquitetura. |
| C2 | Reconhece requisitos de segurança bem e mal escritos. | Deriva requisitos verificáveis a partir de objetivos, ameaças e obrigações normativas. | Estrutura uma especificação rastreável (objetivo → atributo → requisito → controle → evidência). |
| C3 | Lê diagramas e identifica componentes, fluxos e trust boundaries. | Produz o As-Is de um sistema com inventário, fluxos de dados e dependências. | Avalia o As-Is de um ambiente híbrido corporativo e identifica lacunas estruturais. |
| C4 | Diferencia ameaça, vulnerabilidade, risco e exposição. | Conduz threat modeling de um sistema e estima riscos com método explícito. | Agrega riscos técnicos em riscos de negócio e prioriza tratamento no nível do portfólio. |
| C5 | Descreve vantagens e limitações de soluções conhecidas. | Compara alternativas com matriz de decisão e critérios ponderados. | Avalia alternativas considerando custo total, operação, lock-in, resiliência e capacidade da equipe. |
| C6 | Diferencia arquitetura conceitual, lógica e física. | Desenha o To-Be de uma solução nas três visões, coerente com padrões corporativos. | Desenha arquiteturas de referência e blueprints reutilizáveis para múltiplas organizações. |
| C7 | Classifica controles por função e tipo (preventivo, detectivo, corretivo, compensatório). | Seleciona controles por camada a partir de riscos e requisitos, com referências a frameworks. | Define controles universais e adaptações por ambiente, e controles compensatórios para exceções. |
| C8 | Lê um ADR e identifica contexto, decisão e consequências. | Escreve ADRs completos, com alternativas e consequências negativas. | Mantém um registro de decisões coerente, com riscos residuais formalmente aceitos por responsáveis. |
| C9 | Ordena entregas simples por dependência. | Constrói um plano de implementação com fases, dependências e critérios de aceitação. | Constrói roadmaps de 90 dias, 6 e 12 meses alinhados a orçamento, risco e capacidade. |
| C10 | Explica um conceito com clareza para um público técnico. | Apresenta uma solução para engenharia, com diagramas e justificativas. | Defende uma proposta para CISO e executivos, negociando risco, custo e prazo. |

## Onde cada competência é desenvolvida

As colunas indicam os níveis do currículo; as células, os módulos em que a competência é **trabalhada com intenção** (não apenas mencionada).

| # | Nível 0 | Nível 1 | Nível 2 | Nível 3 | Nível 4 | Nível 5 |
|:---|:---|:---|:---|:---|:---|:---|
| C1 | — | M02 | — | M11 | M14 | M16, M17 |
| C2 | — | M02, M03, M04 | M06, M07 | M11 | M12, M13 | M16, M17 |
| C3 | M00 | M02, M04 | M05, M08 | M09, M10, M11 | M14 | M17 |
| C4 | M01 | M03, M04 | M05, M07, M08 | M11 | M12, M13, M14, M15 | M16, M17 |
| C5 | — | M02 | M05, M06, M07 | M09, M10, M11 | M12, M15 | M16, M17 |
| C6 | — | M02, M04 | M05, M06, M07, M08 | M09, M10, M11 | M12, M13 | M16, M17 |
| C7 | M01 | M03 | M05, M06, M07, M08 | M09, M10, M11 | M12, M13, M14, M15 | M16 |
| C8 | — | M02 | M07 | M11 | M14 | M16, M17 |
| C9 | — | — | M07, M08 | M11 | M14 | M16, M17 |
| C10 | — | M02 | — | M11 | M14 | M16, M17 |

## Como as competências são verificadas

| Instrumento | Competências | Onde |
|:---|:---|:---|
| Avaliação diagnóstica | Base de C3, C4 e C7 | [Diagnóstico de fundamentos](../assessments/diagnostic-fundamentals.md) |
| Questões e exercícios de decisão nas aulas | Todas, na profundidade da aula | Cada aula |
| Avaliações de módulo, intermediária e final | Todas, com desafios baseados em competência | [Avaliações](../assessments/index.md) |
| Estudos de caso com rubrica | C1–C10 | [Estudos de caso](../case-studies/index.md) |
| Laboratórios | C3, C4, C6, C7 | [Laboratórios](../labs/index.md) |
| Projeto final | C1–C10 na profundidade Architect | M17 |
