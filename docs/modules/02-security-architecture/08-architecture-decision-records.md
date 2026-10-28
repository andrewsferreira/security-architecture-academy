---
id: M02-L08
title: "Aula 08 — Architecture Decision Records"
public_title: "Módulo 2 — Aula 08 — Architecture Decision Records"
description: Como registrar decisões arquiteturais significativas em ADRs, com contexto, alternativas, consequências, riscos residuais e critérios de revisão — e como manter um registro de decisões útil ao longo do tempo.
domain: enterprise-architecture
tier: architect
status: published
prerequisites: [M02-L07]
objectives:
  - Identificar quais decisões são arquiteturalmente significativas e merecem um ADR.
  - Escrever um ADR completo, com alternativas, consequências negativas e risco residual.
  - Manter um registro de decisões com status, substituição e ligação a exceções e requisitos.
  - Avaliar a qualidade de um ADR e apontar suas falhas.
minutes: 75
sources: [NYGARD-ADR-2011, ISO-42010-2022]
further_reading: [NIST-SP800-160-V1R1, BOOK-GOOGLE-BSRS]
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
module: M02
---

# Aula 08 — Architecture Decision Records { #architecture-decision-records }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 2 · Nível 1</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">75 min · ID técnico: M02-L08</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Daqui a dois anos, alguém vai olhar para a arquitetura e perguntar "por que fizeram assim?". Se a resposta estiver apenas na memória de quem decidiu, a decisão será refeita, contestada ou — pior — revertida sem que ninguém saiba o risco que ela tratava. Architecture Decision Records são a forma mais simples de evitar isso. Esta aula fecha o módulo ensinando a escrever, manter e avaliar ADRs.

