---
id: M01-L01
title: "Aula 01 — Propriedades de segurança: CIA, autenticidade, autorização e não repúdio"
public_title: "Módulo 1 — Aula 01 — Propriedades de segurança: CIA, autenticidade, autorização e não repúdio"
description: O que significa proteger informação — confidencialidade, integridade, disponibilidade, autenticidade, autorização, não repúdio e responsabilização — e como expressar requisitos de segurança em termos dessas propriedades.
domain: security-foundations
tier: fundamental
status: published
prerequisites: [M00-L07]
objectives:
  - Definir confidencialidade, integridade e disponibilidade e distinguir confidencialidade de sigilo e de privacidade.
  - Diferenciar autenticação, autorização, não repúdio e responsabilização.
  - Relacionar cada propriedade aos mecanismos que a realizam.
  - Escrever requisitos de segurança indicando qual propriedade cada um protege.
minutes: 60
sources: [BOOK-ANDERSON-SE3, NIST-SP800-160-V1R1]
further_reading: [SALTZER-SCHROEDER-1975]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M01
---

# Aula 01 — Propriedades de segurança: CIA, autenticidade, autorização e não repúdio { #propriedades-de-seguranca-cia-autenticidade-autorizacao-e-nao-repudio }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 1 · Nível 0</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min · ID técnico: M01-L01</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    "Seguro" não é um requisito — é um adjetivo. Para projetar e avaliar um sistema, é preciso dizer **seguro em relação a quê**: que a informação não seja lida por quem não deve, não seja alterada sem controle, esteja disponível quando necessária, venha de quem diz vir, só seja usada por quem tem autorização e deixe rastro de quem fez o quê. Esta aula define essas propriedades com precisão e mostra como usá-las para transformar pedidos vagos em requisitos verificáveis.

