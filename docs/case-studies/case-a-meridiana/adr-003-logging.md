---
title: "ADR-003 — Centralização de logs com SIEM e serviço gerenciado de detecção e resposta"
description: Decisão de arquitetura do Caso A sobre logs, detecção e resposta na Meridiana Distribuidora — alternativas, matriz de decisão, consequências e risco residual.
status: published
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# ADR-003 — Centralização de logs com SIEM e serviço gerenciado de detecção e resposta

**Status:** Aceita (exemplo do Caso A) · **Data:** 2026-10-23 · **Decisores:** arquiteto de segurança, gerente de TI · **Consultados:** jurídico, corretora do seguro

## Contexto

Os logs da Meridiana ficam apenas nos próprios servidores, por cerca de sete dias, e ninguém os analisa. A empresa provavelmente só perceberia uma intrusão no momento da criptografia. Não há SOC, e a equipe de TI tem nove pessoas, uma delas dedicada à segurança em meio período; a decisão de contratar mais um analista já foi tomada. A seguradora pergunta sobre monitoramento e capacidade de resposta. Os eventos relevantes estão no Active Directory, na VPN, no firewall, no Microsoft 365 e, após o [ADR-002](adr-002-segmentation.md), no firewall interno, além do EDR a ser implantado.

## Requisitos e riscos relacionados

- REQ-09 — EDR com eventos monitorados 24x7.
- REQ-10 — eventos no SIEM em até 15 minutos, retidos por 12 meses.
- Riscos R1, R2 e R3 da [solução do caso](solution.md#analise-de-riscos).

## Alternativas consideradas

- **A — SIEM operado pela própria equipe:** licenciar um SIEM e montar regras e rotinas de análise internamente.
- **B — SIEM com serviço gerenciado de detecção e resposta (MDR):** o provedor monitora 24x7, investiga alertas e executa ações de contenção acordadas; a equipe interna trata os incidentes confirmados.
- **C — Pilha open source própria:** coleta e análise com ferramentas open source hospedadas no datacenter.

| Critério | Peso | A — SIEM próprio | B — SIEM + MDR | C — Open source |
|:---|:---|:---|:---|:---|
| Cobertura de monitoramento 24x7 | 3 | 1 | 3 | 1 |
| Capacidade da equipe para operar | 3 | 1 | 3 | 1 |
| Custo no ano 1 | 2 | 2 | 1 | 3 |
| Controle sobre regras e dados | 1 | 3 | 2 | 3 |
| Aderência às exigências da seguradora | 2 | 2 | 3 | 1 |
| **Total ponderado** | | **17** | **28** | **17** |

O SIEM próprio (A) e a pilha open source (C) dariam visibilidade, mas ninguém estaria olhando às 3 da manhã de um domingo — o horário em que ataques de ransomware costumam ser executados. A pilha open source tem o menor custo de licença, mas o maior custo de operação para uma equipe que não tem esse tempo.

## Decisão

Vamos contratar um **SIEM com serviço gerenciado de detecção e resposta (MDR) 24x7**. Fontes prioritárias, nesta ordem: controladores de domínio, VPN e acesso remoto, EDR, Microsoft 365, firewall de borda, firewall interno e servidores do ERP. O contrato definirá tempos de notificação por severidade, ações de contenção que o provedor pode executar sem aprovação (por exemplo, isolar uma estação pelo EDR) e a retenção de 12 meses, com exportação dos dados ao fim do contrato.

## Consequências

- **Positivas:** monitoramento 24x7 sem SOC próprio; casos de uso de detecção mantidos por especialistas; evidência direta para a seguradora e para a avaliação da construtora.
- **Negativas:** dependência de um terceiro com acesso privilegiado a dados de segurança; custo recorrente relevante (o maior item do orçamento); necessidade de um processo interno claro para tratar o que o provedor escalar, inclusive fora do horário comercial; risco de *lock-in* se os dados não forem exportáveis.
- **Neutras:** a analista de segurança deixa de analisar logs manualmente e passa a gerir o contrato e a resposta.

## Risco residual

A detecção depende da qualidade do provedor e da capacidade interna de responder ao que ele escalar. **Dono do risco:** gerente de TI, com revisão contratual anual baseada em indicadores (tempo de notificação, falsos positivos, incidentes não detectados em exercícios).

## Verificação

- 100% das fontes prioritárias enviando eventos, verificado mensalmente pelo provedor e pela equipe interna.
- Exercício semestral simulado de intrusão para medir tempo de detecção e de notificação.
- Teste de exportação dos dados antes do primeiro ano de contrato.

## Revisão

Na renovação contratual anual, ou se a empresa formar um SOC próprio.

## Relacionamentos

- Recebe eventos das decisões do [ADR-001](adr-001-remote-access.md) e do [ADR-002](adr-002-segmentation.md).
- O plano de resposta a incidentes deve ser alinhado com o provedor e com as exigências da seguradora.
