---
id: M01-L02
title: "Princípios de design seguro"
description: Os princípios que orientam decisões de arquitetura — least privilege, defense in depth, fail-safe defaults, complete mediation, separation of duties, economy of mechanism, open design e minimal trusted elements — e como aplicá-los sem transformá-los em slogans.
domain: security-foundations
tier: fundamental
status: published
prerequisites: [M01-L01]
objectives:
  - Explicar os princípios clássicos de design seguro e sua origem.
  - Aplicar cada princípio a uma decisão concreta de arquitetura.
  - Identificar quando princípios entram em conflito e como decidir.
  - Reconhecer violações de princípios em diagramas e configurações.
minutes: 75
sources: [BOOK-ANDERSON-SE3, NIST-SP800-160-V1R1, SALTZER-SCHROEDER-1975]
further_reading: [NIST-SP800-207, BOOK-GOOGLE-BSRS]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M01
---

# Princípios de design seguro

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 · M01-L02</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">75 min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Princípios de design seguro são **heurísticas acumuladas** — lições de décadas de falhas transformadas em regras de decisão. Bem usados, permitem decidir rapidamente entre alternativas e explicar a decisão. Mal usados, viram slogans em apresentações. Esta aula apresenta os princípios que a formação usa, sua origem, como aplicá-los e, principalmente, como reconhecer quando dois deles puxam para lados opostos.

