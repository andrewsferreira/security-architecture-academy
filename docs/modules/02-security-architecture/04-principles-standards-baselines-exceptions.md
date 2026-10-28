---
id: M02-L04
title: "Aula 04 — Princípios, padrões, baselines e exceções"
public_title: "Módulo 2 — Aula 04 — Princípios, padrões, baselines e exceções"
description: A hierarquia que liga a intenção da direção à configuração no ambiente — política, princípios, padrões, baselines e controles — e como gerenciar exceções sem perder o controle do risco.
domain: grc
tier: professional
status: published
prerequisites: [M02-L03, M01-L02, M01-L06]
objectives:
  - Diferenciar política, princípio, padrão, baseline, diretriz, procedimento e controle.
  - Escrever princípios e padrões de segurança verificáveis.
  - Desenhar um processo de exceções com controles compensatórios, prazo e responsável.
  - Distinguir segurança necessária de complexidade desnecessária ao definir padrões.
minutes: 75
sources: [NIST-SP800-53, CIS-CONTROLS-V8-1, AWS-WA-SECURITY-DESIGN, GCP-WAF-SECURITY]
further_reading: [NIST-SP800-160-V1R1, BOOK-ANDERSON-SE3, SABSA-W105, TOG-TOGAF9-PRINCIPLES]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M02
---

# Aula 04 — Princípios, padrões, baselines e exceções { #principios-padroes-baselines-e-excecoes }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 2 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M02-L04</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Entre a frase "protegemos os dados dos clientes" e a configuração de um servidor existe uma cadeia de documentos e decisões. Quando essa cadeia está bem construída, cada configuração pode ser explicada e cada desvio é consciente. Quando está quebrada, há políticas que ninguém aplica, padrões que ninguém consegue cumprir e exceções que ninguém lembra de encerrar. Esta aula ensina a construir a cadeia e a gerenciar seus desvios.

**Pré-requisitos:** [Arquitetura conceitual, lógica e física](03-conceptual-logical-physical.md), princípios de design seguro (Módulo 1 — Aula 02) e tipos de controle (Módulo 1 — Aula 06).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Diferenciar política, princípio, padrão, baseline, diretriz, procedimento e controle.
- Escrever princípios e padrões de segurança verificáveis.
- Desenhar um processo de exceções com controles compensatórios, prazo e responsável.
- Distinguir segurança necessária de complexidade desnecessária ao definir padrões.

## Conceito

