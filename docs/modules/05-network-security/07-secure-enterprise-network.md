---
id: M05-L07
title: "Aula 07 — Desenho de uma rede corporativa segura"
public_title: "Módulo 5 — Aula 07 — Desenho de uma rede corporativa segura"
description: Aplicação integrada do módulo — do estado atual de uma rede corporativa híbrida ao estado-alvo com zonas, perímetro, controles east-west, acesso remoto por aplicação, SSE, NAC e gestão separada — com priorização por risco, plano de transição e critérios de validação.
domain: network-security
tier: architect
status: published
prerequisites: [M05-L01, M05-L02, M05-L03, M05-L04, M05-L05, M05-L06, M04-L07]
objectives:
  - Analisar uma rede corporativa existente e identificar lacunas por cenário de risco.
  - Desenhar uma arquitetura-alvo coerente, combinando os controles do módulo.
  - Priorizar a transição por redução de risco e viabilidade.
  - Definir critérios de validação e de aceite para cada etapa.
minutes: 90
sources: [NIST-SP800-215, NSA-NETWORK-INFRA-2022, NIST-SP800-46-R2, NIST-SP800-41-R1, PCI-DSS-401, NIST-SP800-53]
further_reading: [NIST-SP800-207, CISA-ZTMM-2, MITRE-ATTACK]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M05
---

# Aula 07 — Desenho de uma rede corporativa segura { #desenho-de-uma-rede-corporativa-segura }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 5 · Nível 2</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">90 min · ID técnico: M05-L07</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    As aulas anteriores trataram cada controle separadamente. Na prática, o arquiteto recebe uma rede existente, com dívidas e restrições, e precisa propor um destino coerente e um caminho viável até ele. Esta aula aplica o módulo inteiro a um caso: a rede da Aurora Pagamentos, com sede, filiais, datacenter, ambiente de dados de cartão e nuvem. O foco não é o desenho ideal, mas o **desenho defensável** — ligado a riscos, priorizado, com transição segura e critérios de validação.

