---
id: M03-L01
title: "Aula 01 — Governança de segurança e o NIST CSF 2.0"
public_title: "Módulo 3 — Aula 01 — Governança de segurança e o NIST CSF 2.0"
description: O que é governança de segurança, como ela se distingue da gestão e da operação, e como usar a estrutura do NIST Cybersecurity Framework 2.0 — Functions, Categories, Profiles e Tiers — para descrever onde a organização está e aonde precisa chegar.
domain: grc
tier: fundamental
status: published
prerequisites: [M02-L01, M01-L06]
objectives:
  - Diferenciar governança, gestão e operação de segurança e identificar quem decide o quê em cada nível.
  - Descrever as seis Functions do NIST CSF 2.0 e as categorias da função GOVERN.
  - Construir um perfil atual e um perfil-alvo e transformar a diferença em plano de ação.
  - Explicar o papel dos Tiers e por que o CSF não prescreve como alcançar os resultados.
minutes: 75
sources: [NIST-CSF-2, NIST-CSF-FAQ, NIST-CSF-INFORMATIVE-REFS]
further_reading: [NIST-SP800-37-R2, CIS-CONTROLS-V8-1, ISO-27001-2022, TOG-RISK-SECURITY]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M03
---

# Aula 01 — Governança de segurança e o NIST CSF 2.0 { #governanca-de-seguranca-e-o-nist-csf-20 }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 3 · Nível 1</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">75 min · ID técnico: M03-L01</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Arquiteturas de segurança não nascem de preferências técnicas: elas respondem a decisões de governança sobre quanto risco a organização aceita, quem responde por ele e quais resultados são prioritários. Esta aula define governança de segurança, separa-a da gestão e da operação, e apresenta o NIST Cybersecurity Framework (CSF) 2.0 como linguagem comum para descrever resultados — com a função GOVERN no centro, perfis para comparar o estado atual com o desejado e Tiers para caracterizar o rigor das práticas.

