---
id: M06-L08
title: "Aula 08 — Ciclo de vida de identidades e segregação de funções"
public_title: "Módulo 6 — Aula 08 — Ciclo de vida de identidades e segregação de funções"
description: Como governar acessos ao longo do tempo — admissão, mudança de função e desligamento a partir de fonte autoritativa, solicitações e aprovações, revisões de acesso úteis, contas órfãs e segregação de funções preventiva e detectiva.
domain: iam
tier: professional
status: published
prerequisites: [M06-L01, M06-L02]
objectives:
  - Desenhar o ciclo joiner-mover-leaver a partir de uma fonte autoritativa.
  - Especificar regras de segregação de funções e aplicá-las de forma preventiva e detectiva.
  - Tornar revisões de acesso úteis, em vez de cerimoniais.
  - Tratar contas órfãs, terceiros e identidades sem fonte autoritativa.
minutes: 60
sources: [NIST-SP800-53, NIST-SP800-162, BOOK-ANDERSON-SE3, CIS-CONTROLS-V8-1]
further_reading: [NIST-SP800-63-4, MS-ENTERPRISE-ACCESS-MODEL, LGPD-L13709]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M06
---

# Aula 08 — Ciclo de vida de identidades e segregação de funções { #ciclo-de-vida-de-identidades-e-segregacao-de-funcoes }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 6 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M06-L08</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Acessos acumulam: a pessoa muda de área e leva os acessos antigos; o terceiro sai e a conta continua ativa; o analista recebe, "temporariamente", a permissão de aprovar o que ele mesmo cadastra. A **governança de identidades** (IGA) existe para que cada identidade tenha os acessos certos **ao longo do tempo**. Esta aula trata do ciclo de vida, das revisões de acesso e da **segregação de funções**, que impede que uma única pessoa execute sozinha uma transação crítica do início ao fim.

