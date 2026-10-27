---
title: Início
description: Plataforma educacional aberta e progressiva de Arquitetura de Segurança da Informação — dos fundamentos às arquiteturas corporativas, cloud e híbridas.
hide:
  - navigation
  - toc
  - path
---

<div class="saa-hero" markdown>

<div class="saa-hero__text" markdown>

<p class="saa-eyebrow">Open-source learning platform</p>

<h1>Security Architecture Academy</h1>

<p class="saa-lead">Uma formação aberta e progressiva em Arquitetura de Segurança da Informação — dos fundamentos às arquiteturas corporativas, cloud e híbridas, com diagramas, padrões e decisões explicadas.</p>

<div class="saa-actions" markdown>

[Conhecer o currículo](curriculum/index.md){ .md-button .md-button--primary }
[Ver o roadmap](about/roadmap.md){ .md-button }

</div>

</div>

<div class="saa-hero__art" markdown>

![Ilustração conceitual: zonas on-premises e cloud dentro de uma fronteira de confiança corporativa, conectadas por um gateway controlado](assets/images/hero-architecture-light.svg#only-light){ width="540" height="320" }
![Ilustração conceitual: zonas on-premises e cloud dentro de uma fronteira de confiança corporativa, conectadas por um gateway controlado](assets/images/hero-architecture-dark.svg#only-dark){ width="540" height="320" }

</div>

</div>

## Learning Paths

<p class="saa-section-intro">Três níveis de formação publicados progressivamente. Cada nível pressupõe o anterior e termina com a capacidade de tomar decisões de arquitetura mais amplas.</p>

<!-- release-status:start -->

!!! success "Disponível agora"

    A Academy é disponibilizada progressivamente, por nível. Publicado: **v0.1.0 — Fundamentals**. Os níveis seguintes entram no portal somente depois de concluídos e revisados.

[Começar pelos Fundamentals](modules/00-foundations/01-computing-os-virtualization.md){ .md-button .md-button--primary }
[Ver o currículo](curriculum/index.md){ .md-button }

<div class="saa-journey" markdown>

<div class="saa-journey__step" markdown>

### Fundamentals

**Módulos 00 a 02.** Infraestrutura, fundamentos de segurança e introdução à arquitetura de segurança, com laboratórios, estudo de caso e avaliação final integradora.

<span class="saa-status saa-status--published">Disponível</span> <span class="saa-meta">v0.1.0</span>

</div>

<div class="saa-journey__step" markdown>

### Professional

**Módulos 03 a 15.** Governança, threat modeling, rede, identidade, Zero Trust, legados, AWS, Azure, Google Cloud, híbrido, aplicações, dados, vulnerabilidades e operações.

<span class="saa-status saa-status--draft">Em desenvolvimento</span> <span class="saa-meta">v0.2.0</span>

</div>

<div class="saa-journey__step" markdown>

### Architect

**Módulos 16 e 17 e complemento de IA.** Arquitetura corporativa, governança entre unidades, estudos de caso integradores e projeto final.

<span class="saa-status saa-status--planned">Planejado</span> <span class="saa-meta">v0.3.0</span>

</div>

</div>

<!-- release-status:end -->

[Detalhes das trilhas](learning-paths/index.md)

## Explore Security Architecture

<p class="saa-section-intro">Os domínios de conhecimento que estruturam a formação. Cada módulo do currículo está mapeado para um ou mais domínios.</p>

<div class="grid cards" markdown>

-   :lucide-server:{ .lg .saa-card-icon } **Infrastructure Foundations**

    ---

    Computação, redes, datacenter, containers e cloud — a base para ler qualquer arquitetura.

-   :lucide-layers:{ .lg .saa-card-icon } **Security Foundations**

    ---

    Princípios, terminologia, defesa em profundidade e o papel do arquiteto de segurança.

-   :lucide-scale:{ .lg .saa-card-icon } **Governance, Risk & Compliance**

    ---

    Políticas, gestão de riscos, frameworks normativos e evidências de conformidade.

-   :lucide-fingerprint:{ .lg .saa-card-icon } **Identity & Access Management**

    ---

    Identidades humanas e de máquina, federação, autorização e acesso privilegiado.

-   :lucide-shield-check:{ .lg .saa-card-icon } **Zero Trust Architecture**

    ---

    Decisões de acesso explícitas, contínuas e baseadas em contexto.

-   :lucide-network:{ .lg .saa-card-icon } **Network Security**

    ---

    Segmentação, zonas de confiança, inspeção de tráfego e conectividade segura.

-   :lucide-cloud:{ .lg .saa-card-icon } **Cloud Security**

    ---

    Modelo de responsabilidade compartilhada, landing zones e guardrails.

-   :lucide-git-fork:{ .lg .saa-card-icon } **Hybrid & Multicloud Security**

    ---

    Políticas consistentes entre data centers e múltiplos provedores.

-   :lucide-code-xml:{ .lg .saa-card-icon } **Application Security**

    ---

    Arquitetura segura de aplicações e APIs, threat modeling e supply chain.

-   :lucide-database:{ .lg .saa-card-icon } **Data Security**

    ---

    Classificação, criptografia, gestão de chaves, privacidade e retenção.

-   :lucide-radar:{ .lg .saa-card-icon } **Vulnerability Management**

    ---

    Gestão de vulnerabilidades e exposição orientada a risco.

-   :lucide-activity:{ .lg .saa-card-icon } **Security Operations & Resilience**

    ---

    Arquitetura de detecção e resposta, continuidade e recuperação.

-   :lucide-building-2:{ .lg .saa-card-icon } **Enterprise Security Architecture**

    ---

    Frameworks, reference architectures, ADRs e governança de arquitetura.

</div>

## Learning Experience

<div class="grid" markdown>

<div class="card" markdown>

**:lucide-book-open: Aulas técnicas**

Conceitos explicados em português, com terminologia em inglês e referências rastreáveis a normas e frameworks.

</div>

<div class="card" markdown>

**:lucide-workflow: Diagramas arquiteturais**

Cada conceito estrutural acompanhado de diagramas editáveis, legíveis em modo claro e escuro.

</div>

<div class="card" markdown>

**:lucide-flask-conical: Exercícios e laboratórios**

Atividades práticas com ambientes fictícios — nunca dados, credenciais ou sistemas reais.

</div>

<div class="card" markdown>

**:lucide-file-check-2: Projetos de arquitetura**

Estudos de caso, ADRs e uma reference architecture como projeto final.

</div>

</div>

## Featured Architecture

<p class="saa-section-intro">Exemplo conceitual da relação que a formação explora: o negócio orienta o risco, o risco define requisitos, os requisitos viram controles e os controles protegem workloads em ambientes híbridos.</p>

```mermaid
--8<-- "assets/diagrams/architecture-overview.mmd"
```

## Project Roadmap

<p class="saa-section-intro">A plataforma, o currículo completo e a Research Library já existem; o conteúdo chega ao portal por níveis, cada um com revisão própria antes da publicação. O estado de cada nível aparece acima e no roadmap.</p>

[Roadmap completo](about/roadmap.md)

## Start Exploring

<div class="grid cards" markdown>

-   :lucide-map:{ .lg .saa-card-icon } **[Curriculum Roadmap](curriculum/index.md)**

    Os 18 módulos e 135 aulas, por nível e domínio, com status editorial real.

-   :lucide-compass:{ .lg .saa-card-icon } **[Como usar a Academy](getting-started/index.md)**

    Como a plataforma está organizada e como acompanhar a evolução.

-   :lucide-info:{ .lg .saa-card-icon } **[Sobre o projeto](about/index.md)**

    Propósito, princípios e o que esperar da formação.

-   :lucide-git-pull-request:{ .lg .saa-card-icon } **[Contribuir](internal/workflow.md)**

    Fluxo de contribuição, padrões editoriais e Design System.

</div>
