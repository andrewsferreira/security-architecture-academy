---
id: M03-L03
title: "Aula 03 — Seleção e tailoring de controles: SP 800-53 e CIS Controls"
public_title: "Módulo 3 — Aula 03 — Seleção e tailoring de controles: SP 800-53 e CIS Controls"
description: Como passar de um catálogo com centenas de controles ao conjunto proporcional de um sistema — baselines da SP 800-53B, overlays, tailoring, controles comuns e compensatórios — e quando usar a priorização dos CIS Controls por Implementation Groups.
domain: grc
tier: professional
status: published
prerequisites: [M03-L02]
objectives:
  - Explicar a estrutura do catálogo SP 800-53 Rev. 5 e o papel das baselines da SP 800-53B.
  - Aplicar tailoring — escopo, parâmetros, compensatórios e adicionais — com justificativa registrada.
  - Comparar a abordagem por baselines do NIST com os Implementation Groups dos CIS Controls.
  - Especificar um conjunto de controles que a engenharia consiga implementar e a auditoria consiga verificar.
minutes: 90
sources: [NIST-SP800-53, NIST-SP800-53B, CIS-CONTROLS-V8-1, NIST-SP800-37-R2]
further_reading: [NIST-CSF-INFORMATIVE-REFS, ISO-27002-2022]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M03
---

# Aula 03 — Seleção e tailoring de controles: SP 800-53 e CIS Controls { #selecao-e-tailoring-de-controles-sp-800-53-e-cis-controls }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 3 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">90 min · ID técnico: M03-L03</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Catálogos de controles são grandes de propósito: precisam servir a sistemas de todos os tipos e impactos. O trabalho do arquiteto é **selecionar** — partir de uma baseline proporcional ao impacto, ajustá-la ao contexto do sistema e registrar por que cada ajuste foi feito. Esta aula mostra como isso funciona com a SP 800-53 Rev. 5 e as baselines da SP 800-53B, e quando a priorização por Implementation Groups dos CIS Controls v8.1 é o caminho mais adequado.