**Pré-requisitos:** [Business-driven Security Architecture](07-business-driven-requirements.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Identificar quais decisões são arquiteturalmente significativas e merecem um ADR.
- Escrever um ADR completo, com alternativas, consequências negativas e risco residual.
- Manter um registro de decisões com status, substituição e ligação a exceções e requisitos.
- Avaliar a qualidade de um ADR e apontar suas falhas.

## Conceito

### O que é um ADR

Um **Architecture Decision Record** é um documento curto que registra **uma** decisão de arquitetura significativa: o contexto em que foi tomada, a decisão, seu status e suas consequências. O formato foi popularizado por Michael Nygard em 2011, com cinco seções:

| Seção | Conteúdo |
|:---|:---|
| **Título** | Frase curta e numerada que nomeia a decisão |
| **Contexto** | As forças em jogo — técnicas, de negócio, políticas, de projeto —, descritas de forma factual, inclusive quando conflitam |
| **Decisão** | A resposta a essas forças, em voz ativa: "Vamos…" |
| **Status** | Proposta, aceita, depreciada ou substituída |
| **Consequências** | Todos os efeitos resultantes — positivos, negativos e neutros |

Nygard também recomendou que os ADRs sejam numerados sequencialmente sem reutilizar números, guardados no repositório do projeto em formato de texto simples, escritos em frases completas e mantidos curtos — uma ou duas páginas.

### Por que existem

Decisões de arquitetura têm três características que as tornam difíceis de preservar:

1. **São tomadas sob um contexto que muda.** A melhor escolha de hoje pode parecer absurda daqui a dois anos para quem não conhece as restrições da época.
2. **Suas consequências aparecem tarde.** O custo de uma decisão às vezes só se manifesta quando outra decisão depende dela.
3. **Vivem na memória de poucas pessoas.** Quando essas pessoas saem, o raciocínio sai junto.

### Qual problema resolvem

ADRs resolvem o problema da **memória arquitetural**. Com eles:

- novas pessoas entendem por que a arquitetura é como é;
- decisões não são refeitas a cada reunião;
- reverter uma decisão passa a ser uma nova decisão consciente, que considera o que a anterior tratava;
- riscos residuais aceitos ficam visíveis e têm dono.

### Decisão arquiteturalmente significativa

Nem toda decisão merece um ADR. Nygard sugere registrar as decisões que afetam a **estrutura**, as **características não funcionais**, as **dependências**, as **interfaces** ou as **técnicas de construção**. Em segurança, acrescente:

- decisões que **aceitam risco residual**;
- decisões que **desviam de um padrão** corporativo;
- decisões que **escolhem entre alternativas com trade-offs relevantes** de segurança, custo ou experiência;
- decisões **difíceis de reverter**.

Um teste simples: *se esta decisão fosse revertida daqui a um ano por alguém que não participou dela, algum risco importante poderia voltar sem que ninguém percebesse?* Se sim, ela merece um ADR.

## Fundamentos técnicos

### Extensões úteis para segurança

O formato original é deliberadamente enxuto. Para decisões de segurança, estas seções adicionais costumam valer o esforço:

| Seção | Por que acrescentar |
|:---|:---|
| **Decisores e consultados** | Saber quem decidiu e quem foi ouvido |
| **Requisitos e riscos relacionados** | Rastrear a decisão até os requisitos e ameaças que trata (ver [aula 07](07-business-driven-requirements.md)) |
| **Alternativas consideradas** | Mostrar que houve escolha, com critérios e a matriz de decisão |
| **Risco residual e dono do risco** | Tornar explícito o que permanece e quem aceitou |
| **Critérios de verificação** | Como saber se a decisão foi implementada como decidido |
| **Data de revisão** | Decisões tomadas sob restrições temporárias precisam ser revisitadas |

O modelo da Academy, com todas essas seções, está em [Architecture Decision Record](../../artifacts/architecture-decision-record.md).

### Ciclo de vida e imutabilidade

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l08-adr-lifecycle.mmd"
```

<figcaption>Figura 1 — Ciclo de vida de um ADR e encadeamento de decisões.</figcaption>
</figure>

- Um ADR **aceito não é editado** para mudar a decisão. Se a decisão muda, escreve-se um novo ADR que **substitui** o anterior, e o antigo recebe o status *Substituído por ADR-NNN*.
- Correções de forma (erros de digitação, links) são aceitáveis; mudanças de conteúdo, não.
- Decisões revertidas **não são apagadas**: o histórico é parte do valor.

Essa imutabilidade é o que diferencia um registro de decisões de uma página de documentação qualquer.

### Encadeamento

As consequências de um ADR frequentemente se tornam o **contexto** de ADRs seguintes. Exemplo:

- ADR-012 decide usar Session Manager para acesso administrativo na AWS. Consequência: dois formatos de auditoria.
- ADR-015 decide normalizar os eventos de sessão no SIEM. O contexto cita a consequência do ADR-012.

Ligações explícitas entre ADRs permitem reconstruir o raciocínio de uma área inteira.

### Onde guardar

| Tipo de decisão | Onde |
|:---|:---|
| Decisão de uma solução | No repositório da solução, junto do código e da infraestrutura como código (por exemplo, `docs/adr/`) |
| Decisão corporativa | Repositório de arquitetura corporativa, com o mesmo formato |
| Decisão que afeta ambas | No repositório corporativo, referenciada pela solução |

ADRs no repositório têm uma vantagem prática: **mudam junto com o código** que implementa a decisão e passam pelo mesmo fluxo de revisão.

### ADRs, exceções e requisitos

| Artefato | Registra | Relação |
|:---|:---|:---|
| Requisito | O que precisa ser verdade | O ADR escolhe *como* atender um ou mais requisitos |
| ADR | A escolha e suas consequências | Pode gerar exceções ou novos requisitos |
| Exceção | Um desvio temporário de padrão | Costuma ser justificada por um ADR e tem prazo próprio |

## Exemplo empresarial

!!! example "Aurora Pagamentos — ADR-012"

    A decisão tomada no exercício da [aula 03](03-conceptual-logical-physical.md#exercicio-de-tomada-de-decisao), registrada como ADR:

    ---

    **ADR-012 — Acesso administrativo aos workloads de pagamento na AWS por Session Manager**

    **Status:** Aceita · **Data:** 2026-09-15 · **Decisores:** arquiteto de segurança, líder de plataforma cloud · **Consultados:** infraestrutura do datacenter, SOC, compliance PCI

    **Contexto.** A visão lógica do acesso administrativo (ponto único de acesso, elevação just-in-time pelo broker PAM, gravação de sessões e eventos no SIEM) foi aprovada no ADR-009. Os workloads de pagamento estão migrando para a conta de produção PCI na AWS. No datacenter, o ponto único é realizado por VMs bastion. A conexão privada com a AWS é única, e incidentes recentes mostraram que, quando ela falha, a equipe perde o acesso administrativo justamente quando precisa diagnosticar o problema. A equipe de plataforma tem três pessoas.

    **Requisitos relacionados:** REQ-ADM-01 (ponto único de acesso), REQ-ADM-03 (gravação de sessões), REQ-ADM-05 (sem portas administrativas expostas na zona PCI).

    **Alternativas consideradas.** (A) Estender o bastion do datacenter pela conexão privada; (B) AWS Systems Manager Session Manager, integrado ao broker PAM; (C) bastions dedicados por conta na AWS. A matriz de decisão está no anexo; B obteve a maior pontuação, principalmente por eliminar portas de entrada nas instâncias e não depender da conexão com o datacenter.

    **Decisão.** Vamos realizar o ponto único de acesso administrativo na AWS com Session Manager. A permissão de iniciar sessões será concedida exclusivamente pelo broker PAM, por tempo limitado. O registro de sessões será obrigatório, com logs no CloudWatch Logs e chamadas de API no CloudTrail, ambos encaminhados ao SIEM. Nenhuma instância da zona PCI terá regras de entrada para SSH ou RDP.

    **Consequências.**

    - *Positivas:* elimina a exposição de portas administrativas; mantém a administração da AWS disponível quando a conexão com o datacenter falha; reduz a operação de VMs bastion.
    - *Negativas:* passam a existir dois formatos de auditoria de sessão (bastion e Session Manager), que precisam ser normalizados no SIEM; a equipe precisa aprender a operar o serviço.
    - *Neutras:* o ADR-009 continua válido; muda apenas a realização física na AWS.

    **Risco residual.** Durante a transição, consultas de auditoria precisam considerar os dois formatos, com risco de lacunas em investigações. **Dono do risco:** gerente do SOC, até a conclusão do ADR-015 (normalização no SIEM), prevista para dezembro.

    **Verificação.** (1) Config rule verificando ausência de regras de entrada 22/3389 nas instâncias da conta PCI; (2) teste mensal de que uma sessão iniciada aparece no SIEM em até 5 minutos; (3) revisão trimestral das permissões de início de sessão.

    **Revisão:** junho do próximo ano, ou antes se a AWS deixar de suportar algum requisito.

    ---

    Observe que o ADR **não repete a análise inteira**: aponta o ADR anterior, os requisitos e a matriz. E registra uma consequência negativa que gerou outro ADR — o encadeamento em ação.

## Arquitetura tradicional versus recomendada

| Aspecto | Tradicional | Recomendado |
|:---|:---|:---|
| Onde estão as decisões | Atas, e-mails, apresentações, memória | ADRs numerados no repositório |
| Alternativas | Raramente registradas | Registradas com critérios |
| Consequências negativas | Omitidas para "vender" a decisão | Explícitas — são o que protege a decisão no futuro |
| Mudança de decisão | Documento editado; histórico perdido | Novo ADR substitui o anterior |
| Riscos aceitos | Implícitos | Risco residual com dono e data de revisão |

## Controles e padrões relevantes

| Elemento | Objetivo | Referência |
|:---|:---|:---|
| Formato de ADR | Registrar decisões de forma curta e consistente | M. Nygard, *Documenting Architecture Decisions* (2011) |
| Separação entre arquitetura e sua descrição | ADRs fazem parte da descrição de arquitetura, não da arquitetura em si | ISO/IEC/IEEE 42010:2022 |
| Aceitação formal de risco | Registrar o dono do risco residual | Detalhado no Módulo 3 (tratamento de riscos) |
| Modelo da Academy | Estrutura com extensões de segurança | [Architecture Decision Record](../../artifacts/architecture-decision-record.md) |

## Aplicabilidade: on-premises, cloud e híbrido

| Aspecto | On-premises | Cloud | Híbrido |
|:---|:---|:---|:---|
| Decisões típicas | Topologia de zonas, escolha de appliances, estratégia de backup | Estrutura de contas, serviços gerenciados versus autogeridos, guardrails | Onde cada componente roda, como identidade e conectividade atravessam ambientes |
| Onde o ADR vive | Repositório de arquitetura de infraestrutura | Junto da infraestrutura como código da plataforma | Repositório corporativo, referenciado pelos dois lados |
| Quem decide | Infraestrutura com segurança | Plataforma cloud com segurança | **Ambos os donos de ambiente** — uma decisão de integração tomada por um só lado tende a ignorar as restrições do outro |
| Gatilho de revisão comum | Fim de suporte de tecnologia | Novos serviços do provedor que mudam as alternativas | Mudança na conectividade ou no modelo de identidade |

**Particularidade do híbrido:** decisões híbridas devem registrar explicitamente o **comportamento em falha da integração** (o que acontece se a conexão ou a federação cair) — exatamente o tipo de consequência que só aparece no pior momento.

## Como especificar e implementar

1. **Defina o gatilho:** quais decisões exigem ADR (use a lista de decisões significativas desta aula).
2. **Adote um modelo** — o [modelo da Academy](../../artifacts/architecture-decision-record.md) ou uma variação — e mantenha-o igual em toda a organização.
3. **Crie o diretório** de ADRs em cada repositório relevante e um índice simples.
4. **Escreva durante a decisão**, não depois: o ADR começa como *Proposta* e é discutido no mesmo fluxo de revisão do código.
5. **Defina quem aceita:** decisões de solução, pelo time com o arquiteto; decisões corporativas, pelo fórum de arquitetura; aceitação de risco, pelo dono do risco.
6. **Revise periodicamente** os ADRs com data de revisão e os riscos residuais abertos.

## Trade-offs, limitações e antipadrões

| Antipadrão | Sintoma | Correção |
|:---|:---|:---|
| **ADR para tudo** | Centenas de ADRs triviais; ninguém lê | Registrar apenas decisões significativas |
| **ADR retroativo** | Escrito meses depois, para cumprir processo | Escrever como proposta, durante a decisão |
| **ADR de propaganda** | Só consequências positivas | Exigir consequências negativas e risco residual |
| **ADR editável** | A decisão muda e o documento é sobrescrito | Imutabilidade; substituição por novo ADR |
| **ADR sem contexto** | "Decidimos usar X" | Contexto factual com as forças em conflito |
| **ADR como aprovação burocrática** | O documento vira formulário de autorização | O ADR registra raciocínio; a aprovação é um campo, não o propósito |
| **Risco residual sem dono** | "Risco aceito" sem nome | Dono do risco com autoridade e data de revisão |

**Limitação:** ADRs registram decisões, mas não garantem que elas sejam implementadas. Por isso a seção de **verificação** é tão importante — e por isso ADRs funcionam melhor quando vivem perto do código que os implementa.

## Como validar

| Indicador | Critério |
|:---|:---|
| Cobertura | Decisões significativas dos projetos de alto risco têm ADR |
| Completude | ADRs aceitos têm contexto, alternativas, consequências negativas e risco residual |
| Atualidade | ADRs com data de revisão vencida são revisados |
| Rastreabilidade | ADRs apontam requisitos; exceções apontam ADRs |
| Verificação | Critérios de verificação dos ADRs estão automatizados ou incluídos em revisões |

## Como apresentar e justificar

- **Para a diretoria:** "Cada decisão relevante de segurança passa a ter um registro de uma página, com o risco que permanece e quem o aceitou. Isso reduz a dependência de pessoas-chave e responde a auditorias com rapidez."
- **Para engenharia:** "ADRs ficam no repositório e passam pelo mesmo pull request do código. Escrever um custa menos do que rediscutir a mesma decisão a cada trimestre."
- **Para novos membros da equipe:** "Antes de propor mudar algo, leia os ADRs da área. Se o contexto mudou, proponha um novo ADR que substitua o anterior."

## Checklist de revisão arquitetural

- [ ] O ADR trata de uma única decisão significativa.
- [ ] O contexto descreve as forças em jogo de forma factual, inclusive conflitos.
- [ ] As alternativas consideradas estão listadas, com critérios.
- [ ] A decisão está em voz ativa e é específica.
- [ ] As consequências incluem efeitos negativos.
- [ ] O risco residual tem dono com autoridade adequada.
- [ ] Há critérios de verificação e data de revisão.
- [ ] O ADR aponta requisitos, ADRs relacionados e exceções.
- [ ] Em decisões híbridas, o comportamento em falha da integração está descrito.

## Questões de compreensão

**1.** Quais das decisões a seguir merecem um ADR? (a) Renomear uma variável em um módulo de infraestrutura. (b) Usar um provedor de identidade separado para clientes. (c) Aceitar que um sistema legado não use mTLS por nove meses. (d) Atualizar uma biblioteca de log para uma versão de correção.

??? success "Resposta comentada"

    **(b)** e **(c)**. A decisão (b) afeta estrutura, dependências e interfaces, e é difícil de reverter. A decisão (c) aceita risco residual e desvia de um padrão — além do ADR, gera uma exceção com prazo. As decisões (a) e (d) são de implementação, sem efeito arquitetural.

**2.** Uma decisão registrada em ADR mudou. Por que não basta editar o ADR original?

??? success "Resposta comentada"

    Porque se perderia o histórico do raciocínio: por que a decisão anterior foi tomada, sob quais restrições, e por que mudou. O correto é escrever um novo ADR que **substitui** o anterior, que recebe o status *Substituído por ADR-NNN*. A imutabilidade é o que permite confiar no registro.

**3.** Por que as consequências negativas são a parte mais importante de um ADR para o futuro?

??? success "Resposta comentada"

    Porque são elas que explicam os custos aceitos e os riscos que permaneceram. Quem revisitar a decisão precisa saber o que já se sabia que era ruim — para não "descobrir" o problema de novo, nem eliminar a decisão sem considerar o que ela evitava. Um ADR sem consequências negativas parece uma peça de convencimento, não um registro.

**4.** Em uma decisão híbrida, que consequência costuma ser omitida e deveria estar explícita?

??? success "Resposta comentada"

    O **comportamento em falha da integração**: o que acontece com autenticação, acesso administrativo, registro de eventos e operação quando a conexão entre ambientes ou a federação de identidade falham.

## Exercício de tomada de decisão

!!! question "Cenário: revise este ADR"

    A equipe de integração da Aurora submeteu o ADR abaixo para aceitação. Identifique pelo menos **seis problemas** e proponha como corrigi-los. Depois, suponha que a análise mostrou que o único requisito do time não atendido pelo serviço corporativo de segredos é a integração nativa com o barramento de integração, contornável com um conector. Compare (A) serviço corporativo de segredos com conector; (B) CofreX; (C) serviço gerenciado de segredos do provedor cloud, pelos critérios aderência ao padrão e integração com rotação e SIEM, atendimento aos requisitos do time e custo de operação, e escreva a decisão do ADR corrigido.

    > **ADR-020 — Usar o produto CofreX**
    >
    > **Status:** Aceito
    >
    > **Contexto:** Precisamos guardar segredos.
    >
    > **Decisão:** O CofreX é o melhor cofre do mercado e será usado pelo time de integração. Ele tem criptografia forte e é muito seguro.
    >
    > **Consequências:** Os segredos ficarão seguros. O time ficará mais produtivo.

??? success "Resolução de referência"

    | # | Problema | Correção |
    |:---|:---|:---|
    | 1 | O título nomeia um produto, não a decisão | "Gestão de segredos do time de integração fora do serviço corporativo" — ou, se não houver desvio, "Uso do serviço corporativo de segredos pelo time de integração" |
    | 2 | Status *Aceito* sem decisores nem data | Status *Proposta* até a análise; registrar decisores, consultados e data |
    | 3 | Contexto vazio: não descreve forças, restrições nem conflito | Descrever quais segredos, volume, requisitos de rotação, a existência de um **serviço corporativo de segredos** (padrão vigente) e por que ele seria ou não adequado |
    | 4 | Não há alternativas consideradas | Listar ao menos: usar o serviço corporativo; usar o CofreX; usar um serviço gerenciado do provedor cloud — com critérios |
    | 5 | Decisão justificada por adjetivos ("o melhor", "muito seguro") | Justificar pelos critérios e requisitos atendidos |
    | 6 | Desvio de padrão sem exceção | Se o CofreX for mantido, registrar exceção ao padrão corporativo, com prazo e compensatórios |
    | 7 | Consequências só positivas | Incluir negativas: novo componente para operar, auditar e integrar ao SIEM; dois locais de segredos na organização; custo de licença |
    | 8 | Sem risco residual nem dono | Registrar riscos (por exemplo, segredos fora do processo corporativo de rotação e de resposta a incidentes) e o dono |
    | 9 | Sem verificação nem revisão | Critérios de verificação (rotação, logs no SIEM) e data de revisão |

    **Comparação das alternativas:**

    | Critério | Peso | A — Serviço corporativo com conector | B — CofreX | C — Serviço do provedor cloud |
    |:---|:---|:---|:---|:---|
    | Aderência ao padrão e integração com rotação e SIEM | 3 | 3 | 1 | 2 |
    | Atendimento aos requisitos do time | 2 | 2 | 3 | 2 |
    | Custo de operação | 2 | 3 | 1 | 2 |
    | **Total ponderado** | | **19** | **11** | **14** |

    **Decisão do ADR corrigido:** "Usaremos o serviço corporativo de segredos, com um conector para o barramento de integração, porque atende aos requisitos de rotação e auditoria sem criar um segundo local de segredos. Rejeitamos o CofreX porque exigiria exceção ao padrão para resolver um requisito que o conector atende." Consequência negativa a registrar: o conector é um componente novo, com dono e manutenção.

    **Ponto central:** um ADR que não menciona o padrão corporativo de segredos esconde que se trata de um **desvio**. A pergunta certa para o fórum não é "o CofreX é bom?", mas "o serviço corporativo não atende a qual requisito, e o desvio se justifica?".

## Pontos-chave

- ADRs registram uma decisão significativa: contexto, decisão, status e consequências — em uma ou duas páginas.
- Registre decisões que afetam estrutura, qualidades, dependências, interfaces, técnicas de construção, aceitam risco ou desviam de padrões.
- Consequências negativas e risco residual com dono são o que tornam o ADR útil no futuro.
- ADRs aceitos são imutáveis: mudanças geram novos ADRs que substituem os anteriores.
- ADRs vivem perto do código, ligam-se a requisitos e exceções, e precisam de critérios de verificação.

<!-- next-steps:start -->

!!! tip "Próximos passos"

    Você concluiu a última aula do **Módulo 2** — [voltar ao módulo](index.md).

    Pratique e avalie o módulo:

    - [Laboratório 02 — Modelagem arquitetural como código](../../labs/lab-02-architecture-modeling.md)
    - [Avaliação do Módulo 2](../../assessments/m02-security-architecture.md)

    Atividades integradoras:

    - [Caso A — Datacenter tradicional (Meridiana Distribuidora)](../../case-studies/case-a-meridiana/index.md)
    - [Avaliação integradora do Módulo Inicial ao Módulo 2](../../assessments/fundamentals-final.md)

    Em seguida: [Módulo 3 — Governança, Riscos e Controles](../../modules/03-governance-risk/index.md).

<!-- next-steps:end -->

## Referências

- M. Nygard. *Documenting Architecture Decisions*. Cognitect, 2011. <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions> — gratuito.
- ISO/IEC/IEEE. *42010:2022 — Software, systems and enterprise — Architecture description*. 2022. <https://committee.iso.org/standard/74393.html> — norma paga, não consultada na íntegra; a descrição usada nesta aula se apoia na página oficial da norma e em resumos públicos.

### Leituras de aprofundamento

Incluídas na revisão bibliográfica de 2026-10-23, **depois** da escrita desta aula: complementam e permitem conferir o conteúdo, mas não foram a base original do texto. A situação de cada leitura está entre parênteses.

- NIST. *SP 800-160 Vol. 1 Rev. 1*, 2022, Apêndice I.3 *Decision Management* (p. 153). *(localizado pelo sumário.)*
- H. Adkins *et al.* *Building Secure and Reliable Systems*. O'Reilly, 2020, Cap. 4 *Design Tradeoffs*. *(sumário conferido; leitura pendente.)*

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
| Revisão bibliográfica | 2026-10-23 — [registro da revisão retroativa](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/retroactive-review-m02.md) |
