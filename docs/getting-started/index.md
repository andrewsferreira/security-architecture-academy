---
title: Como usar a Academy
description: Como a Security Architecture Academy está organizada, por onde começar conforme a sua experiência e como cada aula, laboratório, estudo de caso e avaliação funciona.
---

# Como usar a Academy

## O que está disponível

A **Release 1 — Fundamentals** (v0.1.0) está publicada: três módulos completos, com laboratórios, estudo de caso, avaliações e modelos.

<div class="grid cards" markdown>

-   :lucide-server:{ .lg .saa-card-icon } **[Módulo Inicial — Infraestrutura e Computação](../modules/00-foundations/index.md)**

    ---

    Sete aulas: computação e virtualização, TCP/IP, segmentação, datacenter e alta disponibilidade, containers e APIs, cloud e leitura de diagramas.

-   :lucide-shield-check:{ .lg .saa-card-icon } **[Módulo 1 — Fundamentos de Segurança](../modules/01-security-fundamentals/index.md)**

    ---

    Sete aulas: propriedades de segurança, princípios de design, fronteiras de confiança, criptografia, PKI e TLS, risco e modelos formais.

-   :lucide-route:{ .lg .saa-card-icon } **[Módulo 2 — Introdução à Arquitetura de Segurança](../modules/02-security-architecture/index.md)**

    ---

    Oito aulas sobre o papel do arquiteto, níveis de arquitetura, padrões e exceções, referências, frameworks, requisitos e ADRs.

-   :lucide-flask-conical:{ .lg .saa-card-icon } **[Laboratórios 00, 01 e 02](../labs/index.md)**

    ---

    Plano de rede, mecanismos de segurança e arquitetura como código — locais, sem custo e com dados fictícios.

-   :lucide-building-2:{ .lg .saa-card-icon } **[Caso A — Meridiana](../case-studies/case-a-meridiana/index.md)**

    ---

    Uma distribuidora com rede plana, VPN só com senha e pressão da seguradora. As-Is, To-Be e ADRs.

-   :lucide-clipboard-check:{ .lg .saa-card-icon } **[Avaliações](../assessments/index.md)**

    ---

    Diagnóstica, uma por módulo e a avaliação final integradora de Fundamentals, com gabaritos comentados.

</div>

Os níveis Professional e Architect estão no [currículo](../curriculum/index.md) e no [roadmap](../about/roadmap.md) e entram no portal depois de concluídos e revisados.

## Por onde começar

| Seu ponto de partida | Percurso sugerido |
|:---|:---|
| **Iniciando na área** | [Módulo Inicial](../modules/00-foundations/index.md) → [Laboratório 00](../labs/lab-00-network-plan.md) → [avaliação do Módulo Inicial](../assessments/m00-foundations.md) → [Módulo 1](../modules/01-security-fundamentals/index.md) → [Laboratório 01](../labs/lab-01-security-mechanisms.md) → [avaliação do Módulo 1](../assessments/m01-security-fundamentals.md) → [Módulo 2](../modules/02-security-architecture/index.md) → [Laboratório 02](../labs/lab-02-architecture-modeling.md) → [Caso A](../case-studies/case-a-meridiana/index.md) → [avaliação do Módulo 2](../assessments/m02-security-architecture.md) → [avaliação final](../assessments/fundamentals-final.md) |
| **Vindo de infraestrutura, desenvolvimento ou suporte** | Faça a [avaliação diagnóstica](../assessments/diagnostic-fundamentals.md). Revise no Módulo Inicial ou 01 os temas das seções abaixo de 5 de 6, depois siga para o Módulo 2, o Caso A e a avaliação final. |
| **Analista de segurança querendo migrar para arquitetura** | Diagnóstico → revisar no Módulo 1 os temas indicados → Módulo 2 completo → Caso A → Laboratório 02 → avaliação do Módulo 2 → avaliação final. |
| **Já atua como arquiteto** | Leia o [mapa de competências](../curriculum/competencies.md), faça direto as [avaliações dos módulos](../assessments/index.md) e use as aulas para preencher lacunas. |
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

Para ler o conteúdo offline, clone o [repositório](https://github.com/andrewsferreira/security-architecture-academy) e, com Python 3.11 ou superior, execute `make install` e `make serve`; o portal abre em <http://localhost:8000/security-architecture-academy/>.
