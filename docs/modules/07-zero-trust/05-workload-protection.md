---
id: M07-L05
title: "Aula 05 — Segmentação e proteção de workloads"
public_title: "Módulo 7 — Aula 05 — Segmentação e proteção de workloads"
description: Como aplicar Zero Trust à comunicação entre serviços — identidade de workload, TLS mútuo, políticas de nível de identidade e de rede, service mesh, gateways e telemetria — em aplicações distribuídas entre nuvem e datacenter.
domain: zero-trust
tier: professional
status: published
prerequisites: [M07-L03, M06-L07, M05-L01]
objectives:
  - Explicar por que a comunicação serviço a serviço precisa de autenticação e autorização próprias.
  - Combinar políticas de nível de identidade e de nível de rede, conforme a SP 800-207A.
  - Avaliar service mesh, gateways e agentes como pontos de aplicação para workloads.
  - Especificar telemetria e detecção para tráfego entre serviços.
minutes: 60
sources: [NIST-SP800-207A, NIST-SP800-207, NIST-SP800-215, SPIFFE-CONCEPTS, NIST-SP800-53]
further_reading: [NIST-SP800-204, K8S-SECURITY-OVERVIEW, GCP-WORKLOAD-IDENTITY-FED]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M07
---

# Aula 05 — Segmentação e proteção de workloads { #segmentacao-e-protecao-de-workloads }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 7 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M07-L05</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    O segundo princípio da SP 800-207 — toda comunicação protegida, independentemente da localização — vale também para **serviços conversando com serviços**. Em aplicações distribuídas, a maioria das chamadas não envolve usuário: é um serviço pedindo algo a outro, às vezes em outra nuvem ou no datacenter. Esta aula mostra como dar a cada workload uma identidade, autenticar e autorizar cada chamada e observar o tráfego, combinando políticas de identidade e de rede.

