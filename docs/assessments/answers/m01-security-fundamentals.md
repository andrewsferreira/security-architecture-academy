---
title: "Gabarito — Avaliação do Módulo 01"
description: Gabarito comentado da avaliação do Módulo 01, com justificativa das alternativas incorretas, respostas de referência das tarefas e rubrica de correção.
status: published
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
---

# Gabarito — Avaliação do Módulo 01

!!! warning "Responda primeiro"

    Este é o gabarito da [avaliação do Módulo 01](../m01-security-fundamentals.md). Faça a avaliação antes de ler.

## Parte 1 — Respostas comentadas

| Questão | Resposta | Aula |
|:---|:---|:---|
| 1 | **b** | M01-L01 |
| 2 | **d** | M01-L01 |
| 3 | **a** | M01-L02 |
| 4 | **c** | M01-L02 |
| 5 | **d** | M01-L03 |
| 6 | **b** | M01-L04 |
| 7 | **a** | M01-L04 |
| 8 | **c** | M01-L05 |
| 9 | **b** | M01-L06 |
| 10 | **d** | M01-L07 |

**1 — (b).** Autenticação não é autorização: saber quem é o usuário não diz se ele pode acessar aquele pedido. É uma das falhas mais comuns em APIs. (a), (c) e (d) não descrevem a falha.

**2 — (d).** Não repúdio e responsabilização exigem registros que nem administradores alterem sem deixar rastro. (a) o log pode até ser confidencial, mas o problema é a alteração; (b) o sistema continua disponível; (c) a sessão não está em questão.

**3 — (a).** Em falha, o estado seguro é negar ou degradar de forma controlada; aceitar tudo transforma a indisponibilidade de um controle em ausência dele. (b), (c) e (d) são princípios válidos, mas não os violados.

**4 — (c).** Separação de funções exige que operações críticas envolvam mais de uma pessoa. (a) trata de não depender de segredo do mecanismo; (b) de camadas independentes; (d) de simplicidade.

**5 — (d).** Fronteiras de confiança são onde controles precisam atuar: autenticação, autorização, validação, cifragem. (a), (b) e (c) não indicam por si só o nível de exposição.

**6 — (b).** Simétrica é rápida e adequada a grandes volumes; a assimétrica (ou o serviço de chaves) protege a chave simétrica — é a criptografia híbrida. (a) hash não cifra; (c) viola o princípio de Kerckhoffs e o *open design*; (d) ignora o requisito de confidencialidade justamente para os maiores volumes.

**7 — (a).** Sem sal, hashes iguais revelam senhas iguais e tabelas pré-calculadas funcionam; com função lenta e sal, cada tentativa fica cara e as tabelas, inúteis. (b) SHA-256 não é reversível, mas é rápido; (c) não é o problema; (d) é o erro que o laboratório 01 demonstra.

**8 — (c).** O cliente valida cadeia, validade e nome; sem a correspondência de nome, o certificado pode ser de outro serviço legítimo usado em um ataque. (a) e (b) ignoram a validação de nome; (d) transfere ao usuário uma decisão que ele não tem como tomar.

**9 — (b).** Vulnerabilidade é condição; risco combina ameaça, exposição e impacto. O achado deve ser registrado, e a decisão (inclusive aceitar até o desligamento) deve ser explícita. (a) ignora o contexto; (c) perde o registro; (d) confunde baixo com zero.

**10 — (d).** Bell-LaPadula: *no read up*, *no write down*, voltado à confidencialidade. (a) Biba trata integridade, com regras invertidas; (b) Clark-Wilson trata integridade por transações bem-formadas e separação de funções; (c) Brewer-Nash trata conflito de interesses.

## Parte 2 — Respostas de referência

**Tarefa 1 — Requisitos por propriedade.** Exemplos de resposta adequada:

| Propriedade | Requisito | Verificação |
|:---|:---|:---|
| Confidencialidade | Pacientes veem apenas os próprios agendamentos; atendentes, apenas os da sua unidade. | Teste de autorização por objeto com usuários de unidades diferentes |
| Integridade e autorização | Alterar ou cancelar agendamento exige autenticação do paciente ou de atendente da unidade; toda alteração é registrada. | Revisão de logs e tentativa de alteração sem permissão |
| Disponibilidade | O agendamento tem RTO de 4 horas e RPO de 1 hora. | Teste de restauração com tempo medido |
| Responsabilização | Toda ação é atribuída a uma identidade individual; sem contas compartilhadas; registros retidos por 5 anos. | Inventário de contas e amostragem de registros |

**Tarefa 2 — Risco e controles.**

- **Ameaça:** fraudador com credenciais obtidas por phishing. **Vulnerabilidade:** alteração de dado crítico apenas com senha. **Ativo:** pagamentos a fornecedores. **Impacto:** desvio de valores, perda financeira e reputacional.
- **Preventivo:** MFA para o portal e confirmação da alteração bancária por canal independente (ligação ao contato cadastrado) ou segunda aprovação interna.
- **Detectivo:** alerta para alterações de conta bancária seguidas de pagamento em curto prazo, ou feitas de localização incomum.
- **Corretivo:** procedimento para suspender pagamentos, reverter a alteração e acionar o banco e o fornecedor.
- **Risco residual:** fraude com a colaboração de alguém do fornecedor ou engenharia social sobre quem confirma a alteração — menor, aceito pelo dono do processo e revisto periodicamente.

## Rubrica das tarefas

| Nível | Pontos | Descrição |
|:---|:---|:---|
| **Excelente** | 20 | Responde a tudo, usa os conceitos corretamente, considera o cenário e declara trade-offs ou risco residual. |
| **Adequado** | 14 | Correto, mas sem trade-offs, sem verificação ou sem uma das partes pedidas. |
| **Insuficiente** | 6 | Incorreto, genérico ou ignora o cenário. |

## Se você não atingiu o mínimo

| Questões ou tarefa com erro | Revise |
|:---|:---|
| 1, 2, Tarefa 1 | [M01-L01](../../modules/01-security-fundamentals/01-security-properties.md) |
| 3, 4 | [M01-L02](../../modules/01-security-fundamentals/02-secure-design-principles.md) |
| 5 | [M01-L03](../../modules/01-security-fundamentals/03-trust-boundaries-attack-surface.md) |
| 6, 7 | [M01-L04](../../modules/01-security-fundamentals/04-applied-cryptography.md) e o [Laboratório 01](../../labs/lab-01-security-mechanisms.md) |
| 8 | [M01-L05](../../modules/01-security-fundamentals/05-pki-tls-key-management.md) |
| 9, Tarefa 2 | [M01-L06](../../modules/01-security-fundamentals/06-threat-vulnerability-risk.md) |
| 10 | [M01-L07](../../modules/01-security-fundamentals/07-formal-security-models.md) |
