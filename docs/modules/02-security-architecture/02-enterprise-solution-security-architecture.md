---
id: M02-L02
title: "Aula 02 — Enterprise, Solution e Security Architecture"
public_title: "Módulo 2 — Aula 02 — Enterprise, Solution e Security Architecture"
description: Diferença entre arquitetura corporativa, arquitetura de soluções e arquitetura de segurança, como se relacionam, e como a segurança aparece como preocupação transversal nos dois níveis.
domain: enterprise-architecture
tier: fundamental
status: published
prerequisites: [M02-L01]
objectives:
  - Diferenciar Enterprise Architecture, Solution Architecture e Security Architecture por escopo, horizonte e artefatos.
  - Explicar por que a segurança é uma preocupação transversal e não apenas um domínio isolado.
  - Usar os conceitos de stakeholder, concern, viewpoint e view para estruturar uma visão de segurança.
  - Decidir como tratar o conflito entre um padrão corporativo e a necessidade de uma solução específica.
minutes: 60
sources: [ISO-42010-2022, TOG-TOGAF-10, TOG-RISK-SECURITY, TOG-SABSA-2011]
further_reading: [BOOK-ANDERSON-SE3, SABSA-W117]
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
module: M02
---

# Aula 02 — Enterprise, Solution e Security Architecture { #enterprise-solution-e-security-architecture }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 2 · Nível 1</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min · ID técnico: M02-L02</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    "Arquitetura" significa coisas diferentes conforme o escopo: a estrutura de toda a organização, o desenho de uma solução ou a forma como ambos atingem seus objetivos de segurança. Esta aula separa esses três significados, mostra como eles se alimentam e explica por que a segurança precisa estar presente nos dois primeiros, em vez de existir como um terceiro documento à parte.

