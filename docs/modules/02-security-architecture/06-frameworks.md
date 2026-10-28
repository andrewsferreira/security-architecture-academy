---
id: M02-L06
title: "Aula 06 — Frameworks, padrões e certificações: NIST, SABSA, TOGAF, CISSP e ISSAP"
public_title: "Módulo 2 — Aula 06 — Frameworks, padrões e certificações: NIST, SABSA, TOGAF, CISSP e ISSAP"
description: A diferença entre framework, método, padrão, arquitetura de referência e certificação; o propósito de NIST CSF, RMF, SP 800-53, SABSA e TOGAF; o que as certificações CISSP e ISSAP representam; e por que conformidade não é sinônimo de segurança efetiva.
domain: enterprise-architecture
tier: professional
status: published
prerequisites: [M02-L02, M02-L04]
objectives:
  - Classificar frameworks por propósito — resultados, processo, catálogo de controles, método de arquitetura e mapa de competências.
  - Explicar o que NIST CSF 2.0, NIST RMF, SP 800-53, SABSA e TOGAF oferecem e onde se limitam.
  - Combinar frameworks de forma coerente para o contexto de uma organização.
  - Diferenciar conformidade normativa de segurança efetiva.
minutes: 90
sources: [NIST-CSF-2, NIST-CSF-FAQ, NIST-RMF, NIST-SP800-53, NIST-SP800-160-V1R1, SABSA-W101, TOG-TOGAF-10, TOG-RISK-SECURITY, ISC2-CISSP-OUTLINE, ISC2-ISSAP-2025, CIS-CONTROLS-V8-1]
further_reading: [NIST-CSF-INFORMATIVE-REFS, BOOK-ANDERSON-SE3, SABSA-W101, SABSA-W100]
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
module: M02
---

# Aula 06 — Frameworks, padrões e certificações: NIST, SABSA, TOGAF, CISSP e ISSAP { #frameworks-padroes-e-certificacoes-nist-sabsa-togaf-cissp-e-issap }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 2 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">90 min · ID técnico: M02-L06</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    "Qual framework devemos adotar?" é uma pergunta mal formulada. Frameworks diferentes respondem a perguntas diferentes: um descreve resultados, outro organiza um processo, outro lista controles, outro conecta o negócio ao mecanismo técnico. E nem tudo o que aparece nessas listas é framework: há padrões publicados por organismos de normalização e certificações profissionais. Esta aula separa essas categorias, classifica os principais frameworks por propósito, mostra como combiná-los e explica por que nenhum deles, sozinho, garante segurança.

