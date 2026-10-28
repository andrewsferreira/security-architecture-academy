# Roadmap

Este roadmap descreve como a Academy chega ao público e o estado real de cada entrega. O status de cada módulo e aula está no [Curriculum Roadmap](https://andrewsferreira.github.io/security-architecture-academy/curriculum/), gerado a partir de [`curriculum/manifest.yml`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/curriculum/manifest.yml); as mudanças de cada versão publicada estão no [CHANGELOG](https://github.com/andrewsferreira/security-architecture-academy/blob/main/CHANGELOG.md).

**Legenda:** ✅ concluído · 🔄 em andamento · ⏳ planejado

## Modelo de publicação

A formação é publicada **por nível, em releases cumulativas**. Cada release passa por validação técnica completa e pela revisão do mantenedor antes de chegar ao portal; as anteriores permanecem disponíveis e são revalidadas a cada nova publicação. Correções de uma release publicada saem como versões de correção (por exemplo, v0.1.1).

<!-- roadmap-releases:start -->

| Release | Níveis | Escopo | Versão | Estado |
|:---|:---|:---|:---|:---|
| **1 — Fundamentals Base** | Nível 0; Nível 1 | **Módulo Inicial, Módulo 1 e Módulo 2.** Infraestrutura, fundamentos de segurança e introdução à arquitetura de segurança, com laboratórios, estudo de caso e avaliação integradora. | v0.1.0 (2026-10-27), v0.1.1 (2026-10-27) | ✅ disponível |
| **2 — Fundamentals: conclusão do Nível 1** | Nível 1 | **Módulos 3 e 4.** Governança, riscos e controles; métodos de design e threat modeling; avaliação integradora do Nível 1. | v0.2.0 | ✅ disponível |
| **3 — Nível 2: Arquiteturas de Infraestrutura** | Nível 2 | **Módulos 5 a 8.** Rede, identidade, Zero Trust e ambientes on-premises e legados. | v0.3.0 | 🔄 em desenvolvimento |
| **4 — Nível 3: Arquitetura Cloud e Híbrida** | Nível 3 | **Módulos 9 a 11.** AWS, Azure, Google Cloud e a integração segura entre ambientes. | v0.4.0 | 🔄 em desenvolvimento |
| **5 — Nível 4: Arquitetura de Segurança Aplicada** | Nível 4 | **Módulos 12 a 15.** Aplicações, dados, gestão de vulnerabilidades e exposição, operações e resiliência. | v0.5.0 | ⏳ planejada |
| **6 — Nível 5: Arquitetura Corporativa Avançada** | Nível 5 | **Módulos 16 e 17 e complemento de IA.** Arquitetura corporativa, governança entre unidades, estudos de caso integradores e projeto final. | v0.6.0 | ⏳ planejada |

<!-- roadmap-releases:end -->

O estado da tabela é calculado a partir do manifesto: uma release só aparece como disponível quando todo o seu escopo está publicado.

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

<a id="release-1-fundamentals"></a>

## Release 1 — Fundamentals Base

Primeira publicação (v0.1.0, 2026-10-27) e versão de correção v0.1.1 (estabilização da navegação, da nomenclatura e do escopo público), registradas no [CHANGELOG](https://github.com/andrewsferreira/security-architecture-academy/blob/main/CHANGELOG.md).

| Entrega |
|:---|
| [Módulo Inicial — Fundamentos de Infraestrutura e Computação](https://andrewsferreira.github.io/security-architecture-academy/modules/00-foundations/) (7 aulas) |
| [Módulo 1 — Fundamentos de Segurança](https://andrewsferreira.github.io/security-architecture-academy/modules/01-security-fundamentals/) (7 aulas) |
| [Módulo 2 — Introdução à Arquitetura de Segurança](https://andrewsferreira.github.io/security-architecture-academy/modules/02-security-architecture/) (8 aulas) |
| [Laboratórios 00, 01 e 02](https://andrewsferreira.github.io/security-architecture-academy/labs/) — locais, sem custo, executados e testados |
| [Caso A — Meridiana Distribuidora](https://andrewsferreira.github.io/security-architecture-academy/case-studies/case-a-meridiana/), com solução de referência e ADRs |
| [Avaliação diagnóstica, avaliações do Módulo Inicial, do Módulo 1 e do Módulo 2 e avaliação integradora do Módulo Inicial ao Módulo 2](https://andrewsferreira.github.io/security-architecture-academy/assessments/), com gabaritos |
| [Modelos de ADR, especificação de requisitos e checklist de revisão](https://andrewsferreira.github.io/security-architecture-academy/artifacts/) |

## Release 2 — Fundamentals: conclusão do Nível 1

Completa o **Nível 1 — Fundamentos de Arquitetura**: com ela, os Níveis 0 e 1 ficam inteiros no portal (5 módulos, 37 aulas).

| Entrega |
|:---|
| Módulo 3 — Governança, Riscos e Controles (8 aulas) |
| Módulo 4 — Métodos de Design e Threat Modeling (7 aulas) |
| Avaliação integradora do Nível 1, com rubrica, solução de referência e gabarito comentado |

<a id="release-2-professional"></a>
<a id="release-3-architect"></a>

## Releases 3 a 6 — Níveis 2 a 5

Cada release publica um nível inteiro, depois de escrito, validado e revisado:

- **Release 3 — Nível 2, Arquiteturas de Infraestrutura:** Módulos 5 a 8, avaliação intermediária e modelos de avaliação de arquitetura, threat model, matriz de controles e registro de riscos.
- **Release 4 — Nível 3, Arquitetura Cloud e Híbrida:** Módulos 9 a 11, Casos B e C e blueprint de arquitetura híbrida.
- **Release 5 — Nível 4, Arquitetura de Segurança Aplicada:** Módulos 12 a 15, Caso E e modelos de maturidade e de programa de vulnerabilidades.
- **Release 6 — Nível 5, Arquitetura Corporativa Avançada:** Módulos 16 e 17, complemento de IA, Caso D, avaliação final, avaliação avançada em inglês e modelos de roadmap, resumo executivo e matriz RACI.

## Contínuo

- Revisão periódica das fontes cuja versão muda (publicações NIST, documentação de provedores, guias de certificação).
- Regressão completa das releases anteriores a cada nova publicação.
- Alterações em conteúdo publicado registradas no [CHANGELOG](https://github.com/andrewsferreira/security-architecture-academy/blob/main/CHANGELOG.md).

## Fora de escopo

- Emissão de certificados ou afiliação a programas de certificação de terceiros.
- Conteúdo que dependa de dados reais, credenciais ou ambientes de produção.