### A hierarquia

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l04-hierarchy.mmd"
```

<figcaption>Figura 1 — Hierarquia de documentos e controles de segurança.</figcaption>
</figure>

| Elemento | O que é | Obrigatório? | Quem aprova | Exemplo |
|:---|:---|:---|:---|:---|
| **Política** | Declaração de intenção e de responsabilidades da direção | Sim | Diretoria ou conselho | "Dados de clientes são protegidos conforme sua classificação e as obrigações legais." |
| **Princípio** | Regra orientadora para decisões de arquitetura, com justificativa e implicações | Orienta; desvios exigem justificativa | Fórum de arquitetura | "Negar por padrão: nenhum acesso é concedido sem autorização explícita." |
| **Padrão** | Requisito específico, mensurável e obrigatório | Sim | Fórum de arquitetura ou CISO | "Comunicação entre serviços internos usa TLS 1.2 ou superior com autenticação mútua." |
| **Baseline** | Conjunto mínimo de configurações para uma tecnologia ou plataforma | Sim | Dono da plataforma com a segurança | "Servidores Linux seguem o benchmark CIS nível 1, com os desvios listados no anexo." |
| **Diretriz** | Recomendação; orienta quando não há padrão | Não | Segurança | "Prefira serviços gerenciados de gestão de segredos a soluções próprias." |
| **Procedimento** | Passo a passo para executar uma tarefa | Sim, para quem executa | Dono do processo | "Como rotacionar o certificado do gateway de APIs." |
| **Controle** | Mecanismo que modifica o risco no ambiente | — | — | A regra de firewall, a política de IAM, o alerta no SIEM |

### Por que a hierarquia existe

Cada nível muda em um ritmo e é lido por um público diferente. A política dura anos e é lida pela diretoria e pelos auditores; o padrão muda quando a tecnologia muda e é lido por arquitetos; a baseline muda a cada versão de sistema operacional e é lida — ou executada — por engenheiros e ferramentas. Misturar níveis cria documentos que envelhecem rápido demais para a diretoria aprovar e devagar demais para a engenharia usar.

### Qual problema resolve

A hierarquia resolve o problema da **rastreabilidade e da aplicabilidade**:

- **Rastreabilidade:** cada configuração pode ser explicada até a intenção da direção. Isso importa em auditorias, em incidentes e quando alguém pergunta "posso desligar isso?".
- **Aplicabilidade:** cada regra está no nível em que pode ser cumprida e verificada. "Proteja os dados" não é verificável; "dados confidenciais em repouso são criptografados com chaves gerenciadas pelo serviço central de chaves" é.

### Princípios × padrões × controles

Esta é a aula principal do currículo para essa distinção:

- Um **princípio** orienta uma escolha quando há mais de um caminho possível. Ele raramente é verificado diretamente — verifica-se se as decisões o respeitam.
- Um **padrão** é verificável: um sistema está ou não está conforme.
- Um **controle** é o mecanismo concreto, no ambiente, que torna o padrão verdadeiro.

O mesmo princípio gera vários padrões, e o mesmo padrão é realizado por controles diferentes em ambientes diferentes.

### Segurança necessária × complexidade desnecessária

Padrões têm custo: cada requisito obrigatório consome tempo de engenharia, gera exceções e precisa ser verificado. Um padrão é **necessário** quando trata um risco relevante, de forma proporcional, e não há maneira mais simples de obter o mesmo efeito. Ele vira **complexidade desnecessária** quando:

- trata um risco que já está mitigado por outro controle de forma suficiente;
- exige o mesmo rigor para ativos de valor muito diferente;
- especifica *como* fazer quando bastaria especificar *o que* atingir;
- ninguém consegue cumpri-lo, e a organização vive de exceções.

Um sinal confiável de complexidade desnecessária é a **taxa de exceções**: se a maioria das soluções precisa de exceção a um padrão, o problema provavelmente está no padrão.

## Fundamentos técnicos

### Como escrever um bom princípio

Um formato consagrado em arquitetura corporativa — o da documentação de princípios do TOGAF — descreve cada princípio com **nome, declaração, justificativa e implicações** (*Name, Statement, Rationale, Implications*). Segundo essa documentação, a justificativa deve destacar os benefícios para o negócio, em termos de negócio, e as implicações devem destacar os requisitos, para o negócio e para TI, de cumprir o princípio. As implicações são a parte mais importante, porque transformam a frase em consequências práticas. O mesmo texto propõe critérios para um bom conjunto de princípios: compreensível, robusto, completo, consistente e estável.

!!! example "Princípio — Identidade como fronteira primária"

    **Declaração:** decisões de acesso são baseadas na identidade verificada do solicitante e no contexto da requisição, e não apenas na sua localização de rede.

    **Justificativa:** usuários, parceiros e workloads estão distribuídos entre datacenter, cloud e internet; a localização de rede deixou de indicar confiança.

    **Implicações:**

    - Serviços expostos a qualquer rede exigem autenticação, mesmo dentro da rede corporativa.
    - Workloads possuem identidades próprias; segredos estáticos compartilhados são evitados.
    - A segmentação de rede continua necessária como camada adicional, não como controle único.

### Como escrever um bom padrão

Um padrão precisa ser **verificável, delimitado e mantido**:

| Atributo | Pergunta | Exemplo |
|:---|:---|:---|
| Identificador e versão | Qual padrão, em qual versão? | `SEC-STD-007 v2.1` |
| Escopo | A quais sistemas se aplica? | "Todos os serviços que trocam dados classificados como confidenciais." |
| Requisito | O que precisa ser verdade? | "Usam TLS 1.2 ou superior com autenticação mútua por certificado emitido pela PKI interna." |
| Verificação | Como se comprova? | "Varredura trimestral de endpoints internos; configuração do service mesh." |
| Princípio de origem | Por que existe? | "Identidade como fronteira primária." |
| Dono e vigência | Quem mantém e desde quando vale? | "Arquitetura de segurança; vigente desde 01/03." |
| Exceções | Como solicitar desvio? | Link para o processo de exceções. |

Compare com um requisito mal escrito: "Use criptografia forte". Ele não diz onde, com que algoritmo, nem como verificar — e por isso não pode ser cumprido nem auditado.

### Baselines

Uma baseline é o conjunto mínimo de configurações seguras para uma tecnologia. Raramente se escreve uma baseline do zero: o ponto de partida costuma ser uma referência pública — como os **CIS Benchmarks** ou as recomendações dos provedores de cloud — seguida de um registro dos **desvios justificados** para a realidade da organização.

Boas práticas para baselines:

- **Escolher o nível de rigor pelo risco.** Aplicar o perfil mais restritivo de um benchmark a todos os servidores costuma quebrar aplicações; o perfil deve corresponder à criticidade.
- **Documentar desvios da referência.** "Item 5.2.3 do benchmark desativado porque o agente de backup exige acesso X; compensado por Y."
- **Implementar como código.** Baselines aplicadas por ferramentas de configuração ou políticas de cloud são verificáveis continuamente; baselines em PDF não.

### Controles e suas funções

Controles são classificados pela função que exercem sobre o risco (detalhado em Módulo 1 — Aula 06):

| Função | Objetivo | Exemplo |
|:---|:---|:---|
| Preventivo | Impedir que o evento ocorra | MFA, negação por padrão no firewall |
| Detectivo | Identificar que o evento ocorreu | Alerta de login impossível no SIEM |
| Corretivo | Limitar o dano e restaurar | Revogação automática de sessão, restauração de backup |
| **Compensatório** | Substituir, total ou parcialmente, um controle que não pode ser aplicado | Segmentação reforçada para um sistema que não suporta criptografia |

Controles compensatórios são o elo entre padrões e exceções: quase toda exceção bem aprovada vem acompanhada de um.

### Exceções

Uma exceção é um **desvio aprovado, temporário e monitorado** de um padrão ou baseline. Ela existe porque nenhum padrão prevê todas as situações reais — sistemas legados, restrições de fornecedores, prazos de negócio — e porque é melhor um desvio consciente e controlado do que um desvio silencioso.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l04-exception-flow.mmd"
```

