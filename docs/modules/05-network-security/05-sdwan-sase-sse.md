---
id: M05-L05
title: "Aula 05 — SD-WAN, SASE e SSE"
public_title: "Módulo 5 — Aula 05 — SD-WAN, SASE e SSE"
description: Como a convergência de rede e segurança muda a arquitetura de filiais e usuários remotos — SD-WAN, SASE e SSE —, o que cada termo cobre, que serviços de segurança entram no pacote e que decisões de arquitetura e de dependência de fornecedor isso implica.
domain: network-security
tier: professional
status: published
prerequisites: [M05-L04]
objectives:
  - Explicar SD-WAN, SASE e SSE e a relação entre eles.
  - Identificar os serviços de segurança típicos de SASE e SSE e o que cada um protege.
  - Avaliar quando SASE ou SSE resolvem problemas reais da organização e quando apenas deslocam o perímetro.
  - Especificar requisitos de arquitetura para adoção de serviços de borda entregues em nuvem.
minutes: 60
sources: [NIST-SP800-215, TECHTARGET-SASE-SSE-2024, NIST-SP800-53]
further_reading: [NIST-SP800-207, CISA-ZTMM-2, MPLIFY-169-SSE]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M05
---

# Aula 05 — SD-WAN, SASE e SSE { #sd-wan-sase-e-sse }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 5 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M05-L05</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Quando os usuários estão em qualquer lugar e as aplicações estão em SaaS e em várias nuvens, levar todo o tráfego até o datacenter para inspecioná-lo deixa de fazer sentido. **SD-WAN** moderniza a conectividade de filiais; **SASE** combina essa conectividade com serviços de segurança entregues em nuvem; **SSE** é o subconjunto de segurança. Esta aula explica os termos sem marketing, mostra que serviços entram no pacote e quais decisões de arquitetura — inclusive de dependência de fornecedor — eles exigem.

