---
id: M08-L02
title: "Aula 02 — Hardening e baselines de configuração"
public_title: "Módulo 8 — Aula 02 — Hardening e baselines de configuração"
description: Como definir, aplicar e manter configurações seguras — benchmarks de referência, baselines aprovadas, gestão de configuração focada em segurança, automação, detecção de desvios e exceções — para servidores, estações e equipamentos de rede.
domain: infrastructure-foundations
tier: professional
status: published
prerequisites: [M08-L01, M02-L04]
objectives:
  - Diferenciar benchmark de referência, baseline aprovada e configuração efetiva.
  - Aplicar as quatro fases da gestão de configuração focada em segurança.
  - Escolher entre perfis de benchmark conforme o risco e o impacto operacional.
  - Detectar e tratar desvios com correção automática ou exceção registrada.
minutes: 75
sources: [NIST-SP800-128, NIST-SP800-70-R5, CIS-BENCHMARKS, CIS-CONTROLS-V8-1, NIST-SP800-53]
further_reading: [NSA-NETWORK-INFRA-2022, CISA-STOPRANSOMWARE-GUIDE]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M08
---

# Aula 02 — Hardening e baselines de configuração { #hardening-e-baselines-de-configuracao }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 8 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M08-L02</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Sistemas saem de fábrica configurados para funcionar, não para resistir a ataques: serviços desnecessários habilitados, protocolos legados ligados, contas padrão, registros mínimos. **Hardening** é reduzir essa superfície; **baselines** são a forma de fazer isso de maneira repetível e verificável. Esta aula mostra como escolher referências, transformá-las em baselines aprovadas, aplicá-las por automação e manter o ambiente nelas ao longo do tempo.

