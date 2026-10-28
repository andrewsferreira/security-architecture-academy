---
id: M01
title: "Módulo 1 — Fundamentos de Segurança"
description: As propriedades que a segurança protege, os princípios de design seguro, fronteiras de confiança e superfície de ataque, criptografia aplicada, PKI e gestão de chaves, a linguagem de risco e os modelos formais de controle de acesso e integridade.
stage: n0
status: published
prerequisites: [M00]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# Módulo 1 — Fundamentos de Segurança { #modulo-01-fundamentos-de-seguranca }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 — Fundamentos de Tecnologia e Segurança</span>
<span class="saa-meta">7 aulas · cerca de 8 h de aulas</span>
<span class="saa-status saa-status--published">Published</span>
</div>

## Resumo

!!! abstract "Sobre este módulo"

    Este módulo constrói o **vocabulário e o raciocínio** que todas as decisões de arquitetura usam: o que se protege (propriedades), como se decide (princípios), onde se aplica (fronteiras e superfície de ataque), com que mecanismos (criptografia e PKI), por que se investe (risco) e com que fundamentos formais (modelos de controle de acesso e integridade). Não é um catálogo de definições: cada aula termina com uma decisão a ser tomada.

Ao concluir o módulo, você será capaz de:

- Expressar requisitos em termos de propriedades de segurança, inclusive autorização, não repúdio e responsabilização.
- Aplicar princípios de design seguro — de least privilege a fail-safe defaults — a decisões concretas.
- Mapear fronteiras de confiança e superfície de ataque de um sistema.
- Escolher mecanismos criptográficos adequados e reconhecer erros comuns de uso.
- Explicar como PKI e TLS estabelecem confiança e o que muda com certificados de validade curta e criptografia pós-quântica.
- Usar com precisão os termos ameaça, vulnerabilidade, exposição, risco e controle.
- Relacionar Bell-LaPadula, Biba, Clark-Wilson e Brewer-Nash a controles reais.

## Aulas

<!-- lessons:start -->

| Aula | Tema | Profundidade | Duração |
|:---|:---|:---|:---|
| [Aula 01](01-security-properties.md) | Propriedades de segurança: CIA, autenticidade, autorização e não repúdio | Fundamental | 60 min |
| [Aula 02](02-secure-design-principles.md) | Princípios de design seguro | Fundamental | 75 min |
| [Aula 03](03-trust-boundaries-attack-surface.md) | Trust boundaries, attack surface e responsabilidade compartilhada | Fundamental | 60 min |
| [Aula 04](04-applied-cryptography.md) | Criptografia aplicada: simétrica, assimétrica, hashing e assinaturas | Fundamental | 75 min |
| [Aula 05](05-pki-tls-key-management.md) | PKI, certificados, TLS e gerenciamento de chaves | Fundamental | 75 min |
| [Aula 06](06-threat-vulnerability-risk.md) | Ameaça, vulnerabilidade, risco, exposição e controle | Fundamental | 60 min |
| [Aula 07](07-formal-security-models.md) | Modelos formais: Bell-LaPadula, Biba, Clark-Wilson e Brewer-Nash | Professional | 60 min |

<!-- lessons:end -->

## Mapa do módulo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m01-module-map.mmd"
```

<figcaption>Figura 1 — Mapa do Módulo 1.</figcaption>
</figure>

## Pré-requisitos

| Pré-requisito | Por quê | Como validar |
|:---|:---|:---|
| [Módulo Inicial](../00-foundations/index.md) | As aulas usam isolamento, redes, segmentação e cloud como contexto | Seção A da [avaliação diagnóstica](../../assessments/diagnostic-fundamentals.md) |

## Atividades

- [Avaliação diagnóstica de fundamentos](../../assessments/diagnostic-fundamentals.md) — Seções B e C cobrem este módulo.
- [Laboratório 01 — Mecanismos de segurança na prática](../../labs/lab-01-security-mechanisms.md) — integridade, HMAC, armazenamento de senhas e autorização por objeto (1 h 30 min, sem custo).
- [Avaliação do Módulo 1](../../assessments/m01-security-fundamentals.md) — dez questões situacionais e duas tarefas de aplicação, com gabarito comentado.
- Exercício de decisão ao final de cada aula, com resolução de referência.

## Referências principais do módulo

- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020 — capítulos 1, 6, 9, 10 e 12. <https://www.cl.cam.ac.uk/archive/rja14/book.html>.
- NIST. *SP 800-160 Vol. 1 Rev. 1 — Engineering Trustworthy Secure Systems*. 2022. <https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final>.
- NIST. *SP 800-57 Part 1 Rev. 5 — Recommendation for Key Management*. 2020. <https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final>.
- NIST. *SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments*. 2012. <https://csrc.nist.gov/pubs/sp/800/30/r1/final>.
