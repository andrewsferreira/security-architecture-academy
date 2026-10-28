---
id: M03
title: "Módulo 3 — Governança, Riscos e Controles"
description: Governança de segurança com o NIST CSF 2.0, o Risk Management Framework, seleção e tailoring de controles, o papel da ISO/IEC 27001, da LGPD e do PCI DSS, análise de impacto no negócio, avaliação e tratamento de riscos, catálogo de controles ligado à arquitetura e indicadores para a governança.
stage: n1
status: published
prerequisites: [M02]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
---

# Módulo 3 — Governança, Riscos e Controles { #modulo-03-governanca-riscos-e-controles }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 1 — Fundamentos de Arquitetura</span>
<span class="saa-meta">8 aulas · cerca de 10 h de aulas</span>
<span class="saa-status saa-status--published">Published</span>
</div>

## Resumo

!!! abstract "Sobre este módulo"

    Toda decisão de arquitetura de segurança responde, explícita ou implicitamente, a uma decisão de governança: quanto risco a organização aceita, quem responde por ele e quais resultados importam primeiro. Este módulo dá ao arquiteto as ferramentas para trabalhar nessa fronteira — enquadrar riscos, selecionar controles proporcionais, distinguir obrigações legais de referências voluntárias, transformar impacto no negócio em requisitos de recuperação e medir se a arquitetura está funcionando.

Ao concluir o módulo, você será capaz de:

- Usar o NIST CSF 2.0 para descrever perfis atual e alvo e transformar lacunas em plano de ação.
- Aplicar o raciocínio do Risk Management Framework a sistemas fora do governo norte-americano.
- Selecionar e ajustar controles a partir de baselines, com justificativas registradas.
- Classificar referências como lei, contrato ou adoção voluntária e derivar requisitos de arquitetura da LGPD e do PCI DSS.
- Conduzir uma BIA e derivar RTO e RPO verificáveis.
- Manter um risk register vivo, ligado a apetite, tolerância, donos e ADRs.
- Construir um catálogo interno de controles rastreável do risco à evidência.
- Reportar à governança com medidas de implementação, eficácia, eficiência e impacto.

!!! info "Frameworks não são obrigações legais universais"

    NIST CSF, SP 800-53, CIS Controls e ISO/IEC 27001 são referências voluntárias, a menos que um contrato ou regulação setorial as exija. A LGPD é lei. O módulo deixa explícita a natureza de cada referência; a interpretação jurídica de casos concretos cabe ao jurídico e ao encarregado de dados.

## Aulas

<!-- lessons:start -->

| Aula | Tema | Profundidade | Duração |
|:---|:---|:---|:---|
| [Aula 01](01-governance-csf.md) | Governança de segurança e o NIST CSF 2.0 | Fundamental | 75 min |
| [Aula 02](02-nist-rmf.md) | NIST Risk Management Framework (SP 800-37) | Professional | 75 min |
| [Aula 03](03-control-selection-tailoring.md) | Seleção e tailoring de controles: SP 800-53 e CIS Controls | Professional | 90 min |
| [Aula 04](04-iso-lgpd-pci.md) | ISO/IEC 27001/27002, LGPD e PCI DSS: propósito e escopo | Fundamental | 75 min |
| [Aula 05](05-bia-rto-rpo.md) | Business Impact Analysis, RTO e RPO | Professional | 60 min |
| [Aula 06](06-risk-assessment-register.md) | Risk assessment, risk register e tratamento de riscos | Professional | 90 min |
| [Aula 07](07-control-catalog-risk-architecture.md) | Catálogo de controles e arquitetura baseada em risco | Architect | 75 min |
| [Aula 08](08-metrics-maturity-reporting.md) | Indicadores, maturidade e reporte à governança | Architect | 60 min |

<!-- lessons:end -->

## Mapa do módulo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m03-module-map.mmd"
```

<figcaption>Figura 1 — Mapa do Módulo 3.</figcaption>
</figure>

## Pré-requisitos

| Pré-requisito | Por quê | Como validar |
|:---|:---|:---|
| [Módulo 2](../02-security-architecture/index.md) | O módulo usa princípios, padrões, exceções, rastreabilidade e ADRs | [Avaliação do Módulo 2](../../assessments/m02-security-architecture.md) |
| [Módulo 1 — Aula 06](../01-security-fundamentals/06-threat-vulnerability-risk.md) | A linguagem de risco é usada em todas as aulas | Questões de compreensão da aula |

## Atividades

- Exercício de decisão ao final de cada aula, com matriz de decisão ponderada, pesos justificados, risco residual e as condições que mudariam a escolha. A matriz organiza a comparação; a decisão continua dependendo do julgamento profissional e da análise de riscos — uma obrigação legal ou um limite de tolerância elimina uma opção antes de qualquer soma.
- O cenário de ransomware do [Caso A — Meridiana Distribuidora](../../case-studies/case-a-meridiana/index.md) é o contexto dos exemplos de BIA, risk register e catálogo de controles.

## Organizações fictícias usadas no módulo

| Organização | Perfil |
|:---|:---|
| **Meridiana Distribuidora** | Distribuidora com três centros de distribuição, datacenter próprio e risco de ransomware (Caso A). |
| **Lumen Saúde** | Rede de clínicas com portal do paciente e dados de saúde (dados pessoais sensíveis na LGPD). |
| **Aurora Pagamentos** | Empresa de meios de pagamento sujeita a PCI DSS e com clientes que exigem ISO/IEC 27001. |

## Referências principais do módulo

- NIST. *The NIST Cybersecurity Framework (CSF) 2.0*. CSWP 29, 2024. <https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final>.
- NIST. *SP 800-37 Rev. 2 — Risk Management Framework*. 2018. <https://csrc.nist.gov/pubs/sp/800/37/r2/final>.
- NIST. *SP 800-53 Rev. 5* (Release 5.2.0) e *SP 800-53B*. <https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final>.
- NIST. *SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments*. 2012. <https://csrc.nist.gov/pubs/sp/800/30/r1/final>.
- NIST. *SP 800-34 Rev. 1 — Contingency Planning Guide*. 2010. <https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final>.
- NIST. *SP 800-55 Vol. 1 — Measurement Guide for Information Security*. 2024. <https://csrc.nist.gov/pubs/sp/800/55/v1/final>.
- Brasil. *Lei nº 13.709/2018 — LGPD*. <https://planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>.
- CIS. *CIS Controls v8.1*. <https://www.cisecurity.org/controls/v8-1>.
