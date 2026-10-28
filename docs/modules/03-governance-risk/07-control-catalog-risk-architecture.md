---
id: M03-L07
title: "Aula 07 — Catálogo de controles e arquitetura baseada em risco"
public_title: "Módulo 3 — Aula 07 — Catálogo de controles e arquitetura baseada em risco"
description: Como construir e governar um catálogo interno de controles que liga cenários de risco, objetivos de controle, building blocks de arquitetura, evidências e indicadores, mapeado a frameworks externos sem depender de nenhum deles.
domain: grc
tier: architect
status: published
prerequisites: [M03-L03, M03-L06, M02-L07]
objectives:
  - Estruturar um catálogo interno de controles com objetivo, implementação, dono, evidência e mapeamentos.
  - Traçar a cadeia risco → objetivo de controle → controle → building block → evidência → indicador.
  - Usar o catálogo para revisar arquiteturas e para responder a várias auditorias com a mesma evidência.
  - Governar o ciclo de vida do catálogo — criação, mudança, exceção e aposentadoria de controles.
minutes: 75
sources: [NIST-SP800-53, NIST-CSF-INFORMATIVE-REFS, NIST-SP800-37-R2, SABSA-W100]
further_reading: [CIS-CONTROLS-V8-1, ISO-27002-2022, TOG-RISK-SECURITY]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M03
---

# Aula 07 — Catálogo de controles e arquitetura baseada em risco { #catalogo-de-controles-e-arquitetura-baseada-em-risco }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 3 · Nível 1</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">75 min · ID técnico: M03-L07</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Organizações maduras não gerenciam "a ISO", "o PCI" e "o NIST" como programas separados: mantêm um **catálogo interno de controles**, escrito na linguagem da própria organização, em que cada controle tem objetivo, implementação de referência, dono, evidência e mapeamentos para as referências externas. Para o arquiteto, o catálogo é a ponte entre o risk register e a arquitetura: cada cenário de risco aponta para objetivos de controle, cada controle para building blocks de arquitetura, cada building block para evidências e indicadores. Esta aula mostra como estruturar e governar esse catálogo.

