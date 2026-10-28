---
id: AS-N1
title: "Avaliação integradora do Nível 1 — Rede Jacarandá Farmácias"
description: Avaliação integradora do Nível 1 — Fundamentos de Arquitetura (Módulos 2, 3 e 4). O estudante analisa uma rede de farmácias fictícia, identifica ativos e fronteiras, desenha o DFD, modela ameaças, registra e classifica riscos, seleciona controles, compara alternativas, propõe As-Is e To-Be com ADR, define evidências e critérios de aceite e comunica a recomendação, com rubrica e critérios objetivos de correção.
status: published
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
---

# Avaliação integradora do Nível 1 — Rede Jacarandá Farmácias

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Avaliação integradora · Nível 1 · Módulos 2, 3 e 4</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">5 a 6 h · 8 tarefas · 100 pontos</span>
</div>

## Instruções

- Esta avaliação encerra o **Nível 1 — Fundamentos de Arquitetura**. Ela não repete a [avaliação integradora do Módulo Inicial ao Módulo 2](fundamentals-final.md), que integra o Módulo Inicial, o Módulo 1 e o Módulo 2: aqui o foco são as decisões de governança, risco e threat modeling dos Módulos 3 e 4, aplicadas com o raciocínio arquitetural do Módulo 2.
- Faça as oito tarefas em um documento próprio. Diagramas podem ser desenhados à mão, em Mermaid ou em qualquer ferramenta.
- **Aprovação:** 70 pontos ou mais **e** nenhuma tarefa avaliada como *Insuficiente*.
- Use os modelos do portal quando ajudarem: [ADR](../artifacts/architecture-decision-record.md), [especificação de requisitos](../artifacts/security-requirements-specification.md) e [checklist de revisão](../artifacts/architecture-review-checklist.md).
- A correção usa os **critérios objetivos** de cada tarefa e a [rubrica](#rubrica). Confira o [gabarito comentado](answers/level-1-integrative.md) somente ao final.
- Esta avaliação não é aconselhamento jurídico: quando uma tarefa envolver LGPD ou PCI DSS, indique a natureza da obrigação e o que precisa ser confirmado com o jurídico, o encarregado de dados ou o assessor de conformidade.

## Cenário

A **Rede Jacarandá Farmácias** (empresa fictícia) tem 38 lojas, uma loja virtual com app e um programa de fidelidade. São 1.200 funcionários; a área de TI tem nove pessoas, duas delas dedicadas à segurança. A diretoria quer lançar em **90 dias** o **envio de receitas pelo app**: o cliente fotografa a receita, o farmacêutico a valida e o pedido segue para retirada na loja ou entrega por um parceiro.

Fatos levantados em entrevistas:

1. App, loja virtual, API de pedidos e painel de validação rodam em **uma única conta de nuvem**, sem separação entre produção e testes. A equipe de desenvolvimento tem acesso administrativo à conta, e o ambiente de testes usa uma cópia da base de produção.
2. O **programa de fidelidade** tem 600 mil clientes: nome, CPF, telefone, endereço e histórico de compras — que inclui medicamentos e pode revelar condições de saúde.
3. No piloto do envio de receitas, as fotos são gravadas em um **armazenamento de objetos acessível por link público** "difícil de adivinhar".
4. Os **farmacêuticos** validam receitas em um painel na nuvem, com a conta do diretório corporativo e **só senha**. Há dois meses, a credencial de um farmacêutico foi obtida por phishing e usada para consultar históricos de compra de clientes; o abuso só foi percebido **três semanas depois**, por reclamação de um cliente.
5. O **parceiro de entregas** chama a API de pedidos com **uma chave única para todas as lojas** e recebe o pedido completo, inclusive o histórico do cliente.
6. O pagamento online usa a **página hospedada** do provedor de pagamentos. Nas lojas, o pagamento com cartão usa terminais do adquirente.
7. No **datacenter próprio** ficam o ERP e o estoque, o diretório corporativo — único para lojas e datacenter — e o **backup em NAS montado no domínio**. Um serviço de **sincronização** troca pedidos e estoque entre a nuvem e o ERP usando uma **credencial administrativa** do banco do ERP.
8. As lojas usam PDV ligado ao datacenter por **VPN site-to-site**.
9. **BIA preliminar** (aprovada pelos donos dos processos):

    | Processo | Dono | MTD | RPO desejado |
    |:---|:---|:---|:---|
    | Vendas nas lojas (PDV) | Diretor de operações | 4 h (há contingência off-line por até 4 h) | 1 h |
    | Validação de receitas | Farmacêutica responsável técnica | 24 h | 15 min |
    | Loja virtual e app | Diretora comercial | 12 h | 1 h |

10. **Governança:** a diretoria aprovou como apetite e tolerância: "nenhum dado de saúde exposto publicamente; risco alto envolvendo dados de saúde só pode ser aceito pelo diretor de operações e por no máximo 60 dias; parada das lojas acima de 4 horas é inaceitável".
11. **Obrigações e contratos:** a Jacarandá é controladora de dados pessoais (LGPD); o contrato com o adquirente exige conformidade com o PCI DSS; o contrato com o parceiro de entregas pede "segurança compatível com a ISO/IEC 27001", sem exigir certificação. A retenção de receitas segue regra sanitária específica, que ainda precisa ser confirmada com o jurídico e com a farmacêutica responsável.
12. **Restrições:** equipe pequena, preferência por serviços gerenciados e orçamento para no máximo **três iniciativas estruturais** neste semestre.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/as-n1-as-is.mmd"
```

<figcaption>Figura 1 — Arquitetura atual da Rede Jacarandá (As-Is).</figcaption>
</figure>

### Partes interessadas

| Parte | Interesse principal |
|:---|:---|
| Diretor de operações | Lojas vendendo; dono dos riscos de parada e dos aceites de risco de saúde |
| Diretora comercial | Lançar o envio de receitas no prazo; experiência do cliente |
| Farmacêutica responsável técnica | Validação correta das receitas e guarda conforme a regra sanitária |
| Encarregado de dados | Conformidade com a LGPD e resposta a incidentes com dados pessoais |
| Coordenador de segurança e gerente de TI | Viabilidade com nove pessoas; operação da solução |
| Parceiro de entregas | Integração estável, com o mínimo de mudanças |

## Tarefa 1 — Contexto, partes interessadas e ativos (10 pontos)

Entregue: (a) os **objetivos de negócio** e as **restrições** que limitam a arquitetura; (b) uma matriz de **responsabilidades** com, para cada decisão relevante (aceite de risco, validação de receitas, retenção, resposta a incidentes, operação da integração), quem decide, quem executa e quem é consultado; (c) o inventário dos **ativos de informação** com classificação (dado pessoal, dado pessoal sensível, dado de cartão, dado operacional) e o processo da BIA que cada um suporta.

**Critérios objetivos:** distingue objetivo (lançar em 90 dias, proteger dados de saúde, manter as lojas vendendo) de restrição (equipe, orçamento, três iniciativas); atribui o aceite de risco ao dono previsto na governança, não à TI; classifica receitas e histórico de medicamentos como dados que podem revelar saúde (art. 5º, II, da LGPD); identifica que a Jacarandá não armazena dados de cartão no fluxo online.

## Tarefa 2 — DFD e fronteiras de confiança (15 pontos)

Desenhe um **DFD de nível 1** do envio e da validação de receitas, incluindo a integração com o parceiro de entregas e a sincronização com o ERP. Numere os fluxos, marque as **fronteiras de confiança** e indique quais fluxos as atravessam, com dado, canal e forma de autenticação.

**Critérios objetivos:** usa os elementos do DFD corretamente (nenhum fluxo liga dois armazenamentos sem processo); representa pelo menos quatro fronteiras (internet, borda, dados, organização × parceiro, nuvem × datacenter); trata o app como ambiente não confiável; rotula os fluxos que atravessam fronteiras; aponta pelo menos dois problemas do As-Is visíveis no DFD (link público das receitas, chave única do parceiro, credencial administrativa da sincronização).

## Tarefa 3 — Threat modeling (15 pontos)

Para os elementos priorizados do seu DFD, entregue: (a) **STRIDE por elemento**, com pelo menos seis ameaças registradas no formato da Aula 02 do Módulo 4 (elemento, categoria, descrição, pré-condições, impacto, resposta, decisão); (b) um **abuse case** de fraude ou abuso de funcionalidade legítima; (c) o incidente do fato 4 descrito como **sequência de táticas e técnicas do MITRE ATT&CK**, com a versão usada e, para cada passo, um controle que previne, detecta ou recupera.

**Critérios objetivos:** as ameaças são específicas do cenário (não "risco de spoofing"); cobre pelo menos quatro das seis categorias STRIDE; o abuse case tem ator malicioso, faixa de privilégio, dano e refutação desejada; a sequência ATT&CK registra a versão e tem pelo menos quatro passos coerentes com o fato 4; ameaças aceitas têm justificativa.

## Tarefa 4 — Registro e classificação de riscos (15 pontos)

Registre os **cinco cenários de risco mais relevantes** no formato do risk register (Módulo 3 — Aula 06): ativos e processos, fonte e evento de ameaça, vulnerabilidades e condições predisponentes, probabilidade e impacto com justificativa, risco inerente, tratamento, residual esperado, dono e prazo. Para cada cenário, indique a **natureza das obrigações envolvidas** (lei, contrato ou adoção voluntária) e compare o residual com a **tolerância** do fato 10.

**Critérios objetivos:** cada cenário tem todos os campos; pelo menos três dos cinco estão entre: exposição de receitas por link público; abuso de credencial de farmacêutico; chave única do parceiro com dados em excesso; testes com cópia da base de produção; sincronização com credencial administrativa; backup alcançável pelo domínio; os donos seguem a governança; nenhum risco alto de saúde fica aceito por mais de 60 dias; a LGPD é tratada como lei, o PCI DSS como obrigação contratual e a referência à ISO/IEC 27001 como exigência contratual de adoção voluntária.

## Tarefa 5 — Seleção de controles e requisitos (10 pontos)

Proponha o **conjunto de controles** para o escopo do envio de receitas: escolha uma baseline de partida (por exemplo, CIS IG1 como piso e controles adicionais para dados de saúde), registre os ajustes de tailoring com justificativa e identifique controles herdados do provedor de nuvem. Depois escreva **quatro requisitos de segurança verificáveis**, cada um rastreado a uma ameaça da Tarefa 3 ou a um risco da Tarefa 4, com critério de aceite.

**Critérios objetivos:** a baseline é coerente com o porte da equipe; cada ajuste tem justificativa; herança indica provedor e evidência; os requisitos descrevem resultado e parâmetros testáveis; pelo menos um requisito trata de detecção e um de recuperação ligado ao RPO da BIA.

## Tarefa 6 — Alternativas, As-Is e To-Be (15 pontos)

Escolha a **decisão de arquitetura mais importante** do cenário e compare pelo menos **três alternativas** com uma **matriz ponderada** (critérios, pesos justificados, notas e total). Depois desenhe a **arquitetura-alvo (To-Be)**, liste as lacunas entre As-Is e To-Be e proponha uma **transição em etapas** compatível com o prazo de 90 dias e com a restrição de três iniciativas estruturais.

**Critérios objetivos:** a matriz está correta aritmeticamente, tem pesos justificados e não substitui a análise (critérios eliminatórios, como a tolerância a dados de saúde expostos, são tratados antes da soma); o To-Be elimina o link público das receitas, separa produção e testes ou elimina dados reais dos testes, limita o que o parceiro recebe e protege o acesso dos farmacêuticos; a transição mantém as lojas vendendo e cabe nas restrições.

## Tarefa 7 — ADR e riscos residuais (10 pontos)

Escreva um **ADR** para a decisão da Tarefa 6, com contexto, alternativas, critérios, decisão, consequências positivas e negativas e **riscos residuais com dono**.

**Critérios objetivos:** o ADR segue o modelo do Módulo 2 — Aula 08; declara pelo menos uma consequência negativa real; os riscos residuais têm dono e prazo de revisão compatíveis com a governança; o ADR referencia os cenários de risco que trata.

## Tarefa 8 — Evidências, validação e comunicação (10 pontos)

Entregue: (a) para quatro controles críticos do To-Be, o **método de validação** (examinar, entrevistar ou testar), a **evidência** esperada e o **critério de aceite**; (b) uma **medida** de eficácia ou de impacto para o cenário de risco mais crítico, com fórmula, fonte de dados e meta; (c) um **resumo executivo** de no máximo 200 palavras para a diretoria, com a recomendação, a ordem das ações e as **decisões pedidas**.

**Critérios objetivos:** controles críticos são validados por teste; a evidência é verificável por terceiros; a medida não é só de implementação; o resumo é compreensível sem jargão, liga as ações a consequências de negócio e termina com decisões que a diretoria pode tomar.

## Rubrica

| Tarefa | Pontos | Excelente | Adequado | Insuficiente | Resultados de aprendizagem verificados |
|:---|:---|:---|:---|:---|:---|
| 1 | 10 | 10 | 7 | 3 | 1, 2 |
| 2 | 15 | 15 | 11 | 4 | 6, 7 |
| 3 | 15 | 15 | 11 | 4 | 8, 9 |
| 4 | 15 | 15 | 11 | 4 | 3, 4 |
| 5 | 10 | 10 | 7 | 3 | 5, 10 |
| 6 | 15 | 15 | 11 | 4 | 11, 12 |
| 7 | 10 | 10 | 7 | 3 | 13 |
| 8 | 10 | 10 | 7 | 3 | 14, 15 |

**Excelente:** atende a todos os critérios objetivos da tarefa e declara trade-offs. **Adequado:** atende à maioria dos critérios, sem trade-offs ou com uma lacuna menor. **Insuficiente:** não atende a metade dos critérios, é genérico ou ignora o cenário. Quem obtém *Adequado* em todas as tarefas soma 72 pontos e é aprovado, como na rubrica padrão. A [rubrica padrão](rubrics.md) detalha os níveis; para a Tarefa 6, aplique também o critério *Justificativas* da rubrica padrão.

### Resultados de aprendizagem do Nível 1

| Nº | Ao concluir o Nível 1, o estudante é capaz de… | Onde é trabalhado |
|:---|:---|:---|
| 1 | Interpretar objetivos de negócio e restrições arquiteturais | Módulo 2 — Aula 07; Módulo 3 — Aula 01 |
| 2 | Identificar stakeholders e responsabilidades | Módulo 2 — Aula 01; Módulo 3 — Aulas 01 e 02 |
| 3 | Compreender governança de segurança | Módulo 3 — Aulas 01, 07 e 08 |
| 4 | Realizar análises de risco | Módulo 3 — Aulas 05 e 06 |
| 5 | Selecionar e adaptar controles | Módulo 3 — Aulas 03 e 07 |
| 6 | Construir e interpretar DFDs | Módulo 4 — Aula 01 |
| 7 | Identificar fronteiras de confiança | Módulo 4 — Aula 01; Módulo 3 — Aula 02 |
| 8 | Aplicar STRIDE | Módulo 4 — Aula 02 |
| 9 | Estruturar cenários de ameaça | Módulo 4 — Aulas 03 e 04; Módulo 3 — Aula 06 |
| 10 | Relacionar ameaças a requisitos de segurança | Módulo 4 — Aula 06; Módulo 2 — Aula 07 |
| 11 | Produzir As-Is e To-Be | Módulo 4 — Aula 07 |
| 12 | Comparar arquiteturas e trade-offs | Exercícios de decisão com matriz ponderada dos Módulos 3 e 4; Módulo 4 — Aula 07 |
| 13 | Registrar ADRs | Módulo 2 — Aula 08; Módulo 4 — Aula 07 |
| 14 | Definir evidências e critérios de validação | Módulo 3 — Aulas 07 e 08; Módulo 4 — Aulas 06 e 07 |
| 15 | Comunicar uma recomendação arquitetural | Seções "Como apresentar e justificar" das aulas; Módulo 3 — Aula 08 |

## Depois da avaliação

- Confira o [gabarito comentado](answers/level-1-integrative.md), que traz uma solução de referência — não a única possível.
- Para cada tarefa *Insuficiente*, revise as aulas indicadas na tabela de resultados de aprendizagem e refaça somente aquela parte.