**Pré-requisitos:** [Segurança de datacenters](01-datacenter-security.md) e [Princípios, padrões, baselines e exceções](../02-security-architecture/04-principles-standards-baselines-exceptions.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Diferenciar benchmark de referência, baseline aprovada e configuração efetiva.
- Aplicar as quatro fases da gestão de configuração focada em segurança.
- Escolher entre perfis de benchmark conforme o risco e o impacto operacional.
- Detectar e tratar desvios com correção automática ou exceção registrada.

## Conceito

### Três níveis

| Nível | O que é | Exemplo |
|:---|:---|:---|
| **Benchmark de referência** | Guia externo de configuração segura | CIS Benchmark, checklist do National Checklist Program |
| **Baseline aprovada** | Configuração adotada pela organização, com parâmetros e exceções decididos | "Windows Server — baseline Meridiana v3" |
| **Configuração efetiva** | O estado real de cada sistema | O que a varredura encontra |

A NIST SP 800-128 define baseline de configuração como um conjunto de especificações **formalmente revisado e acordado** em um momento, que **só pode ser alterado por procedimentos de controle de mudança** (Sec. 2.3.7, p. 11).

### Referências externas

- **CIS Benchmarks** — guias de configuração desenvolvidos por consenso, com mais de 100 benchmarks em mais de 25 famílias de produtos; o perfil **Level 1** é aplicável rapidamente, com pouco impacto, e o **Level 2** oferece defesa em profundidade onde a segurança é prioridade, podendo causar problemas se aplicado sem cuidado; o perfil **STIG** substituiu o antigo Level 3.
- **National Checklist Program (NIST SP 800-70 Rev. 5, maio de 2026)** — checklists de configuração com instruções, procedimentos ou conteúdo executável para configurar um produto, verificar a configuração, detectar mudanças não autorizadas e produzir evidência de postura.
- **CIS Controls v8.1** — a configuração segura de ativos é parte do IG1 (Módulo 3 — Aula 03).

## Fundamentos técnicos

### As quatro fases da gestão de configuração

A SP 800-128 define gestão de configuração focada em segurança (SecCM) como a gestão e o controle de configurações seguras de um sistema para viabilizar a segurança e a gestão de risco (Sec. 2.1.3, p. 6), em quatro fases (Sec. 2.2, p. 7):

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m08-l02-seccm.mmd"
```

<figcaption>Figura 1 — Planejamento, identificação e implementação da baseline, controle de mudanças e monitoração com tratamento de desvios.</figcaption>
</figure>

| Fase | Atividades | Produto |
|:---|:---|:---|
| **Planejamento** | Política, papéis, comitê de controle de configuração | Processo de SecCM |
| **Identificar e implementar** | Escolher benchmark, decidir parâmetros, aprovar baseline, automatizar | Baseline versionada e aplicada |
| **Controlar mudanças** | Análise de impacto de segurança, aprovação | Mudanças rastreáveis |
| **Monitorar** | Varreduras contra a baseline, correção ou exceção | Relatório de conformidade e desvios |

O **comitê de controle de configuração** é descrito como grupo com responsabilidade e autoridade coletivas para revisar e aprovar mudanças — um mecanismo de pesos e contrapesos (*check and balance*) sobre as mudanças de configuração (Sec. 2.3.3, pp. 9–10).

### Escolhendo o perfil

| Tipo de sistema | Perfil inicial sugerido | Observação |
|:---|:---|:---|
| Estações de usuários | Level 1 | Testar com aplicações de negócio |
| Servidores de aplicação | Level 1 + itens de Level 2 selecionados | Testar com a aplicação |
| Plano de controle (DCs, PKI, sincronização) | Level 2 | Impacto aceitável dado o risco |
| Equipamentos de rede | Benchmark do fabricante + guia da NSA | Gerenciamento seguro, logs centralizados |

### Do documento à automação

Baselines só se mantêm com automação:

- **Aplicação:** políticas de grupo, ferramentas de gerência de configuração, imagens de referência (*golden images*), infraestrutura como código.
- **Verificação:** varreduras periódicas comparando a configuração efetiva com a baseline; conteúdo executável quando disponível.
- **Correção:** automática para desvios não autorizados de baixo risco; chamado para os demais.
- **Exceção:** registrada com dono, justificativa, compensação e prazo (Módulo 2 — Aula 04).

O #StopRansomware Guide recomenda manter **imagens de referência** de sistemas operacionais e aplicações para reconstrução rápida e versionar modelos de infraestrutura como código — práticas que também sustentam a baseline.

### Hardening além do sistema operacional

| Área | Exemplos de itens |
|:---|:---|
| Serviços | Desabilitar o que não é usado; remover software desnecessário |
| Contas | Renomear ou desabilitar contas padrão; senhas locais únicas e gerenciadas |
| Protocolos | Desabilitar legados após inventário (Aula 06) |
| Registro | Auditoria de eventos de segurança, envio ao SIEM |
| Execução | Controle de aplicações permitidas em servidores críticos |
| Rede | Firewall de host com negar por padrão |

## Exemplo empresarial

!!! example "Aurora Pagamentos — de 61% a 96% de conformidade"

    A primeira varredura de servidores Linux da Aurora contra o benchmark Level 1 mostrou 61% de conformidade média, com grande variação entre servidores do mesmo papel.

    A equipe definiu a baseline Aurora a partir do benchmark, com 14 itens ajustados por necessidade de negócio (cada um justificado), aplicou-a por gerência de configuração e passou a construir novos servidores a partir de imagens de referência. Desvios eram corrigidos automaticamente a cada hora, exceto itens que exigiam reinício. Em três meses, a conformidade média chegou a 96%, e as exceções restantes (18) estavam registradas com dono e prazo.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Configuração | Manual, servidor a servidor | Baseline versionada aplicada por automação |
| Referência | Experiência do administrador | Benchmark externo adaptado e aprovado |
| Mudanças | Diretas em produção | Controle de mudanças com análise de impacto |
| Desvios | Descobertos em auditoria | Detectados continuamente e corrigidos |
| Exceções | Implícitas | Registradas, com dono e prazo |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias para a gestão de configuração:

| Controle ou padrão | Objetivo na baseline | Referência |
|:---|:---|:---|
| Configuração de referência | Baseline documentada, mantida sob controle de configuração e revisada | SP 800-53: CM-2 (Baseline Configuration) e CM-2(2) (Automation Support for Accuracy and Currency) |
| Parâmetros de configuração | Parâmetros definidos a partir de benchmarks, com desvios aprovados e monitorados; gestão automatizada | SP 800-53: CM-6 (Configuration Settings) e CM-6(1) (Automated Management, Application, and Verification) |
| Controle de mudanças | Mudanças revisadas e aprovadas, com análise de impacto | SP 800-53: CM-3 (Configuration Change Control) e CM-4 (Impact Analyses) |
| Funcionalidade mínima | Desabilitar serviços, portas e funções desnecessários | SP 800-53: CM-7 (Least Functionality) |
| Configuração segura | Processo de configuração segura de ativos e software | CIS v8.1: Controle 4 (Secure Configuration of Enterprise Assets and Software) |
| Referências externas | Benchmarks e checklists de configuração | CIS Benchmarks; NIST SP 800-70 Rev. 5 (National Checklist Program) |

## Aplicabilidade: on-premises, cloud e híbrido

On-premises, a baseline é aplicada a servidores de vida longa e precisa de correção contínua de desvios. Em cloud, imagens de referência e infraestrutura como código permitem substituir em vez de corrigir — e benchmarks também existem para a configuração das contas de nuvem (Módulos 9 e 10). Em ambientes híbridos, a mesma baseline lógica deve valer para servidores nos dois lados, com mecanismos de aplicação diferentes.

## Como especificar e implementar

- "Cada tipo de sistema tem baseline aprovada, derivada de benchmark de referência, versionada e com justificativa para os ajustes."
- "Baselines são aplicadas por automação; novos sistemas nascem de imagens de referência."
- "Mudanças na baseline passam pelo comitê de controle de configuração com análise de impacto de segurança."
- "A conformidade é verificada ao menos diariamente nos sistemas críticos; desvios são corrigidos ou registrados como exceção."

## Trade-offs, limitações e antipadrões

- **Trade-off:** perfis mais restritivos reduzem a superfície, mas aumentam incidentes operacionais; teste antes de aplicar em massa.
- **Antipadrão — benchmark aplicado sem teste:** a aplicação quebra e o hardening é revertido por inteiro.
- **Antipadrão — conformidade de 100% em relatório e exceções invisíveis.**
- **Limitação:** baseline protege contra configurações fracas, não contra vulnerabilidades de software — correção de vulnerabilidades é outro processo (Módulo 14).

## Como validar

- Rodar a varredura de conformidade e conferir uma amostra manualmente.
- Alterar um item em servidor de teste e medir o tempo até a correção automática.
- Revisar exceções vencidas.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Conformidade à baseline dentro da meta por papel | Relatório de varredura, com amostra conferida manualmente |
| Desvio não autorizado corrigido dentro do tempo definido | Teste de alteração em servidor de homologação, cronometrado |
| Nenhuma exceção vencida | Lista de exceções com dono e prazo |
| Toda mudança na baseline com aprovação e análise de impacto | Histórico de versões da baseline |

## Como apresentar e justificar

- **Para a diretoria:** "Os servidores saíam de fábrica abertos. Agora todos seguem a mesma configuração segura, verificada a cada hora."
- **Para a operação:** "Quem precisar de uma exceção registra o motivo e o prazo. O que não estiver registrado volta para a baseline sozinho."

## Checklist de revisão arquitetural

- [ ] Baseline aprovada por tipo de sistema, derivada de referência externa.
- [ ] Ajustes justificados.
- [ ] Aplicação por automação e imagens de referência.
- [ ] Controle de mudanças com análise de impacto.
- [ ] Verificação contínua e correção de desvios.
- [ ] Exceções com dono e prazo.

## Questões de compreensão

**1.** Qual a diferença entre um benchmark e uma baseline?

??? success "Resposta comentada"

    O benchmark é uma referência externa genérica; a baseline é a configuração adotada pela organização, com parâmetros e ajustes decididos, formalmente aprovada e alterável só por controle de mudança.

**2.** Quais são as quatro fases da SecCM?

??? success "Resposta comentada"

    Planejamento; identificação e implementação de configurações; controle de mudanças de configuração; monitoração.

**3.** Quando usar o perfil Level 2 de um benchmark?

??? success "Resposta comentada"

    Onde a segurança é prioridade e o impacto operacional é aceitável — por exemplo, em sistemas do plano de controle —, sempre com teste, porque o perfil pode causar problemas se aplicado sem cuidado.

## Exercício de tomada de decisão

!!! question "Cenário: baseline dos servidores Windows da Meridiana"

    A Meridiana tem 80 servidores Windows configurados manualmente ao longo de dez anos. A equipe quer aplicar o benchmark Level 2 em todos no próximo fim de semana. As opções são:

    - **A** — aplicar Level 2 em todos no fim de semana, como proposto;
    - **B** — baseline por papel, com piloto, ondas e automação;
    - **C** — aplicar Level 1 em todos rapidamente e avaliar Level 2 depois.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e proponha um plano.

**Objetivos avaliados:** Escolher entre perfis de benchmark conforme o risco e o impacto operacional; detectar e tratar desvios com correção automática ou exceção registrada.

**Entrega esperada:** Matriz ponderada e o plano em etapas: inventário, baseline por papel, piloto, ondas e automação.

**Critérios de avaliação:**

- A baseline varia por papel, com perfil mais rígido para o plano de controle.
- Há piloto e reversão preparada antes da aplicação em massa.
- A sustentação é automática (verificação de desvios e correção ou exceção registrada).

??? success "Resolução de referência"

    | Critério | Peso | A — Level 2 em todos no fim de semana | B — Baseline por papel, piloto e ondas | C — Level 1 em todos, Level 2 depois |
    |:---|:---|:---|:---|:---|
    | Redução da superfície nos sistemas críticos | 3 | 3 | 3 | 2 |
    | Risco de quebra e de reversão do hardening | 3 | 1 | 3 | 2 |
    | Tempo até a primeira melhoria | 2 | 3 | 2 | 3 |
    | Sustentação (automação, exceções, desvios) | 1 | 1 | 3 | 2 |
    | **Total ponderado** | | **19** | **25** | **20** |

    - **Pesos:** o objetivo é reduzir a superfície dos sistemas críticos, e uma quebra em massa costuma levar à reversão total do hardening — os dois pesam 3. O tempo pesa 2; a sustentação, 1, porque B e C podem ganhá-la depois.
    - **Recomendação: B**, com o plano a seguir.

    1. **Inventário e classificação** por papel: controladores de domínio, servidores de aplicação, servidor de etiquetas (legado), arquivos.
    2. **Baseline por papel:** Level 2 para DCs e servidores do plano de controle; Level 1 com itens selecionados de Level 2 para aplicação; legado tratado como exceção com compensações (Aula 05).
    3. **Piloto:** aplicar em ambiente de homologação e em um servidor de cada papel, com dono da aplicação acompanhando.
    4. **Implantação gradual:** por ondas de papel, em janelas de manutenção, com reversão preparada.
    5. **Automação:** políticas de grupo e verificação diária; correção automática de desvios.
    6. **Exceções:** registradas com dono e prazo.
    - **Por que não no fim de semana:** aplicar Level 2 sem teste em 80 servidores tende a quebrar aplicações e provocar a reversão total do hardening.
    - **Trade-off aceito e risco residual:** servidores das últimas ondas continuam com a configuração atual por semanas; o residual é tratado colocando os DCs e o plano de controle na primeira onda e o servidor de etiquetas como exceção compensada.
    - **O que mudaria a decisão:** um incidente em curso ou uma exigência de auditoria com prazo curto favorece C como medida imediata, seguida de B; um ambiente de homologação fiel e pequeno número de papéis aproximaria A de B.

    **Erros comuns:**

    - Aplicar o perfil mais restritivo em todos os servidores de uma vez, sem teste.
    - Tratar o benchmark como baseline aprovada sem adaptação ao ambiente.
    - Aplicar a baseline uma vez e não medir os desvios depois.

## Pontos-chave

- Benchmark é referência; baseline é decisão aprovada; configuração efetiva é a realidade.
- A SecCM tem quatro fases: planejar, implementar, controlar mudanças e monitorar.
- Escolha perfis conforme o risco e teste antes de aplicar.
- Automação e imagens de referência mantêm a baseline; varreduras detectam desvios.
- Exceções são legítimas quando registradas, com dono e prazo.

## Referências

### Fundamentação principal

- NIST. *SP 800-128 — Guide for Security-Focused Configuration Management of Information Systems*. 2011 (atualizações de 2019). <https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-128.pdf> — Sec. 2.1.3 a 2.3.7 (pp. 6–11). *(Lido; páginas reconferidas em 2026-10-29.)*
- NIST. *SP 800-70 Rev. 5 — National Checklist Program*. 2026. <https://csrc.nist.gov/pubs/sp/800/70/r5/final>. *(Página oficial conferida.)*
- CIS. *CIS Benchmarks — FAQ*. <https://www.cisecurity.org/cis-benchmarks>. *(Lido.)*
- CIS. *CIS Controls v8.1* — Controle 4 — gratuito.
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — família CM; controles CM-2, CM-2(2), CM-3, CM-4, CM-6, CM-6(1) e CM-7, conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- NSA. *Network Infrastructure Security Guidance* — configuração de equipamentos de rede.
- CISA. *#StopRansomware Guide* — imagens de referência e IaC.

### Aplicação prática

- Escolha um tipo de servidor da sua organização, rode uma verificação contra o benchmark Level 1 em um sistema de teste e liste os itens que você ajustaria na baseline, com justificativa.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