<figcaption>Figura 2 — Ciclo de vida de uma exceção.</figcaption>
</figure>

Uma solicitação de exceção completa contém:

1. **Padrão ou baseline afetado** e o requisito específico.
2. **Motivo** do desvio e por que a conformidade não é viável agora.
3. **Risco** resultante, com probabilidade e impacto.
4. **Controles compensatórios** e como serão verificados.
5. **Prazo** de validade e plano de correção.
6. **Responsável** pelo risco, com autoridade compatível com seu nível.

A autoridade para aprovar deve crescer com o risco: um risco baixo pode ser aceito pelo dono do sistema; um risco alto, apenas pela diretoria responsável pelo negócio afetado. **O arquiteto recomenda; quem aceita o risco é quem responde pelo negócio.**

## Exemplo empresarial

!!! example "Aurora Pagamentos — o sistema de conciliação que não fala mTLS"

    A Aurora adotou o padrão `SEC-STD-007`: comunicação entre serviços internos com dados confidenciais usa TLS com autenticação mútua (mTLS). O sistema de conciliação bancária, um produto de fornecedor instalado há oito anos, troca arquivos com o serviço de liquidação por um protocolo sem suporte a mTLS. O fornecedor promete uma versão compatível em nove meses.

    **Solicitação de exceção:**

    | Campo | Conteúdo |
    |:---|:---|
    | Padrão afetado | `SEC-STD-007 v2.1` — mTLS entre serviços com dados confidenciais |
    | Motivo | Produto do fornecedor não suporta mTLS na versão atual |
    | Risco | Interceptação ou falsificação de arquivos de conciliação por um atacante já presente na rede interna. Probabilidade baixa; impacto alto (fraude em liquidação). **Risco: médio.** |
    | Compensatórios | (1) Os dois servidores em um segmento dedicado, com firewall permitindo apenas o fluxo entre eles; (2) verificação de integridade por hash assinado de cada arquivo, já suportada pelo produto; (3) alerta no SIEM para qualquer conexão ao segmento originada de outro endereço. |
    | Prazo | Nove meses, alinhado à versão do fornecedor; revisão no sexto mês |
    | Responsável | Diretora de Operações Financeiras |

    Repare que o controle compensatório (2) trata **exatamente** o risco que o mTLS trataria — a integridade e a autenticidade dos arquivos — por outro caminho. Compensatórios que apenas "adicionam segurança genérica" não compensam nada.

## Arquitetura tradicional versus recomendada

