---
id: M04
title: "Módulo 4 — Métodos de Design e Threat Modeling"
description: Threat modeling como prática de arquitetura — DFDs e fronteiras de confiança, STRIDE, árvores de ataque e abuse cases, MITRE ATT&CK, pontos únicos de falha e dependências, requisitos verificáveis e revisão arquitetural com As-Is/To-Be e validação de controles.
stage: n1
status: published
prerequisites: [M02]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
---

# Módulo 4 — Métodos de Design e Threat Modeling { #modulo-04-metodos-de-design-e-threat-modeling }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 1 — Fundamentos de Arquitetura</span>
<span class="saa-meta">7 aulas · cerca de 8 h de aulas</span>
<span class="saa-status saa-status--published">Published</span>
</div>

## Resumo

!!! abstract "Sobre este módulo"

    Threat modeling é a forma disciplinada de responder, ainda no desenho, a quatro perguntas: o que estamos construindo, o que pode dar errado, o que vamos fazer a respeito e se fizemos um bom trabalho. Este módulo percorre essas perguntas com métodos complementares — cada um encontra um tipo de problema que os outros deixam passar — e termina na revisão arquitetural, onde o resultado vira decisão, requisito, condição e risco residual com dono.

Ao concluir o módulo, você será capaz de:

- Desenhar DFDs com fronteiras de confiança e priorizar os fluxos que as atravessam.
- Aplicar STRIDE por elemento e registrar ameaças acionáveis.
- Construir árvores de ataque e abuse cases para objetivos de adversário e fraudes de negócio.
- Descrever cenários de risco como sequências de táticas e técnicas do MITRE ATT&CK v20.
- Encontrar pontos únicos de falha e de comprometimento e limitar o raio de impacto.
- Transformar ameaças em requisitos verificáveis, apoiados no OWASP ASVS 5.0.
- Conduzir revisões com As-Is/To-Be e validar controles por exame, entrevista e teste.

## Aulas

<!-- lessons:start -->

| Aula | Tema | Profundidade | Duração |
|:---|:---|:---|:---|
| [Aula 01](01-data-flow-diagrams.md) | Data Flow Diagrams e fluxos de confiança | Fundamental | 60 min |
| [Aula 02](02-stride.md) | STRIDE aplicado à arquitetura | Professional | 75 min |
| [Aula 03](03-attack-trees-abuse-cases.md) | Attack trees e abuse cases | Professional | 60 min |
| [Aula 04](04-mitre-attack-scenarios.md) | MITRE ATT&CK para cenários de ataque | Professional | 75 min |
| [Aula 05](05-single-points-of-failure.md) | Pontos únicos de falha e análise de dependências | Professional | 60 min |
| [Aula 06](06-threats-to-requirements.md) | De ameaças a requisitos de segurança | Architect | 75 min |
| [Aula 07](07-architecture-review-validation.md) | Revisão arquitetural, As-Is/To-Be e validação de controles | Architect | 75 min |

<!-- lessons:end -->

## Mapa do módulo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m04-module-map.mmd"
```

<figcaption>Figura 1 — Mapa do Módulo 4.</figcaption>
</figure>

## Pré-requisitos

| Pré-requisito | Por quê | Como validar |
|:---|:---|:---|
| [Módulo 2](../02-security-architecture/index.md) | Rastreabilidade, requisitos de negócio e ADRs são usados em todas as aulas | [Avaliação do Módulo 2](../../assessments/m02-security-architecture.md) |
| [Módulo 1 — Aula 03](../01-security-fundamentals/03-trust-boundaries-attack-surface.md) | Fronteiras de confiança e superfície de ataque | Questões de compreensão da aula |
| [Módulo 3 — Aula 06](../03-governance-risk/06-risk-assessment-register.md) | Ameaças viram cenários do risk register | Questões de compreensão da aula |

## Atividades

- Exercício de decisão ao final de cada aula, com matriz de decisão ponderada, pesos justificados, risco residual e as condições que mudariam a escolha. A matriz apoia a decisão, mas não substitui o julgamento profissional nem o threat model que a fundamenta.
- O exercício encadeado das Aulas 01 a 06 sobre a integração de laudos da Lumen forma um threat model completo, do DFD aos requisitos.

## Organizações fictícias usadas no módulo

| Organização | Perfil |
|:---|:---|
| **Lumen Saúde** | Agendamento, portal do paciente e integração de laudos com laboratório parceiro. |
| **Meridiana Distribuidora** | Cenário de ransomware (Caso A), fraude no cadastro de fornecedores e dependências da expedição. |
| **Aurora Pagamentos** | Integração de parceiros por arquivos e nova API de antecipação de recebíveis. |

## Referências principais do módulo

- Threat Modeling Manifesto Working Group. *Threat Modeling Manifesto*. <https://threatmodelingmanifesto.org/>.
- Microsoft. *Threats — Microsoft Threat Modeling Tool*. <https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats>.
- B. Schneier. *Attack Trees*. Dr. Dobb's Journal, 1999. <https://www.schneier.com/academic/archives/1999/12/attack_trees.html>.
- J. McDermott, C. Fox. *Using Abuse Case Models for Security Requirements Analysis*. ACSAC, 1999.
- MITRE. *ATT&CK* v20. <https://attack.mitre.org/>.
- H. Adkins et al. *Building Secure and Reliable Systems*. O'Reilly, 2020. <https://google.github.io/building-secure-and-reliable-systems/raw/toc.html>.
- OWASP. *ASVS 5.0.0*. <https://owasp.org/www-project-ASVS/>.
- NIST. *SP 800-53A Rev. 5*. <https://csrc.nist.gov/pubs/sp/800/53/a/r5/final>.