**Pré-requisitos:** as Aulas 01 a 06 deste módulo e [Revisão arquitetural, As-Is/To-Be e validação](../04-threat-modeling/07-architecture-review-validation.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Analisar uma rede corporativa existente e identificar lacunas por cenário de risco.
- Desenhar uma arquitetura-alvo coerente, combinando os controles do módulo.
- Priorizar a transição por redução de risco e viabilidade.
- Definir critérios de validação e de aceite para cada etapa.

## Conceito

### Um método em cinco passos

1. **Entender o negócio e as restrições** — processos críticos, obrigações (PCI DSS, LGPD), equipe, contratos vigentes.
2. **Mapear o estado atual** — zonas reais (não as do documento), fluxos, acessos remotos, administração.
3. **Analisar por cenários** — que cenários do register a rede atual favorece (Módulo 4 — Aula 04)?
4. **Desenhar o estado-alvo** — com os padrões do módulo, cada decisão ligada a um cenário.
5. **Planejar a transição** — etapas que reduzem risco cedo, sem parar a operação, com validação.

### O caso: Aurora Pagamentos

A Aurora tem sede, duas filiais, um datacenter com o ambiente de dados de cartão (CDE), uma conta de nuvem e 400 usuários híbridos. Os cenários prioritários do register são: **comprometimento do CDE** a partir da rede corporativa; **ransomware** a partir de acesso remoto; e **exfiltração** de dados de lojistas.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m05-l07-as-is.mmd"
```

<figcaption>Figura 1 — As-Is: rede interna ampla sobre MPLS, CDE separado só por ACL, VPN com acesso a toda a rede, administração direta e VPN com a nuvem sem filtragem.</figcaption>
</figure>

## Fundamentos técnicos

### Análise do estado atual por cenário

| Lacuna | Cenários favorecidos | Referência |
|:---|:---|:---|
| Rede interna ampla, sem firewall interno | Ransomware, comprometimento do CDE | Aulas 01 e 03 |
| CDE separado só por ACL de switch | Comprometimento do CDE; escopo PCI amplo | Aula 01; PCI DSS |
| VPN com acesso a toda a rede | Ransomware via acesso remoto | Aula 04; SP 800-46 Rev. 2 |
| Administração direta de estações | Movimento lateral com credenciais privilegiadas | Aulas 03 e 04 |
| VPN com a nuvem sem filtragem | Comprometimento de um lado alcança o outro | Aula 03; NSA Sec. 2.3 |
| Saída centralizada na sede, remotos sem proteção | Exfiltração e malware em usuários remotos | Aula 05 |
| Qualquer dispositivo nas tomadas | Acesso não autorizado à rede interna | Aula 06 |

### Estado-alvo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m05-l07-to-be.mmd"
```

<figcaption>Figura 2 — To-Be: SD-WAN e SSE para escritórios e remotos, ZTNA por aplicação, firewall interno com matriz de fluxos, CDE acessível só a partir da tokenização, gestão separada com acesso privilegiado, hub de trânsito com inspeção para a nuvem e telemetria no SIEM.</figcaption>
</figure>

| Decisão | Cenário tratado | Padrão |
|:---|:---|:---|
| Zonas de usuários, aplicações, dados, gestão e CDE, com firewall interno e matriz de fluxos | Ransomware, CDE | Segmentação (Aula 01) |
| CDE aceita apenas fluxos documentados a partir da tokenização; microsegmentação interna | CDE; redução de escopo | Segmentação + PCI DSS |
| ZTNA por aplicação; VPN residual como exceção | Ransomware via acesso remoto | Acesso remoto (Aula 04) |
| Administração só pela zona de gestão via acesso privilegiado | Movimento lateral | East-west (Aula 03), bastion (Aula 04) |
| Hub de trânsito com firewall entre datacenter e nuvem | Propagação entre ambientes | East-west (Aula 03) |
| SSE com SWG, CASB e DLP para todos os usuários | Exfiltração | SSE (Aula 05) |
| 802.1X nos escritórios | Acesso não autorizado | NAC (Aula 06) |
| Telemetria de fluxos e eventos no SIEM | Detecção em todos os cenários | Aula 03 |

### Priorização da transição

| Etapa | Ações | Redução de risco | Esforço |
|:---|:---|:---|:---|
| **1 — 0 a 3 meses** | MFA resistente a phishing na VPN; pool da VPN como zona; firewall entre rede interna e CDE com fluxos mínimos; filtragem na VPN com a nuvem | Alta | Médio |
| **2 — 3 a 6 meses** | Zona de gestão e acesso privilegiado; firewall interno com matriz de fluxos em modo monitor e depois bloqueio | Alta | Alto |
| **3 — 6 a 9 meses** | ZTNA para aplicações web; SSE para remotos | Média | Médio |
| **4 — 9 a 15 meses** | SD-WAN nas filiais ao fim do contrato MPLS; SSE para escritórios; 802.1X | Média | Alto |

A ordem segue o princípio de reduzir primeiro os caminhos mais prováveis e de maior impacto (acesso remoto e CDE) e deixar para depois mudanças caras com contratos vigentes (MPLS).

### Critérios de validação por etapa

| Etapa | Critério de aceite | Método |
|:---|:---|:---|
| 1 | Da rede de usuários, nenhuma conexão ao CDE é aceita; VPN recusa login sem MFA resistente a phishing | Testar |
| 2 | RDP/SSH para servidores só a partir da zona de gestão; regras do firewall interno sem "any-any" | Testar + examinar |
| 3 | Usuário remoto via ZTNA alcança só as aplicações concedidas | Testar |
| 4 | Dispositivo desconhecido em tomada de filial vai para visitantes | Testar |

## Exemplo empresarial

!!! example "Aurora — a etapa 1 que mudou o escopo PCI"

    Ao implantar o firewall entre a rede interna e o CDE (etapa 1), a equipe descobriu que 31 servidores tinham conexões com o CDE "por precaução" — muitos sem nenhuma necessidade. Restringir os fluxos à tokenização e a três serviços de suporte, com justificativa, reduziu o número de sistemas conectados ao CDE e, com a orientação do assessor de conformidade, o escopo da avaliação PCI DSS seguinte. A mesma etapa reduziu o risco do cenário de comprometimento do CDE de crítico para médio, antes de qualquer investimento em SASE.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Ponto de partida | Catálogo de produtos | Cenários de risco e restrições |
| Desenho | Ideal, sem caminho | Alvo defensável com transição em etapas |
| Priorização | Projetos mais visíveis | Maior redução de risco por esforço |
| Aceite | "Implantado" | Critério testável por etapa |
| Dependências | Ignoradas | Contratos, equipe e operação considerados |

## Controles e padrões relevantes

A arquitetura-alvo combina os controles das Aulas 01 a 06. Os controles abaixo, do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), tratam do desenho e da transição como um todo — referência voluntária:

