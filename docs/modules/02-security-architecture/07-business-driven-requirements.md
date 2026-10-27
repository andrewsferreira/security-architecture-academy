---
id: M02-L07
title: "Business-driven Security Architecture: de requisitos de negócio a requisitos de segurança"
description: Como partir de objetivos de negócio para chegar a requisitos de segurança verificáveis e rastreáveis, traduzindo riscos técnicos em riscos de negócio e conciliando segurança com experiência e custo.
domain: enterprise-architecture
tier: architect
status: published
prerequisites: [M02-L04, M02-L06, M01-L06]
objectives:
  - Derivar requisitos de segurança verificáveis a partir de objetivos de negócio, ameaças e obrigações.
  - Diferenciar requisitos funcionais de segurança, requisitos de qualidade e restrições.
  - Traduzir um risco técnico em risco de negócio e vice-versa.
  - Construir uma matriz de rastreabilidade do objetivo de negócio à evidência.
  - Conciliar requisitos de segurança conflitantes com requisitos de negócio.
minutes: 90
sources: [SABSA-W101, NIST-CSF-2, NIST-SP800-160-V1R1, NIST-SP800-53]
further_reading: [NIST-SP800-160-V1R1, BOOK-ANDERSON-SE3]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M02
---

# Business-driven Security Architecture: de requisitos de negócio a requisitos de segurança

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 1 · M02-L07</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">90 min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    O momento mais importante de uma arquitetura de segurança acontece antes de qualquer diagrama: quando alguém transforma "queremos vender mais para pequenos lojistas" em requisitos que a engenharia consegue implementar e a auditoria consegue verificar. Esta aula ensina esse caminho — e a fazer o caminho inverso, explicando ao negócio por que cada controle existe.

**Pré-requisitos:** [Princípios, padrões, baselines e exceções](04-principles-standards-baselines-exceptions.md), [Frameworks](06-frameworks.md) e os conceitos de risco (M01-L06).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Derivar requisitos de segurança verificáveis a partir de objetivos de negócio, ameaças e obrigações.
- Diferenciar requisitos funcionais de segurança, requisitos de qualidade e restrições.
- Traduzir um risco técnico em risco de negócio e vice-versa.
- Construir uma matriz de rastreabilidade do objetivo de negócio à evidência.
- Conciliar requisitos de segurança conflitantes com requisitos de negócio.

## Conceito

### O que é arquitetura de segurança orientada ao negócio

**Business-driven Security Architecture** é a prática de derivar cada decisão de segurança de uma necessidade de negócio identificável — um objetivo, um ativo, uma obrigação ou um risco que a organização se importa em evitar. A ideia está no centro do SABSA, mas não depende do método completo: qualquer arquitetura pode (e deve) ser rastreável até o negócio.

### Por que existe

Porque segurança desconectada do negócio falha de duas formas:

- **Excesso:** controles caros que protegem ativos de pouco valor ou tratam riscos irrelevantes, gerando atrito e perda de credibilidade.
- **Falta:** riscos de negócio relevantes que ninguém traduziu em requisitos técnicos e, por isso, ninguém tratou.

A orientação ao negócio é o que permite ao arquiteto dizer **"isto é necessário"** e **"isto não é"** com a mesma convicção.

### Qual problema resolve

Resolve o problema da **justificativa e da proporcionalidade**. Um requisito rastreável até um objetivo de negócio:

- pode ser priorizado contra outros requisitos;
- pode ser explicado a quem paga por ele;
- pode ser removido quando o objetivo deixar de existir.

### Requisitos funcionais × não funcionais

Esta é a aula principal do currículo para essa distinção. Em engenharia de software, **requisitos funcionais** descrevem o que o sistema faz; **requisitos não funcionais** (ou de qualidade) descrevem como ele se comporta — desempenho, disponibilidade, segurança, usabilidade. Para a segurança, é útil separar três categorias:

