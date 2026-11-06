---
id: M07-L02
title: "Aula 02 — Componentes lógicos: Policy Engine, Policy Administrator e PEP"
public_title: "Módulo 7 — Aula 02 — Componentes lógicos: Policy Engine, Policy Administrator e PEP"
description: Os componentes lógicos de uma arquitetura Zero Trust segundo a NIST SP 800-207 — motor de política, administrador de política, ponto de aplicação de política e fontes de dados —, a separação entre plano de controle e plano de dados, e como mapear produtos reais a esses papéis sem perder de vista disponibilidade e integridade da decisão.
domain: zero-trust
tier: professional
status: published
prerequisites: [M07-L01, M06-L02]
objectives:
  - Descrever as funções do Policy Engine, do Policy Administrator e do Policy Enforcement Point.
  - Identificar as fontes de dados que alimentam a decisão e sua criticidade.
  - Mapear componentes de produtos reais aos papéis lógicos.
  - Especificar requisitos de disponibilidade, integridade e registro para os componentes de decisão.
minutes: 60
sources: [NIST-SP800-207, NIST-SP800-162, NIST-SP800-215, NIST-SP800-53]
further_reading: [NIST-SP1800-35, MS-ENTERPRISE-ACCESS-MODEL]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M07
---

# Aula 02 — Componentes lógicos: Policy Engine, Policy Administrator e PEP { #componentes-logicos-policy-engine-policy-administrator-e-pep }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 7 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M07-L02</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Toda arquitetura Zero Trust, qualquer que seja o produto, precisa responder às mesmas perguntas: **quem decide**, **quem executa a decisão**, **com que informação** e **por qual caminho**. A NIST SP 800-207 dá nome a esses papéis — Policy Engine, Policy Administrator e Policy Enforcement Point — e às fontes de dados que os alimentam. Esta aula usa esse vocabulário para ler propostas de mercado e para especificar requisitos que um diagrama de produto costuma omitir.

