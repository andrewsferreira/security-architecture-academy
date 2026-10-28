---
id: M03-L05
title: "Aula 05 — Business Impact Analysis, RTO e RPO"
public_title: "Módulo 3 — Aula 05 — Business Impact Analysis, RTO e RPO"
description: Como a análise de impacto no negócio transforma a pergunta "quanto tempo podemos ficar parados?" em requisitos de arquitetura — MTD, RTO e RPO por processo, dependências e prioridades de recuperação — e como validar que a arquitetura entrega esses números.
domain: grc
tier: professional
status: published
prerequisites: [M03-L01, M00-L04]
objectives:
  - Conduzir as três etapas de uma BIA e produzir requisitos de recuperação por processo de negócio.
  - Definir MTD, RTO e RPO e explicar por que o RTO precisa ser menor que o MTD.
  - Derivar decisões de arquitetura (replicação, backup, redundância) a partir dos objetivos de recuperação.
  - Identificar dependências ocultas que invalidam objetivos declarados.
minutes: 60
sources: [NIST-SP800-34-R1, AWS-DR-WHITEPAPER, AWS-WA-RELIABILITY]
further_reading: [NIST-CSF-2, ISO-27002-2022]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M03
---

# Aula 05 — Business Impact Analysis, RTO e RPO { #business-impact-analysis-rto-e-rpo }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 3 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M03-L05</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    "Alta disponibilidade" não é requisito: é um adjetivo. Requisito é "o faturamento não pode ficar parado mais de 4 horas e não pode perder mais de 15 minutos de pedidos". A **Business Impact Analysis (BIA)** é o método que produz esses números a partir do impacto no negócio, e os objetivos de recuperação — **MTD, RTO e RPO** — são a ponte entre a governança e decisões de arquitetura como replicação, backup e redundância. Esta aula mostra como conduzir a BIA, como interpretar os objetivos e como verificar se a arquitetura os cumpre.