**Pré-requisitos:** [Disciplinas de identidade](01-identity-disciplines.md) e [Modelos de autorização](02-authorization-models.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Desenhar o ciclo joiner-mover-leaver a partir de uma fonte autoritativa.
- Especificar regras de segregação de funções e aplicá-las de forma preventiva e detectiva.
- Tornar revisões de acesso úteis, em vez de cerimoniais.
- Tratar contas órfãs, terceiros e identidades sem fonte autoritativa.

## Conceito

### Joiner, mover, leaver

| Evento | O que deve acontecer | Falha comum |
|:---|:---|:---|
| **Joiner** (admissão) | Identidade criada a partir do RH, com acessos de nascimento pelo cargo | Acessos copiados de "alguém parecido" |
| **Mover** (mudança) | Acessos do novo cargo concedidos; antigos revogados após transição | Acúmulo — a pessoa leva tudo |
| **Leaver** (desligamento) | Identidade desabilitada imediatamente; sessões e tokens revogados | Conta ativa por semanas; tokens de SaaS válidos |

A chave é a **fonte autoritativa**: o RH para funcionários, o sistema de contratos para terceiros, o cadastro de parceiros para identidades externas. Sem fonte autoritativa, não há como saber se uma conta deveria existir.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m06-l08-jml.mmd"
```

<figcaption>Figura 1 — Admissão, mudança e pedidos passam pela verificação de segregação de funções; desligamento desabilita imediatamente; contas órfãs são investigadas.</figcaption>
</figure>

### Segregação de funções

O controle **AC-5 (Separation of Duties)** da SP 800-53 Rev. 5 pede que a organização identifique e documente os deveres que exigem separação e defina autorizações de acesso que suportem essa separação. A discussão do controle explica que a separação reduz o risco de atividade maliciosa sem conluio e cita dividir funções de negócio e de suporte entre pessoas ou papéis diferentes e garantir que quem administra o controle de acesso não administre também as funções de auditoria; como violações podem atravessar sistemas, a política deve considerar o conjunto dos sistemas.

A ideia remonta ao modelo de **Clark-Wilson** (Módulo 1 — Aula 07), em que dados críticos só mudam por procedimentos controlados, com separação de funções e trilha de auditoria — Anderson discute esse modelo no capítulo 12 de *Security Engineering*.

## Fundamentos técnicos

### Matriz de conflitos

Segregação de funções começa por uma matriz de **pares conflitantes**, definida com o negócio:

| Função A | Função B | Risco do acúmulo |
|:---|:---|:---|
| Cadastrar fornecedor | Aprovar pagamento | Fornecedor fictício pago pela mesma pessoa |
| Alterar dados bancários | Aprovar alteração | Desvio de pagamento (Módulo 4 — Aula 03) |
| Desenvolver código | Implantar em produção sem revisão | Código malicioso em produção |
| Administrar contas | Administrar logs de auditoria | Apagar rastros do próprio abuso |
| Solicitar acesso | Aprovar o próprio acesso | Autoconcessão |

### Preventivo e detectivo

| Abordagem | Como | Quando |
|:---|:---|:---|
| **Preventiva** | O sistema de IGA ou a aplicação bloqueia a concessão do par conflitante | Sempre que possível |
| **Detectiva** | Relatórios periódicos de conflitos e de transações em que a mesma pessoa executou as duas funções | Quando a prevenção não é viável (equipes pequenas) |
| **Compensatória** | Revisão independente de todas as transações de quem acumula funções | Exceções aprovadas, com dono e prazo |

Equipes pequenas frequentemente não conseguem separar todas as funções. Nesse caso, a exceção é aceitável **se** houver controle detectivo ou compensatório — e se a exceção estiver registrada.

### Revisões de acesso que funcionam

Revisões trimestrais de centenas de itens, aprovadas em lote, são cerimônia. Para que sirvam:

- **Revisar o que importa:** acessos privilegiados, a sistemas críticos e a dados sensíveis — não tudo.
- **Mostrar contexto:** último uso, data de concessão, quem aprovou, se o acesso é do cargo ou exceção.
- **Revisor certo:** o dono do recurso para o "o quê"; o gestor para o "quem".
- **Revogação automática** do que não for confirmado.
- **Medir:** taxa de revogação (uma taxa próxima de zero por anos indica revisão cerimonial).

### Contas órfãs e terceiros

- **Conta órfã:** sem correspondência na fonte autoritativa. Deve ser desabilitada e investigada — pode ser resquício de desligamento ou criação indevida.
- **Terceiros:** identidade com data de término vinculada ao contrato, patrocinador interno responsável e revisão mais frequente.
- **Contas genéricas:** proibidas para uso interativo; quando inevitáveis, com dono e acesso intermediado (Aula 06).

### Dados pessoais

Bases de identidade contêm dados pessoais de funcionários e terceiros. A LGPD (Módulo 3 — Aula 04) aplica-se: finalidade, necessidade e segurança orientam quais atributos coletar e por quanto tempo mantê-los após o desligamento.

## Exemplo empresarial

!!! example "Meridiana — o analista que cadastrava e aprovava"

    Uma auditoria interna na Meridiana encontrou três analistas com permissão para cadastrar fornecedores e aprovar pagamentos — acumulada ao longo de mudanças de função. Também encontrou 64 contas ativas de ex-funcionários e terceiros, e revisões trimestrais com taxa de revogação de 0,3%.

    Medidas:

    1. Integração do RH com o diretório: desligamentos desabilitam a conta no mesmo dia; mudanças de cargo geram revogação automática após 30 dias.
    2. Matriz de conflitos com cinco pares, aplicada de forma **preventiva** no ERP para os dois pares financeiros.
    3. Revisões trimestrais restritas a acessos financeiros e privilegiados, com último uso exibido e revogação automática do que não for confirmado.
    4. Contas de terceiros com data de término do contrato.

    Na primeira revisão redesenhada, a taxa de revogação foi de 18%.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Criação de acessos | Cópia de outro usuário | Acessos de nascimento pelo cargo |
| Mudança de função | Acúmulo | Revogação dos antigos após transição |
| Desligamento | Chamado manual | Automático a partir do RH, com revogação de sessões |
| Segregação | Implícita | Matriz de conflitos, preventiva quando possível |
| Revisões | Tudo, em lote | Foco no que importa, com contexto e revogação automática |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias para cada etapa do ciclo de vida:

| Controle ou padrão | Objetivo no ciclo de vida | Referência |
|:---|:---|:---|
| Gestão de contas | Criar, modificar, desabilitar e remover contas com base em autorização e revisar a conformidade | SP 800-53: AC-2 (Account Management) |
| Desabilitar contas | Desabilitar contas expiradas, sem pessoa associada, em violação de política ou inativas | SP 800-53: AC-2(3) (Disable Accounts) |
| Desligamento | Desabilitar o acesso em prazo definido e revogar autenticadores e credenciais | SP 800-53: PS-4 (Personnel Termination) |
| Mudança de função | Revisar e confirmar a necessidade dos acessos e ajustá-los na transferência | SP 800-53: PS-5 (Personnel Transfer) |
| Terceiros | Requisitos de segurança de pessoal para prestadores, com aviso de saídas e transferências | SP 800-53: PS-7 (External Personnel Security) |
| Segregação de funções | Identificar deveres que exigem separação e definir autorizações que a suportem | SP 800-53: AC-5 (Separation of Duties) |
| Revisão de privilégios | Revisar privilégios periodicamente e remover os desnecessários | SP 800-53: AC-6(7) (Review of User Privileges) |
| Restrição de mudanças | Restrições de acesso para mudanças no sistema (quem implanta) | SP 800-53: CM-5 (Access Restrictions for Change) |
| Gestão de contas e de acesso | Inventário de contas e processos de concessão e revogação | CIS v8.1: Controles 5 (Account Management) e 6 (Access Control Management) |

## Aplicabilidade: on-premises, cloud e híbrido

O ciclo de vida precisa alcançar o diretório local, o IdP em nuvem, os SaaS e as contas nos consoles de nuvem. Desabilitar só o AD não revoga tokens de SaaS já emitidos; o desligamento precisa revogar sessões no IdP e, quando suportado, nas aplicações. Em cloud, papéis concedidos diretamente a usuários (fora de grupos governados) escapam do ciclo de vida — evite-os.

## Como especificar e implementar

- "Toda identidade tem fonte autoritativa; contas sem correspondência são desabilitadas e investigadas."
- "Desligamentos desabilitam identidades e revogam sessões no mesmo dia útil."
- "Mudanças de função revogam acessos do cargo anterior após período definido."
- "Pares de funções conflitantes são definidos com o negócio e bloqueados preventivamente onde possível; exceções têm controle compensatório, dono e prazo."
- "Revisões de acesso cobrem acessos privilegiados e a sistemas e dados críticos, com revogação automática do não confirmado."

## Trade-offs, limitações e antipadrões

- **Trade-off:** segregação estrita versus tamanho da equipe — controles detectivos e compensatórios equilibram.
- **Antipadrão — "espelhar acessos do colega":** propaga acúmulos.
- **Antipadrão — revisão sem contexto:** gestores aprovam o que não entendem.
- **Limitação:** IGA governa acessos concedidos; não detecta abuso de acessos legítimos — isso exige monitoração.

## Como validar

- Cruzar contas ativas com a fonte autoritativa e contar órfãs.
- Medir o tempo entre o desligamento no RH e a desabilitação.
- Executar o relatório de conflitos de segregação.
- Acompanhar a taxa de revogação nas revisões.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhuma conta ativa sem correspondência na fonte autoritativa, fora das investigadas | Cruzamento contas × RH, contratos e cadastro de parceiros |
| Desligamento desabilita a identidade e revoga sessões no mesmo dia útil | Tempo medido entre o registro no RH e a desabilitação, em amostra |
| Nenhum acúmulo de par conflitante sem exceção registrada | Relatório de conflitos de segregação, com exceções, donos e prazos |
| Revisões com revogação efetiva | Taxa de revogação por ciclo e revogação automática do não confirmado |
| Terceiros com data de término e patrocinador | Amostra de contas de terceiros |

## Como apresentar e justificar

- **Para a diretoria:** "Três pessoas conseguiam cadastrar um fornecedor e pagá-lo sozinhas. Agora o sistema impede."
- **Para gestores:** "A revisão ficou menor: só acessos financeiros e privilegiados, com a data do último uso. O que vocês não confirmarem sai automaticamente."

## Checklist de revisão arquitetural

- [ ] Fonte autoritativa para cada tipo de identidade.
- [ ] Desligamento automático com revogação de sessões.
- [ ] Revogação de acessos antigos em mudanças de função.
- [ ] Matriz de conflitos definida e aplicada.
- [ ] Revisões focadas, com contexto e revogação automática.
- [ ] Contas órfãs e genéricas tratadas.

## Questões de compreensão

**1.** Por que a fonte autoritativa é essencial ao ciclo de vida?

??? success "Resposta comentada"

    Porque é ela que diz se uma identidade deveria existir e com que cargo. Sem ela, não há como detectar contas órfãs, automatizar desligamentos nem derivar acessos de nascimento.

**2.** O que o controle AC-5 da SP 800-53 pede?

??? success "Resposta comentada"

    Que a organização identifique e documente os deveres que exigem separação e defina autorizações de acesso que a suportem — por exemplo, dividindo funções de negócio e de suporte entre pessoas diferentes e separando a administração de acesso da administração de auditoria.

**3.** Quando uma exceção de segregação de funções é aceitável?

??? success "Resposta comentada"

    Quando a separação é inviável (por exemplo, equipe muito pequena) e há controle detectivo ou compensatório — como revisão independente de todas as transações —, com a exceção registrada, dono e prazo.

## Exercício de tomada de decisão

!!! question "Cenário: segregação no deploy da Lumen"

    A equipe do portal do paciente da Lumen tem quatro desenvolvedores. Todos podem aprovar pull requests e implantar em produção. O auditor pede que "quem desenvolve não implante". As opções são:

    - **A** — separar por equipe: só uma equipe de operações implanta em produção;
    - **B** — separar autor e aprovador pelo processo: proteção de ramo, implantação só pela pipeline com federação de workload, aprovação de ambiente por pessoa diferente do autor e relatório detectivo;
    - **C** — manter o modelo atual e acrescentar uma revisão mensal das implantações pelo gestor.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e proponha controles proporcionais.

**Objetivos avaliados:** Especificar regras de segregação de funções e aplicá-las de forma preventiva e detectiva; tornar revisões de acesso úteis, em vez de cerimoniais.

**Entrega esperada:** Matriz ponderada, controles preventivos e detectivos e a resposta ao auditor em um parágrafo.

**Critérios de avaliação:**

- A separação é entre autor e aprovador da mudança, aplicada pela plataforma e não só por processo.
- Há controle detectivo com indicador esperado (implantações com aprovador igual ao autor = zero).
- O risco residual reconhece o conluio e diz como é tratado.

??? success "Resolução de referência"

    | Critério | Peso | A — Equipe separada implanta | B — Autor e aprovador separados no processo | C — Revisão mensal |
    |:---|:---|:---|:---|:---|
    | Nenhuma mudança chega à produção sem revisão de outra pessoa | 3 | 3 | 3 | 1 |
    | Proporcionalidade ao tamanho da equipe | 2 | 1 | 3 | 3 |
    | Evidência verificável pelo auditor | 2 | 2 | 3 | 2 |
    | Custo de implantação e operação | 1 | 1 | 2 | 3 |
    | **Total ponderado** | | **16** | **23** | **16** |

    - **Pesos:** o risco a tratar é uma mudança não revisada chegar à produção (peso 3). Proporcionalidade e evidência pesam 2: o controle precisa caber em uma equipe de quatro pessoas e ser demonstrável. O custo pesa 1.
    - **Recomendação: B**, com os controles a seguir. A opção A atende ao texto do pedido, mas cria uma fila para uma equipe pequena e não impede que a equipe de operações implante algo sem revisão; C só descobre o problema depois que ele está em produção.

    **Controles da opção B:**

    - **Preventivo:** proteção de ramo exigindo aprovação de **outro** desenvolvedor para mesclar em `main`; o autor não pode aprovar o próprio código.
    - **Implantação:** só a pipeline implanta em produção, a partir de `main`, com federação de workload (Aula 07) — nenhum desenvolvedor tem credencial direta de produção.
    - **Aprovação de ambiente:** implantação em produção exige aprovação de uma pessoa diferente do autor da mudança.
    - **Detectivo:** relatório mensal de implantações cujo aprovador coincide com o autor (deve ser zero) e de alterações fora da pipeline.
    - **Resposta ao auditor:** a separação é entre **autor da mudança** e **aprovador**, aplicada pelo processo e pela pipeline, e não entre pessoas de equipes diferentes — proporcional ao tamanho da equipe e verificável.
    - **Trade-off aceito e risco residual:** dois desenvolvedores em conluio ainda conseguem levar uma mudança maliciosa à produção — a segregação reduz o risco de abuso sem conluio, como registra a discussão do AC-5; o residual é tratado pelo relatório detectivo e pela revisão de alterações fora da pipeline.
    - **O que mudaria a decisão:** uma exigência regulatória explícita de separação entre equipes (por exemplo, em um sistema de pagamentos) ou o crescimento da equipe tornaria A proporcional; se a plataforma de repositórios não permitir proteção de ramo nem aprovação de ambiente, C passa a ser a medida provisória, com prazo para B.

    **Erros comuns:**

    - Separar por equipes em uma equipe de quatro pessoas, criando fila sem impedir mudança não revisada.
    - Contar com revisão mensal, que só descobre o problema depois da produção.
    - Deixar credenciais diretas de produção com os desenvolvedores.

## Pontos-chave

- O ciclo joiner-mover-leaver depende de fonte autoritativa e de automação.
- Desligamento precisa revogar sessões e tokens, não só desabilitar a conta.
- Segregação de funções começa por uma matriz de conflitos definida com o negócio.
- Prefira prevenção; use detecção e compensação quando a prevenção não for viável.
- Revisões de acesso só funcionam com foco, contexto e revogação automática.

## Referências

### Fundamentação principal

- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-2, AC-2(3), AC-5 (enunciado e discussão), AC-6(7), CM-5, PS-4, PS-5 e PS-7, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controles 5 e 6 — gratuito.
- NIST. *SP 800-162* — atributos de fontes autoritativas (Sec. 2.4.2 e 3.1.3.3). *(Lido.)*
- R. Anderson. *Security Engineering*, 3ª ed. — Cap. 12, §12.2.3, Clark-Wilson. *(Lido.)*

### Leitura complementar

- NIST. *SP 800-63-4* — ciclo de vida de autenticadores.
- Microsoft. *The enterprise access model* — separação de funções entre planos.
- Brasil. *LGPD* — princípios aplicáveis a dados de identidade.

### Aplicação prática

- Monte a matriz de conflitos para um processo financeiro da sua organização e verifique, em um sistema, quantas pessoas acumulam pares conflitantes hoje.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