**Pré-requisitos:** [Fundamentos de Zero Trust](01-zero-trust-fundamentals.md) e [Modelos de autorização](../06-iam/02-authorization-models.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Descrever as funções do Policy Engine, do Policy Administrator e do Policy Enforcement Point.
- Identificar as fontes de dados que alimentam a decisão e sua criticidade.
- Mapear componentes de produtos reais aos papéis lógicos.
- Especificar requisitos de disponibilidade, integridade e registro para os componentes de decisão.

## Conceito

### Os três componentes centrais

A SP 800-207 descreve (§3, pp. 9–10):

| Componente | Função | Analogia com ABAC (Módulo 6 — Aula 02) |
|:---|:---|:---|
| **Policy Engine (PE)** | Toma a decisão de conceder acesso a um recurso, usando a política e um **algoritmo de confiança**, e registra a decisão | PDP |
| **Policy Administrator (PA)** | Estabelece ou encerra o caminho de comunicação entre sujeito e recurso, emitindo credenciais de sessão conforme a decisão do PE | Parte do PDP que comanda a execução |
| **Policy Enforcement Point (PEP)** | Habilita, monitora e encerra conexões entre sujeito e recurso; pode ser um componente único ou dividido em lado do cliente e lado do recurso | PEP |

O documento divide o **ponto de decisão de política (PDP)** em dois componentes lógicos: o PE e o PA (§3, p. 9). Entre os requisitos de rede para suportar a arquitetura (§3.4.1, pp. 21–22), estão que os recursos **não devem ser alcançáveis sem passar por um PEP** (item 4) e que **plano de dados e plano de controle sejam logicamente separados** (item 5).

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m07-l02-components.mmd"
```

<figcaption>Figura 1 — PE e PA no plano de controle; PEP e recurso no plano de dados; fontes de dados alimentam a decisão.</figcaption>
</figure>

### Fontes de dados

A decisão do PE usa fontes como (§3, pp. 10–11): **diagnóstico e mitigação contínuos (CDM)** — estado dos ativos —, **conformidade setorial**, **inteligência de ameaças**, **logs de rede e de atividade**, **políticas de acesso a dados**, **PKI corporativa**, **gestão de identidades** e **SIEM**. Cada uma é uma dependência: se a fonte de postura de dispositivos estiver errada, o PE decide errado com perfeita consistência.

## Fundamentos técnicos

### Mapeando produtos aos papéis

| Situação real | PE / PA | PEP | Fontes |
|:---|:---|:---|:---|
| Acesso condicional do IdP para SaaS | Motor de políticas do IdP | O próprio IdP ao emitir (ou não) o token; a aplicação ao validar | Diretório, MDM/EDR, risco de sessão |
| ZTNA para aplicações internas (Módulo 5 — Aula 04) | Controlador do ZTNA | Gateway ou conector junto à aplicação | IdP, postura do dispositivo |
| Microsegmentação com identidade de workload (Módulo 5 — Aula 01) | Controlador de políticas | Agente no host, proxy ou sidecar | Inventário de workloads, identidades de serviço |
| Acesso privilegiado (Módulo 6 — Aula 06) | Motor de aprovação just-in-time | Proxy de sessão do PAM | IdP, aprovações, ITSM |

Na prática, uma organização tem **vários PDPs e PEPs**, de fornecedores diferentes. A arquitetura precisa garantir que as políticas sejam **coerentes** entre eles — por exemplo, que "dispositivo não conforme" signifique o mesmo para o IdP e para o ZTNA.

### Requisitos que os diagramas de produto omitem

| Requisito | Por quê | Referência |
|:---|:---|:---|
| **Alta disponibilidade e resiliência** do PE, PA e PEP | Ataques ou falhas nesses componentes interrompem a operação | §5.2 |
| **Controle de mudanças e auditoria** das políticas e da configuração do PE/PA | Um PE ou PA comprometido ou mal configurado concede acessos não aprovados | §5.1 |
| **Modo de falha** definido (fechar ou abrir) por recurso | Indisponibilidade do PDP não pode ser resolvida no improviso | Prática de arquitetura (Módulo 5 — Aula 05) |
| **Registro de decisões** com sujeito, recurso, sinais e resultado | Investigação e ajuste de políticas | §3; princípio 7 |
| **Proteção das contas que administram o PE/PA** | Fazem parte do plano de controle | Módulo 6 — Aula 06 |
| **Qualidade das fontes de dados** | Decisão correta depende de entrada correta | SP 800-162, Sec. 3 |

A SP 800-207 também lista como ameaça o uso de **entidades não humanas** na administração da ZTA (§5.7) — contas automatizadas que precisam dos mesmos controles das identidades privilegiadas.

### Onde ficam os PEPs

| Posição | Vantagem | Limitação |
|:---|:---|:---|
| **No dispositivo (agente)** | Visibilidade de postura; protege fora da rede corporativa | Exige dispositivos gerenciados |
| **Junto ao recurso (gateway, sidecar)** | Protege o recurso independentemente do cliente | Mais componentes a operar |
| **Na borda de serviço (proxy, portal)** | Sem software no cliente | Pouca visibilidade sobre o dispositivo |

A SP 800-215 descreve a mesma divisão para ZTNA: cliente ou navegador, controlador (PDP) e gateway (PEP) (Sec. 5, p. 17).

## Exemplo empresarial

!!! example "Aurora Pagamentos — três PDPs, uma política"

    A Aurora já tinha acesso condicional no IdP, um ZTNA e uma solução de acesso privilegiado — três PDPs com políticas escritas por equipes diferentes. Uma revisão encontrou incoerências: dispositivos sem EDR eram bloqueados no ZTNA, mas aceitos pelo IdP para SaaS; o PAM não consultava a postura do dispositivo.

    O arquiteto propôs um **catálogo de condições comuns** (dispositivo gerenciado, EDR ativo, sistema atualizado, local permitido, nível de risco) com uma única fonte para cada sinal, e exigiu que os três PDPs usassem as mesmas definições. Também registrou em ADR o modo de falha de cada PDP e criou um processo de mudança de políticas com revisão em pares e testes.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Decisão | Embutida em cada equipamento | PDPs identificados, com políticas coerentes |
| Acesso ao recurso | Pela rede | Somente por PEP |
| Planos | Controle e dados misturados | Separados |
| Mudanças de política | Ad hoc | Versionadas, revisadas, testadas e auditadas |
| Disponibilidade | Assumida | Projetada, com modo de falha decidido |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referências voluntárias que dão requisitos verificáveis aos componentes lógicos:

| Controle ou padrão | Objetivo para PE, PA e PEP | Referência |
|:---|:---|:---|
| Aplicação de acesso | O PEP aplica as autorizações aprovadas em todo acesso | SP 800-53: AC-3 (Access Enforcement) |
| Decisão antes da aplicação | A decisão do PDP é aplicada a cada pedido antes do acesso | SP 800-53: AC-24 (Access Control Decisions) |
| Controle de mudanças | Mudanças de política e de configuração do PDP revisadas, aprovadas e registradas | SP 800-53: CM-3 (Configuration Change Control) |
| Modo de falha | Falhar para um estado conhecido, preservando o que foi definido; procedimentos de falha segura | SP 800-53: SC-24 (Fail in Known State) e SI-17 (Fail-safe Procedures) |
| Registro de decisões | Gerar registros de decisão com sujeito, recurso, sinais e resultado | SP 800-53: AU-2 (Event Logging) e AU-12 (Audit Record Generation) |
| Administração do PDP | Contas privilegiadas restritas e monitoradas, inclusive as não humanas | SP 800-53: AC-6(5) (Privileged Accounts) e AC-2(7) (Privileged User Accounts) |
| Componentes lógicos e ameaças | PE, PA, PEP, fontes de dados, requisitos de rede e ameaças ao processo de decisão | NIST SP 800-207, §3, §3.4.1 e §5 |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, IdP e serviços nativos de acesso cumprem os papéis de PE/PA e PEP para consoles, APIs e aplicações. Em on-premises, o PEP costuma ser um gateway ou conector diante de aplicações que não falam protocolos modernos. Em ambientes híbridos, o PDP frequentemente está em nuvem e o PEP no datacenter — a conectividade entre eles torna-se dependência crítica, com modo de falha definido.

## Como especificar e implementar

- "Para cada recurso crítico, o PDP e o PEP estão identificados; o recurso só é alcançável pelo PEP."
- "Políticas usam um catálogo comum de condições, com fonte única para cada sinal."
- "Mudanças em políticas e na configuração de PDPs passam por revisão, teste e registro."
- "PDPs e PEPs têm alta disponibilidade e modo de falha documentado por recurso."
- "Decisões são registradas com sujeito, recurso, sinais e resultado e enviadas ao SIEM."

## Trade-offs, limitações e antipadrões

- **Trade-off:** vários PDPs especializados versus um PDP central — o primeiro é realista, o segundo é mais coerente; o catálogo de condições comuns reduz a distância.
- **Antipadrão — PEP contornável:** o recurso continua alcançável diretamente pela rede, "para emergências".
- **Antipadrão — política sem dono:** regras de acesso condicional criadas por diferentes administradores, sem revisão.
- **Limitação:** o modelo lógico não diz como implementar; implementações reais misturam papéis em um mesmo produto.

## Como validar

- Tentar alcançar o recurso sem passar pelo PEP.
- Comparar decisões dos diferentes PDPs para o mesmo dispositivo não conforme.
- Simular indisponibilidade do PDP e verificar o modo de falha.
- Revisar o histórico de mudanças de política.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhum recurso crítico alcançável sem o PEP | Teste de acesso direto pela rede, negado, para cada recurso do escopo |
| Mesma decisão de todos os PDPs para o mesmo dispositivo não conforme | Teste com dispositivo de referência não conforme contra IdP, ZTNA e PAM |
| Modo de falha documentado e exercitado por recurso | ADR por recurso e registro do teste de indisponibilidade do PDP |
| Toda mudança de política com revisão, teste e registro | Histórico do repositório de políticas no período |
| Decisões no SIEM com sujeito, recurso, sinais e resultado | Amostra de registros de decisão |

## Como apresentar e justificar

- **Para a diretoria:** "Temos três sistemas decidindo acesso com regras diferentes. Vamos alinhar as regras e garantir que nenhum deles possa ser contornado."
- **Para a operação:** "Política é código: muda por pull request, com teste."

## Checklist de revisão arquitetural

- [ ] PDP e PEP identificados por recurso crítico.
- [ ] Recursos alcançáveis apenas pelo PEP.
- [ ] Planos de controle e de dados separados.
- [ ] Catálogo comum de condições entre PDPs.
- [ ] Mudanças de política controladas e auditadas.
- [ ] Alta disponibilidade e modo de falha definidos.

## Questões de compreensão

**1.** Qual a diferença entre Policy Engine e Policy Administrator?

??? success "Resposta comentada"

    O PE decide se o acesso é concedido, usando política e algoritmo de confiança. O PA executa a decisão no plano de controle, estabelecendo ou encerrando o caminho de comunicação e emitindo credenciais de sessão para o PEP.

**2.** Por que a SP 800-207 recomenda que recursos não sejam alcançáveis sem passar por um PEP?

??? success "Resposta comentada"

    Porque, se o recurso puder ser alcançado diretamente, a decisão de política pode ser contornada, e a arquitetura volta a depender da rede.

**3.** Que ameaças aos componentes de decisão a SP 800-207 destaca?

??? success "Resposta comentada"

    A subversão do processo de decisão — PE ou PA comprometido ou mal configurado concedendo acessos não aprovados — e ataques de negação de serviço ou falhas de rede que interrompem PE, PA ou PEPs. Também destaca contas não humanas usadas na administração da ZTA.

## Exercício de tomada de decisão

!!! question "Cenário: modo de falha do PDP na Lumen"

    O acesso condicional do IdP da Lumen é o PDP para o portal de prontuários usado nas clínicas. Se o IdP ficar indisponível, as clínicas não acessam prontuários. As opções de modo de falha são:

    - **A** — fechar sempre: sem acesso enquanto o IdP estiver indisponível;
    - **B** — fechado fora das clínicas e contingência limitada nas clínicas, por modo de emergência do sistema de prontuários;
    - **C** — abrir pela rede: durante a indisponibilidade, o portal aceita qualquer acesso a partir da rede da clínica.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e proponha os controles associados.

**Objetivos avaliados:** Especificar requisitos de disponibilidade, integridade e registro para os componentes de decisão; identificar as fontes de dados que alimentam a decisão e sua criticidade.

**Entrega esperada:** Matriz ponderada, modo de falha recomendado por contexto e os controles da contingência.

**Critérios de avaliação:**

- O modo de falha é definido por recurso e por contexto, não de forma única para tudo.
- A contingência tem limite de escopo, autenticação, alerta e revisão posterior.
- A resiliência do próprio PDP (SLA, contas de emergência) é tratada.

??? success "Resolução de referência"

    | Critério | Peso | A — Fechar sempre | B — Contingência limitada nas clínicas | C — Abrir pela rede |
    |:---|:---|:---|:---|:---|
    | Continuidade do atendimento | 3 | 1 | 3 | 3 |
    | Proteção dos dados de saúde durante a falha | 3 | 3 | 2 | 1 |
    | Rastreabilidade dos acessos na contingência | 2 | 3 | 3 | 1 |
    | Simplicidade de implantação e de teste | 1 | 3 | 1 | 2 |
    | **Total ponderado** | | **21** | **22** | **16** |

    - **Pesos:** atendimento ao paciente e proteção de dados de saúde são os dois objetivos em conflito (peso 3 para ambos). A rastreabilidade pesa 2, porque é o que permite revisar o que aconteceu na contingência. A simplicidade pesa 1.
    - **Recomendação: B**, por pequena margem sobre A. A contingência limitada preserva o atendimento sem voltar à confiança pela rede da opção C, que é o antipadrão que a arquitetura quer eliminar.
    - **Modo de falha:** **fechado** para acesso a prontuários a partir de fora das clínicas; para as clínicas, **contingência limitada** — leitura dos prontuários de pacientes com consulta agendada no dia, a partir de dispositivos gerenciados da rede da clínica, por um modo de emergência do sistema de prontuários com autenticação local forte.
    - **Controles:** ativação do modo de emergência apenas pela coordenação clínica, com registro; alerta imediato ao SOC; revisão de todos os acessos ao fim da indisponibilidade; teste semestral.
    - **Resiliência do PDP:** IdP com SLA compatível e contas de emergência para administração (Módulo 6 — Aula 06).
    - **Registro:** ADR com a decisão e o risco residual aceito pela diretoria clínica.
    - **Trade-off aceito e risco residual:** o modo de emergência é um segundo caminho de acesso, com autenticação local que precisa ser mantida e testada; durante a contingência, um funcionário mal-intencionado pode ler prontuários dos pacientes do dia. O residual é tratado com a revisão de todos os acessos ao fim da indisponibilidade.
    - **O que mudaria a decisão:** a margem sobre A é pequena e depende do peso da continuidade. Se as clínicas tiverem procedimento clínico em papel aceito pela coordenação para indisponibilidades curtas, ou se o histórico de indisponibilidade do IdP for desprezível, A passa a ser preferível pela simplicidade; se o modo de emergência não puder limitar a leitura aos pacientes do dia, B perde a nota de proteção e A vence.

    **Erros comuns:**

    - Abrir pela rede durante a indisponibilidade, voltando à confiança implícita.
    - Fechar sempre sem avaliar o impacto clínico.
    - Criar o modo de emergência e não testá-lo.

## Pontos-chave

- PE decide, PA executa no plano de controle, PEP aplica no plano de dados.
- Recursos só devem ser alcançáveis pelo PEP; planos de controle e dados ficam separados.
- Fontes de dados são dependências críticas da decisão.
- Organizações reais têm vários PDPs; políticas coerentes exigem um catálogo comum de condições.
- Disponibilidade, modo de falha e controle de mudanças dos componentes de decisão são requisitos de arquitetura.

## Referências

### Fundamentação principal

- NIST. *SP 800-207 — Zero Trust Architecture*. 2020 — §3 (pp. 9–11), §3.4.1 (pp. 21–22) e §5 (pp. 28–30). *(Lido; componentes, fontes de dados e requisitos de rede reconferidos no PDF em 2026-10-29.)*
- NIST. *SP 800-162* — PDP, PEP, PIP e PAP. *(Lido.)*
- NIST. *SP 800-215* — Sec. 5 (p. 17). *(Lido; página reconferida em 2026-10-29.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-2(7), AC-3, AC-6(5), AC-24, AU-2, AU-12, CM-3, SC-24 e SI-17, conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- NIST. *SP 1800-35* — implementações de exemplo com produtos reais mapeados aos componentes.
- Microsoft. *The enterprise access model*.

### Aplicação prática

- Para três recursos críticos do seu ambiente, identifique o PDP, o PEP e as fontes de dados da decisão, e verifique se o recurso pode ser alcançado sem passar pelo PEP.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
