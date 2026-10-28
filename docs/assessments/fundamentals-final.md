---
id: AS-FUND
title: "Avaliação final de Fundamentals — Livraria Ipê"
description: Avaliação integradora da trilha Fundamentals (Módulo Inicial, Módulo 1 e Módulo 2) — o estudante analisa a arquitetura de uma pequena empresa fictícia, identifica fronteiras e riscos, seleciona controles, escreve requisitos rastreáveis, propõe uma arquitetura-alvo com ADR e a explica em linguagem executiva, com critérios objetivos de correção.
status: published
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# Avaliação final de Fundamentals — Livraria Ipê

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Avaliação integradora · Módulo Inicial · Módulo 1 · Módulo 2</span>
<span class="saa-tier saa-tier--fundamental">Fundamental → Professional</span>
<span class="saa-meta">3 a 4 h · 6 tarefas · 100 pontos</span>
</div>

## Instruções

- Esta avaliação encerra a trilha **Fundamentals**. Ela verifica se você consegue **usar** o que estudou: ler uma arquitetura, encontrar riscos, escolher controles e defender uma proposta.
- Faça as seis tarefas em um documento próprio. Diagramas podem ser desenhados à mão, em Mermaid ou em qualquer ferramenta.
- **Aprovação:** 70 pontos ou mais **e** nenhuma tarefa avaliada como *Insuficiente*.
- A correção usa os **critérios objetivos** de cada tarefa. Confira o [gabarito comentado](answers/fundamentals-final.md) somente ao final.

## Cenário

A **Livraria Ipê** (empresa fictícia) vende livros pela internet e em uma loja física. Tem 40 funcionários, um escritório e uma pequena equipe de TI de três pessoas. Fatos levantados em entrevistas:

