---
title: Início
description: Formação aberta e progressiva em Arquitetura de Segurança da Informação — objetivo do projeto e os fundamentos que serão tratados no primeiro nível.
hide:
  - navigation
  - toc
  - path
---

<div class="saa-hero" markdown>

<div class="saa-hero__text" markdown>

<p class="saa-eyebrow">Open-source learning platform</p>

<h1>Security Architecture Academy</h1>

<p class="saa-lead">Uma formação aberta, gratuita e progressiva em Arquitetura de Segurança da Informação — dos fundamentos às arquiteturas corporativas, cloud e híbridas, com diagramas, padrões e decisões explicadas.</p>

<div class="saa-actions" markdown>

[Fundamentos da formação](#fundamentos-que-serao-tratados){ .md-button .md-button--primary }
[Repositório no GitHub](https://github.com/andrewsferreira/security-architecture-academy){ .md-button }

</div>

</div>

<div class="saa-hero__art" markdown>

![Ilustração conceitual: zonas on-premises e cloud dentro de uma fronteira de confiança corporativa, conectadas por um gateway controlado](assets/images/hero-architecture-light.svg#only-light){ width="540" height="320" }
![Ilustração conceitual: zonas on-premises e cloud dentro de uma fronteira de confiança corporativa, conectadas por um gateway controlado](assets/images/hero-architecture-dark.svg#only-dark){ width="540" height="320" }

</div>

</div>

## Objetivo

<p class="saa-section-intro">Formar profissionais capazes de projetar, avaliar e justificar arquiteturas de segurança em ambientes corporativos, cloud e híbridos.</p>

A Security Architecture Academy é um projeto educacional independente, em português brasileiro, que preserva a terminologia técnica em inglês usada no mercado. Mais do que apresentar controles e ferramentas, a formação ensina a **raciocinar como arquiteto de segurança**: entender o negócio e os riscos, transformar necessidades em requisitos, comparar alternativas com critérios explícitos e registrar decisões que outras pessoas consigam revisar.

<div class="grid cards" markdown>

-   :lucide-graduation-cap:{ .lg .saa-card-icon } **Progressiva**

    ---

    Três níveis cumulativos — Fundamentals, Professional e Architect —, cada um apoiado no anterior.

-   :lucide-workflow:{ .lg .saa-card-icon } **Orientada a decisões**

    ---

    Diagramas, trade-offs, matrizes de decisão e registros de decisão arquitetural (ADRs) em todas as aulas.

-   :lucide-book-open:{ .lg .saa-card-icon } **Fundamentada e prática**

    ---

    Fontes reconhecidas — NIST, ISO, CIS, OWASP, SABSA, TOGAF e literatura técnica —, com versão e data; estudos de caso e laboratórios locais, sem custo, com dados fictícios.

</div>

## Fundamentos que serão tratados

<p class="saa-section-intro">O primeiro nível, <strong>Fundamentals</strong>, constrói a base para o restante da formação, na sequência infraestrutura → segurança da informação → arquitetura de segurança.</p>

<div class="grid cards" markdown>

-   :lucide-server:{ .lg .saa-card-icon } **M00 — Fundamentos de Infraestrutura e Computação**

    ---

    - Computação, sistemas operacionais e virtualização
    - Redes TCP/IP: modelo OSI, endereçamento, DNS, DHCP e NAT
    - Segmentação e conectividade: VLAN, roteamento, VPN, TLS e firewalls
    - Datacenters, armazenamento, clusters e alta disponibilidade
    - Containers, Kubernetes, APIs, microsserviços e serverless
    - Cloud computing: modelos de serviço e de implantação
    - Leitura de diagramas arquiteturais: componentes, fluxos e fronteiras

-   :lucide-layers:{ .lg .saa-card-icon } **M01 — Fundamentos de Segurança**

    ---

    - Propriedades de segurança: CIA, autenticidade, autorização e não repúdio
    - Princípios de design seguro e defense in depth
    - Trust boundaries, attack surface e responsabilidade compartilhada
    - Criptografia aplicada: simétrica, assimétrica, hashing e assinaturas
    - PKI, certificados, TLS e gerenciamento de chaves
    - Ameaça, vulnerabilidade, risco, exposição e controle
    - Modelos formais: Bell-LaPadula, Biba, Clark-Wilson e Brewer-Nash

-   :lucide-building-2:{ .lg .saa-card-icon } **M02 — Introdução à Arquitetura de Segurança**

    ---

    - O papel do Security Architect
    - Enterprise, Solution e Security Architecture
    - Arquitetura conceitual, lógica e física
    - Princípios, padrões, baselines e exceções
    - Arquiteturas de referência e blueprints
    - Frameworks: NIST, SABSA, TOGAF, CISSP e ISSAP
    - Requisitos de segurança orientados ao negócio
    - Architecture Decision Records

</div>

Os fundamentos incluem também **laboratórios locais e sem custo** (plano de endereçamento e segmentação, mecanismos de segurança na prática e modelagem arquitetural como código), um **estudo de caso** de datacenter tradicional, **avaliações por módulo** com gabaritos comentados e uma **avaliação final integradora**.

## Próximos níveis

| Nível | Foco | Situação |
|:---|:---|:---|
| **Fundamentals** | Infraestrutura, fundamentos de segurança e introdução à arquitetura de segurança | <span class="saa-status saa-status--in-review">Em revisão</span> |
| **Professional** | Governança e riscos, threat modeling, redes, identidade, Zero Trust, legados, AWS, Azure, Google Cloud, híbrido e multicloud, aplicações, dados, vulnerabilidades e operações | <span class="saa-status saa-status--draft">Em desenvolvimento</span> |
| **Architect** | Arquitetura corporativa, governança entre unidades, segurança de IA e projeto final | <span class="saa-status saa-status--planned">Planejado</span> |

!!! info "Conteúdo em preparação"

    As aulas ainda não estão publicadas. O primeiro nível está em revisão e será disponibilizado neste endereço depois de aprovado; os níveis seguintes serão publicados progressivamente.

## Licença e independência

O conteúdo educacional é distribuído sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br) e o código sob [MIT](https://opensource.org/license/mit). A Security Architecture Academy é um projeto independente, sem afiliação, patrocínio ou endosso das organizações, normas e certificações citadas.