**Pré-requisito:** [Acesso remoto: VPN, ZTNA e bastion hosts](04-remote-access.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar SD-WAN, SASE e SSE e a relação entre eles.
- Identificar os serviços de segurança típicos de SASE e SSE e o que cada um protege.
- Avaliar quando SASE ou SSE resolvem problemas reais da organização e quando apenas deslocam o perímetro.
- Especificar requisitos de arquitetura para adoção de serviços de borda entregues em nuvem.

## Conceito

### O problema

A SP 800-215 descreve as limitações das abordagens tradicionais: WANs MPLS com saída para a internet em pontos designados aumentam latência e complicam a gestão (Sec. 2.3, p. 6), e VPNs levam o tráfego de nuvem de volta à sede (Sec. 2.2). Com SaaS e trabalho remoto, o perímetro centralizado vira gargalo e deixa de ver boa parte do tráfego.

### SD-WAN

Segundo a SP 800-215, o **SD-WAN** remove o acoplamento rígido entre plano de controle e plano de dados da rede (p. 23). Objetivos comuns incluem conectividade sobre qualquer transporte de WAN, **consciência de aplicação** para escolher o caminho, integração de funções de rede e segurança e **gestão centralizada** (pp. 23–24). O documento destaca que uma plataforma de rede multicloud deve entregar **política comum de segurança de entrada e saída** entre nuvens (p. 25).

### SASE e SSE

| Termo | Definição | Fonte |
|:---|:---|:---|
| **SASE** | Arquitetura que converge funções de rede e de segurança e as entrega em escala global como serviço em nuvem, a partir de pontos de presença distribuídos | SP 800-215, p. 26 |
| **SSE** | Conjunto de capacidades de segurança do SASE, com menos foco em conectividade — descrito no mercado como "SASE sem SD-WAN" | Artigo da TechTarget (2024), termo atribuído ao Gartner (2021); arcabouço Mplify 169 (2026) |

A SP 800-215 lista como **serviços mínimos** de SASE: firewall, secure web gateway, anti-malware, IPS, CASB e DLP; e como recursos avançados, isolamento de navegador e a estratégia CARTA de avaliação contínua de risco e confiança (p. 27). O documento trata o **ZTNA** como um arcabouço próprio (Sec. 5), que o SASE pode complementar; no mercado, o ZTNA costuma vir incluído nas ofertas de SSE.

Não há uma definição normativa única de SSE: o termo nasceu como categoria de mercado. Para especificar o que se contrata, uma referência neutra em relação a fornecedores é o arcabouço **Mplify 169** (2026), da organização de padrões do setor antes chamada MEF, que descreve atributos de serviço para ofertas de SSE a partir de funções como acesso seguro, proxies direto e reverso, CASB, DLP e gateway seguro. O próprio documento avisa que não é uma especificação implementável isolada — serve para comparar ofertas e escrever requisitos, não para certificar uma arquitetura.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m05-l05-sase.mmd"
```

<figcaption>Figura 1 — Filiais com SD-WAN e usuários remotos chegam a pontos de presença onde serviços SSE aplicam política única antes do acesso à internet, SaaS, nuvem e datacenter.</figcaption>
</figure>

## Fundamentos técnicos

### Serviços e o que protegem

| Serviço | Protege | Exemplo de política |
|:---|:---|:---|
| **SWG** | Usuários contra sites maliciosos; controle de categorias | Bloquear domínios recém-registrados |
| **CASB** | Uso de SaaS: descoberta, dados, configuração | Bloquear upload de dados classificados para SaaS não aprovado |
| **FWaaS** | Tráfego de filiais e usuários, por aplicação e porta | Mesma política de firewall para todas as filiais |
| **ZTNA** | Acesso a aplicações internas | Aplicações do datacenter publicadas por aplicação |
| **DLP** | Dados em trânsito | Detectar números de cartão saindo para webmail |

### Decisões de arquitetura

1. **Que tráfego vai para o serviço?** Todo o tráfego de internet? Só usuários remotos? Filiais também? Cada escolha tem impacto de custo, latência e visibilidade.
2. **Onde termina a inspeção de TLS?** No provedor. Isso significa que as chaves de inspeção e o conteúdo inspecionado passam por um terceiro — exigindo avaliação contratual e de proteção de dados (LGPD, Módulo 3 — Aula 04).
3. **Qual a dependência?** Um único provedor de SASE concentra rede e segurança: sua indisponibilidade afeta conectividade e proteção ao mesmo tempo. É preciso definir **modo de falha** (bloquear ou permitir) por categoria de tráfego e um plano de contingência.
4. **Como a política é governada?** Política como código, revisões e integração com o SIEM e com o IdP corporativo.
5. **O que continua on-premises?** Firewalls internos, segmentação do datacenter e controles east-west não são substituídos pelo SASE.

### Quando faz sentido

| Situação | Tendência |
|:---|:---|
| Muitas filiais, usuários remotos, uso intenso de SaaS | SASE ou SSE agregam valor real |
| Organização concentrada em uma sede, poucos remotos | Benefício menor; perímetro tradicional bem configurado pode bastar |
| Exigência regulatória de inspeção local ou de residência de dados | Avaliar pontos de presença e onde os dados são processados |
| Equipe pequena | Serviço gerenciado reduz carga operacional, mas aumenta dependência |

## Exemplo empresarial

!!! example "Aurora Pagamentos — SSE primeiro, SD-WAN depois"

    A Aurora tinha duas filiais, 400 usuários híbridos e quase todas as aplicações de escritório em SaaS. O tráfego de usuários remotos voltava pela VPN até a sede para passar pelo proxy. O arquiteto propôs começar pelo **SSE** (SWG, CASB, DLP e ZTNA) para usuários remotos e escritórios, mantendo o MPLS existente até o fim do contrato, e só então avaliar SD-WAN.

    O modo de falha foi decidido por categoria: tráfego para SaaS corporativos em **permitir com registro** durante indisponibilidade do provedor; tráfego para categorias de risco em **bloquear**. O CDE e o datacenter continuaram protegidos por firewalls internos — o SSE não entra no caminho do tráfego east-west.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Saída para internet | Centralizada na sede | Próxima do usuário, com política única |
| Política | Por appliance, por site | Central, aplicada em todos os pontos de presença |
| Usuários remotos | VPN até a sede | SSE com ZTNA e SWG |
| Dependência | Do próprio hardware | Do provedor — com modo de falha e contingência definidos |
| Escopo | "SASE resolve tudo" | SASE/SSE para borda; segmentação interna continua necessária |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referência voluntária para especificar a adoção de serviços de borda em nuvem:

| Controle ou padrão | Objetivo na adoção de SASE/SSE | Referência |
|:---|:---|:---|
| Serviços de sistemas externos | Exigir do provedor os requisitos de segurança e privacidade da organização e definir supervisão e papéis | SP 800-53: SA-9 (External System Services) |
| Local de processamento e armazenamento | Restringir onde o tráfego inspecionado e os logs são processados e guardados | SP 800-53: SA-9(5) (Processing, Storage, and Service Location) |
| Serviços de telecomunicação alternativos | Ter caminhos alternativos para a retomada de funções essenciais | SP 800-53: CP-8 e CP-8(2) (Single Points of Failure) |
| Falha segura | Evitar estado inseguro na falha de um dispositivo de fronteira — o modo "bloquear"; o modo "permitir com registro" é uma exceção consciente, por categoria | SP 800-53: SC-7(18) (Fail Secure) |
| Proxy autenticado e monitoramento | Encaminhar a saída por proxy autenticado e monitorar o tráfego de entrada e saída | SP 800-53: SC-7(8) e SI-4(4) |
| Serviços mínimos de SASE | Firewall, SWG, anti-malware, IPS, CASB e DLP | SP 800-215, Sec. 6 (p. 27) |

## Aplicabilidade: on-premises, cloud e híbrido

SASE e SSE são, por definição, serviços em nuvem que protegem usuários e filiais em qualquer lugar. Para workloads em cloud, a política de saída dos servidores costuma ficar em controles nativos ou no hub de trânsito (Módulo 11), e não no SSE de usuários. Em ambientes híbridos, o valor está em unificar a política para quem acessa — usuário remoto, filial ou sede — aplicações em qualquer ambiente.

## Como especificar e implementar

- "O tráfego de usuários para internet e SaaS passa por SWG e CASB com política única, independentemente da localização."
- "Aplicações internas são publicadas a usuários por ZTNA."
- "O modo de falha do serviço é definido por categoria de tráfego e testado."
- "Contratos com o provedor cobrem localização do processamento, retenção de logs, inspeção de TLS e notificação de incidentes."
- "Controles de segmentação e east-west do datacenter e da nuvem permanecem independentes do serviço de borda."

## Trade-offs, limitações e antipadrões

- **Trade-off:** simplicidade operacional versus concentração de dependência em um provedor.
- **Antipadrão — trocar o perímetro de lugar:** levar todas as regras antigas para o SASE, sem revisar.
- **Antipadrão — modo de falha indefinido:** descobrir na primeira indisponibilidade que tudo para ou que tudo passa sem inspeção.
- **Limitação:** SASE/SSE não substituem segmentação interna, identidade forte nem proteção de workloads.

## Como validar

- Testar a política a partir de usuário remoto, filial e sede, verificando resultado idêntico.
- Simular indisponibilidade do provedor e verificar o modo de falha.
- Conferir se eventos do serviço chegam ao SIEM com identidade do usuário.
- Revisar contratualmente onde os dados inspecionados são processados.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Mesma política para usuário remoto, filial e sede | Testes com o mesmo destino a partir dos três locais, com resultado idêntico |
| Modo de falha conforme o definido por categoria | Teste de indisponibilidade simulada, registrado |
| Eventos no SIEM com a identidade do usuário | Amostra de eventos do serviço com usuário e dispositivo |
| Localização do processamento e retenção de logs no contrato | Cláusulas conferidas pelo jurídico e pela segurança |
| Tráfego east-west e do datacenter fora do serviço de borda | Rotas e políticas do datacenter conferidas |

## Como apresentar e justificar

- **Para a diretoria:** "Os usuários estão em qualquer lugar e as aplicações também. Proteger com um serviço próximo do usuário é mais barato e mais eficaz que trazer tudo para a sede."
- **Para a operação:** "Uma política, em um lugar. Mas precisamos decidir hoje o que acontece se o provedor cair."

## Checklist de revisão arquitetural

- [ ] O escopo de tráfego enviado ao serviço está definido.
- [ ] A inspeção de TLS no provedor foi avaliada contratual e juridicamente.
- [ ] O modo de falha está definido por categoria e foi testado.
- [ ] A política é governada e versionada.
- [ ] Controles internos do datacenter e da nuvem continuam independentes.

## Questões de compreensão

**1.** Qual a relação entre SASE e SSE?

??? success "Resposta comentada"

    SSE é o conjunto de serviços de segurança entregues em nuvem (SWG, CASB, ZTNA, FWaaS, DLP). SASE combina esses serviços com a parte de rede, tipicamente SD-WAN. No mercado, SSE é descrito como SASE sem SD-WAN.

**2.** Que serviços a SP 800-215 lista como mínimos em SASE?

??? success "Resposta comentada"

    Firewall, secure web gateway, anti-malware, IPS, CASB e DLP; isolamento de navegador e avaliação contínua de risco e confiança aparecem como recursos avançados.

**3.** Por que o modo de falha precisa ser definido antes da adoção?

??? success "Resposta comentada"

    Porque o serviço concentra conectividade e segurança. Em uma indisponibilidade, ou o tráfego para (impacto no negócio), ou passa sem inspeção (impacto na segurança). A escolha deve ser consciente, por categoria, e testada.

## Exercício de tomada de decisão

!!! question "Cenário: SASE para os centros de distribuição da Meridiana"

    O fornecedor de rede oferece à Meridiana um pacote SASE completo para os três CDs e a sede. Os CDs têm link único (Módulo 4 — Aula 05) e dependem do WMS no datacenter; a BIA define MTD de 24 horas para a expedição (Módulo 3 — Aula 05). Há três caminhos:

    - **A** — SASE completo como proposto: SD-WAN nos CDs e todo o tráfego, inclusive CD → WMS, passando pelos pontos de presença do provedor;
    - **B** — SD-WAN com dois links por CD; tráfego operacional CD → datacenter por túnel direto entre as bordas SD-WAN; SSE só para internet e SaaS;
    - **C** — sem SASE: manter o MPLS, contratar um segundo link por CD e manter firewall local em cada CD.

    Compare os caminhos com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e indique condições para a escolha.

**Objetivos avaliados:** Avaliar quando SASE ou SSE resolvem problemas reais da organização e quando apenas deslocam o perímetro; especificar requisitos de arquitetura para adoção de serviços de borda entregues em nuvem.

**Entrega esperada:** Matriz ponderada, recomendação com as condições contratuais e técnicas e o modo de falha por categoria de tráfego.

**Critérios de avaliação:**

- A resposta separa o ganho de rede (dois links, eliminação do ponto único de falha) do ganho de segurança (SSE).
- O tráfego operacional crítico não fica dependente da disponibilidade do provedor sem SLA compatível com o MTD.
- Há condições verificáveis: SLA, localização do processamento de logs, saída sem penalidade e diversidade de rota.

??? success "Resolução de referência"

    | Critério | Peso | A — SASE completo | B — SD-WAN + SSE só para internet | C — MPLS + segundo link |
    |:---|:---|:---|:---|:---|
    | Continuidade da expedição dentro do MTD de 24 horas | 3 | 2 | 3 | 2 |
    | Proteção do acesso dos CDs à internet e a SaaS | 2 | 3 | 3 | 1 |
    | Controle da dependência de provedor e do modo de falha | 2 | 1 | 2 | 3 |
    | Custo e esforço de operação | 1 | 2 | 2 | 2 |
    | **Total ponderado** | | **16** | **21** | **16** |

    - **Pesos:** a continuidade da expedição é o risco que motiva a mudança (peso 3). A proteção do acesso à internet e o controle da dependência pesam 2, porque o pacote concentra rede e segurança em um único provedor. O custo pesa 1: as três opções têm custo comparável no horizonte de três anos.
    - **Recomendação: B.** O maior ganho está na parte de **rede**: dois links por CD resolvem o ponto único de falha da Aula 05 do Módulo 4. Manter o tráfego operacional fora do ponto de presença evita que uma indisponibilidade do provedor pare a expedição.
    - **Condições:** modo de falha da internet dos CDs em "bloquear categorias de risco, permitir as demais com registro"; SLA da parte de rede compatível com o MTD; localização do processamento de logs no contrato; saída sem penalidade se o SLA for descumprido; firewall interno e segmentação do datacenter mantidos.
    - **Trade-off aceito e risco residual:** a política de segurança fica em dois lugares (SSE para internet, firewalls internos para o tráfego operacional), o que exige governança das duas; os dois links de cada CD podem compartilhar a mesma infraestrutura física na região — a diversidade de rota precisa ser conferida com as operadoras.
    - **O que mudaria a decisão:** se o provedor demonstrasse pontos de presença redundantes no país com SLA contratual superior ao do túnel direto, A passaria a ser competitivo; se a Meridiana não tivesse uso relevante de SaaS nos CDs, C resolveria o ponto único de falha com menos mudança.

    A matriz organiza a decisão; a condição de que a expedição não dependa de um único provedor vale antes de qualquer soma.

    **Erros comuns:**

    - Tratar SASE como substituto dos controles internos do datacenter.
    - Não definir o modo de falha (bloquear ou permitir) quando o provedor estiver indisponível.
    - Contratar dois links sem conferir se compartilham a mesma infraestrutura física.

## Pontos-chave

- SD-WAN moderniza a conectividade; SASE converge rede e segurança em nuvem; SSE é a parte de segurança.
- Os serviços típicos são SWG, CASB, FWaaS, ZTNA e DLP.
- A inspeção passa a ocorrer no provedor — exige avaliação contratual e de proteção de dados.
- Defina o modo de falha por categoria de tráfego.
- SASE/SSE protegem a borda de usuários; não substituem segmentação interna nem proteção de workloads.

## Referências

### Fundamentação principal

- NIST. *SP 800-215 — Guide to a Secure Enterprise Network Landscape*. 2022 — Sec. 2.2–2.3 (pp. 5–6) e Sec. 6 (pp. 23–27). *(Lido.)*
- D. Shackleford. *SASE vs. SSE: Explaining the differences*. TechTarget, 11/06/2024. <https://www.techtarget.com/cybersecurity/tip/SASE-vs-SSE-Explaining-the-differences>. *(Lido; fonte de mercado.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles SA-9, SA-9(5), CP-8, CP-8(2), SC-7(18), SC-7(8) e SI-4(4), conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- NIST. *SP 800-207 — Zero Trust Architecture*.
- CISA. *Zero Trust Maturity Model 2.0* — pilares de redes e de aplicações.
- Mplify Alliance (antigo MEF Forum). *Mplify 169 — Security Service Edge Framework*. Fevereiro de 2026. <https://www.mplify.net/resources/mplify-169-security-service-edge-framework/> — atributos de serviço para ofertas de SSE; funções como acesso seguro, proxies direto e reverso, CASB, DLP e gateway seguro. *(Página oficial conferida em 2026-11-05; PDF não lido.)*

### Aplicação prática

- Mapeie para onde vai o tráfego de um usuário remoto da sua organização ao acessar SaaS, internet e uma aplicação interna. Indique onde cada fluxo é inspecionado hoje.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
