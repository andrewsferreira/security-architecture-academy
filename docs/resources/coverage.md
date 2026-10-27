---
title: Cobertura bibliográfica
description: Relatório de cobertura bibliográfica por módulo — fontes verificadas, leitura essencial, capítulos localizados e lidos, conceitos mapeados e lacunas.
---

# Cobertura bibliográfica

Relatório gerado por `scripts/validate_references.py`. Cobertura mede **fundamentação disponível**, não qualidade do conteúdo: módulos planejados podem ter boa cobertura antes de existir qualquer aula.

<!-- coverage:start -->

**189 referências** · 166 capítulos ou seções localizados, 93 efetivamente lidos · 53 conceitos no mapa de conhecimento.

| Verificação | Qtde. |
|:---|---:|
| Verificada | 171 |
| Parcialmente verificada | 12 |
| Indisponível | 2 |
| Pendente | 4 |

**Critério de cobertura:** *Boa* — pelo menos 3 fontes verificadas, leitura essencial, 3 conceitos mapeados e algum trecho efetivamente lido · *Localizada* — fontes e conceitos existem, mas os trechos foram só localizados ou são poucos · *Parcial* — menos de 3 fontes verificadas, sem leitura essencial ou sem conceitos mapeados · *Sem fontes*.

| Módulo | Status | Fontes verificadas | Leitura essencial | Capítulos localizados (lidos) | Conceitos mapeados | Cobertura |
|:---|:---|---:|:---|---:|---:|:---|
| M00 — Fundamentos de Infraestrutura e Computação | published | 12 | `BOOK-ANDERSON-SE3`, `NIST-SP800-215`, `NIST-SP800-145` | 4 (3) | 9 | Boa |
| M01 — Fundamentos de Segurança | published | 17 | `BOOK-ANDERSON-SE3`, `NIST-SP800-160-V1R1`, `NIST-SP800-30-R1`, `NIST-SP800-57-PT1-R5`, `BOOK-GOOGLE-BSRS` | 21 (14) | 21 | Boa |
| M02 — Introdução à Arquitetura de Segurança | published | 29 | `BOOK-ANDERSON-SE3`, `NIST-SP800-160-V1R1`, `SABSA-W101`, `SABSA-W105`, `NIST-SP800-207`, `NIST-CSF-2`, `BOOK-GOOGLE-BSRS` | 20 (9) | 20 | Boa |
| M03 — Governança, Riscos e Controles | planned | 29 | `BOOK-ANDERSON-SE3`, `NIST-CSF-2`, `NIST-SP800-30-R1`, `NIST-SP800-37-R2`, `LGPD-L13709`, `BOOK-GOOGLE-BSRS` | 28 (24) | 9 | Boa |
| M04 — Métodos de Design e Threat Modeling | planned | 13 | `BOOK-ANDERSON-SE3`, `NIST-SP800-160-V1R1`, `SCHNEIER-ATTACK-TREES-1999`, `TM-MANIFESTO`, `BOOK-GOOGLE-BSRS` | 11 (5) | 4 | Boa |
| M05 — Network Security Architecture | planned | 15 | `BOOK-ANDERSON-SE3`, `NIST-SP800-207`, `NIST-SP800-215`, `BOOK-GOOGLE-BSRS` | 19 (16) | 3 | Boa |
| M06 — Identity & Access Management | planned | 24 | `BOOK-ANDERSON-SE3`, `NIST-SP800-207`, `NIST-SP800-63-4`, `RFC-9700`, `BOOK-GOOGLE-BSRS` | 11 (9) | 5 | Boa |
| M07 — Zero Trust Architecture | planned | 12 | `NIST-SP800-207`, `NIST-SP800-215`, `NIST-SP800-63-4`, `BOOK-GOOGLE-BSRS` | 14 (10) | 7 | Boa |
| M08 — On-Premises e Sistemas Legados | planned | 18 | `BOOK-ANDERSON-SE3`, `CISA-STOPRANSOMWARE-GUIDE` | 3 (3) | 3 | Boa |
| M09 — AWS Security Architecture | planned | 41 | `AWS-SECURITY-PILLAR`, `AWS-SHARED-RESPONSIBILITY`, `NIST-SP800-145`, `AWS-IAM-BEST-PRACTICES` | 9 (9) | 4 | Boa |
| M10 — Azure e Google Cloud | planned | 33 | `NIST-SP800-215`, `AZURE-LANDING-ZONE`, `AZURE-WAF-SECURITY`, `GCP-ENTERPRISE-FOUNDATIONS`, `GCP-RESOURCE-HIERARCHY`, `NIST-SP800-145`, `GCP-IAM-OVERVIEW` | 0 (0) | 4 | Localizada |
| M11 — Hybrid & Multicloud Security Architecture | planned | 61 | `NIST-SP800-207`, `AWS-SECURITY-PILLAR`, `AWS-SHARED-RESPONSIBILITY`, `AZURE-WAF-SECURITY`, `GCP-ENTERPRISE-FOUNDATIONS`, `NIST-SP800-145` | 3 (2) | 8 | Boa |
| M12 — Application Security Architecture | planned | 13 | `BOOK-ANDERSON-SE3`, `RFC-9700`, `TM-MANIFESTO`, `BOOK-GOOGLE-BSRS` | 8 (4) | 4 | Boa |
| M13 — Data Security Architecture | planned | 18 | `BOOK-ANDERSON-SE3`, `LGPD-L13709`, `NIST-SP800-57-PT1-R5` | 8 (7) | 6 | Boa |
| M14 — Vulnerability & Exposure Management Architecture | planned | 10 | `BOOK-ANDERSON-SE3`, `NIST-SP800-30-R1`, `BOOK-GOOGLE-BSRS` | 6 (5) | 4 | Boa |
| M15 — Security Operations & Resilience Architecture | planned | 19 | `BOOK-ANDERSON-SE3`, `BOOK-GOOGLE-BSRS`, `CISA-STOPRANSOMWARE-GUIDE` | 11 (3) | 4 | Boa |
| M16 — Enterprise Security Architecture | planned | 31 | `BOOK-ANDERSON-SE3`, `NIST-SP800-160-V1R1`, `SABSA-W101`, `SABSA-W105`, `NIST-SP800-207`, `AWS-SECURITY-PILLAR`, `AZURE-WAF-SECURITY`, `GCP-ENTERPRISE-FOUNDATIONS`, `NIST-CSF-2`, `NIST-SP800-37-R2`, `LGPD-L13709`, `BOOK-GOOGLE-BSRS` | 13 (7) | 11 | Boa |
| M17 — Estudos de Caso e Projeto Final | planned | 2 | `NIST-SP800-160-V1R1`, `NIST-SP800-63-4` | 0 (0) | 0 | Parcial |

**Lacunas:** M17 (parcial)

<!-- coverage:end -->
