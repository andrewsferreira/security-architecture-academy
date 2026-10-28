---
id: M04-L06
title: "Aula 06 — De ameaças a requisitos de segurança"
public_title: "Módulo 4 — Aula 06 — De ameaças a requisitos de segurança"
description: Como responder à pergunta "o que vamos fazer a respeito?" — escolher o tratamento de cada ameaça, escrever requisitos de segurança verificáveis, apoiar-se em padrões como o OWASP ASVS 5.0 e manter a rastreabilidade entre ameaça, requisito, controle e teste.
domain: application-security
tier: architect
status: published
prerequisites: [M04-L02, M04-L04, M02-L07]
objectives:
  - Decidir o tratamento de cada ameaça — mitigar, eliminar, transferir ou aceitar — com base no risco.
  - Escrever requisitos de segurança verificáveis, sem prescrever tecnologia desnecessariamente.
  - Usar o OWASP ASVS 5.0 como referência de requisitos e de nível de verificação.
  - Manter a rastreabilidade ameaça → requisito → controle → teste.
minutes: 75
sources: [OWASP-ASVS-5, TM-MANIFESTO, NIST-SP800-160-V1R1]
further_reading: [MITRE-CAPEC, NIST-SP800-53, SABSA-W100]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M04
---

# Aula 06 — De ameaças a requisitos de segurança { #de-ameacas-a-requisitos-de-seguranca }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 4 · Nível 1</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">75 min · ID técnico: M04-L06</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Uma lista de ameaças não protege nada até virar decisões e trabalho. Esta aula trata da terceira pergunta do threat modeling — **o que vamos fazer a respeito?** —: decidir o tratamento de cada ameaça, escrever **requisitos verificáveis** que a engenharia consiga implementar e a validação consiga testar, apoiar-se em padrões como o **OWASP ASVS 5.0** e manter a rastreabilidade até o teste que prova que a resposta funciona.

