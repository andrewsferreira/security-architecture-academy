---
id: M05-L01
title: "Aula 01 — Zonas de confiança, segmentação e microsegmentação"
public_title: "Módulo 5 — Aula 01 — Zonas de confiança, segmentação e microsegmentação"
description: Como dividir uma rede em zonas de confiança, definir a matriz de fluxos permitidos entre elas e decidir quando a segmentação por zonas basta e quando é preciso microsegmentação com política por workload.
domain: network-security
tier: fundamental
status: published
prerequisites: [M00-L03, M01-L03]
objectives:
  - Definir zonas de confiança a partir de função, sensibilidade e exposição, e não da topologia física.
  - Especificar uma matriz de fluxos entre zonas com política negar por padrão.
  - Diferenciar segmentação por zonas e microsegmentação e escolher entre elas.
  - Reconhecer pré-requisitos e limites da microsegmentação baseada em identidade.
minutes: 75
sources: [NIST-SP800-215, NSA-NETWORK-INFRA-2022, NIST-SP800-41-R1, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [NIST-SP800-207, BOOK-GOOGLE-BSRS]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M05
---

# Aula 01 — Zonas de confiança, segmentação e microsegmentação { #zonas-de-confianca-segmentacao-e-microsegmentacao }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 5 · Nível 2</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">75 min · ID técnico: M05-L01</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Segmentar é limitar o raio de impacto (Módulo 4 — Aula 05) no plano da rede: garantir que comprometer um sistema não dê acesso automático a todos os outros. A segmentação começa com **zonas de confiança** definidas por função e sensibilidade, segue com uma **matriz de fluxos** explícita entre elas e, para ambientes dinâmicos ou críticos, chega à **microsegmentação**, com política por workload. Esta aula mostra como desenhar cada nível e como escolher o que é proporcional ao risco.

**Pré-requisitos:** [Segmentação e conectividade](../00-foundations/03-segmentation-connectivity.md) e [Trust boundaries e attack surface](../01-security-fundamentals/03-trust-boundaries-attack-surface.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Definir zonas de confiança a partir de função, sensibilidade e exposição, e não da topologia física.
- Especificar uma matriz de fluxos entre zonas com política negar por padrão.
- Diferenciar segmentação por zonas e microsegmentação e escolher entre elas.
- Reconhecer pré-requisitos e limites da microsegmentação baseada em identidade.

## Conceito

### Zona de confiança

Uma **zona de confiança** é um conjunto de sistemas com requisitos de segurança semelhantes, que podem ser tratados com a mesma política de entrada e saída. A NSA, em seu guia de segurança de infraestrutura de rede, recomenda **agrupar logicamente sistemas semelhantes** — estações, servidores, impressoras, telefonia — e lembra que tecnologia operacional normalmente precisa ser isolada das demais redes (Sec. 2.2).

Critérios para definir zonas:

| Critério | Pergunta | Exemplo de zona |
|:---|:---|:---|
| **Função** | O que o sistema faz? | Usuários, aplicações, dados, gestão |
| **Sensibilidade** | Que dados trata e com que impacto? | Ambiente de dados de cartão (CDE), dados de saúde |
| **Exposição** | Quem pode alcançá-lo? | DMZ (público), parceiros |
| **Confiabilidade do dispositivo** | Quem gerencia o dispositivo? | Visitantes, IoT, OT, legados sem suporte |
| **Dono e ciclo de vida** | Quem responde e com que frequência muda? | Laboratório, desenvolvimento, produção |

### Por que a rede plana é o problema

Em uma rede plana, qualquer sistema alcança qualquer outro. O cenário de ransomware da Meridiana (Módulo 4 — Aula 04) mostra a consequência: depois do acesso inicial, o movimento lateral não encontra barreiras. A NIST SP 800-215 registra que mais de 75% do tráfego de rede já é **east-west** (Sec. 2.1, p. 5) — e é exatamente esse tráfego que redes planas não controlam.

## Fundamentos técnicos

### Matriz de fluxos

A segmentação só vale se houver uma política explícita entre zonas. A forma mais clara é uma **matriz de fluxos** — origem, destino, protocolo, justificativa e dono —, aplicada com **negar por padrão**: a SP 800-41 Rev. 1 recomenda que firewalls bloqueiem todo tráfego de entrada e saída que não tenha sido expressamente permitido (Sec. 4, p. 4-1), e a NSA recomenda regras que permitam apenas o necessário e neguem o resto, com registro (Sec. 2.4).

| Origem | Destino | Protocolo | Justificativa | Dono |
|:---|:---|:---|:---|:---|
| Usuários | Aplicações | HTTPS (443) | Acesso às aplicações web internas | Infraestrutura |
| Aplicações | Dados | Protocolo do banco (porta específica) | Persistência | Dono da aplicação |
| Gestão | Todas | SSH, RDP, protocolos de gerenciamento | Administração | Infraestrutura |
| Usuários | Dados | — | **Negado**: acesso a dados só via aplicação | — |
| Usuários | Gestão | — | **Negado**: administração só a partir da zona de gestão | — |

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m05-l01-zones.mmd"
```

<figcaption>Figura 1 — À esquerda, segmentação por zonas com ponto de controle e matriz de fluxos; à direita, microsegmentação com política por workload na zona de aplicações.</figcaption>
</figure>

### Mecanismos de segmentação

| Mecanismo | Granularidade | Observações |
|:---|:---|:---|
| VLANs e sub-redes + firewall entre elas | Zona | Barato e conhecido; a SP 800-215 lembra que a política se aplica a sub-redes, não a hosts individuais (p. 19) |
| Firewall interno de datacenter | Zona | A SP 800-215 observa que firewalls dentro do datacenter podem segmentar a rede interna e impedir movimento lateral (p. 9) |
| Grupos de segurança e listas de controle em cloud | Workload ou conjunto | Política próxima do recurso; precisa de governança para não virar "permitir tudo" |
| Firewall de host ou de hypervisor | Workload | Política aplicada no próprio host ou na camada de virtualização |
| Política baseada em identidade de workload | Workload / serviço | Política por identidade, não por IP |

### Microsegmentação

A SP 800-215 descreve a microsegmentação como dividir a rede interna em segmentos isolados para que o tráfego de cada um possa ser monitorado e controlado, com o objetivo principal de impedir a escalada de ataques (pp. 17–18). O documento lista pré-requisitos importantes (pp. 18–19):

- **Identidade única de aplicação** — "inevitável", segundo o texto —, com identidade de workload confiável (o documento cita identificadores SPIFFE).
- **Descoberta de serviços** e **mapeamento à infraestrutura**.
- **Segmentação de workloads** coerente com as dependências reais.

E descreve três abordagens de implementação (pp. 20–21): **baseada em servidor virtualizado** (firewall de hypervisor ou overlays), **baseada em host** (agentes) e **baseada em identidade**, que usa identificadores contextuais da aplicação em vez de endereços IP.

### Zonas ou microsegmentação?

| Situação | Abordagem proporcional |
|:---|:---|
| Ambiente estável, poucas aplicações, equipe pequena | Zonas com matriz de fluxos e firewall interno |
| Ambiente regulado com escopo a reduzir (CDE) | Zona dedicada + microsegmentação dentro dela |
| Workloads dinâmicos (containers, autoscaling) | Microsegmentação baseada em identidade |
| Legados sem suporte | Zona de isolamento com fluxos mínimos (Módulo 8 — Aula 05) |

Microsegmentação sem conhecer as dependências reais quebra aplicações; por isso a implantação costuma começar em **modo de observação**, aprendendo os fluxos antes de bloquear.

## Exemplo empresarial

!!! example "Meridiana — da rede plana a seis zonas"

    A Meridiana tinha uma única rede para estações, servidores, coletores dos CDs e o servidor de etiquetas. O arquiteto propôs seis zonas — usuários, aplicações, dados, gestão, centros de distribuição e legados — e uma matriz com 23 fluxos permitidos, cada um com dono.

    A primeira versão do firewall interno ficou **duas semanas em modo de registro**, sem bloquear. Os logs revelaram 11 fluxos não documentados, entre eles uma rotina de exportação do ERP gravando diretamente no servidor de arquivos de uma estação de usuário. Nove fluxos foram incluídos na matriz com justificativa; dois foram eliminados. Só então o bloqueio foi ativado.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Estrutura | Rede plana ou VLANs sem política | Zonas por função, sensibilidade e exposição |
| Política | "Permitir tudo interno" | Matriz de fluxos com negar por padrão |
| Granularidade | Igual para tudo | Zonas onde basta; microsegmentação onde o risco exige |
| Implantação | Bloqueio imediato | Observação, documentação dos fluxos, depois bloqueio |
| Governança | Regras sem dono | Cada fluxo com justificativa, dono e revisão |

## Controles e padrões relevantes

Os controles abaixo são do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1. São referências voluntárias: ajudam a especificar e auditar a segmentação, mas a obrigação de aplicá-los vem de um contrato, de uma norma setorial (por exemplo, o PCI DSS para o CDE) ou da política da organização.

| Controle ou padrão | Objetivo na segmentação | Referência |
|:---|:---|:---|
| Imposição do fluxo de informação | Autorizar fluxos entre zonas segundo uma política explícita — a matriz de fluxos | SP 800-53: AC-4 (Information Flow Enforcement) |
| Separação lógica ou física de fluxos | Separar fluxos de natureza diferente, como gestão e dados de produção | SP 800-53: AC-4(21) (Physical or Logical Separation of Information Flows) |
| Proteção de fronteira | Controlar a comunicação nas interfaces externas e nas interfaces internas-chave entre zonas | SP 800-53: SC-7 (Boundary Protection) |
| Negar por padrão | Bloquear todo tráfego e permitir só as exceções da matriz | SP 800-53: SC-7(5) (Deny by Default — Allow by Exception); SP 800-41 Rev. 1, Sec. 4 |
| Particionamento do sistema | Colocar componentes em domínios separados conforme a criticidade | SP 800-53: SC-32 (System Partitioning) |
| Arquitetura de rede segura | Manter a arquitetura de rede, inclusive a segmentação, documentada e gerida | CIS Controls v8.1: Controle 12 (Network Infrastructure Management) |

## Aplicabilidade: on-premises, cloud e híbrido

Em on-premises, zonas são implementadas com VLANs, sub-redes e firewalls internos. Em cloud, a segmentação combina **contas ou assinaturas**, **redes virtuais**, **grupos de segurança** e **identidade de workload** — e a política fica próxima do recurso, o que facilita a microsegmentação, mas exige guardrails para evitar regras abertas. Em ambientes híbridos, a matriz de fluxos precisa cobrir as travessias entre ambientes, com um ponto de controle no hub de conectividade (Módulo 11).

## Como especificar e implementar

- "A rede é dividida em zonas de confiança definidas por função, sensibilidade e exposição."
- "Fluxos entre zonas seguem uma matriz documentada, com negar por padrão, justificativa e dono por fluxo."
- "Ambientes regulados e workloads críticos aplicam microsegmentação com política baseada em identidade de workload."
- "Novas regras de segmentação passam por período de observação antes do bloqueio."
- "A matriz é revisada periodicamente; fluxos sem uso são removidos."

## Trade-offs, limitações e antipadrões

- **Trade-off:** granularidade versus operação. Mais segmentos significam mais regras para manter e mais chamados por bloqueio indevido.
- **Antipadrão — VLAN sem firewall:** separação lógica sem política não impede movimento lateral.
- **Antipadrão — regra "any-any" temporária:** criada em um incidente e nunca removida.
- **Limitação:** segmentação de rede não protege contra abuso de credenciais em fluxos permitidos — por isso complementa, e não substitui, controles de identidade (Módulos 6 e 7).

## Como validar

- Testar, a partir de cada zona, fluxos que deveriam ser negados (por exemplo, usuário → banco).
- Comparar a matriz com telemetria de fluxos e investigar divergências.
- Revisar regras com contador zerado por 90 dias para remoção.

Critérios de aceite que podem ser medidos antes de declarar a segmentação concluída:

| Critério | Evidência |
|:---|:---|
| Todo fluxo permitido existe na matriz, com justificativa e dono | Exportação das regras do firewall comparada à matriz; nenhuma regra sem correspondência |
| Nenhuma regra "any-any" entre zonas | Relatório de regras do firewall interno |
| Fluxos proibidos bloqueados | Resultado dos testes a partir de cada zona (por exemplo, estação → banco e estação → gestão negados e registrados) |
| Divergências do período de observação tratadas | Lista de fluxos observados e não documentados, cada um incluído na matriz ou eliminado |
| Revisão periódica funcionando | Registro da última revisão e das regras removidas por falta de uso |

## Como apresentar e justificar

- **Para a diretoria:** "Hoje, um computador infectado alcança o ERP e o backup. Com seis zonas, ele alcança só o que um usuário precisa."
- **Para a operação:** "Duas semanas em modo de registro antes de bloquear. Nada quebra sem aviso."

## Checklist de revisão arquitetural

- [ ] Zonas definidas por função, sensibilidade e exposição.
- [ ] Matriz de fluxos com negar por padrão, justificativa e dono.
- [ ] Usuários não alcançam dados nem gestão diretamente.
- [ ] Microsegmentação onde o risco e a dinâmica do ambiente exigem.
- [ ] Período de observação antes do bloqueio.
- [ ] Fluxos negados testados periodicamente.

## Questões de compreensão

**1.** Por que VLANs sozinhas não constituem segmentação de segurança?

??? success "Resposta comentada"

    Porque separam domínios de broadcast, mas sem uma política aplicada entre elas (firewall ou listas de controle) o tráfego continua roteado livremente. Segmentação de segurança exige uma política explícita de fluxos permitidos.

**2.** Quais pré-requisitos a SP 800-215 aponta para a microsegmentação?

??? success "Resposta comentada"

    Identidade única e confiável de aplicação ou workload, descoberta de serviços, segmentação coerente com os workloads e mapeamento à infraestrutura. Sem conhecer identidades e dependências, a política quebra aplicações ou fica permissiva demais.

**3.** Por que começar em modo de observação?

??? success "Resposta comentada"

    Porque a documentação raramente reflete todos os fluxos reais. Observar primeiro revela dependências desconhecidas, que podem ser documentadas ou eliminadas antes de o bloqueio interromper a operação.

## Exercício de tomada de decisão

!!! question "Cenário: segmentar o portal do paciente da Lumen"

    O portal do paciente da Lumen roda em containers em cloud, com 12 serviços que escalam automaticamente, um banco de dados de agendamentos e uma fila de mensagens. Hoje, todos os serviços estão na mesma sub-rede e podem conversar entre si. O portal trata dados de saúde. A equipe de plataforma tem duas pessoas, e a diretoria pede a redução do risco de movimento lateral em até um trimestre, sem interromper o atendimento. Há três propostas:

    - **A** — zonas por sub-rede (borda, serviços e dados), com grupos de segurança entre elas;
    - **B** — as mesmas zonas, mais microsegmentação entre serviços com política baseada em identidade de workload, fornecida pela plataforma de containers;
    - **C** — microsegmentação com agente em cada host, com política baseada em endereço IP e rótulos.

    Compare as propostas com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e descreva o plano de implantação.

**Objetivos avaliados:** Diferenciar segmentação por zonas e microsegmentação e escolher entre elas; reconhecer pré-requisitos e limites da microsegmentação baseada em identidade.

**Entrega esperada:** Matriz ponderada preenchida, recomendação com plano de implantação em etapas e o risco residual declarado, em até uma página.

**Critérios de avaliação:**

- A recomendação conecta a política entre serviços ao comportamento da plataforma (escala automática, endereços que mudam).
- O plano começa por observação de fluxos e só depois bloqueia, na ordem de maior risco (banco e fila primeiro).
- O risco residual reconhece que um serviço comprometido ainda alcança o que chama legitimamente, e diz como isso é tratado.

??? success "Resolução de referência"

    | Critério | Peso | A — Zonas por sub-rede | B — Zonas + identidade de workload | C — Agente por host |
    |:---|:---|:---|:---|:---|
    | Contenção de movimento lateral entre serviços | 3 | 1 | 3 | 2 |
    | Compatibilidade com escala automática e IPs dinâmicos | 3 | 2 | 3 | 1 |
    | Esforço de operação para uma equipe de duas pessoas | 2 | 3 | 2 | 1 |
    | Risco de interromper o atendimento na implantação | 2 | 3 | 2 | 2 |
    | **Total ponderado** | | **21** | **26** | **15** |

    - **Pesos:** o motivo da iniciativa é conter o movimento lateral em um sistema com dados de saúde, e a política precisa sobreviver à escala automática — sem isso, ela vira "permitir tudo" na primeira expansão. Os dois critérios pesam 3. A capacidade da equipe e o risco de interrupção são restrições reais, mas administráveis com observação antes do bloqueio (peso 2).
    - **Recomendação: B.** As zonas resolvem o essencial (o banco só aceita conexões da zona de serviços, na porta do banco), e a política por identidade de workload define quais serviços chamam quais — por exemplo, só o serviço de agendamento grava no banco de agendamentos —, sem depender de endereços que mudam. A proposta C contém mais que A, mas política por IP em ambiente com escala automática exige atualização constante e quebra com facilidade.
    - **Implantação:** (1) habilitar telemetria de fluxos e mapear as chamadas reais por duas semanas; (2) aplicar as zonas e a política entre serviços em modo de auditoria; (3) bloquear primeiro o acesso ao banco e à fila; (4) depois, os fluxos entre serviços, um grupo por vez.
    - **Trade-off aceito e risco residual:** a política entre serviços aumenta o trabalho da equipe e depende de a plataforma emitir identidades confiáveis. Um serviço comprometido ainda alcança os serviços que legitimamente chama; o risco é reduzido com autenticação mútua entre serviços (Módulo 7 — Aula 05) e monitoramento das chamadas.
    - **O que mudaria a decisão:** se a plataforma não oferecer identidade de workload e não houver como adotá-la no trimestre, A é o primeiro passo defensável, com B planejado; se parte dos serviços rodar em máquinas virtuais estáveis, fora da plataforma de containers, C pode ser adequado para esse trecho.

    A matriz organiza a comparação, mas não substitui o julgamento: se uma norma aplicável exigisse isolamento específico dos dados de saúde, a exigência valeria antes de qualquer soma.

    **Erros comuns:**

    - Escolher a opção mais granular sem considerar a capacidade de uma equipe de duas pessoas.
    - Tratar política por endereço IP como equivalente a política por identidade de workload em ambiente com escala automática.
    - Ativar o bloqueio sem período de observação e sem mapa das chamadas reais.

## Pontos-chave

- Zonas de confiança agrupam sistemas com requisitos semelhantes, por função, sensibilidade e exposição.
- A segmentação só vale com uma matriz de fluxos e negar por padrão.
- Mais de 75% do tráfego é east-west, segundo a SP 800-215 — e redes planas não o controlam.
- Microsegmentação aplica política por workload e depende de identidade de workload e de descoberta de dependências.
- Observar antes de bloquear evita interromper a operação.

## Referências

### Fundamentação principal

- NIST. *SP 800-215 — Guide to a Secure Enterprise Network Landscape*. R. Chandramouli, 2022. <https://csrc.nist.gov/pubs/sp/800/215/final> — Sec. 2.1 (p. 5), Sec. 3 (p. 9) e Sec. 5 (pp. 17–21). *(Lido.)*
- NSA. *Network Infrastructure Security Guidance* (PP-22-0266), mar. 2022 — Sec. 2.2 e 2.4. *(Lido.)*
- NIST. *SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy*. 2009. <https://csrc.nist.gov/pubs/sp/800/41/r1/final> — Sec. 4, *deny by default* (p. 4-1). *(Lido.)*
- NIST. *SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations*, Release 5.2.0. <https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final> — controles AC-4, AC-4(21), SC-7, SC-7(5) e SC-32, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1*. <https://www.cisecurity.org/controls/v8-1> — Controle 12 — gratuito.

### Leitura complementar

- NIST. *SP 800-207 — Zero Trust Architecture* — segmentação no contexto de Zero Trust (Módulo 7).
- H. Adkins et al. *Building Secure and Reliable Systems* — Cap. 8, compartimentalização.

### Aplicação prática

- Monte a matriz de fluxos entre as zonas de um ambiente que você conhece. Marque os fluxos sem justificativa e os que deveriam ser negados.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
