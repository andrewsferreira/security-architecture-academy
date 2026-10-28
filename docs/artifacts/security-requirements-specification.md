---
id: ART-SRS
title: "Modelo: Security Requirements Specification"
description: Modelo editável de especificação de requisitos de segurança, com contexto de negócio, atributos com métricas, requisitos classificados e matriz de rastreabilidade até a verificação.
status: published
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# Modelo: Security Requirements Specification

A especificação de requisitos de segurança transforma objetivos de negócio, ameaças e obrigações em requisitos verificáveis. Fundamentos na [Aula 07 do Módulo 2](../modules/02-security-architecture/07-business-driven-requirements.md).

## Modelo

```markdown
# Security Requirements Specification — <Nome da solução>

**Versão:** <x.y> · **Data:** <AAAA-MM-DD> · **Responsável:** <papel>
**Aprovado por (negócio):** <papel> · **Aprovado por (segurança):** <papel>

## 1. Contexto de negócio

- **Objetivo:** <o que a solução deve alcançar, com métrica>
- **Ativos de valor:** <dados, processos, receita, reputação>
- **Partes interessadas:** <quem ganha e quem perde se algo der errado>
- **Apetite a risco declarado:** <o que é e o que não é aceitável — confirmado por quem responde pelo negócio>

## 2. Restrições

| ID | Restrição | Origem |
|:---|:---|:---|
| RST-01 | <restrição> | <lei, contrato, norma, padrão corporativo> |

## 3. Atributos de negócio

| Atributo | Definição | Métrica e meta |
|:---|:---|:---|
| <Disponível> | <o que significa para esta solução> | <métrica e meta> |

## 4. Ameaças consideradas

| ID | Ameaça | Componente ou fluxo afetado |
|:---|:---|:---|
| AME-01 | <ameaça> | <componente> |

## 5. Requisitos de segurança

| ID | Requisito | Categoria | Origem | Prioridade |
|:---|:---|:---|:---|:---|
| REQ-01 | <O sistema …, verificável e neutro em produto> | <Funcional · Qualidade · Restrição> | <atributo, ameaça, restrição> | <Obrigatório · Desejável> |

## 6. Rastreabilidade e verificação

| Requisito | Controles | Método de verificação | Critério de aceitação | Evidência |
|:---|:---|:---|:---|:---|
| REQ-01 | <controle> | <teste, inspeção, medição contínua> | <condição objetiva> | <onde fica a evidência> |

## 7. Modos degradados (obrigatório em soluções híbridas)

| Falha | Comportamento esperado |
|:---|:---|
| <conectividade entre ambientes indisponível> | <o que acontece com autenticação, autorização e registro> |

## 8. Conflitos e decisões

- <conflito entre atributos> → <ADR-NNN>

## 9. Riscos residuais

| Risco | Dono | Data de revisão |
|:---|:---|:---|
| <risco> | <papel> | <data> |
```

## Critérios de qualidade de cada requisito

| Critério | Pergunta |
|:---|:---|
| Específico | Diz exatamente o que precisa ser verdade? |
| Verificável | Existe um método objetivo para comprovar? |
| Rastreável | Aponta atributo, ameaça ou restrição de origem? |
| Necessário | O que se perde se for removido? |
| Viável | É implementável com as restrições do projeto? |
| Neutro em produto | Descreve o resultado, não a ferramenta? |

## Exemplos preenchidos

- [Requisitos de segurança do Caso A — Meridiana](../case-studies/case-a-meridiana/solution.md#requisitos-de-seguranca)
- [Matriz de rastreabilidade do pagamento por link](../modules/02-security-architecture/07-business-driven-requirements.md#exemplo-empresarial), na Aula 07 do Módulo 2
