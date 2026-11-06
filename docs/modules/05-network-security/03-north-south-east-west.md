---
id: M05-L03
title: "Aula 03 — Tráfego North-South e East-West"
public_title: "Módulo 5 — Aula 03 — Tráfego North-South e East-West"
description: A diferença entre tráfego que cruza a borda e tráfego entre workloads, por que controles de perímetro não veem o segundo e como combinar firewall interno, microsegmentação, autenticação entre serviços e telemetria de fluxos para controlar e detectar movimento lateral.
domain: network-security
tier: professional
status: published
prerequisites: [M05-L01, M05-L02]
objectives:
  - Distinguir tráfego north-south e east-west e os controles adequados a cada um.
  - Explicar por que o movimento lateral é invisível para controles de borda.
  - Combinar controles preventivos e detectivos para tráfego east-west.
  - Dimensionar a inspeção east-west sem criar gargalos ou pontos únicos de falha.
minutes: 60
sources: [NIST-SP800-215, NIST-SP800-41-R1, MITRE-ATTACK, NIST-SP800-53]
further_reading: [NIST-SP800-207, NIST-SP800-94]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M05
---

# Aula 03 — Tráfego North-South e East-West { #trafego-north-south-e-east-west }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 5 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M05-L03</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Durante muito tempo, a segurança de rede concentrou-se no tráfego que entra e sai — **north-south**. Mas a maior parte do tráfego de um ambiente moderno circula **entre workloads** — **east-west** — e é por ele que um atacante se move depois do acesso inicial. Esta aula explica a diferença, por que controles de borda não veem o movimento lateral e como combinar prevenção e detecção no tráfego interno de forma proporcional.