**Pré-requisitos:** [Lendo diagramas arquiteturais](../00-foundations/07-reading-architecture-diagrams.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Definir confidencialidade, integridade e disponibilidade e distinguir confidencialidade de sigilo e de privacidade.
- Diferenciar autenticação, autorização, não repúdio e responsabilização.
- Relacionar cada propriedade aos mecanismos que a realizam.
- Escrever requisitos de segurança indicando qual propriedade cada um protege.

## Conceito

### A tríade CIA

A forma mais difundida de organizar os objetivos de segurança é a tríade **CIA**:

| Propriedade | Pergunta que responde | Exemplo de violação |
|:---|:---|:---|
| **Confidencialidade** | Quem pode **ler**? | Lista de clientes exposta em um bucket público |
| **Integridade** | Quem pode **alterar**, e como saberemos se algo foi alterado? | Conta bancária de pagamento trocada em um cadastro de fornecedor |
| **Disponibilidade** | O sistema e os dados estarão **acessíveis quando necessário**? | ERP cifrado por ransomware |

A tríade é útil, mas incompleta. Muitos incidentes graves não se encaixam bem nela: um pagamento autorizado por quem não tinha alçada, uma alteração que ninguém consegue atribuir a uma pessoa. Por isso arquitetos trabalham com um conjunto maior de propriedades.

### Confidencialidade, sigilo e privacidade

Anderson faz uma distinção útil (*Security Engineering*, Cap. 1, §1.7, p. 11): **sigilo** é um conceito técnico de mecanismo — restringir o acesso a uma informação; **confidencialidade** é a obrigação de proteger segredos de outras pessoas, que você conhece por causa de uma relação (o banco e o cliente, o hospital e o paciente); **privacidade** é o direito de um indivíduo de controlar informações sobre si mesmo. A diferença importa para arquitetos porque leis de proteção de dados, como a LGPD, tratam de privacidade — e exigem mais do que cifrar: exigem finalidade, minimização e direitos do titular, temas do Módulo 13.

### Além da tríade

| Propriedade | Definição | Mecanismos típicos |
|:---|:---|:---|
| **Autenticidade** | A entidade ou a mensagem é quem/o que diz ser | Autenticação de usuários e dispositivos; MAC e assinatura de mensagens |
| **Autorização** | A entidade autenticada só faz o que lhe foi permitido | Políticas de acesso (RBAC, ABAC), verificação a cada operação |
| **Não repúdio** | Quem realizou uma ação não consegue negá-la de forma plausível | Assinatura digital com chave sob controle exclusivo do autor; registros protegidos |
| **Responsabilização** (*accountability*) | É possível atribuir cada ação a uma entidade individual | Identidades individuais (sem contas compartilhadas) e trilhas de auditoria |

**Autenticação não é autorização.** Saber que é a Maria (autenticação) não diz se a Maria pode aprovar um pagamento de R$ 500 mil (autorização). Uma das falhas mais comuns em APIs é justamente autenticar o usuário e deixar de verificar se ele pode acessar **aquele** objeto específico.

**Não repúdio exige mais do que um log.** Um registro de que "o usuário maria aprovou" pode ser contestado se administradores podem editar o log ou se a senha da Maria é conhecida por outros. Não repúdio forte depende de uma credencial que só o autor controla — tipicamente uma chave privada — e de registros que nem administradores conseguem alterar sem deixar rastro.

## Fundamentos técnicos

### Propriedades e mecanismos

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m01-l01-properties.mmd"
```

<figcaption>Figura 1 — Propriedades de segurança e mecanismos típicos que as realizam.</figcaption>
</figure>

A relação não é de um para um: a criptografia serve a confidencialidade, integridade e autenticidade; registros de auditoria servem a responsabilização e ao não repúdio. O que importa é que **cada mecanismo seja escolhido por causa de uma propriedade**, e não por hábito.

### Do pedido à decisão

As propriedades de autenticidade, autorização e responsabilização aparecem em sequência em quase toda operação sensível. Separar as etapas evita o erro de achar que "o usuário está logado" responde à pergunta "ele pode fazer isso?":

1. **Identificação** — a entidade declara quem é (um nome de usuário, um identificador de dispositivo).
2. **Autenticação** — a declaração é comprovada por um ou mais fatores (algo que sabe, tem ou é).
3. **Autorização** — uma política decide se **aquela** identidade pode executar **aquela** ação sobre **aquele** objeto, no contexto atual.
4. **Registro** — a decisão e a ação ficam registradas de forma que permita atribuí-las à identidade (responsabilização).

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m01-l01-aaa-flow.mmd"
```

<figcaption>Figura 2 — A Maria é identificada e autenticada pelo provedor de identidade, mas a política de autorização nega a aprovação acima do seu limite; a tentativa fica registrada.</figcaption>
</figure>

Repare que o provedor de identidade não sabe nada sobre limites de aprovação: ele responde **quem é**. A decisão **pode ou não pode** está em outro componente, alimentado por regras de negócio. Os módulos Módulo 6 (identidade e acesso) e Módulo 7 (Zero Trust) aprofundam cada etapa.

### Propriedades conflitam

Propriedades competem entre si e com o negócio:

- **Confidencialidade × disponibilidade:** cifrar dados com uma chave que só uma pessoa conhece protege a confidencialidade, mas a disponibilidade depende dessa pessoa.
- **Integridade × disponibilidade:** bloquear uma transação que falha numa verificação de integridade interrompe o negócio.
- **Responsabilização × privacidade:** registrar tudo o que cada pessoa faz serve à auditoria, mas é tratamento de dados pessoais.

A SP 800-160 Vol. 1 Rev. 1 trata isso com o conceito de sistema **adequadamente seguro** (§3.2): o nível aceitável de segurança é específico das necessidades das partes interessadas e depende do contexto; um sistema é adequadamente seguro quando atende a níveis mínimos toleráveis e é *as secure as reasonably practicable* (ASARP) — isto é, melhorias adicionais custariam desproporcionalmente em custo, prazo ou desempenho. E essa conclusão exige **evidência**. É por isso que requisitos precisam dizer **qual propriedade**, **em que grau** e **como será verificada**.

### Requisitos expressos por propriedade

| Pedido vago | Requisito com propriedade explícita |
|:---|:---|
| "Os dados do cliente devem estar seguros" | **Confidencialidade:** apenas o próprio cliente e atendentes do seu atendimento leem os dados; dados cifrados em repouso. |
| "O cadastro de fornecedores precisa ser confiável" | **Integridade e autorização:** alteração de conta bancária exige aprovação de uma segunda pessoa; toda alteração é registrada. |
| "O sistema não pode parar" | **Disponibilidade:** RTO de 2 horas e RPO de 15 minutos. |
| "Precisamos saber quem aprovou" | **Não repúdio e responsabilização:** aprovações assinadas com credencial individual; registros imutáveis por 5 anos. |

## Exemplo empresarial

!!! example "Meridiana — a fraude do cadastro de fornecedores"

    Um e-mail falso, aparentemente de um fornecedor, pediu a troca da conta bancária para pagamentos. Um analista do financeiro fez a alteração no ERP; no mês seguinte, R$ 380 mil foram pagos a uma conta de golpistas.

    A análise por propriedades mostrou onde a arquitetura falhou:

    | Propriedade | O que aconteceu | Controle ausente |
    |:---|:---|:---|
    | Autenticidade (da mensagem) | O pedido não foi verificado por um canal independente | Confirmação por telefone cadastrado previamente |
    | Integridade (do cadastro) | Um único analista alterou dado crítico | Dupla aprovação para dados bancários |
    | Responsabilização | O ERP usava uma conta compartilhada no financeiro | Contas individuais |
    | Detecção | Ninguém foi alertado da alteração | Alerta ao fornecedor e ao gestor em toda troca de conta |

    Nenhum firewall ou antivírus teria evitado esse incidente. Ele foi uma falha de **integridade e autenticidade** num processo de negócio — e a solução foi arquitetural.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Requisitos | "O sistema deve ser seguro" | Requisitos por propriedade, com grau e forma de verificação |
| Foco | Confidencialidade (cifrar tudo) | Todas as propriedades proporcionalmente ao impacto |
| Identidade | Contas compartilhadas por área | Contas individuais; responsabilização possível |
| Autorização | Verificada só no login | Verificada a cada operação e objeto |
| Registros | Logs editáveis por administradores | Registros protegidos contra alteração e centralizados |

## Aplicabilidade: on-premises, cloud e híbrido

As propriedades são as mesmas em qualquer ambiente; mudam os mecanismos e quem os opera. Em cloud, por exemplo, a disponibilidade da infraestrutura é do provedor, mas a disponibilidade **dos seus dados** depende das escolhas de backup e redundância que você fizer; a confidencialidade depende de configuração de acesso que é sempre sua.

## Como especificar e implementar

- Cada requisito de segurança indica a propriedade protegida, o grau esperado e a forma de verificação.
- Dados e transações críticos são classificados quanto a confidencialidade, integridade e disponibilidade (C, I e A), o que orienta a escolha dos controles.
- Operações de alto impacto têm requisitos explícitos de autorização e responsabilização.

## Trade-offs, limitações e antipadrões

- **Antipadrão — "cifrar resolve":** cifragem protege confidencialidade em repouso, mas não impede um usuário autorizado de alterar um dado indevidamente.
- **Antipadrão — confundir autenticação com autorização.**
- **Limitação:** propriedades descrevem objetivos, não ameaças — combinam-se com a análise de ameaças (Módulo 4).

## Como validar

- Para cada requisito de segurança, perguntar: que propriedade protege? Como saberemos que foi atendido?
- Em revisões, testar autorização por objeto (um usuário consegue acessar dados de outro?).
- Verificar se ações críticas podem ser atribuídas a uma pessoa e se os registros resistem a alterações.

## Como apresentar e justificar

- **Para engenharia:** "A troca de conta bancária é um problema de integridade: precisamos de dupla aprovação e alerta, não de mais criptografia."
- **Para gestores:** "Vamos garantir que nenhuma pessoa sozinha consiga desviar um pagamento, e que toda alteração tenha autor identificado."

## Checklist de revisão arquitetural

- [ ] Os dados e transações críticos têm classificação de C, I e A.
- [ ] Cada requisito de segurança indica a propriedade protegida e como será verificado.
- [ ] A autorização é verificada por operação e por objeto, não apenas no login.
- [ ] Não há contas compartilhadas em operações críticas.
- [ ] Registros de ações críticas são protegidos contra alteração.

## Questões de compreensão

**1.** Um usuário autenticado consegue ver os pedidos de outros clientes trocando o número do pedido na URL. Qual propriedade foi violada e qual mecanismo falhou?

??? success "Resposta comentada"

    Confidencialidade, por falha de **autorização**: o sistema autenticou o usuário, mas não verificou se ele tinha permissão para acessar aquele pedido específico.

**2.** Por que um registro de log editável por administradores não garante não repúdio?

??? success "Resposta comentada"

    Porque o autor da ação pode alegar que o registro foi alterado ou criado por outra pessoa. Não repúdio exige uma credencial sob controle exclusivo do autor e registros protegidos contra alteração.

**3.** Diferencie confidencialidade de privacidade.

??? success "Resposta comentada"

    Confidencialidade é a obrigação de proteger informações de terceiros que se conhece por causa de uma relação; privacidade é o direito do indivíduo de controlar informações sobre si mesmo. Leis de proteção de dados tratam da privacidade e exigem mais do que proteção contra leitura indevida — por exemplo, finalidade e minimização.

## Exercício de tomada de decisão

!!! question "Cenário: aprovação de pagamentos na Aurora"

    A Aurora quer que pagamentos acima de R$ 100 mil sejam aprovados por dois diretores. Hoje, a aprovação é um clique no sistema após login com senha. Que propriedades estão em jogo? Compare (A) manter o login com senha e exigir um segundo clique de outro diretor; (B) dupla aprovação com MFA resistente a phishing, bloqueio de autoaprovação e registro imutável; (C) a alternativa B mais assinatura digital de cada aprovação com certificado individual em token, pelos critérios autenticidade e não repúdio, correção da autorização e usabilidade e custo.

??? success "Resolução de referência"

    | Critério | Peso | A — Senha e segundo clique | B — MFA, segregação e registro imutável | C — B com assinatura digital |
    |:---|:---|:---|:---|:---|
    | Autenticidade e não repúdio | 3 | 1 | 2 | 3 |
    | Correção da autorização (duas pessoas distintas, com alçada) | 3 | 2 | 3 | 3 |
    | Usabilidade e custo | 2 | 3 | 2 | 1 |
    | **Total ponderado** | | **15** | **19** | **20** |

    **Recomendação: C, por margem pequena.** A diferença entre B e C está no não repúdio: com assinatura individual, o diretor não consegue sustentar que a aprovação foi feita por outra pessoa com acesso à sua sessão. Se a Aurora não tiver infraestrutura de certificados, B é aceitável como primeira etapa, com C planejada.

    - **Autorização:** a política precisa exigir dois aprovadores distintos, com alçada adequada, e impedir que o solicitante aprove o próprio pagamento.
    - **Autenticidade e não repúdio:** login com senha é insuficiente; recomendar autenticação forte (MFA resistente a phishing) e, para o nível mais alto, assinatura da aprovação com credencial individual.
    - **Responsabilização:** registros imutáveis de quem solicitou, quem aprovou, quando e de onde.
    - **Integridade:** os dados do pagamento aprovados não podem ser alterados depois da aprovação sem reiniciar o fluxo.

    O ponto central é que **a política de dupla aprovação só tem valor se a identidade de cada aprovador for confiável e o registro for incontestável**.

## Pontos-chave

- "Seguro" não é requisito: diga qual propriedade, em que grau e como será verificado.
- A tríade CIA é a base, mas autenticidade, autorização, não repúdio e responsabilização são igualmente necessárias.
- Autenticação diz quem é; autorização diz o que pode fazer.
- Propriedades conflitam entre si e com o negócio; o objetivo é segurança adequada, não máxima.
- Muitos incidentes graves são falhas de integridade e autorização em processos de negócio.

## Referências

### Fundamentação principal

- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020. Cap. 1, §1.7 *Definitions* (p. 11) — distinção entre sigilo, confidencialidade e privacidade; *trusted* versus *trustworthy*. Cap. 12, §12.2.4 *Designing internal controls* (p. 411) — dupla custódia e separação de funções em processos financeiros.
- NIST. *SP 800-160 Vol. 1 Rev. 1*. 2022. §3.2 *The Concept of an Adequately Secure System* (p. 13) — segurança adequada como específica das partes interessadas, níveis mínimos toleráveis, ASARP e decisão baseada em evidência. <https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final>

### Leitura complementar

- J. Saltzer e M. Schroeder. *The Protection of Information in Computer Systems*. Proceedings of the IEEE, 63(9), 1975 — artigo clássico que organizou os objetivos e princípios de proteção. *(Dados bibliográficos conferidos em fonte secundária.)*

### Aplicação prática

- Use a tabela "pedido vago → requisito com propriedade" na revisão de qualquer documento de requisitos; ela é retomada na [Aula 07 do Módulo 2](../02-security-architecture/07-business-driven-requirements.md).
- O experimento `authz` do [Laboratório 01](../../labs/lab-01-security-mechanisms.md) reproduz o exemplo da Maria: autenticada, com o papel certo, e ainda assim sem autorização para aquele pagamento.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
