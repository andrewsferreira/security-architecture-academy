---
id: ART-RR
title: "Modelo: Risk Register"
description: Modelo editável de risk register para arquitetura de segurança — cenário com fonte, evento, vulnerabilidades e condições predisponentes, probabilidade e impacto justificados, tratamento, controles e ADRs, residual comparado à tolerância, dono, obrigações e revisão —, com escalas, ciclo de vida, critérios de qualidade e exemplo preenchido.
status: published
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
---

# Modelo: Risk Register

O risk register registra os **cenários de risco** que orientam decisões de arquitetura: o que pode acontecer, por que é possível, quanto importa, o que foi decidido e quem responde pela decisão. Fundamentos na [Aula 06 do Módulo 3](../modules/03-governance-risk/06-risk-assessment-register.md) (avaliação, register e tratamento), com a linguagem de risco da [Aula 06 do Módulo 1](../modules/01-security-fundamentals/06-threat-vulnerability-risk.md) e a ligação com controles da [Aula 07 do Módulo 3](../modules/03-governance-risk/07-control-catalog-risk-architecture.md).

## Quando usar

- Ao avaliar uma arquitetura (com o [Security Architecture Assessment](security-architecture-assessment.md)) ou um novo projeto.
- Quando um threat model ([Threat Model](threat-model.md)) produz ameaças que merecem decisão do negócio.
- Para justificar controles na [Security Control Matrix](security-control-matrix.md) e decisões em [ADRs](architecture-decision-record.md).

## Escalas

Defina as escalas **antes** de avaliar e use as mesmas em todo o register. Exemplo de escala qualitativa:

| Nível | Probabilidade | Impacto |
|:---|:---|:---|
| **Muito alto** | Já ocorreu ou ocorre com frequência no setor, sem barreira efetiva | Excede o MTD de processo crítico; exposição de dados sensíveis em massa; obrigação legal descumprida |
| **Alto** | Caminho conhecido e explorável, com barreiras fracas | Interrupção relevante dentro do MTD; exposição limitada de dados sensíveis |
| **Médio** | Exige condições adicionais ou esforço relevante do atacante | Impacto localizado, recuperável sem perda relevante |
| **Baixo** | Improvável com os controles e o contexto atuais | Impacto pequeno e reversível |

| Probabilidade × impacto | Baixo | Médio | Alto | Muito alto |
|:---|:---|:---|:---|:---|
| **Muito alta** | Médio | Alto | Crítico | Crítico |
| **Alta** | Médio | Alto | Alto | Crítico |
| **Média** | Baixo | Médio | Alto | Alto |
| **Baixa** | Baixo | Baixo | Médio | Médio |

A matriz é uma convenção da organização, não uma verdade: registre a **justificativa** de cada nota, porque é ela que permite revisar a avaliação.

## Modelo

```markdown
# Risk register — <Organização ou escopo>

**Versão:** <N> · **Data:** <AAAA-MM-DD> · **Responsável pelo register:** <papel>
**Apetite e tolerância de referência:** <declaração aprovada pela governança, com data>
**Escalas:** <link para a definição de probabilidade, impacto e matriz>

## RSK-<NNN> — <Título que descreve o cenário, não o controle>

| Campo | Conteúdo |
|:---|:---|
| Ativos e processos afetados | <processos da BIA, sistemas, dados> |
| Fonte de ameaça | <quem: grupo criminoso, insider, terceiro, falha> |
| Evento de ameaça | <o que acontece — técnicas ATT&CK quando ajudar> |
| Vulnerabilidades | <fraquezas exploradas> |
| Condições predisponentes | <características do ambiente que facilitam: rede plana, contas compartilhadas> |
| Probabilidade | <nível> — <justificativa> |
| Impacto | <nível> — <justificativa ligada ao MTD, aos dados ou à obrigação> |
| Risco inerente | <nível> |
| Tratamento | <Mitigar | Transferir | Evitar | Aceitar> — <ações> |
| Controles e ADRs | <CTL-..., ADR-...> |
| Residual esperado | <nível> — <condição para atingi-lo> |
| Comparação com a tolerância | <dentro | fora — e o que isso exige> |
| Obrigações envolvidas | <lei | contrato | adoção voluntária — qual> |
| Dono do risco | <papel com autoridade para aceitar o residual> |
| Aceite | <data e prazo de validade do aceite, quando houver> |
| Próxima revisão | <data ou gatilho> |
| Status | <Identificado | Em tratamento | Residual aceito | Encerrado> |
```

## Orientação por campo

