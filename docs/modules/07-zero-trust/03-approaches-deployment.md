---
id: M07-L03
title: "Aula 03 — Abordagens identity-centric, resource-centric e de rede"
public_title: "Módulo 7 — Aula 03 — Abordagens identity-centric, resource-centric e de rede"
description: As três abordagens de Zero Trust descritas pela NIST SP 800-207 — governança de identidade reforçada, microsegmentação e infraestrutura de rede com perímetros definidos por software —, os quatro modelos de implantação e como combiná-los conforme o tipo de recurso, de usuário e de dispositivo.
domain: zero-trust
tier: professional
status: published
prerequisites: [M07-L02]
objectives:
  - Diferenciar as abordagens centradas em identidade, em recurso (microsegmentação) e em rede (SDP).
  - Comparar os modelos de implantação agente/gateway, gateway de enclave, portal de recursos e sandboxing.
  - Escolher a combinação adequada a cada classe de recurso e de dispositivo.
  - Reconhecer os limites de visibilidade de cada modelo.
minutes: 60
sources: [NIST-SP800-207, NIST-SP800-215, NIST-SP800-207A, NIST-SP800-53]
further_reading: [NIST-SP1800-35, SPIFFE-CONCEPTS]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M07
---

# Aula 03 — Abordagens identity-centric, resource-centric e de rede { #abordagens-identity-centric-resource-centric-e-de-rede }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 7 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M07-L03</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Não há uma única forma de implantar Zero Trust. A NIST SP 800-207 descreve três **abordagens** — dar à identidade o papel principal, proteger recursos com microsegmentação ou reconfigurar a rede com perímetros definidos por software — e quatro **modelos de implantação** que posicionam os pontos de aplicação de política de formas diferentes. Organizações reais combinam várias. Esta aula ajuda a escolher a combinação certa para cada classe de recurso.

