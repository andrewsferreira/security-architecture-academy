---
title: Dependências entre módulos
description: Grafo de pré-requisitos entre os 18 módulos da Security Architecture Academy, gerado a partir do manifesto do currículo.
---

# Dependências entre módulos

O grafo abaixo mostra quais módulos são pré-requisitos de quais. Ele é **gerado automaticamente** a partir do manifesto, então qualquer mudança de pré-requisito aparece aqui sem edição manual. Módulos com contorno destacado já têm conteúdo produzido.

<!-- dependencies:start -->

```mermaid
flowchart TB
  accTitle: Dependências entre os módulos
  accDescr: Grafo de pré-requisitos gerado a partir do manifesto do currículo. Cada seta liga um módulo pré-requisito ao módulo que depende dele; os módulos estão agrupados pelos seis níveis do currículo.

  subgraph N0["Nível 0 — Fundamentos de Tecnologia e Segurança"]
    direction LR
    M00["Módulo Inicial · Fundamentos de Infraestrutura e Computação"]
    M01["Módulo 1 · Fundamentos de Segurança"]
  end
  subgraph N1["Nível 1 — Fundamentos de Arquitetura"]
    direction LR
    M02["Módulo 2 · Introdução à Arquitetura de Segurança"]
    M03["Módulo 3 · Governança, Riscos e Controles"]
    M04["Módulo 4 · Métodos de Design e Threat Modeling"]
  end
  subgraph N2["Nível 2 — Arquiteturas de Infraestrutura"]
    direction LR
    M05["Módulo 5 · Network Security Architecture"]
    M06["Módulo 6 · Identity & Access Management"]
    M07["Módulo 7 · Zero Trust Architecture"]
    M08["Módulo 8 · On-Premises e Sistemas Legados"]
  end
  subgraph N3["Nível 3 — Arquitetura Cloud e Híbrida"]
    direction LR
    M09["Módulo 9 · AWS Security Architecture"]
    M10["Módulo 10 · Azure e Google Cloud"]
    M11["Módulo 11 · Hybrid & Multicloud Security Architecture"]
  end
  subgraph N4["Nível 4 — Arquitetura de Segurança Aplicada"]
    direction LR
    M12["Módulo 12 · Application Security Architecture"]
    M13["Módulo 13 · Data Security Architecture"]
    M14["Módulo 14 · Vulnerability & Exposure Management Architecture"]
    M15["Módulo 15 · Security Operations & Resilience Architecture"]
  end
  subgraph N5["Nível 5 — Arquitetura Corporativa Avançada"]
    direction LR
    M16["Módulo 16 · Enterprise Security Architecture"]
    M17["Módulo 17 · Estudos de Caso e Projeto Final"]
  end
  C01["C01 · Segurança de IA/LLM e identidades não humanas"]

  M00 --> M01
  M00 --> M02
  M01 --> M02
  M02 --> M03
  M02 --> M04
  M00 --> M05
  M02 --> M05
  M01 --> M06
  M02 --> M06
  M05 --> M07
  M06 --> M07
  M05 --> M08
  M06 --> M08
  M05 --> M09
  M06 --> M09
  M05 --> M10
  M06 --> M10
  M06 --> M11
  M07 --> M11
  M04 --> M12
  M06 --> M12
  M01 --> M13
  M03 --> M13
  M03 --> M14
  M05 --> M15
  M06 --> M15
  M03 --> M16
  M11 --> M16
  M16 --> M17
  M06 --> C01
  M12 --> C01

  classDef zone fill:transparent,stroke:#64748b,stroke-width:1px,stroke-dasharray:4 3
  classDef active stroke:#0e9fb8,stroke-width:3px
  class N0,N1,N2,N3,N4,N5 zone
  class M00,M01,M02 active
```

<!-- dependencies:end -->

## Como usar o grafo

- **Ordem mínima:** antes de iniciar um módulo, conclua os módulos que apontam para ele.
- **Revisão de fundamentos:** módulos dos Níveis 2 a 5 retomam conceitos do Módulo Inicial e do Módulo 1 sempre que necessário; quem já domina esses fundamentos pode validar o conhecimento na [avaliação diagnóstica](../assessments/diagnostic-fundamentals.md) e avançar.
- **Ordem de produção ≠ ordem de estudo:** o Módulo 2 foi produzido primeiro por ser a referência de qualidade do curso. A ordem recomendada de estudo está no [plano de estudo](../learning-paths/study-plan.md).

## Justificativa das principais dependências

| Módulo | Depende de | Por quê |
|:---|:---|:---|
| Módulo 2 Introdução à Arquitetura | Módulo Inicial e Módulo 1 | Ler diagramas e conhecer princípios de segurança é condição para discutir arquitetura. |
| Módulo 3 — Governança, Riscos e Controles | Módulo 2 | Seleção de controles e arquitetura baseada em risco pressupõem o vocabulário de princípios, padrões e requisitos. |
| Módulo 7 Zero Trust | Módulos 5 e 6 | Zero Trust combina decisões de identidade com pontos de aplicação na rede e nos workloads. |
| Módulo 11 Hybrid & Multicloud | Módulos 6 e 7 | A integração híbrida depende de identidade federada e de decisões de acesso independentes de localização. |
| Módulo 16 — Enterprise Security Architecture | Módulos 3 e 11 | Governança corporativa entre empresas exige gestão de riscos e domínio de ambientes heterogêneos. |
| Módulo 17 Projeto Final | Módulo 16 | O projeto integra todas as competências em uma proposta corporativa completa. |