| Categoria | O que descreve | Exemplo |
|:---|:---|:---|
| **Requisito funcional de segurança** | Uma função de segurança que o sistema executa | "O sistema exige um segundo fator para alterar a conta bancária de recebimento do lojista." |
| **Requisito de qualidade relacionado à segurança** | Uma propriedade mensurável do comportamento | "O serviço de autorização mantém disponibilidade de 99,95% no mês." · "Eventos de autenticação chegam ao SIEM em até 5 minutos." |
| **Restrição** | Uma condição imposta, não negociável no projeto | "Dados de cartão não são armazenados fora do ambiente de dados de cartão." · "Dados pessoais de brasileiros seguem a LGPD." |

A distinção importa porque cada categoria é verificada de forma diferente: funções por testes, qualidades por medição contínua, restrições por inspeção de desenho e de configuração.

### Risco técnico × risco de negócio

Esta também é a aula principal para essa distinção. **Risco técnico** descreve o que pode acontecer com um componente; **risco de negócio** descreve o que isso significa para a organização.

| Risco técnico | Risco de negócio |
|:---|:---|
| "A API de links permite enumerar identificadores de transação." | "Concorrentes ou fraudadores podem extrair o volume de vendas de lojistas, gerando quebra de confidencialidade contratual e reclamações." |
| "O webhook ao lojista não é assinado." | "Um fraudador pode falsificar a confirmação de pagamento e levar o lojista a entregar mercadoria não paga — com prejuízo atribuído à Aurora." |
| "O serviço de autorização roda em uma única zona de disponibilidade." | "Uma falha na zona interrompe vendas de todos os lojistas; cada hora parada representa perda de receita e risco de descumprimento de SLA contratual." |

Arquitetos precisam fazer a tradução nos dois sentidos: **de baixo para cima**, para conseguir decisão e orçamento; **de cima para baixo**, para transformar apetite a risco em requisitos.

## Fundamentos técnicos