**Pré-requisito:** [Componentes lógicos](02-logical-components.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Diferenciar as abordagens centradas em identidade, em recurso (microsegmentação) e em rede (SDP).
- Comparar os modelos de implantação agente/gateway, gateway de enclave, portal de recursos e sandboxing.
- Escolher a combinação adequada a cada classe de recurso e de dispositivo.
- Reconhecer os limites de visibilidade de cada modelo.

## Conceito

### Três abordagens

| Abordagem (§3.1) | Ideia central | Melhor para |
|:---|:---|:---|
| **Governança de identidade reforçada** (§3.1.1) | A identidade dos atores é o componente-chave da criação de políticas | SaaS, aplicações web, ambientes com IdP maduro |
| **Microsegmentação** (§3.1.2) | Recursos individuais ou grupos de recursos em segmentos próprios, protegidos por um componente de segurança de gateway | Datacenters, workloads críticos, ambientes regulados |
| **Infraestrutura de rede e perímetros definidos por software** (§3.1.3) | O PA atua como controlador de rede e reconfigura a rede conforme as decisões do PE | Acesso a aplicações internas sem expô-las; overlays |

A SP 800-215 descreve o **SDP** como abordagem que torna os recursos invisíveis até que o usuário seja autenticado e autorizado, com reavaliação contínua e privilégio mínimo (pp. 21–22).

### Quatro modelos de implantação

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m07-l03-deployment-models.mmd"
```

<figcaption>Figura 1 — Modelos de implantação da SP 800-207: agente e gateway, gateway de enclave, portal de recursos e sandboxing de aplicações.</figcaption>
</figure>

| Modelo (§3.2) | Como funciona | Vantagem | Limitação |
|:---|:---|:---|:---|
| **Agente e gateway** (§3.2.1) | Agente no dispositivo e gateway diante de cada recurso | Maior visibilidade e controle | Exige gestão forte de dispositivos |
| **Gateway de enclave** (§3.2.2) | Um gateway protege um grupo de recursos | Útil para legados | Sujeitos podem ver recursos do enclave que não estão autorizados a usar |
| **Portal de recursos** (§3.2.3) | Portal único diante dos recursos, sem software no cliente | Bom para terceiros e dispositivos não gerenciados | Só analisa o dispositivo quando ele se conecta ao portal — sem visibilidade entre sessões |
| **Sandboxing de aplicações** (§3.2.4) | Aplicações aprovadas executam em compartimentos isolados no dispositivo | Protege a aplicação de um dispositivo potencialmente comprometido | Exige ecossistema de aplicações compatível |

## Fundamentos técnicos

### Escolhendo por classe de recurso e de dispositivo

| Recurso | Dispositivo gerenciado | Dispositivo não gerenciado (terceiro, BYOD) |
|:---|:---|:---|
| **SaaS e aplicações web modernas** | Identidade reforçada + postura (agente) | Identidade reforçada + portal ou acesso restrito (sem download) |
| **Aplicações internas web** | ZTNA com agente e gateway | ZTNA em modo portal |
| **Aplicações internas legadas (protocolos antigos)** | Gateway de enclave com fluxos mínimos | Portal com sessão remota isolada (VDI) |
| **Workloads e dados críticos (serviço a serviço)** | Microsegmentação com identidade de workload (Aula 05) | Não se aplica |
| **Administração** | Caminho privilegiado (Módulo 6 — Aula 06) | Não permitido |

### Microsegmentação na prática

A SP 800-215 descreve três implementações de microsegmentação — baseada em servidor virtualizado, baseada em host e baseada em identidade — e destaca a identidade única de aplicação como pré-requisito (Sec. 5.1.1 e 5.1.2, pp. 18–21; Módulo 5 — Aula 01). Para aplicações cloud-native distribuídas em vários ambientes, a SP 800-207A recomenda **políticas de nível de identidade e de nível de rede** aplicadas por gateways e infraestrutura de identidade de serviço, com apoio de uma infraestrutura integrada como um **service mesh**.

### Visibilidade e trade-offs

| Modelo | O que o PDP sabe sobre o dispositivo |
|:---|:---|
| Agente e gateway | Muito: postura contínua pelo agente |
| Gateway de enclave | Depende do que o cliente informa; dentro do enclave, pouco controle por recurso |
| Portal | Pouco: só o que o navegador revela durante a sessão |
| Sandboxing | Estado da aplicação isolada, não do dispositivo inteiro |

Por isso a mesma organização costuma aplicar políticas **mais restritivas** quando a visibilidade é menor — por exemplo, acesso somente leitura e sem download via portal.

## Exemplo empresarial

!!! example "Aurora Pagamentos — combinação por classe"

    A Aurora mapeou suas 140 aplicações em cinco classes e escolheu o modelo de cada uma:

    | Classe | Exemplos | Modelo |
    |:---|:---|:---|
    | SaaS corporativo | E-mail, RH, CRM | Identidade reforçada com postura |
    | Web interna | Portal de lojistas interno, BI | ZTNA agente e gateway; portal para terceiros |
    | Legado com cliente pesado | Sistema de conciliação antigo | Gateway de enclave + VDI para terceiros |
    | Serviços do CDE | Tokenização, autorização | Microsegmentação com identidade de workload |
    | Administração | Consoles, servidores | Caminho privilegiado |

    O sistema de conciliação ficou em um enclave com três fluxos permitidos e virou prioridade de modernização — o próprio modelo tornou visível a limitação.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Estratégia | Um modelo para tudo | Combinação por classe de recurso e de dispositivo |
| Legados | Fora do escopo | Enclave com fluxos mínimos e plano de modernização |
| Terceiros | VPN | Portal ou VDI com restrições proporcionais à visibilidade |
| Workloads | Rede confiável | Microsegmentação com identidade de workload |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referências voluntárias que correspondem às escolhas de abordagem e de modelo:

| Controle ou padrão | Objetivo na escolha do modelo | Referência |
|:---|:---|:---|
| Acesso remoto | Restrições, requisitos de conexão e autorização para cada tipo de acesso remoto | SP 800-53: AC-17 (Remote Access) |
| Sistemas externos e não gerenciados | Permitir uso de dispositivos de terceiros só nas condições definidas, com limites de uso | SP 800-53: AC-20 (Use of External Systems) e AC-20(1) (Limits on Authorized Use) |
| Fluxos mínimos no enclave | Controlar os fluxos de informação entre o gateway e os recursos | SP 800-53: AC-4 (Information Flow Enforcement) |
| Isolamento de componentes | Isolar componentes críticos por mecanismos de fronteira (microsegmentação, enclave) | SP 800-53: SC-7(21) (Isolation of System Components) |
| Isolamento de execução | Domínio de execução separado — a base do sandboxing de aplicações | SP 800-53: SC-39 (Process Isolation) |
| Abordagens e modelos de implantação | Identidade reforçada, microsegmentação, SDP; agente e gateway, enclave, portal, sandboxing | NIST SP 800-207, §3.1 e §3.2 |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, a abordagem de identidade reforçada é quase nativa, e a microsegmentação usa grupos de segurança, políticas de rede e identidade de serviço. On-premises, gateways de enclave e ZTNA com conectores fazem a ponte para aplicações que não conhecem identidade moderna. Em ambientes híbridos, o desafio é aplicar a mesma classificação e a mesma política a aplicações nos dois lados.

## Como especificar e implementar

- "Cada aplicação é classificada e protegida pelo modelo de implantação definido para sua classe."
- "Acessos a partir de dispositivos não gerenciados usam portal ou sessão isolada, com restrições proporcionais à visibilidade."
- "Aplicações legadas ficam em enclaves com fluxos mínimos e plano de modernização."
- "Comunicação entre workloads críticos usa microsegmentação com identidade de workload."

## Trade-offs, limitações e antipadrões

- **Trade-off:** o modelo mais forte (agente e gateway) é também o mais exigente em gestão de dispositivos.
- **Antipadrão — enclave grande:** um gateway "Zero Trust" na frente de uma rede inteira reproduz o perímetro.
- **Antipadrão — portal com acesso total para terceiros:** visibilidade baixa com permissões altas.
- **Limitação:** os modelos da SP 800-207 são abstratos; produtos reais combinam vários deles.

## Como validar

- Para cada classe, verificar se as aplicações seguem o modelo definido.
- Testar, a partir de um dispositivo não gerenciado, as restrições aplicadas.
- Verificar o tamanho e os fluxos de cada enclave.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Toda aplicação do escopo com classe e modelo definidos | Inventário de aplicações com classe, modelo e dono |
| Dispositivo não gerenciado recebe as restrições da sua classe | Teste com dispositivo não gerenciado: sem download, sem impressão, sessão limitada |
| Cada enclave com fluxos mínimos documentados e plano de saída | Regras do gateway comparadas aos fluxos aprovados; data de modernização |
| Workloads críticos com política por identidade | Política de microsegmentação e teste de fluxo não autorizado negado |

## Como apresentar e justificar

- **Para gestores:** "Não existe um modelo para tudo. Classificamos as aplicações e aplicamos o modelo que cada classe permite — e os legados ficaram visíveis como dívida."
- **Para engenharia:** "Serviço novo nasce com identidade de workload; o gateway de enclave é só para o que não tem como mudar agora."

## Checklist de revisão arquitetural

- [ ] Aplicações classificadas por classe de recurso.
- [ ] Modelo de implantação definido por classe.
- [ ] Restrições proporcionais à visibilidade do dispositivo.
- [ ] Enclaves pequenos, com fluxos mínimos e plano de saída.
- [ ] Workloads críticos com microsegmentação baseada em identidade.

## Questões de compreensão

**1.** Qual a principal limitação do gateway de enclave?

??? success "Resposta comentada"

    Proteger um grupo de recursos com um único gateway faz com que os sujeitos possam ver recursos do enclave que não estão autorizados a usar, e o controle dentro do enclave é menos granular.

**2.** Quando o modelo de portal de recursos é preferível?

??? success "Resposta comentada"

    Quando não é possível instalar software no dispositivo — terceiros, BYOD —, aceitando visibilidade limitada sobre o dispositivo e compensando com restrições na sessão.

**3.** O que a SP 800-207A recomenda para aplicações cloud-native em vários ambientes?

??? success "Resposta comentada"

    Políticas de nível de identidade e de nível de rede, aplicadas por gateways e infraestrutura de identidade de serviço, com monitoração e telemetria, apoiadas por uma infraestrutura integrada como um service mesh.

## Exercício de tomada de decisão

!!! question "Cenário: médicos parceiros acessando prontuários na Lumen"

    Médicos parceiros, com consultórios próprios e computadores não gerenciados pela Lumen, precisam consultar prontuários de pacientes encaminhados. As opções são:

    - **A** — portal de recursos, sem agente, com restrições na sessão;
    - **B** — VDI com sessão isolada;
    - **C** — ZTNA com agente instalado nos computadores dos consultórios.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e proponha as restrições.

**Objetivos avaliados:** Escolher a combinação adequada a cada classe de recurso e de dispositivo; reconhecer os limites de visibilidade de cada modelo.

**Entrega esperada:** Matriz ponderada, modelo de implantação recomendado e a lista de restrições de sessão.

**Critérios de avaliação:**

- A escolha considera que o dispositivo não é gerenciado e compensa a baixa visibilidade com restrições.
- A autorização limita o acesso aos pacientes encaminhados ao médico parceiro.
- Há condição explícita para mudar de modelo (volume, tipo de dado, dispositivos gerenciados).

??? success "Resolução de referência"

    | Critério | Peso | A — Portal com restrições | B — VDI com sessão isolada | C — ZTNA com agente |
    |:---|:---|:---|:---|:---|
    | Proteção dos prontuários em dispositivo não gerenciado | 3 | 2 | 3 | 2 |
    | Viabilidade em consultórios sem gestão da Lumen | 2 | 3 | 3 | 1 |
    | Custo e operação | 2 | 3 | 1 | 2 |
    | Experiência do médico | 1 | 3 | 2 | 2 |
    | **Total ponderado** | | **21** | **19** | **14** |

    - **Pesos:** prontuários são dados de saúde, e o dispositivo não é da Lumen (peso 3). Viabilidade e custo pesam 2: a Lumen não administra os consultórios, e o volume de acessos é baixo. A experiência pesa 1.
    - **Recomendação: A.** O portal atende ao volume atual sem software no consultório; a baixa visibilidade sobre o dispositivo é compensada por restrições na sessão. B protege mais, mas custa mais por um volume pequeno; C depende de instalar e manter agente em computadores que a Lumen não administra.
    - **Modelo:** portal de recursos (sem agente), com identidade federada do médico (ou conta de parceiro com MFA resistente a phishing).
    - **Autorização:** ABAC com vínculo de encaminhamento paciente–médico (Módulo 6 — Aula 02).
    - **Restrições pela baixa visibilidade:** somente leitura; sem download nem impressão; marca d'água com identificação do usuário; sessão com tempo limitado; reautenticação para cada novo paciente.
    - **Alternativa para maior volume:** VDI com sessão isolada.
    - **Monitoração:** alertas para consultas fora do vínculo ou em volume anômalo; revisão mensal dos acessos de parceiros.
    - **Trade-off aceito e risco residual:** o portal só analisa o dispositivo quando ele se conecta; malware no computador do consultório pode capturar a tela durante a sessão. O residual é limitado pela leitura restrita aos pacientes encaminhados e pela marca d'água, que dá rastreabilidade a vazamentos por foto ou captura.
    - **O que mudaria a decisão:** volume maior de parceiros ou acesso a dados mais amplos (exames de imagem completos, prescrição) favorecem B; se os parceiros passarem a usar equipamentos fornecidos e gerenciados pela Lumen, C passa a ser viável e dá a maior visibilidade.

    **Erros comuns:**

    - Exigir agente em computadores que a organização não administra.
    - Permitir download e impressão em sessão sem visibilidade do dispositivo.
    - Autorizar por papel "médico parceiro" sem vínculo com o paciente.

## Pontos-chave

- Três abordagens: identidade reforçada, microsegmentação e rede definida por software.
- Quatro modelos de implantação: agente e gateway, enclave, portal e sandboxing.
- Combine conforme a classe de recurso e a gestão do dispositivo.
- Menos visibilidade sobre o dispositivo pede mais restrição na sessão.
- Enclaves servem a legados, mas devem ser pequenos e temporários.

## Referências

### Fundamentação principal

- NIST. *SP 800-207 — Zero Trust Architecture*. 2020 — §3.1 (pp. 11–12) e §3.2 (pp. 13–16). *(Lido; abordagens e modelos reconferidos no PDF em 2026-10-29.)*
- NIST. *SP 800-215* — microsegmentação e SDP (pp. 17–22). *(Lido.)*
- NIST. *SP 800-207A*. 2023 — políticas de identidade e de rede para aplicações cloud-native (notícia oficial conferida).
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-4, AC-17, AC-20, AC-20(1), SC-7(21) e SC-39, conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- NIST. *SP 1800-35* — implementações de exemplo.
- SPIFFE. *SPIFFE Concepts* — identidade de workload.

### Aplicação prática

- Classifique dez aplicações da sua organização nas classes desta aula e indique o modelo de implantação adequado para cada uma.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
