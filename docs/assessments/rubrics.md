---
title: Rubricas de avaliação
description: Rubrica objetiva para estudos de caso, laboratórios de desenho e projetos da Security Architecture Academy — segurança, requisitos, justificativas, viabilidade, resiliência, custo e documentação.
---

# Rubricas de avaliação

A rubrica abaixo é aplicada a **estudos de caso, laboratórios de desenho e ao projeto final**. Ela avalia a qualidade arquitetural da entrega, e não a quantidade de controles listados.

## Rubrica padrão de projetos

Cada critério recebe um dos três níveis. O peso indica a contribuição para a nota final (0–100).

| Critério | Peso | Excelente (100%) | Adequado (70%) | Insuficiente (30%) |
|:---|:---|:---|:---|:---|
| **Segurança** | 20 | Controles tratam os riscos priorizados em mais de uma camada, sem lacunas nos fluxos que cruzam trust boundaries. | Os riscos principais são tratados; há lacunas menores em riscos secundários. | Riscos prioritários sem tratamento, ou controles desconectados dos riscos. |
| **Cobertura de requisitos** | 15 | Todos os requisitos rastreados de objetivo a controle e evidência. | Requisitos principais atendidos; rastreabilidade parcial. | Requisitos ignorados ou não verificáveis. |
| **Justificativas** | 20 | Alternativas comparadas com critérios explícitos; decisões em ADR com consequências negativas declaradas. | Decisões justificadas, mas comparação superficial de alternativas. | Decisões sem justificativa ou baseadas em preferência por tecnologia. |
| **Viabilidade operacional** | 15 | Considera a capacidade da equipe, processos, dependências e transição; plano exequível. | Viável, com dependências ou impacto operacional pouco detalhados. | Proposta que a organização descrita não conseguiria operar. |
| **Resiliência** | 10 | Pontos únicos de falha identificados e tratados; recuperação considerada no desenho. | Resiliência considerada nos componentes críticos. | Disponibilidade e recuperação ignoradas. |
| **Custo** | 10 | Custos de implantação e operação estimados e comparados entre alternativas; priorização coerente. | Custo mencionado qualitativamente. | Custo ignorado ou incompatível com as restrições. |
| **Documentação** | 10 | Diagramas nas visões adequadas, ADRs e riscos residuais claros para engenharia e para executivos. | Documentação suficiente para a engenharia, sem visão executiva. | Documentação ausente, inconsistente ou ilegível. |

**Cálculo:** soma de (peso × percentual do nível). Exemplo: Excelente em Segurança (20 × 1,0) + Adequado nos demais (80 × 0,7) = 76.

**Aprovação:** nota ≥ 70 **e** nenhum critério *Insuficiente*.

## Rubrica de questões dissertativas

| Nível | Descrição |
|:---|:---|
| **Excelente** | Responde ao que foi pedido, usa os conceitos corretamente, considera o contexto do cenário e declara trade-offs. |
| **Adequado** | Responde corretamente, mas sem considerar trade-offs ou restrições do cenário. |
| **Insuficiente** | Resposta incorreta, genérica ("usar boas práticas") ou que ignora o cenário. |

## Como usar a rubrica na autoavaliação

1. Faça a entrega sem consultar a solução de referência.
2. Avalie cada critério com honestidade, anotando a evidência que justifica o nível.
3. Compare com a solução de referência: divergências não são necessariamente erros — avalie se a sua justificativa se sustenta.
4. Para cada critério *Insuficiente*, revise as aulas indicadas na solução e refaça somente aquela parte.
