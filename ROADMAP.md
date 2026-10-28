# Roadmap

Este roadmap descreve como a Academy chega ao público e o estado real de cada entrega. O status de cada módulo e aula está no [Curriculum Roadmap](https://andrewsferreira.github.io/security-architecture-academy/curriculum/), gerado a partir de [`curriculum/manifest.yml`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/curriculum/manifest.yml); as mudanças de cada versão publicada estão no [CHANGELOG](https://github.com/andrewsferreira/security-architecture-academy/blob/main/CHANGELOG.md).

**Legenda:** ✅ concluído · 🔄 em andamento · ⏳ planejado

## Modelo de publicação

A formação é publicada em **três releases cumulativas por nível**. Cada release passa por validação técnica completa e pela revisão do mantenedor antes de chegar ao portal; as anteriores permanecem disponíveis e são revalidadas a cada nova publicação.

| Release | Escopo | Versão |
|:---|:---|:---|
| **1 — Fundamentals** | Módulo Inicial, Módulo 1 e Módulo 2; Laboratórios 00, 01 e 02; Caso A; avaliação diagnóstica, avaliações dos módulos e avaliação final integradora; modelos de ADR, requisitos e revisão | v0.1.0 — **publicada em 2026-10-27** |
| **2 — Professional** | Módulos 3 a 15; Casos B, C e E; avaliação intermediária; modelos de avaliação, threat model, matriz de controles, registro de riscos, blueprint híbrido, maturidade e programa de vulnerabilidades | v0.2.0 |
| **3 — Architect** | Módulos 16 e 17 e o complemento de IA; Caso D; avaliação final e avaliação avançada; roadmap, resumo executivo e matriz RACI | v0.3.0 |

## Fundação da plataforma ✅

| Entrega | Status |
|:---|:---|
| Identidade visual, portal (Zensical) com modo claro e escuro, busca e navegação | ✅ |
| Design System, guia editorial, modelo de conteúdo e critérios de publicação | ✅ |
| 13 templates de autoria | ✅ |
| Curriculum manifest com 18 módulos, 135 aulas e complemento | ✅ |
| Research Library com bibliografia verificada e mapa de conhecimento | ✅ |
| CI de validação, publicação manual no GitHub Pages e exportação de releases | ✅ |
| Licenças: conteúdo CC BY 4.0, código MIT, marca com direitos reservados | ✅ |

## Release 1 — Fundamentals ✅

**Published** — versão v0.1.0, revisada e aprovada pelo mantenedor e publicada no portal em 2026-10-27. Correções posteriores são publicadas como versões de correção (v0.1.x) e registradas no [CHANGELOG](https://github.com/andrewsferreira/security-architecture-academy/blob/main/CHANGELOG.md).

| Entrega | Status |
|:---|:---|
| [Módulo Inicial — Fundamentos de Infraestrutura e Computação](https://andrewsferreira.github.io/security-architecture-academy/modules/00-foundations/) (7 aulas) | ✅ disponível |
| [Módulo 1 — Fundamentos de Segurança](https://andrewsferreira.github.io/security-architecture-academy/modules/01-security-fundamentals/) (7 aulas) | ✅ disponível |
| [Módulo 2 — Introdução à Arquitetura de Segurança](https://andrewsferreira.github.io/security-architecture-academy/modules/02-security-architecture/) (8 aulas) | ✅ disponível |
| [Laboratórios 00, 01 e 02](https://andrewsferreira.github.io/security-architecture-academy/labs/) — locais, sem custo, executados e testados | ✅ disponível |
| [Caso A — Meridiana Distribuidora](https://andrewsferreira.github.io/security-architecture-academy/case-studies/case-a-meridiana/), com solução de referência e ADRs | ✅ disponível |
| [Avaliação diagnóstica, avaliações do Módulo Inicial, do Módulo 1 e do Módulo 2 e avaliação final integradora](https://andrewsferreira.github.io/security-architecture-academy/assessments/), com gabaritos | ✅ disponível |
| [Modelos de ADR, especificação de requisitos e checklist de revisão](https://andrewsferreira.github.io/security-architecture-academy/artifacts/) | ✅ disponível |

## Release 2 — Professional 🔄

Em desenvolvimento. Os módulos são escritos, validados e mantidos fora do portal público até a release.

| Entrega | Status |
|:---|:---|
| Módulos 3 a 10 — aulas escritas | 🔄 em revisão no repositório de desenvolvimento |
| Módulo 11 — Hybrid & Multicloud | 🔄 em escrita |
| Módulos 12 a 15 | ⏳ |
| Casos B, C e E; avaliação intermediária; modelos associados | ⏳ |

## Release 3 — Architect ⏳

Módulos 16 e 17, complemento C01 de IA/LLM e identidades não humanas, Caso D, avaliação final e avaliação avançada em inglês.

## Contínuo

- Revisão periódica das fontes cuja versão muda (publicações NIST, documentação de provedores, guias de certificação).
- Regressão completa das releases anteriores a cada nova publicação.
- Alterações em conteúdo publicado registradas no [CHANGELOG](https://github.com/andrewsferreira/security-architecture-academy/blob/main/CHANGELOG.md).

## Fora de escopo

- Emissão de certificados ou afiliação a programas de certificação de terceiros.
- Conteúdo que dependa de dados reais, credenciais ou ambientes de produção.
