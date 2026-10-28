---
id: M02-L05
title: "Aula 05 — Arquiteturas de referência e blueprints"
public_title: "Módulo 2 — Aula 05 — Arquiteturas de referência e blueprints"
description: O que são arquiteturas de referência, blueprints, padrões de desenho e landing zones, como adaptar referências públicas ao contexto da organização e como mantê-las vivas.
domain: enterprise-architecture
tier: professional
status: published
prerequisites: [M02-L03, M02-L04]
objectives:
  - Diferenciar arquitetura de referência, blueprint, padrão de desenho e landing zone.
  - Avaliar a adequação de uma referência pública ao contexto de uma organização.
  - Estruturar uma arquitetura de referência interna, com escopo, componentes, decisões e variações.
  - Definir o ciclo de vida e os indicadores de uso de uma referência.
minutes: 60
sources: [AWS-SRA, MS-MCRA, NIST-SP800-207, AWS-WA-SECURITY-DESIGN]
further_reading: [NIST-SP800-207, GCP-ENTERPRISE-FOUNDATIONS, AZURE-WAF-SECURITY-CHECKLIST]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M02
---

# Aula 05 — Arquiteturas de referência e blueprints { #arquiteturas-de-referencia-e-blueprints }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 2 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M02-L05</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Arquiteturas de referência são a forma mais eficaz de escalar o trabalho de um arquiteto: uma boa referência responde de antemão às perguntas que cada projeto faria. Mas referências públicas foram desenhadas para um contexto que não é o seu. Esta aula mostra como usar referências externas como matéria-prima, construir referências internas e mantê-las úteis ao longo do tempo.