| Controle ou padrão | Objetivo no desenho e na transição | Referência |
|:---|:---|:---|
| Arquitetura de segurança do sistema | Documentar requisitos e abordagem de proteção e a relação com a arquitetura corporativa | SP 800-53: PL-8 (Security and Privacy Architectures) |
| Arquitetura corporativa | Manter a arquitetura corporativa considerando segurança, privacidade e risco | SP 800-53: PM-7 (Enterprise Architecture) |
| Análise de impacto de mudanças | Avaliar o impacto de segurança antes de cada mudança de bloqueio | SP 800-53: CM-4 (Impact Analyses) |
| Avaliação de controles | Planejar e executar os testes de aceite de cada etapa | SP 800-53: CA-2 (Control Assessments) |
| Monitoramento contínuo | Acompanhar métricas e efetividade depois de cada etapa | SP 800-53: CA-7 (Continuous Monitoring) |
| Fluxos e fronteiras | Matriz de fluxos e proteção das interfaces internas e externas | SP 800-53: AC-4 e SC-7 (Aulas 01 a 03) |
| Escopo do CDE | Segmentação para reduzir os sistemas no escopo da avaliação | PCI DSS v4.0.1 — aplicabilidade conferida em fonte oficial; requisitos específicos dependem do texto do padrão e do assessor |

## Aplicabilidade: on-premises, cloud e híbrido

O caso é híbrido por natureza: o datacenter mantém o CDE, a nuvem hospeda workloads novos e os usuários acessam SaaS de qualquer lugar. O princípio que une os ambientes é a **política explícita em cada travessia** — escritório para SSE, SSE para aplicações, nuvem para datacenter via hub, gestão para tudo. Os Módulos 9 a 11 aprofundam os controles nativos de cada provedor e o desenho do hub.

## Como especificar e implementar

- "A arquitetura de rede-alvo liga cada decisão a um cenário de risco do register."
- "A transição é planejada em etapas, com critérios de aceite testáveis e redução de risco mensurável a cada etapa."
- "Toda travessia entre zonas, ambientes ou serviços de borda tem política explícita, dono e registro no SIEM."
- "Mudanças de bloqueio passam por modo monitor; exceções têm dono e prazo."

## Trade-offs, limitações e antipadrões

- **Trade-off:** velocidade de redução de risco versus esforço operacional; etapas pequenas reduzem risco mais cedo, mas exigem mais gestão de mudança.
- **Antipadrão — big bang:** trocar toda a rede em um fim de semana.
- **Antipadrão — desenho-alvo sem dono:** a arquitetura bonita que ninguém implementa.
- **Limitação:** a rede é uma camada; identidade (Módulo 6), Zero Trust (Módulo 7) e proteção de workloads completam a defesa.

## Como validar

- Executar os critérios de aceite de cada etapa e registrar resultados.
- Repetir o exercício do cenário de ransomware (Módulo 4 — Aula 04) a cada etapa e contar os pontos de interrupção.
- Revisar com o assessor de conformidade o efeito das mudanças no escopo PCI DSS.

Critérios de aceite do programa (os de cada etapa estão em "Critérios de validação por etapa"):

