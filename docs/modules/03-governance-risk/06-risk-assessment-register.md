---
id: M03-L06
title: "Aula 06 — Risk assessment, risk register e tratamento de riscos"
public_title: "Módulo 3 — Aula 06 — Risk assessment, risk register e tratamento de riscos"
description: Como conduzir uma avaliação de riscos útil para decisões de arquitetura — enquadramento, modelo de risco, abordagens de avaliação e de análise —, como manter um risk register vivo e como escolher e registrar o tratamento de cada risco.
domain: grc
tier: professional
status: published
prerequisites: [M01-L06, M03-L05]
objectives:
  - Aplicar o modelo genérico de risco da SP 800-30 Rev. 1 a cenários concretos.
  - Escolher entre abordagens qualitativa, semiquantitativa e quantitativa, e entre análise orientada a ameaça, a ativo ou a vulnerabilidade.
  - Estruturar um risk register com campos que sustentem decisões e auditoria.
  - Definir apetite e tolerância e usá-los para decidir entre mitigar, transferir, evitar ou aceitar.
minutes: 90
sources: [NIST-SP800-30-R1, NIST-CSF-2, BOOK-ANDERSON-SE3]
further_reading: [NIST-SP800-37-R2, MITRE-ATTACK, TOG-RISK-SECURITY]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M03
---

# Aula 06 — Risk assessment, risk register e tratamento de riscos { #risk-assessment-risk-register-e-tratamento-de-riscos }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 3 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">90 min · ID técnico: M03-L06</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    A [Aula 06 do Módulo 1](../01-security-fundamentals/06-threat-vulnerability-risk.md) definiu a linguagem do risco. Esta aula transforma a linguagem em **processo**: enquadrar o contexto, avaliar cenários com um modelo explícito, registrar os resultados em um risk register que as pessoas consultem, decidir o tratamento conforme o apetite a risco e monitorar se a decisão continua válida. O foco é o que torna a avaliação útil para a arquitetura: cenários concretos, justificativas, donos e prazos.