| Aspecto | Tradicional | Recomendado |
|:---|:---|:---|
| Políticas | Documento extenso que mistura intenção, padrões e procedimentos | Política curta; padrões e baselines separados e versionados |
| Padrões | "Use criptografia forte" | Requisito verificável, com escopo, verificação e dono |
| Baselines | Referência pública aplicada integralmente, ou nenhuma | Referência escolhida pelo risco, com desvios documentados e aplicação como código |
| Exceções | Aprovadas por e-mail, sem prazo | Processo formal, compensatórios verificáveis, prazo e dono do risco |
| Evolução | Padrões revistos quando há auditoria | Exceções recorrentes disparam revisão do padrão |

## Controles e padrões relevantes

| Elemento | Objetivo | Referência |
|:---|:---|:---|
| Baseline de configuração | Garantir configuração mínima segura e conhecida | NIST SP 800-53 Rev. 5: CM-2 (Baseline Configuration), CM-6 (Configuration Settings) |
| Configuração segura de ativos | Estabelecer e manter configurações seguras | CIS Controls v8.1: Controle 4 |
| Políticas e procedimentos por família de controles | Garantir que cada família tenha política e procedimento | NIST SP 800-53 Rev. 5: controles "-1" de cada família (por exemplo, AC-1) |
| Aceitação formal de risco | Exceções aceitas por autoridade adequada | Detalhado no Módulo 3 (risk register e tratamento de riscos) |
| Automação de boas práticas | Padrões aplicados e verificados continuamente | AWS Well-Architected, princípio *Automate security best practices* |
| Segurança por design | Princípios incorporados desde o desenho | Google Cloud Well-Architected, princípio *Implement security by design* |

## Aplicabilidade: on-premises, cloud e híbrido

O padrão é o mesmo; o **ponto de aplicação** e a **forma de verificação** mudam.

| Aspecto | On-premises | Cloud | Híbrido |
|:---|:---|:---|:---|
| Como a baseline é aplicada | Ferramentas de gestão de configuração, GPOs, imagens padronizadas | Políticas de organização (por exemplo, SCPs na AWS, Azure Policy, Organization Policy no Google Cloud) e imagens padronizadas | Ambos — idealmente com a mesma fonte de verdade para a baseline |
| Como a conformidade é verificada | Varreduras periódicas | Avaliação contínua por serviços de postura | Ferramenta que cubra os dois ambientes, ou extensão do plano de controle da cloud a servidores locais (por exemplo, Azure Arc) |
| Velocidade de deriva | Lenta, mas pouco visível | Rápida, mas detectável | Desigual: a cloud é corrigida em horas, o datacenter em semanas |
| Exceções típicas | Sistemas legados sem suporte | Serviços que não suportam um controle exigido | Integrações que não conseguem cumprir o padrão dos dois lados |
| Responsabilidade | Organização | Compartilhada — parte das configurações é do provedor | Fragmentada entre equipes; risco de padrões divergentes por ambiente |

**Particularidade do híbrido:** é comum que a mesma organização tenha dois padrões para o mesmo tema — um escrito para o datacenter, outro para a cloud — que evoluíram separadamente. A recomendação é ter **um padrão por tema**, com seções de implementação por ambiente, e não um padrão por ambiente.

## Como especificar e implementar

1. **Comece por poucos princípios.** Entre cinco e doze princípios de segurança costumam bastar para orientar decisões; listas longas viram decoração.
2. **Derive padrões dos princípios e dos riscos.** Cada padrão aponta seu princípio de origem e o risco que trata.
3. **Escolha referências para baselines.** Use referências públicas e registre os desvios.
4. **Implemente como código** sempre que possível: políticas de cloud, perfis de configuração, regras de verificação.
5. **Publique o processo de exceções** junto com os padrões — padrão sem caminho de exceção gera desvio silencioso.
6. **Meça e revise:** acompanhe conformidade, exceções por padrão e exceções vencidas.

## Trade-offs, limitações e antipadrões

| Antipadrão | Problema | Correção |
|:---|:---|:---|
| Política-enciclopédia | Mistura intenção, padrões e procedimentos; ninguém lê | Separar níveis e versionar padrões |
| Princípios-slogan | "Segurança em primeiro lugar" não orienta nenhuma decisão | Declaração + justificativa + implicações |
| Padrão inverificável | Não é possível dizer se um sistema está conforme | Requisito mensurável e método de verificação |
| Benchmark aplicado sem análise | Aplicações quebram; equipes desativam a baseline inteira | Perfil adequado ao risco e desvios documentados |
| Exceção eterna | Desvio temporário vira permanente sem nova análise | Prazo, renovação com reanálise e indicador de exceções vencidas |
| Compensatório genérico | "Monitoramento reforçado" sem relação com o risco | Compensatório que trate o mesmo risco do controle ausente |
| Exceção aprovada pelo arquiteto | Quem não responde pelo negócio aceita o risco | Aprovação pelo dono do risco, com recomendação do arquiteto |

