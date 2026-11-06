---
id: M07-L07
title: "Aula 07 — Implantação progressiva com sistemas legados e restrições"
public_title: "Módulo 7 — Aula 07 — Implantação progressiva com sistemas legados e restrições"
description: Como planejar uma migração realista para Zero Trust — as etapas da seção 7 da NIST SP 800-207, a convivência entre arquitetura de perímetro e Zero Trust, o tratamento de sistemas legados com gateways de enclave e controles compensatórios, e a priorização por ondas com critérios de aceite.
domain: zero-trust
tier: architect
status: published
prerequisites: [M07-L01, M07-L02, M07-L03, M07-L04, M07-L05, M07-L06]
objectives:
  - Aplicar as etapas de migração da SP 800-207 a uma organização real.
  - Planejar a convivência entre arquitetura de perímetro e Zero Trust.
  - Tratar sistemas legados sem bloquear a evolução nem deixá-los invisíveis.
  - Priorizar ondas por redução de risco, dependências e capacidade da organização.
minutes: 90
sources: [NIST-SP800-207, NIST-SP1800-35, CISA-ZTMM-2, NIST-SP800-215, NIST-SP800-53]
further_reading: [NIST-SP800-207A, MS-ENTERPRISE-ACCESS-MODEL]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M07
---

# Aula 07 — Implantação progressiva com sistemas legados e restrições { #implantacao-progressiva-com-sistemas-legados-e-restricoes }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 7 · Nível 2</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">90 min · ID técnico: M07-L07</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Nenhuma organização com história migra para Zero Trust de uma vez. Há sistemas que não suportam autenticação moderna, equipamentos que não aceitam agentes, contratos vigentes e equipes com capacidade limitada. A NIST SP 800-207 reconhece isso: a maioria das organizações opera uma **arquitetura híbrida** — perímetro e Zero Trust — durante a transição. Esta aula transforma os princípios do módulo em um plano em ondas, com tratamento explícito para legados e critérios de aceite por etapa.

**Pré-requisitos:** as Aulas 01 a 06 deste módulo.

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Aplicar as etapas de migração da SP 800-207 a uma organização real.
- Planejar a convivência entre arquitetura de perímetro e Zero Trust.
- Tratar sistemas legados sem bloquear a evolução nem deixá-los invisíveis.
- Priorizar ondas por redução de risco, dependências e capacidade da organização.

## Conceito

### Zero Trust puro e híbrido

A SP 800-207 distingue uma **ZTA pura**, que substitui o desenho de perímetro, da situação mais comum: organizações que operam **um híbrido** de ambos durante a transição (§7.1–7.2, p. 36). Reconhecer o híbrido não é fraqueza; é planejamento honesto. O que importa é que a parcela de perímetro **encolha** e que suas exceções sejam conhecidas.

### As etapas da SP 800-207

A seção 7.3 descreve passos para introduzir Zero Trust em uma rede baseada em perímetro (pp. 37–41):