**Pré-requisitos:** [Arquitetura conceitual, lógica e física](03-conceptual-logical-physical.md) e [Princípios, padrões, baselines e exceções](04-principles-standards-baselines-exceptions.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Diferenciar arquitetura de referência, blueprint, padrão de desenho e landing zone.
- Avaliar a adequação de uma referência pública ao contexto de uma organização.
- Estruturar uma arquitetura de referência interna, com escopo, componentes, decisões e variações.
- Definir o ciclo de vida e os indicadores de uso de uma referência.

## Conceito

### O que são

| Termo | O que é | Granularidade | Exemplo |
|:---|:---|:---|:---|
| **Padrão de desenho** (pattern) | Solução reutilizável para um problema recorrente e delimitado | Pequena | "Ponto único de acesso administrativo com elevação just-in-time" |
| **Arquitetura de referência** | Arquitetura genérica para uma classe de problemas, combinando princípios, padrões e componentes | Média a grande | "Integração segura com SaaS", "API exposta a parceiros" |
| **Blueprint** | Desenho prescritivo e implementável derivado de uma referência, frequentemente acompanhado de código | Específica | Módulo de infraestrutura como código que cria um ambiente de API conforme a referência |
| **Landing zone** | Blueprint de plataforma cloud: estrutura de contas ou assinaturas, identidade, rede, logs e guardrails | Plataforma | Estrutura multi-account com contas de log e segurança separadas |

A diferença essencial entre referência e blueprint é o **grau de prescrição**. A referência diz *o que deve existir e por quê*; o blueprint diz *exatamente como construir*, para um contexto.

### Por que existem

Referências existem porque a maior parte dos problemas de arquitetura **se repete**. Toda organização expõe APIs, integra SaaS, recebe acesso remoto, administra servidores. Responder a essas perguntas uma vez, bem, e reutilizar a resposta:

- reduz o custo e o prazo de cada projeto;
- aumenta a consistência — e com ela a capacidade de operar e auditar;
- concentra a atenção do arquiteto no que é realmente novo, viabilizando o modelo de autoatendimento visto na [aula 01](01-security-architect-role.md#como-especificar-e-implementar).

### Referências externas

Provedores, organismos de padronização e comunidades publicam referências que servem de ponto de partida. Exemplos verificados:

- **AWS Security Reference Architecture (AWS SRA):** diretrizes para implantar os serviços de segurança da AWS em um ambiente multi-account, com um diagrama de página única que mostra onde cada serviço deve ser implantado e como eles interagem. O próprio documento afirma que é uma referência, não uma prescrição, e que deve ser adaptada a cada ambiente.
- **Microsoft Cybersecurity Reference Architectures (MCRA):** conjunto de diagramas, antipadrões e boas práticas de segurança baseados em Zero Trust, cobrindo ambientes híbridos, multicloud, OT e IA; distribuído como apresentação.
- **NIST SP 800-207:** descreve componentes lógicos de uma arquitetura Zero Trust e modelos de implantação, de forma neutra em relação a fornecedores.

### Qual problema a adaptação resolve

Referências externas foram desenhadas para um **contexto genérico** — ou para o ecossistema de um fornecedor. Copiá-las sem adaptação produz arquiteturas grandes demais (todos os serviços de um provedor, em uma empresa com três sistemas), dependentes de um fornecedor sem decisão consciente, ou incompatíveis com restrições locais (regulação, equipe, orçamento). A adaptação transforma uma referência externa em uma **referência interna**, que incorpora os princípios, padrões e restrições da organização.

## Fundamentos técnicos

### Da referência externa à solução

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l05-reference-chain.mmd"
```

<figcaption>Figura 1 — Da referência externa à solução implantada.</figcaption>
</figure>

### Anatomia de uma arquitetura de referência interna

Uma referência interna útil contém, no mínimo:

| Seção | Conteúdo |
|:---|:---|
| **Escopo e problema** | Que classe de soluções cobre — e quais não cobre |
| **Princípios e padrões aplicados** | Quais princípios e padrões corporativos a referência materializa |
| **Visões** | Conceitual e lógica obrigatórias; física quando houver blueprint |
| **Componentes e serviços de segurança** | O que é obrigatório e o que é opcional |
| **Decisões já tomadas** | ADRs que as soluções herdam sem rediscutir |
| **Pontos de variação** | O que cada solução pode — e deve — decidir |
| **Requisitos de verificação** | Como comprovar que uma solução segue a referência |
| **Blueprints associados** | Implementações por ambiente, quando existirem |
| **Dono, versão e status** | Quem mantém, versão vigente, data de revisão |

Os **pontos de variação** são o que diferencia uma referência útil de uma rígida. Exemplo: uma referência de API para parceiros pode fixar a autenticação (OAuth 2.0 com credenciais de cliente) e deixar como ponto de variação o limite de requisições, que depende do produto.

### Como avaliar a adequação de uma referência externa

Antes de adotar uma referência pública, responda:

1. **Problema:** ela resolve a mesma classe de problema que a organização tem?
2. **Escala:** foi desenhada para uma organização de porte e complexidade semelhantes?
3. **Fornecedor:** depende de um ecossistema específico? Essa dependência é desejada?
4. **Restrições:** é compatível com a regulação, o orçamento e a capacidade da equipe?
5. **Atualidade:** está mantida? Qual a data da versão?
6. **Lacunas:** o que ela não cobre e precisará ser complementado?

### Ciclo de vida

Referências envelhecem. Um ciclo de vida mínimo:

| Estado | Significado |
|:---|:---|
| Proposta | Em elaboração, ainda não recomendada |
| Vigente | Recomendada para novas soluções |
| Em transição | Substituída por nova versão; soluções existentes migram conforme o plano |
| Descontinuada | Não usar em novas soluções |

Toda referência vigente precisa de **dono**, **data de próxima revisão** e **indicador de uso**.

## Exemplo empresarial

!!! example "Grupo Horizonte — referência para integração com SaaS"

    Em um ano, as quatro subsidiárias do Grupo Horizonte contrataram onze aplicações SaaS. Cada uma foi integrada de forma diferente: três com contas locais, duas com login federado sem provisionamento automático, uma com uma conta administrativa compartilhada. Quando um gerente de logística foi desligado, sua conta continuou ativa em quatro aplicações por mais de dois meses.

    O arquiteto de segurança do grupo criou a referência interna **RA-003 — Integração segura com SaaS**:

    ```mermaid
    --8<-- "assets/diagrams/m02-l05-saas-ra.mmd"
    ```

    | Elemento | Decisão |
    |:---|:---|
    | Obrigatório | Login federado no provedor central com MFA; provisionamento e desprovisionamento automáticos (SCIM) quando suportados; logs de auditoria no SIEM; avaliação de terceiros antes da contratação |
    | Pontos de variação | Protocolo de federação (SAML ou OIDC), conforme o suporte do SaaS; retenção de logs, conforme a classificação dos dados |
    | Desvio comum previsto | SaaS sem SCIM: revisão de acessos mensal pelo dono da aplicação como compensatório |
    | Verificação | Checklist de integração de quatro itens, preenchido antes da entrada em produção |

    Seis meses depois, as onze aplicações estavam na referência, e o tempo médio entre desligamento e remoção de acesso nas aplicações com SCIM caiu de semanas para horas.

## Arquitetura tradicional versus recomendada

| Aspecto | Tradicional | Recomendado |
|:---|:---|:---|
| Uso de referências externas | Copiadas integralmente, ou ignoradas | Avaliadas e adaptadas em referências internas |
| Cada projeto | Desenha do zero | Parte de uma referência e decide apenas os pontos de variação |
| Revisão de segurança | Revisão completa a cada projeto | Verificação de aderência à referência; revisão completa apenas para desvios |
| Manutenção | Diagramas criados uma vez | Referências com dono, versão e ciclo de vida |

## Controles e padrões relevantes

| Elemento | Objetivo | Referência |
|:---|:---|:---|
| Referência multi-account de serviços de segurança | Posicionar serviços de segurança em uma estrutura de contas | AWS SRA |
| Diagramas de capacidades e antipadrões Zero Trust | Orientar arquiteturas de segurança corporativas | Microsoft MCRA |
| Modelos de implantação Zero Trust | Referência neutra de componentes lógicos | NIST SP 800-207 |
| Segurança em todas as camadas | Garantir que a referência cubra identidade, rede, workload e dados | AWS Well-Architected, princípio *Apply security at all layers* |

## Aplicabilidade: on-premises, cloud e híbrido

| Aspecto | On-premises | Cloud | Híbrido |
|:---|:---|:---|:---|
| Referência típica | Zonas de rede (borda, aplicação, dados, gestão) e acesso administrativo | Landing zone multi-account ou multi-assinatura | Conectividade hub-and-spoke, identidade federada, observabilidade centralizada |
| Forma do blueprint | Documentos de configuração, templates de VM | Infraestrutura como código, políticas de organização | Ambos, com contratos claros de integração |
| Fonte externa útil | Benchmarks e guias de hardening | Referências dos provedores (por exemplo, AWS SRA) | Referências que tratam explicitamente de integração (por exemplo, MCRA cobre ambientes híbridos) |
| Risco específico | Referência desatualizada em relação ao ambiente | Referência do provedor adotada sem considerar escala e custo | Duas referências independentes, uma por ambiente, sem tratar as integrações |
| Responsabilidade | Infraestrutura e segurança | Equipe de plataforma cloud | Precisa de um dono para a referência de integração |

**Particularidade do híbrido:** referências de provedores cloud costumam tratar o datacenter como "rede externa conectada". Em uma empresa híbrida, a referência interna precisa descrever o **contrato entre os ambientes**: quais identidades cruzam, quais fluxos de rede são permitidos, onde os logs convergem e quem opera cada lado.

## Como especificar e implementar

1. **Escolha as referências pelo volume e pelo risco.** Comece pelas classes de solução mais frequentes e de maior risco (API externa, integração SaaS, acesso administrativo, landing zone).
2. **Use referências externas como matéria-prima.** Registre de onde veio cada decisão e o que foi adaptado.
3. **Escreva primeiro as visões conceitual e lógica.** O blueprint físico vem depois, por ambiente.
4. **Declare os pontos de variação.** O que a solução decide e o que herda.
5. **Implemente blueprints como código** quando o ambiente permitir — a referência passa a ser testável.
6. **Publique com checklist de verificação** para o autoatendimento.
7. **Meça o uso** e revise a referência quando os desvios se acumularem.

## Trade-offs, limitações e antipadrões

| Antipadrão | Sintoma | Correção |
|:---|:---|:---|
| Cópia integral da referência do fornecedor | Dezenas de serviços ativados em uma organização pequena; custo alto e alertas sem dono | Selecionar componentes pelo risco e pela capacidade de operar |
| Referência genérica demais | "Use autenticação forte e monitore tudo" | Decisões explícitas e pontos de variação definidos |
| Referência rígida demais | Toda solução precisa de exceção | Mover detalhes para pontos de variação |
| Referência órfã | Ninguém atualiza; diverge do ambiente | Dono, versão e revisão periódica |
| Lock-in não declarado | A referência só funciona com um fornecedor, sem que isso tenha sido decidido | Separar visão lógica (neutra) do blueprint (específico) e registrar a escolha em ADR |

## Como validar

| Indicador | O que mostra |
|:---|:---|
| % de novas soluções que partem de uma referência | Utilidade e alcance das referências |
| Desvios por referência | Rigidez ou desatualização |
| Tempo de revisão para soluções aderentes versus não aderentes | Ganho de produtividade |
| Achados de segurança em soluções aderentes | Qualidade da referência |
| Referências com revisão vencida | Saúde do ciclo de vida |

Blueprints em código permitem uma verificação adicional: **testes automatizados** que confirmam que o ambiente criado atende aos requisitos da referência.

## Como apresentar e justificar

- **Para a diretoria:** "Onze aplicações SaaS foram integradas de onze formas. A referência única reduz o risco de acessos órfãos de ex-funcionários, que hoje persistem por semanas, e acelera novas contratações."
- **Para arquitetos de soluções:** "Vocês herdam as decisões de autenticação, provisionamento e logs. Precisam decidir apenas o protocolo de federação e a retenção."
- **Para fornecedores e compras:** "O suporte a SSO e SCIM passa a ser requisito de contratação; a ausência exige exceção com compensatório."

## Checklist de revisão arquitetural

- [ ] A referência declara escopo, problema e o que não cobre.
- [ ] Indica os princípios e padrões corporativos que materializa.
- [ ] Tem visões conceitual e lógica; blueprints físicos por ambiente quando aplicável.
- [ ] Distingue componentes obrigatórios, opcionais e pontos de variação.
- [ ] Registra as decisões herdadas em ADRs.
- [ ] Indica de onde vieram as decisões adaptadas de referências externas.
- [ ] Tem dono, versão, status e data de próxima revisão.
- [ ] Possui checklist de verificação para autoatendimento.

## Questões de compreensão

**1.** Qual é a diferença essencial entre uma arquitetura de referência e um blueprint?

??? success "Resposta comentada"

    O grau de prescrição. A referência descreve o que deve existir e por quê, de forma reutilizável para uma classe de problemas, geralmente nas visões conceitual e lógica. O blueprint é a realização prescritiva e implementável para um contexto específico, frequentemente como código.

**2.** Uma empresa com 30 funcionários decide implantar integralmente uma referência de segurança multi-account de um provedor cloud. Quais riscos essa decisão traz?

??? success "Resposta comentada"

    A referência foi desenhada para organizações com mais contas, equipes e capacidade operacional. Implantar tudo pode gerar custo alto, volume de alertas que ninguém trata e uma estrutura que a equipe não consegue operar — o que pode reduzir a segurança efetiva. O correto é adotar o núcleo proporcional ao risco (por exemplo, separação de contas de logs e de workloads, guardrails essenciais) e crescer conforme a necessidade.

**3.** Por que os pontos de variação são importantes em uma referência interna?

??? success "Resposta comentada"

    Porque deixam claro o que cada solução pode decidir sem exceção. Sem eles, a referência é rígida (toda diferença vira exceção) ou vaga (tudo é negociável). Pontos de variação bem definidos tornam a referência aplicável a mais casos e reduzem o trabalho de revisão.

**4.** Em um ambiente híbrido, o que uma referência interna precisa descrever que referências de provedores cloud normalmente não descrevem?

??? success "Resposta comentada"

    O **contrato entre ambientes**: identidades que cruzam, fluxos de rede permitidos entre datacenter e cloud, onde os logs convergem e quem opera cada lado da integração. Referências de provedores tendem a tratar o datacenter como uma rede externa conectada.

## Exercício de tomada de decisão

!!! question "Cenário: a primeira landing zone do Grupo Horizonte"

    As quatro subsidiárias do Grupo Horizonte começarão a usar AWS no próximo ano. A equipe central de plataforma tem quatro pessoas. As alternativas:

    - **A — Adotar a AWS SRA integralmente** como referência e implantar todos os serviços de segurança descritos.
    - **B — Referência interna derivada:** usar a AWS SRA e o MCRA como matéria-prima, adotar o núcleo (estrutura de contas com separação de logs, segurança e workloads; identidade federada ao provedor central do grupo; guardrails essenciais) e planejar a ampliação em fases.
    - **C — Autonomia por subsidiária:** cada subsidiária cria sua própria estrutura, seguindo apenas os padrões corporativos já existentes.

    Critérios: redução de risco, capacidade de operação pela equipe de quatro pessoas, consistência no grupo e custo.

??? success "Resolução de referência"

    | Critério | Peso | A — SRA integral | B — Referência derivada | C — Autonomia |
    |:---|:---|:---|:---|:---|
    | Redução de risco | 3 | 3 | 3 | 1 |
    | Capacidade de operação | 3 | 1 | 3 | 2 |
    | Consistência no grupo | 2 | 3 | 3 | 1 |
    | Custo | 1 | 1 | 2 | 2 |
    | **Total ponderado** | | **19** | **26** | **13** |

    **Recomendação: B.** A alternativa A tem o mesmo potencial de redução de risco, mas uma equipe de quatro pessoas dificilmente conseguiria operar todos os serviços e tratar seus alertas — e controle sem operação gera falsa sensação de segurança. A alternativa C repete o problema que o grupo já viveu com SaaS: quatro estruturas diferentes, sem visão consolidada.

    **Condições:** registrar em ADR quais componentes da AWS SRA foram adotados, adiados e por quê; definir os gatilhos para as próximas fases (por exemplo, entrada de dados de saúde ou de cartão em produção).

    **Risco residual:** capacidades adiadas, como detecção em todas as contas desde o primeiro dia. Deve ser aceito formalmente e revisto a cada fase.

## Pontos-chave

- Padrão de desenho, arquitetura de referência, blueprint e landing zone diferem em granularidade e grau de prescrição.
- Referências externas são matéria-prima: avalie problema, escala, fornecedor, restrições, atualidade e lacunas.
- Uma boa referência interna declara o que é obrigatório, o que é opcional e quais são os pontos de variação.
- Referências precisam de dono, versão, ciclo de vida e indicadores de uso.
- Em ambientes híbridos, a referência precisa descrever o contrato entre os ambientes.

## Referências

- AWS. *AWS Security Reference Architecture (AWS SRA)*. Prescriptive Guidance, setembro de 2023 (documento vivo). <https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html> — gratuito.
- Microsoft. *Microsoft Cybersecurity Reference Architectures (MCRA)*. Abril de 2025. <https://learn.microsoft.com/en-us/security/adoption/mcra> — gratuito.
- NIST. *SP 800-207 — Zero Trust Architecture*. 2020. <https://csrc.nist.gov/news/2020/zero-trust-architecture-nist-publishes-sp-800-207> — gratuito.
- AWS. *Well-Architected Framework — Security Pillar: Design principles*. <https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html> — gratuito.

### Leituras de aprofundamento

Incluídas na revisão bibliográfica de 2026-10-23, **depois** da escrita desta aula: complementam e permitem conferir o conteúdo, mas não foram a base original do texto. A situação de cada leitura está entre parênteses.

- NIST. *SP 800-207 — Zero Trust Architecture*, 2020, §3 *Logical Components* (p. 9) e §3.2 *Deployed Variations of the Abstract Architecture* (p. 13). *(localizado pelo sumário.)*
- Google Cloud. *Enterprise foundations blueprint* — exemplo de referência implantável por Terraform. <https://docs.cloud.google.com/architecture/blueprints/security-foundations>. *(conferido.)*
- Microsoft. *Azure Well-Architected — Security design review checklist* (SE:01–SE:12). <https://learn.microsoft.com/en-us/azure/well-architected/security/checklist>. *(conferido.)*

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
| Revisão bibliográfica | 2026-10-23 — [registro da revisão retroativa](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/retroactive-review-m02.md) |
