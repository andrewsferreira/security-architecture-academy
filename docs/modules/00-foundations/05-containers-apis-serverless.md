---
id: M00-L05
title: "Containers, Kubernetes, APIs, microsserviços e serverless"
description: Os componentes das plataformas de aplicação modernas — APIs, microsserviços, imagens e registries, Kubernetes, service mesh e serverless — e as novas fronteiras de segurança que eles criam.
domain: infrastructure-foundations
tier: fundamental
status: published
prerequisites: [M00-L01, M00-L02]
objectives:
  - Explicar o que é uma API e como microsserviços se comunicam.
  - Descrever o ciclo de uma imagem de container, do build ao registry e à execução.
  - Identificar os componentes de um cluster Kubernetes e diferenciar plano de controle e plano de dados.
  - Reconhecer o que muda na responsabilidade de segurança em plataformas serverless.
minutes: 75
sources: [NIST-SP800-190, NIST-SP800-204, K8S-SECURITY-OVERVIEW]
further_reading: [BOOK-ANDERSON-SE3, OWASP-ASVS-5]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M00
---

# Containers, Kubernetes, APIs, microsserviços e serverless

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 · M00-L05</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">75 min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Aplicações modernas raramente são um único programa em um servidor. São dezenas de serviços pequenos que conversam por APIs, empacotados em containers, orquestrados por Kubernetes e complementados por funções serverless. Esta aula explica cada peça e, principalmente, **onde estão as novas fronteiras**: o plano de controle do cluster, o registry de imagens, a comunicação entre serviços e as permissões de cada função.