## Como validar

| Indicador | Meta típica | O que revela |
|:---|:---|:---|
| Conformidade com baselines por plataforma | Definida pelo risco da plataforma | Efetividade da aplicação |
| Exceções abertas por padrão | Baixa e estável | Padrões cumpríveis; picos indicam padrão inadequado |
| Exceções vencidas | Zero | Disciplina do processo |
| Exceções com compensatório verificado | 100% | Se os compensatórios existem de fato |
| Tempo médio de vida das exceções | Compatível com os prazos aprovados | Se o temporário continua temporário |

## Como apresentar e justificar

- **Para a diretoria:** "Temos 14 exceções abertas, 3 vencidas. As vencidas concentram risco em sistemas de liquidação. Precisamos de decisão da área de Operações Financeiras sobre renovação ou correção."
- **Para engenharia:** "O padrão de mTLS vem com uma implementação de referência no service mesh. Quem não conseguir aplicar tem um processo de exceção com prazo de resposta conhecido."
- **Para auditoria:** "Cada configuração da baseline aponta para o padrão de origem; cada desvio tem exceção aprovada pelo dono do risco e compensatórios verificáveis."

## Checklist de revisão arquitetural

- [ ] Os princípios de segurança têm declaração, justificativa e implicações.
- [ ] Cada padrão é verificável, delimitado, versionado e tem dono.
- [ ] Cada padrão aponta o princípio e o risco de origem.
- [ ] As baselines partem de referências reconhecidas, com desvios documentados.
- [ ] As baselines são aplicadas e verificadas como código onde possível.
- [ ] Há um processo de exceções publicado, com prazo, compensatórios e aprovação pelo dono do risco.
- [ ] Exceções vencidas são acompanhadas e reportadas.
- [ ] Em ambientes híbridos, existe um padrão por tema, com implementação por ambiente.

## Questões de compreensão

**1.** Classifique: (a) "Senhas de contas de serviço são armazenadas no cofre corporativo e rotacionadas a cada 90 dias." (b) "Prefira serviços gerenciados a soluções desenvolvidas internamente para gestão de segredos." (c) "Menor privilégio: identidades recebem apenas as permissões necessárias à sua função."

??? success "Resposta comentada"

    (a) **Padrão** — obrigatório e verificável. (b) **Diretriz** — recomendação, não obrigatória. (c) **Princípio** — orienta decisões, mas não é verificável diretamente sem padrões derivados.

**2.** Por que "monitoramento reforçado" costuma ser um controle compensatório insuficiente?

??? success "Resposta comentada"

    Porque um compensatório precisa tratar o **mesmo risco** do controle ausente. Monitoramento genérico detecta alguns eventos depois que ocorrem, mas não substitui um controle preventivo de integridade ou confidencialidade. Ele pode compor a compensação, mas raramente basta sozinho — e "reforçado" precisa ser especificado: que eventos, com que alerta e com que resposta.

**3.** Um padrão de criptografia exige HSM para todas as chaves da organização. Noventa por cento dos novos projetos pedem exceção. O que isso sugere?

??? success "Resposta comentada"

    Que o padrão provavelmente é **complexidade desnecessária** para a maior parte dos casos: aplica o mesmo rigor a ativos de valor muito diferente. A correção é diferenciar por classificação — por exemplo, HSM para chaves de dados de cartão e de assinatura, serviço de chaves gerenciado para os demais — e reduzir as exceções a casos realmente excepcionais.

**4.** Quem deve aprovar uma exceção de risco alto em um sistema de liquidação financeira — o arquiteto de segurança ou a diretoria de operações financeiras? Por quê?

??? success "Resposta comentada"

    A **diretoria de operações financeiras**, que responde pelo negócio afetado e tem autoridade para aceitar o risco. O arquiteto analisa, propõe compensatórios e recomenda, mas aceitar risco é uma decisão de negócio.

## Exercício de tomada de decisão

