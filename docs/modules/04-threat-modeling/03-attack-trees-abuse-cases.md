---
id: M04-L03
title: "Aula 03 — Attack trees e abuse cases"
public_title: "Módulo 4 — Aula 03 — Attack trees e abuse cases"
description: Dois métodos para pensar como o adversário — árvores de ataque, que decompõem um objetivo em caminhos alternativos e necessários com custos, e abuse cases, que descrevem interações completas que causam dano usando funcionalidades legítimas.
domain: application-security
tier: professional
status: published
prerequisites: [M04-L02]
objectives:
  - Construir uma árvore de ataque com nós OU e E e propagar valores para encontrar os caminhos mais baratos.
  - Escrever abuse cases com ator malicioso, recursos, habilidades, dano e faixa de privilégio.
  - Usar árvores e abuse cases para decidir onde os controles rendem mais.
  - Derivar casos de teste a partir de abuse cases.
minutes: 60
sources: [SCHNEIER-ATTACK-TREES-1999, MCDERMOTT-FOX-ABUSE-1999, BOOK-GOOGLE-BSRS]
further_reading: [MITRE-CAPEC, TM-MANIFESTO]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M04
---

# Aula 03 — Attack trees e abuse cases { #attack-trees-e-abuse-cases }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 4 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M04-L03</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    STRIDE olha para os elementos do sistema. Mas adversários não atacam elementos: perseguem **objetivos** — desviar um pagamento, ler prontuários, parar a operação —, combinando passos técnicos e humanos e usando funcionalidades legítimas quando isso é mais barato. Esta aula apresenta dois métodos que partem do objetivo do adversário: **árvores de ataque**, que decompõem o objetivo em caminhos e permitem compará-los por custo ou viabilidade, e **abuse cases**, que descrevem interações completas que causam dano, em linguagem que o negócio entende.