**Pré-requisito:** [NIST Risk Management Framework](02-nist-rmf.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar a estrutura do catálogo SP 800-53 Rev. 5 e o papel das baselines da SP 800-53B.
- Aplicar tailoring — escopo, parâmetros, compensatórios e adicionais — com justificativa registrada.
- Comparar a abordagem por baselines do NIST com os Implementation Groups dos CIS Controls.
- Especificar um conjunto de controles que a engenharia consiga implementar e a auditoria consiga verificar.

## Conceito

### Catálogo, baseline e conjunto do sistema

| Termo | O que é | Quem define |
|:---|:---|:---|
| **Catálogo** | Lista abrangente de controles possíveis | NIST (SP 800-53), CIS, ISO (Anexo A da 27001) |
| **Baseline** | Ponto de partida pré-selecionado para um nível de impacto | NIST (SP 800-53B) ou a própria organização |
| **Overlay** | Ajuste de uma baseline para uma comunidade, tecnologia ou ambiente | Setor, comunidade ou organização |
| **Tailoring** | Ajuste da baseline ao sistema concreto, com justificativa | Dono do sistema e arquiteto |
| **Conjunto do sistema** | Controles efetivamente exigidos, próprios e herdados | Resultado do processo, aprovado pelo dono do risco |

A **SP 800-53 Rev. 5** é um catálogo de controles de segurança e privacidade para sistemas e organizações, descrito pelo NIST como flexível e customizável. A página oficial lista **20 famílias** — de Access Control (AC) a Supply Chain Risk Management (SR) — e a versão vigente é a **Release 5.2.0**, de 27/08/2025, distribuída também em OSCAL (JSON, XML e YAML). O catálogo não é uma lista de obrigações para todas as organizações; ele é matéria-prima para seleção.

A **SP 800-53B** fornece as **baselines** baixa, moderada e alta, uma **baseline de privacidade** independente do nível de impacto, orientação de **tailoring** e de **overlays**. Na Release 5.2.0, o catálogo ganhou os controles e melhorias SA-15(13), SA-24 e SI-02(07), e a SP 800-53B foi reeditada sem mudanças nas baselines.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m03-l03-tailoring.mmd"
```

<figcaption>Figura 1 — Do catálogo ao conjunto de controles do sistema, com controles herdados e o caminho alternativo dos CIS Controls.</figcaption>
</figure>

## Fundamentos técnicos

### Tipos de ajuste no tailoring

| Ajuste | Pergunta | Exemplo | O que registrar |
|:---|:---|:---|:---|
| **Escopo** | Este controle se aplica a este sistema? | Controles de acesso sem fio em um sistema sem rede sem fio | Por que não se aplica |
| **Parâmetros** | Qual valor concreto? | Bloqueio após 5 tentativas; retenção de logs por 13 meses | O valor e a origem (política, lei, risco) |
| **Herança** | Quem já implementa? | Proteção física herdada do datacenter; MFA herdado do IdP | O provedor do controle e a evidência |
| **Compensatório** | O controle exigido é inviável; o que o substitui? | Sistema legado sem MFA publicado só via gateway com MFA | Equivalência de resultado e risco residual |
| **Adicional** | O risco exige mais que a baseline? | Monitoração reforçada de consultas em base de saúde | Cenário de risco que justifica |

O ponto central é a **justificativa**: um conjunto de controles sem justificativas é indistinguível de um conjunto escolhido por conveniência. Para a auditoria, a pergunta não é "por que vocês não têm o controle X?", mas "onde está registrada a decisão sobre o controle X?".

### Parâmetros: onde a política encontra a engenharia

Muitos controles têm parâmetros definidos pela organização — frequências, limites, prazos. Deixá-los em aberto ("periodicamente", "em tempo hábil") torna o controle inverificável. Parametrizar é uma decisão de arquitetura e de governança ao mesmo tempo: o valor precisa ser defensável pelo risco e viável para a operação.

### Controles comuns e responsabilidade compartilhada

O conjunto do sistema mistura controles **próprios**, **herdados de plataformas internas** (landing zone, identidade corporativa, SIEM) e **herdados do provedor** (cloud, SaaS). Herança só é válida quando:

1. O provedor do controle está identificado e assume a responsabilidade.
2. Há evidência vigente — relatório de avaliação, atestado do provedor de cloud, configuração verificável.
3. O sistema realmente usa o serviço que implementa o controle (não basta a plataforma oferecê-lo).

### CIS Controls v8.1 e Implementation Groups

Os **CIS Controls** seguem outra lógica: em vez de baselines por impacto, oferecem um conjunto **priorizado** de 153 safeguards, agrupados em três **Implementation Groups**. O CIS define o **IG1** como *essential cyber hygiene* — o conjunto fundamental que toda organização deveria aplicar contra os ataques mais comuns —, recomenda que todas comecem por ele, e descreve o IG3 como o conjunto que inclui todos os safeguards. A v8.1 é uma atualização iterativa da v8 que realinhou os mapeamentos ao CSF 2.0 e acrescentou a função **Govern**.

| Aspecto | SP 800-53 + 800-53B | CIS Controls v8.1 |
|:---|:---|:---|
| Ponto de partida | Categorização de impacto do sistema | Recursos e perfil de risco da organização (IG) |
| Granularidade | Controles e melhorias detalhados, com parâmetros | Safeguards objetivos e técnicos |
| Força | Rigor, rastreabilidade, privacidade integrada | Priorização clara, adoção rápida |
| Limitação | Esforço de tailoring e documentação | Menos cobertura de governança e de privacidade |
| Uso típico | Sistemas regulados, alto impacto, provedores de serviço | Organizações começando um programa; higiene técnica |

As duas abordagens não competem: muitas organizações usam o IG1 como **piso técnico corporativo** e a SP 800-53 como referência para sistemas de alto impacto, ligando ambos pelo catálogo interno (Aula 07).

## Exemplo empresarial

!!! example "Aurora Pagamentos — tailoring do serviço de antifraude"

    O serviço de antifraude foi categorizado como **moderado** para confidencialidade e **alto** para integridade e disponibilidade. Partindo da baseline alta da SP 800-53B, a equipe registrou os ajustes em uma tabela de uma página por família:

    | Controle (exemplo) | Decisão | Justificativa |
    |:---|:---|:---|
    | Proteção física | Herdado | Provedor de cloud — atestado anual de terceira parte |
    | Autenticação de administradores | Herdado + parâmetro | IdP corporativo; MFA resistente a phishing obrigatório |
    | Retenção de logs | Parâmetro: 13 meses | Requisito contratual com adquirentes e investigação de fraude |
    | Acesso sem fio | Fora de escopo | Serviço sem componentes em rede sem fio |
    | Integridade do modelo de score | Adicional | Cenário de manipulação de modelo (RSK-031) |

    O conjunto final tinha 30% de controles herdados, todos com evidência referenciada, e nenhum controle "não aplicável" sem justificativa.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Seleção | "Aplicar tudo" ou "aplicar o que der" | Baseline por impacto + tailoring justificado |
| Parâmetros | "Periodicamente", "quando necessário" | Valores concretos ligados a política ou risco |
| Herança | Presumida | Declarada, com provedor e evidência |
| Não aplicáveis | Marcados sem explicação | Justificados e revisados quando o sistema muda |
| Formato | Planilha estática | Catálogo versionado, idealmente em formato legível por máquina (OSCAL) |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, boa parte do tailoring é **herança do provedor** e da landing zone, e a evidência vem de atestados e de políticas como código. Em on-premises, a organização implementa mais controles por conta própria. Em ambientes híbridos, o mesmo controle pode ser herdado em um ambiente e próprio no outro — o conjunto do sistema deve mostrar isso por componente, não por sistema como um todo.

## Como especificar e implementar

- "Cada sistema mantém seu conjunto de controles derivado da baseline do seu nível de impacto, com justificativa para cada ajuste."
- "Parâmetros definidos pela organização constam do padrão corporativo e não podem ficar em aberto."
- "Controles herdados referenciam o provedor e a evidência vigente."
- "Controles compensatórios descrevem a equivalência de resultado e o risco residual aceito."
- "Todo ambiente corporativo atende, no mínimo, aos safeguards do CIS IG1."

## Trade-offs, limitações e antipadrões

- **Trade-off:** granularidade versus esforço. Tailoring detalhado melhora a precisão, mas consome tempo; padronize por família e por padrão de arquitetura para reaproveitar decisões.
- **Antipadrão — compensatório de fachada:** "monitoramos manualmente" como substituto de um controle técnico, sem frequência nem dono.
- **Antipadrão — baseline como teto:** tratar a baseline como suficiente mesmo quando um cenário de risco específico exige mais.
- **Limitação:** baselines refletem riscos genéricos; ameaças específicas do sistema só aparecem com threat modeling (Módulo 4).

## Como validar

- Amostrar cinco controles "não aplicáveis" e verificar a justificativa.
- Verificar se cada controle herdado tem evidência dentro da validade.
- Conferir se os parâmetros do sistema batem com os do padrão corporativo.
- Para controles compensatórios, testar o resultado equivalente (por exemplo, tentar acessar o legado sem passar pelo gateway).

## Como apresentar e justificar

- **Para auditoria:** "Este é o conjunto do sistema, com origem na baseline moderada; cada ajuste tem justificativa e cada herança tem evidência."
- **Para engenharia:** "Usando a landing zone padrão, vocês herdam 30% dos controles. O restante está descrito como requisito testável no backlog."

## Checklist de revisão arquitetural

- [ ] A baseline de partida corresponde à categorização do sistema.
- [ ] Todo ajuste de tailoring tem justificativa.
- [ ] Nenhum parâmetro ficou em aberto.
- [ ] Controles herdados têm provedor e evidência vigente.
- [ ] Compensatórios descrevem equivalência e risco residual.
- [ ] Controles adicionais estão ligados a cenários de risco.

## Questões de compreensão

**1.** Qual a diferença entre catálogo e baseline?

??? success "Resposta comentada"

    O catálogo é a lista abrangente de controles possíveis; a baseline é um subconjunto pré-selecionado como ponto de partida para um nível de impacto. O conjunto do sistema surge depois do tailoring da baseline.

**2.** Quando um controle compensatório é aceitável?

??? success "Resposta comentada"

    Quando o controle exigido é inviável e o compensatório entrega um resultado de segurança equivalente — ou próximo, com o risco residual explícito e aceito pelo dono do risco. Precisa ser verificável e ter dono.

**3.** Por que usar CIS IG1 como piso corporativo, mesmo adotando a SP 800-53 para sistemas críticos?

??? success "Resposta comentada"

    Porque o IG1 é um conjunto pequeno, priorizado e técnico de higiene que se aplica a todos os ambientes e protege contra os ataques mais comuns. A SP 800-53 traz rigor e rastreabilidade para sistemas de maior impacto. Combinados, cobrem a base de forma ampla e o topo em profundidade.

## Exercício de tomada de decisão

!!! question "Cenário: qual referência adotar na Meridiana"

    A Meridiana não tem catálogo de controles. O CISO considera três opções: (A) adotar a SP 800-53 com baselines para todos os sistemas; (B) adotar os CIS Controls, começando pelo IG1 em toda a empresa; (C) CIS IG1 como piso corporativo e baseline moderada da SP 800-53 apenas para os sistemas críticos (ERP, WMS e backup). A equipe de segurança tem três pessoas, e a seguradora pediu evidências de controles na próxima renovação. Compare as opções com uma matriz ponderada — redução de risco no curto prazo (peso 3), viabilidade com a equipe atual (3), rigor nos sistemas críticos (2) e rastreabilidade para seguradora e clientes (1); notas de 1 a 3, 3 = melhor desempenho no critério — e recomende uma opção.

??? success "Resolução de referência"

    | Critério | Peso | A — SP 800-53 para tudo | B — CIS IG1 | C — IG1 + 800-53 nos críticos |
    |:---|:---|:---|:---|:---|
    | Redução de risco no curto prazo | 3 | 1 | 3 | 3 |
    | Viabilidade com a equipe atual | 3 | 1 | 3 | 2 |
    | Rigor nos sistemas críticos | 2 | 3 | 1 | 3 |
    | Rastreabilidade para seguradora e clientes | 1 | 3 | 2 | 3 |
    | **Total ponderado** | | **15** | **22** | **24** |

    **Pesos:** redução de risco e viabilidade recebem 3 porque um catálogo que a equipe não consegue manter não reduz risco nenhum; o rigor nos sistemas críticos recebe 2 por causa do cenário de ransomware; a rastreabilidade para a seguradora e os clientes recebe 1 porque as três opções produzem alguma evidência.

    **Recomendação: C.** O IG1 entrega higiene básica em toda a empresa rapidamente, e o rigor da SP 800-53 fica concentrado nos três sistemas cuja parada interrompe a operação. A opção A é inviável para três pessoas; a B deixa os sistemas críticos sem a profundidade que o cenário de ransomware exige.

    **Risco residual:** sistemas não críticos ficam só com o piso IG1; a decisão é revista quando o catálogo interno (Aula 07) estiver estabelecido.

    **O que mudaria a decisão:** se um contrato ou regulador exigisse a SP 800-53 em todos os sistemas, A deixaria de ser opcional e o problema passaria a ser de orçamento e equipe; com uma equipe ainda menor, B seria o primeiro passo, e a baseline nos sistemas críticos viria em seguida.

## Pontos-chave

- O catálogo é matéria-prima; a baseline é ponto de partida; o tailoring torna o conjunto proporcional.
- Toda decisão de tailoring precisa de justificativa registrada.
- Herança só vale com provedor identificado e evidência vigente.
- CIS Controls priorizam por Implementation Groups; o IG1 é a higiene essencial.
- Combinar CIS IG1 como piso e SP 800-53 para sistemas críticos é uma estratégia comum e defensável.

## Referências

### Fundamentação principal

- NIST. *SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations*. Release 5.2.0, 27/08/2025. <https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final> — resumo e lista de famílias. *(Página oficial conferida.)*
- NIST. *SP 800-53B — Control Baselines for Information Systems and Organizations*. 2020. <https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final> — baselines, privacidade, tailoring e overlays. *(Página oficial conferida.)*
- CIS. *CIS Controls v8.1* e *Implementation Groups*. <https://www.cisecurity.org/controls/v8-1>; <https://www.cisecurity.org/controls/implementation-groups>. *(Páginas oficiais conferidas.)*
- NIST. *SP 800-37 Rev. 2* — etapa Select e controles comuns (Sec. 3.1, P-5).

### Leitura complementar

- NIST. *CSF 2.0 Informative References* — mapeamentos entre CSF, SP 800-53, CIS e ISO/IEC 27001.
- ISO/IEC 27002:2022 — orientação de implementação dos controles do Anexo A ([Aula 04](04-iso-lgpd-pci.md)).

### Aplicação prática

- Escolha um sistema e monte uma tabela de tailoring para uma família de controles (por exemplo, AC ou AU), com escopo, parâmetros, herança, compensatórios e adicionais.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