**Pré-requisitos:** [O papel do Security Architect](01-security-architect-role.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Diferenciar Enterprise Architecture, Solution Architecture e Security Architecture por escopo, horizonte e artefatos.
- Explicar por que a segurança é uma preocupação transversal e não apenas um domínio isolado.
- Usar os conceitos de stakeholder, concern, viewpoint e view para estruturar uma visão de segurança.
- Decidir como tratar o conflito entre um padrão corporativo e a necessidade de uma solução específica.

## Conceito

### Enterprise Architecture

**Enterprise Architecture** (arquitetura corporativa) descreve a estrutura da organização como um todo e conduz sua evolução: quais capacidades de negócio existem, quais dados as sustentam, quais aplicações as implementam e sobre qual tecnologia elas operam. O TOGAF organiza essa descrição em quatro domínios tradicionais — **Business, Data, Application e Technology** — e oferece um método iterativo para sair de uma arquitetura atual para uma arquitetura-alvo.

A Enterprise Architecture existe porque organizações grandes tomam milhares de decisões de tecnologia por ano. Sem uma referência comum, cada área otimiza para si, e o resultado é redundância (cinco sistemas de cadastro de clientes), incompatibilidade (integrações frágeis) e custo crescente. A EA resolve o problema da **coerência no nível da organização**.

### Solution Architecture

**Solution Architecture** (arquitetura de soluções) desenha uma solução específica para uma necessidade de negócio: um novo canal digital, a migração de um sistema, a integração com um parceiro. Seu horizonte é o do projeto ou produto, e seu compromisso é entregar a solução **dentro das restrições** que a EA define — princípios, padrões, tecnologias aprovadas e estado-alvo.

A arquitetura de soluções resolve o problema de **transformar uma necessidade em algo construível**, com escolhas técnicas justificadas.

### Security Architecture

**Security Architecture** trata de como a organização e suas soluções atingem os objetivos de segurança. Ela existe nos dois níveis anteriores:

- **Enterprise Security Architecture:** princípios, padrões, capacidades e serviços de segurança que valem para toda a organização — por exemplo, "toda identidade humana é autenticada por um provedor central com autenticação multifator".
- **Solution Security Architecture:** requisitos, ameaças, controles e decisões de uma solução específica — por exemplo, como a API de parceiros da Aurora Pagamentos autentica e autoriza cada chamada.

### Por que a segurança é transversal

A segurança não é um quinto domínio ao lado de negócio, dados, aplicações e tecnologia: ela **atravessa os quatro**. Há requisitos de segurança no processo de negócio (segregação de funções na aprovação de pagamentos), nos dados (classificação e retenção), nas aplicações (autorização) e na tecnologia (segmentação de rede, criptografia).

O guia da The Open Group sobre integração de risco e segurança ao TOGAF segue essa linha: em vez de uma lista de controles, propõe que a arquitetura corporativa incorpore **serviços de segurança** organizados em um catálogo, conectando a gestão de segurança da informação à gestão de riscos corporativos. Em 2011, a The Open Group e o SABSA Institute já haviam publicado um white paper de integração com a mesma premissa: a arquitetura de segurança deve fazer parte da arquitetura corporativa, e não ser uma disciplina paralela.

### Qual problema essa distinção resolve

Sem separar os níveis, dois erros opostos são comuns:

1. **Discutir padrão corporativo dentro de um projeto.** Cada projeto renegocia como fazer autenticação, logging ou criptografia — e o resultado depende de quem estava na reunião.
2. **Impor detalhe de solução como padrão corporativo.** Uma decisão tomada para um sistema específico vira regra para todos, mesmo onde não faz sentido.

Saber em que nível uma decisão pertence é o primeiro passo para tomá-la no fórum certo.

## Fundamentos técnicos

### Comparação dos três escopos

| Dimensão | Enterprise Architecture | Solution Architecture | Security Architecture |
|:---|:---|:---|:---|
| **Escopo** | Toda a organização | Uma iniciativa, produto ou sistema | Transversal: organização e soluções |
| **Horizonte** | 1 a 5 anos | Duração do projeto e ciclo de vida do produto | Ambos |
| **Pergunta central** | *Como a organização deve se estruturar para cumprir sua estratégia?* | *Como construir esta solução atendendo à necessidade e às restrições?* | *Como atingir os objetivos de segurança com risco aceitável?* |
| **Stakeholders** | Diretoria, donos de capacidades, arquitetos de domínio | Produto, engenharia, operação | CISO, risco, donos de ativos, engenharia |
| **Artefatos** | Princípios, mapas de capacidades, estado-alvo, roadmaps | Documento de arquitetura da solução, diagramas, decisões | Princípios e padrões de segurança, catálogo de serviços, threat models, ADRs |
| **Tipo de decisão** | Padrão e direção | Escolha específica | Requisito, controle e aceitação de risco |
| **Fórum** | Comitê ou conselho de arquitetura | Equipe do projeto e design review | Ambos, com dono de risco nas aceitações |

### Níveis intermediários

Entre a organização e a solução costumam existir níveis intermediários:

- **Segmento ou domínio:** arquitetura de uma área de negócio (pagamentos, logística) ou de um domínio técnico (identidade, dados).
- **Plataforma:** arquitetura de um serviço compartilhado usado por muitas soluções — uma landing zone em cloud, uma plataforma de integração, um provedor de identidade central.

Plataformas merecem atenção especial em segurança: um controle implementado na plataforma beneficia todas as soluções que a usam, e uma falha na plataforma afeta todas elas.

### Stakeholders, concerns, viewpoints e views

A ISO/IEC/IEEE 42010 oferece um vocabulário útil para organizar descrições de arquitetura:

| Conceito | Significado | Exemplo em segurança |
|:---|:---|:---|
| **Stakeholder** | Pessoa ou grupo com interesse no sistema | Dono do produto, CISO, auditor, equipe de operação |
| **Concern** (preocupação) | Interesse de um stakeholder em relação ao sistema | "Quem pode aprovar um estorno?" · "Os dados de cartão saem do ambiente PCI?" |
| **Viewpoint** | Convenções para construir um tipo de visão: que preocupações trata, que modelos e notações usa | Viewpoint de segurança: fronteiras de confiança, fluxos de dados, controles por camada |
| **View** | A representação concreta do sistema segundo um viewpoint | O diagrama de fluxos com trust boundaries da API de parceiros |

O valor prático desse vocabulário é forçar a pergunta: **para quem é este diagrama e que pergunta ele responde?** Um diagrama de infraestrutura não responde se dados de cartão cruzam uma fronteira de confiança; uma visão de segurança precisa ser construída para isso.

### Como os níveis se alimentam

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l02-scopes.mmd"
```

<figcaption>Figura 1 — Escopos de arquitetura e o papel transversal da segurança.</figcaption>
</figure>

O fluxo é bidirecional. A EA define princípios e estado-alvo; as soluções os aplicam e, quando não conseguem, geram **exceções** que devolvem informação à EA. Muitas exceções sobre o mesmo padrão indicam que o padrão precisa mudar — ver [Princípios, padrões, baselines e exceções](04-principles-standards-baselines-exceptions.md).

### Serviços de segurança como linguagem comum

Uma forma eficaz de conectar os níveis é descrever a segurança como **serviços** que as soluções consomem, em vez de controles que cada solução implementa por conta própria:

| Serviço de segurança | O que oferece às soluções |
|:---|:---|
| Autenticação | Verificação de identidade de pessoas e workloads por meio de um provedor central |
| Autorização | Decisões de acesso baseadas em políticas |
| Gestão de segredos e chaves | Armazenamento, rotação e auditoria de credenciais e chaves criptográficas |
| Registro e monitoramento | Coleta, retenção e correlação de eventos de segurança |
| Proteção de borda | Inspeção e filtragem do tráfego de entrada |
| Gestão de vulnerabilidades | Descoberta, priorização e acompanhamento de correções |

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l02-security-layers.mmd"
```

<figcaption>Figura 2 — A governança de segurança orienta as camadas da arquitetura (negócio, dados, aplicações e tecnologia) e o catálogo de serviços de segurança transversais que essas camadas consomem.</figcaption>
</figure>

Quando a EA mantém esse catálogo, a arquitetura de uma solução deixa de perguntar "como vamos fazer autenticação?" e passa a perguntar "qual serviço de autenticação usamos e que requisito específico ele não atende?". É uma mudança que reduz custo e inconsistência.

## Exemplo empresarial

!!! example "Grupo Horizonte — sistema de gestão de armazéns em SaaS"

    O Grupo Horizonte tem quatro subsidiárias. A arquitetura corporativa definiu, há dois anos, o princípio "identidade única no grupo": todos os funcionários se autenticam por um provedor de identidade central, com autenticação multifator e federação para aplicações SaaS.

    A subsidiária de logística contrata um sistema de gestão de armazéns (WMS) em SaaS. Na arquitetura da solução, três perguntas aparecem, cada uma em um nível diferente:

    | Pergunta | Nível | Quem decide |
    |:---|:---|:---|
    | Os operadores de armazém autenticam pelo provedor central? | Corporativo (princípio já decidido) | Ninguém precisa decidir de novo: aplica-se o padrão. |
    | Como o WMS integra com o ERP da logística? | Solução | Arquiteto de soluções da logística, com requisitos de segurança. |
    | Operadores temporários, contratados por agência, devem ter identidade no provedor central? | Corporativo — o padrão não previa esse caso | Fórum de arquitetura corporativa, com proposta do arquiteto de segurança. |

    A terceira pergunta parecia um detalhe de projeto, mas a resposta valeria para todas as subsidiárias. Levá-la ao fórum certo evitou que a logística criasse contas locais no WMS — uma exceção que, repetida em outras subsidiárias, teria quebrado o princípio de identidade única.

## Arquitetura tradicional versus recomendada

| Aspecto | Segurança como silo | Segurança integrada às arquiteturas |
|:---|:---|:---|
| Documentação | Um "documento de segurança" separado, escrito depois do desenho | Uma visão de segurança dentro da descrição de arquitetura da solução |
| Padrões | Lista de controles que cada projeto interpreta | Catálogo de serviços de segurança que os projetos consomem |
| Decisões | Tomadas no projeto, mesmo quando têm alcance corporativo | Encaminhadas ao fórum do nível correto |
| Exceções | Informais, por e-mail | Registradas e usadas para revisar padrões |
| Relação com a EA | Paralela | Parte da EA, com princípios e estado-alvo de segurança |

## Controles e padrões relevantes

| Elemento | Objetivo | Referência |
|:---|:---|:---|
| Princípios de segurança dentro dos princípios de arquitetura corporativa | Garantir que decisões de estrutura considerem segurança | TOGAF; guia *Integrating Risk and Security* |
| Catálogo de serviços de segurança | Reutilizar capacidades e reduzir inconsistência | Guia *Integrating Risk and Security* |
| Viewpoint de segurança na descrição de arquitetura | Responder às preocupações de segurança dos stakeholders | ISO/IEC/IEEE 42010:2022 |
| Fórum de arquitetura com papel de segurança | Decidir no nível certo | Detalhado em Módulo 16 — Aula 06 |
| Revisão de conformidade das soluções com a EA | Detectar desvios cedo | Prática de governança de arquitetura |

## Aplicabilidade: on-premises, cloud e híbrido

| Aspecto | On-premises | Cloud | Híbrido |
|:---|:---|:---|:---|
| Onde a EA se materializa | Padrões de infraestrutura, catálogo de tecnologias aprovadas | **Plataformas** (landing zones, contas e assinaturas, pipelines) mantidas por um time central | Arquitetura de integração: conectividade, identidade, DNS e observabilidade entre ambientes |
| Papel da arquitetura de soluções | Escolher servidores, rede e software dentro do catálogo | Compor serviços gerenciados dentro dos guardrails da plataforma | Decidir onde cada componente roda e como atravessa ambientes |
| Serviço de segurança típico | Firewalls e diretório corporativo | Políticas de organização, serviços nativos de detecção, gestão de chaves gerenciada | Provedor de identidade federado e SIEM que recebe dados de todos os ambientes |
| Risco característico | Padrões que ninguém revisita | Equipes criando plataformas paralelas fora do padrão | Dois padrões diferentes para o mesmo serviço, um por ambiente |
| Responsabilidade | Organização | Compartilhada com o provedor | Compartilhada e distribuída entre equipes de plataforma |

**Particularidade do híbrido:** em ambientes híbridos, a arquitetura de integração **é** arquitetura corporativa. A forma como o datacenter se conecta à cloud, como as identidades fluem e onde os logs convergem afeta todas as soluções. Tratar essas decisões projeto a projeto produz múltiplos túneis, múltiplas sincronizações de identidade e nenhuma visão consolidada.

## Como especificar e implementar

### Estrutura de uma visão de segurança na arquitetura de solução

Toda descrição de arquitetura de solução com gatilho de risco deve conter uma visão de segurança com, no mínimo:

1. **Contexto e classificação:** objetivo da solução, dados tratados e sua classificação, obrigações regulatórias.
2. **Stakeholders e preocupações de segurança:** quem precisa de que garantias.
3. **Diagrama de fluxos com trust boundaries:** componentes, fluxos de dados, protocolos e fronteiras de confiança.
4. **Serviços de segurança consumidos:** quais serviços do catálogo corporativo a solução usa.
5. **Requisitos de segurança:** derivados do negócio e das ameaças — ver [Aula 07](07-business-driven-requirements.md).
6. **Ameaças principais e controles:** resumo do threat model.
7. **Decisões e desvios:** ADRs e exceções a padrões corporativos.
8. **Riscos residuais:** o que permanece e quem aceitou.

### Regra para decidir o nível de uma decisão

Uma decisão pertence ao **nível corporativo** quando pelo menos uma das condições é verdadeira:

- A mesma pergunta vai aparecer em outras soluções.
- A decisão cria ou altera um serviço compartilhado.
- A decisão contraria um princípio ou padrão existente.
- O risco envolvido excede o que o dono da solução pode aceitar.

Caso contrário, ela pertence à solução e deve ser registrada no ADR do projeto.

## Trade-offs, limitações e antipadrões

| Escolha | Benefício | Custo ou risco |
|:---|:---|:---|
| Equipe de arquitetura de segurança separada da EA | Profundidade técnica, foco | Risco de silo e de padrões desconectados da estrutura corporativa |
| Arquitetos de segurança dentro da equipe de EA | Integração natural | Risco de a segurança perder voz diante de outras prioridades |
| Padrões corporativos detalhados | Previsibilidade, auditoria fácil | Rigidez; mais exceções |
| Padrões corporativos mínimos | Autonomia das equipes | Inconsistência entre soluções |

**Antipadrões:**

- **EA de papel:** arquitetura corporativa que produz mapas, mas não influencia decisões de projeto.
- **Cada projeto é uma ilha:** soluções que nunca consultam o catálogo de serviços e reinventam autenticação, logging e gestão de segredos.
- **Padrão corporativo nascido de um projeto:** uma decisão local promovida a regra sem análise de aplicabilidade.

## Como validar

- **Rastreabilidade:** cada decisão relevante da solução aponta para um princípio, padrão ou exceção corporativa.
- **Reuso:** percentual de soluções que consomem os serviços do catálogo em vez de implementar os próprios.
- **Exceções por padrão:** muitas exceções ao mesmo padrão indicam que ele está desatualizado ou mal desenhado.
- **Revisão de conformidade:** amostragem periódica de soluções em produção, comparando o desenho aprovado com o ambiente real.

## Como apresentar e justificar

- **Para a diretoria:** "Hoje cada subsidiária resolve autenticação de forma diferente. Um serviço central reduz custo de licenças, acelera a integração de novas aquisições e permite revogar o acesso de um funcionário em todas as empresas de uma só vez."
- **Para arquitetos de soluções:** "Vocês deixam de projetar autenticação, logging e gestão de segredos a cada projeto. Usem o catálogo e tragam ao fórum apenas o que ele não atende."
- **Para engenharia:** "O padrão vem com implementação de referência e módulos prontos. Desviar continua possível, com uma exceção registrada."

## Checklist de revisão arquitetural

- [ ] A descrição da solução contém uma visão de segurança com trust boundaries.
- [ ] Os serviços de segurança corporativos consumidos estão identificados.
- [ ] Decisões com alcance corporativo foram encaminhadas ao fórum de arquitetura.
- [ ] Desvios de padrões corporativos estão registrados como exceções.
- [ ] Cada preocupação de segurança dos stakeholders tem uma visão ou um requisito que a responde.
- [ ] Em soluções híbridas, a integração usa a arquitetura de integração corporativa, e não um mecanismo próprio.

## Questões de compreensão

**1.** Por que a segurança não deve ser tratada como um quinto domínio, ao lado de negócio, dados, aplicações e tecnologia?

??? success "Resposta comentada"

    Porque há requisitos de segurança em todos os quatro domínios: segregação de funções nos processos de negócio, classificação nos dados, autorização nas aplicações e segmentação na tecnologia. Tratá-la como domínio separado tende a produzir documentos paralelos, escritos depois do desenho, em vez de requisitos e serviços incorporados a cada domínio.

**2.** Uma equipe de projeto decide que seu sistema usará um cofre de segredos diferente do adotado pela organização, porque "é mais simples de integrar". Em que nível essa decisão deveria ser tomada, e por quê?

??? success "Resposta comentada"

    No nível corporativo, ou ao menos registrada como **exceção** a ele, porque contraria um padrão existente e cria um serviço paralelo que precisará de operação, auditoria e resposta a incidentes próprias. A equipe pode propor a exceção com justificativa e controles compensatórios; se a dificuldade de integração se repetir em outros projetos, o fórum deve rever o padrão.

**3.** Explique a diferença entre *viewpoint* e *view* com um exemplo de segurança.

??? success "Resposta comentada"

    O **viewpoint** é a convenção — que preocupações uma visão trata e como representá-las (por exemplo, "visão de fluxos de dados com trust boundaries, classificação dos dados e controles em cada travessia"). A **view** é a aplicação dessa convenção a um sistema concreto (o diagrama da API de parceiros da Aurora segundo esse viewpoint).

**4.** Em um ambiente híbrido, por que a arquitetura de integração deve ser tratada como arquitetura corporativa?

??? success "Resposta comentada"

    Porque conectividade, identidade, DNS e observabilidade entre ambientes são usadas por todas as soluções. Decidi-las projeto a projeto multiplica túneis, sincronizações e pontos de confiança sem visão consolidada — aumentando a superfície de ataque e dificultando a resposta a incidentes.

## Exercício de tomada de decisão

!!! question "Cenário: a subsidiária quer seu próprio provedor de identidade"

    A subsidiária de saúde ocupacional do Grupo Horizonte vai lançar um portal para que empresas clientes acessem laudos de seus funcionários. O padrão corporativo define o provedor de identidade central do grupo apenas para **funcionários**. Para clientes externos, não há padrão. A subsidiária propõe usar o provedor de identidade embutido na plataforma do portal, que já suporta autenticação multifator.

    Alternativas:

    - **A — Usar o provedor embutido**, decisão local da solução.
    - **B — Exigir o provedor central** do grupo também para clientes externos.
    - **C — Levar a questão ao fórum corporativo** e definir um padrão de identidade para clientes (CIAM) válido para todas as subsidiárias; até lá, usar o provedor embutido como exceção temporária com requisitos mínimos.

    Avalie as alternativas pelos critérios: adequação ao risco (dados de saúde), consistência no grupo, prazo do projeto e custo. Recomende uma alternativa.

??? success "Resolução de referência"

    | Critério | Peso | A — Embutido | B — Central | C — Padrão CIAM + exceção |
    |:---|:---|:---|:---|:---|
    | Adequação ao risco (dados sensíveis de saúde) | 3 | 2 | 2 | 3 |
    | Consistência no grupo | 2 | 1 | 2 | 3 |
    | Prazo do projeto | 2 | 3 | 1 | 2 |
    | Custo | 1 | 3 | 2 | 2 |
    | **Total ponderado** | | **17** | **14** | **21** |

    **Recomendação: C.** A pergunta "como autenticamos clientes externos?" vai se repetir nas outras subsidiárias — é uma decisão corporativa. Usar o provedor central de funcionários para clientes (B) mistura populações com ciclos de vida, volumes e requisitos de privacidade diferentes, o que costuma ser desaconselhável. A exceção temporária preserva o prazo, desde que tenha requisitos mínimos: autenticação multifator, logs exportados para o SIEM do grupo e um plano de migração para o padrão definido.

    **Risco residual:** a exceção temporária se tornar permanente. Mitigação: prazo explícito, responsável nomeado e revisão no fórum de arquitetura.

    O conceito de CIAM (Customer Identity and Access Management) é aprofundado no Módulo 6.

## Pontos-chave

- Enterprise Architecture busca coerência na organização; Solution Architecture transforma uma necessidade em algo construível; Security Architecture atravessa as duas.
- A segurança é transversal aos domínios de negócio, dados, aplicações e tecnologia.
- Stakeholders, concerns, viewpoints e views ajudam a construir visões de segurança que respondem a perguntas reais.
- Um catálogo de serviços de segurança é a ponte mais eficaz entre o nível corporativo e as soluções.
- Decidir no nível certo evita tanto renegociar padrões em cada projeto quanto promover detalhes locais a regra corporativa.

## Referências

- ISO/IEC/IEEE. *42010:2022 — Software, systems and enterprise — Architecture description*. 2022. <https://committee.iso.org/standard/74393.html> — norma paga, não consultada na íntegra; a descrição usada nesta aula se apoia na página oficial da norma e em resumos públicos.
- The Open Group. *TOGAF Standard, 10th Edition* (anúncio de lançamento). 2022. <https://www.opengroup.org/open-group-announces-launch-togaf-standard-10th-edition> — acesso ao padrão completo não confirmado.
- The Open Group. *TOGAF Series Guide: Integrating Risk and Security within a TOGAF Enterprise Architecture*. <https://pubs.opengroup.org/togaf-standard/integrating-risk-and-security/index.html> — leitura online gratuita.
- The Open Group e The SABSA Institute. *TOGAF and SABSA Integration* (comunicado). 2011. <https://www.opengroup.org/open-group-issues-guide-integrating-togaf%C2%AE-sabsa%C2%AE-secure-architecture-methodology> — acesso ao white paper não confirmado.

### Leituras de aprofundamento

Incluídas na revisão bibliográfica de 2026-10-23, **depois** da escrita desta aula: complementam e permitem conferir o conteúdo, mas não foram a base original do texto. A situação de cada leitura está entre parênteses.

- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020, Cap. 8, §8.6 *The economics of security and dependability* (p. 293) — por que incentivos desalinhados derrubam controles bem desenhados. *(lido.)*
- SABSA Institute. *SABSA–TOGAF Integration White Paper*, outubro de 2011, e *Integrating Risk and Security within a TOGAF Enterprise Architecture* (G152), janeiro de 2016 — <https://sabsa.org/white-paper-requests/>. *(catálogo conferido; leitura pendente.)*

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
| Revisão bibliográfica | 2026-10-23 — [registro da revisão retroativa](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/retroactive-review-m02.md) |
