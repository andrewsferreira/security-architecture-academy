---
id: M02-L03
title: "Aula 03 — Arquitetura conceitual, lógica e física"
public_title: "Módulo 2 — Aula 03 — Arquitetura conceitual, lógica e física"
description: Como representar uma solução em três níveis de abstração, manter a rastreabilidade entre eles e usar a visão lógica para unificar ambientes on-premises, cloud e híbridos.
domain: enterprise-architecture
tier: professional
status: published
prerequisites: [M02-L02, M00-L07]
objectives:
  - Diferenciar arquitetura conceitual, lógica e física pelo tipo de decisão que cada uma registra.
  - Representar uma mesma solução nos três níveis sem misturar abstrações.
  - Manter rastreabilidade entre serviços conceituais, componentes lógicos e elementos físicos.
  - Usar uma única arquitetura lógica para orientar realizações físicas distintas em ambientes híbridos.
minutes: 75
sources: [ISO-42010-2022, AWS-WA-SECURITY-DESIGN, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [BOOK-ANDERSON-SE3, SABSA-W100, SABSA-W101, BOOK-GOOGLE-BSRS]
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
module: M02
---

# Aula 03 — Arquitetura conceitual, lógica e física { #arquitetura-conceitual-logica-e-fisica }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 2 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M02-L03</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    A mesma solução pode ser descrita como "administradores acessam o ambiente de pagamentos por um serviço controlado", como "um broker PAM concede elevação just-in-time e abre sessões por um bastion gravado" ou como "a VM bastion na VLAN 140 alcança a zona PCI pela porta 22". As três frases estão certas — e respondem a perguntas diferentes. Esta aula ensina a separar esses níveis, conectá-los e usar a separação como ferramenta, especialmente em ambientes híbridos.

**Pré-requisitos:** [Enterprise, Solution e Security Architecture](02-enterprise-solution-security-architecture.md) e leitura de diagramas (Módulo Inicial — Aula 07).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Diferenciar arquitetura conceitual, lógica e física pelo tipo de decisão que cada uma registra.
- Representar uma mesma solução nos três níveis sem misturar abstrações.
- Manter rastreabilidade entre serviços conceituais, componentes lógicos e elementos físicos.
- Usar uma única arquitetura lógica para orientar realizações físicas distintas em ambientes híbridos.

## Conceito

### O que são os níveis de abstração

Níveis de abstração são **camadas de descrição** da mesma solução, cada uma com um grau diferente de detalhe e um tipo diferente de decisão:

| Nível | Pergunta que responde | Tipo de decisão | Exemplo |
|:---|:---|:---|:---|
| **Conceitual** | *O quê e por quê?* | Quais capacidades, zonas, atores e serviços existem | "Todo acesso administrativo passa por um serviço controlado e auditado." |
| **Lógico** | *Como, independentemente de produto?* | Que tipos de componentes, padrões, protocolos e interfaces | "Broker PAM com elevação just-in-time, bastion único, autenticação OIDC com MFA resistente a phishing." |
| **Físico** | *Com quê e onde, exatamente?* | Que produtos, versões, configurações, endereços e topologia | "Bastion em duas VMs na VLAN de gestão; na AWS, Systems Manager Session Manager." |

### Por que os níveis existem

Os níveis existem porque **stakeholders diferentes têm preocupações diferentes** e porque **decisões diferentes mudam em ritmos diferentes**:

- Um diretor precisa saber se todo acesso administrativo é controlado e auditado — não qual produto faz isso.
- Um arquiteto precisa garantir que o padrão escolhido resolve o risco — independentemente do fornecedor.
- Um engenheiro precisa saber exatamente o que configurar.

E a velocidade de mudança é diferente: a decisão conceitual ("acesso administrativo controlado") dura anos; a lógica ("bastion + PAM just-in-time"), alguns anos; a física (produto, versão, endereço), meses.

### Qual problema os níveis resolvem

Sem a separação, aparecem três problemas recorrentes:

1. **Escolha prematura de produto.** A discussão começa por "qual ferramenta compramos?" antes de alguém concordar sobre o que precisa ser resolvido.
2. **Diagramas ilegíveis.** Um único diagrama tenta mostrar capacidades de negócio, protocolos e endereços IP — e não serve a ninguém.
3. **Arquitetura presa à implementação.** Quando o produto muda, a "arquitetura" inteira precisa ser refeita, porque ninguém registrou o padrão lógico que o produto realizava.

### Arquitetura versus implementação

Esta é a aula principal do currículo para a distinção **arquitetura × implementação**. A arquitetura está nos níveis conceitual e lógico, e nas decisões físicas *estruturais* (topologia, fronteiras, alta disponibilidade). A implementação é a configuração concreta que realiza essas decisões. Uma regra prática: **se a mudança de um detalhe exige rever o raciocínio de risco, ele é arquitetura; se não exige, é implementação.**

## Fundamentos técnicos

### O que cada nível contém

| Elemento | Conceitual | Lógico | Físico |
|:---|:---|:---|:---|
| Atores | Papéis de negócio (administrador, cliente, parceiro) | Tipos de identidade (humana, workload, privilegiada) | Contas, grupos e papéis concretos |
| Zonas | Zonas de confiança nomeadas pelo propósito | Zonas com política de comunicação entre elas | VLANs, VPCs, subnets, contas, assinaturas |
| Componentes | Serviços e capacidades | Tipos de componente e padrões (IdP, PEP, broker, gateway) | Produtos, versões, instâncias |
| Fluxos | Quem troca informação com quem | Protocolos, direção, autenticação, criptografia, classificação | Portas, endereços, certificados, rotas |
| Controles | Objetivos de controle | Mecanismos de controle | Configurações e parâmetros |
| Resiliência | Requisito de disponibilidade | Padrão de redundância | Quantidade de instâncias, zonas de disponibilidade |

### Rastreabilidade entre os níveis

Cada elemento físico deve **realizar** um componente lógico, que por sua vez **implementa** um serviço conceitual. Essa cadeia é o que permite responder, em uma auditoria ou incidente, *por que* um componente existe e *o que* deixaria de ser protegido se ele fosse removido.

| Serviço conceitual | Componente lógico | Elemento físico — acesso ao datacenter | Elemento físico — acesso à AWS |
|:---|:---|:---|:---|
| Verificação de identidade | IdP com OIDC e MFA resistente a phishing | Microsoft Entra ID federado ao AD | O mesmo |
| Acesso administrativo controlado | Broker PAM com elevação just-in-time | Broker PAM em cluster | O mesmo |
| Acesso administrativo controlado | Ponto único de acesso administrativo | VM bastion na VLAN de gestão | Systems Manager Session Manager |
| Auditoria de sessões | Gravação de sessões e envio de eventos | Gravação do broker + syslog para o SIEM | Logs de sessão no CloudWatch Logs + CloudTrail para o SIEM |

Repare na terceira linha: **o mesmo componente lógico tem duas realizações físicas**. Isso é desejável — desde que ambas atendam aos mesmos requisitos.

### Relação com frameworks

Vários frameworks usam níveis de abstração semelhantes, com nomes e quantidades diferentes. O SABSA, por exemplo, organiza a arquitetura em camadas que vão do contexto de negócio (*contextual*) até componentes e operação, passando por *conceptual*, *logical* e *physical* — aprofundado na [aula 06](06-frameworks.md) e no Módulo 16. O importante não é o nome das camadas, mas **não misturar tipos de decisão em uma mesma visão**.

### As-Is e To-Be em cada nível

A comparação entre o estado atual (**As-Is**) e o estado-alvo (**To-Be**) pode — e deve — ser feita no nível adequado:

- **Lacuna conceitual:** "não existe serviço de auditoria de sessões administrativas". Exige nova capacidade.
- **Lacuna lógica:** "existe acesso administrativo, mas sem elevação just-in-time". Exige mudar o padrão.
- **Lacuna física:** "o bastion existe, mas está em uma única VM". Exige mudar a implementação.

Classificar as lacunas pelo nível ajuda a estimar esforço e a escolher quem decide: lacunas conceituais costumam exigir orçamento e patrocínio; lacunas físicas, apenas engenharia.

## Exemplo empresarial

!!! example "Aurora Pagamentos — acesso administrativo ao ambiente de pagamentos"

    O auditor PCI apontou que administradores acessavam servidores de pagamento diretamente das estações de trabalho, com contas pessoais permanentemente privilegiadas. A Aurora decidiu redesenhar o acesso administrativo, que agora precisa cobrir o datacenter e os novos workloads na AWS.

### Visão conceitual

Para a diretoria e o auditor: quais capacidades existem e onde estão as fronteiras.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l03-conceptual.mmd"
```

<figcaption>Figura 1 — Visão conceitual do acesso administrativo da Aurora Pagamentos.</figcaption>
</figure>

### Visão lógica

Para arquitetos e segurança: padrões, protocolos e mecanismos, sem produtos.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l03-logical.mmd"
```

<figcaption>Figura 2 — Visão lógica do acesso administrativo da Aurora Pagamentos.</figcaption>
</figure>

### Visão física

Para engenharia e operação: produtos, topologia e realização em cada ambiente.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l03-physical.mmd"
```

<figcaption>Figura 3 — Visão física híbrida do acesso administrativo da Aurora Pagamentos.</figcaption>
</figure>

A visão física revela uma decisão importante que não aparece nas outras: na AWS, não há uma "VM bastion". O Session Manager cumpre o papel lógico de **ponto único de acesso administrativo** sem expor portas de entrada nas instâncias — o que é, inclusive, mais restritivo do que o equivalente no datacenter.

## Arquitetura tradicional versus recomendada

| Aspecto | Tradicional: um diagrama para tudo | Recomendado: visões por nível |
|:---|:---|:---|
| Ponto de partida | Produtos e topologia | Serviços e requisitos |
| Diagrama | Mistura capacidades, produtos, IPs e portas | Uma visão por público, com rastreabilidade entre elas |
| Mudança de produto | Redesenho completo | Atualiza apenas a visão física |
| Ambiente híbrido | Dois desenhos sem relação (datacenter e cloud) | Uma visão lógica, duas realizações físicas |
| Revisão de segurança | Discute portas antes de discutir fronteiras | Valida primeiro zonas e fluxos, depois configuração |

## Controles e padrões relevantes

| Objetivo (conceitual) | Mecanismo (lógico) | Referência |
|:---|:---|:---|
| Acesso administrativo controlado | Ponto único de acesso, elevação just-in-time | NIST SP 800-53 Rev. 5: AC-6 (Least Privilege), AC-17 (Remote Access) |
| Autenticação forte | MFA resistente a phishing | NIST SP 800-53 Rev. 5: IA-2 (Identification and Authentication) |
| Rastreabilidade | Gravação de sessão e geração de registros de auditoria | NIST SP 800-53 Rev. 5: AU-12 (Audit Record Generation) |
| Gestão de contas privilegiadas | Contas administrativas separadas e temporárias | CIS Controls v8.1: Controles 5 e 6 |
| Segurança em todas as camadas | Controles na identidade, na rede e no host | AWS Well-Architected, princípio *Apply security at all layers* |

## Aplicabilidade: on-premises, cloud e híbrido

A visão lógica é a **ferramenta central da arquitetura híbrida**: ela fixa os requisitos, e cada ambiente escolhe a realização física mais adequada.

| Aspecto | On-premises | Cloud | Híbrido |
|:---|:---|:---|:---|
| Realização típica do ponto único de acesso | Bastion em VM em zona de gestão | Serviço gerenciado de sessão (por exemplo, AWS Systems Manager Session Manager ou Azure Bastion) | Uma realização por ambiente, sob o mesmo componente lógico |
| Onde as fronteiras se materializam | VLANs e firewalls | Contas, VPCs, security groups e políticas de IAM | Os dois, mais a conectividade entre eles |
| Dependências | Disponibilidade do datacenter | Disponibilidade do provedor e do plano de controle | Conectividade entre ambientes e federação de identidade |
| Responsabilidade | Organização opera tudo | Provedor opera o serviço; organização configura e monitora | Fronteira de responsabilidade diferente para cada realização |
| Risco específico | Bastion como alvo de alto valor | Permissões de IAM que permitem iniciar sessões de forma ampla | Realizações com níveis de controle diferentes — o mais fraco define o risco |
| Trade-off | Controle total, maior esforço operacional | Menos operação, dependência do provedor | Consistência de requisitos com diversidade de implementação |

**Regra para ambientes híbridos:** quando duas realizações físicas coexistem, a revisão deve verificar se ambas atendem a **todos** os requisitos do componente lógico. No exemplo, se o bastion do datacenter grava sessões e o Session Manager não estiver configurado para registrá-las, o requisito de auditoria fica atendido em um ambiente e violado no outro.

## Como especificar e implementar

### O que documentar em cada nível

**Conceitual**

- [ ] Atores e seus papéis
- [ ] Zonas de confiança nomeadas pelo propósito
- [ ] Serviços e capacidades de segurança envolvidos
- [ ] Fluxos principais, sem protocolos
- [ ] Objetivos de segurança da solução

**Lógico**

- [ ] Tipos de componentes e padrões adotados
- [ ] Política de comunicação entre zonas
- [ ] Protocolos, autenticação e criptografia em cada fluxo
- [ ] Classificação dos dados em cada fluxo
- [ ] Serviços de segurança corporativos consumidos
- [ ] Requisitos de disponibilidade e padrão de redundância

**Físico**

- [ ] Produtos e versões
- [ ] Topologia e localização (datacenter, região, conta, assinatura)
- [ ] Endereçamento e regras de filtragem estruturais
- [ ] Quantidade de instâncias e distribuição para alta disponibilidade
- [ ] Integrações de logs e monitoramento

### Convenções de diagrama

- Indique o nível no título do diagrama: "Visão lógica — acesso administrativo".
- Não use nomes de produtos na visão conceitual nem endereços na visão lógica.
- Use os mesmos nomes de zonas nos três níveis, para que a rastreabilidade seja visual.
- Mantenha os diagramas como código, versionados junto com os ADRs — o [Laboratório 02](../../labs/lab-02-architecture-modeling.md) pratica exatamente isso.

## Trade-offs, limitações e antipadrões

- **Custo de manter três visões.** Para soluções pequenas e de baixo risco, uma visão lógica com anotações físicas costuma bastar. Os três níveis completos se justificam em soluções de alto risco, plataformas compartilhadas e ambientes híbridos.
- **Desatualização (diagram drift).** Visões físicas envelhecem rápido. Prefira gerar a visão física a partir do ambiente real ou de infraestrutura como código, e manter manualmente apenas as visões conceitual e lógica.
- **Antipadrão — lógica disfarçada de física:** "Firewall Fabricante X" na visão lógica. O correto é "inspeção de tráfego L7 na borda".
- **Antipadrão — conceitual vazio:** uma visão conceitual com um único bloco "Segurança". Ela precisa mostrar zonas, atores e serviços.
- **Antipadrão — pular o lógico:** ir do conceitual direto aos produtos. É exatamente nesse salto que se perde a capacidade de comparar alternativas.

## Como validar

| Verificação | Como fazer |
|:---|:---|
| Rastreabilidade completa | Todo elemento físico aponta para um componente lógico, e todo componente lógico para um serviço conceitual. |
| Ausência de elementos órfãos | Não há componente sem justificativa nem serviço conceitual sem realização. |
| Equivalência entre realizações | Em ambientes híbridos, cada realização física atende a todos os requisitos do componente lógico. |
| Aderência ao ambiente real | A visão física corresponde à configuração efetiva (inspeção de configuração, inventário, IaC). |
| Separação de níveis | Nenhum produto na visão conceitual; nenhum endereço na visão lógica. |

## Como apresentar e justificar

- **Diretoria e auditoria — visão conceitual:** "Todo acesso administrativo ao ambiente de pagamentos passa agora por um único serviço, que confirma a identidade, concede acesso por tempo limitado e grava a sessão. Isso fecha o apontamento da auditoria."
- **Arquitetura e segurança — visão lógica:** "Adotamos elevação just-in-time com aprovação e um ponto único de acesso. A autenticação é resistente a phishing; todos os eventos chegam ao SIEM."
- **Engenharia — visão física:** "No datacenter, duas VMs bastion na VLAN de gestão; na AWS, Session Manager com logs no CloudWatch Logs. As regras do firewall interno passam a permitir SSH para a zona PCI apenas a partir do bastion."

## Checklist de revisão arquitetural

- [ ] A solução possui visões nos níveis adequados ao seu risco.
- [ ] Cada visão declara seu nível e seu público.
- [ ] Há rastreabilidade entre serviços, componentes lógicos e elementos físicos.
- [ ] As zonas de confiança têm os mesmos nomes em todos os níveis.
- [ ] Em ambientes híbridos, todas as realizações físicas atendem aos mesmos requisitos lógicos.
- [ ] A visão física foi conferida contra o ambiente real ou o código de infraestrutura.
- [ ] As lacunas As-Is/To-Be estão classificadas por nível.

## Questões de compreensão

**1.** Classifique cada afirmação como conceitual, lógica ou física: (a) "O tráfego entre a zona de aplicação e a zona de dados usa TLS mútuo." (b) "Clientes acessam o extrato por um canal digital autenticado." (c) "O balanceador está em três zonas de disponibilidade na região sa-east-1."

??? success "Resposta comentada"

    (a) **Lógica** — define o mecanismo (TLS mútuo) sem produto. (b) **Conceitual** — define ator, serviço e objetivo. (c) **Física** — define topologia e localização concretas.

**2.** Por que a visão lógica é especialmente importante em ambientes híbridos?

??? success "Resposta comentada"

    Porque ela fixa os requisitos de forma independente de produto, permitindo que cada ambiente use a realização física mais adequada — bastion no datacenter, serviço gerenciado na cloud — sem perder a garantia de que ambos cumprem os mesmos requisitos. Sem ela, cada ambiente tende a ter sua própria "arquitetura" e o nível de proteção diverge.

**3.** Um projeto apresenta um único diagrama com o nome de todos os produtos, endereços IP e as capacidades de negócio atendidas. Que problemas esse diagrama causa?

??? success "Resposta comentada"

    Ele mistura níveis: fica ilegível para executivos, não permite comparar alternativas de produto e envelhece rapidamente, porque qualquer mudança física exige revisá-lo. Além disso, esconde o padrão lógico — se o produto for trocado, ninguém saberá quais requisitos o substituto precisa atender.

**4.** Uma lacuna foi descrita como "não há elevação just-in-time; contas administrativas são permanentes". Em que nível ela está, e o que isso sugere sobre quem precisa decidir?

??? success "Resposta comentada"

    É uma **lacuna lógica**: o serviço de acesso administrativo existe, mas o padrão é inadequado. Ela exige decisão de arquitetura (adotar elevação just-in-time) e provavelmente investimento em uma capacidade de PAM — não apenas um ajuste de configuração. Envolve o arquiteto e o dono do orçamento de segurança, não só a engenharia.

## Exercício de tomada de decisão

!!! question "Cenário: realização física do acesso administrativo na AWS"

    A Aurora está migrando parte dos workloads de pagamento para a AWS. A visão lógica já está aprovada (IdP com MFA resistente a phishing, broker PAM just-in-time, ponto único de acesso, gravação de sessões, eventos no SIEM). Falta decidir a realização física do **ponto único de acesso** na AWS:

    - **A — Estender o bastion do datacenter:** administradores acessam as instâncias da AWS a partir do bastion existente, pela conexão privada entre o datacenter e a AWS.
    - **B — Serviço nativo de sessão:** AWS Systems Manager Session Manager, integrado ao broker PAM, com logs no CloudWatch Logs e no CloudTrail.
    - **C — Bastions dedicados na AWS:** instâncias bastion em cada conta de workload, replicando o modelo do datacenter.

    Critérios: atendimento aos requisitos lógicos, superfície de ataque, dependência de conectividade, esforço operacional e consistência de auditoria.

??? success "Resolução de referência"

    | Critério | Peso | A — Bastion do DC | B — Session Manager | C — Bastions na AWS |
    |:---|:---|:---|:---|:---|
    | Atendimento aos requisitos lógicos | 3 | 3 | 3 | 3 |
    | Superfície de ataque | 3 | 2 | 3 | 1 |
    | Dependência de conectividade | 2 | 1 | 3 | 3 |
    | Esforço operacional | 2 | 2 | 3 | 1 |
    | Consistência de auditoria entre ambientes | 1 | 3 | 2 | 3 |
    | **Total ponderado** | | **24** | **32** | **23** |

    **Recomendação: B.** Todas as alternativas podem atender aos requisitos lógicos, mas B elimina portas de entrada nas instâncias e não depende da conexão com o datacenter para administrar a AWS — o que importa justamente durante um incidente que afete essa conexão. A alternativa C multiplica alvos de alto valor; a A torna a administração da cloud refém do datacenter.

    **Condições:** registro de sessões habilitado e enviado ao SIEM; permissões para iniciar sessões concedidas apenas pelo broker PAM, por tempo limitado; o consumo de logs do Session Manager precisa ser incorporado às rotinas de auditoria.

    **Risco residual:** dois formatos de auditoria (bastion e Session Manager) exigem normalização no SIEM. Esse é o motivo do peso baixo de B em consistência — e deve ser tratado como requisito do projeto, não ignorado.

## Pontos-chave

- Conceitual responde *o quê e por quê*; lógico, *como, sem produto*; físico, *com quê e onde*.
- Separar os níveis evita escolha prematura de produto e diagramas que não servem a ninguém.
- Arquitetura é o que exige rever o raciocínio de risco quando muda; implementação é o que não exige.
- Rastreabilidade entre níveis permite explicar por que cada componente existe.
- Em ambientes híbridos, uma visão lógica pode ter várias realizações físicas — todas devem atender aos mesmos requisitos.

## Referências

- ISO/IEC/IEEE. *42010:2022 — Software, systems and enterprise — Architecture description*. 2022. <https://committee.iso.org/standard/74393.html> — norma paga, não consultada na íntegra; a descrição usada nesta aula se apoia na página oficial da norma e em resumos públicos.
- AWS. *Well-Architected Framework — Security Pillar: Design principles*. <https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html> — gratuito.
- NIST. *SP 800-53 Rev. 5 — Security and Privacy Controls* (Release 5.2.0). 2025. <https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls> — gratuito.
- CIS. *CIS Critical Security Controls v8.1*. <https://www.cisecurity.org/controls/implementation-groups> — gratuito.

### Leituras de aprofundamento

Incluídas na revisão bibliográfica de 2026-10-23, **depois** da escrita desta aula: complementam e permitem conferir o conteúdo, mas não foram a base original do texto. A situação de cada leitura está entre parênteses.

- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020, Cap. 6, §6.1–6.3 (pp. 207–231) — controle de acesso em camadas de aplicação, middleware, sistema operacional e hardware: útil para comparar realizações físicas. *(lido.)*
- SABSA. *SABSA White Paper* (W100), 2009, Table 1 (p. 9) — as seis camadas e suas visões, que confirmam a descrição desta aula. *(Lido em cópia não oficial; disponível no [catálogo oficial](https://sabsa.org/white-paper-requests/).)*
- SABSA Institute. *W101 — Architecting a Secure Digital World*, agosto de 2018 — introdução atual ao método. *(catálogo conferido; leitura pendente.)*
- H. Adkins *et al.* *Building Secure and Reliable Systems*. O'Reilly, 2020, Cap. 5 *Design for Least Privilege* — acesso administrativo com privilégio mínimo, como no exemplo da Aurora Pagamentos. *(sumário conferido; leitura pendente.)*

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
| Revisão bibliográfica | 2026-10-23 — [registro da revisão retroativa](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/retroactive-review-m02.md) |