**Pré-requisitos:** [Papel do arquiteto de segurança](../02-security-architecture/01-security-architect-role.md) e [Ameaça, vulnerabilidade, risco e controle](../01-security-fundamentals/06-threat-vulnerability-risk.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Diferenciar governança, gestão e operação de segurança e identificar quem decide o quê em cada nível.
- Descrever as seis Functions do NIST CSF 2.0 e as categorias da função GOVERN.
- Construir um perfil atual e um perfil-alvo e transformar a diferença em plano de ação.
- Explicar o papel dos Tiers e por que o CSF não prescreve como alcançar os resultados.

## Conceito

### Governança, gestão e operação

| Nível | Pergunta que responde | Quem decide | Exemplos de decisão |
|:---|:---|:---|:---|
| **Governança** | O quê, por quê e quanto risco? | Conselho, diretoria, comitê de riscos | Apetite a risco, prioridades, orçamento, quem é dono de cada risco |
| **Gestão** | Como, com que recursos e em que prazo? | CISO, gestores de área, comitê de arquitetura | Programa de segurança, políticas, padrões, roadmap |
| **Operação** | Está funcionando hoje? | Equipes de TI, SOC, engenharia | Configurações, monitoração, resposta, correções |

Governança de segurança é o conjunto de mecanismos pelo qual a organização **define direção, atribui responsabilidade e supervisiona resultados** de segurança. Ela não escolhe firewall; ela decide, por exemplo, que nenhum processo crítico pode ficar parado mais de 24 horas e que o diretor de operações é dono desse risco.

O arquiteto de segurança trabalha na fronteira entre governança e gestão: traduz decisões de governança em princípios, padrões e arquiteturas de referência (Módulo 2 — Aulas 04 e 05), e devolve à governança riscos residuais e decisões que só ela pode tomar.

### Por que um framework de resultados

Sem uma linguagem comum, cada área descreve segurança à sua maneira: a auditoria fala em controles, a infraestrutura em ferramentas, a diretoria em incidentes. O **NIST CSF 2.0**, publicado em 26/02/2024, oferece uma taxonomia de **resultados** de cibersegurança que todos podem usar. O próprio documento declara que descreve resultados e **não prescreve como alcançá-los** (CSWP 29, Sec. 1, p. 1) — o "como" vem de catálogos como SP 800-53 e CIS Controls (Aula 03) e das decisões de arquitetura.

!!! info "Framework não é obrigação legal"

    O CSF é voluntário para organizações fora do governo federal dos Estados Unidos. No Brasil, ele é adotado por escolha, por exigência de clientes ou como referência de setores regulados — nunca deve ser apresentado como lei. Obrigações legais, como a LGPD, são tratadas na [Aula 04](04-iso-lgpd-pci.md).

## Fundamentos técnicos

### As seis Functions

O CSF Core organiza resultados em seis **Functions**, subdivididas em **Categories** e **Subcategories** (Sec. 2, pp. 3–4):

| Function | Resultado em uma frase |
|:---|:---|
| **GOVERN (GV)** | A estratégia, as expectativas e a política de gestão de riscos de cibersegurança estão estabelecidas, comunicadas e monitoradas |
| **IDENTIFY (ID)** | Os riscos atuais de cibersegurança são compreendidos |
| **PROTECT (PR)** | Salvaguardas para gerenciar esses riscos estão em uso |
| **DETECT (DE)** | Possíveis ataques e comprometimentos são encontrados e analisados |
| **RESPOND (RS)** | Ações são tomadas diante de um incidente detectado |
| **RECOVER (RC)** | Ativos e operações afetados por um incidente são restaurados |

A novidade estrutural da versão 2.0 é a função **GOVERN**, que orienta as demais. Suas categorias (Apêndice A, pp. 16–18) mostram o que a governança precisa produzir:

| Categoria | Foco |
|:---|:---|
| **GV.OC** — Organizational Context | Missão, partes interessadas, requisitos legais e contratuais, dependências |
| **GV.RM** — Risk Management Strategy | Prioridades, apetite e tolerância a risco, premissas |
| **GV.RR** — Roles, Responsibilities, and Authorities | Quem responde por quê, inclusive a liderança |
| **GV.PO** — Policy | Política de cibersegurança estabelecida, comunicada e aplicada |
| **GV.OV** — Oversight | Resultados da gestão de riscos usados para ajustar a estratégia |
| **GV.SC** — Cybersecurity Supply Chain Risk Management | Riscos de fornecedores e da cadeia de suprimentos |

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m03-l01-csf-profiles.mmd"
```

<figcaption>Figura 1 — GOVERN orienta as demais funções; perfis atual e alvo usam o vocabulário do Core; Tiers orientam a escolha do alvo.</figcaption>
</figure>

### Organizational Profiles

Um **Organizational Profile** descreve a postura da organização em termos dos resultados do Core. A Sec. 3.1 (pp. 6–7) descreve dois tipos — **Current Profile** (resultados alcançados hoje) e **Target Profile** (resultados desejados e prioridades) — e um ciclo de cinco etapas: definir o escopo do perfil, reunir as informações necessárias, criar o perfil, analisar lacunas e criar um plano de ação, e implementar o plano e atualizar o perfil.

O perfil é útil porque obriga a três decisões que costumam ficar implícitas:

1. **Escopo** — a organização inteira, uma unidade de negócio, um ambiente cloud?
2. **Prioridade** — nem todo resultado tem a mesma importância; o perfil-alvo diz quais importam primeiro.
3. **Evidência** — o que comprova que um resultado foi alcançado?

### Tiers

Os **Tiers** caracterizam o rigor das práticas de governança e gestão de riscos de cibersegurança em quatro níveis: **Partial (1)**, **Risk Informed (2)**, **Repeatable (3)** e **Adaptive (4)** (Sec. 3.2 e Apêndice B). Eles ajudam a escolher um perfil-alvo coerente com o contexto. Na prática de arquitetura, convém tratá-los como **caracterização**, não como meta automática: subir de Tier tem custo e só se justifica se reduzir risco relevante.

### Informative References e mapeamentos

O NIST mantém **Informative References** que mapeiam o CSF a outros documentos — SP 800-53, CIS Controls, ISO/IEC 27001:2022, entre outros — disponíveis para download em planilha e com traduções, inclusive para o português. Os mapeamentos ajudam a reaproveitar evidências, mas o próprio NIST alerta que mapeamentos de terceiros não têm a correção testada por ele.

## Exemplo empresarial

!!! example "Aurora Pagamentos — o primeiro perfil-alvo"

    A Aurora Pagamentos tinha dezenas de iniciativas de segurança simultâneas e nenhuma forma de dizer à diretoria se estava "melhor". O arquiteto de segurança e o CISO conduziram um perfil CSF com escopo no **ambiente de processamento de transações**:

    | Categoria (amostra) | Perfil atual | Perfil-alvo (12 meses) | Prioridade |
    |:---|:---|:---|:---|
    | GV.RM — estratégia de risco | Apetite não formalizado | Apetite e tolerância aprovados pela diretoria | Alta |
    | GV.SC — cadeia de suprimentos | Fornecedores avaliados só na contratação | Fornecedores críticos reavaliados anualmente | Alta |
    | PR.AA — identidade e acesso | MFA em 60% das contas privilegiadas | MFA resistente a phishing em 100% delas | Alta |
    | DE.CM — monitoração contínua | Logs de 40% dos sistemas no SIEM | Todos os sistemas do escopo | Média |
    | RC.RP — recuperação | Restauração nunca testada | Teste semestral com resultado registrado | Alta |

    A análise de lacunas virou um plano de 14 ações com dono, custo e prazo. A diretoria passou a acompanhar **cinco resultados**, e não 60 projetos.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Ponto de partida | Lista de ferramentas a comprar | Resultados desejados e prioridades de negócio |
| Responsabilidade | "Segurança é da TI" | Donos de risco no negócio; TI implementa |
| Uso do framework | Checklist de conformidade | Linguagem para perfil atual, alvo e plano |
| Tiers | Meta de "chegar ao 4" | Nível escolhido conforme o risco e o custo |
| Relato | Projetos e ferramentas | Resultados, lacunas e decisões pedidas |

## Aplicabilidade: on-premises, cloud e híbrido

O CSF é agnóstico a tecnologia: um perfil pode ter escopo em um datacenter, em uma conta cloud ou em um processo de negócio que atravessa ambos. Em cloud, o perfil precisa registrar o que é resultado do provedor e o que é da organização (responsabilidade compartilhada, Módulo Inicial — Aula 06); em ambientes híbridos, um mesmo resultado (por exemplo, "acessos são gerenciados") pode estar alcançado em um ambiente e não no outro — e o perfil deve mostrar essa diferença, não esconder com uma média.

## Como especificar e implementar

- "O programa de segurança mantém um perfil atual e um perfil-alvo no vocabulário do NIST CSF 2.0, com escopo declarado e revisão anual."
- "Cada lacuna priorizada tem ação, dono, custo estimado e prazo."
- "Os riscos de cibersegurança têm donos no negócio, definidos na governança (GV.RR)."
- "O apetite e a tolerância a risco são aprovados pela diretoria e usados nas decisões de arquitetura (GV.RM)."

## Trade-offs, limitações e antipadrões

- **Antipadrão — perfil sem escopo:** um perfil "da empresa toda" esconde que o ambiente crítico está pior que a média.
- **Antipadrão — CSF como checklist:** marcar subcategorias como "atendidas" sem evidência transforma a ferramenta em burocracia.
- **Antipadrão — mapeamento como prova:** dizer "atendemos à ISO porque cumprimos o CSF" com base em um mapeamento de terceiros sem análise.
- **Limitação:** o CSF não diz que controle implementar nem com que intensidade; essa decisão continua sendo de arquitetura e de risco.

## Como validar

- Escolher três subcategorias marcadas como alcançadas e pedir a evidência de cada uma.
- Verificar se o perfil-alvo tem prioridades e se elas batem com os riscos do register (Aula 06).
- Conferir se os donos de risco definidos em GV.RR conhecem e aceitam esse papel.

## Como apresentar e justificar

- **Para a diretoria:** "Hoje alcançamos 3 dos 5 resultados que definimos como prioritários. Os dois que faltam — recuperação testada e fornecedores críticos reavaliados — são os que mais reduzem o risco de parada."
- **Para a engenharia:** "O perfil-alvo diz o resultado; a arquitetura de referência diz como chegamos lá. Vocês participam da escolha do como."

## Checklist de revisão arquitetural

- [ ] O perfil tem escopo declarado.
- [ ] Perfil atual e perfil-alvo usam o mesmo vocabulário e o mesmo escopo.
- [ ] Cada resultado declarado como alcançado tem evidência.
- [ ] Lacunas viraram ações com dono, custo e prazo.
- [ ] Apetite, tolerância e donos de risco estão definidos pela governança.
- [ ] O framework é apresentado como referência voluntária, não como obrigação legal.

## Questões de compreensão

**1.** Qual a diferença entre uma decisão de governança e uma decisão de gestão?

??? success "Resposta comentada"

    Governança define direção, apetite a risco, prioridades e responsabilidades ("nenhum processo crítico parado mais de 24 h; o diretor de operações é dono desse risco"). Gestão define como alcançar isso com recursos e prazos (programa, políticas, padrões, roadmap).

**2.** Por que o CSF 2.0 não diz qual ferramenta ou controle implementar?

??? success "Resposta comentada"

    Porque é um framework de resultados, aplicável a organizações de qualquer porte e setor. O documento declara que não prescreve como alcançar os resultados; o "como" vem de catálogos de controles, arquiteturas de referência e decisões de risco de cada organização.

**3.** Uma empresa quer "chegar ao Tier 4 em todas as áreas". O que você responderia?

??? success "Resposta comentada"

    Que Tiers caracterizam o rigor das práticas e devem ser escolhidos conforme o risco e o custo. Tier 4 em áreas de baixo risco consome recursos que fariam mais diferença em lacunas críticas. O alvo deve vir do perfil-alvo e das prioridades de negócio.

## Exercício de tomada de decisão

!!! question "Cenário: escopo do primeiro perfil da Meridiana"

    A Meridiana Distribuidora quer usar o CSF 2.0 pela primeira vez. O motivo é o risco de ransomware parar os centros de distribuição (Caso A). A equipe de segurança tem três pessoas e a diretoria quer o primeiro resultado em até dois meses. Há três propostas de escopo para o primeiro perfil:

    - **A** — perfil único para a empresa inteira (sugestão da diretoria);
    - **B** — operação logística dos três centros de distribuição (proposta do arquiteto);
    - **C** — piloto em um único centro de distribuição.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende um escopo e indique três categorias que você priorizaria no perfil-alvo.

??? success "Resolução de referência"

    | Critério | Peso | A — Empresa inteira | B — Operação logística | C — Piloto em um CD |
    |:---|:---|:---|:---|:---|
    | Ligação com o risco que motivou a iniciativa | 3 | 2 | 3 | 2 |
    | Viabilidade de reunir evidências em dois meses | 3 | 1 | 2 | 3 |
    | Visão que a diretoria recebe | 2 | 3 | 2 | 1 |
    | Reaproveitamento do método nos demais escopos | 1 | 2 | 3 | 2 |
    | **Total ponderado** | | **17** | **22** | **19** |

    - **Pesos:** o risco que motivou a iniciativa e a capacidade de produzir evidências com três pessoas definem se o perfil será útil, por isso pesam 3. A visão corporativa importa para a diretoria, mas pode vir em uma segunda rodada (peso 2). O reaproveitamento é desejável, sem ser decisivo (peso 1).
    - **Recomendação: B.** É onde está o risco que motivou a iniciativa (ransomware parando os CDs), o escopo é delimitado o suficiente para coletar evidências em semanas e o resultado é comunicável. Um perfil corporativo pode vir depois, reaproveitando o método.
    - **Categorias prioritárias (exemplo justificável):** GV.RM (apetite e tolerância a parada dos CDs), PR.AA (identidade e acesso, dada a VPN sem MFA) e RC.RP (recuperação testada, dado o backup no domínio). Outras escolhas são válidas se ligadas a riscos explícitos.
    - **Trade-off aceito e risco residual:** a diretoria não terá, de início, uma visão da empresa inteira — em troca de um perfil com evidências e ações acionáveis. Riscos fora da logística (por exemplo, fraude no cadastro de fornecedores) ficam sem perfil até a segunda rodada e continuam no register.
    - **O que mudaria a decisão:** uma exigência de seguradora ou de cliente por uma visão corporativa em data fixa aumentaria o peso da visão da diretoria e favoreceria A; se os três CDs operassem com sistemas e equipes muito diferentes, C seria um começo mais seguro.

    A matriz organiza a comparação e torna os pesos discutíveis, mas não substitui o julgamento: um critério que a governança considere inegociável — por exemplo, uma obrigação legal — elimina uma opção antes de qualquer soma.

## Pontos-chave

- Governança decide direção, apetite e responsáveis; gestão decide como; operação executa.
- O CSF 2.0 descreve resultados em seis Functions, com GOVERN orientando as demais.
- Perfis atual e alvo, com escopo declarado, transformam o framework em plano de ação.
- Tiers caracterizam o rigor das práticas; não são meta automática.
- O CSF é voluntário: mapeamentos ajudam a reaproveitar evidências, mas não substituem análise.

## Referências

### Fundamentação principal

- NIST. *The NIST Cybersecurity Framework (CSF) 2.0*. CSWP 29, 26/02/2024. <https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final> — Sec. 1 (p. 1), Sec. 2 (pp. 3–4), Sec. 3.1–3.2 (pp. 6–8), Apêndice A — GOVERN (pp. 16–18) e Apêndice B (pp. 24–26). *(Lido.)*
- NIST. *CSF 2.0 — Frequently Asked Questions*. <https://www.nist.gov/cyberframework/faqs> — Functions e Tiers.
- NIST. *CSF 2.0 Informative References*. <https://www.nist.gov/cyberframework/informative-references> — mapeamentos e traduções.

### Leitura complementar

- NIST. *SP 800-37 Rev. 2 — Risk Management Framework*. 2018 — como o CSF se conecta ao ciclo de vida de sistemas ([Aula 02](02-nist-rmf.md)).
- CIS. *CIS Controls v8.1* — catálogo priorizado de salvaguardas, realinhado ao CSF 2.0 ([Aula 03](03-control-selection-tailoring.md)).
- ISO/IEC 27001:2022 — sistema de gestão de segurança da informação ([Aula 04](04-iso-lgpd-pci.md)).
- The Open Group. *Integrating Risk and Security within a TOGAF Enterprise Architecture* — ligação entre governança de riscos e arquitetura corporativa.

### Aplicação prática

- Escolha um escopo pequeno na sua organização e preencha um perfil atual e um perfil-alvo para cinco categorias, com evidência e prioridade para cada uma.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
