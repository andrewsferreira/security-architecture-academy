---
id: ART-TM
title: "Modelo: Threat Model"
description: Modelo editável de threat model — escopo, ativos, DFD com fronteiras de confiança, premissas, ameaças STRIDE por elemento em formato acionável, abuse cases, cenários MITRE ATT&CK, pontos únicos de falha, requisitos derivados e ameaças aceitas —, com critérios de qualidade e exemplo preenchido.
status: published
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
---

# Modelo: Threat Model

O threat model documenta **o que pode dar errado** em um sistema, **o que será feito** a respeito e **como verificar** que foi feito. Ele responde às quatro perguntas do *Threat Modeling Manifesto* — no que estamos trabalhando, o que pode dar errado, o que vamos fazer, fizemos um bom trabalho — e usa as técnicas do Módulo 4: [DFD e fronteiras](../modules/04-threat-modeling/01-data-flow-diagrams.md), [STRIDE](../modules/04-threat-modeling/02-stride.md), [árvores de ataque e abuse cases](../modules/04-threat-modeling/03-attack-trees-abuse-cases.md), [cenários com MITRE ATT&CK](../modules/04-threat-modeling/04-mitre-attack-scenarios.md), [pontos únicos de falha](../modules/04-threat-modeling/05-single-points-of-failure.md) e [requisitos derivados](../modules/04-threat-modeling/06-threats-to-requirements.md).

## Quando usar

- Antes de construir ou mudar um sistema que atravessa fronteiras de confiança (integração, exposição à internet, novo provedor).
- Em revisões de arquitetura, para mostrar onde o desenho interrompe os cenários críticos.
- Sempre que um incidente ou uma mudança de contexto tornar o modelo anterior desatualizado.

## Modelo

```markdown
# Threat model — <Sistema ou fluxo>

**Versão:** <N> · **Data:** <AAAA-MM-DD> · **Participantes:** <papéis>
**Escopo:** <o que está dentro e o que ficou de fora>
**Documentos relacionados:** <ADRs, requisitos, risk register, diagramas>

## 1. Ativos e objetivos de segurança

| Ativo | Classificação | Objetivo (C, I, D, rastreabilidade) |
|:---|:---|:---|
| <dado ou função> | <pessoal, sensível, financeiro, operacional> | <o que não pode acontecer> |

## 2. DFD e fronteiras de confiança

<Diagrama com entidades externas, processos, armazenamentos e fluxos numerados;
fronteiras de confiança marcadas.>

| Fluxo | Origem → destino | Dado | Canal e autenticação | Fronteira atravessada |
|:---|:---|:---|:---|:---|
| <1> | <A → B> | <dado> | <protocolo, mTLS, OIDC...> | <internet × borda> |

## 3. Premissas e dependências

- <Premissa que, se falsa, invalida parte do modelo — por exemplo, "o IdP exige MFA">
- <Dependência externa: provedor, biblioteca, serviço gerenciado>

## 4. Ameaças (STRIDE por elemento)

| ID | Elemento | Categoria | Descrição | Pré-condições | Impacto | Resposta | Decisão | Requisito | Risco |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| TM-<NN> | <elemento do DFD> | <S/T/R/I/D/E> | <quem faz o quê> | <o que precisa ser verdade> | <consequência> | <controle proposto> | <Mitigar/Eliminar/Transferir/Aceitar> | <SR-NN> | <RSK-NNN> |

## 5. Abuse cases

| Campo | Conteúdo |
|:---|:---|
| Ator malicioso | <quem, com que recursos e objetivo> |
| Faixa de privilégio | <usuário legítimo, parceiro, administrador> |
| Interação | <sequência de uso indevido da funcionalidade> |
| Dano | <para quem e quanto> |
| Refutação desejada | <o que o sistema deve fazer> |
| Casos de teste | <como verificar> |

## 6. Cenários de ataque (MITRE ATT&CK <versão>)

| Passo | Tática | Técnica | Onde o desenho interrompe ou detecta |
|:---|:---|:---|:---|
| <1> | <tática> | <técnica (ID)> | <controle> |

## 7. Pontos únicos de falha

| Componente | Efeito da falha | Tratamento |
|:---|:---|:---|

## 8. Requisitos derivados

| ID | Requisito verificável | Origem (TM, abuse case, cenário) | Critério de aceite |
|:---|:---|:---|:---|

## 9. Ameaças aceitas

| ID | Justificativa | Dono | Revisão |
|:---|:---|:---|:---|

## 10. Revisão do modelo

<Gatilhos: mudança de fronteira, nova integração, incidente, troca de provedor.>
```

## Orientação por campo

