---
id: M06-L05
title: "Aula 05 — Identidade híbrida: Active Directory, Microsoft Entra ID e provedores cloud"
public_title: "Módulo 6 — Aula 05 — Identidade híbrida: Active Directory, Microsoft Entra ID e provedores cloud"
description: Como ligar o Active Directory a um provedor de identidade em nuvem — sincronização, sincronização de hash de senha, autenticação de passagem e federação —, os riscos que a ligação cria entre ambientes, a resiliência de cada opção e como estender a identidade corporativa às nuvens AWS e Google Cloud.
domain: iam
tier: architect
status: published
prerequisites: [M06-L03, M06-L04]
objectives:
  - Comparar sincronização de hash de senha, autenticação de passagem e federação por dependência e resiliência.
  - Identificar os componentes de identidade híbrida que pertencem ao plano de controle.
  - Projetar a extensão da identidade corporativa a múltiplas nuvens sem criar identidades locais paralelas.
  - Avaliar o risco de propagação de comprometimento entre on-premises e nuvem.
minutes: 90
sources: [MS-ENTRA-HYBRID-AUTHN, MS-ENTERPRISE-ACCESS-MODEL, NIST-SP800-63-4, MITRE-ATTACK, NIST-SP800-53]
further_reading: [AZURE-SECURITY-ARCH-PTBR, GCP-ENTERPRISE-FOUNDATIONS, AWS-SRA, MS-AD-FOREST-RECOVERY]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M06
---

# Aula 05 — Identidade híbrida: Active Directory, Microsoft Entra ID e provedores cloud { #identidade-hibrida-active-directory-microsoft-entra-id-e-provedores-cloud }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 6 · Nível 2</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">90 min · ID técnico: M06-L05</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Uma organização com histórico on-premises raramente tem só "identidade em nuvem" ou só "identidade on-premises": tem as duas, ligadas. O Active Directory costuma continuar sendo a fonte de contas e grupos, e um provedor de identidade em nuvem — no ecossistema Microsoft, o **Microsoft Entra ID** — autentica o acesso a SaaS e às nuvens. Essa ligação traz usabilidade e controle, mas cria **um único plano de controle que atravessa ambientes**. Esta aula compara as opções de autenticação híbrida, aponta os ativos críticos e mostra como estender a identidade a múltiplas nuvens.

