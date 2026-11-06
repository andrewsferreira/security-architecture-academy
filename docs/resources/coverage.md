---
title: Cobertura bibliográfica
description: Relatório de cobertura bibliográfica por módulo — fontes verificadas, leitura essencial, capítulos localizados e lidos, conceitos mapeados e lacunas.
---

# Cobertura bibliográfica

Relatório gerado por `scripts/validate_references.py`. Cobertura mede **fundamentação disponível**, não qualidade do conteúdo. Só entram os módulos com conteúdo; os planejados aparecem apenas na nota ao fim da tabela, sem estatísticas.

<!-- coverage:start -->

**193 referências** (119 ligadas aos módulos deste relatório) · 167 capítulos ou seções localizados, 94 efetivamente lidos · 107 conceitos no mapa de conhecimento.

| Verificação | Qtde. |
|:---|---:|
| Verificada | 176 |
| Parcialmente verificada | 12 |
| Indisponível | 2 |
| Pendente | 3 |

**Critério de cobertura:** *Boa* — pelo menos 3 fontes verificadas, leitura essencial, 3 conceitos mapeados e algum trecho efetivamente lido · *Localizada* — fontes e conceitos existem, mas os trechos foram só localizados ou são poucos · *Parcial* — menos de 3 fontes verificadas, sem leitura essencial ou sem conceitos mapeados · *Sem fontes*.

| Módulo | Status | Fontes verificadas | Leitura essencial | Capítulos localizados (lidos) | Conceitos mapeados | Cobertura |
|:---|:---|---:|:---|---:|---:|:---|
| M00 — Fundamentos de Infraestrutura e Computação | published | 21 | `BOOK-ANDERSON-SE3`, `NIST-SP800-160-V1R1`, `NIST-SP800-207`, `NIST-SP800-215`, `AWS-SECURITY-PILLAR`, `AZURE-WAF-SECURITY`, `GCP-ENTERPRISE-FOUNDATIONS`, `NIST-SP800-145`, `BOOK-GOOGLE-BSRS` | 4 (3) | 9 | Boa |
| M01 — Fundamentos de Segurança | published | 22 | `BOOK-ANDERSON-SE3`, `NIST-SP800-160-V1R1`, `NIST-SP800-207`, `AWS-SECURITY-PILLAR`, `NIST-SP800-145`, `NIST-CSF-2`, `NIST-SP800-30-R1`, `NIST-SP800-57-PT1-R5`, `BOOK-GOOGLE-BSRS` | 21 (14) | 22 | Boa |
| M02 — Introdução à Arquitetura de Segurança | published | 32 | `BOOK-ANDERSON-SE3`, `NIST-SP800-160-V1R1`, `SABSA-W101`, `SABSA-W105`, `NIST-SP800-207`, `GCP-ENTERPRISE-FOUNDATIONS`, `NIST-CSF-2`, `BOOK-GOOGLE-BSRS` | 20 (9) | 20 | Boa |
| M03 — Governança, Riscos e Controles | published | 32 | `BOOK-ANDERSON-SE3`, `NIST-CSF-2`, `NIST-SP800-30-R1`, `NIST-SP800-37-R2`, `LGPD-L13709`, `BOOK-GOOGLE-BSRS` | 28 (24) | 24 | Boa |
| M04 — Métodos de Design e Threat Modeling | published | 22 | `BOOK-ANDERSON-SE3`, `NIST-SP800-160-V1R1`, `NIST-CSF-2`, `NIST-SP800-30-R1`, `NIST-SP800-37-R2`, `SCHNEIER-ATTACK-TREES-1999`, `TM-MANIFESTO`, `BOOK-GOOGLE-BSRS` | 11 (5) | 14 | Boa |
| M05 — Network Security Architecture | published | 23 | `BOOK-ANDERSON-SE3`, `NIST-SP800-207`, `NIST-SP800-215`, `NIST-SP800-63-4`, `BOOK-GOOGLE-BSRS` | 20 (17) | 14 | Boa |
| M06 — Identity & Access Management | published | 34 | `BOOK-ANDERSON-SE3`, `NIST-SP800-207`, `GCP-ENTERPRISE-FOUNDATIONS`, `NIST-SP800-63-4`, `RFC-9700`, `LGPD-L13709`, `BOOK-GOOGLE-BSRS` | 11 (9) | 17 | Boa |
| M07 — Zero Trust Architecture | published | 22 | `NIST-SP800-207`, `NIST-SP800-215`, `NIST-CSF-2`, `NIST-SP800-63-4`, `RFC-9700`, `BOOK-GOOGLE-BSRS` | 14 (10) | 22 | Boa |
| M08 — On-Premises e Sistemas Legados | published | 33 | `BOOK-ANDERSON-SE3`, `NIST-SP800-207`, `CISA-STOPRANSOMWARE-GUIDE` | 3 (3) | 14 | Boa |

Módulos planejados (M09, M10, M11, M12, M13, M14, M15, M16, M17) não entram no relatório.

**Lacunas:** nenhuma.

<!-- coverage:end -->