**Pré-requisitos:** [Ameaça, vulnerabilidade, risco e controle](../01-security-fundamentals/06-threat-vulnerability-risk.md) e [BIA, RTO e RPO](05-bia-rto-rpo.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Aplicar o modelo genérico de risco da SP 800-30 Rev. 1 a cenários concretos.
- Escolher entre abordagens qualitativa, semiquantitativa e quantitativa, e entre análise orientada a ameaça, a ativo ou a vulnerabilidade.
- Estruturar um risk register com campos que sustentem decisões e auditoria.
- Definir apetite e tolerância e usá-los para decidir entre mitigar, transferir, evitar ou aceitar.

## Conceito

### Quatro componentes da gestão de riscos

A SP 800-30 Rev. 1 descreve a gestão de riscos em quatro componentes (Sec. 2.1, p. 4):

| Componente | O que produz |
|:---|:---|
| **Enquadrar** (*frame*) | Contexto, premissas, restrições, apetite e tolerância — a estratégia de gestão de riscos |
| **Avaliar** (*assess*) | Ameaças, vulnerabilidades, impacto e probabilidade, resultando em uma determinação de risco |
| **Responder** (*respond*) | Cursos de ação coerentes com a tolerância da organização |
| **Monitorar** (*monitor*) | Acompanhamento da eficácia das respostas e das mudanças nos sistemas e no ambiente |

A avaliação é só um dos quatro. Avaliações sem enquadramento produzem notas sem referência ("risco alto em relação a quê?"); avaliações sem monitoramento envelhecem em meses.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m03-l06-risk-process.mmd"
```

<figcaption>Figura 1 — Componentes da gestão de riscos e o ciclo de vida de um item do risk register.</figcaption>
</figure>

### Três níveis

A mesma publicação distingue três níveis de gestão de riscos — **organização**, **processo de negócio** e **sistema de informação** (Sec. 2.4, p. 17). O arquiteto circula entre eles: um risco de sistema (API sem rate limiting) pode compor um risco de processo (fraude no cadastro) que interessa à organização (perda financeira material).

## Fundamentos técnicos

### O modelo genérico de risco

O modelo da SP 800-30 (Sec. 2.3.1, pp. 8–12) relaciona: **fonte de ameaça** que inicia um **evento de ameaça**, que explora **vulnerabilidades** em um contexto de **condições predisponentes**, com uma **probabilidade** — que combina a chance de o evento ocorrer e a de ele resultar em impacto — e um **impacto**. **Risco** é função da probabilidade e do impacto.

O elemento menos usado na prática — e um dos mais úteis para a arquitetura — é a **condição predisponente**: uma característica do ambiente que aumenta ou reduz a probabilidade de impacto. Rede plana, contas compartilhadas e dependência de um único fornecedor são condições predisponentes; mudá-las costuma ser decisão de arquitetura.

### Abordagens de avaliação

| Abordagem | Característica (Sec. 2.3.2, p. 14) | Quando usar |
|:---|:---|:---|
| **Quantitativa** | Números com significado mantido fora do contexto da avaliação; apoia análise de custo-benefício | Há dados (frequência, perdas) e a decisão envolve investimento relevante |
| **Qualitativa** | Níveis não numéricos (baixo, moderado, alto); facilita comunicação, limita comparação fina | Triagem inicial, poucos dados, público executivo |
| **Semiquantitativa** | Escalas ou faixas que combinam características das duas | Priorização entre muitos riscos com consistência |

### Abordagens de análise

A SP 800-30 descreve três pontos de partida (Sec. 2.3.3, pp. 15–16): **orientada a ameaça** (fontes e eventos primeiro), **orientada a ativo e impacto** (ativos críticos e impactos de preocupação primeiro) e **orientada a vulnerabilidade** (fraquezas e condições predisponentes primeiro). O documento alerta que partir de uma só orientação pode enviesar o resultado; combinar orientações aumenta o rigor.

Na prática de arquitetura, um caminho eficaz é começar pelos **ativos e processos críticos** (a BIA já os identificou), cruzar com **ameaças relevantes** para o setor — o MITRE ATT&CK ajuda a tornar os eventos concretos (Módulo 4 — Aula 04) — e então verificar as **vulnerabilidades e condições predisponentes** que tornam cada cenário possível.

### Apetite e tolerância

- **Apetite a risco:** o quanto de risco a organização está disposta a assumir para atingir seus objetivos — uma declaração de governança (GV.RM no CSF 2.0).
- **Tolerância:** o desvio aceitável em relação ao apetite, expresso de forma verificável ("nenhum risco alto sem tratamento por mais de 90 dias"; "indisponibilidade da expedição acima de 24 horas é inaceitável").

Sem tolerância explícita, toda decisão de aceite é negociada caso a caso — e o arquiteto vira árbitro de algo que é da governança.

### O risk register

Um risk register útil para arquitetura tem, no mínimo:

| Campo | Exemplo | Por que importa |
|:---|:---|:---|
| ID e título do cenário | RSK-007 — Ransomware a partir do acesso remoto | Referência estável para ADRs e controles |
| Ativos e processos afetados | Expedição, ERP, backup | Liga à BIA |
| Fonte e evento de ameaça | Grupo de ransomware; acesso por credencial roubada | Torna o cenário concreto |
| Vulnerabilidades e condições predisponentes | VPN sem MFA; rede plana; backup no domínio | Mostra onde a arquitetura atua |
| Probabilidade e impacto, com justificativa | Alta (VPN exposta, ataques frequentes); muito alto (MTD de 24 h excedido) | Permite revisão crítica |
| Risco inerente e residual | Crítico → Médio | Mostra o efeito do tratamento |
| Tratamento | Mitigar: MFA, segmentação, backup imutável | Decisão explícita |
| Controles e ADRs relacionados | CTL-IAM-03, CTL-BKP-02; ADR-012 | Rastreabilidade (Aula 07) |
| Dono do risco e data de aceite | Diretor de operações, 2026-09-30 | Responsabilização |
| Próxima revisão | 2027-03-31 | Evita envelhecimento |

### Tratamento

As quatro opções — **mitigar**, **transferir**, **evitar**, **aceitar** — foram apresentadas na Aula 06 do Módulo 1. Na decisão, três regras ajudam:

1. O residual de cada opção precisa ser comparado à **tolerância**, não à intuição.
2. **Aceitar** é decisão do dono do risco, registrada, com prazo de revisão — nunca uma omissão.
3. **Transferir** cobre parte do impacto financeiro; parada, dados perdidos e reputação continuam com a organização.

Anderson lembra que estimativas de risco misturam dados, suposições e política interna, e que quantificar riscos raros e de alto impacto é particularmente difícil (*Security Engineering*, Cap. 27, §27.2 e §27.3.6). Por isso, registrar a **justificativa** importa mais do que a precisão aparente do número.

## Exemplo empresarial

!!! example "Aurora Pagamentos — do register esquecido ao register usado"

    O register da Aurora tinha 210 itens, metade sem dono e um terço sem revisão havia dois anos. O arquiteto propôs três mudanças:

    1. **Consolidar em cenários:** 210 itens viraram 34 cenários; vulnerabilidades individuais passaram a ser evidências dentro dos cenários.
    2. **Ligar à governança:** a diretoria aprovou a tolerância "nenhum risco crítico sem tratamento em andamento; nenhum alto aceito por mais de 12 meses sem nova decisão".
    3. **Ligar à arquitetura:** todo ADR passou a referenciar os cenários que trata, e todo cenário, os controles que o reduzem.

    | Cenário | Inerente | Tratamento | Residual | Dono |
    |:---|:---|:---|:---|:---|
    | RSK-012 — Fraude por API de cadastro sem limites | Alto | Mitigar: rate limiting, detecção de anomalias | Médio | Diretor de produtos |
    | RSK-019 — Indisponibilidade do provedor de antifraude | Alto | Transferir parcialmente (SLA com crédito) + mitigar (modo degradado) | Médio | Diretor de operações |
    | RSK-027 — Integração FTP legada com parceiro | Médio | Evitar: migração para API até o fim do trimestre | Baixo | Diretor de parcerias |

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Unidade | Vulnerabilidade individual | Cenário com ativo, ameaça, vulnerabilidade e impacto |
| Escala | Notas sem referência | Escala enquadrada por apetite e tolerância |
| Register | Planilha anual | Registro vivo, ligado a ADRs, controles e indicadores |
| Aceite | Por omissão | Decisão registrada do dono, com prazo |
| Análise | Uma única orientação | Combinação de ativo, ameaça e vulnerabilidade |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, condições predisponentes típicas são permissões excessivas, contas sem guardrails e recursos expostos por configuração; elas mudam rápido, e o register precisa de monitoramento contínuo (postura de cloud, Módulo 10). Em ambientes híbridos, cenários que atravessam ambientes — comprometimento on-premises que alcança a cloud pela sincronização de identidade — costumam ficar fora de avaliações feitas por equipes separadas; um cenário só, com dono único, evita essa lacuna.

## Como especificar e implementar

- "Avaliações de risco descrevem cenários com fonte de ameaça, evento, vulnerabilidades, condições predisponentes, probabilidade e impacto justificados."
- "A escala de risco é enquadrada por apetite e tolerância aprovados pela governança."
- "Todo risco alto ou crítico tem dono, tratamento, prazo e controles relacionados no register."
- "ADRs referenciam os cenários de risco que tratam."
- "O register é revisado ao menos trimestralmente e sempre que houver mudança relevante."

## Trade-offs, limitações e antipadrões

- **Trade-off:** granularidade versus utilidade. Cenários demais tornam o register ilegível; de menos, escondem diferenças importantes.
- **Antipadrão — mapa de calor como fim:** cores bonitas sem tratamento nem dono.
- **Antipadrão — avaliação feita só por segurança:** sem o dono do processo, o impacto vira palpite.
- **Limitação:** a avaliação reflete o conhecimento atual; ameaças novas exigem revisão — por isso o monitoramento é um componente, não um anexo.

## Como validar

- Amostrar cinco riscos altos e verificar dono, tratamento, prazo e justificativa.
- Conferir se os riscos aceitos estão dentro da tolerância declarada.
- Verificar se os controles citados no register existem e têm evidência.
- Comparar incidentes recentes com o register: algum aconteceu sem estar registrado?

## Como apresentar e justificar

- **Para a diretoria:** "Temos 34 cenários. Dois estão fora da tolerância que vocês aprovaram; precisamos de decisão sobre eles."
- **Para engenharia:** "Este ADR existe por causa do RSK-007. Se mudarem a decisão, o risco residual muda e o dono precisa saber."

## Checklist de revisão arquitetural

- [ ] O contexto, o apetite e a tolerância estão enquadrados.
- [ ] Os riscos estão descritos como cenários completos.
- [ ] Probabilidade e impacto têm justificativa.
- [ ] Mais de uma orientação de análise foi usada.
- [ ] Todo risco alto tem dono, tratamento, prazo e controles relacionados.
- [ ] O register está ligado a ADRs, controles e indicadores.

## Questões de compreensão

**1.** O que é uma condição predisponente e por que ela interessa ao arquiteto?

??? success "Resposta comentada"

    É uma característica do ambiente que aumenta ou reduz a probabilidade de um evento de ameaça causar impacto — por exemplo, rede plana ou contas compartilhadas. Interessa porque mudá-la geralmente é uma decisão de arquitetura que reduz o risco de vários cenários ao mesmo tempo.

**2.** Por que a SP 800-30 recomenda combinar orientações de análise?

??? success "Resposta comentada"

    Porque partir só de ameaças, só de ativos ou só de vulnerabilidades enviesa o resultado: cada orientação tende a enxergar o que está no seu ponto de partida e a ignorar o resto. Combinar aumenta a cobertura e o rigor.

**3.** Qual a diferença prática entre apetite e tolerância?

??? success "Resposta comentada"

    O apetite é a declaração geral de quanto risco a organização aceita para alcançar objetivos; a tolerância é o desvio aceitável, expresso de forma verificável. A tolerância é o que permite decidir caso a caso sem renegociar a política a cada risco.

## Exercício de tomada de decisão

!!! question "Cenário: risco do fornecedor de laudos da Lumen"

    O laboratório parceiro da Lumen envia laudos por uma integração que usa credencial estática compartilhada, sem rotação há três anos. A credencial dá acesso de escrita ao repositório de laudos. A tolerância aprovada é "nenhum risco alto envolvendo dados de saúde aceito por mais de 90 dias". O laboratório informou que consegue adotar federação de identidade e assinatura de laudos em cerca de dois meses. Descreva o cenário no formato do register, estime o risco com justificativa e escolha o tratamento entre três opções, usando uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho):

    - **A** — aceitar o risco até a renovação do contrato com o laboratório, daqui a oito meses;
    - **B** — mitigar em duas etapas: rotacionar a credencial, restringir a escrita ao prefixo do laboratório e criar alertas em 30 dias; adotar credencial federada e assinatura de laudos em até 90 dias;
    - **C** — evitar: suspender a integração e voltar ao recebimento manual de laudos até a solução definitiva.

??? success "Resolução de referência"

    - **Cenário RSK-041:** comprometimento da credencial da integração com o laboratório permite alterar ou inserir laudos.
    - **Fonte e evento:** atacante que comprometa o laboratório ou intercepte a credencial; inserção ou alteração de laudos.
    - **Vulnerabilidades e condições predisponentes:** credencial estática, compartilhada e sem rotação; permissão de escrita ampla; ausência de verificação de integridade dos laudos.
    - **Probabilidade:** média — exige comprometer o parceiro, mas a credencial é antiga e compartilhada. **Impacto:** muito alto — integridade de dados de saúde e possível dano ao paciente. **Risco inerente:** alto.
    - **Escolha do tratamento:**

        | Critério | Peso | A — Aceitar até a renovação | B — Mitigar em duas etapas | C — Suspender a integração |
        |:---|:---|:---|:---|:---|
        | Redução do risco à integridade dos laudos | 3 | 1 | 3 | 3 |
        | Compatibilidade com a tolerância de 90 dias | 3 | 1 | 3 | 3 |
        | Continuidade do atendimento aos pacientes | 2 | 3 | 3 | 1 |
        | Custo e esforço (3 = menor) | 1 | 3 | 2 | 2 |
        | **Total ponderado** | | **15** | **26** | **22** |

        **Pesos:** a integridade de dados de saúde e a tolerância aprovada pela governança recebem 3; a continuidade do atendimento recebe 2 porque o recebimento manual atrasa diagnósticos; custo recebe 1 porque as três opções cabem no orçamento da área. A opção A está fora da tolerância — oito meses superam os 90 dias aprovados — e, mesmo que somasse mais pontos, exigiria uma decisão formal de exceção pela governança.

    - **Tratamento recomendado — B, mitigar:** credencial por workload com rotação automática ou federação; escrita restrita a um prefixo por laboratório; assinatura dos laudos pelo laboratório e verificação na ingestão; alerta para volume ou horário anômalo.
    - **Residual:** baixo a médio, com comprometimento do próprio laboratório como risco remanescente. **Dono:** diretor clínico. **Prazo:** dentro dos 90 dias da tolerância; se a mitigação atrasar, nova decisão formal.
    - **O que mudaria a decisão:** evidência de uso indevido da credencial antecipa C imediatamente, como contenção; se o laboratório não conseguir adotar federação e assinatura no prazo, a segunda etapa vira exceção formal com controles compensatórios e nova data.

## Pontos-chave

- Avaliar é só um dos quatro componentes: enquadrar, avaliar, responder e monitorar.
- Cenários completos, com condições predisponentes, tornam o risco acionável pela arquitetura.
- Escolha a abordagem de avaliação conforme os dados e combine orientações de análise.
- Apetite e tolerância transformam aceites em decisões verificáveis.
- O register só é útil se estiver ligado a donos, ADRs, controles e indicadores.

## Referências

### Fundamentação principal

- NIST. *SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments*. 2012. <https://csrc.nist.gov/pubs/sp/800/30/r1/final> — Sec. 2.1 (p. 4), 2.3.1 (pp. 8–12), 2.3.2 (p. 14), 2.3.3 (pp. 15–16) e 2.4 (p. 17). *(Lido até a Sec. 2.4.)*
- NIST. *CSF 2.0* — GV.RM, estratégia de gestão de riscos, apetite e tolerância.
- R. Anderson. *Security Engineering*, 3ª ed. Cap. 27, §27.2 *Risk management* (p. 966) e §27.3.6 *Quantifying risks* (p. 975).

### Leitura complementar

- NIST. *SP 800-37 Rev. 2* — tarefa P-3, avaliação de riscos da organização.
- MITRE. *ATT&CK* — eventos de ameaça concretos para cenários (Módulo 4 — Aula 04).
- The Open Group. *Integrating Risk and Security within a TOGAF Enterprise Architecture*.

### Aplicação prática

- Use o modelo de [risk register](../../artifacts/index.md) do portal (quando disponível) ou uma planilha com os campos desta aula e registre três cenários do seu ambiente, com dono e tolerância.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