**Pré-requisito:** [STRIDE aplicado à arquitetura](02-stride.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Construir uma árvore de ataque com nós OU e E e propagar valores para encontrar os caminhos mais baratos.
- Escrever abuse cases com ator malicioso, recursos, habilidades, dano e faixa de privilégio.
- Usar árvores e abuse cases para decidir onde os controles rendem mais.
- Derivar casos de teste a partir de abuse cases.

## Conceito

### Árvores de ataque

Bruce Schneier popularizou as **árvores de ataque** em artigo de 1999 na *Dr. Dobb's Journal*: o **objetivo** do adversário fica na raiz e as diferentes formas de alcançá-lo, nas folhas. Dois tipos de nó estruturam a árvore:

- **Nó OU:** alternativas — basta uma para alcançar o subobjetivo.
- **Nó E:** passos necessários — todos precisam ter sucesso.

As folhas recebem **valores** — booleanos (possível ou impossível) ou contínuos (custo, tempo, necessidade de equipamento especial) — que se propagam para cima: em custo, um nó OU vale o filho mais barato e um nó E vale a soma dos filhos. Olhando a raiz, sabe-se se o objetivo é alcançável e por qual caminho; o artigo destaca também que árvores podem formar **bibliotecas reutilizáveis** e ser combinadas.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m04-l03-attack-tree.mmd"
```

<figcaption>Figura 1 — Árvore de ataque para desviar um pagamento a fornecedor na Meridiana; folhas tracejadas são as mais baratas para o atacante.</figcaption>
</figure>

### Abuse cases

McDermott e Fox, em trabalho apresentado na ACSAC de 1999, propõem **abuse cases**: a especificação de uma interação **completa** entre o sistema e um ou mais atores que **resulta em dano** ao sistema, a um ator ou a uma parte interessada. Diferenças em relação ao use case:

| Use case | Abuse case |
|:---|:---|
| Interação desejada | Família de interações indesejadas |
| Não precisa causar dano | Só existe se causar dano |
| Atores comuns | Atores maliciosos, separados dos atores do modelo de uso |
| — | Descreve a faixa de privilégio que o ator pode abusar |

Os autores propõem descrever o ator malicioso por **recursos** (pessoas, ferramentas, dinheiro, tempo), **habilidades** e **objetivos** — e contrastam um atacante amador com 24 horas a um adversário altamente capaz com 90 dias. O abuse case serve à conversa com usuários e clientes sobre o que o produto vai e não vai impedir, orienta o desenho (cada abuse case deve ser refutado até um nível de garantia declarado) e pode ser convertido em **famílias de casos de teste**.

## Fundamentos técnicos

### Construindo uma árvore útil

1. **Escolha um objetivo de negócio**, não técnico: "desviar pagamento", não "explorar SQL injection".
2. **Decomponha em alternativas** (OU) até chegar a ações concretas.
3. **Marque os passos necessários** (E) — muitas vezes é ali que um controle quebra o caminho inteiro.
4. **Atribua um valor** às folhas — custo, habilidade necessária, probabilidade de detecção. Use a mesma escala na árvore inteira.
5. **Propague** e identifique os caminhos mais baratos.
6. **Simule controles:** "se exigirmos dupla aprovação, o nó E passa a exigir comprometer duas pessoas — quanto o caminho encarece?".

Na Figura 1, o caminho "alterar dados bancários no ERP" depende de dois passos (nó E), mas um deles — superar a aprovação — **não existe hoje**. Os dois caminhos mais baratos, ambos de custo muito baixo, são a **conta compartilhada** e o **e-mail falso do fornecedor** — e o segundo não exige nenhum acesso técnico. Controles técnicos no ERP sem tratar o e-mail falso deixariam o caminho mais barato intacto.

### Escrevendo um abuse case

| Campo | Exemplo — AC-03, Meridiana |
|:---|:---|
| **Nome** | Fraudador troca dados bancários de fornecedor por e-mail |
| **Ator malicioso** | Fraudador externo; recursos: domínio parecido com o do fornecedor, e-mails antigos obtidos em vazamento; habilidade: engenharia social; objetivo: receber um pagamento |
| **Faixa de privilégio** | Nenhum acesso ao ERP; usa o privilégio legítimo do analista de cadastro |
| **Interação** | Envia e-mail "do fornecedor" pedindo troca de conta; analista altera no ERP; próximo pagamento vai para a conta do fraudador |
| **Dano** | Perda financeira; fornecedor real não recebe; atraso de entregas |
| **Refutação desejada** | Alteração bancária só após confirmação por canal previamente cadastrado e dupla aprovação |
| **Casos de teste** | Solicitação por e-mail sem confirmação é recusada; segunda aprovação pelo mesmo usuário é bloqueada; alteração gera alerta ao fornecedor |

### Quando usar cada método

| Situação | Método mais adequado |
|:---|:---|
| Comparar caminhos e custo de controles para um objetivo | Árvore de ataque |
| Discutir fraude e abuso de funcionalidades com o negócio | Abuse case |
| Cobrir sistematicamente componentes técnicos | STRIDE (Aula 02) |
| Representar cadeias de ataque observadas no mundo real | ATT&CK (Aula 04) |

### O adversário certo

O capítulo 2 de *Building Secure and Reliable Systems* lembra que atacantes têm motivações diversas — de diversão a ganho financeiro, espionagem e destruição —, que a sofisticação do ataque não prevê seu sucesso (atacantes escolhem o caminho mais simples que funciona) e que vale focar nos **métodos** antes das identidades, porque atribuição é difícil. Isso orienta as árvores: as folhas mais baratas e simples merecem atenção primeiro.

## Exemplo empresarial

!!! example "Meridiana — o controle que o ERP não resolvia"

    A Meridiana planejava investir em um módulo de segurança avançada do ERP para reduzir o cenário RSK-011 (fraude no cadastro de fornecedores). A árvore de ataque mostrou que o caminho mais barato — e-mail falso pedindo troca de conta — **não passa por nenhuma vulnerabilidade técnica do ERP**: usa o privilégio legítimo do analista.

    A decisão mudou: primeiro, **confirmação por canal previamente cadastrado** e **dupla aprovação** de alterações bancárias (custo baixo, efeito sobre dois caminhos); depois, eliminar a conta compartilhada; por último, avaliar o módulo do ERP. O abuse case AC-03 virou três casos de teste executados pela auditoria interna a cada trimestre.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Ponto de partida | Vulnerabilidades técnicas | Objetivos do adversário |
| Fraude | Tratada só por auditoria | Abuse cases no desenho, com testes |
| Priorização de controles | Pelo que o fornecedor oferece | Pelo efeito nos caminhos mais baratos |
| Adversário | Genérico | Recursos, habilidades e objetivos explícitos |

## Aplicabilidade: on-premises, cloud e híbrido

Árvores e abuse cases independem de ambiente, mas as folhas mudam. Em cloud, folhas típicas incluem **chave de acesso vazada em repositório**, **papel com permissão de criar credenciais** e **recurso compartilhado publicamente**. Em ambientes híbridos, é comum que o caminho mais barato para um objetivo em cloud passe pelo **ambiente on-premises** — por exemplo, comprometer o servidor de sincronização de identidade — e a árvore deixa isso explícito.

## Como especificar e implementar

- "Funcionalidades que movimentam dinheiro, alteram dados críticos ou concedem acesso têm abuse cases documentados e testados."
- "Para cada objetivo de adversário de alto impacto, há uma árvore de ataque com os caminhos mais baratos identificados e o efeito dos controles propostos."
- "Abuse cases geram casos de teste executados em regressão ou por auditoria."

## Trade-offs, limitações e antipadrões

- **Trade-off:** árvores completas são caras; foque nos objetivos de maior impacto e aceite árvores incompletas, marcadas como tal.
- **Antipadrão — árvore técnica demais:** começar em "explorar CVE" e esquecer engenharia social e abuso de funcionalidade.
- **Antipadrão — valores inventados com falsa precisão:** use escalas simples e registre a justificativa.
- **Limitação:** a árvore só tem os caminhos que a equipe imaginou; revise com pessoas de fora e com dados de incidentes.

## Como validar

- Executar os casos de teste derivados dos abuse cases.
- Pedir a um red team ou a uma equipe externa que tente o caminho mais barato.
- Conferir se incidentes reais de fraude ou abuso estavam previstos em alguma árvore ou abuse case.

## Como apresentar e justificar

- **Para o negócio:** "O jeito mais barato de desviar um pagamento hoje é um e-mail falso. Nenhuma ferramenta técnica no ERP resolve isso; a dupla aprovação resolve."
- **Para engenharia:** "Este abuse case vira três testes automatizados no fluxo de alteração bancária."

## Checklist de revisão arquitetural

- [ ] Objetivos de adversário de alto impacto têm árvore de ataque.
- [ ] Os caminhos mais baratos estão identificados.
- [ ] Controles foram escolhidos pelo efeito nesses caminhos.
- [ ] Funcionalidades sensíveis têm abuse cases com ator, recursos, dano e refutação.
- [ ] Abuse cases geraram casos de teste.

## Questões de compreensão

**1.** Em uma árvore com custos, qual o valor de um nó OU e de um nó E?

??? success "Resposta comentada"

    O nó OU vale o custo do filho mais barato, porque o atacante escolhe a alternativa mais fácil. O nó E vale a soma dos filhos, porque todos os passos são necessários.

**2.** O que diferencia um abuse case de um use case com "fluxo de exceção"?

??? success "Resposta comentada"

    O abuse case descreve uma interação completa que causa dano, com um ator malicioso caracterizado por recursos, habilidades e objetivos, e com a faixa de privilégio que ele abusa. Um fluxo de exceção trata erros do usuário legítimo, sem modelar intenção maliciosa nem dano.

**3.** Por que um controle em um nó E pode ser especialmente eficiente?

??? success "Resposta comentada"

    Porque basta impedir um dos passos necessários para bloquear todo o caminho abaixo daquele nó. Se o mesmo nó E aparece em vários caminhos, o controle tem efeito multiplicado.

## Exercício de tomada de decisão

!!! question "Cenário: ler prontuários da Lumen"

    Construa uma árvore de ataque para o objetivo "ler prontuários de um paciente específico da Lumen" com pelo menos três alternativas de primeiro nível. Atribua custo baixo, médio ou alto às folhas e indique os dois controles que mais encarecem os caminhos mais baratos. Para justificar a escolha, compare quatro candidatos com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho): (A) monitoração de acesso a prontuários com justificativa e alertas; (B) proibição de dados reais fora de produção, com mascaramento; (C) MFA resistente a phishing para todos os funcionários; (D) testes de autorização por objeto na API do portal.

??? success "Resolução de referência"

    - **Raiz:** ler prontuários de um paciente específico.
    - **OU (primeiro nível):**
        1. **Usar acesso interno legítimo** — funcionário curioso com perfil clínico (custo **baixo**).
        2. **Comprometer credencial de funcionário** — E: obter senha por phishing (baixo) **e** superar o MFA (médio, se o MFA for por push; alto, se for resistente a phishing).
        3. **Explorar a API do portal** — OU: falha de autorização por objeto, trocando o ID do paciente (médio); token roubado do app (médio).
        4. **Obter cópia de dados** — backup ou ambiente de testes com dados reais (custo **baixo** se a cópia existir).
    - **Caminhos mais baratos:** acesso interno legítimo e cópia de dados fora de produção.
    - **Controles de maior efeito:** (a) **monitoração de acesso a prontuários com justificativa e alertas para padrões anômalos** (encarece o caminho 1, tornando-o detectável); (b) **proibição de dados reais fora de produção, com mascaramento** (elimina o caminho 4). MFA resistente a phishing e testes de autorização por objeto vêm em seguida.
    - **Comparação dos candidatos:**

        | Critério | Peso | A — Monitoração de acesso | B — Sem dados reais fora de produção | C — MFA resistente a phishing | D — Testes de autorização por objeto |
        |:---|:---|:---|:---|:---|:---|
        | Efeito nos caminhos mais baratos da árvore | 3 | 3 | 3 | 2 | 1 |
        | Tempo para implantar (3 = mais rápido) | 2 | 2 | 2 | 2 | 3 |
        | Impacto na rotina clínica e de testes (3 = menor) | 2 | 3 | 2 | 2 | 3 |
        | Custo (3 = menor) | 1 | 2 | 2 | 2 | 3 |
        | **Total ponderado** | | **21** | **19** | **16** | **18** |

        **Pesos:** o efeito nos caminhos mais baratos recebe 3 porque é o que a árvore mede; tempo e impacto na rotina recebem 2; custo recebe 1. **Recomendação: A e B**, os dois maiores totais e os únicos que atacam os dois caminhos mais baratos. D soma mais que C por ser barato e rápido, mas atua sobre um caminho de custo médio — a matriz confirma a ordem, e a árvore explica por quê.
    - **Risco residual:** o funcionário com acesso legítimo continua podendo ler o prontuário; a monitoração torna o abuso detectável e passível de responsabilização, não impossível.
    - **O que mudaria a decisão:** se a análise de logs mostrasse tentativas de troca de ID na API do portal, D subiria para o primeiro lugar; se o MFA atual fosse só por SMS e houvesse phishing direcionado à equipe clínica, C ganharia peso.

## Pontos-chave

- Árvores de ataque partem do objetivo do adversário e comparam caminhos por custo ou viabilidade.
- Nó OU vale a alternativa mais barata; nó E, a soma dos passos.
- Abuse cases descrevem interações completas que causam dano, com ator malicioso caracterizado.
- O caminho mais barato muitas vezes usa privilégio legítimo e engenharia social.
- Abuse cases viram testes; árvores orientam onde investir em controles.

## Referências

### Fundamentação principal

- B. Schneier. *Attack Trees*. Dr. Dobb's Journal, dez. 1999. <https://www.schneier.com/academic/archives/1999/12/attack_trees.html>. *(Lido.)*
- J. McDermott, C. Fox. *Using Abuse Case Models for Security Requirements Analysis*. ACSAC, 1999. <https://www.ida.liu.se/~TDDC90/literature/papers/mcdermott_acsac99.pdf>. *(Lido.)*
- H. Adkins et al. *Building Secure and Reliable Systems*. O'Reilly, 2020 — Cap. 2, *Understanding Adversaries*. <https://google.github.io/building-secure-and-reliable-systems/raw/toc.html>. *(Lido.)*

### Leitura complementar

- MITRE. *CAPEC* — padrões de ataque úteis para preencher folhas de árvores.
- *Threat Modeling Manifesto* — o lugar desses métodos na pergunta "o que pode dar errado?".

### Aplicação prática

- Escolha uma funcionalidade que movimenta dinheiro ou dados sensíveis no seu ambiente, escreva um abuse case e derive dele três casos de teste.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
