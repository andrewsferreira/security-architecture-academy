---
id: M07-L06
title: "Aula 06 — CISA Zero Trust Maturity Model"
public_title: "Módulo 7 — Aula 06 — CISA Zero Trust Maturity Model"
description: Como usar o CISA Zero Trust Maturity Model 2.0 — cinco pilares, três capacidades transversais e quatro estágios — para avaliar a situação atual, definir alvos por pilar e priorizar uma evolução coerente, sem transformar a maturidade em meta em si.
domain: zero-trust
tier: architect
status: published
prerequisites: [M07-L04, M07-L05, M03-L08]
objectives:
  - Descrever os pilares, as capacidades transversais e os estágios do ZTMM 2.0.
  - Avaliar a maturidade por pilar e por função com evidências.
  - Definir alvos por pilar ligados a riscos e dependências entre pilares.
  - Usar o modelo para comunicar progresso sem confundi-lo com redução de risco.
minutes: 60
sources: [CISA-ZTMM-2, NIST-SP800-207, NIST-SP800-55-V1, NIST-SP800-53]
further_reading: [NIST-SP1800-35, NIST-CSF-2]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M07
---

# Aula 06 — CISA Zero Trust Maturity Model { #cisa-zero-trust-maturity-model }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 7 · Nível 2</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">60 min · ID técnico: M07-L06</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    A SP 800-207 diz o que é Zero Trust; o **Zero Trust Maturity Model (ZTMM)** da CISA ajuda a responder "onde estamos e para onde vamos". A versão 2.0, de abril de 2023, organiza a jornada em cinco pilares e três capacidades transversais, cada um evoluindo por quatro estágios. O modelo foi escrito para agências federais dos Estados Unidos, mas sua estrutura é amplamente usada como referência. Esta aula mostra como aplicá-lo com evidências e como evitar que a maturidade vire um fim em si.