**Pré-requisitos:** [STRIDE](02-stride.md), [MITRE ATT&CK](04-mitre-attack-scenarios.md) e [Business-driven Security Architecture](../02-security-architecture/07-business-driven-requirements.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Decidir o tratamento de cada ameaça — mitigar, eliminar, transferir ou aceitar — com base no risco.
- Escrever requisitos de segurança verificáveis, sem prescrever tecnologia desnecessariamente.
- Usar o OWASP ASVS 5.0 como referência de requisitos e de nível de verificação.
- Manter a rastreabilidade ameaça → requisito → controle → teste.

## Conceito

### Quatro respostas a uma ameaça

| Resposta | Significado no threat model | Exemplo |
|:---|:---|:---|
| **Mitigar** | Reduzir probabilidade ou impacto com controles | Credencial de workload de curta duração para o laboratório |
| **Eliminar** | Remover a funcionalidade, o fluxo ou o dado que cria a ameaça | Retirar a especialidade médica do SMS |
| **Transferir** | Passar a responsabilidade a quem pode tratá-la melhor | Página de pagamento hospedada pelo provedor (escopo PCI) |
| **Aceitar** | Assumir conscientemente, com dono e prazo | DoS na integração de laudos, não crítica para o atendimento imediato |

**Eliminar** costuma ser a resposta mais barata e a mais esquecida: o dado que não é coletado não vaza; o fluxo que não existe não é adulterado. É também a aplicação direta do princípio de minimização da LGPD (Módulo 3 — Aula 04).

### Requisito verificável

Um requisito de segurança é verificável quando um terceiro consegue, sem perguntar ao autor, dizer se ele foi atendido. Compare:

| Fraco | Verificável |
|:---|:---|
| "A integração deve ser segura." | "A integração aceita apenas requisições autenticadas por credencial de workload com validade máxima de 1 hora, emitida para o laboratório remetente." |
| "Usar criptografia forte." | "Laudos são assinados pelo laboratório; a ingestão rejeita laudos com assinatura inválida ou de chave não cadastrada." |
| "Logar tudo." | "Cada gravação de laudo registra identidade da credencial, prefixo, hash do arquivo e horário, em repositório que a integração não pode alterar." |

O requisito descreve o **resultado** e os **parâmetros** que importam; só prescreve tecnologia quando ela é a decisão de arquitetura (por exemplo, um padrão corporativo).

## Fundamentos técnicos

### Rastreabilidade

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m04-l06-threat-to-requirement.mmd"
```

<figcaption>Figura 1 — Da ameaça ao requisito verificável, ao controle do catálogo e ao teste que realimenta o threat model.</figcaption>
</figure>

A cadeia é a mesma ideia de rastreabilidade da Aula 07 do Módulo 2 e do catálogo de controles da Aula 07 do Módulo 3, agora no nível da solução:

| Ameaça | Tratamento | Requisito | Controle do catálogo | Teste |
|:---|:---|:---|:---|:---|
| TM-07 — S: laboratório falso | Mitigar | SR-14 — credencial de workload de curta duração; escrita só no próprio prefixo | CTL-IAM-08 | Credencial expirada e prefixo alheio rejeitados |
| TM-08 — T: laudo alterado | Mitigar | SR-15 — assinatura do laudo verificada na ingestão | CTL-INT-02 | Laudo com assinatura inválida rejeitado |
| TM-10 — R: origem não provada | Mitigar | SR-16 — registro imutável de cada gravação | CTL-LOG-04 | Tentativa de alterar registro falha e gera alerta |
| TM-11 — D: envio massivo | Aceitar | — (limite de taxa simples registrado como decisão) | — | — |

O teste fecha a quarta pergunta do threat modeling — **fizemos um bom trabalho?** — e alimenta a revisão (Aula 07).

### OWASP ASVS 5.0 como referência

O **Application Security Verification Standard (ASVS)**, versão 5.0.0, publicada em 30/05/2025 e licenciada em CC BY-SA 4.0, é um catálogo de requisitos verificáveis para aplicações. Segundo fonte secundária consultada, ele se organiza em 17 capítulos — de V1 *Encoding and Sanitization* a V17 *WebRTC*, passando por V6 *Authentication*, V8 *Authorization*, V15 *Secure Coding and Architecture* e V16 *Security Logging and Error Handling* — e em três **níveis cumulativos**. A tabela abaixo resume o uso típico de cada nível segundo a mesma fonte secundária; antes de fixar o nível de um sistema, confira a descrição no documento oficial:

| Nível | Uso típico |
|:---|:---|
| **L1** | Piso para qualquer aplicação; vulnerabilidades mais exploradas |
| **L2** | Aplicações de negócio com dados sensíveis |
| **L3** | Alta garantia: finanças, saúde, infraestrutura crítica |

Os requisitos são identificados por capítulo, seção e número e, segundo o site oficial do ASVS, devem ser citados no formato `v<versão>-<capítulo>.<seção>.<requisito>` (por exemplo, `v5.0.0-6.2.1`), para evitar ambiguidade entre versões.

Como usar o ASVS na arquitetura:

1. **Escolher o nível** por sistema, a partir da categorização de impacto (Módulo 3 — Aula 02): o portal do paciente da Lumen, com dados de saúde, mira L2 com requisitos selecionados de L3.
2. **Usar o ASVS como base** de requisitos da solução, e o threat model para **acrescentar** requisitos específicos (lógica de negócio, integrações) e **priorizar**.
3. **Referenciar** o identificador versionado no requisito interno, para que a verificação use o mesmo critério.

### Requisitos que nascem de outras análises

- **Árvores e abuse cases** (Aula 03) geram requisitos de lógica de negócio: dupla aprovação, confirmação por canal cadastrado.
- **ATT&CK** (Aula 04) gera requisitos de arquitetura e de detecção: MFA resistente a phishing, alertas para técnicas não prevenidas.
- **Análise de dependências** (Aula 05) gera requisitos de resiliência: domínios de falha, recuperação isolada, acesso de emergência.

### Requisitos para o que não se previne

Quando a arquitetura não consegue prevenir uma ameaça com custo razoável, o requisito passa a ser de **detecção e resposta**: "acessos a prontuários acima de N por hora por usuário geram alerta tratado em até 24 horas". O requisito de detecção é tão verificável quanto o preventivo — e precisa de teste.

## Exemplo empresarial

!!! example "Aurora Pagamentos — de 41 ameaças a 19 requisitos"

    O threat model da nova API de antecipação de recebíveis da Aurora encontrou 41 ameaças. A equipe:

    1. **Eliminou** 6 (removendo campos e um endpoint de exportação desnecessário).
    2. **Agrupou** ameaças equivalentes e cobriu 17 delas com requisitos do ASVS L2 já presentes no padrão de APIs da empresa (herança).
    3. **Escreveu 19 requisitos específicos**, a maioria de lógica de negócio (limites de antecipação por lojista, dupla aprovação acima de valor) e de detecção.
    4. **Aceitou** 2, com dono e prazo.

    Cada um dos 19 requisitos virou um item de backlog com critério de aceite testável; 14 foram automatizados como testes de regressão na pipeline.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Saída do threat model | Lista de ameaças | Decisões de tratamento e requisitos verificáveis |
| Formato do requisito | "Deve ser seguro" | Resultado e parâmetros testáveis |
| Base de requisitos | Escrita do zero a cada projeto | ASVS no nível adequado + requisitos específicos |
| Eliminação | Raramente considerada | Primeira opção quando possível |
| Prova | Declaração da equipe | Teste vinculado ao requisito |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, muitos requisitos podem ser expressos como **políticas como código** (guardrails, regras de admissão, verificações na pipeline), o que torna a verificação contínua. Em on-premises, a verificação tende a ser periódica e manual; o requisito deve deixar claro como e com que frequência será verificado. Em ambientes híbridos, requisitos sobre o canal entre ambientes (autenticação mútua, cifragem, origem permitida) precisam ser verificáveis nos dois lados.

## Como especificar e implementar

- "Toda ameaça do threat model tem decisão de tratamento registrada."
- "Requisitos de segurança são escritos como resultados verificáveis, com parâmetros, e têm critério de aceite testável."
- "Aplicações adotam o nível do ASVS definido pela categorização, citando os identificadores com a versão."
- "Requisitos de detecção têm teste equivalente ao de requisitos preventivos."
- "A rastreabilidade ameaça → requisito → controle → teste é mantida no repositório do sistema."

## Trade-offs, limitações e antipadrões

- **Trade-off:** requisitos detalhados reduzem ambiguidade, mas podem engessar a implementação; descreva o resultado, não o código.
- **Antipadrão — ASVS inteiro como backlog:** centenas de itens sem priorização; a equipe desiste.
- **Antipadrão — requisito sem teste:** vira opinião na revisão final.
- **Limitação:** padrões cobrem o comum; lógica de negócio e integrações específicas sempre exigem análise própria.

## Como validar

- Amostrar requisitos e verificar se um terceiro consegue testá-los sem perguntar ao autor.
- Conferir se cada ameaça mitigada tem requisito, controle e teste.
- Executar os testes de segurança na pipeline e revisar falhas recorrentes.

## Como apresentar e justificar

- **Para engenharia:** "São 19 requisitos, cada um com critério de aceite. Os demais já vêm do padrão de APIs."
- **Para o dono do produto:** "Eliminamos o endpoint de exportação: menos funcionalidade, menos risco, menos trabalho."

## Checklist de revisão arquitetural

- [ ] Toda ameaça tem tratamento decidido.
- [ ] A eliminação foi considerada antes de mitigar.
- [ ] Requisitos são verificáveis e têm critério de aceite.
- [ ] O nível do ASVS está definido e os identificadores citam a versão.
- [ ] Ameaças não prevenidas têm requisitos de detecção testáveis.
- [ ] A rastreabilidade até o teste está mantida.

## Questões de compreensão

**1.** Por que "eliminar" é frequentemente a melhor resposta a uma ameaça?

??? success "Resposta comentada"

    Porque remove a causa — o dado, o fluxo ou a funcionalidade — em vez de acrescentar controles que custam, falham e precisam ser mantidos. Também aplica o princípio de minimização.

**2.** O que torna um requisito de segurança verificável?

??? success "Resposta comentada"

    Descrever um resultado observável, com parâmetros concretos, de forma que um terceiro consiga testar se foi atendido sem consultar o autor.

**3.** Como o ASVS e o threat model se complementam?

??? success "Resposta comentada"

    O ASVS fornece uma base de requisitos verificáveis para problemas comuns, no nível adequado ao sistema. O threat model acrescenta requisitos específicos (lógica de negócio, integrações, cenários de ataque) e prioriza o que importa naquele sistema.

## Exercício de tomada de decisão

!!! question "Cenário: requisitos para a alteração bancária da Meridiana"

    A partir da árvore de ataque e do abuse case AC-03 da Aula 03, escreva três requisitos verificáveis para o fluxo de alteração de dados bancários de fornecedores, com critério de aceite, e indique uma ameaça que você aceitaria. Antes de escrever, escolha a estratégia com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho) entre: (A) apenas dupla aprovação interna; (B) confirmação por canal cadastrado, dupla aprovação e período de carência; (C) bloquear a alteração pelo portal e exigir solicitação formal com firma reconhecida.

??? success "Resolução de referência"

    | Critério | Peso | A — Só dupla aprovação | B — Confirmação + dupla aprovação + carência | C — Solicitação formal fora do portal |
    |:---|:---|:---|:---|:---|
    | Interrompe o caminho mais barato (e-mail falso do fornecedor) | 3 | 1 | 3 | 3 |
    | Verificável por testes automatizados | 2 | 3 | 3 | 1 |
    | Atrito para o fornecedor legítimo (3 = menor) | 2 | 3 | 2 | 1 |
    | Custo operacional (3 = menor) | 1 | 3 | 2 | 1 |
    | **Total ponderado** | | **18** | **21** | **14** |

    **Pesos:** interromper o caminho mais barato recebe 3, porque é o resultado que a árvore mostrou ser decisivo; verificabilidade e atrito recebem 2; custo operacional recebe 1. A dupla aprovação sozinha (A) não detém o e-mail falso: os dois aprovadores confiam no mesmo pedido. **Recomendação: B**, traduzida nos requisitos abaixo.

    - **SR-21 — Confirmação por canal cadastrado:** "Alterações de dados bancários só são efetivadas após confirmação pelo contato do fornecedor cadastrado antes da solicitação, por canal diferente do que originou o pedido." *Aceite:* pedido recebido por e-mail e confirmado pelo mesmo e-mail é recusado pelo sistema.
    - **SR-22 — Dupla aprovação:** "Alterações bancárias exigem aprovação de dois usuários distintos, sendo um deles de perfil diferente do solicitante." *Aceite:* segunda aprovação pelo mesmo usuário ou pelo mesmo perfil é bloqueada.
    - **SR-23 — Notificação e período de carência:** "Após a alteração, o fornecedor é notificado nos contatos antigo e novo, e pagamentos para a nova conta só ocorrem após 48 horas." *Aceite:* pagamento agendado dentro do período é retido e gera alerta.
    - **Ameaça aceita (risco residual):** fornecedor legítimo com e-mail comprometido que confirme a fraude pelo canal cadastrado — mitigada parcialmente pelo período de carência e pela notificação; residual aceito pelo diretor financeiro, com revisão semestral.
    - **O que mudaria a decisão:** perdas recorrentes mesmo com B, ou fornecedores de alto valor com histórico de fraude, justificariam C para esse grupo — com o custo de atrito assumido explicitamente.

## Pontos-chave

- Cada ameaça precisa de decisão: mitigar, eliminar, transferir ou aceitar.
- Requisitos verificáveis descrevem resultado e parâmetros testáveis.
- O ASVS 5.0 é uma base de requisitos em três níveis cumulativos; cite a versão.
- O threat model acrescenta requisitos de negócio, integração, detecção e resiliência.
- A rastreabilidade termina em um teste — a resposta à pergunta "fizemos um bom trabalho?".

## Referências

### Fundamentação principal

- OWASP. *Application Security Verification Standard 5.0.0*. 2025. <https://owasp.org/www-project-ASVS/> e <https://asvs.owasp.org/> — versão estável, data de publicação (30/05/2025), licença e formato dos identificadores conferidos no site oficial; estrutura de capítulos e uso típico dos níveis conferidos em fonte secundária (<https://quality.arc42.org/standards/owasp-asvs>).
- *Threat Modeling Manifesto* — perguntas "o que vamos fazer a respeito?" e "fizemos um bom trabalho?".
- NIST. *SP 800-160 Vol. 1 Rev. 1* — §3.2, determinação de segurança adequada baseada em evidências.

### Leitura complementar

- MITRE. *CAPEC* — mitigações sugeridas por padrão de ataque.
- NIST. *SP 800-53 Rev. 5* — controles organizacionais para requisitos que vão além da aplicação.
- SABSA. *White Paper W100* — rastreabilidade de requisitos de negócio a mecanismos.

### Aplicação prática

- Pegue cinco ameaças do threat model que você fez na Aula 02 e escreva para cada uma a decisão de tratamento e, quando for mitigar, um requisito verificável com critério de aceite e referência ao ASVS quando houver.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