**Pré-requisitos:** [Zonas e segmentação](01-zones-segmentation.md) e [Perímetro e inspeção](02-perimeter-inspection.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Distinguir tráfego north-south e east-west e os controles adequados a cada um.
- Explicar por que o movimento lateral é invisível para controles de borda.
- Combinar controles preventivos e detectivos para tráfego east-west.
- Dimensionar a inspeção east-west sem criar gargalos ou pontos únicos de falha.

## Conceito

### Duas direções

| | North-south | East-west |
|:---|:---|:---|
| **O que é** | Tráfego que cruza a borda do datacenter ou da nuvem | Tráfego entre sistemas dentro do ambiente |
| **Exemplos** | Cliente acessando o site; servidor chamando um parceiro | Web → aplicação → banco; servidor → controlador de domínio; serviço → serviço |
| **Controles típicos** | NGFW, WAF, IPS, proxies (Aula 02) | Firewall interno, microsegmentação, mTLS, telemetria |
| **Volume** | Menor | Maior — mais de 75% do tráfego, segundo a SP 800-215 (p. 5) |
| **Visibilidade tradicional** | Alta | Baixa |

A SP 800-215 observa que ferramentas de perímetro observam principalmente o tráfego north-south, enquanto o east-west fica em grande parte invisível para equipes focadas na borda (Sec. 2.1, p. 5).

### Movimento lateral

No ATT&CK, **Lateral Movement** é a tática de mover-se pelo ambiente — por exemplo, usando **Remote Services (T1021)** com credenciais válidas (Módulo 4 — Aula 04). Esse tráfego nunca passa pela borda: vai de um servidor comprometido a outro, dentro da mesma rede. Por isso, a pergunta de arquitetura é: **depois que um sistema é comprometido, o que ele consegue alcançar — e alguém percebe?**

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m05-l03-ns-ew.mmd"
```

<figcaption>Figura 1 — Tráfego north-south passa pelos controles de borda; o east-west circula entre workloads e precisa de microsegmentação e telemetria próprias.</figcaption>
</figure>

## Fundamentos técnicos

### Controles preventivos east-west

| Controle | Como atua | Observação |
|:---|:---|:---|
| **Firewall interno entre zonas** | Aplica a matriz de fluxos (Aula 01) | A SP 800-215 lembra que firewalls dentro do datacenter podem segmentar a rede e impedir movimento lateral (p. 9) |
| **Microsegmentação** | Política por workload | Depende de identidade de workload e de mapa de dependências |
| **Firewall de host** | Política no próprio servidor | Útil onde não há firewall de rede entre hosts; requer gestão centralizada |
| **Autenticação mútua entre serviços (mTLS)** | Um serviço só aceita chamadas de identidades autorizadas | Protege mesmo dentro do mesmo segmento (Módulo 7 — Aula 05) |
| **Restrição de protocolos administrativos** | RDP, SSH e protocolos de gerenciamento só a partir da zona de gestão | Corta o caminho mais usado no movimento lateral |

A SP 800-41 Rev. 1 alertava, já em 2009, que tráfego entre sistemas virtualizados no mesmo host **não pode ser monitorado por um firewall externo** (p. 2-9) — o que torna controles no hypervisor, no host ou baseados em identidade necessários em ambientes virtualizados.

### Controles detectivos east-west

- **Telemetria de fluxos** (registros de conexões entre hosts) para identificar padrões anômalos: servidor web iniciando conexões administrativas, estação acessando dezenas de servidores.
- **Registros de autenticação** do diretório: logins administrativos fora do padrão.
- **IDS de rede ou análise de comportamento de rede** em pontos de agregação — a SP 800-94 inclui a análise de comportamento de rede entre as classes de IDPS.
- **EDR** nos endpoints e servidores: a SP 800-215 registra que o tráfego east-west é em grande parte invisível para as equipes de segurança e que parte dessa visibilidade é buscada com soluções de EDR, que coletam telemetria nos endpoints (Sec. 2.1, p. 5).

### Dimensionamento

Inspecionar todo o tráfego east-west com appliances centrais cria **gargalo** e **ponto único de falha**. Estratégias comuns:

1. **Filtrar** (permitir ou negar) em todo lugar, de forma distribuída — barato e eficaz.
2. **Inspecionar em profundidade** apenas nas travessias mais sensíveis (por exemplo, para o CDE ou para a zona de dados).
3. **Observar** (telemetria) em todo lugar, para detecção.

## Exemplo empresarial

!!! example "Lumen Saúde — o servidor de relatórios que alcançava tudo"

    Um teste de intrusão interno na Lumen partiu de um servidor de relatórios comprometido. Sem passar por nenhum controle de borda, o testador alcançou o banco de prontuários, o controlador de domínio e o servidor de backup. Os logs de perímetro não registraram nada.

    A resposta combinou: restrição de RDP e SSH à zona de gestão; firewall interno entre aplicações e dados com a matriz de fluxos; microsegmentação no cluster de containers do portal; e telemetria de fluxos enviada ao SIEM com três detecções iniciais (conexões administrativas fora da zona de gestão, varredura interna e acesso novo ao banco de prontuários). No reteste, o mesmo ponto de partida alcançou apenas a réplica de leitura que o servidor de relatórios usa legitimamente — e a tentativa de varredura gerou alerta em minutos.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Foco | Borda | Borda e tráfego interno |
| Rede interna | Confiável por padrão | Fluxos explícitos, negar por padrão |
| Protocolos administrativos | Abertos entre servidores | Somente a partir da zona de gestão |
| Visibilidade | Logs de perímetro | Telemetria de fluxos, autenticação e EDR |
| Inspeção | Toda em appliances centrais | Filtrar em todo lugar, inspecionar onde é sensível, observar tudo |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referência voluntária:

| Controle ou padrão | Objetivo no tráfego east-west | Referência |
|:---|:---|:---|
| Imposição do fluxo de informação | Aplicar a matriz de fluxos também entre sistemas internos | SP 800-53: AC-4 (Information Flow Enforcement) |
| Fronteira nas interfaces internas | Monitorar e controlar as interfaces internas-chave, não só a borda | SP 800-53: SC-7 (Boundary Protection), item sobre *key internal managed interfaces* |
| Sub-redes para funções críticas | Isolar componentes e funções críticas em sub-redes próprias | SP 800-53: SC-7(29) (Separate Subnets to Isolate Functions) |
| Funcionalidade mínima | Restringir protocolos administrativos e serviços desnecessários entre servidores | SP 800-53: CM-7 (Least Functionality) |
| Autenticação entre serviços | Exigir que serviços se identifiquem e autentiquem antes de se comunicar | SP 800-53: IA-9 (Service Identification and Authentication) |
| Monitoramento interno | Posicionar monitoramento dentro do sistema e analisar eventos quase em tempo real | SP 800-53: SI-4 (System Monitoring) e SI-4(2) |
| Movimento lateral | Saber o que detectar e o que bloquear | MITRE ATT&CK v20: tática Lateral Movement, técnica T1021 |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, o tráfego east-west é controlado por grupos de segurança, políticas de rede de clusters e identidade de serviço, e registrado por logs de fluxo da rede virtual — recursos nativos que precisam ser habilitados e enviados ao SIEM. Em ambientes híbridos, o tráfego entre datacenter e nuvem é east-west do ponto de vista da organização, mas atravessa um canal de conectividade: trate-o como travessia de zona, com política e inspeção no hub (Módulo 11).

## Como especificar e implementar

- "O tráfego east-west segue a matriz de fluxos entre zonas e, nos ambientes críticos, política por workload."
- "Protocolos administrativos só são aceitos a partir da zona de gestão."
- "Logs de fluxo e de autenticação de todas as zonas são enviados ao SIEM, com detecções de movimento lateral."
- "Inspeção profunda é aplicada às travessias para zonas sensíveis; filtragem e telemetria, a todas."

## Trade-offs, limitações e antipadrões

- **Trade-off:** inspeção central dá visibilidade, mas cria gargalo e ponto único de falha.
- **Antipadrão — "dentro é confiável":** a premissa que o Zero Trust (Módulo 7) existe para eliminar.
- **Antipadrão — logs de fluxo coletados e não analisados:** custo sem detecção.
- **Limitação:** controles de rede não distinguem um administrador legítimo de um atacante com a credencial dele; identidade e comportamento completam a defesa.

## Como validar

- Partir de um servidor comum e tentar alcançar dados, gestão e outros servidores.
- Simular varredura interna e verificar se gera alerta.
- Conferir se os logs de fluxo de todas as zonas chegam ao SIEM.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Um servidor comum alcança só os destinos da matriz | Teste de alcance a partir do servidor, comparado à matriz |
| RDP, SSH e protocolos de gerência só a partir da zona de gestão | Tentativas a partir de outras zonas bloqueadas e registradas |
| Varredura interna gera alerta | Simulação controlada e alerta no SIEM dentro do tempo de resposta acordado |
| Todas as zonas enviam logs de fluxo e de autenticação | Painel de fontes do SIEM sem zona ausente |
| A inspeção profunda tem redundância | Teste de falha de um nó de inspeção sem interrupção do tráfego permitido |

## Como apresentar e justificar

- **Para a diretoria:** "O teste mostrou que um servidor de relatórios comprometido alcançava prontuários e backups sem que nada registrasse. Hoje ele alcança só o que precisa, e a tentativa gera alerta."
- **Para a operação:** "Administração só pela zona de gestão. É uma mudança de hábito com grande redução de risco."

## Checklist de revisão arquitetural

- [ ] O tráfego east-west tem política explícita.
- [ ] Protocolos administrativos estão restritos à zona de gestão.
- [ ] Ambientes virtualizados e de containers têm controles próprios.
- [ ] Logs de fluxo e de autenticação chegam ao SIEM, com detecções.
- [ ] A inspeção profunda não cria ponto único de falha.

## Questões de compreensão

**1.** Por que o movimento lateral costuma passar despercebido em organizações com perímetro forte?

??? success "Resposta comentada"

    Porque ocorre entre sistemas internos e não atravessa os controles de borda. Sem política e telemetria east-west, não há onde bloquear nem registrar o movimento.

**2.** Que limitação a SP 800-41 Rev. 1 aponta para ambientes virtualizados?

??? success "Resposta comentada"

    Tráfego entre sistemas virtualizados no mesmo host não pode ser monitorado por um firewall externo; são necessários controles no hypervisor, no host ou baseados em identidade.

**3.** Qual a estratégia de dimensionamento recomendada para controles east-west?

??? success "Resposta comentada"

    Filtrar de forma distribuída em todo lugar, inspecionar em profundidade apenas as travessias mais sensíveis e coletar telemetria de todo o ambiente para detecção.

## Exercício de tomada de decisão

!!! question "Cenário: inspeção do tráfego para o CDE da Aurora"

    O ambiente de dados de cartão (CDE) da Aurora recebe chamadas de oito serviços. O CISO quer inspeção profunda com IPS em todo o tráfego east-west do datacenter. A equipe de rede alerta que o volume interno é dez vezes o da borda e que um IPS central viraria gargalo. As propostas são:

    - **A** — IPS em todo o tráfego east-west, em appliances centrais;
    - **B** — filtrar em todo lugar (matriz de fluxos e microsegmentação no CDE), IPS em alta disponibilidade só nas travessias para o CDE e para a zona de dados, e telemetria em todo o ambiente;
    - **C** — filtrar em todo lugar e observar com telemetria e EDR, sem IPS.

    Compare as propostas com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e recomende uma.

**Objetivos avaliados:** Dimensionar a inspeção east-west sem criar gargalos ou pontos únicos de falha; combinar controles preventivos e detectivos para tráfego east-west.

**Entrega esperada:** Matriz ponderada, recomendação com a localização dos pontos de inspeção e o critério de dimensionamento.

**Critérios de avaliação:**

- A resposta distingue filtrar, inspecionar e observar, e diz onde cada um é aplicado.
- Os pontos de inspeção profunda ficam onde o risco se concentra, com alta disponibilidade para não parar pagamentos.
- A detecção no restante do datacenter é coberta por telemetria e EDR, com o limite dessa cobertura declarado.

??? success "Resolução de referência"

    | Critério | Peso | A — IPS em tudo | B — Filtrar, inspecionar onde é sensível, observar tudo | C — Filtrar e observar |
    |:---|:---|:---|:---|:---|
    | Proteção do CDE contra exploração vinda de outros sistemas | 3 | 3 | 3 | 2 |
    | Disponibilidade e latência (sem gargalo nem ponto único de falha) | 3 | 1 | 2 | 3 |
    | Proteção da zona de dados (bases fora do CDE) contra exploração | 2 | 3 | 3 | 2 |
    | Custo de capacidade e de operação | 1 | 1 | 2 | 3 |
    | **Total ponderado** | | **19** | **23** | **22** |

    - **Pesos:** o CDE concentra o risco e o motivo da discussão, e a disponibilidade dos pagamentos é inegociável para o negócio — os dois pesam 3. A zona de dados guarda as bases que alimentam o CDE e pesa 2; o custo é relevante, mas secundário diante dos dois primeiros (peso 1). A detecção de movimento lateral no restante do datacenter não entra como critério porque B e C a fazem da mesma forma — telemetria em todo o ambiente — e não diferenciaria as opções.
    - **Recomendação: B.** Concentra a inspeção profunda onde o risco está, com capacidade dimensionada para esse volume e alta disponibilidade. A filtragem distribuída e a telemetria cobrem o resto sem criar gargalo. A diferença para C é pequena na soma, mas decisiva no critério principal: sem IPS, uma exploração vinda de um serviço autorizado a falar com o CDE só seria vista depois.
    - **Trade-off aceito e risco residual:** tráfego entre sistemas fora do CDE e da zona de dados é filtrado e observado, não inspecionado; exploração nesse trecho depende da detecção por telemetria e EDR. Assinaturas de baixa confiança ficam em modo de detecção, para não bloquear pagamentos legítimos.
    - **O que mudaria a decisão:** uma exigência contratual ou setorial de inspeção em pontos internos específicos ampliaria o escopo de B; se o CDE fosse migrado para uma plataforma com política por identidade de workload e autenticação mútua, C poderia ser suficiente para o tráfego entre serviços.

    A matriz organiza a discussão com o CISO e torna os pesos explícitos; a decisão final continua sendo de julgamento profissional.

    **Erros comuns:**

    - Colocar IPS central em todo o tráfego east-west sem avaliar gargalo e ponto único de falha.
    - Confundir telemetria (detecta depois) com inspeção em linha (pode bloquear antes).
    - Ignorar a disponibilidade do CDE como critério de peso igual ao da segurança.

## Pontos-chave

- North-south cruza a borda; east-west circula entre workloads e é a maior parte do tráfego.
- Movimento lateral não passa pela borda: exige política e telemetria internas.
- Restringir protocolos administrativos à zona de gestão é uma das medidas mais eficazes.
- Filtre em todo lugar, inspecione onde é sensível, observe tudo.
- Controles de rede não bastam contra credenciais válidas — identidade e comportamento completam.

## Referências

### Fundamentação principal

- NIST. *SP 800-215* — Sec. 2.1 (p. 5) e Sec. 3 (p. 9). *(Lido.)*
- NIST. *SP 800-41 Rev. 1* — firewalls para infraestruturas virtuais (p. 2-9). *(Lido.)*
- MITRE. *ATT&CK v20* — tática Lateral Movement e técnica Remote Services (T1021). *(Lido.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-4, SC-7, SC-7(29), CM-7, IA-9, SI-4 e SI-4(2), conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- NIST. *SP 800-207 — Zero Trust Architecture* — fim da confiança implícita na rede interna.
- NIST. *SP 800-94* — análise de comportamento de rede como classe de IDPS.

### Aplicação prática

- Escolha um servidor comum do seu ambiente e liste tudo que ele consegue alcançar na rede. Compare com o que ele realmente precisa.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