**Pré-requisitos:** [Verificação contínua](04-continuous-verification.md), [Proteção de workloads](05-workload-protection.md) e [Indicadores e maturidade](../03-governance-risk/08-metrics-maturity-reporting.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Descrever os pilares, as capacidades transversais e os estágios do ZTMM 2.0.
- Avaliar a maturidade por pilar e por função com evidências.
- Definir alvos por pilar ligados a riscos e dependências entre pilares.
- Usar o modelo para comunicar progresso sem confundi-lo com redução de risco.

!!! info "Sobre as fontes desta aula"

    O PDF oficial do ZTMM 2.0 não pôde ser aberto pela ferramenta de verificação (tentativas em 2026-10-23 e 2026-10-29). Os pilares, as capacidades transversais e as definições dos estágios foram conferidos no Microsoft Learn (reconferidos em 2026-10-29); as funções por pilar e os exemplos por função, em reprodução do documento publicada por um fornecedor. Antes de usar o modelo em uma avaliação formal, consulte o documento oficial da CISA.

## Conceito

### Estrutura

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m07-l06-ztmm.mmd"
```

<figcaption>Figura 1 — Cinco pilares sustentados por três capacidades transversais; cada pilar evolui pelos quatro estágios de forma independente.</figcaption>
</figure>

| Pilar | Funções (conforme reprodução consultada) |
|:---|:---|
| **Identity** | Authentication; Identity Stores; Risk Assessments; Access Management |
| **Devices** | Policy Enforcement & Compliance Monitoring; Asset & Supply Chain Risk Management; Resource Access; Device Threat Protection |
| **Networks** | Network Segmentation; Network Traffic Management; Traffic Encryption; Network Resilience |
| **Applications and Workloads** | Application Access; Application Threat Protections; Accessible Applications; Secure Application Development & Deployment Workflow; Application Security Testing |
| **Data** | Data Inventory Management; Data Categorization; Data Availability; Data Access; Data Encryption |

As **capacidades transversais** — *Visibility and Analytics*, *Automation and Orchestration* e *Governance* — aparecem em todos os pilares.

### Os quatro estágios

Segundo a descrição do Microsoft Learn:

| Estágio | Característica geral |
|:---|:---|
| **Traditional** | Ciclos de vida e atribuições configurados manualmente, políticas estáticas, privilégio mínimo definido só no provisionamento, pilares isolados, resposta manual, pouca correlação de logs |
| **Initial** | Início de automação em atributos, ciclos de vida e decisões de política; integração inicial entre pilares; visibilidade agregada dos sistemas internos |
| **Advanced** | Ciclos de vida automatizados onde aplicável, visibilidade e aplicação de política centralizadas, respostas com mitigações predefinidas, ajuste dinâmico em direção ao privilégio mínimo com base em sinais de risco e postura |
| **Optimal** | Ciclos de vida just-in-time automatizados, privilégio mínimo dinâmico, monitoração contínua e consciência situacional abrangente |

Exemplos por função, conforme a reprodução consultada: em **Identity — Authentication**, a evolução vai de senha ou MFA com acesso estático até revalidação contínua com MFA resistente a phishing; em **Networks — Network Segmentation**, de grandes segmentos de perímetro com túneis VPN amplos até microperímetros distribuídos, microsegmentação por perfil de aplicação e conectividade just-in-time.

## Fundamentos técnicos

### Avaliar com evidências

Uma avaliação útil é feita **por função**, não por pilar inteiro, e cada nota tem evidência:

| Pilar / função | Estágio atual | Evidência | Estágio-alvo (18 meses) |
|:---|:---|:---|:---|
| Identity / Authentication | Initial | MFA por push para todos; 40% dos administradores com chave FIDO2 | Advanced |
| Devices / Policy Enforcement | Traditional | Postura não usada em decisões | Initial |
| Networks / Network Segmentation | Traditional | Rede plana no datacenter; VPN ampla | Initial |
| Applications / Application Access | Initial | SSO para 70% das aplicações | Advanced |
| Data / Data Categorization | Traditional | Sem classificação aplicada | Initial |

Como discutido na Aula 08 do Módulo 3, uma nota de maturidade é uma **avaliação semiquantitativa**, não uma medida. Para provar progresso, cada alvo deve ter **medidas** associadas — por exemplo, "% de contas privilegiadas com autenticação resistente a phishing" para Identity/Authentication.

### Dependências entre pilares

Pilares não evoluem isoladamente:

- Políticas contextuais (Identity, Advanced) dependem de **postura de dispositivo** (Devices).
- Microsegmentação (Networks) depende de **inventário e identidade de workload** (Applications and Workloads).
- Controle de acesso a dados (Data) depende de **categorização** e de **identidade** madura.

Um alvo "Optimal" em um pilar com os outros em "Traditional" costuma ser inviável ou ilusório.

### Maturidade não é a meta

O modelo é instrumento de planejamento. A meta é reduzir o risco dos cenários do register (Módulo 3 — Aula 06). Alvos devem ser escolhidos pelo efeito nos cenários e pelas dependências — não pelo desejo de "chegar ao Optimal".

## Exemplo empresarial

!!! example "Meridiana — perfil de maturidade ligado a cenários"

    A Meridiana avaliou as funções do ZTMM e escolheu alvos apenas onde havia ligação com cenários do register:

    | Função | Atual | Alvo | Cenário |
    |:---|:---|:---|:---|
    | Identity / Authentication | Traditional | Advanced (privilegiados e remoto) | RSK-007 |
    | Networks / Network Segmentation | Traditional | Initial (isolamento dos críticos) | RSK-007 |
    | Devices / Device Threat Protection | Initial | Advanced (EDR com integração ao acesso) | RSK-007 |
    | Applications / Application Access | Traditional | Initial (ZTNA para web) | RSK-007 |
    | Data / Data Availability | Traditional | Initial (backup imutável) | RSK-007 |

    Funções sem cenário ligado ficaram no estágio atual, registradas como decisão consciente. O reporte à diretoria mostrava estágio e **medida** lado a lado — por exemplo, seis meses depois, "Identity/Authentication: Traditional → Initial; 78% dos acessos privilegiados com FIDO2".

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Avaliação | Nota por pilar, sem evidência | Estágio por função, com evidência |
| Alvos | "Optimal em tudo" | Por função, ligados a cenários e dependências |
| Progresso | Mudança de estágio | Estágio + medidas de implementação e eficácia |
| Uso | Fim em si | Instrumento de planejamento e comunicação |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referências voluntárias para o programa de maturidade, e os modelos usados na aula:

| Controle ou padrão | Objetivo na gestão da maturidade | Referência |
|:---|:---|:---|
| Medidas de desempenho | Desenvolver, monitorar e reportar medidas de segurança | SP 800-53: PM-6 (Measures of Performance) |
| Estratégia de risco | Alvos escolhidos pela estratégia de gestão de risco, não pelo estágio | SP 800-53: PM-9 (Risk Management Strategy) |
| Monitoração contínua da organização | Métricas organizacionais e frequências de monitoração | SP 800-53: PM-31 (Continuous Monitoring Strategy) |
| Avaliação com evidência | Plano de avaliação com escopo, procedimentos e evidências | SP 800-53: CA-2 (Control Assessments) |
| Medidas versus avaliações | Distinguir avaliação semiquantitativa de medida | NIST SP 800-55 Vol. 1 |
| Pilares, capacidades e estágios | Estrutura de referência para a avaliação | CISA ZTMM 2.0 |

## Aplicabilidade: on-premises, cloud e híbrido

Ambientes em cloud tendem a avançar mais rápido em Identity e Applications, com capacidades nativas; on-premises costuma ficar para trás em Networks e Devices. O ZTMM ajuda a tornar essa diferença visível — e a avaliação deveria registrar o estágio **por ambiente** quando ele divergir, em vez de uma média.

## Como especificar e implementar

- "A maturidade Zero Trust é avaliada por função do ZTMM, com evidência, ao menos uma vez por ano."
- "Alvos são definidos por função, ligados a cenários de risco e às dependências entre pilares."
- "Cada alvo tem medidas de implementação e de eficácia associadas."
- "Diferenças relevantes entre ambientes são registradas separadamente."

## Trade-offs, limitações e antipadrões

- **Trade-off:** granularidade da avaliação versus esforço — avaliar todas as funções todo trimestre é caro; avalie por função anualmente e acompanhe medidas mensalmente.
- **Antipadrão — maturidade como KPI do CISO:** incentiva subir estágios no papel.
- **Antipadrão — média entre ambientes:** esconde o ambiente atrasado.
- **Limitação:** o ZTMM foi escrito para agências federais dos EUA; requisitos citados nele não são obrigações no Brasil.

## Como validar

- Para três funções avaliadas, pedir a evidência e conferir.
- Verificar se cada alvo tem medida associada.
- Conferir se as dependências entre pilares foram consideradas nos alvos.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Cada função avaliada tem evidência verificável | Amostra de três funções com a evidência conferida |
| Cada alvo está ligado a um cenário do register | Tabela de alvos com o cenário correspondente |
| Cada alvo tem medida de implementação ou de eficácia | Medida definida, com fonte e periodicidade |
| Nenhum alvo ignora uma dependência entre pilares | Revisão das dependências registrada com os alvos |

## Como apresentar e justificar

- **Para a diretoria:** "Estamos em Traditional em quatro de cinco pilares. Não vamos perseguir 'Optimal': vamos avançar onde reduz o risco de ransomware, e medir o efeito."
- **Para as equipes:** "O estágio é uma fotografia; a medida mostra se estamos andando."

## Checklist de revisão arquitetural

- [ ] Avaliação por função, com evidência.
- [ ] Alvos ligados a cenários de risco.
- [ ] Dependências entre pilares consideradas.
- [ ] Medidas associadas a cada alvo.
- [ ] Diferenças entre ambientes registradas.

## Questões de compreensão

**1.** Quais são os cinco pilares e as três capacidades transversais do ZTMM 2.0?

??? success "Resposta comentada"

    Pilares: Identity, Devices, Networks, Applications and Workloads e Data. Capacidades transversais: Visibility and Analytics, Automation and Orchestration e Governance.

**2.** Por que avaliar por função e não só por pilar?

??? success "Resposta comentada"

    Porque funções de um mesmo pilar podem estar em estágios muito diferentes — por exemplo, autenticação avançada com gestão de acessos tradicional. A avaliação por função mostra onde agir.

**3.** Por que uma nota de maturidade não basta para mostrar progresso?

??? success "Resposta comentada"

    Porque é uma avaliação semiquantitativa e pode subir sem que o risco diminua. Medidas de implementação e de eficácia associadas aos alvos mostram o efeito real.

## Exercício de tomada de decisão

!!! question "Cenário: alvo único na Lumen"

    O conselho da Lumen pediu "Advanced em todos os pilares em 12 meses". Hoje a Lumen está em Initial em Identity e Applications e em Traditional nos demais. As respostas possíveis são:

    - **A** — aceitar o alvo do conselho e planejar Advanced em todos os pilares;
    - **B** — propor alvos diferenciados por função, ligados a cenários de risco e às dependências entre pilares, com medidas;
    - **C** — não definir alvos de maturidade e acompanhar só medidas de implementação e eficácia.

    Compare as respostas com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e recomende uma, considerando dependências e riscos.

**Objetivos avaliados:** Definir alvos por pilar ligados a riscos e dependências entre pilares; usar o modelo para comunicar progresso sem confundi-lo com redução de risco.

**Entrega esperada:** Matriz ponderada, alvos por função ligados a cenários e dependências, e as medidas de acompanhamento.

**Critérios de avaliação:**

- Cada alvo é justificado por um cenário de risco e respeita as dependências entre pilares.
- As medidas acompanham redução de risco, não só o estágio de maturidade.
- Funções sem alvo ficam no estágio atual por decisão registrada, com revisão.

??? success "Resolução de referência"

    | Critério | Peso | A — Advanced em todos | B — Alvos diferenciados com medidas | C — Só medidas |
    |:---|:---|:---|:---|:---|
    | Redução de risco nos cenários priorizados | 3 | 2 | 3 | 2 |
    | Viabilidade em 12 meses, considerando dependências | 3 | 1 | 3 | 3 |
    | Clareza para o conselho | 2 | 3 | 2 | 1 |
    | Mensurabilidade do progresso | 1 | 1 | 3 | 3 |
    | **Total ponderado** | | **16** | **25** | **20** |

    - **Pesos:** o objetivo do programa é reduzir o risco dos cenários (peso 3), e um alvo inviável em 12 meses compromete a credibilidade do programa (peso 3). A clareza para o conselho pesa 2 — é ele quem patrocina. A mensurabilidade pesa 1, porque B e C a resolvem igualmente.
    - **Recomendação: B** — propor alvos diferenciados. Identity/Authentication e Applications/Application Access em **Advanced** (dados de saúde, cenário de acesso indevido a prontuários); Devices/Policy Enforcement em **Initial → Advanced** apenas para dispositivos clínicos, porque políticas contextuais dependem dele; Data/Data Categorization em **Initial**, pré-requisito para controles de acesso a dados; Networks em **Initial**, com isolamento dos equipamentos médicos (Módulo 5 — Aula 06).
    - **Justificativa:** Advanced em Identity sem postura de dispositivo (Devices) é inviável; Advanced em Data sem categorização também.
    - **Medidas:** % de acessos a prontuários com autenticação resistente a phishing; % de dispositivos clínicos com postura avaliada; % de repositórios com dados de saúde classificados.
    - **Registro:** decisão com dono e revisão semestral.
    - **Trade-off aceito e risco residual:** o conselho recebe uma resposta menos simples que "Advanced em tudo", e pilares sem alvo (Networks fora dos equipamentos médicos, por exemplo) ficam no estágio atual por decisão registrada; o risco residual desses pilares é aceito até a revisão semestral.
    - **O que mudaria a decisão:** uma exigência regulatória ou contratual expressa em estágios do ZTMM tornaria parte de A obrigatória para as funções exigidas; se o conselho não aceitar estágios por função, C com um painel de medidas por cenário é a alternativa de comunicação.

    **Erros comuns:**

    - Aceitar "Advanced em tudo" sem avaliar dependências e capacidade.
    - Tratar o estágio de maturidade como meta em si, desligado dos riscos.
    - Avaliar por pilar inteiro, sem evidência por função.

## Pontos-chave

- O ZTMM 2.0 tem cinco pilares, três capacidades transversais e quatro estágios.
- Avalie por função, com evidência; pilares evoluem em ritmos diferentes.
- Alvos devem seguir riscos e dependências, não o desejo de "Optimal".
- Associe medidas aos alvos para provar progresso.
- O modelo é referência; não é obrigação fora do governo federal dos EUA.

## Referências

### Fundamentação principal

- CISA. *Zero Trust Maturity Model, Version 2.0*. Abril de 2023. <https://www.cisa.gov/zero-trust-maturity-model> — pilares, capacidades transversais e estágios conferidos em Microsoft Learn (<https://learn.microsoft.com/en-us/security/zero-trust/cisa-zero-trust-maturity-model-intro>, reconferido em 2026-10-29); funções por pilar em reprodução da Thales. *(PDF oficial não aberto pela ferramenta.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles CA-2, PM-6, PM-9 e PM-31, conferidos no catálogo OSCAL oficial — gratuito.
- NIST. *SP 800-207*. *(Lido.)*
- NIST. *SP 800-55 Vol. 1* — avaliação semiquantitativa versus medida (Módulo 3 — Aula 08). *(Lido.)*

### Leitura complementar

- NIST. *SP 1800-35* — implementações de exemplo mapeadas ao CSF e à SP 800-53.
- NIST. *CSF 2.0* — perfis atual e alvo (Módulo 3 — Aula 01).

### Aplicação prática

- Avalie cinco funções do ZTMM no seu ambiente, com evidência, e defina alvo e medida apenas para as funções ligadas a cenários do seu register.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