### O caminho do objetivo à evidência

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l07-traceability.mmd"
```

<figcaption>Figura 1 — Rastreabilidade do objetivo de negócio à evidência.</figcaption>
</figure>

### Passo 1 — Entender o objetivo e o contexto

Antes de falar de segurança, registre:

- **Objetivo de negócio:** o que a iniciativa deve alcançar, preferencialmente com uma métrica.
- **Ativos de valor:** dados, processos, reputação, receita.
- **Partes interessadas:** quem ganha e quem perde se algo der errado.
- **Restrições:** leis, contratos, normas, prazos e orçamento.
- **Apetite a risco:** o que a organização aceita perder, e o que não aceita.

### Passo 2 — Definir atributos de negócio

Atributos de negócio expressam **o que o negócio precisa que seja verdade** em termos que o próprio negócio entende. É a ideia do *Business Attributes Profile* do SABSA: cada atributo tem definição e métrica com meta (o W100 descreve definição e métrica; registrar também a justificativa de cada atributo é uma prática recomendada por este curso).

| Atributo | Definição | Métrica e meta |
|:---|:---|:---|
| Disponível | Lojistas e compradores conseguem pagar quando precisam | Disponibilidade mensal do fluxo de pagamento ≥ 99,95% |
| Confidencial | Dados de cartão e de vendas só são acessados por quem tem direito | Zero incidentes de exposição de dados de cartão |
| Íntegro | Transações e confirmações não podem ser falsificadas | Zero confirmações de pagamento aceitas sem assinatura válida |
| Rastreável | Toda alteração sensível tem autor identificável | 100% das alterações de dados bancários com autor e segundo fator registrados |
| Conforme | Atende às obrigações legais e contratuais | Sem não conformidades em avaliações PCI DSS e de LGPD |
| Fluido | O pagamento não cria atrito desnecessário ao comprador | Taxa de abandono no checkout ≤ meta definida pelo produto |

Note o último atributo: **orientar ao negócio também significa proteger a experiência**. Atributos de segurança e de negócio entram juntos na mesma tabela, e os conflitos ficam visíveis.

### Passo 3 — Considerar ameaças e obrigações

Requisitos não nascem só dos atributos. Eles também vêm de:

- **Ameaças** identificadas por threat modeling (aprofundado no M04).
- **Obrigações** legais, contratuais e normativas — que geram, em geral, restrições.
- **Padrões corporativos** já existentes, que a solução herda.

### Passo 4 — Escrever requisitos verificáveis

Um bom requisito de segurança é:

| Qualidade | Pergunta de teste | Ruim | Bom |
|:---|:---|:---|:---|
| **Específico** | Diz exatamente o que precisa ser verdade? | "Proteger o webhook" | "Toda notificação enviada ao lojista é assinada com HMAC-SHA256 usando segredo exclusivo por lojista." |
| **Verificável** | É possível provar que foi atendido? | "Logs adequados" | "Eventos de alteração de dados bancários chegam ao SIEM em até 5 minutos, com identificador do usuário e do dispositivo." |
| **Rastreável** | Aponta para atributo, ameaça ou obrigação? | Requisito sem origem | `REQ-07` ← atributo *Íntegro* e ameaça *falsificação de confirmação* |
| **Necessário** | O que se perde se ele for removido? | "Criptografar tudo com HSM" sem análise | Requisito que trata um risco ou obrigação específicos |
| **Viável** | É implementável com as restrições do projeto? | Requisito que exige tecnologia indisponível | Requisito compatível com a plataforma |
| **Neutro em produto** | Descreve o quê, não com qual ferramenta? | "Usar o produto X" | "Usar o serviço corporativo de gestão de segredos" |

Escreva requisitos com verbo no presente e sujeito claro: "O serviço **registra**…", "O sistema **exige**…". Evite "deveria", "se possível", "adequado".

### Passo 5 — Ligar requisitos a controles e evidências

Cada requisito precisa de pelo menos um controle e de um **método de verificação**: teste automatizado, revisão de configuração, medição contínua ou inspeção de desenho. A [matriz de rastreabilidade](#exemplo-empresarial) do exemplo mostra o formato.

## Exemplo empresarial

!!! example "Aurora Pagamentos — pagamento por link"

    **Objetivo de negócio:** aumentar em 30% o número de pequenos lojistas ativos em 12 meses, oferecendo pagamento por link enviado por mensagem, sem que o lojista precise de site próprio.

    **Restrições:** PCI DSS para dados de cartão; LGPD para dados pessoais de compradores; prazo de lançamento de quatro meses.

    **Apetite a risco declarado pela diretoria:** nenhuma tolerância a exposição de dados de cartão; tolerância baixa a fraude por falsificação de confirmação; tolerância moderada a indisponibilidade de até 30 minutos por mês fora do horário comercial.

    ```mermaid
    --8<-- "assets/diagrams/m02-l07-paylink.mmd"
    ```

    **Matriz de rastreabilidade (extrato)**

    | ID | Requisito | Categoria | Origem | Controle | Verificação |
    |:---|:---|:---|:---|:---|:---|
    | REQ-01 | Dados de cartão são capturados apenas na página de pagamento hospedada no ambiente de dados de cartão; o portal do lojista e o serviço de links nunca os recebem. | Restrição | Atributo *Confidencial*; PCI DSS | Página hospedada; segmentação do ambiente de dados de cartão | Revisão de fluxos; teste de que nenhum endpoint fora do ambiente aceita dados de cartão |
    | REQ-02 | Toda notificação ao lojista é assinada com HMAC-SHA256 com segredo exclusivo por lojista, rotacionável pelo lojista. | Funcional | Atributo *Íntegro*; ameaça de falsificação de confirmação | Assinatura de webhook; gestão de segredos | Teste automatizado rejeitando notificações sem assinatura válida |
    | REQ-03 | A alteração da conta bancária de recebimento exige um segundo fator e gera notificação ao e-mail cadastrado. | Funcional | Atributo *Rastreável*; ameaça de tomada de conta do lojista | MFA na operação sensível; notificação | Teste funcional; amostragem de eventos no SIEM |
    | REQ-04 | Links de pagamento expiram em até 72 horas e são de uso único. | Funcional | Ameaça de reutilização de links | Lógica do serviço de links | Teste automatizado |
    | REQ-05 | O fluxo de pagamento mantém disponibilidade mensal ≥ 99,95%. | Qualidade | Atributo *Disponível* | Implantação em múltiplas zonas; monitoramento de disponibilidade | Medição contínua |
    | REQ-06 | Dados pessoais de compradores são retidos pelo prazo definido pela área jurídica e eliminados ao fim dele. | Restrição | Atributo *Conforme*; LGPD | Política de retenção automatizada | Auditoria trimestral de retenção |
    | REQ-07 | Identificadores de links e de transações são aleatórios e não sequenciais, e o serviço verifica se o recurso consultado pertence ao lojista autenticado. | Funcional | Atributo *Confidencial*; ameaça de enumeração | Identificadores aleatórios; autorização em nível de objeto | Teste de autorização com dois lojistas distintos |

    Repare que **nenhum requisito nomeia um produto** e que cada um aponta sua origem. Se, no futuro, a Aurora deixar de enviar webhooks, o REQ-02 sai junto — e todo mundo sabe por quê.

## Arquitetura tradicional versus recomendada

| Aspecto | Tradicional — orientada a controles | Recomendada — orientada ao negócio |
|:---|:---|:---|
| Ponto de partida | Lista de controles da norma | Objetivo, ativos, apetite a risco |
| Requisitos | "Atender ao PCI DSS" | Requisitos específicos derivados do fluxo, com a norma como restrição |
| Linguagem | Técnica | Técnica para a engenharia; de negócio para a diretoria — conectadas pela rastreabilidade |
| Conflitos com a experiência do usuário | Descobertos depois do lançamento | Explicitados nos atributos e resolvidos no desenho |
| Remoção de controles | Ninguém sabe se pode remover | A rastreabilidade mostra o que deixa de ser protegido |

## Controles e padrões relevantes

| Elemento | Objetivo | Referência |
|:---|:---|:---|
| Business Attributes Profile | Traduzir necessidades de negócio em atributos mensuráveis | SABSA |
| Perfil-alvo de resultados | Ligar os requisitos de uma solução aos resultados de cibersegurança da organização | NIST CSF 2.0 (Organizational Profiles) |
| Requisitos de segurança no ciclo de vida | Definir requisitos de proteção como parte da engenharia do sistema | NIST SP 800-160 Vol. 1 Rev. 1 |
| Especificação precisa de controles | Linguagem comum para requisitos e controles | NIST SP 800-53 Rev. 5 |
| Modelo de especificação | Estrutura para documentar requisitos | [Security Requirements Specification](../../artifacts/security-requirements-specification.md) |

## Aplicabilidade: on-premises, cloud e híbrido

Requisitos bem escritos são **independentes de ambiente**. O ambiente aparece em três lugares: nas restrições, nas ameaças específicas e na forma de verificação.

| Aspecto | On-premises | Cloud | Híbrido |
|:---|:---|:---|:---|
| Restrições típicas | Capacidade do datacenter, janelas de mudança | Regiões disponíveis, residência de dados, modelo de responsabilidade | Ambas, mais latência e dependência da conectividade entre ambientes |
| Ameaças específicas | Movimentação lateral em rede plana | Configurações públicas por engano, permissões excessivas | Abuso da confiança entre ambientes (identidade sincronizada, túneis) |
| Verificação dos requisitos | Inspeção e testes periódicos | Verificação contínua por políticas e serviços de postura | Duas formas de verificação para o mesmo requisito — que precisam produzir evidências comparáveis |
| Requisito que costuma faltar | Recuperação em caso de perda do datacenter | Saída do provedor e portabilidade | Comportamento quando a conexão entre ambientes falha |

**Particularidade do híbrido:** inclua sempre requisitos sobre **modos degradados** — o que acontece com autenticação, autorização e registro de eventos quando a conectividade entre datacenter e cloud cai. Esses requisitos raramente são pedidos pelo negócio, mas protegem exatamente os atributos *Disponível* e *Rastreável*.

## Como especificar e implementar

1. **Conduza uma sessão de contexto** com produto, negócio e jurídico: objetivo, ativos, restrições e apetite a risco.
2. **Monte o perfil de atributos** com métricas — inclusive atributos de experiência e custo.
3. **Identifique ameaças** sobre o fluxo conceitual (threat modeling simplificado; completo no M04).
4. **Escreva os requisitos** com IDs estáveis e categoria (funcional, qualidade, restrição).
5. **Monte a matriz de rastreabilidade:** origem → requisito → controle → verificação.
6. **Valide com os stakeholders:** o negócio confirma os atributos e o apetite; a engenharia confirma a viabilidade.
7. **Registre conflitos e decisões** em ADRs — ver a [próxima aula](08-architecture-decision-records.md).
8. **Use o modelo** de [Security Requirements Specification](../../artifacts/security-requirements-specification.md).

## Trade-offs, limitações e antipadrões

| Antipadrão | Problema | Correção |
|:---|:---|:---|
| **Copiar a norma como requisito** | "Atender ao PCI DSS" não diz o que construir | Derivar requisitos específicos do fluxo; a norma vira restrição e fonte de verificação |
| **Gold plating** | Requisitos máximos para todos os ativos | Proporcionalidade pelo valor do ativo e pelo apetite a risco |
| **Requisitos de ferramenta** | "Usar o WAF X" | Descrever o resultado; o produto é decisão física |
| **Requisitos órfãos** | Ninguém sabe por que o requisito existe | Origem obrigatória na matriz |
| **Ignorar a experiência** | Segurança que derruba a conversão é contornada pelo negócio | Atributos de experiência no mesmo perfil |
| **Apetite a risco presumido** | O arquiteto decide sozinho o que é aceitável | Apetite declarado por quem responde pelo negócio |

**Limitação:** a orientação ao negócio depende de o negócio conseguir articular seus objetivos e seu apetite a risco. Quando isso não acontece, o arquiteto precisa **propor** atributos e metas e obter confirmação explícita — nunca presumir.

## Como validar

| Verificação | Critério |
|:---|:---|
| Cobertura | Todo atributo de negócio tem ao menos um requisito; todo requisito tem origem. |
| Verificabilidade | Todo requisito tem método de verificação e critério de aceitação. |
| Confirmação | Atributos, metas e apetite a risco foram confirmados por quem responde pelo negócio. |
| Proporcionalidade | Requisitos de alto custo apontam para ativos de alto valor ou obrigações. |
| Conflitos explícitos | Conflitos entre atributos estão registrados e decididos. |

## Como apresentar e justificar

O mesmo requisito, contado para públicos diferentes:

| Público | Como apresentar o REQ-02 (webhook assinado) |
|:---|:---|
| Diretoria | "Sem isso, um fraudador poderia falsificar a confirmação de pagamento e o lojista entregaria mercadoria não paga. O prejuízo e o dano à marca seriam nossos." |
| Produto | "O lojista ganha a garantia de que toda confirmação veio da Aurora. Para integrações simples, oferecemos bibliotecas que validam a assinatura automaticamente." |
| Engenharia | "HMAC-SHA256 com segredo por lojista no serviço de gestão de segredos; rejeitar notificações sem assinatura válida; permitir rotação sem indisponibilidade." |

## Checklist de revisão arquitetural

- [ ] Objetivo de negócio, ativos, restrições e apetite a risco estão registrados e confirmados.
- [ ] Há um perfil de atributos com métricas, incluindo atributos de experiência.
- [ ] Os requisitos estão classificados em funcionais, de qualidade e restrições.
- [ ] Cada requisito é específico, verificável, rastreável, necessário, viável e neutro em produto.
- [ ] A matriz de rastreabilidade liga origem, requisito, controle e verificação.
- [ ] Os riscos técnicos relevantes foram traduzidos em riscos de negócio para a decisão.
- [ ] Os conflitos entre atributos estão registrados em ADRs.
- [ ] Em soluções híbridas, há requisitos para modos degradados de conectividade.

## Questões de compreensão

**1.** Classifique: (a) "O sistema bloqueia a conta após 10 tentativas de login malsucedidas em 15 minutos." (b) "O tempo de resposta da autorização permanece abaixo de 300 ms no percentil 95, mesmo com a inspeção de fraude ativa." (c) "Dados de cartão não podem ser armazenados em logs."

??? success "Resposta comentada"

    (a) **Requisito funcional de segurança** — uma função que o sistema executa. (b) **Requisito de qualidade** — uma propriedade mensurável que a segurança não pode degradar. (c) **Restrição** — imposta por obrigação normativa e verificada por inspeção de desenho e de configuração.

**2.** Reescreva o requisito "O sistema deve ter logs adequados" de forma verificável.

??? success "Resposta comentada"

    Uma reescrita possível: "O serviço de links registra criação, uso, expiração e cancelamento de links, com identificador do lojista, endereço de origem e horário, e envia os eventos ao SIEM em até 5 minutos; os registros são retidos por 12 meses." O requisito agora diz o que registrar, onde, em quanto tempo e por quanto tempo — e pode ser testado. Os prazos devem vir das obrigações e da necessidade de investigação de cada organização.

**3.** Traduza para risco de negócio: "As credenciais de acesso ao banco de dados de pedidos estão no código-fonte, em um repositório acessível a 80 desenvolvedores."

??? success "Resposta comentada"

    "Qualquer um dos 80 desenvolvedores — ou alguém que comprometa a conta de um deles ou o repositório — pode ler e alterar todos os pedidos de clientes. Isso permite vazamento de dados pessoais, com exposição a sanções da LGPD e dano à reputação, e fraude na alteração de pedidos, com perda financeira direta." Uma boa tradução nomeia quem pode agir, o que pode fazer e o impacto para o negócio.

**4.** Por que "atender ao PCI DSS" não é um bom requisito de segurança para uma solução?

??? success "Resposta comentada"

    Porque não diz o que construir. A norma é uma **restrição** e uma fonte de verificação; a solução precisa de requisitos específicos derivados do seu fluxo — onde os dados de cartão são capturados, por onde passam, onde nunca podem estar. Sem isso, cada equipe interpreta a norma de um jeito e a conformidade vira descoberta tardia.

**5.** Que tipo de requisito costuma faltar em soluções híbridas, e por quê?

??? success "Resposta comentada"

    Requisitos de **modo degradado**: o que acontece com autenticação, autorização e registro de eventos quando a conectividade entre ambientes falha. O negócio raramente os pede explicitamente, mas eles protegem a disponibilidade e a rastreabilidade em incidentes — justamente quando mais importam.

## Exercício de tomada de decisão

!!! question "Cenário: atrito no checkout"

    No pagamento por link, a equipe de prevenção a fraudes pede autenticação adicional do comprador (por exemplo, o protocolo de autenticação do emissor do cartão) em **todas** as transações. O produto argumenta que isso aumentará o abandono no checkout e comprometerá o objetivo de crescimento. Alternativas:

    - **A — Autenticação adicional em todas as transações.**
    - **B — Autenticação adicional baseada em risco:** acionada por valor, comportamento, dispositivo ou histórico do lojista.
    - **C — Nenhuma autenticação adicional:** apenas análise de fraude após a autorização.

    Critérios, com pesos confirmados pela diretoria: redução de fraude (3), conversão no checkout (3), custo operacional (1), clareza de responsabilidade em caso de fraude (2).

??? success "Resolução de referência"

    | Critério | Peso | A — Sempre | B — Por risco | C — Nunca |
    |:---|:---|:---|:---|:---|
    | Redução de fraude | 3 | 3 | 2 | 1 |
    | Conversão no checkout | 3 | 1 | 3 | 3 |
    | Custo operacional | 1 | 2 | 2 | 1 |
    | Clareza de responsabilidade | 2 | 3 | 2 | 1 |
    | **Total ponderado** | | **20** | **21** | **15** |

    **Recomendação: B, com ressalvas.** A diferença entre A e B é pequena — o que indica que a decisão é sensível aos pesos. Se a diretoria aumentasse o peso de redução de fraude, A venceria. Por isso, a decisão deve ser registrada em ADR com:

    - **Critérios de acionamento** iniciais e responsável por calibrá-los.
    - **Métricas de acompanhamento:** taxa de fraude e taxa de abandono, revistas mensalmente.
    - **Gatilho de revisão:** se a fraude ultrapassar o limite aceito pela diretoria, a política passa para A até nova análise.

    **Risco residual:** fraudes em transações abaixo do limiar de acionamento. Aceito pela diretoria de produto, com limite mensal monitorado.

    Este exercício ilustra um ponto central: **o arquiteto não decide os pesos** — eles expressam o apetite a risco e as prioridades do negócio. O arquiteto torna o trade-off explícito e mostra quanto a decisão depende deles.

## Pontos-chave

- Toda decisão de segurança deve ser rastreável a um objetivo, ativo, obrigação ou risco de negócio.
- Atributos de negócio com métricas — incluindo experiência e custo — tornam os conflitos visíveis.
- Requisitos podem ser funcionais, de qualidade ou restrições, e cada categoria é verificada de forma diferente.
- Bons requisitos são específicos, verificáveis, rastreáveis, necessários, viáveis e neutros em produto.
- O arquiteto traduz risco técnico em risco de negócio e torna os trade-offs explícitos; quem responde pelo negócio decide os pesos e aceita o risco.

## Referências

- The SABSA Institute. *W101 — Architecting a Secure Digital World*. Agosto de 2018. <https://sabsa.org/white-paper-w101-architecting-a-secure-digital-world/> — download gratuito pelo [catálogo de white papers](https://sabsa.org/white-paper-requests/) (conferido em 2026-10-23).
- NIST. *The NIST Cybersecurity Framework (CSF) 2.0*, CSWP 29. 2024. <https://doi.org/10.6028/NIST.CSWP.29> — gratuito.
- NIST. *SP 800-160 Vol. 1 Rev. 1 — Engineering Trustworthy Secure Systems*. 2022. <https://csrc.nist.gov/news/2022/guidance-on-engineering-trustworthy-secure-systems> — gratuito.
- NIST. *SP 800-53 Rev. 5* (Release 5.2.0). 2025. <https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls> — gratuito.

### Leituras de aprofundamento

Incluídas na revisão bibliográfica de 2026-10-23, **depois** da escrita desta aula: complementam e permitem conferir o conteúdo, mas não foram a base original do texto. A situação de cada leitura está entre parênteses.

- NIST. *SP 800-160 Vol. 1 Rev. 1*, 2022, Apêndice C.3 *Distinguishing Requirements, Policy, and Mechanisms* (p. 68) e Apêndice H, H.1–H.4 (pp. 115–122) — da análise de missão à definição de arquitetura. *(localizado pelo sumário.)*
- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020, Cap. 27, §27.4 *Prioritising protection goals* (p. 978) e §27.2 *Risk management* (p. 966). *(lido.)*

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
| Revisão bibliográfica | 2026-10-23 — [registro da revisão retroativa](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/retroactive-review-m02.md) |