**Pré-requisitos:** [AD, LDAP e Kerberos](03-directories-kerberos.md) e [Federação](04-federation-saml-oauth-oidc.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Comparar sincronização de hash de senha, autenticação de passagem e federação por dependência e resiliência.
- Identificar os componentes de identidade híbrida que pertencem ao plano de controle.
- Projetar a extensão da identidade corporativa a múltiplas nuvens sem criar identidades locais paralelas.
- Avaliar o risco de propagação de comprometimento entre on-premises e nuvem.

## Conceito

### Três formas de autenticar em nuvem com contas do AD

A documentação da Microsoft descreve três métodos:

| Método | Onde a senha é validada | Infraestrutura local adicional |
|:---|:---|:---|
| **Password hash synchronization (PHS)** | Na nuvem, a partir de hashes sincronizados | Apenas o servidor de sincronização |
| **Pass-through authentication (PTA)** | No AD, por agentes locais | Um ou mais agentes leves (a Microsoft recomenda três) |
| **Federação** (por exemplo, AD FS) | No servidor de federação local | Dois ou mais servidores AD FS, dois ou mais proxies (WAP) na DMZ, balanceamento e certificado TLS |

A recomendação da Microsoft é **habilitar a sincronização de hash de senha em qualquer cenário** — como contingência quando a infraestrutura local falha (a troca para PHS não é automática: é feita manualmente, e só funciona se o PHS foi configurado antes da falha) e porque o relatório de usuários com credenciais vazadas do Entra ID Protection exige PHS. O documento registra que organizações que já tinham PHS habilitado, em indisponibilidades por ransomware, trocaram o método principal e voltaram a operar em questão de horas; as que não tinham levaram semanas para restaurar a identidade local antes que os usuários voltassem a entrar em aplicações em nuvem.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m06-l05-hybrid.mmd"
```

<figcaption>Figura 1 — O servidor de sincronização leva contas, grupos e hashes ao IdP em nuvem; PTA e federação fazem o login em nuvem depender do ambiente local.</figcaption>
</figure>

### Resiliência comparada

| Situação | PHS | PTA | Federação |
|:---|:---|:---|:---|
| Ambiente local indisponível | Login em nuvem continua | Login falha | Login falha |
| Ransomware no datacenter | SaaS e nuvem continuam acessíveis | Indisponíveis até a troca manual | Indisponíveis até a troca manual |
| Estados de conta do AD aplicados no login em nuvem | Só conta desabilitada, com até 30 minutos de atraso; bloqueio, expiração da conta, senha expirada e horário de logon não são aplicados | Todos, no momento do login | Todos, no momento do login |
| Infraestrutura exposta à internet | Nenhuma adicional | Nenhuma de entrada | Proxies de federação na DMZ |

## Fundamentos técnicos

### O que pertence ao plano de controle

Na identidade híbrida, o plano de controle (Aula 01) inclui:

- **Controladores de domínio** e a conta krbtgt.
- **Servidor de sincronização** — tem privilégios no AD e no IdP em nuvem; quem o controla pode alterar identidades nos dois lados.
- **Servidores de federação** e suas chaves de assinatura de tokens — quem obtém o certificado de assinatura pode forjar tokens SAML com quaisquer declarações de permissão (ATT&CK v20, T1606.002 *Forge Web Credentials: SAML Tokens*).
- **Agentes de PTA**.
- **Contas administrativas do IdP em nuvem**.

Esses componentes devem ser administrados apenas a partir de estações de acesso privilegiado, por contas do plano de controle, e monitorados como DCs.

### Propagação de comprometimento

| Direção | Caminho | Mitigação |
|:---|:---|:---|
| On-premises → nuvem | Comprometimento do AD altera grupos sincronizados que têm papéis na nuvem; roubo da chave de federação | Contas administrativas da nuvem **somente em nuvem**, não sincronizadas; grupos privilegiados da nuvem não derivados do AD; proteção da chave de federação ou migração para PHS |
| Nuvem → on-premises | Recursos de escrita de volta (*writeback*) e agentes com privilégios locais | Habilitar writeback só quando necessário, com escopo mínimo; monitorar alterações |

A regra mais eficaz é simples: **contas administrativas do IdP em nuvem não são sincronizadas do AD** e usam autenticação resistente a phishing — assim, um domínio comprometido não se converte automaticamente em controle da nuvem.

### Estendendo a identidade a múltiplas nuvens

Usuários não deveriam ter contas locais em cada nuvem. O padrão é federar os consoles e APIs de cada provedor com o IdP corporativo:

| Nuvem | Padrão | Observação |
|:---|:---|:---|
| Azure | Nativo ao Entra ID | Papéis atribuídos a grupos, com ativação just-in-time para privilegiados |
| AWS | Federação do IdP com o serviço de identidade centralizado da organização AWS | Permissões por conjuntos de papéis; aprofundado no Módulo 9 |
| Google Cloud | Federação do IdP com o Cloud Identity | Grupos sincronizados; aprofundado no Módulo 10 |

Os detalhes de cada provedor estão nos Módulos 9 e 10; o princípio arquitetural é **um IdP de força de trabalho, grupos governados, papéis por nuvem**.

## Exemplo empresarial

!!! example "Meridiana — a decisão que encurtou a indisponibilidade"

    A Meridiana usava autenticação de passagem com dois agentes em servidores do datacenter. Na análise do cenário RSK-007, o arquiteto mostrou que, com o datacenter cifrado, os agentes cairiam e ninguém conseguiria acessar o e-mail e o SaaS de RH — inclusive a equipe de resposta.

    Decisões:

    1. Habilitar **PHS** como método principal, mantendo os agentes de PTA desligados.
    2. Criar **contas administrativas do Entra ID somente em nuvem**, com chaves de segurança FIDO2, e remover papéis administrativos de contas sincronizadas.
    3. Tratar o **servidor de sincronização como plano de controle**: zona de gestão, administração por estação dedicada, monitoração.
    4. Registrar em ADR a troca do método de autenticação e o risco aceito: hashes de senha passam a residir no IdP em nuvem.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Método de autenticação | Federação por padrão | PHS habilitado em qualquer cenário; federação só com justificativa |
| Administradores da nuvem | Contas sincronizadas do AD | Contas somente em nuvem, com autenticação resistente a phishing |
| Servidor de sincronização | "Mais um servidor" | Ativo do plano de controle |
| Múltiplas nuvens | Contas locais em cada uma | Federação com o IdP; grupos governados |
| Writeback | Habilitado por conveniência | Escopo mínimo e monitorado |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referências voluntárias, e a técnica do MITRE ATT&CK que motiva a proteção da chave de federação:

| Controle ou padrão | Objetivo na identidade híbrida | Referência |
|:---|:---|:---|
| Contas privilegiadas separadas | Administradores da nuvem em contas próprias, com atribuições monitoradas e revogadas quando inadequadas | SP 800-53: AC-2(7) (Privileged User Accounts) e AC-6(5) (Privileged Accounts) |
| MFA para contas privilegiadas | Autenticação multifator — resistente a phishing — para administradores do IdP | SP 800-53: IA-2(1); SP 800-63B-4 (AAL3) |
| Chave de assinatura de tokens | Estabelecer e gerenciar as chaves que assinam tokens de federação | SP 800-53: SC-12 (Cryptographic Key Establishment and Management) |
| Contingência da autenticação | Plano de contingência com a troca do método de autenticação e o tempo de recuperação | SP 800-53: CP-2 (Contingency Plan) |
| Funcionalidade mínima | Writeback e agentes só com as funções necessárias | SP 800-53: CM-7 (Least Functionality) |
| Ameaça de referência | Forja de tokens SAML com o certificado de assinatura | MITRE ATT&CK v20: T1606.002 |
| Planos de controle, gestão e dados | Sincronização, federação e agentes administrados como plano de controle | Microsoft, modelo de acesso corporativo |

## Aplicabilidade: on-premises, cloud e híbrido

Esta aula trata, por definição, do cenário híbrido. Organizações que nasceram em nuvem podem dispensar o AD para usuários, mas costumam mantê-lo para servidores Windows legados. Organizações on-premises que adotam SaaS passam a ser híbridas no primeiro dia — e a decisão de método de autenticação deveria ser tomada como decisão de arquitetura, não de instalação.

## Como especificar e implementar

- "A sincronização de hash de senha está habilitada, mesmo quando outro método é o principal."
- "Contas com papéis administrativos no IdP em nuvem são somente em nuvem e usam autenticação resistente a phishing."
- "Servidores de sincronização, federação e agentes de autenticação são administrados como ativos do plano de controle."
- "Consoles e APIs de todas as nuvens são federados com o IdP corporativo; contas locais são exceção de emergência."
- "Recursos de writeback só são habilitados com justificativa e escopo mínimo."

## Trade-offs, limitações e antipadrões

- **Trade-off — PHS:** hashes de senha passam a existir no IdP em nuvem, e o login em nuvem não aplica bloqueio, expiração nem horário de logon do AD (a documentação da Microsoft lista só contas desabilitadas, com até 30 minutos de atraso); em troca, ganha-se resiliência e detecção de credenciais vazadas.
- **Trade-off — federação:** controle total da autenticação local, ao custo de infraestrutura exposta, chaves de assinatura críticas e dependência do datacenter.
- **Antipadrão — administrador global sincronizado:** comprometer o AD significa comprometer a nuvem.
- **Limitação:** esta aula usa o ecossistema Microsoft como exemplo por ser comum no Brasil; outros IdPs têm mecanismos equivalentes com nomes diferentes.

## Como validar

- Simular indisponibilidade do datacenter em exercício e verificar o acesso a SaaS e nuvens.
- Listar contas com papéis administrativos na nuvem e verificar se alguma é sincronizada.
- Verificar quem pode administrar o servidor de sincronização e de onde.
- Conferir se há contas locais nos consoles de nuvem além das de emergência.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| PHS habilitado, mesmo com outro método principal | Configuração da sincronização |
| Troca do método de autenticação exercitada, com tempo medido | Registro do exercício de indisponibilidade do datacenter, dentro do tempo-alvo do plano de contingência |
| Nenhuma conta com papel administrativo na nuvem sincronizada do AD | Relatório de papéis privilegiados com a origem de cada conta |
| Administradores da nuvem com autenticação resistente a phishing | Relatório de métodos de autenticação |
| Servidor de sincronização administrado só a partir da zona de gestão | Regras de acesso e eventos de logon do servidor |

## Como apresentar e justificar

- **Para a diretoria:** "Se o datacenter for cifrado, hoje perdemos também o e-mail e os sistemas em nuvem. Com uma configuração, eles continuam funcionando."
- **Para a equipe de identidade:** "O servidor de sincronização é tão crítico quanto um controlador de domínio. Tratem-no assim."

## Checklist de revisão arquitetural

- [ ] O método de autenticação foi decidido e registrado em ADR.
- [ ] PHS habilitado como contingência.
- [ ] Administradores da nuvem somente em nuvem, com autenticação resistente a phishing.
- [ ] Componentes de identidade híbrida tratados como plano de controle.
- [ ] Todas as nuvens federadas com o IdP.
- [ ] Writeback com escopo mínimo.

## Questões de compreensão

**1.** Por que a Microsoft recomenda habilitar a sincronização de hash de senha mesmo quando o método principal é outro?

??? success "Resposta comentada"

    Porque permite manter o login em nuvem quando a infraestrutura local falha — a troca é manual — e habilita a detecção de credenciais vazadas. A documentação registra recuperação em horas para quem tinha PHS em incidentes de ransomware.

**2.** Por que contas administrativas da nuvem não deveriam ser sincronizadas do AD?

??? success "Resposta comentada"

    Porque o comprometimento do AD permitiria alterar ou usar essas contas e, com isso, controlar a nuvem. Contas somente em nuvem quebram esse caminho de propagação.

**3.** Cite três componentes de identidade híbrida que pertencem ao plano de controle.

??? success "Resposta comentada"

    Controladores de domínio, servidor de sincronização, servidores de federação e suas chaves de assinatura, agentes de autenticação de passagem e contas administrativas do IdP em nuvem.

## Exercício de tomada de decisão

!!! question "Cenário: federação exigida por auditoria na Aurora"

    A Aurora usa federação com servidores locais porque, anos atrás, a auditoria exigiu que "senhas não saíssem da empresa". Hoje, a federação é o maior componente exposto na DMZ, e a chave de assinatura de tokens nunca foi rotacionada. As opções são:

    - **A** — manter a federação, endurecida: rotacionar a chave, protegê-la em HSM e monitorar a emissão de tokens;
    - **B** — migrar para PHS com MFA resistente a phishing no IdP em nuvem e desativar a federação após período de convivência;
    - **C** — migrar para PTA com três agentes, com PHS habilitado apenas como contingência.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e diga como apresentá-la à auditoria.

**Objetivos avaliados:** Comparar sincronização de hash de senha, autenticação de passagem e federação por dependência e resiliência; avaliar o risco de propagação de comprometimento entre on-premises e nuvem.

**Entrega esperada:** Matriz ponderada, recomendação com o período de convivência e o argumento à auditoria por escrito.

**Critérios de avaliação:**

- A comparação usa dependência do datacenter e infraestrutura exposta, não só preferência de produto.
- A transição protege a chave de assinatura enquanto a federação existir (rotação, HSM, monitoração).
- O argumento à auditoria compara riscos e registra o residual, como os estados de conta do AD que o PHS não aplica.

??? success "Resolução de referência"

    | Critério | Peso | A — Federação endurecida | B — PHS com MFA resistente a phishing | C — PTA com PHS de contingência |
    |:---|:---|:---|:---|:---|
    | Superfície exposta e risco de forja de tokens | 3 | 1 | 3 | 3 |
    | Login em nuvem com o datacenter indisponível | 3 | 1 | 3 | 2 |
    | Validação da senha no ambiente local (requisito original) | 2 | 3 | 1 | 2 |
    | Esforço de implantação e operação | 2 | 1 | 3 | 2 |
    | **Total ponderado** | | **14** | **26** | **23** |

    - **Pesos:** a federação exposta com chave nunca rotacionada é o risco que motivou a revisão, e a indisponibilidade do datacenter é o cenário de ransomware do setor (peso 3 para ambos). O requisito original da auditoria e o esforço pesam 2: o requisito precisa ser respondido, mas protegia contra um risco que hoje tem outros controles.
    - **Recomendação: B.** Remove a infraestrutura exposta e a chave que permite forjar tokens, e mantém o login em nuvem com o datacenter fora do ar. Enquanto a federação existir no período de convivência, rotacionar a chave de assinatura, protegê-la em HSM e monitorar a emissão de tokens — as medidas de A, como transição. A opção C é uma alternativa defensável se a auditoria mantiver a exigência de validação local, mas depende de troca manual em uma crise.
    - **Argumento à auditoria:** o requisito original ("senhas não saem da empresa") protegia contra um risco; hoje, a federação cria riscos maiores — infraestrutura exposta, chave que permite forjar tokens, dependência do datacenter. Com PHS, o que sai são hashes sincronizados, e a autenticação passa a exigir fator resistente a phishing, o que reduz o risco de comprometimento de contas.
    - **Trade-off aceito e risco residual:** hashes de senha passam a residir no IdP em nuvem, e o login em nuvem deixa de aplicar os estados de conta do AD — bloqueio, expiração, senha expirada e horário de logon; contas desabilitadas são refletidas com até 30 minutos de atraso, o que exige que desligamentos também revoguem as sessões no IdP (Aula 08); o residual é aceito pelo dono do risco em ADR, com riscos comparados.
    - **O que mudaria a decisão:** uma exigência regulatória ou contratual explícita de que a senha seja validada localmente elevaria esse critério a peso 3 e favoreceria C — assim como a necessidade de aplicar no login em nuvem o bloqueio de conta e o horário de logon do AD, que só PTA e federação aplicam; se a organização for adotar autenticação sem senha para todos os usuários, a discussão sobre onde a senha é validada perde peso, e B fica ainda mais forte.

    **Erros comuns:**

    - Manter a federação só porque um requisito antigo pediu, sem reavaliar o risco que ele tratava.
    - Esquecer que PHS reflete conta desabilitada com atraso, o que exige revogar sessões no desligamento.
    - Desativar a federação sem período de convivência e sem plano de reversão.

## Pontos-chave

- PHS, PTA e federação diferem em onde a senha é validada e em dependência do ambiente local.
- Habilite PHS como contingência; só PHS mantém o login em nuvem com o datacenter fora do ar.
- Sincronização, federação e agentes pertencem ao plano de controle.
- Administradores da nuvem devem ser contas somente em nuvem, com autenticação resistente a phishing.
- Estenda a identidade corporativa a todas as nuvens por federação, sem contas locais paralelas.

## Referências

### Fundamentação principal

- Microsoft. *Authentication for Microsoft Entra hybrid identity solutions*. Microsoft Learn, 2025. <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn>. *(Lido; recomendações e tabela comparativa reconferidas em 2026-10-29.)*
- Microsoft. *The enterprise access model*. *(Lido.)*
- NIST. *SP 800-63B-4* — autenticação resistente a phishing (AAL3). *(Lido.)*
- MITRE. *ATT&CK v20* — T1606.002 Forge Web Credentials: SAML Tokens. *(Página conferida.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-2(7), AC-6(5), IA-2(1), SC-12, CP-2 e CM-7, conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- Microsoft. *Arquitetura de segurança do Azure* (documentação em português).
- Google Cloud. *Enterprise foundations blueprint* — identidade e organização (Módulo 10).
- AWS. *Security Reference Architecture* — identidade em múltiplas contas (Módulo 9).
- Microsoft. *Active Directory Forest Recovery Guide* ([Aula 09](09-identity-recovery.md)).

### Aplicação prática

- Descubra qual método de autenticação híbrida sua organização usa, se PHS está habilitado e quais contas com papéis administrativos na nuvem são sincronizadas do AD.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