**Pré-requisitos:** [Propriedades de segurança](01-security-properties.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar os princípios clássicos de design seguro e sua origem.
- Aplicar cada princípio a uma decisão concreta de arquitetura.
- Identificar quando princípios entram em conflito e como decidir.
- Reconhecer violações de princípios em diagramas e configurações.

## Conceito

### De onde vêm os princípios

Em 1975, Jerome Saltzer e Michael Schroeder publicaram *The Protection of Information in Computer Systems*, que reuniu oito princípios de design — *economy of mechanism*, *fail-safe defaults*, *complete mediation*, *open design*, *separation of privilege*, *least privilege*, *least common mechanism* e *psychological acceptability* — e dois adicionais, *work factor* e *compromise recording*. Quase cinquenta anos depois, a maioria continua no centro das discussões de arquitetura.

A referência normativa atual mais completa é o **Apêndice E** da NIST SP 800-160 Vol. 1 Rev. 1 (*Principles for Trustworthy Secure Design*, p. 82), com trinta princípios — entre eles *Defense In Depth* (E.9), *Least Privilege* (E.16), *Mediated Access* (E.19), *Minimal Trusted Elements* (E.20), *Protective Defaults* (E.22) e *Protective Failure* (E.23).

### O que é — e o que não é — um princípio

Um princípio **orienta uma escolha** quando há mais de um caminho. Ele não é verificável diretamente: verifica-se se as decisões o respeitam (tema da [M02-L04](../02-security-architecture/04-principles-standards-baselines-exceptions.md)). "Segurança em primeiro lugar" não é um princípio — não ajuda a escolher nada. "Negar por padrão" é: diante de uma regra de firewall ou de uma permissão nova, diz qual é o ponto de partida.

## Fundamentos técnicos

### Os princípios que a formação usa

| Princípio | Significado | Aplicação típica | Violação típica |
|:---|:---|:---|:---|
| **Least privilege** | Cada entidade recebe apenas os privilégios necessários, pelo tempo necessário | Contas de serviço dedicadas; elevação just-in-time | Conta de serviço com administrador de domínio |
| **Defense in depth** | Camadas independentes de proteção, de modo que a falha de uma não exponha o ativo | Identidade + segmentação + criptografia + detecção | Tudo depende do firewall de borda |
| **Fail-safe defaults / Protective defaults** | O padrão é negar; o acesso precisa ser concedido explicitamente | Firewall "negar e registrar" ao final; buckets privados por padrão | Regras "permitir tudo" entre redes internas |
| **Protective failure (fail secure)** | Em falha, o sistema assume o estado mais seguro aceitável | Autorização indisponível → negar | Validação de token falha → aceitar a requisição |
| **Complete mediation / Mediated access** | Todo acesso é verificado, a cada vez, por um mediador | Autorização em toda chamada de API, não só no login | Permissão guardada em cache por dias |
| **Separation of duties (privilege)** | Operações críticas exigem mais de uma pessoa ou chave | Dupla aprovação de pagamentos; quem desenvolve não implanta sozinho | Mesmo analista cadastra e paga fornecedores |
| **Economy of mechanism** | Mecanismos simples são mais fáceis de verificar | Um provedor de identidade central em vez de dez sistemas de login | Lógica de autorização espalhada e duplicada |
| **Open design** | A segurança não depende de o mecanismo ser secreto | Algoritmos públicos; segredo está só nas chaves | "Ninguém conhece esta porta" |
| **Minimal trusted elements** | Minimizar os componentes que precisam ser confiáveis | Poucos administradores de domínio; poucos sistemas com acesso ao HSM | Dezenas de sistemas com credenciais de alto privilégio |
| **Psychological acceptability** | Controles precisam ser utilizáveis, ou serão contornados | MFA com aprovação por toque e biometria | Senha trocada a cada 30 dias, anotada em papel |

### Defense in depth na prática

Defense in depth não é "mais controles": é **controles independentes**, de modo que um único erro não leve ao ativo. Duas camadas que dependem da mesma credencial ou do mesmo fornecedor não são independentes.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m01-l02-defense-in-depth.mmd"
```

<figcaption>Figura 1 — Camadas independentes no acesso a um sistema de pagamentos.</figcaption>
</figure>

Na figura, um atacante que contorne o WAF ainda precisa de uma identidade válida com MFA; com ela, ainda esbarra na autorização por objeto; e, se explorar a aplicação, encontra a segmentação e os dados cifrados com chave fora do servidor. A detecção atravessa todas as camadas, porque **algumas falhas só são percebidas pela correlação entre elas**.

### Quando princípios conflitam

| Conflito | Exemplo | Como decidir |
|:---|:---|:---|
| *Least privilege* × *psychological acceptability* | Permissões tão restritas que a equipe pede exceções diariamente | Medir a taxa de exceções; usar elevação just-in-time para equilibrar |
| *Defense in depth* × *economy of mechanism* | Cinco produtos de segurança sobrepostos, ninguém sabe configurá-los | Camadas independentes, mas cada uma simples e operável |
| *Fail-safe* × disponibilidade | Bloquear todas as vendas quando o antifraude cai | Decisão de negócio explícita: falhar aberto com limite de valor, ou fechado, com risco documentado |

O último exemplo é importante: "fail secure" nem sempre significa "negar tudo". Significa assumir **o estado mais seguro aceitável para o negócio**, decidido com antecedência — e não descoberto durante o incidente.

## Exemplo empresarial

!!! example "Aurora Pagamentos — princípios aplicados a uma API"

    A equipe da Aurora submeteu uma nova API de estornos. A revisão por princípios encontrou:

    | Princípio | Achado | Correção |
    |:---|:---|:---|
    | Least privilege | A conta de serviço da API tinha permissão de escrita em todas as tabelas | Permissão apenas na tabela de estornos |
    | Complete mediation | A alçada do operador era verificada só na tela, não na API | Verificação de alçada na API, a cada requisição |
    | Fail-safe defaults | Se o serviço de limites estivesse indisponível, o estorno era aprovado | Em falha, o estorno fica pendente para análise |
    | Separation of duties | O mesmo operador solicitava e aprovava estornos | Aprovador diferente do solicitante acima de um valor |
    | Open design | A API usava um "token secreto" fixo no código do aplicativo | Autenticação com OAuth 2.0 e credenciais por cliente |

    Cada achado foi expresso em termos de um princípio — o que tornou a discussão objetiva: ninguém defendeu que "aprovar quando o serviço de limites cai" era uma boa ideia depois que o ponto foi formulado assim.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Uso dos princípios | Lista em slides | Critério explícito de decisão em revisões e ADRs |
| Privilégios | Concedidos para "não atrapalhar" | Mínimos, com elevação temporária quando necessário |
| Camadas | Muitos produtos dependentes entre si | Poucas camadas independentes e operáveis |
| Falha | Comportamento descoberto no incidente | Comportamento em falha decidido e testado |

## Aplicabilidade: on-premises, cloud e híbrido

Os princípios são independentes de ambiente. Em cloud, ganham mecanismos poderosos: políticas que negam por padrão em toda a organização, permissões que expiram, identidades de workload sem segredos fixos. Em ambientes híbridos, o risco é aplicar o princípio em um lado e não no outro — por exemplo, least privilege rigoroso na cloud e contas de serviço administradoras no datacenter que se conecta a ela.

## Como especificar e implementar

- Publicar um conjunto **curto** de princípios (entre cinco e doze), cada um com declaração, justificativa e implicações.
- Referenciar os princípios nos padrões e ADRs: "Este padrão aplica *least privilege* ao…".
- Definir, para cada sistema crítico, o comportamento em falha dos controles de que depende.

## Trade-offs, limitações e antipadrões

- **Antipadrão — princípio-slogan:** citado sem consequência prática.
- **Antipadrão — camadas dependentes chamadas de defense in depth.**
- **Limitação:** princípios não dizem quanto investir — isso vem do risco (L06) e do negócio.

## Como validar

- Em revisões, para cada decisão relevante, perguntar qual princípio a sustenta e qual princípio ela tensiona.
- Testar o comportamento em falha: derrubar o serviço de autorização em ambiente de teste e observar.
- Medir: quantas contas têm privilégios administrativos? Quantas exceções a padrões existem?

## Como apresentar e justificar

- **Para engenharia:** "Pela *complete mediation*, a alçada precisa ser verificada na API, não só na tela."
- **Para gestores:** "Nenhuma pessoa sozinha poderá aprovar e executar um estorno grande, e uma falha técnica não vai liberar estornos automaticamente."

## Checklist de revisão arquitetural

- [ ] Contas e serviços têm privilégios mínimos e documentados.
- [ ] Há camadas independentes protegendo os ativos críticos.
- [ ] O padrão de acesso é negar; permissões são concedidas explicitamente.
- [ ] O comportamento em falha dos controles está decidido e testado.
- [ ] Operações críticas exigem separação de funções.
- [ ] A segurança não depende de segredo do mecanismo.

## Questões de compreensão

**1.** Uma empresa tem firewall, IPS e WAF do mesmo fabricante, gerenciados pelo mesmo console, com a mesma credencial administrativa. Isso é defense in depth?

??? success "Resposta comentada"

    Apenas parcialmente. São mecanismos diferentes, mas compartilham dependências críticas: um comprometimento do console ou da credencial desativa todas as camadas de uma vez. Defense in depth exige camadas independentes.

**2.** Por que "fail secure" não significa sempre "negar tudo"?

??? success "Resposta comentada"

    Porque o estado mais seguro precisa ser aceitável para o negócio. Em alguns casos, negar tudo causa um dano maior do que o risco evitado; a decisão — inclusive limites e compensações — deve ser tomada com antecedência e documentada.

**3.** Dê um exemplo de violação de *open design*.

??? success "Resposta comentada"

    Proteger um serviço apenas por estar em uma porta incomum ou por usar um algoritmo próprio não publicado. Quando o "segredo" do mecanismo é descoberto, a proteção desaparece; o segredo deveria estar apenas nas chaves.

## Exercício de tomada de decisão

!!! question "Cenário: acesso de suporte ao banco de produção da Lumen"

    O suporte da Lumen Saúde pede acesso permanente de leitura ao banco de produção para investigar chamados. O banco contém dados de pacientes. Avalie três opções à luz dos princípios: (A) conta de leitura compartilhada permanente; (B) contas individuais de leitura permanentes, restritas às tabelas de agendamento; (C) acesso individual just-in-time, aprovado por chamado, por até 4 horas, a uma réplica com dados sensíveis mascarados. Critérios: *least privilege*, responsabilização e agilidade do suporte.

??? success "Resolução de referência"

    | Critério | Peso | A — Conta compartilhada | B — Contas individuais permanentes | C — Just-in-time em réplica mascarada |
    |:---|:---|:---|:---|:---|
    | *Least privilege* | 3 | 1 | 2 | 3 |
    | Responsabilização | 2 | 1 | 3 | 3 |
    | Agilidade do suporte | 2 | 3 | 3 | 2 |
    | **Total ponderado** | | **11** | **18** | **19** |

    **Recomendação: C**, com B como etapa intermediária se a ferramenta de just-in-time não estiver disponível.

    - **A** viola *least privilege* (permanente e amplo), *separation of duties* e torna a responsabilização impossível (conta compartilhada).
    - **B** resolve a responsabilização e reduz o escopo, mas mantém privilégio permanente sobre dados sensíveis.
    - **C** aplica *least privilege* no tempo (just-in-time), no escopo (réplica mascarada) e mantém a responsabilização — com custo de implantação maior. A *psychological acceptability* é preservada se a aprovação for rápida.

## Pontos-chave

- Princípios são heurísticas de decisão, não slogans; cada um deve mudar alguma escolha.
- Os princípios de Saltzer e Schroeder (1975) e o Apêndice E da SP 800-160 são as referências principais.
- Defense in depth exige camadas **independentes**.
- Fail secure significa o estado mais seguro **aceitável**, decidido antes do incidente.
- Princípios conflitam; as decisões e seus trade-offs devem ser registrados.

## Referências

### Fundamentação principal

- J. Saltzer e M. Schroeder. *The Protection of Information in Computer Systems*. Proceedings of the IEEE, 63(9):1278–1308, 1975 — lista original dos princípios. *(Dados e lista de princípios conferidos em fonte secundária; o artigo original não foi aberto.)*
- NIST. *SP 800-160 Vol. 1 Rev. 1*. 2022. Apêndice E, *Principles for Trustworthy Secure Design* (E.1–E.30, p. 82). <https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final> *(nomes e numeração conferidos no sumário; definições não acessíveis ao ambiente de verificação)*.
- R. Anderson. *Security Engineering*, 3ª ed. Cap. 6, §6.4 *What goes wrong* e §6.4.4 *Remedies* (pp. 231–238) — falhas de controle de acesso e o papel de *least privilege*; Cap. 12, §12.2.4 (p. 411) — separação de funções e dupla custódia.

### Leitura complementar

- H. Adkins *et al.* *Building Secure and Reliable Systems*. Cap. 5 *Design for Least Privilege*. *(Capítulo localizado pelo sumário.)*
- NIST. *SP 800-207*. §2.1 (p. 6) — princípios de Zero Trust como extensão de *complete mediation* e *least privilege*.

### Aplicação prática

- Use a tabela de princípios como roteiro da revisão de qualquer API ou integração nova; registre o princípio associado a cada achado.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