**Pré-requisitos:** [Abordagens e modelos de implantação](03-approaches-deployment.md), [Workload Identity Federation](../06-iam/07-workload-identity-federation.md) e [Zonas e microsegmentação](../05-network-security/01-zones-segmentation.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar por que a comunicação serviço a serviço precisa de autenticação e autorização próprias.
- Combinar políticas de nível de identidade e de nível de rede, conforme a SP 800-207A.
- Avaliar service mesh, gateways e agentes como pontos de aplicação para workloads.
- Especificar telemetria e detecção para tráfego entre serviços.

## Conceito

### O problema

Em muitas arquiteturas de microsserviços, qualquer serviço dentro do cluster ou da rede virtual consegue chamar qualquer outro, sem autenticação — porque "está dentro". Um único serviço comprometido (por uma dependência vulnerável, por exemplo) alcança todos os outros e seus dados. É o movimento lateral (Módulo 5 — Aula 03) no nível de aplicação.

### Identidade de workload como base

A SP 800-215 afirma, entre os pré-requisitos da microsegmentação, que uma **identidade única de aplicação é inevitável** e dá o SPIFFE ID como exemplo de identidade de workload (Sec. 5.1.1, p. 18); a SP 800-207A descreve o SPIFFE ID como uma cadeia que identifica de forma única e específica um workload (Sec. 4.6.2, p. 18). O SPIFFE entrega a cada workload um documento de identidade (X.509-SVID ou JWT-SVID) pela Workload API, com a chave privada correspondente e um *trust bundle* para validar os outros (Módulo 6 — Aula 06).

### Políticas de identidade e de rede

A SP 800-207A, de setembro de 2023, trata de aplicações cloud-native distribuídas em vários ambientes de nuvem e on-premises e propõe políticas em múltiplas camadas (Sec. 3.3, pp. 9–11):

- **Políticas de nível de identidade** (*identity-tier*) — escopo de acesso a serviços e recursos com base nas identidades de serviços e de usuários: qual serviço pode chamar qual serviço, com que operação.
- **Políticas de nível de rede** (*network-tier*) — a comunicação permitida entre elementos da rede: que segmentos e portas são alcançáveis.
- **Componentes** que as aplicam: gateways de entrada, saída e borda, *sidecar proxies* entre serviços do cluster e uma infraestrutura de identidade de aplicação, como o SPIFFE (Sec. 2.1 e 4.5).
- **Monitoração e telemetria** para ajustar direitos de acesso — conceder, revogar, restringir — e para exigir autenticação adicional (*step-up*) (seção sobre o arcabouço de monitoração, pp. 20–21).
- Uma plataforma integrada, o **service mesh**, que reúne os serviços de aplicação (sumário executivo, p. 1; Sec. 4.2).

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m07-l05-workloads.mmd"
```

<figcaption>Figura 1 — Serviços em nuvem e no datacenter com identidade de workload, mTLS e políticas de identidade e de rede aplicadas por proxies, com telemetria das chamadas.</figcaption>
</figure>

## Fundamentos técnicos

### Camadas de proteção de workloads

| Camada | Pergunta | Mecanismo |
|:---|:---|:---|
| **Rede** | Este segmento pode alcançar aquele? | Grupos de segurança, políticas de rede do cluster, firewall interno |
| **Identidade** | Quem está chamando? | mTLS com identidade de workload (SVID, identidade gerenciada) |
| **Autorização** | Este serviço pode fazer esta operação? | Políticas por serviço e operação no proxy ou na aplicação |
| **Dados** | Este registro pertence a quem pede? | Autorização por objeto na aplicação (Módulo 6 — Aula 02, Módulo 12) |
| **Observação** | O padrão de chamadas mudou? | Telemetria de chamadas e detecção |

As camadas se complementam: política de rede sozinha não distingue serviços no mesmo segmento; identidade sozinha não impede um workload de varrer a rede.

### Pontos de aplicação para workloads

| Opção | Como funciona | Vantagem | Cuidado |
|:---|:---|:---|:---|
| **Service mesh** (proxy ao lado de cada serviço) | Proxies fazem mTLS e aplicam política, configurados centralmente | Transparente para o código; telemetria uniforme | Complexidade operacional; o plano de controle do mesh é crítico |
| **Bibliotecas na aplicação** | O próprio serviço valida identidade e autoriza | Sem componente extra | Inconsistência entre linguagens e equipes |
| **Gateway de API interno** | Chamadas entre domínios passam por gateway | Bom para fronteiras entre domínios | Pode virar gargalo; não cobre chamadas dentro do domínio |
| **Agente no host** | Política aplicada no sistema operacional | Funciona com legados | Granularidade por processo, não por operação |

A NIST SP 800-204 trata de estratégias de segurança para microsserviços e é leitura complementar para o desenho do mesh; a arquitetura de microsserviços é apresentada no Módulo Inicial — Aula 05.

### Telemetria e detecção

Com identidades em cada chamada, a telemetria passa a dizer **quem chamou quem**, não só qual IP falou com qual IP. Detecções úteis:

- Serviço chamando outro com o qual nunca falou.
- Operação nova (por exemplo, exportação em massa) por um serviço que só fazia leituras pontuais.
- Falhas de autenticação mútua repetidas — certificado inválido ou identidade não autorizada.

## Exemplo empresarial

!!! example "Aurora Pagamentos — o serviço de relatórios e o serviço de autorização"

    No ambiente de antecipação de recebíveis da Aurora, qualquer serviço do cluster podia chamar o serviço de autorização de pagamentos. Um teste mostrou que o serviço de relatórios — exposto internamente a analistas e com uma dependência vulnerável — conseguia submeter autorizações.

    A equipe adotou identidade de workload e mTLS em todo o cluster, com políticas de identidade em modo de auditoria por duas semanas (para descobrir as chamadas reais) e depois em modo de bloqueio. O serviço de autorização passou a aceitar apenas o serviço de antecipação, apenas na operação de autorização. A telemetria revelou ainda dois jobs agendados que chamavam serviços sem necessidade — removidos.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Confiança entre serviços | Rede do cluster | Identidade de workload com mTLS |
| Autorização | Nenhuma ou por IP | Por serviço e operação |
| Credenciais de serviço | Segredos estáticos | Certificados de curta duração emitidos pela plataforma |
| Visibilidade | IP para IP | Serviço para serviço, com operação |
| Implantação | Bloqueio imediato | Auditoria, ajuste e bloqueio |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referências voluntárias para a proteção serviço a serviço, e o modelo da SP 800-207A:

| Controle ou padrão | Objetivo na proteção de workloads | Referência |
|:---|:---|:---|
| Autenticação de serviços | Identificar e autenticar o serviço chamador antes da comunicação | SP 800-53: IA-9 (Service Identification and Authentication) |
| Comunicação protegida | mTLS: confidencialidade e integridade na transmissão por criptografia | SP 800-53: SC-8 e SC-8(1) (Cryptographic Protection) |
| Autorização por serviço e operação | Aplicar as autorizações aprovadas a cada chamada | SP 800-53: AC-3 (Access Enforcement) |
| Políticas de rede | Controlar fluxos entre segmentos e negar por padrão | SP 800-53: AC-4 (Information Flow Enforcement) e SC-7(5) (Deny by Default — Allow by Exception) |
| Telemetria e detecção | Monitorar o sistema e analisar o tráfego em pontos internos selecionados para descobrir anomalias | SP 800-53: SI-4 (System Monitoring) e SI-4(11) (Analyze Communications Traffic Anomalies) |
| Políticas em múltiplas camadas | Políticas de identidade e de rede, aplicadas por gateways, *sidecars* e identidade de aplicação | NIST SP 800-207A, Sec. 3.3 e 4 |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, identidades gerenciadas, políticas de rede de clusters e meshes gerenciados facilitam a adoção. On-premises, agentes e meshes em clusters locais cumprem o mesmo papel. Em ambientes híbridos, um **domínio de confiança** comum (ou federação entre domínios) permite que um serviço na nuvem autentique um serviço no datacenter sem depender da VPN como mecanismo de confiança — a SP 800-207A trata exatamente desse cenário de múltiplos locais.

## Como especificar e implementar

- "Todo workload tem identidade emitida pela plataforma, com credenciais de curta duração."
- "Chamadas entre serviços usam autenticação mútua e são autorizadas por serviço e operação."
- "Políticas de rede limitam os segmentos alcançáveis por cada workload, complementando as políticas de identidade."
- "Políticas novas entram em modo de auditoria antes do bloqueio."
- "Telemetria de chamadas entre serviços é enviada ao SIEM, com detecções de comportamento novo."

## Trade-offs, limitações e antipadrões

- **Trade-off:** service mesh traz uniformidade e telemetria ao custo de complexidade; para poucos serviços, bibliotecas ou gateways podem bastar.
- **Antipadrão — mTLS sem autorização:** todos os serviços se autenticam, mas qualquer um pode chamar qualquer operação.
- **Antipadrão — exceções permanentes "para o job noturno".**
- **Limitação:** identidade de workload não protege contra um serviço legítimo comprometido usando seus próprios direitos — reduz o alcance, não elimina o risco.

## Como validar

- A partir de um serviço, tentar chamar uma operação não autorizada em outro serviço.
- Apresentar um certificado expirado ou de outro domínio de confiança e verificar a rejeição.
- Comparar o grafo de chamadas real com as políticas.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Chamada a operação não autorizada é negada | Teste a partir de um serviço sem permissão, com o registro da negação |
| Certificado expirado ou de outro domínio de confiança é rejeitado | Teste com certificado inválido |
| Nenhuma chamada observada fora das políticas | Grafo de chamadas da telemetria comparado às políticas, sem divergência não explicada |
| Toda política nova passou por modo de auditoria antes do bloqueio | Histórico de mudanças com período de auditoria |

## Como apresentar e justificar

- **Para a diretoria:** "Um serviço de relatórios conseguia autorizar pagamentos. Agora cada serviço só faz o que precisa, e o sistema registra quem chamou quem."
- **Para engenharia:** "A identidade vem da plataforma; ninguém gerencia certificados à mão. As políticas são código revisado."

## Checklist de revisão arquitetural

- [ ] Workloads com identidade emitida pela plataforma.
- [ ] mTLS em chamadas entre serviços.
- [ ] Autorização por serviço e operação.
- [ ] Políticas de rede complementares.
- [ ] Modo de auditoria antes do bloqueio.
- [ ] Telemetria serviço a serviço com detecções.

## Questões de compreensão

**1.** Por que políticas de rede não bastam para proteger serviços no mesmo cluster?

??? success "Resposta comentada"

    Porque serviços no mesmo segmento são indistinguíveis por rede; endereços mudam com escalonamento. Só a identidade de workload permite dizer qual serviço está chamando e autorizar a operação.

**2.** Por que, para workloads cloud-native, a SP 800-207A combina políticas de nível de identidade com políticas de nível de rede, em vez de usar só uma delas?

??? success "Resposta comentada"

    Políticas só de rede não distinguem serviços que compartilham um segmento nem acompanham endereços que mudam com o escalonamento; políticas só de identidade não limitam o alcance de rede de um serviço comprometido. A combinação, aplicada por gateways e pela infraestrutura de identidade de serviço — como um service mesh —, com monitoração e telemetria, cobre as duas lacunas.

**3.** Qual o risco de mTLS sem autorização?

??? success "Resposta comentada"

    Todos os serviços provam quem são, mas qualquer serviço autenticado pode chamar qualquer operação de qualquer outro. A autenticação precisa ser seguida de autorização por serviço e operação.

## Exercício de tomada de decisão

!!! question "Cenário: chamada da nuvem ao datacenter na Lumen"

    O portal do paciente, em nuvem, precisa consultar o sistema de agenda, que roda no datacenter da Lumen. Hoje a chamada passa pela VPN site a site e o sistema de agenda aceita qualquer origem da rede da nuvem. As opções são:

    - **A** — manter a VPN e restringir o firewall do datacenter à sub-rede do portal;
    - **B** — gateway no datacenter que exige mTLS e valida a identidade de workload do portal, com autorização por operação e rede restrita ao hub de trânsito;
    - **C** — publicar a API de agenda em um gateway de API na internet, com OAuth 2.0 *client credentials*, sem passar pela VPN.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e proponha a arquitetura de proteção.

**Objetivos avaliados:** Combinar políticas de nível de identidade e de nível de rede, conforme a SP 800-207A; avaliar service mesh, gateways e agentes como pontos de aplicação para workloads.

**Entrega esperada:** Matriz ponderada e a arquitetura de proteção: identidade, autorização por operação, rede, telemetria e efeito esperado.

**Critérios de avaliação:**

- A solução identifica o serviço chamador por identidade de workload, não pela sub-rede.
- A autorização limita as operações permitidas, além de autenticar.
- A rede continua restrita, combinando política de identidade e de rede, como na SP 800-207A.

??? success "Resolução de referência"

    | Critério | Peso | A — VPN com firewall restrito | B — Gateway com mTLS e identidade de workload | C — Gateway de API na internet |
    |:---|:---|:---|:---|:---|
    | Identificação e autorização do serviço chamador | 3 | 1 | 3 | 2 |
    | Exposição do sistema de agenda | 2 | 2 | 3 | 1 |
    | Esforço de implantação e operação | 2 | 3 | 1 | 2 |
    | Independência da VPN como mecanismo de confiança | 1 | 1 | 3 | 3 |
    | **Total ponderado** | | **14** | **20** | **15** |

    - **Pesos:** o problema é a agenda aceitar qualquer origem da rede da nuvem — saber quem chama e o que pode fazer pesa 3. Exposição e esforço pesam 2. A independência da VPN pesa 1: é desejável, mas a VPN pode continuar como transporte.
    - **Recomendação: B.** Só B identifica o serviço do portal e limita as operações sem expor a agenda à internet. A restringe a rede, mas qualquer workload na sub-rede do portal continua aceito; C autentica o cliente, mas expõe um sistema interno à internet e depende de um segredo de cliente, salvo se usar autenticação por chave privada.

    - **Identidade:** o serviço do portal recebe identidade de workload; o sistema de agenda é publicado por um gateway no datacenter que exige mTLS e valida a identidade do serviço do portal (domínio de confiança comum ou federação).
    - **Autorização:** o gateway permite apenas as operações de consulta de horários e criação de agendamento, apenas para o serviço do portal.
    - **Rede:** o gateway aceita conexões apenas a partir do hub de trânsito da nuvem (Módulo 11), e o sistema de agenda só aceita conexões do gateway.
    - **Telemetria:** chamadas registradas com identidade e operação; alerta para volume anômalo.
    - **Efeito:** a VPN deixa de ser o mecanismo de confiança; comprometer outro workload na nuvem não dá acesso ao sistema de agenda.
    - **Trade-off aceito e risco residual:** o gateway e a infraestrutura de identidade são novos componentes críticos, com certificados a manter; o comprometimento do próprio serviço do portal continua dando acesso às duas operações permitidas. O residual é limitado pela autorização por operação e pelo alerta de volume.
    - **O que mudaria a decisão:** se a Lumen não tiver infraestrutura de identidade de workload nem previsão de tê-la, A com regra restrita ao endereço do serviço (não à sub-rede) é a medida provisória; se a agenda for consumida também por parceiros externos, um gateway de API (C) com autenticação do cliente por chave privada e tokens restritos ao remetente passa a fazer sentido.

    **Erros comuns:**

    - Considerar a VPN site a site como mecanismo de confiança.
    - Publicar um sistema interno na internet para resolver um problema de identidade.
    - Autenticar o chamador sem restringir as operações que ele pode executar.

## Pontos-chave

- Serviço a serviço também precisa de autenticação e autorização — "estar dentro" não basta.
- Identidade de workload emitida pela plataforma é a base.
- Combine políticas de identidade (quem chama e o quê) com políticas de rede (o que é alcançável).
- Service mesh, bibliotecas, gateways e agentes são opções de PEP para workloads.
- Telemetria com identidade revela comportamentos novos e caminhos não autorizados.

## Referências

### Fundamentação principal

- NIST. *SP 800-207A — A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Location Environments*. 2023. <https://csrc.nist.gov/pubs/sp/800/207/a/final> — sumário executivo, Sec. 2.1, 3.3, 4.2, 4.5, 4.6.2 e arcabouço de monitoração (pp. 20–21). *(Lido em 2026-10-29.)*
- NIST. *SP 800-207* — princípio 2 (§2.1). *(Lido.)*
- NIST. *SP 800-215* — identidade única de aplicação (Sec. 5.1.1, p. 18). *(Lido; reconferido em 2026-10-29.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-3, AC-4, IA-9, SC-7(5), SC-8, SC-8(1), SI-4 e SI-4(11), conferidos no catálogo OSCAL oficial — gratuito.
- SPIFFE. *SPIFFE Concepts*. *(Lido.)*

### Leitura complementar

- NIST. *SP 800-204 — Security Strategies for Microservices-based Application Systems*.
- Kubernetes. *Security overview*.
- Google Cloud. *Workload Identity Federation*.

### Aplicação prática

- Desenhe o grafo de chamadas de uma aplicação distribuída que você conhece e escreva a política de identidade para três chamadas críticas: serviço de origem, serviço de destino e operações permitidas.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