| Seção | Pergunta que responde | Erro comum |
|:---|:---|:---|
| Escopo | O que foi modelado? | Modelar "o sistema todo" sem dizer o que ficou de fora |
| Ativos | O que precisamos proteger? | Listar servidores em vez de dados e funções |
| DFD | Por onde os dados passam? | Fluxo ligando dois armazenamentos sem processo; fronteiras ausentes |
| Premissas | Em que o modelo confia? | Premissas implícitas que ninguém verifica |
| Ameaças | O que pode dar errado aqui? | Ameaças genéricas ("risco de spoofing"), sem pré-condições nem decisão |
| Abuse cases | Como a funcionalidade legítima pode ser abusada? | Ignorar fraude e abuso por usuários autorizados |
| ATT&CK | Como um ataque real atravessaria o desenho? | Omitir a versão; usar técnicas que não existem nela |
| Pontos únicos de falha | O que derruba o serviço? | Tratar só confidencialidade |
| Requisitos | O que a engenharia precisa entregar? | Requisito sem critério de aceite |
| Ameaças aceitas | O que decidimos não tratar, e por quê? | Descartes silenciosos |

## Critérios de qualidade

- [ ] O DFD tem fluxos numerados e todas as fronteiras de confiança relevantes, com os fluxos que as atravessam rotulados.
- [ ] As ameaças são específicas do sistema, com pré-condições, impacto, resposta e decisão.
- [ ] As categorias STRIDE aplicáveis a cada elemento priorizado foram consideradas.
- [ ] Há pelo menos um abuse case para funcionalidades que movimentam dinheiro, dados sensíveis ou privilégios.
- [ ] Os cenários ATT&CK registram a versão e mostram onde o desenho interrompe cada passo.
- [ ] Cada ameaça mitigada aponta para um requisito verificável; cada ameaça aceita tem justificativa, dono e revisão.
- [ ] Ameaças relevantes para o negócio estão no [risk register](risk-register.md).

## Exemplo preenchido

Trecho do threat model da **integração de laudos da Lumen Saúde** (organização fictícia usada no [Módulo 4 — Aula 02](../modules/04-threat-modeling/02-stride.md)): um laboratório parceiro envia laudos de exames para a API da Lumen.

**Fluxos que atravessam fronteiras:**

| Fluxo | Origem → destino | Dado | Canal e autenticação | Fronteira |
|:---|:---|:---|:---|:---|
| 1 | Laboratório → API de laudos | Laudo do paciente | HTTPS com credencial estática (As-Is) | Organização × parceiro |
| 2 | API de laudos → armazenamento de laudos | Laudo | TLS interno, com identidade de serviço | Aplicação × dados |
| 3 | Portal do paciente → API de laudos | Pedido de leitura | HTTPS com sessão do paciente | Internet × borda |

**Ameaças:**

| ID | Elemento | Cat. | Descrição | Pré-condições | Impacto | Resposta | Decisão | Requisito | Risco |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| TM-07 | Fluxo 1 | S | Atacante com a credencial estática do laboratório envia laudos falsos em nome dele | Credencial compartilhada, sem rotação, aceita de qualquer origem | Laudo falso associado a paciente real | Credencial de workload de curta duração; escrita restrita ao prefixo do laboratório | Mitigar | SR-14 | RSK-041 |
| TM-11 | Fluxo 1 | D | Envio em massa derruba a integração | Sem limite por parceiro | Atraso na liberação de laudos | Limite de taxa simples | Aceitar — integração não crítica para o atendimento imediato | — | — |
| TM-13 | Fluxo 3 | I | Paciente troca o identificador do laudo no portal e lê o de outro paciente | Autorização só na borda, sem verificação por objeto | Exposição de dado de saúde | Autorização por objeto na API | Mitigar | SR-17 | Novo cenário a registrar no register |

**Requisito derivado (exemplo):** SR-17 — "A API de laudos só devolve um laudo se o paciente da sessão for o titular ou se houver vínculo autorizado." *Aceite:* teste automatizado com identificador de outro paciente retorna erro e gera evento.

**Ameaça aceita (exemplo):** TM-11 — envio em massa pelo laboratório. A integração não é crítica para o atendimento imediato, e um limite de taxa simples reduz o efeito; a decisão de aceitar fica registrada, com dono (diretor clínico) e revisão anual ou quando o volume de laudos crescer.

TM-07, TM-11 e SR-14 são os mesmos da Aula 02 e da Aula 06 do Módulo 4; o fluxo 3 (portal do paciente), a TM-13 e o SR-17 são acréscimos ilustrativos deste exemplo; o fluxo completo de ameaça a requisito está na [Aula 06 do Módulo 4](../modules/04-threat-modeling/06-threats-to-requirements.md).
