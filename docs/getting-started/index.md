---
title: Como usar a Academy
description: Como a Security Architecture Academy está organizada, por onde começar conforme a sua experiência e como cada aula, laboratório, estudo de caso e avaliação funciona.
---

# Como usar a Academy

## O que está disponível

O primeiro conjunto de conteúdo é o **Módulo 02 — Introdução à Arquitetura de Segurança**, com o material que o acompanha:

<div class="grid cards" markdown>

-   :lucide-route:{ .lg .saa-card-icon } **[Módulo 02](../modules/02-security-architecture/index.md)**

    ---

    Oito aulas sobre o papel do arquiteto, níveis de arquitetura, padrões e exceções, referências, frameworks, requisitos e ADRs.

-   :lucide-clipboard-check:{ .lg .saa-card-icon } **[Avaliação diagnóstica](../assessments/diagnostic-fundamentals.md)**

    ---

    Verifica os fundamentos de infraestrutura, segurança e risco que o Módulo 02 pressupõe.

-   :lucide-building-2:{ .lg .saa-card-icon } **[Caso A — Meridiana](../case-studies/case-a-meridiana/index.md)**

    ---

    Uma distribuidora com rede plana, VPN só com senha e pressão da seguradora. As-Is, To-Be e ADRs.

-   :lucide-flask-conical:{ .lg .saa-card-icon } **[Laboratório 02](../labs/lab-02-architecture-modeling.md)**

    ---

    Arquitetura como código: modele, analise fronteiras de confiança e construa o To-Be localmente, sem custo.

</div>

Os demais módulos estão planejados no [currículo](../curriculum/index.md), com aulas, pré-requisitos e fase de produção definidos. O status de cada item aparece ao lado dele.

## Por onde começar

| Seu ponto de partida | Percurso sugerido |
|:---|:---|
| **Vindo de infraestrutura, desenvolvimento ou suporte** | Faça a [avaliação diagnóstica](../assessments/diagnostic-fundamentals.md). Se alguma seção ficar abaixo de 5 de 6, revise os temas indicados no gabarito antes do Módulo 02. |
| **Analista de segurança querendo migrar para arquitetura** | Diagnóstico → Módulo 02 completo → Caso A → Laboratório 02 → avaliação do módulo. |
| **Já atua como arquiteto** | Leia o [mapa de competências](../curriculum/competencies.md), faça direto a [avaliação do Módulo 02](../assessments/m02-security-architecture.md) e use as aulas para preencher lacunas. |
| **Preparando-se para certificações** | Use o [mapeamento de certificações](../certification-mapping/index.md) como guia complementar — a Academy não substitui o material oficial. |

Para um cronograma semana a semana, veja o [plano de estudos](../learning-paths/study-plan.md).

## Como cada aula funciona

Todas as aulas seguem a mesma estrutura, para que você saiba onde procurar:

1. **Resumo e conceito** — o que é e por que importa.
2. **Fundamentos técnicos e exemplo empresarial** — o mecanismo e um cenário fictício realista.
3. **Arquitetura tradicional *versus* recomendada** — com diagrama e as diferenças explicadas.
4. **Aplicabilidade** em on-premises, cloud e híbrido.
5. **Como especificar, validar e justificar** — o que entra em um requisito, como verificar e como apresentar a decisão.
6. **Trade-offs e antipadrões.**
7. **Checklist, questões e exercício de decisão** — as respostas ficam recolhidas; o exercício usa uma matriz ponderada com resolução de referência.

!!! tip "Tente antes de abrir a resposta"

    As respostas das questões, a solução do estudo de caso e os gabaritos das avaliações ficam em blocos recolhidos ou em páginas separadas. O aprendizado vem da tentativa — compare depois.

## Princípios que você vai encontrar

- **Dados sempre fictícios.** Empresas, endereços e números são inventados; domínios usam `example.com`.
- **Fontes rastreáveis.** Afirmações normativas trazem a fonte, a versão e a data de verificação. Fontes que não puderam ser confirmadas são marcadas como tal no [registro de fontes](../resources/index.md).
- **Neutralidade de produto.** Conceitos e padrões vêm antes; provedores aparecem como exemplos.
- **Sem custo obrigatório.** Laboratórios rodam localmente ou em camadas gratuitas, com aviso explícito quando houver qualquer risco de cobrança.

## Acompanhar a evolução

- Use **Watch → Custom → Releases** no [repositório](https://github.com/andrewsferreira/security-architecture-academy) para ser avisado a cada publicação.
- O [CHANGELOG](https://github.com/andrewsferreira/security-architecture-academy/blob/main/CHANGELOG.md) registra o que mudou em cada versão.

## Executar o portal localmente

Para ler o conteúdo offline ou contribuir, veja [Desenvolvimento local](local-development.md).
