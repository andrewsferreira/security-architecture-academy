---
id: M06-L02
title: "Aula 02 — Modelos de autorização: RBAC, ABAC e acesso contextual"
public_title: "Módulo 6 — Aula 02 — Modelos de autorização: RBAC, ABAC e acesso contextual"
description: Como decidir quem pode fazer o quê — listas de controle, papéis, atributos e contexto —, os componentes de uma arquitetura de autorização (PDP, PEP, PIP, PAP), os limites de cada modelo e como combiná-los sem perder a capacidade de auditar.
domain: iam
tier: professional
status: published
prerequisites: [M06-L01, M01-L07]
objectives:
  - Comparar ACL, RBAC e ABAC e reconhecer a explosão de papéis.
  - Descrever os componentes PDP, PEP, PIP e PAP e onde ficam na arquitetura.
  - Projetar autorização híbrida — papéis para o acesso base, atributos e contexto para refinamento.
  - Avaliar a auditabilidade de cada modelo.
minutes: 75
sources: [NIST-SP800-162, NIST-SP800-207, MS-ENTERPRISE-ACCESS-MODEL, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [OWASP-ASVS-5, BOOK-ANDERSON-SE3]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M06
---

# Aula 02 — Modelos de autorização: RBAC, ABAC e acesso contextual { #modelos-de-autorizacao-rbac-abac-e-acesso-contextual }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 6 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M06-L02</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Autenticar diz **quem** é; autorizar decide **o que** essa identidade pode fazer, sobre **qual** recurso, **em que** circunstâncias. Escolher o modelo de autorização é uma decisão de arquitetura com efeitos de longo prazo: papéis demais tornam o sistema ingovernável; atributos sem governança tornam as decisões imprevisíveis. Esta aula compara os modelos, apresenta a arquitetura de decisão e mostra como combiná-los.

**Pré-requisitos:** [Disciplinas de identidade](01-identity-disciplines.md) e [Modelos formais](../01-security-fundamentals/07-formal-security-models.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Comparar ACL, RBAC e ABAC e reconhecer a explosão de papéis.
- Descrever os componentes PDP, PEP, PIP e PAP e onde ficam na arquitetura.
- Projetar autorização híbrida — papéis para o acesso base, atributos e contexto para refinamento.
- Avaliar a auditabilidade de cada modelo.

## Conceito

### Três modelos

A NIST SP 800-162 compara os modelos (Sec. 2, a partir da p. 4):

| Modelo | Decisão baseada em | Força | Limitação |
|:---|:---|:---|:---|
| **ACL / por identidade** | Lista de identidades por objeto | Simples, direta | Cada objeto tem sua lista; permissões obsoletas se acumulam |
| **RBAC** | Papéis atribuídos à identidade | Agrupa permissões por função; fácil de revisar | **Explosão de papéis** quando as regras dependem de contexto fino |
| **ABAC** | Atributos do sujeito, do objeto e condições de ambiente, avaliados por regras | Expressa regras complexas sem criar papéis | Mais difícil responder "quem pode acessar este objeto?" |

O documento observa que ACL e RBAC são, de certa forma, **casos especiais de ABAC** quanto aos atributos usados — a identidade e o papel são atributos.

### Explosão de papéis

Suponha uma regra: "analistas de crédito podem aprovar operações até R$ 50 mil da própria região, em horário comercial". Em RBAC puro, seriam necessários papéis por região e faixa de valor — e um novo papel a cada variação. Em ABAC, uma regra com atributos (função, região do sujeito, região do cliente, valor, horário) resolve.

### Acesso contextual

Acesso contextual acrescenta à decisão **condições de ambiente**: localização, dispositivo gerenciado e conforme, nível de risco da sessão, horário. É a forma de ABAC mais presente em IdPs modernos (políticas de acesso condicional) e um pilar do Zero Trust (Módulo 7 — Aula 04). A NIST SP 800-207 trata a decisão de acesso como avaliação de política com base em múltiplas fontes de dados — o mesmo padrão lógico.

## Fundamentos técnicos

### Arquitetura de decisão

A SP 800-162 descreve os pontos funcionais de um mecanismo de controle de acesso distribuído na empresa (Sec. 2.4.3, pp. 14–16; definições nas pp. 15–16):

| Componente | Papel | Exemplo |
|:---|:---|:---|
| **PEP** — Policy Enforcement Point | Intercepta o pedido e aplica a decisão | Gateway de API, middleware da aplicação, proxy |
| **PDP** — Policy Decision Point | Avalia as políticas e decide | Motor de políticas, serviço de autorização |
| **PIP** — Policy Information Point | Fornece atributos | Diretório, RH, inventário de dados, MDM |
| **PAP** — Policy Administration Point | Cria, testa e publica políticas | Repositório de políticas como código |

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m06-l02-abac.mmd"
```

<figcaption>Figura 1 — O PEP consulta o PDP, que avalia políticas do PAP com atributos do sujeito, do objeto e do ambiente fornecidos pelos PIPs.</figcaption>
</figure>

### Governança de atributos

ABAC é tão confiável quanto seus atributos. A SP 800-162 trata dessa governança em vários pontos:

- Atributos do sujeito são fornecidos por **autoridades de atributo** (Sec. 2.4.2, p. 13), e uma declaração de práticas de atributos pode identificar as **fontes autoritativas** da empresa (Sec. 3.1.3.3, p. 23).
- O sujeito **não deve poder alterar** os próprios atributos — o exemplo do documento é o nível de habilitação (Sec. 3.1.3.3, p. 23).
- As políticas partem de requisitos de alto nível em **linguagem natural** (*Natural Language Policies*), depois traduzidos em políticas digitais avaliáveis pelo mecanismo (Sec. 2.4.1, p. 12).

Como prática desta trilha, acrescenta-se: atributos de objeto (classificação, dono, tags) protegidos contra alteração por quem é avaliado por eles, e políticas locais que não enfraquecem a política corporativa.

### Modelo híbrido recomendado

| Camada | Modelo | Exemplo |
|:---|:---|:---|
| **Acesso base** | RBAC, poucos papéis por função | "Analista de crédito" acessa o sistema de crédito |
| **Refinamento** | ABAC com atributos de negócio | Só clientes da própria região; valor até o limite do cargo |
| **Contexto** | Condições de ambiente | Dispositivo gerenciado; bloqueio fora do país; MFA reforçado em risco alto |
| **Dados** | Autorização por objeto na aplicação | O registro pertence ao cliente consultado |

A camada de **dados** merece destaque: falhas de autorização por objeto — o usuário troca um identificador e lê o registro de outro — são uma classe recorrente de vulnerabilidade em APIs, e nenhum IdP as resolve; a aplicação precisa verificar (capítulo V8 do OWASP ASVS 5.0; Módulo 12).

### Auditabilidade

| Pergunta de auditoria | RBAC | ABAC |
|:---|:---|:---|
| "O que esta pessoa pode fazer?" | Fácil: listar papéis | Depende de avaliar regras com os atributos atuais |
| "Quem pode acessar este objeto?" | Fácil a moderada | Difícil — a SP 800-162 observa que exige esforço significativo de recuperação de dados e de computação (Sec. 3.1.2.3, p. 20) |
| "Por que este acesso foi permitido?" | Papel X | Regra Y com atributos Z — exige registro da decisão |

Por isso, em ABAC, o **registro de decisões** (entrada, regra aplicada, resultado) é requisito, não opção.

## Exemplo empresarial

!!! example "Aurora Pagamentos — de 640 papéis a 38"

    O sistema de antecipação de recebíveis da Aurora tinha 640 papéis, criados para combinar função, região, carteira de lojistas e faixa de valor. As revisões trimestrais eram aprovadas sem leitura.

    O redesenho manteve **38 papéis** de função e moveu região, carteira e faixa de valor para **atributos** vindos do RH e do cadastro de lojistas, avaliados por um serviço de autorização central (PDP) chamado pela API (PEP). As políticas passaram a ser versionadas e testadas em pipeline (PAP), e cada decisão de valor acima de R$ 100 mil passou a ser registrada com a regra aplicada. A revisão trimestral voltou a ser possível — e encontrou 14 pessoas com carteira incorreta no RH, um problema de qualidade de atributo que antes estava escondido nos papéis.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Modelo | Um papel para cada combinação | Poucos papéis + atributos + contexto |
| Lógica | Espalhada no código | PDP central ou biblioteca padrão, políticas como código |
| Atributos | De qualquer origem | Fontes autoritativas, protegidas contra alteração |
| Auditoria | Lista de papéis | Papéis + registro de decisões |
| Objeto | Assumido pela interface | Verificado em cada acesso pela aplicação |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias que nomeiam cada parte da arquitetura de autorização:

| Controle ou padrão | Objetivo na arquitetura de autorização | Referência |
|:---|:---|:---|
| Aplicação de acesso | Aplicar as autorizações aprovadas em todo acesso lógico (o papel do PEP) | SP 800-53: AC-3 (Access Enforcement) |
| RBAC e ABAC como política | Aplicar política baseada em papéis e em atributos sobre sujeitos e objetos definidos | SP 800-53: AC-3(7) (Role-based Access Control) e AC-3(13) (Attribute-based Access Control) |
| Decisão antes da aplicação | Garantir que a decisão de acesso seja aplicada a cada pedido antes do acesso (o papel do PDP) | SP 800-53: AC-24 (Access Control Decisions) |
| Atributos de segurança | Associar atributos à informação, definir valores permitidos e auditar alterações de atributos | SP 800-53: AC-16 (Security and Privacy Attributes) |
| Acesso de emergência auditado | *Break-glass*: sobrepor o mecanismo automático em condições definidas, sempre com registro | SP 800-53: AC-3(10) (Audited Override of Access Control Mechanisms) |
| Privilégio mínimo e registro | Conceder só o necessário; registrar decisões para investigação posterior | SP 800-53: AC-6 (Least Privilege), AU-2 (Event Logging) e AU-12 (Audit Record Generation) |
| Gestão do controle de acesso | Processos para conceder, revisar e revogar acessos | CIS v8.1: Controle 6 (Access Control Management) |
| Requisitos de autorização em aplicações | Verificação por função, por objeto e por campo nas aplicações | OWASP ASVS 5.0, capítulo V8 (Authorization) |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, o IAM do provedor combina papéis com condições baseadas em atributos e tags — um ABAC nativo que precisa de governança de tags, porque quem pode alterar a tag pode alterar o acesso. Em on-premises, grupos do AD costumam fazer o papel de RBAC; o refinamento por atributos fica na aplicação. Em ambientes híbridos, o desafio é manter **os mesmos atributos** e **a mesma semântica** nos dois lados — por exemplo, "classificação: confidencial" significando o mesmo em um bucket e em um compartilhamento de arquivos.

## Como especificar e implementar

- "Acessos base são concedidos por papéis de função; refinamentos usam atributos de fontes autoritativas."
- "Políticas de autorização são versionadas, testadas e publicadas por processo controlado."
- "Decisões de autorização para operações críticas são registradas com a regra e os atributos avaliados."
- "Aplicações verificam autorização por objeto em todas as operações sobre dados."
- "Sujeitos não podem alterar os próprios atributos; alterações de tags e atributos de recursos são controladas e registradas."

## Trade-offs, limitações e antipadrões

- **Trade-off:** expressividade (ABAC) versus simplicidade de auditoria (RBAC).
- **Antipadrão — papel por pessoa:** RBAC degenerado em ACL.
- **Antipadrão — atributo editável pelo próprio usuário:** "departamento" alterável no perfil pessoal.
- **Limitação:** a SP 800-162 alerta que serviços de autorização sozinhos não bastam para garantir a segurança necessária (Sec. 3.1.2.5, p. 21); autenticação, proteção de dados e monitoramento continuam necessários.

## Como validar

- Para três usuários, comparar o que o modelo diz que podem fazer com o que conseguem fazer de fato.
- Testar acesso a objeto de outro cliente trocando identificadores na API.
- Alterar um atributo em ambiente de teste e verificar o efeito previsto na decisão.
- Conferir se decisões críticas estão registradas com a regra aplicada.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhum acesso a objeto de outro titular por troca de identificador | Testes automatizados de autorização por objeto na API, sem falha |
| Cada papel corresponde a uma função de negócio | Catálogo de papéis com dono e descrição, sem papéis por região, valor ou pessoa |
| Atributos usados nas regras vêm de fonte autoritativa e não são editáveis pelo sujeito | Mapa atributo → fonte, e teste de alteração negado pelo próprio usuário |
| Políticas versionadas e testadas antes da publicação | Histórico do repositório de políticas e execução dos testes no pipeline |
| Decisões críticas e acessos de emergência registrados com regra e atributos | Amostra de registros com regra, atributos, resultado e justificativa |

## Como apresentar e justificar

- **Para gestores:** "Trocamos 640 papéis que ninguém conseguia revisar por 38 papéis e regras claras. A revisão trimestral volta a significar algo."
- **Para engenharia:** "A API pergunta ao serviço de autorização; a regra fica versionada no repositório, com testes."

## Checklist de revisão arquitetural

- [ ] O número de papéis é proporcional às funções reais.
- [ ] Atributos vêm de fontes autoritativas e são protegidos.
- [ ] PEP, PDP, PIP e PAP estão identificados.
- [ ] Políticas são versionadas e testadas.
- [ ] Decisões críticas são registradas.
- [ ] A autorização por objeto é verificada na aplicação.

## Questões de compreensão

**1.** O que é explosão de papéis e como o ABAC ajuda?

??? success "Resposta comentada"

    É a multiplicação de papéis para representar combinações de função com contexto (região, valor, horário). O ABAC expressa essas combinações em regras sobre atributos, mantendo poucos papéis para o acesso base.

**2.** Qual a função do PIP?

??? success "Resposta comentada"

    Fornecer ao PDP os atributos necessários à decisão — do sujeito, do objeto e do ambiente —, a partir de fontes como diretório, RH, inventário de dados ou MDM.

**3.** Por que o registro de decisões é requisito em ABAC?

??? success "Resposta comentada"

    Porque a decisão depende de regras e de valores de atributos no momento do pedido. Sem registrar regra, atributos e resultado, não é possível explicar por que um acesso foi permitido, nem investigar abusos.

## Exercício de tomada de decisão

!!! question "Cenário: acesso a prontuários na Lumen"

    Regra de negócio da Lumen: "médicos acessam prontuários de pacientes com consulta agendada ou realizada com eles nos últimos 12 meses; em emergência, acessam qualquer prontuário, com justificativa e revisão posterior". As opções em discussão são:

    - **A** — RBAC apenas: papéis por unidade e especialidade, sem verificar o vínculo com o paciente;
    - **B** — modelo híbrido: papéis de função para o acesso base, atributo de vínculo médico–paciente, contexto do dispositivo e regra de emergência auditada;
    - **C** — ABAC puro: nenhum papel; toda decisão por atributos do sujeito, do paciente e do ambiente.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e desenhe a autorização: papéis, atributos, contexto, componentes e registro.

**Objetivos avaliados:** Projetar autorização híbrida — papéis para o acesso base, atributos e contexto para refinamento; descrever os componentes PDP, PEP, PIP e PAP e onde ficam na arquitetura.

**Entrega esperada:** Matriz ponderada e o desenho da autorização: papéis, atributos, contexto, regra de emergência, componentes (PDP, PEP, PIP, PAP) e registro.

**Critérios de avaliação:**

- A regra de vínculo médico–paciente é aplicada por atributo vindo de fonte autoritativa nomeada.
- A regra de emergência tem justificativa obrigatória, alerta e revisão com prazo.
- Cada decisão é registrada com regra e atributos, de modo a explicar o acesso a um titular ou a uma auditoria.

??? success "Resolução de referência"

    | Critério | Peso | A — RBAC apenas | B — Híbrido com vínculo e emergência | C — ABAC puro |
    |:---|:---|:---|:---|:---|
    | Aplicação da regra de vínculo médico–paciente | 3 | 1 | 3 | 3 |
    | Explicar e revisar cada acesso | 3 | 2 | 3 | 2 |
    | Esforço de implantação e operação | 2 | 3 | 2 | 1 |
    | Emergência sem bloquear o atendimento e com controle | 2 | 1 | 3 | 3 |
    | **Total ponderado** | | **17** | **28** | **23** |

    - **Pesos:** a regra de vínculo é o requisito central (dados de saúde, sigilo médico) e explicar cada acesso é o que permite investigar abusos e responder ao titular — peso 3 para ambos. Esforço e emergência pesam 2: importam, mas uma solução que não aplica a regra ou não explica o acesso falha no essencial.
    - **Recomendação: B.** Papéis dão a base revisável ("quem é médico"); o atributo de vínculo aplica a regra de negócio; a regra de emergência atende o pronto-atendimento com registro. A opção A deixa todo médico acessar todo prontuário; a C aplica a regra, mas sem papéis a pergunta "quem pode acessar este prontuário?" exige avaliar regras com todos os atributos, e a implantação é mais pesada.
    - **Trade-off aceito e risco residual:** a decisão depende da qualidade do atributo de vínculo — um agendamento fictício cria vínculo. O risco é tratado com alerta para agendamentos criados e usados pelo mesmo médico no mesmo dia e com a revisão dos acessos de emergência; continua dependendo de quem revisa.
    - **O que mudaria a decisão:** se o sistema de agendamento não puder servir de fonte autoritativa (dados incompletos ou sem API), o vínculo não é confiável e a Lumen precisaria primeiro corrigir a fonte, operando com A acrescida de registro e revisão por amostragem; se o volume de regras crescer muito (pesquisa clínica, convênios, unidades parceiras), C ganha peso pela expressividade.

    **Desenho da opção B:**

    - **Papéis (RBAC):** "médico", "enfermagem", "recepção" — acesso base ao sistema de prontuários.
    - **Atributos (ABAC):** vínculo médico–paciente (consulta agendada ou realizada nos últimos 12 meses), vindo do sistema de agendamento como fonte autoritativa; unidade do médico.
    - **Contexto:** dispositivo gerenciado da clínica; fora dele, só leitura resumida.
    - **Emergência (*break-glass*):** regra que permite acesso sem vínculo mediante justificativa obrigatória, com alerta imediato à coordenação e revisão em 48 horas.
    - **Componentes:** PEP na API de prontuários; PDP no serviço de autorização; PIPs = agendamento, RH e MDM; PAP = repositório de políticas com testes.
    - **Registro:** toda decisão com paciente, regra e atributos; acessos de emergência destacados para revisão.

    **Erros comuns:**

    - Resolver a regra com papéis por especialidade, o que ainda deixa todo médico acessar todo prontuário.
    - Não dizer de onde vem o atributo de vínculo, nem o que acontece se a fonte estiver errada.
    - Esquecer o caso de emergência ou resolvê-lo com uma conta compartilhada.

## Pontos-chave

- ACL decide por identidade; RBAC por papel; ABAC por atributos e contexto.
- RBAC puro tende à explosão de papéis; ABAC puro, à dificuldade de auditoria.
- O modelo híbrido — papéis para a base, atributos e contexto para refinar — é o mais comum e defensável.
- PEP aplica, PDP decide, PIP fornece atributos, PAP administra políticas.
- Atributos precisam de fontes autoritativas; decisões críticas, de registro; objetos, de verificação na aplicação.

## Referências

### Fundamentação principal

- NIST. *SP 800-162 — Guide to Attribute Based Access Control (ABAC) Definition and Considerations*. V. Hu et al., 2014 (atualizações de 2019). <https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-162.pdf> — Sec. 2 (pp. 4–16; pontos funcionais na Sec. 2.4.3) e Sec. 3.1 (pp. 18–24). *(Lido.)*
- NIST. *SP 800-207 — Zero Trust Architecture*. 2020 — Sec. 3, decisão de acesso por política a partir de múltiplas fontes de dados. *(Lido.)*
- Microsoft. *The enterprise access model* — princípios para papéis privilegiados. *(Lido.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-3, AC-3(7), AC-3(10), AC-3(13), AC-6, AC-16, AC-24, AU-2 e AU-12, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controle 6 — gratuito.

### Leitura complementar

- OWASP. *ASVS 5.0* — capítulo V8, Authorization.
- R. Anderson. *Security Engineering*, 3ª ed. — Cap. 6, controle de acesso.

### Aplicação prática

- Escolha um sistema com muitos papéis e identifique quais papéis existem apenas para representar contexto (região, valor, unidade). Proponha a redução para papéis de função e atributos.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