| Critério | Evidência |
|:---|:---|
| Critério de aceite de cada etapa concluída verificado por teste | Registro do teste ao fim da etapa, com o método da tabela por etapa |
| Pontos de interrupção do cenário de ransomware aumentam a cada etapa | Reexecução do cenário documentada depois de cada etapa |
| Mudanças no escopo PCI DSS avaliadas antes de cada etapa que afeta o CDE | Parecer do assessor de conformidade registrado |
| Toda regra nova passa por modo monitor antes do bloqueio | Histórico de mudanças do firewall com o período em monitor |

## Como apresentar e justificar

- **Para a diretoria:** "Em três meses reduzimos os dois riscos mais graves — acesso remoto e CDE — com custo moderado. As etapas seguintes melhoram a experiência e a proteção de remotos, e coincidem com o fim do contrato atual de rede."
- **Para a operação:** "Cada bloqueio passa antes por modo monitor. Ninguém descobre uma regra nova pelo telefone."

## Checklist de revisão arquitetural

- [ ] O estado atual foi mapeado com fluxos reais.
- [ ] Cada lacuna está ligada a cenários de risco.
- [ ] Cada decisão do estado-alvo trata um cenário explícito.
- [ ] A transição tem etapas priorizadas por redução de risco.
- [ ] Cada etapa tem critério de aceite testável.
- [ ] Restrições de contratos, equipe e operação foram consideradas.

## Questões de compreensão

**1.** Por que a etapa 1 começa pelo acesso remoto e pelo CDE, e não pelo SD-WAN?

??? success "Resposta comentada"

    Porque esses são os caminhos dos cenários mais prováveis e de maior impacto (ransomware via acesso remoto e comprometimento do CDE), e as ações têm custo moderado. O SD-WAN traz benefícios, mas depende do fim do contrato MPLS e reduz menos risco imediato.

**2.** O que torna o estado-alvo "defensável"?

??? success "Resposta comentada"

    Cada decisão está ligada a um cenário de risco, considera restrições reais e vem acompanhada de um caminho de transição com critérios de aceite testáveis.

**3.** Por que a VPN com a nuvem sem filtragem é uma lacuna relevante?

??? success "Resposta comentada"

    Porque transforma datacenter e nuvem em uma única rede de confiança: o comprometimento de um lado alcança o outro sem passar por política. Um hub com firewall torna a travessia explícita e registrada.

## Exercício de tomada de decisão

!!! question "Cenário: orçamento reduzido"

    A diretoria da Aurora aprovou apenas 40% do orçamento proposto para o primeiro ano. Que ações você manteria, quais adiaria e que risco residual apresentaria para aceite? Compare três formas de usar os 40% com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério):

    - **A** — executar as etapas 1 e 2 completas (acesso remoto, CDE, nuvem e gestão) e adiar o restante;
    - **B** — distribuir os 40% proporcionalmente entre as quatro etapas;
    - **C** — priorizar ZTNA e SSE para todos os usuários, adiando firewall interno e zona de gestão.

**Objetivos avaliados:** Priorizar a transição por redução de risco e viabilidade; analisar uma rede corporativa existente e identificar lacunas por cenário de risco.

**Entrega esperada:** Matriz ponderada, lista do que se mantém e do que se adia, e o risco residual com dono para aceite formal.

**Critérios de avaliação:**

- A escolha conclui etapas inteiras que interrompem os cenários prioritários, em vez de iniciar todas.
- O risco residual de cada adiamento é nomeado, classificado e tem dono e data de revisão.
- Há uma alternativa de menor custo para o que foi adiado, quando ela existe.