**Pré-requisitos:** [Seleção e tailoring de controles](03-control-selection-tailoring.md), [Risk assessment e risk register](06-risk-assessment-register.md) e [Business-driven Security Architecture](../02-security-architecture/07-business-driven-requirements.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Estruturar um catálogo interno de controles com objetivo, implementação, dono, evidência e mapeamentos.
- Traçar a cadeia risco → objetivo de controle → controle → building block → evidência → indicador.
- Usar o catálogo para revisar arquiteturas e para responder a várias auditorias com a mesma evidência.
- Governar o ciclo de vida do catálogo — criação, mudança, exceção e aposentadoria de controles.

## Conceito

### Por que um catálogo interno

| Sem catálogo interno | Com catálogo interno |
|:---|:---|
| Cada auditoria pede evidências no formato de sua referência | Uma evidência por controle, mapeada a várias referências |
| Controles descritos em linguagem genérica de framework | Controles descritos na linguagem e na tecnologia da organização |
| Projetos reinventam controles | Projetos reutilizam building blocks com controles já avaliados |
| Mudança de framework exige refazer o programa | Mudança de framework exige atualizar mapeamentos |

O catálogo interno é o equivalente, no domínio de controles, do que a arquitetura de referência é no domínio de soluções (Módulo 2 — Aula 05): uma decisão tomada uma vez, reutilizada muitas vezes.

### A cadeia de rastreabilidade

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m03-l07-risk-to-architecture.mmd"
```

<figcaption>Figura 1 — Do cenário de risco à evidência e ao indicador, com frameworks externos como mapeamentos.</figcaption>
</figure>

Essa cadeia é a mesma ideia de rastreabilidade do SABSA (Módulo 2 — Aulas 06 e 07): requisitos de negócio levam a atributos e objetivos, que levam a mecanismos, que levam a componentes — e cada nível pode ser justificado pelo anterior. O catálogo materializa a cadeia nas operações do dia a dia.

## Fundamentos técnicos

### Anatomia de um controle no catálogo

| Campo | Exemplo — CTL-IAM-03 | Observação |
|:---|:---|:---|
| **Objetivo** | Acesso remoto e administrativo exige autenticação resistente a phishing | Resultado, não ferramenta |
| **Escopo** | Todas as contas com acesso remoto ou privilegiado | Explícito |
| **Implementação de referência** | IdP corporativo com FIDO2; gateway de acesso que exige o IdP | Building blocks da arquitetura |
| **Parâmetros** | Sem métodos de fallback por SMS; reautenticação a cada 12 h | Verificáveis |
| **Tipo e função** | Técnico, preventivo | Ajuda a combinar funções |
| **Dono** | Gerente de identidade | Responde pela eficácia |
| **Evidência** | Relatório semanal de métodos de autenticação por conta; política exportada do IdP | Preferencialmente automática |
| **Indicador** | % de contas do escopo com FIDO2; tentativas bloqueadas por método fraco | Liga a Aula 08 |
| **Cenários de risco** | RSK-007, RSK-015 | Rastreabilidade ao register |
| **Mapeamentos** | CSF 2.0 PR.AA; SP 800-53 IA-2; ISO/IEC 27001 Anexo A (controle correspondente); PCI DSS req. 8 | Referências, não a definição |
| **Exceções vigentes** | EXC-022 — sistema de etiquetas, até 2027-03 | Visíveis no mesmo lugar |

Mapear a referências externas é útil, e o NIST oferece mapeamentos oficiais do CSF 2.0 para outras referências — mas o próprio NIST alerta que mapeamentos de terceiros não têm a correção testada por ele. O controle é definido pelo **objetivo interno**; o mapeamento é uma conveniência para auditoria.

### Objetivos de controle versus controles

Um **objetivo de controle** diz o que precisa ser verdade ("somente pessoas autorizadas administram a produção"); um **controle** diz o mecanismo que torna isso verdade em um contexto. Um objetivo pode ter vários controles (preventivo, detectivo, corretivo), e um controle pode servir a vários objetivos. Separar os dois permite trocar a tecnologia sem reescrever o catálogo.

### Controles como código

A SP 800-53 Release 5.2.0 é distribuída também em **OSCAL** — formato legível por máquina (JSON, XML e YAML). Seguir a mesma ideia no catálogo interno permite:

- Validar automaticamente se todo controle tem dono, evidência e mapeamento.
- Gerar a Declaração de Aplicabilidade ou o conjunto de controles de um sistema a partir do catálogo.
- Ligar controles a **políticas como código** (guardrails de cloud, regras de pipeline) cuja execução já é a evidência.

### O catálogo na revisão de arquitetura

Em uma revisão (Módulo 4 — Aula 07), o catálogo transforma perguntas abertas em perguntas objetivas:

1. Que cenários de risco esta solução cria ou altera?
2. Que objetivos de controle esses cenários exigem?
3. A solução usa os building blocks de referência que implementam esses controles? Se não, qual a alternativa e qual a evidência?
4. Há exceções necessárias? Com que compensações, dono e prazo?

### Ciclo de vida

| Evento | Quem decide | O que registrar |
|:---|:---|:---|
| **Criação** de controle | Comitê de arquitetura e dono do risco | Cenário que justifica, dono, evidência |
| **Mudança** de implementação | Dono do controle, com revisão de arquitetura | Equivalência de resultado; atualização de building blocks |
| **Exceção** | Dono do risco | Compensações, residual, prazo (Módulo 2 — Aula 04) |
| **Aposentadoria** | Comitê, com dono do risco | Cenário que deixou de existir ou controle substituto |

## Exemplo empresarial

!!! example "Aurora Pagamentos — catálogo como fonte única"

    A Aurora consolidou 412 requisitos de três referências em um catálogo de **86 controles internos**, agrupados em 12 domínios. Cada controle foi descrito com a tecnologia real da empresa e apontado para um building block da arquitetura de referência.

    Efeitos medidos no primeiro ano:

    - A preparação das auditorias PCI DSS e ISO/IEC 27001 passou a usar o mesmo pacote de evidências, gerado em grande parte automaticamente.
    - Novos projetos que adotavam a landing zone e o IdP de referência herdavam 31 controles sem esforço adicional.
    - O register passou a mostrar, para cada cenário, o estado dos controles relacionados — e dois cenários "mitigados" voltaram a "em tratamento" quando os indicadores revelaram baixa cobertura.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Fonte dos controles | Texto do framework | Catálogo interno, mapeado aos frameworks |
| Ligação com risco | Inexistente | Cada controle ligado a cenários do register |
| Ligação com arquitetura | Inexistente | Cada controle implementado por building blocks |
| Evidência | Manual, por auditoria | Automática quando possível, uma por controle |
| Formato | Documentos | Dados estruturados, versionados e validados |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, muitos controles podem ser implementados e evidenciados como **guardrails** (políticas que impedem configurações proibidas) e **detecções de postura**; o catálogo aponta para essas políticas. Em on-premises, a evidência tende a ser mais manual — e o catálogo ajuda a priorizar onde automatizar. Em ambientes híbridos, o mesmo objetivo de controle pode ter implementações diferentes em cada ambiente; o catálogo deve registrá-las lado a lado, com a mesma evidência de resultado.

## Como especificar e implementar

- "A organização mantém um catálogo interno de controles versionado, com objetivo, escopo, implementação de referência, parâmetros, dono, evidência, indicador, cenários de risco e mapeamentos."
- "Todo controle está ligado a pelo menos um cenário de risco; controles sem cenário são revisados para aposentadoria."
- "Arquiteturas de referência indicam quais controles cada building block implementa."
- "Mudanças de implementação de controle passam por revisão de arquitetura."

## Trade-offs, limitações e antipadrões

- **Trade-off:** granularidade. Controles muito amplos não são verificáveis; muito específicos se multiplicam e envelhecem.
- **Antipadrão — catálogo como cópia do framework:** troca o nome dos controles e mantém a linguagem genérica.
- **Antipadrão — mapeamento como verdade:** declarar conformidade com uma referência apenas porque existe um mapeamento.
- **Limitação:** o catálogo descreve controles conhecidos; ameaças novas exigem threat modeling e revisão dos cenários.

## Como validar

- Executar uma validação automática: controles sem dono, sem evidência ou sem cenário.
- Escolher um cenário crítico e percorrer a cadeia até os indicadores.
- Comparar a evidência de um controle com a configuração real em produção.
- Verificar se os building blocks de referência ainda implementam os controles que declaram.

## Como apresentar e justificar

- **Para auditores:** "Este é o controle interno, sua evidência e seus mapeamentos para PCI DSS e ISO/IEC 27001. A mesma evidência atende às duas."
- **Para a diretoria:** "Cada real investido em controles está ligado a um cenário de risco do register. Os indicadores mostram se o investimento está funcionando."
- **Para engenharia:** "Usem os building blocks de referência e herdem os controles. Saindo deles, a revisão vai pedir a evidência equivalente."

## Checklist de revisão arquitetural

- [ ] Cada controle tem objetivo, dono, evidência e indicador.
- [ ] Cada controle está ligado a cenários de risco.
- [ ] Building blocks de referência declaram os controles que implementam.
- [ ] Mapeamentos externos são referências, não a definição do controle.
- [ ] Exceções aparecem junto ao controle, com prazo.
- [ ] O catálogo é versionado e validado automaticamente.

## Questões de compreensão

**1.** Qual a diferença entre objetivo de controle e controle?

??? success "Resposta comentada"

    O objetivo descreve o resultado que precisa ser verdadeiro; o controle é o mecanismo que o torna verdadeiro em um contexto. Separá-los permite trocar a tecnologia sem alterar o objetivo e combinar controles preventivos, detectivos e corretivos para o mesmo objetivo.

**2.** Por que não definir os controles diretamente com o texto de um framework?

??? success "Resposta comentada"

    Porque o texto do framework é genérico, não descreve a tecnologia e os donos da organização e muda com as versões do framework. O catálogo interno descreve o controle real; o framework entra como mapeamento.

**3.** Como o catálogo ajuda a revisão de arquitetura?

??? success "Resposta comentada"

    Transforma perguntas abertas em verificáveis: que cenários a solução cria, que objetivos eles exigem, se a solução usa os building blocks que implementam os controles e, se não, qual a alternativa e a evidência equivalente.

## Exercício de tomada de decisão

!!! question "Cenário: dois controles de backup na Meridiana"

    A Meridiana descobriu que tem dois controles de backup no rascunho do catálogo: um escrito pela equipe de infraestrutura ("backup diário de todos os servidores") e outro pela auditoria ("cópias de segurança devem ser testadas"). O cenário RSK-007 (ransomware) exige recuperação da expedição em até 8 horas, com RPO de 1 hora. O comitê de arquitetura discute três formas de registrar o tema no catálogo:

    - **A** — manter os dois controles e apenas melhorar a redação;
    - **B** — fundir os dois em um único controle amplo de "backup e restauração";
    - **C** — escrever um objetivo de controle e controles separados por função (preventivo, detectivo, corretivo), cada um com evidência e indicador.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho) e escreva a opção escolhida como objetivo de controle e controles, com evidência e indicador.

??? success "Resolução de referência"

    | Critério | Peso | A — Dois controles reescritos | B — Um controle amplo | C — Objetivo + três controles |
    |:---|:---|:---|:---|:---|
    | Verificabilidade de cada controle | 3 | 1 | 2 | 3 |
    | Cobertura do cenário RSK-007, inclusive com o domínio comprometido | 3 | 1 | 2 | 3 |
    | Clareza de dono e de evidência | 2 | 2 | 1 | 3 |
    | Esforço de manutenção do catálogo (3 = menor) | 1 | 3 | 3 | 2 |
    | **Total ponderado** | | **13** | **17** | **26** |

    **Pesos:** verificabilidade e cobertura do cenário recebem 3 porque um controle de backup que não prova recuperação dentro do RTO e do RPO não reduz o RSK-007; dono e evidência recebem 2; o esforço de manter mais itens no catálogo recebe 1. **Recomendação: C**, detalhada abaixo. **O que mudaria a decisão:** em um catálogo ainda inicial, sem donos definidos, B pode ser um primeiro passo — desde que o controle amplo tenha indicador de restauração medida e seja desdobrado quando os donos existirem.

    - **Objetivo de controle OBJ-BKP-01:** dados e configurações dos processos críticos são recuperáveis a partir de um ponto íntegro, dentro do RPO e do RTO aprovados, mesmo com o domínio comprometido.
    - **CTL-BKP-01 (preventivo):** cópias horárias dos sistemas da expedição em repositório imutável, administrado por identidade separada do domínio corporativo. *Evidência:* configuração de imutabilidade e relatório de jobs. *Indicador:* % de sistemas críticos com cópia imutável dentro do RPO.
    - **CTL-BKP-02 (detectivo):** alerta de falha de job e de alteração da política de retenção. *Evidência:* registros de alerta. *Indicador:* tempo para tratar falhas de backup.
    - **CTL-BKP-03 (corretivo e de validação):** restauração completa da expedição em ambiente isolado a cada semestre. *Evidência:* relatório com tempos medidos. *Indicador:* RTO medido versus RTO aprovado.
    - **Mapeamentos:** CSF 2.0 (PR.DS e RC.RP), SP 800-53 (CP-9 e CP-4) e o controle correspondente do Anexo A da ISO/IEC 27001.
    - Os dois rascunhos originais são aposentados e substituídos por esses três, todos ligados ao RSK-007.
    - **Risco residual:** comprometimento simultâneo da identidade separada que administra o repositório imutável; tratado com acesso de emergência sob dupla custódia (Módulo 4 — Aula 05).

## Pontos-chave

- Um catálogo interno, mapeado a frameworks, evita programas e evidências duplicados.
- A cadeia risco → objetivo → controle → building block → evidência → indicador é a espinha da arquitetura baseada em risco.
- Objetivos descrevem resultados; controles descrevem mecanismos.
- Catálogos estruturados e versionados permitem validação e evidência automáticas.
- Mapeamentos são conveniência para auditoria, não definição de controle.

## Referências

### Fundamentação principal

- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — catálogo e distribuição em OSCAL. <https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final>. *(Página oficial conferida.)*
- NIST. *CSF 2.0 Informative References*. <https://www.nist.gov/cyberframework/informative-references> — mapeamentos e alerta sobre mapeamentos de terceiros.
- NIST. *SP 800-37 Rev. 2* — controles comuns e herança (P-5).
- The SABSA Institute. *SABSA White Paper* (W100), 2009. <https://sabsa.org/white-paper-requests/> — rastreabilidade entre camadas e matriz de arquitetura.

### Leitura complementar

- CIS. *CIS Controls v8.1* — safeguards técnicos priorizados, úteis como base de controles de higiene.
- ISO/IEC 27002:2022 — atributos de controle como forma de organizar o catálogo.
- The Open Group. *Integrating Risk and Security within a TOGAF Enterprise Architecture*.

### Aplicação prática

- Escreva três controles do seu ambiente no formato desta aula, com objetivo, building block, evidência, indicador, cenário de risco e dois mapeamentos externos.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