| Campo | Pergunta que responde | Erro comum |
|:---|:---|:---|
| Título | Que cenário pode acontecer? | Título com o controle ("falta de MFA") em vez do evento |
| Ativos e processos | O que é afetado? | Não ligar à BIA, o que impede comparar com o MTD |
| Fonte e evento | Quem age e como? | Fonte genérica ("hackers"), sem evento concreto |
| Vulnerabilidades e condições | Por que é possível aqui? | Esquecer as condições predisponentes, onde a arquitetura mais atua |
| Probabilidade e impacto | Quanto importa? | Nota sem justificativa |
| Tratamento | O que foi decidido? | "Aceitar" por omissão |
| Controles e ADRs | Onde está a decisão e o que a implementa? | Tratamento sem rastreabilidade |
| Residual e tolerância | O que sobra, e é aceitável? | Comparar o residual com a intuição, não com a tolerância aprovada |
| Obrigações | Há lei, contrato ou referência voluntária? | Tratar norma de adoção voluntária como lei, ou o contrário |
| Dono | Quem decide pelo negócio? | TI como dona de risco de negócio |
| Revisão | Quando revisitar? | Itens sem revisão há anos |

## Ciclo de vida de um item

| Status | Entra quando | Sai quando |
|:---|:---|:---|
| **Identificado** | Cenário registrado, ainda não avaliado | Probabilidade, impacto e dono definidos |
| **Em tratamento** | Tratamento decidido, ações em curso | Ações concluídas e residual verificado |
| **Residual aceito** | Dono aceitou formalmente o residual, com prazo | Prazo vence (volta à avaliação) ou o contexto muda |
| **Encerrado** | O cenário deixou de existir (sistema desativado, processo extinto) | — |

Aceites têm **prazo**. Um aceite vencido volta para avaliação — não se renova sozinho.

## Critérios de qualidade

- [ ] Cada cenário tem fonte, evento, ativo e vulnerabilidade concretos.
- [ ] Probabilidade e impacto têm justificativa, e o impacto é ligado à BIA, a dados ou a obrigações.
- [ ] Todo risco alto ou crítico tem tratamento, dono, prazo e controles relacionados.
- [ ] O residual é comparado com a tolerância aprovada; o que fica fora dela tem decisão explícita do dono previsto na governança.
- [ ] Obrigações estão classificadas como lei, contrato ou adoção voluntária.
- [ ] Nenhum aceite sem prazo; nenhum item sem data de revisão.
- [ ] O register é curto o bastante para ser lido: cenários equivalentes são agrupados.

## Exemplo preenchido

Trecho do register da **Meridiana Distribuidora** (organização fictícia do [Caso A](../case-studies/case-a-meridiana/index.md)), depois da revisão de arquitetura.

| Campo | RSK-007 — Ransomware a partir do acesso remoto |
|:---|:---|
| Ativos e processos afetados | Expedição (MTD de 24 h), ERP, WMS, backup |
| Fonte de ameaça | Grupo criminoso de ransomware |
| Evento de ameaça | Login na VPN com credencial roubada (T1133, T1078); escalada com credenciais privilegiadas do domínio (T1003); inibição da recuperação e cifragem (T1490, T1486) — ATT&CK v20 |
| Vulnerabilidades | VPN só com senha; administradores do domínio fazendo login em servidores comuns |
| Condições predisponentes | Rede plana; backup integrado ao domínio |
| Probabilidade | Alta — VPN exposta e ataques frequentes no setor |
| Impacto | Muito alto — parada da expedição além do MTD de 24 h |
| Risco inerente | Crítico |
| Tratamento | Mitigar — MFA resistente a phishing e acesso por aplicação; separação de contas administrativas; backup com identidade própria e cópia isolada |
| Controles e ADRs | CTL-IAM-03, CTL-BKP-02; ADR-001 (acesso remoto) |
| Residual esperado | Médio — depois das etapas 1 e 2 do plano |
| Comparação com a tolerância | Fora da tolerância até a conclusão da etapa 2; exceção aprovada pelo diretor de operações por 90 dias |
| Obrigações envolvidas | LGPD (lei), se houver dados pessoais afetados; contratos com clientes que exigem continuidade |
| Dono do risco | Diretor de operações |
| Próxima revisão | Ao fim da etapa 2, ou antes, se houver incidente relevante |
| Status | Em tratamento |

O mesmo formato vale para cenários de natureza diferente — por exemplo, um sistema sem suporte isolado com compensatórios ([Módulo 8 — Aula 05](../modules/08-onprem-legacy/05-unsupported-systems.md)), cujo tratamento é a exceção com prazo, e não a mitigação completa.