??? success "Resolução de referência"

    - **Manter (alto efeito, custo moderado):** MFA resistente a phishing e zona para a VPN; firewall entre rede interna e CDE com fluxos mínimos; filtragem da VPN com a nuvem; zona de gestão com acesso privilegiado para administradores.
    - **Adiar:** SD-WAN (aguardar fim do contrato MPLS), 802.1X nas filiais, SSE para escritórios.
    - **Alternativa barata:** SWG apenas para usuários remotos, em vez de SSE completo.
    - **Risco residual para aceite:** exfiltração e malware por usuários em escritórios sem SSE (médio), acesso de dispositivos não autorizados nas filiais (médio), dependência do MPLS (baixo). Dono: CIO, com revisão no próximo ciclo orçamentário.

    Matriz das três alternativas do enunciado:

    | Critério | Peso | A — Etapas 1 e 2 completas | B — Corte proporcional | C — Experiência do usuário primeiro |
    |:---|:---|:---|:---|:---|
    | Redução do risco dos cenários prioritários (CDE e ransomware via acesso remoto) | 3 | 3 | 2 | 2 |
    | Viabilidade com 40% do orçamento e a equipe atual | 2 | 3 | 1 | 2 |
    | Impacto na operação e nos usuários durante a mudança | 2 | 2 | 2 | 3 |
    | Independência de contratos vigentes (MPLS) | 1 | 3 | 2 | 3 |
    | **Total ponderado** | | **22** | **14** | **19** |

    - **Pesos:** o orçamento foi cortado, mas os cenários de risco não mudaram — a redução de risco continua pesando 3. Viabilidade e impacto operacional pesam 2; a dependência do contrato MPLS, 1, porque afeta só a etapa 4.
    - **Recomendação: A.** Concluir poucas etapas inteiras reduz mais risco que começar todas: uma matriz de fluxos pela metade ou um ZTNA sem a zona de gestão deixa os caminhos principais abertos. A opção C melhora a experiência, mas deixa o CDE e a administração como estão.
    - **Trade-off aceito:** usuários em escritórios seguem sem SSE no primeiro ano, com o risco residual acima formalmente aceito pelo CIO.
    - **O que mudaria a decisão:** um incidente de exfiltração por usuário de escritório, ou uma exigência de cliente sobre proteção de dados de lojistas, aumentaria o peso desse cenário e traria o SWG ou o SSE dos escritórios para o primeiro ano.

    **Erros comuns:**

    - Distribuir o orçamento proporcionalmente, deixando todas as etapas pela metade.
    - Priorizar o que melhora a experiência do usuário em vez do que fecha os caminhos de ataque.
    - Apresentar o corte sem pedir aceite formal do risco residual.

## Pontos-chave

- Comece pelo negócio, pelas restrições e pelos cenários de risco, não pelos produtos.
- Cada decisão do estado-alvo trata um cenário explícito.
- A transição em etapas reduz o risco mais grave primeiro, sem parar a operação.
- Critérios de aceite testáveis transformam "implantado" em "funcionando".
- A rede é uma camada; identidade e Zero Trust completam a arquitetura.

<!-- next-steps:start -->

!!! tip "Próximos passos"

    Você concluiu a última aula do **Módulo 5** — [voltar ao módulo](index.md).

    Em seguida: [Módulo 6 — Identity & Access Management](../../modules/06-iam/index.md).

<!-- next-steps:end -->

## Referências

### Fundamentação principal

- NIST. *SP 800-215 — Guide to a Secure Enterprise Network Landscape*. 2022. *(Lido.)*
- NSA. *Network Infrastructure Security Guidance*. 2022. *(Lido.)*
- NIST. *SP 800-46 Rev. 2* e *SP 800-41 Rev. 1*. *(Lidos.)*
- PCI SSC. *PCI DSS v4.0.1* — aplicabilidade conferida na página oficial do padrão; requisitos específicos de segmentação não conferidos no texto do padrão.
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles PL-8, PM-7, CM-4, CA-2, CA-7, AC-4 e SC-7, conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- NIST. *SP 800-207* e CISA. *Zero Trust Maturity Model 2.0* — evolução da rede para Zero Trust (Módulo 7).
- MITRE. *ATT&CK v20* — cenários usados na validação.

### Aplicação prática

- Aplique o método de cinco passos a uma rede que você conhece: liste lacunas por cenário, desenhe o estado-alvo e proponha três etapas com critérios de aceite testáveis.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