**Pré-requisitos:** [Computação, SO e virtualização](01-computing-os-virtualization.md) e [Redes TCP/IP](02-tcp-ip-networking.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar o que é uma API e como microsserviços se comunicam.
- Descrever o ciclo de uma imagem de container, do build ao registry e à execução.
- Identificar os componentes de um cluster Kubernetes e diferenciar plano de controle e plano de dados.
- Reconhecer o que muda na responsabilidade de segurança em plataformas serverless.

## Conceito

### De monólitos a serviços

Um **monólito** concentra todas as funções de uma aplicação em um único programa implantado como um bloco. É simples de entender, mas difícil de escalar por partes e arriscado de atualizar: qualquer mudança exige reimplantar tudo.

**Microsserviços** dividem a aplicação em serviços pequenos, cada um responsável por uma capacidade de negócio (pedidos, pagamentos, notificações), implantado de forma independente e com seus próprios dados. Ganha-se agilidade e escala; perde-se simplicidade. Para segurança, a mudança mais importante é esta: **chamadas que antes eram internas a um processo passam a atravessar a rede**. Cada uma delas precisa de autenticação, autorização e proteção em trânsito.

### APIs

Uma **API** (*Application Programming Interface*) é o contrato pelo qual um serviço expõe funções a outros: quais operações existem, quais dados recebem e devolvem, como o chamador se identifica. Em aplicações web, predominam APIs HTTP (REST, GraphQL, gRPC). Uma API é, ao mesmo tempo, **o produto que o serviço oferece e a sua superfície de ataque**.

## Fundamentos técnicos

### Imagens, registries e execução

Um container é executado a partir de uma **imagem**: um pacote imutável com a aplicação, suas bibliotecas e configuração. O ciclo é:

1. **Build** — a imagem é construída a partir de um arquivo de definição, geralmente sobre uma imagem base pública.
2. **Registry** — a imagem é armazenada em um repositório (*registry*) de onde os hosts a baixam.
3. **Execução** — o runtime cria o container a partir da imagem.

Cada etapa é um ponto de controle: o build pode incluir dependências vulneráveis ou segredos esquecidos; o registry precisa garantir que só imagens aprovadas sejam baixadas; a execução precisa limitar privilégios. O NIST SP 800-190 organiza suas contramedidas justamente por esses componentes, em seis níveis: imagem, registry, orquestrador, container, sistema operacional do host e hardware (conforme o boletim do ITL que apresenta a publicação).

### Kubernetes

O **Kubernetes** orquestra containers em um conjunto de máquinas (*nodes*). Seus componentes se dividem em dois planos:

| Plano | Componentes | Função | Se comprometido |
|:---|:---|:---|:---|
| **Controle** | API server, etcd, scheduler, controllers | Recebe ordens, guarda o estado desejado, decide onde rodar cada carga | O atacante controla o cluster inteiro: cria cargas, lê segredos, altera permissões. |
| **Dados** | Nodes com kubelet e runtime, *pods* com os containers | Executa as cargas | O impacto depende do isolamento do pod e das permissões que ele tem. |

Conceitos que aparecem em qualquer diagrama de Kubernetes:

- **Pod** — a menor unidade implantável, com um ou mais containers.
- **Namespace** — divisão lógica do cluster, usada para separar equipes ou aplicações. Por si só, **não isola a rede**: sem *network policies*, pods de namespaces diferentes se alcançam.
- **Service e Ingress** — expõem pods dentro do cluster e para fora dele.
- **Service account** — identidade com a qual um pod chama a API do Kubernetes ou outros serviços.
- **RBAC** — define o que cada identidade pode fazer na API do cluster.
- **Secrets** — objetos para credenciais; por padrão, são apenas codificados, e sua proteção depende de cifragem em repouso e de RBAC.

A documentação do Kubernetes descreve a segurança em camadas — **Cloud, Cluster, Container e Code** — lembrando que cada camada depende da segurança da camada externa.

### Service mesh

Um **service mesh** adiciona a cada serviço um componente (normalmente um *sidecar*) que intercepta a comunicação entre serviços e aplica mTLS, autorização e telemetria de forma uniforme, sem mudar o código das aplicações. É uma forma de tratar a "rede interna" como não confiável.

### Serverless

Em **serverless** (*Functions as a Service*), o desenvolvedor entrega apenas o código de uma função; o provedor executa, escala e cobra por invocação. O cliente não gerencia servidores nem containers, mas continua responsável por:

- o código e suas dependências;
- **as permissões da função** — uma função com permissões amplas é uma credencial poderosa exposta a qualquer falha no código;
- a validação dos eventos que a acionam;
- os segredos e a configuração.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m00-l05-modern-platforms.mmd"
```

<figcaption>Figura 1 — Aplicação com API gateway, microsserviços em Kubernetes e função serverless.</figcaption>
</figure>

A figura mostra as fronteiras típicas: o **API gateway** é o ponto de entrada autenticado; o **plano de controle** do cluster é separado das cargas e precisa de proteção própria; os **namespaces** organizam os serviços, mas a comunicação entre eles precisa de política; o **registry** é parte da cadeia de confiança; a **função serverless** age com as permissões que receber.

## Exemplo empresarial

!!! example "Aurora Pagamentos — o namespace que não isolava"

    A Aurora migrou seus serviços para Kubernetes e colocou pagamentos e marketing em namespaces diferentes, acreditando que estavam isolados. Durante um teste, um pod do serviço de marketing — que processava arquivos enviados por parceiros — conseguiu chamar diretamente a API interna de pagamentos.

    A investigação mostrou dois problemas: não havia *network policies*, então qualquer pod alcançava qualquer outro; e a service account do marketing tinha permissão para listar segredos de todo o cluster.

    As correções seguiram as camadas: política de rede negando tráfego entre namespaces por padrão; RBAC com permissões mínimas por service account; mTLS entre serviços, com autorização explícita de quais serviços podem chamar pagamentos.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Comunicação entre serviços | Confiança implícita por estar "dentro do cluster" | Autenticação e autorização entre serviços (mTLS, tokens) e política de rede |
| Imagens | Qualquer imagem pública, tags `latest` | Imagens base aprovadas, varredura de vulnerabilidades, registry controlado, versões fixas |
| Plano de controle | API do cluster acessível amplamente, credenciais administrativas compartilhadas | Acesso restrito, RBAC mínimo, autenticação federada, registro de auditoria |
| Segredos | Em variáveis de ambiente ou na imagem | Em gerenciador de segredos, com cifragem e acesso por identidade |
| Funções serverless | Permissão ampla "para funcionar" | Permissões mínimas por função |

## Aplicabilidade: on-premises, cloud e híbrido

| Ambiente | O que muda |
|:---|:---|
| **On-premises** | A organização opera o plano de controle do Kubernetes, os nodes e o registry. |
| **Kubernetes gerenciado em cloud** | O provedor opera o plano de controle; o cliente configura acesso a ele, nodes (em muitos serviços), cargas, RBAC e políticas. |
| **Serverless** | O provedor opera toda a plataforma; o cliente responde por código, permissões, eventos e dados. |
| **Híbrido** | Clusters em vários ambientes exigem políticas e identidade de serviços consistentes — tema da M11-L09 e do M12. |

## Como especificar e implementar

- "Serviços autenticam-se mutuamente e cada chamada entre serviços é autorizada explicitamente."
- "Pods não se comunicam entre namespaces, exceto por políticas de rede aprovadas."
- "Somente imagens de registries aprovados, construídas a partir de imagens base mantidas pela organização, podem ser executadas em produção."
- "Cada função serverless tem um papel próprio com as permissões mínimas para sua tarefa."

## Trade-offs, limitações e antipadrões

- **Microsserviços multiplicam a superfície de ataque.** Cada serviço é uma API a proteger; nem toda aplicação ganha com essa divisão.
- **Kubernetes é complexo.** Configurações padrão priorizam funcionamento, não segurança; operar com segurança exige maturidade.
- **Antipadrão — namespace como fronteira de segurança sem política de rede e RBAC.**
- **Antipadrão — "serverless não tem servidor, então não tem o que proteger".**

## Como validar

- Testar se um pod consegue alcançar serviços de outros namespaces sem política explícita.
- Revisar o RBAC do cluster buscando permissões amplas (acesso a segredos, criação de pods privilegiados).
- Verificar a origem das imagens em execução e o resultado das varreduras.
- Revisar as permissões atribuídas às funções serverless.

## Como apresentar e justificar

- **Para engenharia:** "Namespaces organizam, mas não isolam. Precisamos de política de rede e RBAC mínimo para que um serviço comprometido não alcance pagamentos."
- **Para gestores:** "A migração para containers trouxe agilidade, mas também removeu barreiras que tínhamos entre sistemas. As correções restabelecem essas barreiras sem perder a agilidade."

## Checklist de revisão arquitetural

- [ ] Toda comunicação entre serviços é autenticada e autorizada.
- [ ] Há política de rede no cluster negando tráfego não aprovado.
- [ ] O plano de controle tem acesso restrito e auditado.
- [ ] Imagens vêm de fontes aprovadas e são verificadas.
- [ ] Segredos ficam em gerenciador de segredos, não em imagens ou variáveis em claro.
- [ ] Funções serverless têm permissões mínimas.

## Questões de compreensão

**1.** Por que microsserviços aumentam a importância da segurança de APIs?

??? success "Resposta comentada"

    Porque chamadas que eram internas a um processo passam a atravessar a rede, cada uma exposta por uma API. Cada interface precisa de autenticação, autorização e proteção em trânsito.

**2.** Qual o impacto de comprometer o plano de controle de um cluster Kubernetes, comparado ao de comprometer um pod?

??? success "Resposta comentada"

    Comprometer o plano de controle dá controle sobre o cluster inteiro: criar cargas, ler segredos, mudar permissões. Comprometer um pod dá, em princípio, apenas o que aquele pod pode fazer — que depende de seu isolamento, da política de rede e das permissões de sua service account.

**3.** Em serverless, quem é responsável pelas permissões da função?

??? success "Resposta comentada"

    O cliente. O provedor executa a função, mas é o cliente quem define o papel e as permissões dela; permissões excessivas tornam qualquer falha no código muito mais grave.

## Exercício de tomada de decisão

!!! question "Cenário: onde rodar o processamento de arquivos de parceiros na Aurora"

    O serviço que processa arquivos enviados por parceiros — o mais exposto a conteúdo malicioso — hoje roda no mesmo cluster e no mesmo pool de nodes que o serviço de pagamentos. Avalie: (A) manter no mesmo cluster, com política de rede, RBAC mínimo e mTLS; (B) além de A, executar o processamento em um pool de nodes dedicado, sem acesso aos segredos de pagamentos; (C) mover o processamento para funções serverless em uma conta de cloud separada, entregando os resultados por uma fila. A equipe opera Kubernetes há dois anos e ainda não usa serverless nem várias contas de cloud. Critérios: força da separação, capacidade da equipe de operar e custo da mudança.

??? success "Resolução de referência"

    | Critério | Peso | A — Mesmo cluster, controles de rede e acesso | B — Pool de nodes dedicado | C — Serverless em outra conta |
    |:---|:---|:---|:---|:---|
    | Força da separação | 3 | 1 | 2 | 3 |
    | Capacidade da equipe de operar | 2 | 3 | 3 | 1 |
    | Custo da mudança | 1 | 3 | 2 | 1 |
    | **Total ponderado** | | **12** | **14** | **12** |

    **Recomendação: B para esta equipe; A é o mínimo.** Se a equipe já dominasse serverless e governança multi-conta, a nota de operação de C subiria para 3 e o total para 16 — a escolha passaria a ser C. A matriz mostra que a resposta depende da maturidade, não só da tecnologia.

    - **A** reduz o alcance pela rede e pela API do cluster, mas o processamento e os pagamentos continuam podendo compartilhar o mesmo kernel em um node.
    - **B** acrescenta separação de execução: um escape de container no processamento não cai em um node que roda pagamentos.
    - **C** cria a separação mais forte (outra conta, outra plataforma) e um contrato estreito (a fila), mas exige que a equipe domine serverless e governança multi-conta.

    O critério é o mesmo da L01: **quanto maior a diferença de confiança entre as cargas, mais forte deve ser a fronteira entre elas**.

## Pontos-chave

- Microsserviços transformam chamadas internas em tráfego de rede, cada uma exigindo autenticação e autorização.
- Imagens, registries e execução são etapas da cadeia de confiança de containers.
- O plano de controle do Kubernetes é a fronteira mais crítica do cluster.
- Namespaces organizam; política de rede, RBAC e isolamento de nodes protegem.
- Serverless transfere a operação, não a responsabilidade por código, permissões e dados.

## Referências

### Fundamentação principal

- NIST. *SP 800-190 — Application Container Security Guide*. 2017. <https://csrc.nist.gov/pubs/sp/800/190/final> — contramedidas organizadas em seis níveis: imagem, registry, orquestrador, container, SO do host e hardware. *(Página oficial e boletim ITL de outubro de 2017 conferidos.)*
- NIST. *SP 800-204 — Security Strategies for Microservices-based Application Systems*. 2019. <https://csrc.nist.gov/pubs/sp/800/204/final> — estratégias de segurança para microsserviços. As partes tratam de service mesh (204A, 2020), ABAC com service mesh (204B, 2021), DevSecOps (204C, 2022) e segurança da cadeia de suprimentos em pipelines CI/CD (204D, 2024). *(Páginas oficiais conferidas.)*
- Kubernetes. *Overview of Cloud Native Security*. <https://kubernetes.io/docs/concepts/security/overview/> — modelo de camadas Cloud, Cluster, Container e Code. *(Parcialmente verificada.)*

### Leitura complementar

- OWASP. *Application Security Verification Standard 5.0.0*. <https://owasp.org/www-project-ASVS/> — requisitos verificáveis para aplicações e APIs, usados no M12.
- R. Anderson. *Security Engineering*, 3ª ed. Cap. 6, §6.2.11 *Sandboxing* e §6.2.12 *Virtualisation* (pp. 224–225).

### Aplicação prática

- Ao revisar um diagrama de cluster, marque as quatro fronteiras desta aula: gateway de entrada, plano de controle, comunicação entre serviços e registry.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
