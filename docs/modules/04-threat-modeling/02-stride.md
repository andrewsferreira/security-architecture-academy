---
id: M04-L02
title: "Aula 02 — STRIDE aplicado à arquitetura"
public_title: "Módulo 4 — Aula 02 — STRIDE aplicado à arquitetura"
description: Como usar as seis categorias STRIDE para encontrar ameaças de forma sistemática em um DFD — relação com as propriedades de segurança, STRIDE por elemento, registro das ameaças e os limites do método.
domain: application-security
tier: professional
status: published
prerequisites: [M04-L01, M01-L01]
objectives:
  - Relacionar cada categoria STRIDE à propriedade de segurança que ela ameaça.
  - Aplicar STRIDE por elemento a um DFD e registrar ameaças de forma acionável.
  - Distinguir ameaças relevantes de ruído usando o contexto do sistema.
  - Reconhecer o que STRIDE não encontra e quando complementá-lo.
minutes: 75
sources: [MS-TMT-STRIDE, OSTERMAN-STRIDE-PER-ELEMENT-2007, TM-MANIFESTO]
further_reading: [MITRE-CAPEC, OWASP-TM-PROJECT, OWASP-ASVS-5]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M04
---

# Aula 02 — STRIDE aplicado à arquitetura { #stride-aplicado-a-arquitetura }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 4 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M04-L02</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Diante de um DFD, a pergunta "o que pode dar errado?" é aberta demais: cada pessoa pensa nas ameaças que conhece. **STRIDE** é um mnemônico que transforma a pergunta em seis perguntas específicas, uma para cada categoria de ameaça, e que pode ser aplicado elemento por elemento. Esta aula mostra as categorias, como cada uma se liga a uma propriedade de segurança, como aplicá-las a um DFD e como registrar o resultado de forma que vire decisão — e não uma planilha de 200 linhas.