**Pré-requisitos:** [Enterprise, Solution e Security Architecture](02-enterprise-solution-security-architecture.md) e [Princípios, padrões, baselines e exceções](04-principles-standards-baselines-exceptions.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Classificar frameworks por propósito — resultados, processo, catálogo de controles, método de arquitetura e mapa de competências.
- Explicar o que NIST CSF 2.0, NIST RMF, SP 800-53, SABSA e TOGAF oferecem e onde se limitam.
- Combinar frameworks de forma coerente para o contexto de uma organização.
- Diferenciar conformidade normativa de segurança efetiva.

## Conceito

### O que é um framework

Um framework é uma **estrutura reutilizável** que organiza conhecimento, decisões ou atividades em torno de um propósito. Em segurança, a palavra é usada para coisas muito diferentes — e essa é a raiz da confusão:

| Tipo | Pergunta que responde | Exemplos |
|:---|:---|:---|
| **Framework de resultados** | *O que precisamos alcançar?* | NIST CSF 2.0 |
| **Framework de processo** | *Que passos seguir?* | NIST RMF (SP 800-37), TOGAF ADM |
| **Catálogo de controles** | *Que controles existem para escolher?* | NIST SP 800-53, CIS Controls |
| **Método de arquitetura** | *Como ir do negócio ao mecanismo com rastreabilidade?* | SABSA, TOGAF |
| **Engenharia de sistemas** | *Como incorporar segurança ao ciclo de engenharia?* | NIST SP 800-160 |
| **Sistema de gestão** | *Como gerir a segurança de forma contínua e auditável?* | ISO/IEC 27001 (detalhado no Módulo 3) |
| **Mapa de competências** | *O que um profissional deve saber?* | Outlines de CISSP e ISSAP |

### Framework, método, padrão, referência e certificação

Os nomes desta aula pertencem a categorias diferentes, e confundi-las leva a escolhas erradas — por exemplo, organizar um projeto pelos domínios de uma certificação.

| Categoria | O que é | Exemplos nesta aula |
|:---|:---|:---|
| **Framework** | Estrutura que organiza resultados, atividades ou conhecimento; geralmente de adoção voluntária e adaptável | NIST CSF 2.0, NIST RMF |
| **Método** | Sequência de passos e técnicas para produzir um resultado, como uma arquitetura | SABSA, TOGAF ADM |
| **Padrão (*standard*)** | Documento publicado por um organismo, com requisitos ou práticas que podem ser exigidos por contrato, regulação ou certificação de conformidade | ISO/IEC 27001; *The TOGAF Standard*; NIST SP 800-53 como catálogo de controles |
| **Arquitetura de referência** | Modelo de solução reutilizável para um tipo de problema ([aula 05](05-reference-architectures-blueprints.md)) | AWS SRA, MCRA |
| **Certificação profissional** | Atestado de que uma pessoa demonstrou conhecimentos descritos em um *outline* | CISSP e ISSAP, da ISC2 |

As fronteiras não são rígidas — o TOGAF é publicado como padrão e contém um método; o SABSA é chamado de framework e de método. O que importa é saber **qual pergunta** cada um responde, assunto da próxima tabela.

### Por que existem tantos

Porque os problemas são diferentes. Uma diretoria precisa de uma linguagem comum para falar de postura e prioridades; um arquiteto precisa de um método que conecte o negócio ao desenho; uma equipe precisa saber quais controles implementar; um órgão regulador precisa de evidências verificáveis. Nenhum framework único faz tudo isso bem.

### Qual problema esta aula resolve

Dois erros opostos são comuns:

1. **Tratar frameworks como equivalentes** — "já usamos CIS, não precisamos de CSF". Um é catálogo priorizado de controles, o outro é linguagem de resultados e governança.
2. **Adotar todos** — mapeamentos sem fim entre frameworks, documentação que ninguém usa, e nenhum ganho de segurança.

O caminho é escolher frameworks **pelo propósito**, combiná-los conscientemente e lembrar que eles organizam o trabalho, mas não o substituem.

### Conformidade normativa × segurança efetiva

Esta é a aula principal do currículo para essa distinção. **Conformidade** significa que a organização demonstrou atender a um conjunto de requisitos em um momento, segundo um método de avaliação. **Segurança efetiva** significa que os riscos relevantes estão de fato reduzidos a um nível aceitável, continuamente.

As duas se sobrepõem, mas não coincidem:

- Uma organização pode ser **conforme e insegura**: o controle existe no papel e na amostra auditada, mas não cobre os ativos que importam, ou não funciona sob ataque real.
- Pode ser **segura em um aspecto e não conforme**: um controle eficaz implementado de forma diferente da exigida.

Frameworks de conformidade são valiosos — criam disciplina, evidências e linguagem comum. O erro é tratá-los como **teto** quando deveriam ser **piso**.

## Fundamentos técnicos

### NIST Cybersecurity Framework 2.0

Publicado em fevereiro de 2024, o CSF 2.0 é uma **taxonomia de resultados de cibersegurança** de alto nível, aplicável a organizações de qualquer setor e porte. Seus elementos centrais:

- **Seis Functions:** *Govern, Identify, Protect, Detect, Respond* e *Recover*. A função *Govern*, nova na versão 2.0, trata da estratégia, das expectativas, da política e dos papéis de gestão de riscos de cibersegurança.
- **Organizational Profiles:** o *Current Profile* descreve os resultados que a organização alcança hoje; o *Target Profile*, os que deseja alcançar. A diferença entre eles orienta prioridades.
- **Tiers:** *Partial, Risk Informed, Repeatable* e *Adaptive* descrevem o rigor das práticas de gestão de riscos.

**Para o arquiteto:** o CSF é a linguagem com que a arquitetura se comunica com a governança. Um roadmap de arquitetura que mostra como fecha lacunas entre o perfil atual e o perfil-alvo é compreensível para a diretoria.

**Limite:** o CSF descreve *o que* alcançar, não *como* desenhar a arquitetura nem quais controles específicos implementar.

### NIST Risk Management Framework (SP 800-37 Rev. 2)

O RMF organiza a gestão de riscos de segurança e privacidade **no ciclo de vida de um sistema**, em sete passos: *Prepare, Categorize, Select, Implement, Assess, Authorize* e *Monitor*. A seleção de controles usa o catálogo da SP 800-53, e a autorização é uma decisão baseada em risco tomada por um responsável sênior.

**Para o arquiteto:** o RMF mostra onde as decisões de arquitetura entram no processo de risco — especialmente nos passos *Select* e *Implement*.

**Limite:** foi desenhado para sistemas de informação no contexto federal norte-americano; fora desse contexto é usado como referência de processo, adaptado.

### NIST SP 800-53 Rev. 5

Catálogo extenso de **controles de segurança e privacidade**, organizado em famílias (por exemplo, AC — Access Control, AU — Audit and Accountability, CM — Configuration Management). A Release 5.2.0, de agosto de 2025, acrescentou orientações sobre atualização e integridade de software.

**Para o arquiteto:** linguagem precisa para especificar controles e rastrear requisitos.

**Limite:** é um catálogo, não uma priorização — selecionar todos os controles seria inviável e desnecessário. Os **CIS Controls v8.1**, com seus grupos de implementação IG1 a IG3, oferecem uma priorização mais direta para organizações que precisam começar pelo essencial.

### NIST SP 800-160 Vol. 1 Rev. 1

Trata a segurança como disciplina de **engenharia de sistemas**: a segurança é uma propriedade emergente, que exige um processo disciplinado ao longo de todo o ciclo de vida, e a responsabilidade não é apenas dos especialistas em segurança.

**Para o arquiteto:** fundamenta a integração da arquitetura ao ciclo de vida (visto na [aula 01](01-security-architect-role.md)).

**Limite:** descreve processos e princípios de engenharia de sistemas, não um método de arquitetura corporativa nem um catálogo de controles; aplicá-lo exige adaptação ao porte e ao ciclo de vida da organização. Os princípios de design do seu Apêndice E são a referência de nomenclatura usada na [Aula 02 do Módulo 1](../01-security-fundamentals/02-secure-design-principles.md).

### SABSA

O SABSA é um método de **arquitetura de segurança orientada ao negócio**. Suas ideias centrais:

- **Camadas de abstração**, cada uma com uma perspectiva: *Contextual* (visão do negócio), *Conceptual* (visão do arquiteto), *Logical* (visão do projetista), *Physical* (visão do construtor), *Component* (visão do especialista) e *Security Service Management*, a visão do gestor de serviços, que atravessa as demais. O modelo segue de perto o trabalho de John Zachman em arquitetura corporativa, adaptado à segurança.
- **Seis perguntas** aplicadas a cada camada: o quê (ativos), por quê (motivação, expressa em termos de risco), como (processos), quem (pessoas), onde (localização) e quando (tempo) — formando a matriz SABSA de 6 × 6.
- **Business Attributes Profile:** técnica de engenharia de requisitos, descrita como o coração do método, que traduz necessidades de negócio em uma forma normalizada. O perfil seleciona atributos de uma taxonomia (agrupada em categorias como gestão, usuário, operação, gestão de riscos, estratégia técnica, estratégia de negócio e jurídico-regulatória) — por exemplo, *Available*, *Auditable*, *Compliant*, *Usable*, *Scalable* —, cada um com definição e métrica, e fica na camada conceitual da matriz.
- **Rastreabilidade bidirecional:** cada mecanismo técnico deve ser justificável por um requisito de negócio, e cada requisito de negócio deve estar coberto por mecanismos.

**Para o arquiteto:** é o método mais diretamente útil para a [aula 07](07-business-driven-requirements.md) — derivar requisitos de segurança do negócio.

**Limite:** exige disciplina e investimento em formação; aplicado integralmente a soluções pequenas, pode ser excessivo. Muitas organizações adotam seus conceitos (atributos, rastreabilidade, camadas) sem o método completo.

!!! note "Fontes sobre o SABSA"

    O SABSA é mantido pelo SABSA Institute, que disponibiliza white papers introdutórios. A descrição das camadas, das perguntas e do Business Attributes Profile nesta aula foi conferida no texto do *SABSA White Paper* (W100, © 1995–2009 SABSA Limited), pp. 8–20 — lido em uma cópia hospedada fora do site do instituto, já que o catálogo oficial não expõe o link direto ao ambiente de verificação. O tema é aprofundado no Módulo 16.

### TOGAF

O TOGAF (*The TOGAF Standard*) é um padrão aberto de **arquitetura corporativa** mantido pela The Open Group; a 10ª edição foi lançada em 2022 com estrutura modular. Seu núcleo é o **ADM (Architecture Development Method)**, um ciclo iterativo com uma fase preliminar, as fases A a H — visão de arquitetura; arquiteturas de negócio, de sistemas de informação e de tecnologia; oportunidades e soluções; planejamento de migração; governança da implementação; e gestão de mudanças na arquitetura — e a gestão de requisitos no centro.

A segurança não é um domínio separado no TOGAF. A The Open Group publica um guia específico — *Integrating Risk and Security within a TOGAF Enterprise Architecture* — que orienta como incorporar risco e segurança ao método, propondo um catálogo de serviços de segurança. Um white paper conjunto com o SABSA Institute, de 2011, trata da integração entre os dois métodos.

**Para o arquiteto:** é o processo no qual a arquitetura de segurança precisa se inserir em organizações que praticam EA formalmente.

**Limite:** é amplo e genérico; sem adaptação, tende a gerar documentação extensa.

### CISSP e ISSAP

CISSP e ISSAP **não são frameworks de arquitetura**: são certificações da ISC2, cujos outlines descrevem o conhecimento esperado de um profissional.

| Certificação | Outline vigente | Estrutura | Uso para o arquiteto |
|:---|:---|:---|:---|
| **CISSP** | Desde 15/04/2024 | Oito domínios, de *Security and Risk Management* a *Software Development Security*; o domínio 3 é *Security Architecture and Engineering* | Mapa amplo de conhecimento em segurança |
| **ISSAP** | Desde 01/08/2025 | Quatro domínios: GRC (21%), *Security Architecture Modeling* (22%), *Infrastructure and System Security Architecture* (32%) e *IAM Architecture* (25%) | Mapa do conhecimento específico de arquitetura; exige o CISSP |

Use os outlines como **checklists de competência** — para identificar lacunas próprias ou da equipe —, e não como método de trabalho. O mapeamento completo para os módulos está em [Mapeamento para certificações](../../certification-mapping/index.md).

### Como os frameworks se complementam

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l06-framework-map.mmd"
```

<figcaption>Figura 1 — Como os frameworks se complementam.</figcaption>
</figure>

| Framework | Propósito | Melhor uso | Limitação principal | Acesso |
|:---|:---|:---|:---|:---|
| NIST CSF 2.0 | Resultados e governança | Linguagem com a diretoria; perfis atual e alvo | Não diz como desenhar | Gratuito |
| NIST RMF | Processo de risco por sistema | Ciclo de vida de autorização de sistemas | Origem no contexto federal dos EUA | Gratuito |
| NIST SP 800-53 | Catálogo de controles | Especificar controles com precisão | Extenso; exige seleção | Gratuito |
| CIS Controls v8.1 | Controles priorizados | Começar pelo essencial (IG1) | Menos detalhe arquitetural | Gratuito |
| SABSA | Método orientado ao negócio | Derivar requisitos e rastrear decisões | Curva de aprendizado | White papers; formação paga |
| TOGAF | Arquitetura corporativa | Inserir a segurança no processo de EA | Genérico, documentação extensa | Acesso ao padrão completo não confirmado |
| CISSP / ISSAP | Mapas de competência | Desenvolvimento profissional | Não são métodos | Outline público; exame pago |

## Exemplo empresarial

!!! example "Grupo Horizonte — cada framework no seu lugar"

    O conselho do Grupo Horizonte pediu "um framework único de segurança para o grupo". O arquiteto de segurança propôs uma combinação, cada peça com um propósito:

    | Necessidade | Framework | Como foi usado |
    |:---|:---|:---|
    | Comparar a postura das quatro subsidiárias e reportar ao conselho | NIST CSF 2.0 | Um *Current Profile* por subsidiária e um *Target Profile* do grupo, ajustado ao risco de cada negócio |
    | Definir controles mínimos para subsidiárias pequenas | CIS Controls v8.1 | IG1 como piso para todas; IG2 para as que tratam dados de saúde e financeiros |
    | Desenhar o novo portal de laudos de saúde ocupacional | Conceitos do SABSA | Business Attributes Profile do portal, com métricas, e rastreabilidade até os mecanismos |
    | Inserir a segurança nos projetos de arquitetura corporativa | TOGAF (já usado pela EA do grupo) | Requisitos de segurança incluídos nas fases de visão e de arquitetura; catálogo de serviços de segurança mantido pela EA |
    | Desenvolver a equipe de arquitetura | Outline do ISSAP | Mapa de lacunas de competência por arquiteto |

    O resultado não foi "um framework único", mas **uma linguagem única para o conselho** (CSF) e ferramentas específicas para cada nível de decisão.

## Arquitetura tradicional versus recomendada

| Aspecto | Tradicional | Recomendado |
|:---|:---|:---|
| Escolha | "Adotamos o framework X" | Combinação explícita, cada framework com um propósito |
| Relação com auditoria | Arquitetura desenhada para passar na auditoria | Arquitetura desenhada para reduzir riscos; a conformidade é demonstrada a partir dela |
| Mapeamentos | Planilhas extensas cruzando todos os frameworks | Mapeamento apenas onde há uso real (por exemplo, controles para perfis do CSF) |
| Certificações | Usadas como método de trabalho | Usadas como mapa de competências |

## Controles e padrões relevantes

| Uso | Framework | Elemento |
|:---|:---|:---|
| Governança e papéis de cibersegurança | NIST CSF 2.0 | Função *Govern* |
| Priorização da arquitetura | NIST CSF 2.0 | Lacuna entre *Current* e *Target Profile* |
| Seleção de controles para um sistema | NIST RMF + SP 800-53 | Passos *Categorize* e *Select* |
| Piso de controles para organizações pequenas | CIS Controls v8.1 | Implementation Group 1 |
| Requisitos de segurança orientados ao negócio | SABSA | Business Attributes Profile |
| Integração da segurança à EA | TOGAF | Guia *Integrating Risk and Security* |

## Aplicabilidade: on-premises, cloud e híbrido

Os frameworks neutros (CSF, RMF, SP 800-53, SABSA, TOGAF) **valem igualmente para todos os ambientes**. O que muda é a camada de frameworks específicos de cada provedor e a forma de mapear entre eles.

| Aspecto | On-premises | Cloud | Híbrido |
|:---|:---|:---|:---|
| Frameworks específicos | Benchmarks de configuração por tecnologia | Frameworks dos provedores (AWS, Azure e Google Cloud Well-Architected) e benchmarks de cloud | Os dois conjuntos |
| Evidência de conformidade | Coletada manualmente ou por varreduras | Serviços de postura do provedor, com mapeamentos prontos para alguns frameworks | Precisa ser consolidada em uma visão única |
| Responsabilidade pelos controles | Organização | Compartilhada — parte dos controles é herdada do provedor | Mistura; o perfil precisa indicar quem implementa cada resultado |
| Risco específico | Perfil baseado em amostras pouco representativas | Confundir conformidade do provedor com conformidade da carga de trabalho | Perfis separados por ambiente que escondem lacunas nas integrações |

**Particularidade do híbrido:** mantenha **um único perfil CSF por escopo de negócio**, cobrindo todos os ambientes, e use os frameworks dos provedores como fonte de evidência para os resultados correspondentes. Perfis separados por ambiente tendem a esconder justamente os riscos que ficam entre eles.

## Como especificar e implementar

Para escolher a combinação de frameworks de uma organização, responda:

1. **Qual linguagem a diretoria e os reguladores esperam?** Isso define o framework de resultados ou o sistema de gestão.
2. **Há exigências contratuais ou regulatórias específicas?** Elas definem obrigações não negociáveis (por exemplo, PCI DSS para dados de cartão).
3. **Qual a maturidade e a capacidade da equipe?** Organizações iniciantes ganham mais com um catálogo priorizado do que com um catálogo extenso.
4. **A organização pratica arquitetura corporativa formal?** Se sim, a segurança precisa se integrar ao método existente.
5. **Onde estão os maiores riscos de desenho?** Soluções de alto risco justificam um método orientado ao negócio.

Registre a combinação escolhida — e o propósito de cada peça — em um ADR corporativo.

## Trade-offs, limitações e antipadrões

| Antipadrão | Sintoma | Correção |
|:---|:---|:---|
| Fadiga de frameworks | Equipe dedicada a mapeamentos, sem tempo para reduzir riscos | Manter apenas os mapeamentos que têm uso |
| Arquitetura de auditoria | Decisões guiadas pela pergunta "o auditor aceita?" | Guiar pelo risco; demonstrar conformidade a partir do desenho |
| Framework como produto | "Implantamos o CSF" | O CSF é linguagem e estrutura; a implantação é de controles e práticas |
| Certificação como método | Projetos organizados pelos domínios do CISSP | Usar outlines para competências; métodos de arquitetura para projetos |
| Equivalência forçada | "CIS e SP 800-53 são a mesma coisa" | Explicar propósitos diferentes: priorização versus catálogo |

## Como validar

- **Uso efetivo:** cada framework adotado tem um uso identificável (relatório, decisão, processo) e um responsável.
- **Fechamento de lacunas:** a arquitetura reduz a diferença entre os perfis atual e alvo ao longo do tempo.
- **Testes de efetividade:** exercícios de ataque, revisões de incidentes e testes de controles mostram se o que está conforme também é eficaz.
- **Divergência entre conformidade e incidentes:** incidentes em áreas avaliadas como conformes indicam que a avaliação mede presença, não efetividade.

## Como apresentar e justificar

- **Para o conselho:** "Usaremos o CSF 2.0 para reportar a postura de cada subsidiária em uma linguagem comum. As prioridades de investimento saem da diferença entre o perfil atual e o perfil-alvo."
- **Para auditoria:** "A conformidade é demonstrada a partir dos controles da arquitetura; cada resultado do perfil aponta para controles e evidências."
- **Para engenharia:** "O CIS IG1 é o piso; não haverá exigências derivadas de frameworks que não tenham um risco associado."

## Checklist de revisão arquitetural

- [ ] A organização sabe qual framework usa para cada propósito, e por quê.
- [ ] A combinação de frameworks está registrada em ADR corporativo.
- [ ] Os resultados do perfil-alvo estão ligados a capacidades e controles da arquitetura.
- [ ] Obrigações regulatórias específicas estão identificadas separadamente dos frameworks voluntários.
- [ ] A efetividade dos controles é testada, além da sua presença.
- [ ] Em ambientes híbridos, há um perfil por escopo de negócio, cobrindo todos os ambientes.
- [ ] Certificações são usadas como mapa de competências, não como método de projeto.

## Questões de compreensão

**1.** Uma gerente afirma: "Já seguimos o CIS Controls; o CSF seria redundante." Avalie a afirmação.

??? success "Resposta comentada"

    É incorreta. O CIS Controls é um conjunto priorizado de controles; o CSF 2.0 é uma taxonomia de resultados, com governança, perfis e tiers, usada para comunicar e priorizar. Eles são complementares: o CSF diz o que alcançar e permite reportar a postura; o CIS ajuda a escolher controles para alcançar parte desses resultados.

**2.** Em que passo do RMF as decisões de arquitetura têm maior influência, e por quê?

??? success "Resposta comentada"

    Principalmente nos passos **Select** e **Implement**: é ali que os controles são escolhidos e posicionados no sistema. O passo **Categorize** também depende da arquitetura, porque o impacto é avaliado sobre os componentes e fluxos que ela define.

**3.** O que é um Business Attributes Profile no SABSA e por que ele é útil?

??? success "Resposta comentada"

    É um conjunto de atributos de negócio que a segurança precisa garantir (por exemplo, disponível, confidencial, rastreável), cada um com definição e métrica. É útil porque transforma necessidades de negócio em requisitos mensuráveis e permite rastrear cada mecanismo técnico até um atributo — e vice-versa.

**4.** Dê um exemplo de organização conforme e insegura.

??? success "Resposta comentada"

    Uma empresa que atende ao requisito de revisão trimestral de acessos com evidências impecáveis, mas cuja revisão cobre apenas os sistemas do escopo da auditoria. Contas privilegiadas órfãs em sistemas fora do escopo — mas conectados ao ambiente auditado — permanecem ativas. O controle existe e é conforme; o risco continua.

**5.** Por que CISSP e ISSAP não devem ser usados como método de arquitetura?

??? success "Resposta comentada"

    Porque seus outlines descrevem **conhecimentos esperados de um profissional**, organizados para avaliação, e não um processo para desenhar arquiteturas. São úteis para mapear competências e lacunas; para conduzir projetos, usam-se métodos como SABSA, TOGAF e as práticas de modelagem vistas neste módulo.

## Exercício de tomada de decisão

!!! question "Cenário: o pedido do conselho"

    A subsidiária de logística do Grupo Horizonte (200 funcionários, equipe de TI de seis pessoas, nenhum profissional dedicado à segurança) recebeu do conselho a orientação de "adotar os melhores frameworks do mercado". Uma consultoria propôs:

    - **A — Adoção completa:** certificação ISO/IEC 27001, perfis CSF, SABSA para todos os projetos e TOGAF para a arquitetura da subsidiária.
    - **B — Combinação proporcional:** perfil CSF 2.0 integrado ao perfil do grupo; CIS Controls v8.1 IG1 como piso de controles; conceitos de SABSA apenas para projetos com gatilho de alto risco.
    - **C — Certificação primeiro:** foco exclusivo na certificação ISO/IEC 27001 nos próximos 12 meses.

    Critérios: adequação ao propósito, tempo até redução de risco, capacidade de execução e coerência com o grupo.

??? success "Resolução de referência"

    | Critério | Peso | A — Completa | B — Proporcional | C — Certificação |
    |:---|:---|:---|:---|:---|
    | Adequação ao propósito | 3 | 2 | 3 | 2 |
    | Tempo até redução de risco | 3 | 1 | 3 | 1 |
    | Capacidade de execução | 2 | 1 | 3 | 2 |
    | Coerência com o grupo | 2 | 2 | 3 | 2 |
    | **Total ponderado** | | **15** | **30** | **17** |

    **Recomendação: B.** Com seis pessoas de TI e nenhum especialista, a adoção completa consumiria a capacidade da equipe em documentação, e a certificação como primeiro passo concentraria o esforço em evidências antes de reduzir os riscos mais básicos. A combinação B coloca a subsidiária na linguagem do grupo (CSF), dá um piso concreto de controles (IG1) e reserva o método mais pesado para os projetos que o justificam.

    **Observação:** se houver exigência contratual de certificação ISO/IEC 27001 por parte de clientes, ela passa a ser uma restrição — e o plano deve incluí-la, preferencialmente aproveitando o trabalho do CSF e do IG1 como base.

    **Risco residual:** controles além do IG1 em áreas específicas (por exemplo, integrações com transportadoras) ficam para fases posteriores; devem constar do perfil-alvo com prazo.

## Pontos-chave

- Framework, método, padrão, arquitetura de referência e certificação são categorias diferentes; frameworks diferentes respondem a perguntas diferentes: resultados, processo, catálogo de controles, método de arquitetura ou competências.
- CSF 2.0 é a linguagem de governança; RMF, o processo por sistema; SP 800-53 e CIS, os catálogos; SABSA e TOGAF, os métodos de arquitetura.
- CISSP e ISSAP são mapas de competência — o ISSAP tem novo outline com quatro domínios desde agosto de 2025.
- Combine frameworks pelo propósito e registre a combinação em ADR.
- Conformidade é piso, não teto: teste a efetividade, não apenas a presença dos controles.

## Referências

- NIST. *The NIST Cybersecurity Framework (CSF) 2.0*, CSWP 29. Fevereiro de 2024. <https://doi.org/10.6028/NIST.CSWP.29> — gratuito.
- NIST. *Cybersecurity Framework — FAQs* (Functions, Tiers e Profiles). <https://nist.gov/cyberframework/faqs> — gratuito.
- NIST. *Risk Management Framework* (SP 800-37 Rev. 2). <https://csrc.nist.gov/projects/risk-management> — gratuito.
- NIST. *SP 800-53 Rev. 5* (Release 5.2.0). 2025. <https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls> — gratuito.
- NIST. *SP 800-160 Vol. 1 Rev. 1*. 2022. <https://csrc.nist.gov/news/2022/guidance-on-engineering-trustworthy-secure-systems> — gratuito.
- The SABSA Institute. *W101 — Architecting a Secure Digital World*. Agosto de 2018. <https://sabsa.org/white-paper-w101-architecting-a-secure-digital-world/> — download gratuito pelo [catálogo de white papers](https://sabsa.org/white-paper-requests/) (conferido em 2026-10-23).
- The Open Group. *TOGAF Series Guide: Integrating Risk and Security within a TOGAF Enterprise Architecture*. <https://pubs.opengroup.org/togaf-standard/integrating-risk-and-security/index.html> — leitura online gratuita.
- ISC2. *CISSP Certification Exam Outline*. <https://www.isc2.org/certifications/cissp/cissp-exam-outline> — gratuito.
- ISC2. *New exam outlines for ISC2 advanced certifications*. 2025. <https://www.isc2.org/insights/2025/07/new-exam-outlines-for-isc2-advanced-certifications> — gratuito.
- CIS. *CIS Critical Security Controls v8.1 — Implementation Groups*. <https://www.cisecurity.org/controls/implementation-groups> — gratuito.

### Leituras de aprofundamento

Incluídas na revisão bibliográfica de 2026-10-23, **depois** da escrita desta aula: complementam e permitem conferir o conteúdo, mas não foram a base original do texto. A situação de cada leitura está entre parênteses.

- NIST. *CSF 2.0 Informative References* — mapeamentos oficiais para SP 800-53 Rev. 5.2.0, ISO/IEC 27001:2022, CIS Controls 8.1 e outros, com tradução para português. <https://www.nist.gov/cyberframework/csf-20-informative-references>. *(conferido.)*
- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020, Cap. 28, §28.2 *Evaluation* (p. 1018) — limites de avaliações e certificações como evidência de segurança. *(lido.)*
- SABSA Institute. *W101 — Architecting a Secure Digital World*, agosto de 2018. *(catálogo conferido; leitura pendente.)*
- SABSA. *SABSA White Paper* (W100), 2009 — Table 1 (camadas e visões, p. 9), Table 3 (matriz, p. 16) e Business Attributes Profile (pp. 19–20). *(Lido em 2026-10-23 em cópia não oficial; disponível no [catálogo de white papers](https://sabsa.org/white-paper-requests/).)*

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-27 |
| Revisão bibliográfica | 2026-10-23 — [registro da revisão retroativa](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/retroactive-review-m02.md) |