1. A loja virtual roda em **uma única máquina virtual** em um provedor de nuvem IaaS, com IP público. Aplicação e banco de dados estão na mesma VM; o backup diário é gravado **no mesmo disco**.
2. O banco guarda nome, endereço, CPF, e-mail e histórico de compras de cerca de 120 mil clientes. Dados de cartão não são armazenados: o pagamento é feito por um provedor externo, chamado pela aplicação com uma **chave de API escrita no código-fonte**.
3. Os três técnicos administram a VM por **RDP aberto à internet**, usando a conta **Administrator compartilhada**.
4. No escritório, há **uma rede única** com as estações, o servidor de arquivos (notas fiscais e contratos) e o **Wi-Fi de visitantes**.
5. Funcionários do atendimento acessam o painel administrativo da loja pela internet, **só com senha**.
6. Não há coleta centralizada de logs. Ninguém sabe dizer quantas tentativas de login falharam no último mês.
7. A diretoria quer abrir uma segunda loja física em seis meses e tem orçamento limitado: prefere serviços gerenciados a contratar mais pessoas.
8. A empresa está sujeita à LGPD.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/as-fund-as-is.mmd"
```

<figcaption>Figura 1 — Arquitetura atual da Livraria Ipê (As-Is).</figcaption>
</figure>

## Tarefa 1 — Ler a arquitetura (15 pontos)

Aplique o método de leitura do Módulo Inicial — Aula 07. Entregue:

- a lista de componentes, incluindo os que **faltam** no diagrama e deveriam estar lá;
- a lista de fluxos, com protocolo e dado transportado;
- as **fronteiras de confiança** e quais fluxos as atravessam.

**Critérios objetivos:** identifica pelo menos quatro fronteiras (internet/nuvem, internet/escritório, escritório/visitantes, organização/provedor de pagamentos); aponta pelo menos três elementos ausentes (por exemplo, DNS, logs, backup fora da VM, identidade dos usuários do painel); rotula fluxos com dado e protocolo.

## Tarefa 2 — Identificar riscos (20 pontos)

Descreva os **cinco riscos mais relevantes** no formato do Módulo 1 — Aula 06: ameaça, vulnerabilidade, ativo, impacto e uma estimativa qualitativa (alta, média, baixa), justificando a ordem.

**Critérios objetivos:** cada risco tem os quatro elementos; pelo menos três dos cinco riscos estão entre: RDP exposto com conta compartilhada; backup no mesmo disco (ransomware ou falha); banco na mesma VM exposta; chave de API no código; painel administrativo só com senha; rede plana com Wi-Fi de visitantes; ausência de logs; a ordenação considera impacto sobre dados pessoais e continuidade.

## Tarefa 3 — Selecionar controles (20 pontos)

Para cada risco da Tarefa 2, proponha controles **preventivos, detectivos e corretivos** quando fizer sentido, indique o **princípio de design** que cada um aplica (Módulo 1 — Aula 02) e a **camada** em que atua (identidade, rede, aplicação, dados, operação).

**Critérios objetivos:** cada risco tem pelo menos um controle preventivo e, nos três principais, também um detectivo ou corretivo; princípios citados corretamente (por exemplo, *least privilege*, *defense in depth*, *separation of duties*, *fail-safe defaults*); nenhum controle genérico sem ligação ao risco ("seguir boas práticas").

## Tarefa 4 — Escrever requisitos rastreáveis (15 pontos)

Escreva **quatro requisitos de segurança** que liguem objetivo de negócio, risco e controle (Módulo 2 — Aula 07), cada um com a propriedade de segurança, o grau e a forma de verificação (Módulo 1 — Aula 01).

**Critérios objetivos:** cada requisito é verificável; cita a propriedade; rastreia a um risco da Tarefa 2; pelo menos um trata de disponibilidade com números (RTO/RPO) e pelo menos um de dados pessoais.

## Tarefa 5 — Propor a arquitetura-alvo (20 pontos)

Desenhe a **arquitetura-alvo** em visão lógica (Módulo 2 — Aula 03) e escreva **um ADR** (Módulo 2 — Aula 08) para a decisão mais importante, com pelo menos duas alternativas, consequências negativas e risco residual. Respeite as restrições do cenário: equipe de três pessoas, orçamento limitado e preferência por serviços gerenciados.

**Critérios objetivos:** o desenho separa exposição, aplicação e dados; elimina RDP exposto e contas compartilhadas; coloca backup fora do alcance da VM; segmenta o escritório; o ADR compara alternativas com critérios explícitos e declara risco residual; a proposta é operável pela equipe descrita.

## Tarefa 6 — Explicar para a diretoria (10 pontos)

Em **no máximo 150 palavras**, explique à diretoria o que muda, por que e em que ordem — sem jargão técnico desnecessário.

**Critérios objetivos:** ordena as ações por risco; liga cada ação a uma consequência de negócio (vazamento de dados de clientes, parada das vendas, multa ou reputação); indica o que fica para depois e por quê.

## Correção

| Tarefa | Pontos | Excelente | Adequado | Insuficiente |
|:---|:---|:---|:---|:---|
| 1 | 15 | 15 | 10 | 4 |
| 2 | 20 | 20 | 14 | 6 |
| 3 | 20 | 20 | 14 | 6 |
| 4 | 15 | 15 | 10 | 4 |
| 5 | 20 | 20 | 14 | 6 |
| 6 | 10 | 10 | 7 | 3 |

**Excelente:** atende a todos os critérios objetivos da tarefa e declara trade-offs. **Adequado:** atende à maioria dos critérios, sem trade-offs ou com uma lacuna menor. **Insuficiente:** não atende a metade dos critérios, é genérico ou ignora o cenário. A [rubrica padrão](rubrics.md) detalha os níveis.

## Depois da avaliação

- Confira o [gabarito comentado](answers/fundamentals-final.md), que traz uma solução de referência — não a única possível.
- Concluída a trilha Fundamentals, os próximos passos são o Módulo 3 (governança e riscos) e o Módulo 4 (threat modeling), que aprofundam as Tarefas 2 e 4.