**Pré-requisitos:** [Data Flow Diagrams e fluxos de confiança](01-data-flow-diagrams.md) e [Propriedades de segurança](../01-security-fundamentals/01-security-properties.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Relacionar cada categoria STRIDE à propriedade de segurança que ela ameaça.
- Aplicar STRIDE por elemento a um DFD e registrar ameaças de forma acionável.
- Distinguir ameaças relevantes de ruído usando o contexto do sistema.
- Reconhecer o que STRIDE não encontra e quando complementá-lo.

## Conceito

### As seis categorias

As definições abaixo seguem a documentação do Microsoft Threat Modeling Tool; a coluna de propriedade relaciona cada categoria às propriedades vistas na Aula 01 do Módulo 1.

| Categoria | Definição resumida | Propriedade ameaçada | Exemplo |
|:---|:---|:---|:---|
| **S**poofing | Usar indevidamente a identidade ou as credenciais de outro | Autenticidade | Laboratório falso enviando laudos |
| **T**ampering | Modificação maliciosa de dados, em repouso ou em trânsito | Integridade | Alterar o valor de um arquivo de liquidação |
| **R**epudiation | Negar ter realizado uma ação sem que se possa provar o contrário | Não repúdio / responsabilização | Operador nega ter aprovado uma alteração bancária |
| **I**nformation disclosure | Exposição de informação a quem não deveria ter acesso | Confidencialidade | Laudos legíveis por outro laboratório |
| **D**enial of service | Negar o serviço a usuários válidos | Disponibilidade | Gateway saturado por requisições |
| **E**levation of privilege | Usuário sem privilégio obtém acesso privilegiado | Autorização | Paciente que acessa a API administrativa |

### Por que um mnemônico ajuda

STRIDE não é uma lista completa de ataques; é um **instrumento de cobertura**. Percorrer as seis categorias para cada elemento relevante reduz a chance de a análise se concentrar só no tipo de ameaça que a equipe conhece melhor — em geral, confidencialidade.

## Fundamentos técnicos

### STRIDE por elemento

Nem todas as categorias fazem sentido para todos os elementos de um DFD. Osterman, ao descrever a prática da Microsoft, observa que para cada tipo de elemento há um conjunto limitado de categorias aplicáveis, e que **todo fluxo de dados está sujeito a Tampering, Information Disclosure e Denial of Service**. O mapeamento usual para os demais elementos é:

| Elemento | S | T | R | I | D | E |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Entidade externa | sim | | sim | | | |
| Processo | sim | sim | sim | sim | sim | sim |
| Armazenamento | | sim | sim¹ | sim | sim | |
| Fluxo de dados | | sim | | sim | sim | |

¹ Repudiation se aplica a armazenamentos que guardam registros de auditoria, porque eles sustentam a prova de quem fez o quê.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m04-l02-stride-flow.mmd"
```

<figcaption>Figura 1 — STRIDE por elemento na integração de laudos da Lumen: letras indicam as categorias consideradas em cada elemento.</figcaption>
</figure>

### Registrar ameaças de forma acionável

Uma linha "Spoofing no processo X" não ajuda ninguém. Uma ameaça útil tem:

| Campo | Exemplo |
|:---|:---|
| **ID** | TM-07 |
| **Elemento e categoria** | Integração de laudos — Spoofing |
| **Descrição** | Um atacante com a credencial estática do laboratório envia laudos falsos em nome dele |
| **Pré-condições** | Credencial compartilhada, sem rotação, aceita de qualquer origem |
| **Impacto** | Laudo falso associado a paciente real — integridade de dado de saúde |
| **Resposta proposta** | Credencial de workload de curta duração; assinatura do laudo; escrita restrita ao prefixo do laboratório |
| **Decisão** | Mitigar — requisito SR-14 (Aula 06) |
| **Risco relacionado** | RSK-041 no register (Módulo 3 — Aula 06) |

### Filtrar com contexto

Aplicar seis categorias a 30 elementos gera, em tese, 180 perguntas. O contexto reduz o trabalho:

- **Priorize** fluxos que atravessam fronteiras e elementos com dados sensíveis ou privilégio.
- **Agrupe** ameaças equivalentes ("todos os fluxos internos sem TLS") em uma só, com uma resposta padrão.
- **Reaproveite** respostas de arquiteturas de referência: se o gateway padrão já trata autenticação e limites de taxa, registre a herança em vez de reanalisar.
- **Descarte com justificativa**, não por omissão: "Denial of service no relatório mensal — aceito; processo não crítico, pode ser reexecutado."

### Os limites de STRIDE

STRIDE é bom para encontrar ameaças a **componentes técnicos**. Ele encontra menos:

- **Abuso de lógica de negócio** — a fraude que usa funcionalidades legítimas (Aula 03, abuse cases).
- **Cadeias de ataque** — como um adversário combina passos ao longo do ambiente (Aula 04, ATT&CK).
- **Falhas não maliciosas e dependências** — pontos únicos de falha (Aula 05).
- **Ameaças à privacidade** que não envolvem violação de segurança — como coletar dados além da finalidade.

Para padrões de ataque mais detalhados por categoria, o **CAPEC** da MITRE oferece um catálogo público de padrões de ataque com mitigações sugeridas.

## Exemplo empresarial

!!! example "Lumen Saúde — STRIDE na integração de laudos"

    Com o DFD da Aula 01, a equipe aplicou STRIDE à integração de laudos em 40 minutos:

    | ID | Elemento | Cat. | Ameaça | Decisão |
    |:---|:---|:---|:---|:---|
    | TM-07 | Integração | S | Laudos enviados com a credencial estática por quem não é o laboratório | Mitigar |
    | TM-08 | Fluxo laboratório → integração | T | Laudo alterado em trânsito | Mitigar (TLS já existe; acrescentar assinatura do laudo) |
    | TM-09 | Repositório | I | Um laboratório lê laudos de outro, pois a credencial dá acesso a todo o repositório | Mitigar |
    | TM-10 | Log de auditoria | R | Sem registro de qual credencial gravou cada laudo, impossível provar a origem | Mitigar |
    | TM-11 | Integração | D | Envio massivo derruba a integração | Aceitar com limite de taxa simples; integração não crítica para o atendimento imediato |
    | TM-12 | Integração | E | Processo roda com permissão de administrador do repositório | Mitigar — privilégio mínimo |

    Cinco ameaças viraram requisitos; uma foi aceita com justificativa. O register ganhou o cenário RSK-041.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Identificação | Brainstorm livre | STRIDE por elemento, priorizado por fronteiras |
| Registro | "Risco de spoofing" | Ameaça com pré-condições, impacto, resposta e decisão |
| Volume | Centenas de linhas genéricas | Poucas ameaças específicas; equivalentes agrupadas |
| Descarte | Silencioso | Justificado e registrado |
| Escopo | Só ameaças técnicas | STRIDE + abuse cases + ATT&CK + dependências |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, Elevation of Privilege inclui **escalada de permissões de identidade** — um papel que pode criar outro papel com mais permissões — e Spoofing inclui **uso indevido de credenciais de workload**. Information Disclosure inclui configurações de compartilhamento de recursos. Em ambientes híbridos, o canal entre ambientes é um fluxo com T, I e D, e o agente que sincroniza identidades é um processo com as seis categorias — frequentemente o mais crítico do modelo.

## Como especificar e implementar

- "O threat model aplica STRIDE por elemento, no mínimo, a todos os elementos que atravessam fronteiras de confiança ou tratam dados sensíveis."
- "Cada ameaça registra elemento, categoria, descrição, pré-condições, impacto, resposta e decisão."
- "Ameaças descartadas ou aceitas têm justificativa e, quando aplicável, dono e prazo."

## Trade-offs, limitações e antipadrões

- **Trade-off:** completude versus foco. STRIDE completo em sistemas grandes é caro; priorize por fronteiras e dados.
- **Antipadrão — planilha de 200 linhas:** ninguém a lê; ameaças importantes se perdem no ruído.
- **Antipadrão — STRIDE como único método:** perde abuso de negócio, cadeias de ataque e dependências.
- **Limitação:** STRIDE depende da qualidade do DFD; elementos ausentes não são analisados.

## Como validar

- Para os elementos que atravessam fronteiras, conferir se as seis (ou as aplicáveis) categorias foram consideradas.
- Verificar se cada ameaça mitigada gerou requisito e se cada aceita tem justificativa.
- Comparar o modelo com incidentes e achados de testes recentes: algum deles estaria no modelo?

## Como apresentar e justificar

- **Para a equipe:** "Seis perguntas por elemento, começando pelos que vêm de fora. Em uma sessão saímos com as ameaças que importam."
- **Para gestores:** "Encontramos seis ameaças na integração de laudos; cinco viram tarefas de engenharia, uma foi aceita conscientemente."

## Checklist de revisão arquitetural

- [ ] STRIDE foi aplicado aos elementos que atravessam fronteiras e aos que tratam dados sensíveis.
- [ ] Cada ameaça tem pré-condições, impacto, resposta e decisão.
- [ ] Ameaças equivalentes foram agrupadas.
- [ ] Descartes e aceites têm justificativa.
- [ ] Abuso de negócio, cadeias de ataque e dependências foram tratados por outros métodos.

## Questões de compreensão

**1.** Que propriedade de segurança a categoria Repudiation ameaça e que tipo de elemento costuma sustentá-la?

??? success "Resposta comentada"

    Não repúdio e responsabilização. É sustentada por registros de auditoria confiáveis — por isso Repudiation se aplica a armazenamentos que guardam logs, além de entidades externas e processos.

**2.** Por que todo fluxo de dados está sujeito a Tampering, Information Disclosure e Denial of Service?

??? success "Resposta comentada"

    Porque dados em movimento podem ser alterados, lidos ou interrompidos no canal. Mesmo que a ameaça seja aceita (por exemplo, em uma rede interna considerada confiável), ela existe e deve ser decidida, não ignorada.

**3.** Cite um tipo de ameaça que STRIDE tende a não encontrar.

??? success "Resposta comentada"

    Abuso de lógica de negócio — fraude com funcionalidades legítimas —, cadeias de ataque ao longo do ambiente, falhas não maliciosas por dependências e ameaças à privacidade sem violação de segurança.

## Exercício de tomada de decisão

!!! question "Cenário: STRIDE no fluxo de notificações da Lumen"

    No DFD da Aula 01, o serviço de notificações consome eventos da fila e envia SMS com data e especialidade da consulta pelo provedor externo (fluxo 7). Aplique STRIDE ao serviço de notificações e ao fluxo 7, registre as ameaças mais relevantes e decida o tratamento de cada uma. Para a ameaça de Information Disclosure no fluxo 7, compare três respostas com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho), sabendo que um terço dos pacientes não instalou o app:

    - **A** — manter a especialidade no SMS e exigir cláusulas de confidencialidade do provedor;
    - **B** — retirar a especialidade e enviar só data, horário e link autenticado;
    - **C** — abandonar o SMS e notificar apenas por push no app.

??? success "Resolução de referência"

    | Critério | Peso | A — Especialidade + contrato | B — SMS sem dado sensível | C — Só push no app |
    |:---|:---|:---|:---|:---|
    | Proteção do dado de saúde | 3 | 1 | 3 | 3 |
    | Alcance do lembrete (pacientes avisados) | 3 | 3 | 3 | 1 |
    | Dependência de terceiros (3 = menor) | 2 | 1 | 2 | 3 |
    | Custo de mudança (3 = menor) | 1 | 3 | 3 | 2 |
    | **Total ponderado** | | **17** | **25** | **20** |

    **Pesos:** proteção do dado sensível e alcance do lembrete recebem 3 — o primeiro decorre do dever de segurança da LGPD (art. 46) para dados que podem revelar saúde, o segundo é a razão de existir do serviço; dependência de terceiros recebe 2; custo de mudança recebe 1, porque as três respostas são baratas. **Recomendação: B**, que elimina o dado sensível sem perder pacientes. Contratos protegem pouco quando o dado aparece na tela do celular.

    - **Fluxo 7 — I:** a especialidade no SMS pode revelar condição de saúde (dado sensível) ao provedor e a quem vir o celular. **Eliminar o dado (B):** remover a especialidade da mensagem; enviar só data, horário e link autenticado.
    - **Fluxo 7 — T:** mensagem alterada no provedor para incluir link malicioso. **Mitigar parcialmente:** contrato com o provedor e links apenas para domínio próprio; **residual aceito** e comunicado aos pacientes ("nunca pedimos senha por SMS").
    - **Serviço — S:** um processo qualquer publica eventos falsos na fila. **Mitigar:** apenas o serviço de agendamento tem permissão de publicar.
    - **Serviço — E:** credencial do provedor de SMS com permissões de administração da conta. **Mitigar:** credencial restrita a envio.
    - **Serviço — D:** fila inundada atrasa notificações. **Aceitar:** impacto baixo; monitorar profundidade da fila.
    - **Serviço — R:** sem registro de quais mensagens foram enviadas. **Mitigar:** registrar ID do evento e status de entrega, sem conteúdo sensível.
    - **Risco residual:** o horário e o fato de haver uma consulta continuam visíveis no celular; o paciente pode optar por não receber SMS.
    - **O que mudaria a decisão:** se quase todos os pacientes usassem o app, C eliminaria também a dependência do provedor de SMS.

## Pontos-chave

- STRIDE transforma "o que pode dar errado?" em seis perguntas ligadas a propriedades de segurança.
- STRIDE por elemento reduz o trabalho; todo fluxo está sujeito a T, I e D.
- Ameaças úteis têm pré-condições, impacto, resposta e decisão.
- Priorize fronteiras e dados sensíveis; agrupe equivalentes; descarte com justificativa.
- Complemente STRIDE com abuse cases, ATT&CK e análise de dependências.

## Referências

### Fundamentação principal

- Microsoft. *Threats — Microsoft Threat Modeling Tool*. Microsoft Learn, atualizada em 25/08/2022. <https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats> — definições das categorias STRIDE. *(Lido.)*
- L. Osterman. *Threat Modeling Again, STRIDE per Element*. 2007. <https://learn.microsoft.com/ru-ru/archive/blogs/larryosterman/threat-modeling-again-stride-per-element>. *(Lido; a tabela completa está em imagem.)*
- *Threat Modeling Manifesto*. <https://threatmodelingmanifesto.org/>.

### Leitura complementar

- MITRE. *CAPEC — Common Attack Pattern Enumeration and Classification*. <https://capec.mitre.org/about>.
- OWASP. *Threat Modeling Project* — ferramentas para registrar o modelo como código.
- OWASP. *ASVS 5.0* — requisitos verificáveis para responder a ameaças em aplicações (Aula 06).

### Aplicação prática

- Aplique STRIDE por elemento aos três fluxos priorizados no DFD que você desenhou na Aula 01 e registre as ameaças no formato desta aula.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