**Pré-requisitos:** [Governança de segurança e o NIST CSF 2.0](01-governance-csf.md) e [Datacenter e alta disponibilidade](../00-foundations/04-datacenter-high-availability.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Conduzir as três etapas de uma BIA e produzir requisitos de recuperação por processo de negócio.
- Definir MTD, RTO e RPO e explicar por que o RTO precisa ser menor que o MTD.
- Derivar decisões de arquitetura (replicação, backup, redundância) a partir dos objetivos de recuperação.
- Identificar dependências ocultas que invalidam objetivos declarados.

## Conceito

### O que a BIA responde

A BIA responde a três perguntas, nesta ordem:

1. **Quais processos de negócio são críticos e quanto tempo podem ficar parados?**
2. **De que recursos — sistemas, dados, pessoas, fornecedores — cada processo depende?**
3. **Em que ordem esses recursos precisam ser recuperados?**

A NIST SP 800-34 Rev. 1 organiza a BIA exatamente nessas três etapas — determinar processos e criticidade de recuperação, identificar requisitos de recursos e identificar prioridades de recuperação (Sec. 3.2, pp. 15–19) — e a coloca como a segunda das sete etapas do planejamento de contingência, logo após a política e antes da escolha de controles preventivos e estratégias (Cap. 3, p. 13).

### Os três objetivos

| Objetivo | Definição de trabalho | Pergunta |
|:---|:---|:---|
| **MTD** — Maximum Tolerable Downtime | Tempo total de interrupção que o dono do processo está disposto a aceitar | Quanto tempo o **processo** pode ficar parado? |
| **RTO** — Recovery Time Objective | Tempo máximo que um **recurso** pode ficar indisponível antes de causar impacto inaceitável | Em quanto tempo o **sistema** precisa voltar? |
| **RPO** — Recovery Point Objective | Ponto no tempo, antes da interrupção, até o qual os dados precisam ser recuperáveis | Quanto **dado** podemos perder? |

A SP 800-34 observa que o RTO normalmente precisa ser **menor** que o MTD — porque, depois que o sistema volta, ainda é preciso verificar dados e retomar o processo — e que o RPO **não faz parte** do MTD (Sec. 3.2.1, p. 17).

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m03-l05-bia-timeline.mmd"
```

<figcaption>Figura 1 — RPO mede a perda de dados antes do incidente; RTO mede a recuperação do recurso; o MTD limita a interrupção total do processo.</figcaption>
</figure>

## Fundamentos técnicos

### Etapa 1 — processos e criticidade

A BIA começa pelos **processos de negócio**, não pelos sistemas. Para cada processo, o dono responde como o impacto evolui no tempo: financeiro, operacional, legal, reputacional, de segurança de pessoas. Uma curva de impacto ajuda a escolher o MTD:

| Tempo parado | Faturamento | Expedição | Folha de pagamento |
|:---|:---|:---|:---|
| 1 hora | Baixo | Médio | Nenhum |
| 4 horas | Alto — pedidos acumulam | Alto — caminhões parados | Nenhum |
| 24 horas | Muito alto — perda de clientes | Muito alto — contratos com multa | Baixo |
| 5 dias | Inaceitável | Inaceitável | Alto, se coincidir com o fechamento |

### Etapa 2 — recursos e dependências

Para cada processo crítico, liste os recursos dos quais ele depende — e as dependências **deles**. É aqui que objetivos declarados costumam ser invalidados:

- O ERP tem RTO de 4 horas, mas depende do Active Directory, cujo plano de recuperação leva 12 horas.
- O sistema de expedição foi replicado para outro site, mas a impressora de etiquetas só funciona com um servidor que não foi.
- O backup está em outro datacenter, mas a chave de cifragem do backup está no cofre que foi cifrado pelo ransomware.

O RTO efetivo de um processo é limitado pela **cadeia de dependências mais lenta**.

### Etapa 3 — prioridades de recuperação

Com dependências mapeadas, define-se a **ordem**: identidade, rede e DNS geralmente vêm antes das aplicações; bancos de dados antes dos serviços que os consomem. A ordem precisa estar escrita e ensaiada — em uma crise, discutir a sequência consome o RTO.

### Dos objetivos à arquitetura

| Objetivo (faixa indicativa) | Opções de arquitetura (do mais barato ao mais caro) |
|:---|:---|
| **RPO de dias** | Backup diário fora do ambiente |
| **RPO de horas** | Backups incrementais frequentes, snapshots |
| **RPO de minutos** | Replicação assíncrona, envio contínuo de logs de transação |
| **RPO próximo de zero** | Replicação síncrona — com custo de latência e distância |
| **RTO de dias** | Reconstrução a partir de backup |
| **RTO de horas** | Dados replicados e infraestrutura mínima pronta para ser ampliada (*pilot light*) |
| **RTO de dezenas de minutos** | Ambiente sempre ativo com capacidade reduzida (*warm standby*) |
| **RTO de minutos** | Ativo-passivo com failover automatizado ou ativo-ativo |

As faixas da tabela são indicativas: o tempo real depende da implementação, da automação e de ensaios. O whitepaper *Disaster Recovery of Workloads on AWS* descreve qualitativamente as quatro estratégias em cloud — backup e restauração, *pilot light*, *warm standby* e multi-site ativo-ativo — em ordem de recuperação mais rápida e custo maior; o raciocínio vale para qualquer provedor ou ambiente. O mesmo documento alerta que a replicação contínua pode não proteger contra corrupção de dados ou exclusão maliciosa tão bem quanto backups pontuais, e que, mesmo no ativo-ativo, a recuperação de corrupção costuma depender de backups — com ponto de recuperação diferente de zero.

!!! warning "Disponibilidade e recuperação de ransomware não são a mesma coisa"

    Replicação síncrona protege contra a queda de um site — e replica a cifragem do ransomware em segundos. Para ataques que corrompem dados, o RPO real depende de uma **cópia imutável ou isolada**, anterior ao comprometimento. Uma BIA de segurança precisa perguntar: "de qual ponto conseguimos recuperar com confiança de que o dado está íntegro?".

## Exemplo empresarial

!!! example "Meridiana Distribuidora — o RTO que não fechava"

    A BIA da Meridiana definiu para a **expedição dos CDs**: MTD de 24 horas, RTO de 8 horas para o WMS e RPO de 1 hora. A arquitetura proposta replicava o WMS para um segundo datacenter.

    O mapeamento de dependências revelou:

    | Dependência | Tempo de recuperação atual | Problema |
    |:---|:---|:---|
    | Active Directory | 12 h (reconstrução manual) | Excede o RTO de 8 h |
    | Backup do WMS | Diário, no mesmo domínio | RPO real de 24 h; vulnerável ao ransomware |
    | Servidor de etiquetas | Sem cópia | Expedição parada mesmo com o WMS de pé |

    Decisões: procedimento de recuperação do AD ensaiado com meta de 4 horas, cópia imutável do backup fora do domínio a cada hora e o servidor de etiquetas incluído no plano. O RTO de 8 horas deixou de ser apenas declarado: passou a ser medido em exercícios, e o reporte à diretoria acompanha a distância entre o tempo medido e a meta ([Aula 08](08-metrics-maturity-reporting.md)).

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Ponto de partida | Sistemas e infraestrutura | Processos de negócio e impacto no tempo |
| Objetivos | "Alta disponibilidade" para tudo | MTD, RTO e RPO por processo, aprovados pelo dono |
| Dependências | Ignoradas | Mapeadas até identidade, rede, chaves e fornecedores |
| Ransomware | Tratado como desastre físico | Cópias imutáveis ou isoladas e ponto íntegro conhecido |
| Comprovação | Plano em documento | Exercícios com tempos medidos |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, opções de RTO e RPO curtos ficam mais acessíveis (múltiplas zonas, snapshots, réplicas gerenciadas), mas dependências críticas mudam: o **plano de controle do provedor**, a **identidade** usada para administrar a conta e as **chaves de cifragem** passam a fazer parte da BIA. Em ambientes híbridos, a conectividade entre ambientes e a sincronização de identidade frequentemente são a dependência mais lenta — e as menos testadas.

## Como especificar e implementar

- "Todo processo crítico tem MTD aprovado pelo dono do processo; RTO e RPO dos sistemas que o suportam derivam dele."
- "O RTO de um sistema considera o tempo de recuperação de todas as suas dependências."
- "Sistemas críticos têm cópia de dados imutável ou isolada, com retenção suficiente para recuperar a partir de um ponto íntegro."
- "A ordem de recuperação está documentada e é ensaiada ao menos uma vez por ano, com tempos medidos."

## Trade-offs, limitações e antipadrões

- **Trade-off:** custo cresce de forma acentuada quando RTO e RPO se aproximam de zero; nem todo processo justifica ativo-ativo.
- **Antipadrão — RTO declarado e nunca testado:** o número está no contrato, mas ninguém mediu.
- **Antipadrão — BIA feita pela TI:** sem o dono do processo, o MTD vira palpite técnico.
- **Limitação:** a BIA é uma fotografia; mudanças de processo e de arquitetura exigem revisão.

## Como validar

- Executar exercícios de recuperação e comparar o tempo medido com o RTO.
- Restaurar dados de um ponto anterior e verificar a integridade, confirmando o RPO real.
- Revisar o mapa de dependências de um processo crítico com a equipe de infraestrutura.
- Verificar se a chave e as credenciais necessárias à restauração estão disponíveis em um cenário de comprometimento do domínio.

## Como apresentar e justificar

- **Para a diretoria:** "Hoje, se o datacenter parar, a expedição volta em 30 horas — o limite que vocês aceitaram é 24. Estas três mudanças miram 8 horas, e vamos medir o resultado em exercício."
- **Para engenharia:** "O RPO de 1 hora vale para ransomware também. Replicação síncrona sozinha não atende: precisamos de um ponto imutável."

## Checklist de revisão arquitetural

- [ ] MTD aprovado pelo dono de cada processo crítico.
- [ ] RTO menor que o MTD, com margem para verificação e retomada.
- [ ] Dependências mapeadas, inclusive identidade, DNS, chaves e fornecedores.
- [ ] RPO considera corrupção de dados, não apenas perda de site.
- [ ] Ordem de recuperação documentada e ensaiada.
- [ ] Tempos medidos em exercício registrados.

## Questões de compreensão

**1.** Por que o RTO precisa ser menor que o MTD?

??? success "Resposta comentada"

    Porque o MTD mede a interrupção total do processo. Depois que o recurso de TI é recuperado (RTO), ainda é preciso verificar dados, reprocessar transações e retomar o trabalho. Se o RTO for igual ao MTD, não sobra tempo para essas etapas.

**2.** Um sistema tem replicação síncrona para outro site. Seu RPO para ransomware é zero?

??? success "Resposta comentada"

    Não. A replicação síncrona copia a cifragem ou a corrupção imediatamente. O RPO efetivo para ransomware é determinado pela cópia íntegra mais recente — em geral, uma cópia imutável ou isolada.

**3.** Por que a BIA começa pelos processos de negócio e não pelos sistemas?

??? success "Resposta comentada"

    Porque o impacto acontece no negócio. Um sistema só é crítico porque um processo crítico depende dele. Começar pelos sistemas leva a objetivos técnicos sem relação com o impacto real e omite dependências não tecnológicas, como pessoas e fornecedores.

## Exercício de tomada de decisão

!!! question "Cenário: estratégia de recuperação do agendamento da Lumen"

    A BIA da Lumen definiu para o agendamento de consultas: MTD de 8 horas (há atendimento telefônico de contingência), do qual a equipe derivou um RTO de 4 horas para o sistema, e RPO de 15 minutos (agendamentos perdidos geram faltas e retrabalho). O sistema roda em cloud, em uma região. Opções: (A) backup a cada 15 minutos e reconstrução em outra região; (B) réplica do banco em outra região com envio contínuo de logs e ambiente pré-provisionado (*warm standby*); (C) ativo-ativo em duas regiões. Compare as opções com uma matriz ponderada — atende ao RTO com margem para o MTD (peso 3), atende ao RPO de 15 minutos (3), custo (2) e complexidade operacional (2); notas de 1 a 3, 3 = melhor desempenho no critério, inclusive nos de custo e complexidade, em que 3 significa o menor custo ou a menor complexidade — e recomende.

??? success "Resolução de referência"

    | Critério | Peso | A — Backup + reconstrução | B — Warm standby | C — Ativo-ativo |
    |:---|:---|:---|:---|:---|
    | Atende ao RTO com margem para o MTD | 3 | 1 | 3 | 3 |
    | Atende ao RPO de 15 min | 3 | 2 | 3 | 3 |
    | Custo (3 = menor) | 2 | 3 | 2 | 1 |
    | Complexidade operacional (3 = menor) | 2 | 3 | 2 | 1 |
    | **Total ponderado** | | **21** | **26** | **22** |

    **Pesos:** RTO e RPO recebem 3 porque são os requisitos aprovados pelo dono do processo; uma opção que não os atende não resolve o problema. Custo e complexidade recebem 2 porque a equipe de plataforma é pequena e o atendimento telefônico reduz a urgência de soluções mais caras.

    **Recomendação: B.** Atende aos objetivos com folga e custo moderado. A opção A tem RTO incerto (reconstruir em outra região sob pressão) e RPO no limite; a C entrega mais do que o MTD de 8 horas exige, com custo e complexidade maiores.

    **Complemento obrigatório:** cópia imutável dos dados, porque a réplica de B não protege contra corrupção ou ransomware. **Residual:** falha simultânea das duas regiões, coberta pelo atendimento telefônico.

    **O que mudaria a decisão:** se o atendimento telefônico deixasse de existir e o MTD caísse para menos de uma hora, C passaria a ser necessária; se o dono do processo aceitasse um MTD de alguns dias, A seria suficiente — desde que a reconstrução fosse ensaiada e medida.

## Pontos-chave

- A BIA parte dos processos de negócio e de como o impacto cresce no tempo.
- MTD é do processo; RTO é do recurso; RPO é dos dados.
- O RTO precisa ser menor que o MTD; o RPO não faz parte do MTD.
- Dependências — identidade, DNS, chaves, fornecedores — frequentemente determinam o RTO real.
- Para ransomware, o RPO depende de cópias imutáveis ou isoladas, não de replicação.

## Referências

### Fundamentação principal

- NIST. *SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems*. 2010. <https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final> — Cap. 3 (p. 13), Sec. 3.2 (pp. 15–19), Sec. 3.2.1 (p. 17). *(Lido.)*
- AWS. *Disaster Recovery of Workloads on AWS: Recovery in the Cloud* — seção *Disaster recovery options in the cloud*. <https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html>. *(Lido.)*
- AWS. *Well-Architected Framework — Reliability Pillar*. <https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html> — princípios de confiabilidade e recuperação.

### Leitura complementar

- NIST. *CSF 2.0* — categorias de recuperação (RC) e de resiliência na função PROTECT.
- ISO/IEC 27002:2022 — controle 5.30, prontidão de TIC para continuidade de negócios.

### Aplicação prática

- Escolha um processo de negócio, desenhe a curva de impacto com o dono do processo e mapeie as dependências até identidade, rede e chaves. Compare o RTO declarado com o que as dependências permitem.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