!!! question "Cenário: baseline para os servidores de pagamento"

    A Aurora vai criar a baseline dos servidores Linux da zona de pagamentos, no datacenter e na AWS. O time de engenharia apresenta três propostas:

    - **A — Perfil mais restritivo do benchmark CIS integralmente**, nos dois ambientes.
    - **B — Perfil básico do benchmark CIS com desvios documentados**, aplicado por ferramenta de configuração no datacenter e por imagem padronizada e verificação contínua na AWS, mais controles adicionais específicos para PCI.
    - **C — Baseline própria**, escrita pela equipe a partir da experiência, sem referência externa.

    O sistema de pagamentos usa um agente de monitoramento de fornecedor que, segundo testes, falha com algumas restrições do perfil mais restritivo. Critérios: redução de risco, compatibilidade com as aplicações, verificabilidade e esforço de manutenção.

??? success "Resolução de referência"

    | Critério | Peso | A — Perfil restritivo | B — Perfil básico + desvios + PCI | C — Própria |
    |:---|:---|:---|:---|:---|
    | Redução de risco | 3 | 3 | 3 | 2 |
    | Compatibilidade com as aplicações | 2 | 1 | 3 | 3 |
    | Verificabilidade | 2 | 3 | 3 | 1 |
    | Esforço de manutenção | 1 | 2 | 2 | 1 |
    | **Total ponderado** | | **19** | **23** | **15** |

    **Recomendação: B.** O perfil básico com controles adicionais direcionados ao risco PCI atinge redução de risco comparável à alternativa A sem quebrar o agente de monitoramento — e cada desvio fica documentado e justificado. A alternativa A geraria exceções imediatas, e a tendência das equipes seria desativar a baseline inteira. A alternativa C perde a referência externa, dificulta a auditoria e depende do conhecimento de poucas pessoas.

    **Risco residual:** os itens do perfil restritivo não adotados. Eles devem ser analisados um a um; os que tratam riscos relevantes para a zona de pagamentos entram como controles adicionais, e os demais são registrados como desvios aceitos.

## Pontos-chave

- Política expressa intenção; princípio orienta decisões; padrão é obrigatório e verificável; baseline é a configuração mínima; controle é o mecanismo no ambiente.
- Princípios bem escritos têm declaração, justificativa e implicações.
- Padrões precisam ser verificáveis, delimitados, versionados e ter dono.
- Exceções são desvios conscientes: com risco analisado, compensatório que trate o mesmo risco, prazo e aprovação pelo dono do risco.
- Muitas exceções ao mesmo padrão indicam complexidade desnecessária — revise o padrão.

## Referências

- NIST. *SP 800-53 Rev. 5 — Security and Privacy Controls* (Release 5.2.0). 2025. <https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls> — gratuito.
- CIS. *CIS Critical Security Controls v8.1 — Implementation Groups*. <https://www.cisecurity.org/controls/implementation-groups> — gratuito.
- AWS. *Well-Architected Framework — Security Pillar: Design principles*. <https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html> — gratuito.
- Google Cloud. *Well-Architected Framework: Security, privacy, and compliance pillar*. <https://docs.cloud.google.com/architecture/framework/security> — gratuito.

### Leituras de aprofundamento

Incluídas na revisão bibliográfica de 2026-10-23, **depois** da escrita desta aula: complementam e permitem conferir o conteúdo, mas não foram a base original do texto. A situação de cada leitura está entre parênteses.

- NIST. *SP 800-160 Vol. 1 Rev. 1*, 2022, Apêndice E *Principles for Trustworthy Secure Design* (p. 82) — trinta princípios (E.1–E.30), entre eles *Least Privilege* (E.16) e *Minimal Trusted Elements* (E.20). *(localizado pelo sumário.)*
- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020, Cap. 6, §6.4.5 *Environmental creep* (p. 238) — mecanismos que perdem eficácia quando o contexto muda: argumento para exceções com prazo e revisão periódica de padrões. *(lido.)*
- The Open Group. *TOGAF — Architecture Principles* (documentação online da série TOGAF 9) — <https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap20.html>. *(lido em 2026-10-23; formato e critérios de princípios.)*
- SABSA Institute. *W105 — SABSA Enterprise Security Architecture Principles*, janeiro de 2026 — <https://sabsa.org/white-paper-requests/>. *(catálogo conferido; leitura pendente.)*

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
| Revisão bibliográfica | 2026-10-23 — [registro da revisão retroativa](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/retroactive-review-m02.md) |