| Etapa | Pergunta | Produto |
|:---|:---|:---|
| **Identificar atores** (§7.3.1) | Quem — pessoas e entidades não humanas — acessa os recursos? | Inventário de sujeitos, inclusive contas de serviço |
| **Identificar ativos** (§7.3.2) | Quais dispositivos e recursos existem? | Inventário de ativos, inclusive não gerenciados |
| **Identificar processos-chave e avaliar riscos** (§7.3.3) | Que processos de negócio importam mais e quais seus riscos? | Priorização (BIA e register, Módulo 3) |
| **Formular políticas** (§7.3.4) | Que regras de acesso cada recurso precisa? | Políticas por recurso |
| **Identificar soluções candidatas** (§7.3.5) | Que componentes implementam PE, PA, PEP? | Arquitetura de solução |
| **Implantação inicial e monitoração** (§7.3.6) | As políticas funcionam sem quebrar a operação? | Modo de observação, ajustes |
| **Expandir** (§7.3.7) | Que recursos entram a seguir? | Próxima onda |

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m07-l07-roadmap.mmd"
```

<figcaption>Figura 1 — Fundação, ondas sucessivas com observação, aplicação e expansão, e tratamento paralelo dos legados em enclaves.</figcaption>
</figure>

## Fundamentos técnicos

### Legados: o que fazer com o que não muda

| Situação | Tratamento | Referência |
|:---|:---|:---|
| Aplicação sem autenticação moderna | Publicar por gateway ou proxy que exija identidade e postura antes de alcançá-la | Gateway de enclave (§3.2.2, pp. 14–15) |
| Equipamento sem agente (OT, médico, coletores) | Segmento isolado, fluxos mínimos, NAC com perfilamento, monitoração | Módulo 5 — Aulas 01 e 06 |
| Protocolo legado (NTLM, LDAP em claro) | Isolamento de origem e destino, cifragem no canal, plano de remoção | Módulo 6 — Aula 03, Módulo 8 — Aula 06 |
| Sistema sem suporte | Controles compensatórios, exceção com dono e prazo | Módulo 8 — Aula 05, Módulo 2 — Aula 04 |

Dois cuidados: o **enclave** deve ser pequeno — um gateway "Zero Trust" na frente de uma rede inteira reproduz o perímetro —, e cada legado precisa de **dono e data** para sair do enclave.

### Critérios para priorizar ondas

| Critério | Pergunta |
|:---|:---|
| **Redução de risco** | A onda interrompe cenários críticos do register? |
| **Dependências** | Os pré-requisitos (identidade, postura, inventário) estão prontos? |
| **Esforço e capacidade** | A equipe consegue operar o que será implantado? |
| **Visibilidade de resultado** | O efeito é mensurável e comunicável? |
| **Janelas** | Contratos, renovações, projetos de modernização em curso |

### Riscos da própria migração

A SP 800-207 lista ameaças específicas de uma ZTA que precisam estar no plano (§5): subversão do processo de decisão, negação de serviço contra PE/PA/PEP, credenciais roubadas, visibilidade reduzida em tráfego cifrado, armazenamento de informação sensível sobre a rede, dependência de formatos proprietários e entidades não humanas na administração. A migração deve ter **modo de falha**, **controle de mudanças** e **plano de reversão** por onda.

### Aprendendo com implementações de referência

A NIST SP 1800-35, publicada em junho de 2025, apresenta 19 implementações de exemplo construídas com 24 fornecedores e mapeia as capacidades ao CSF e à SP 800-53 Rev. 5. É material útil para comparar soluções candidatas (§7.3.5) e para entender como os componentes lógicos se materializam em produtos.

## Exemplo empresarial

!!! example "Meridiana — plano em três ondas"

    Com equipe de segurança de três pessoas e um parceiro de serviços gerenciados, a Meridiana planejou:

    | Onda | Escopo | Pré-requisitos | Critério de aceite |
    |:---|:---|:---|:---|
    | **Fundação (2 meses)** | Inventário de identidades, ativos e aplicações; políticas por classe | — | 95% das aplicações classificadas; contas de serviço com dono |
    | **Onda 1 (4 meses)** | Acesso remoto por aplicação; MFA resistente a phishing para privilegiados e remoto; caminho privilegiado | Inventário | VPN restrita a 12 exceções; nenhum administrador com privilégio permanente no domínio |
    | **Onda 2 (6 meses)** | Postura de dispositivo em acesso condicional; ZTNA para aplicações web internas | Onda 1, MDM | 90% dos acessos a aplicações sensíveis com dispositivo conforme |
    | **Onda 3 (6 meses)** | Microsegmentação dos sistemas críticos do datacenter | Mapa de fluxos | ERP, WMS e backup acessíveis só por fluxos documentados |
    | **Legados (contínuo)** | Servidor de etiquetas e coletores em enclave | Segmentação | Enclave com 4 fluxos; substituição contratada até o fim do ano |

    A cada onda, o cenário RSK-007 era reavaliado: o número de pontos de interrupção do ataque passou de zero para seis ao fim da Onda 3.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Abordagem | Big bang ou "um dia faremos" | Ondas com pré-requisitos e critérios de aceite |
| Legados | Ignorados ou bloqueadores | Enclaves pequenos, dono e data de saída |
| Convivência | Implícita | Híbrido declarado, encolhendo a cada onda |
| Riscos da migração | Não considerados | Modo de falha, controle de mudanças e reversão |
| Sucesso | Produtos implantados | Cenários interrompidos e medidas |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referências voluntárias para conduzir a migração, e a sequência da SP 800-207:

| Controle ou padrão | Objetivo na implantação progressiva | Referência |
|:---|:---|:---|
| Arquitetura de segurança | Arquitetura-alvo descrita, com requisitos e abordagem, atualizada a cada onda | SP 800-53: PL-8 (Security and Privacy Architectures) |
| Plano de ação e marcos | Ondas, pendências e prazos documentados e acompanhados | SP 800-53: CA-5 (Plan of Action and Milestones) |
| Análise de impacto e mudança | Analisar o impacto de cada onda antes de aplicar; mudanças controladas e reversíveis | SP 800-53: CM-4 (Impact Analyses) e CM-3 (Configuration Change Control) |
| Componentes sem suporte | Substituir ou dar suporte alternativo a legados sem suporte | SP 800-53: SA-22 (Unsupported System Components) |
| Isolamento de legados | Isolar componentes em enclaves com mecanismos de fronteira | SP 800-53: SC-7(21) (Isolation of System Components) |
| Etapas de migração e ameaças | Atores, ativos, processos, políticas, soluções, implantação inicial, expansão; ameaças à ZTA | NIST SP 800-207, §7.3 e §5 |

## Aplicabilidade: on-premises, cloud e híbrido

Workloads novos em cloud podem nascer em Zero Trust; o datacenter e os legados exigem as ondas e os enclaves. Em ambientes híbridos, a ordem natural costuma ser: identidade (comum aos dois lados), acesso de usuários (ZTNA e acesso condicional), e por fim workloads (microsegmentação e identidade de workload), com o hub de conectividade (Módulo 11) como ponto de política entre ambientes.

## Como especificar e implementar

- "A migração para Zero Trust segue ondas com escopo, pré-requisitos, critérios de aceite, modo de falha e plano de reversão."
- "Cada sistema legado em enclave tem dono, fluxos mínimos, monitoração e data de saída."
- "A parcela de acesso baseada em perímetro é medida e reduzida a cada onda."
- "Cada onda é avaliada pelo efeito nos cenários críticos do register."

## Trade-offs, limitações e antipadrões

- **Trade-off:** ondas pequenas reduzem risco de execução, mas alongam o período híbrido.
- **Antipadrão — enclave permanente:** o legado nunca sai e o enclave cresce.
- **Antipadrão — plano por produto:** a onda é "implantar o produto X", sem critério de aceite.
- **Limitação:** a capacidade operacional da equipe é frequentemente o fator limitante — e precisa entrar no plano.

## Como validar

- Verificar, ao fim de cada onda, o critério de aceite com teste.
- Reexecutar o cenário de ataque (Módulo 4 — Aula 04) e contar pontos de interrupção.
- Medir a parcela de acessos ainda baseados em rede.
- Revisar os enclaves: tamanho, fluxos e datas de saída.

Critérios de aceite (do programa; cada onda tem os seus, como no exemplo da Meridiana):

| Critério | Evidência |
|:---|:---|
| Toda onda com escopo, pré-requisitos, critério de aceite testável, modo de falha e plano de reversão | Plano de ondas revisado |
| Critério de aceite de cada onda concluída verificado por teste | Registro do teste ao fim da onda |
| Parcela de acessos baseados em rede reduzida a cada onda | Medida da parcela antes e depois de cada onda |
| Todo enclave com dono, fluxos documentados e data de saída | Revisão dos enclaves |
| Pontos de interrupção do cenário crítico recontados a cada onda | Reexecução do cenário de ataque documentada |

## Como apresentar e justificar

- **Para a diretoria:** "Três ondas em 18 meses. Ao fim da primeira, o ataque de ransomware mais provável já encontra três barreiras; ao fim da terceira, seis."
- **Para as equipes:** "Cada onda começa em observação. Nada bloqueia sem duas semanas de dados."

## Checklist de revisão arquitetural

- [ ] Atores, ativos, processos e riscos identificados.
- [ ] Políticas formuladas por classe de recurso.
- [ ] Ondas com pré-requisitos, critérios de aceite e reversão.
- [ ] Legados em enclaves pequenos, com dono e data de saída.
- [ ] Riscos da própria ZTA tratados (decisão, disponibilidade, contas não humanas).
- [ ] Efeito medido nos cenários críticos.

## Questões de compreensão

**1.** Por que a SP 800-207 considera o modelo híbrido normal durante a transição?

??? success "Resposta comentada"

    Porque organizações com histórico costumam ter sistemas e processos que não podem migrar de uma vez. O importante é declarar o híbrido, reduzi-lo a cada onda e conhecer suas exceções.

**2.** Quais são as etapas de migração da seção 7.3?

??? success "Resposta comentada"

    Identificar atores; identificar ativos; identificar processos-chave e avaliar riscos; formular políticas; identificar soluções candidatas; implantação inicial e monitoração; expandir.

**3.** O que impede um enclave de legados de reproduzir o perímetro?

??? success "Resposta comentada"

    Mantê-lo pequeno, com fluxos mínimos e documentados, monitoração, dono e data de saída — e não colocá-lo diante de redes inteiras.

## Exercício de tomada de decisão

!!! question "Cenário: qual onda primeiro na Aurora"

    A Aurora tem orçamento para uma onda neste semestre. Opções: (A) microsegmentação de todo o datacenter; (B) acesso por aplicação (ZTNA) e acesso condicional com postura para usuários; (C) identidade de workload e mTLS no cluster do CDE. Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e recomende uma.

**Objetivos avaliados:** Priorizar ondas por redução de risco, dependências e capacidade da organização; tratar sistemas legados sem bloquear a evolução nem deixá-los invisíveis.

**Entrega esperada:** Matriz ponderada, a onda recomendada e o que precisa começar em paralelo para a onda seguinte.

**Critérios de avaliação:**

- A onda escolhida tem pré-requisitos prontos e termina no semestre.
- A resposta indica o trabalho preparatório (mapa de fluxos) que viabiliza a próxima onda.
- O risco residual do CDE durante o semestre é declarado e tem tratamento provisório.

??? success "Resolução de referência"

    | Critério | Peso | A — Microsegmentação do DC | B — ZTNA e postura | C — Workloads do CDE |
    |:---|:---|:---|:---|:---|
    | Redução de risco dos cenários críticos | 3 | 2 | 3 | 3 |
    | Pré-requisitos prontos | 2 | 1 | 3 | 2 |
    | Capacidade da equipe para operar | 2 | 1 | 2 | 2 |
    | Visibilidade do resultado | 1 | 2 | 3 | 2 |
    | **Total ponderado** | | **12** | **22** | **19** |

    - **Pesos:** a onda existe para reduzir o risco dos cenários críticos (peso 3). Pré-requisitos e capacidade pesam 2, porque uma onda que não termina no semestre não reduz risco algum. A visibilidade do resultado pesa 1.
    - **Recomendação: B**, com C como próxima onda. B interrompe o cenário de acesso remoto e tem pré-requisitos prontos (IdP, MDM). C é muito valiosa para o CDE, mas depende de inventário de serviços ainda incompleto. A, em todo o datacenter de uma vez, excede a capacidade da equipe e falta mapa de fluxos.
    - **Condição:** iniciar em paralelo o mapeamento de fluxos do CDE, para que C comece no semestre seguinte sem atraso.
    - **Trade-off aceito e risco residual:** durante o semestre, chamadas entre serviços do CDE continuam confiando na rede do cluster; um serviço comprometido no CDE ainda alcança os demais. O residual é tratado com as políticas de rede existentes e a monitoração do cluster até a onda C.
    - **O que mudaria a decisão:** uma auditoria do PCI DSS com achado sobre o CDE, ou um incidente no cluster, elevaria C para a primeira onda; se o inventário de serviços do CDE estiver completo antes do início do semestre, C passa a ter pré-requisitos prontos e fica próxima de B.

    **Erros comuns:**

    - Escolher a onda de maior valor teórico sem os pré-requisitos (inventário de serviços).
    - Planejar a microsegmentação de todo o datacenter de uma vez.
    - Não ligar a ordem das ondas aos cenários de risco.

## Pontos-chave

- O híbrido entre perímetro e Zero Trust é normal; declare-o e reduza-o.
- Siga as etapas da SP 800-207: atores, ativos, processos e riscos, políticas, soluções, implantação inicial, expansão.
- Legados vão para enclaves pequenos, com dono e data de saída.
- Priorize ondas por risco, dependências, capacidade e visibilidade.
- Meça o sucesso pelos cenários interrompidos, não pelos produtos implantados.

<!-- next-steps:start -->

!!! tip "Próximos passos"

    Você concluiu a última aula do **Módulo 7** — [voltar ao módulo](index.md).

    Em seguida: [Módulo 8 — On-Premises e Sistemas Legados](../../modules/08-onprem-legacy/index.md).

<!-- next-steps:end -->

## Referências

### Fundamentação principal

- NIST. *SP 800-207 — Zero Trust Architecture*. 2020 — §3.2.2 (pp. 14–15), §5 (pp. 28–30) e §7 (pp. 36–41). *(Lido; sumário das Seções 5 e 7 reconferido no PDF em 2026-10-29.)*
- NIST. *SP 1800-35 — Implementing a Zero Trust Architecture*. 2025 — notícia oficial conferida.
- CISA. *Zero Trust Maturity Model 2.0*. 2023 (fontes secundárias).
- NIST. *SP 800-215* — limitações de VPN e perímetro. *(Lido.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles CA-5, CM-3, CM-4, PL-8, SA-22 e SC-7(21), conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- NIST. *SP 800-207A* — aplicações cloud-native em vários locais.
- Microsoft. *The enterprise access model*.

### Aplicação prática

- Escreva um plano de três ondas para Zero Trust no seu ambiente, com escopo, pré-requisitos, critério de aceite testável e o cenário de risco que cada onda interrompe.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
