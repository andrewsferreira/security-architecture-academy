---
id: M07-L01
title: "Aula 01 — Fundamentos de Zero Trust e o NIST SP 800-207"
public_title: "Módulo 7 — Aula 01 — Fundamentos de Zero Trust e o NIST SP 800-207"
description: O que Zero Trust é e o que não é — o fim da confiança implícita baseada em localização de rede, os sete princípios da NIST SP 800-207, a mudança de perímetro para recurso e os equívocos de mercado que transformam o conceito em rótulo de produto.
domain: zero-trust
tier: fundamental
status: published
prerequisites: [M05-L01, M06-L01]
objectives:
  - Explicar Zero Trust como estratégia de arquitetura, e não como produto.
  - Descrever os sete princípios (tenets) da NIST SP 800-207.
  - Contrastar o modelo de perímetro com o modelo de decisão por requisição.
  - Identificar equívocos comuns e o que Zero Trust não resolve.
minutes: 75
sources: [NIST-SP800-207, NIST-SP800-215, CISA-ZTMM-2, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [NIST-SP1800-35, NIST-SP800-207A, MS-ENTERPRISE-ACCESS-MODEL, BEYONDCORP-2014]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M07
---

# Aula 01 — Fundamentos de Zero Trust e o NIST SP 800-207 { #fundamentos-de-zero-trust-e-o-nist-sp-800-207 }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 7 · Nível 2</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">75 min · ID técnico: M07-L01</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    "Zero Trust" virou rótulo de produto, mas a ideia original é simples e exigente: **nenhuma confiança é concedida implicitamente por causa da localização na rede**. Cada acesso a cada recurso é decidido por política, com base em identidade, estado do dispositivo e contexto, e a decisão é revista ao longo do tempo. Esta aula apresenta o conceito pela referência mais citada — a NIST SP 800-207 — e separa o que é estratégia de arquitetura do que é marketing.

**Pré-requisitos:** [Zonas e segmentação](../05-network-security/01-zones-segmentation.md) e [Disciplinas de identidade](../06-iam/01-identity-disciplines.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar Zero Trust como estratégia de arquitetura, e não como produto.
- Descrever os sete princípios (tenets) da NIST SP 800-207.
- Contrastar o modelo de perímetro com o modelo de decisão por requisição.
- Identificar equívocos comuns e o que Zero Trust não resolve.

## Conceito

### O problema da confiança implícita

No modelo de perímetro, quem passa pela borda entra em uma zona considerada confiável e alcança o que a rede permitir. A NIST SP 800-215 registra que fatores como aplicações distribuídas, tráfego east-west, computação na borda e usuários remotos **anularam o conceito desse perímetro** e ampliaram a superfície de ataque (Sec. 2.1, p. 5). O cenário de ransomware da Meridiana (Módulo 4 — Aula 04) é a ilustração: uma credencial de VPN abre a rede inteira.

A ideia não nasceu com a norma. Em 2014, um relato do Google publicado na revista *;login:* da USENIX descrevia a decisão de **remover a exigência de uma intranet privilegiada** e levar as aplicações corporativas para a internet, porque um perímetro baseado em firewall, uma vez rompido, dá ao atacante acesso relativamente fácil à rede interna (resumo do artigo *BeyondCorp*). A SP 800-207 generaliza esse tipo de experiência em uma arquitetura de referência neutra em relação a fornecedores.

### O que a SP 800-207 propõe

A SP 800-207, publicada em agosto de 2020, descreve Zero Trust como um conjunto de paradigmas que movem as defesas de perímetros estáticos baseados em rede para **usuários, ativos e recursos** (resumo). Os sete princípios do §2.1 (pp. 6–7) podem ser resumidos assim:

| # | Princípio (paráfrase) | Consequência para a arquitetura |
|:---|:---|:---|
| 1 | Todas as fontes de dados e serviços computacionais são recursos | Também dispositivos pessoais, SaaS e workloads em nuvem entram no escopo |
| 2 | Toda comunicação é protegida, independentemente da localização na rede | Estar "dentro" não dispensa cifragem nem autenticação |
| 3 | O acesso a cada recurso é concedido por sessão | Acesso a um recurso não implica acesso a outro |
| 4 | O acesso é determinado por política dinâmica — estado observável da identidade, da aplicação e do ativo solicitante, e possivelmente atributos comportamentais e ambientais | Decisão contextual, não lista estática |
| 5 | A organização monitora e mede a integridade e a postura de segurança de todos os ativos próprios e associados | Postura de dispositivo e de workload alimenta decisões |
| 6 | Autenticação e autorização são dinâmicas e aplicadas estritamente antes do acesso | Verificação contínua, não só no login |
| 7 | A organização coleta o máximo possível de informação sobre ativos, infraestrutura e comunicações e a usa para melhorar a postura | Telemetria é parte da arquitetura |

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m07-l01-implicit-vs-zt.mmd"
```

<figcaption>Figura 1 — No perímetro, uma verificação na borda abre a zona interna; em Zero Trust, cada requisição passa por um ponto de aplicação de política que consulta a decisão.</figcaption>
</figure>

## Fundamentos técnicos

### De "onde está" para "quem é, em que estado, pedindo o quê"

| Pergunta | Perímetro | Zero Trust |
|:---|:---|:---|
| Quem pode acessar o ERP? | Quem está na rede interna | Identidades autorizadas, com dispositivo conforme, no contexto permitido |
| Quando a decisão é tomada? | Na entrada da rede | Em cada sessão, e reavaliada |
| O que é protegido? | O perímetro | Cada recurso |
| O que acontece depois de um comprometimento? | Movimento lateral livre | Alcance limitado às sessões autorizadas daquela identidade |

### Zero Trust é estratégia, não produto

Nenhum produto "entrega" Zero Trust. A arquitetura combina capacidades que este curso já tratou e que serão integradas no módulo:

| Capacidade | Onde foi tratada |
|:---|:---|
| Identidade forte, autenticação resistente a phishing, privilégio just-in-time | Módulo 6 |
| Autorização por política com atributos e contexto | Módulo 6 — Aula 02 |
| Acesso por aplicação em vez de acesso de rede | Módulo 5 — Aula 04 |
| Segmentação e microsegmentação | Módulo 5 — Aula 01 |
| Postura de dispositivo | Módulo 5 — Aula 06, Aula 04 |
| Telemetria e detecção | Módulo 5 — Aula 03, Módulo 15 |

O modelo de maturidade da CISA (Aula 06) organiza essas capacidades em cinco pilares — identidade, dispositivos, redes, aplicações e workloads, dados — e três capacidades transversais.

### O que Zero Trust não resolve

- **Credenciais válidas usadas por quem as roubou** ainda alcançam o que aquela identidade pode alcançar; a SP 800-207 lista credenciais roubadas e ameaça interna entre os riscos de uma ZTA e indica algoritmos de confiança contextuais para detectar padrões anormais (§5.3).
- **Comprometimento do próprio motor de decisão**: um PE ou PA comprometido ou mal configurado pode conceder acessos não aprovados (§5.1).
- **Indisponibilidade dos componentes de decisão** interrompe a operação (§5.2).
- **Vulnerabilidades nas aplicações** autorizadas continuam exploráveis.

## Exemplo empresarial

!!! example "Lumen Saúde — reescrevendo o pedido de compra"

    A diretoria da Lumen aprovou "um projeto de Zero Trust", e a primeira proposta recebida era a compra de um único produto. O arquiteto reescreveu o projeto como **objetivos de arquitetura** ligados aos princípios:

    | Objetivo | Princípio | Situação atual |
    |:---|:---|:---|
    | Acesso ao prontuário decidido por identidade, dispositivo e vínculo com o paciente | 3, 4, 6 | Qualquer funcionário na rede da clínica acessa |
    | Comunicação entre clínicas e datacenter autenticada e cifrada, mesmo na rede privada | 2 | Tráfego interno em claro |
    | Postura dos dispositivos das clínicas avaliada antes do acesso | 5 | Sem inventário confiável |
    | Telemetria de acesso a prontuários usada para detectar abuso | 7 | Logs locais, sem análise |

    Com objetivos claros, a escolha de produtos passou a ser consequência — e a diretoria passou a acompanhar resultados, não licenças.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Confiança | Implícita pela localização | Explícita, por sessão e por recurso |
| Decisão | Estática, na borda | Dinâmica, com contexto, reavaliada |
| Comunicação interna | Em claro, "rede confiável" | Autenticada e cifrada |
| Dispositivos | Assumidos confiáveis se na rede | Postura medida e usada na decisão |
| Projeto | Compra de produto | Objetivos de arquitetura ligados a princípios |

## Controles e padrões relevantes

A SP 800-207 não traz um catálogo de controles; a correspondência abaixo, entre princípios e controles da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, é proposta por esta trilha para tornar os princípios verificáveis. Os catálogos são referências voluntárias.

| Controle ou padrão | Princípio da SP 800-207 que ajuda a cumprir | Referência |
|:---|:---|:---|
| Princípios de engenharia de segurança | Aplicar princípios de segurança no desenho, inclusive os de Zero Trust | SP 800-53: SA-8 (Security and Privacy Engineering Principles) |
| Inventário de ativos | 1 e 5 — todos os recursos e ativos conhecidos, com postura medida | SP 800-53: CM-8 (System Component Inventory); CIS v8.1: Controles 1 e 2 (inventário de ativos e de software) |
| Comunicação protegida | 2 — comunicação protegida independentemente da localização | SP 800-53: SC-8 (Transmission Confidentiality and Integrity) |
| Aplicação de acesso por recurso | 3 e 6 — acesso decidido e aplicado antes de cada sessão | SP 800-53: AC-3 (Access Enforcement) e AC-4 (Information Flow Enforcement) |
| Autenticação de usuários e serviços | 4 e 6 — identidade verificada dinamicamente | SP 800-53: IA-2 e IA-9 |
| Monitoração contínua | 5 e 7 — medir postura e usar a telemetria para melhorar | SP 800-53: CA-7 (Continuous Monitoring) e SI-4 (System Monitoring) |
| Princípios de referência | Os sete princípios e as ameaças à própria arquitetura | NIST SP 800-207, §2.1 e §5 |

## Aplicabilidade: on-premises, cloud e híbrido

Zero Trust é especialmente natural em cloud, onde identidade e política já estão no centro do controle de acesso. Em on-premises, a transição exige trazer identidade e postura para recursos antes protegidos só pela rede — e lidar com legados (Aula 07). Em ambientes híbridos, Zero Trust oferece uma política de acesso **independente de onde o recurso está**, o que reduz a dependência da conectividade entre ambientes como mecanismo de confiança.

## Como especificar e implementar

- "Nenhum acesso a recurso corporativo é concedido apenas pela localização na rede."
- "Acesso a recursos críticos é decidido por política que considera identidade, método de autenticação, postura do dispositivo e contexto, e é reavaliado durante a sessão."
- "Comunicação entre serviços é autenticada e cifrada, inclusive em redes privadas."
- "A telemetria de acesso é coletada e usada para detecção e ajuste de políticas."

## Trade-offs, limitações e antipadrões

- **Trade-off:** mais decisões e mais verificações aumentam a dependência dos componentes de decisão — que precisam de alta disponibilidade.
- **Antipadrão — Zero Trust como produto:** comprar uma solução e declarar o projeto concluído.
- **Antipadrão — "Zero Trust só para remotos":** usuários na sede continuam com confiança implícita.
- **Limitação:** a SP 800-207 é uma referência conceitual; não prescreve tecnologias nem constitui obrigação legal no Brasil.

## Como validar

- Para três recursos críticos, verificar se o acesso de um dispositivo na rede interna, sem identidade adequada, é negado.
- Verificar se a comunicação interna entre serviços críticos é autenticada.
- Conferir se decisões de acesso são registradas e analisadas.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Objetivos do programa expressos por princípio, com situação atual e meta | Documento de objetivos aprovado, sem item definido apenas como produto |
| Recursos críticos do primeiro escopo negam acesso sem identidade adequada, mesmo da rede interna | Teste a partir da rede interna com identidade não autorizada, negado |
| Comunicação entre serviços críticos do escopo autenticada e cifrada | Configuração e captura de tráfego de amostra |
| Decisões de acesso registradas e analisadas | Registros no SIEM com identidade, dispositivo, recurso e resultado |
| Componentes de decisão com alta disponibilidade | Teste de falha de um nó de decisão sem interrupção do acesso autorizado |

## Como apresentar e justificar

- **Para a diretoria:** "Zero Trust não é um produto; é deixar de confiar em quem está 'dentro' só por estar dentro. Vamos medir em quantos recursos críticos isso já é verdade."
- **Para engenharia:** "Cada recurso decide quem entra, com base em identidade e estado do dispositivo. A rede deixa de ser o critério."

## Checklist de revisão arquitetural

- [ ] O projeto está expresso em objetivos ligados aos princípios, não em produtos.
- [ ] Recursos críticos não confiam na localização de rede.
- [ ] Decisões consideram identidade, postura e contexto.
- [ ] Comunicação interna crítica é autenticada e cifrada.
- [ ] Componentes de decisão têm alta disponibilidade e controle de mudanças.

## Questões de compreensão

**1.** Qual a ideia central de Zero Trust segundo a SP 800-207?

??? success "Resposta comentada"

    Eliminar a confiança implícita baseada em localização de rede, movendo as defesas de perímetros estáticos para usuários, ativos e recursos: cada acesso a cada recurso é decidido por política dinâmica, por sessão.

**2.** Por que Zero Trust não elimina o risco de credenciais roubadas?

??? success "Resposta comentada"

    Porque uma credencial válida ainda alcança os recursos a que aquela identidade tem direito. Zero Trust reduz o alcance e permite detectar padrões anormais com algoritmos contextuais, mas não impede o uso legítimo-aparente da credencial.

**3.** Por que "comprar um produto de Zero Trust" não basta?

??? success "Resposta comentada"

    Porque Zero Trust é um conjunto de princípios aplicados a identidade, dispositivos, rede, aplicações e dados, com governança e telemetria. Produtos implementam partes; a arquitetura é que garante coerência e cobertura.

## Exercício de tomada de decisão

!!! question "Cenário: escopo inicial na Meridiana"

    A Meridiana quer começar Zero Trust. Opções de primeiro escopo: (A) todos os usuários e aplicações ao mesmo tempo; (B) acesso remoto e administração privilegiada; (C) apenas os centros de distribuição. Considerando os cenários de risco do Caso A, compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e recomende um escopo.

**Objetivos avaliados:** Explicar Zero Trust como estratégia de arquitetura, e não como produto; identificar equívocos comuns e o que Zero Trust não resolve.

**Entrega esperada:** Matriz ponderada e o escopo inicial recomendado, com o que fica fora e o próximo escopo.

**Critérios de avaliação:**

- O escopo escolhido interrompe passos concretos do cenário de risco prioritário.
- A resposta declara o que continua com confiança pela rede e por quanto tempo.
- A recomendação é viável em meses, com patrocínio e capacidade existentes.

??? success "Resolução de referência"

    | Critério | Peso | A — Tudo ao mesmo tempo | B — Acesso remoto e administração privilegiada | C — Centros de distribuição |
    |:---|:---|:---|:---|:---|
    | Interrupção do cenário RSK-007 | 3 | 3 | 3 | 1 |
    | Viabilidade com a equipe e o orçamento | 2 | 1 | 3 | 2 |
    | Tempo até o primeiro resultado mensurável | 2 | 1 | 3 | 2 |
    | Cobertura para a expansão posterior | 1 | 3 | 2 | 2 |
    | **Total ponderado** | | **16** | **23** | **13** |

    - **Pesos:** o programa nasce do cenário de ransomware (peso 3). Viabilidade e tempo pesam 2: um primeiro escopo que não entrega resultado em meses perde patrocínio. A cobertura pesa 1, porque a expansão é planejada depois (Aula 07).
    - **Recomendação: B.** O cenário RSK-007 começa no acesso remoto e escala por credenciais privilegiadas. Aplicar os princípios a esses dois caminhos — acesso por aplicação com identidade resistente a phishing e postura (Módulo 5 — Aula 04), e administração por caminho privilegiado com just-in-time (Módulo 6 — Aula 06) — interrompe o cenário mais grave com escopo controlável. A opção A interromperia o cenário se concluída, mas é inviável de uma vez; a C trata um ambiente com muitos dispositivos sem suporte a agentes, que exige primeiro inventário e segmentação (Aula 07).
    - **Trade-off aceito e risco residual:** usuários na sede e os centros de distribuição continuam, por ora, com confiança pela rede — o antipadrão "Zero Trust só para remotos" é aceito como etapa, com prazo e próximo escopo definidos. Movimento lateral a partir de uma estação interna comprometida continua dependendo da segmentação do Módulo 5.
    - **O que mudaria a decisão:** um incidente com origem em dispositivo de centro de distribuição, ou uma exigência de cliente sobre a rede operacional, elevaria C; se a Meridiana já tivesse acesso remoto por aplicação e PIM implantados, o primeiro escopo passaria a ser o acesso interno às aplicações críticas.

    **Erros comuns:**

    - Tratar Zero Trust como projeto único para todos os usuários e aplicações ao mesmo tempo.
    - Começar pelo ambiente mais difícil (dispositivos sem agente) sem inventário.
    - Chamar de Zero Trust a simples troca de VPN por ZTNA, sem identidade forte e sem postura.

## Pontos-chave

- Zero Trust elimina a confiança implícita pela localização de rede.
- Os sete princípios da SP 800-207 tratam de recursos, comunicação, sessão, política dinâmica, postura, verificação contínua e telemetria.
- É estratégia de arquitetura; produtos implementam partes.
- Não elimina riscos de credenciais válidas, de comprometimento da decisão nem de indisponibilidade.
- Comece pelos caminhos dos cenários de maior risco.

## Referências

### Fundamentação principal

- NIST. *SP 800-207 — Zero Trust Architecture*. S. Rose et al., 2020. <https://csrc.nist.gov/pubs/sp/800/207/final> — resumo, §2.1 (princípios, pp. 6–7), §5.1–5.3 (ameaças, pp. 28–29). *(Lido; princípios e sumário reconferidos no PDF em 2026-10-29.)*
- NIST. *SP 800-215* — Sec. 2.1 (p. 5). *(Lido.)*
- CISA. *Zero Trust Maturity Model 2.0*. 2023 — pilares e capacidades transversais (conferidos em fontes secundárias; o PDF oficial não abriu na ferramenta em 2026-10-23 nem em 2026-10-29).
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles SA-8, CM-8, SC-8, AC-3, AC-4, IA-2, IA-9, CA-7 e SI-4, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controles 1 e 2 — gratuito.

### Leitura complementar

- NIST. *SP 1800-35 — Implementing a Zero Trust Architecture*. 2025 — 19 implementações de exemplo.
- NIST. *SP 800-207A* — Zero Trust para aplicações cloud-native ([Aula 05](05-workload-protection.md)).
- Microsoft. *The enterprise access model*.
- R. Ward, B. Beyer. *BeyondCorp: A New Approach to Enterprise Security*. USENIX ;login:, v. 39, n. 6, dez. 2014. <https://www.usenix.org/publications/login/dec14/ward> — origem histórica do modelo sem intranet privilegiada. *(Resumo conferido em 2026-11-05; texto completo não lido.)*

### Aplicação prática

- Escolha três recursos críticos da sua organização e verifique, para cada um, se o acesso depende da localização de rede. Reescreva a regra de acesso de um deles com identidade, dispositivo e contexto.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
