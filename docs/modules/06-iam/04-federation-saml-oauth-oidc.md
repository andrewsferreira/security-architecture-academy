---
id: M06-L04
title: "Aula 04 — Federação: SAML 2.0, OAuth 2.0 e OpenID Connect"
public_title: "Módulo 6 — Aula 04 — Federação: SAML 2.0, OAuth 2.0 e OpenID Connect"
description: Como a confiança entre domínios de identidade funciona — SAML 2.0 para SSO corporativo, OAuth 2.0 para autorização delegada e OpenID Connect para autenticação sobre OAuth — e as decisões de segurança que separam uma federação robusta de uma porta de entrada para ataques.
domain: iam
tier: professional
status: published
prerequisites: [M06-L01, M01-L05]
objectives:
  - Explicar papéis, asserções e bindings do SAML 2.0 e os fluxos iniciados pelo SP e pelo IdP.
  - Diferenciar autenticação (OIDC) de autorização delegada (OAuth 2.0) e o papel de cada token.
  - Aplicar as práticas da RFC 9700 — obrigatórias (PKCE para clientes públicos, redirecionamento exato) e recomendadas (tokens restritos ao remetente e à audiência).
  - Escolher o protocolo adequado a cada cenário e especificar a validação de tokens e asserções.
minutes: 90
sources: [OASIS-SAML2-TECH-OVERVIEW, RFC-9700, OIDC-CORE-1, NIST-SP800-63-4, NIST-SP800-53]
further_reading: [OWASP-ASVS-5, GCP-WORKLOAD-IDENTITY-FED]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M06
---

# Aula 04 — Federação: SAML 2.0, OAuth 2.0 e OpenID Connect { #federacao-saml-20-oauth-20-e-openid-connect }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 6 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">90 min · ID técnico: M06-L04</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Federação permite que uma aplicação confie na autenticação feita por outro sistema — o IdP corporativo, um parceiro, um provedor de nuvem. Isso elimina senhas espalhadas por aplicações e concentra o controle no IdP, mas cria uma dependência: **a aplicação passa a confiar em asserções e tokens**, e qualquer falha em emiti-los, transportá-los ou validá-los vira acesso indevido. Esta aula apresenta os três protocolos que dominam o mercado e as práticas que os tornam seguros.

**Pré-requisitos:** [Disciplinas de identidade](01-identity-disciplines.md) e [PKI, TLS e gestão de chaves](../01-security-fundamentals/05-pki-tls-key-management.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar papéis, asserções e bindings do SAML 2.0 e os fluxos iniciados pelo SP e pelo IdP.
- Diferenciar autenticação (OIDC) de autorização delegada (OAuth 2.0) e o papel de cada token.
- Aplicar as práticas da RFC 9700 — obrigatórias (PKCE para clientes públicos, redirecionamento exato) e recomendadas (tokens restritos ao remetente e à audiência).
- Escolher o protocolo adequado a cada cenário e especificar a validação de tokens e asserções.

## Conceito

### Três protocolos, três propósitos

| Protocolo | Propósito | Artefato | Uso típico |
|:---|:---|:---|:---|
| **SAML 2.0** | SSO entre domínios, baseado em XML | Asserção assinada | Aplicações corporativas web e SaaS |
| **OAuth 2.0** | **Autorização delegada**: um cliente obtém acesso limitado a uma API em nome de alguém | Access token (e refresh token) | APIs, aplicações móveis, integrações |
| **OpenID Connect** | **Autenticação** sobre OAuth 2.0 | ID Token (JWT) | Login em aplicações web e móveis modernas |

Confundir OAuth com autenticação é um erro clássico: um access token diz que o portador pode chamar uma API, não necessariamente **quem** é o usuário nem que ele acabou de se autenticar. O **OpenID Connect** existe para isso: a especificação o define como uma camada de identidade sobre o protocolo OAuth 2.0 (*"identity layer on top of the OAuth 2.0 protocol"*), que permite ao cliente verificar a identidade do usuário com base na autenticação feita pelo servidor de autorização.

### SAML 2.0

A visão geral técnica da OASIS descreve os papéis de **identity provider (IdP)** e **service provider (SP)**, e o **sujeito** que a asserção descreve (Sec. 3.1). Uma asserção pode conter declarações de **autenticação**, de **atributos** e de **decisão de autorização**. **Bindings** definem como as mensagens trafegam — por exemplo, HTTP Redirect, HTTP POST e HTTP Artifact —, e o perfil **Web Browser SSO** combina protocolo e bindings para SSO com navegadores (Sec. 4.3).

Dois fluxos são possíveis (Sec. 3.2 e 5.1.1; exemplos nas Sec. 5.1.2 a 5.1.4):

- **Iniciado pelo SP:** o usuário acessa a aplicação, que o redireciona ao IdP com uma requisição de autenticação.
- **Iniciado pelo IdP:** o usuário, já autenticado no IdP, clica em um link e o IdP envia a asserção ao SP **sem requisição prévia** — o documento registra que nenhuma mensagem `<AuthnRequest>` do SP ao IdP está envolvida. Sem um pedido próprio para correlacionar, o SP precisa de cuidados adicionais contra repetição e injeção de asserções.

### OpenID Connect e o ID Token

O ID Token do OIDC traz, obrigatoriamente, `iss` (emissor), `sub` (identificador do sujeito, único e nunca reatribuído no emissor), `aud` (audiência, que deve incluir o `client_id` da aplicação), `exp` (expiração) e `iat` (emissão) (Sec. 2). Claims opcionais informam **como** o usuário se autenticou: `acr` (classe de contexto de autenticação), `amr` (métodos usados) e `auth_time` — este obrigatório quando a aplicação pede `max_age`. O `nonce` associa a sessão do cliente ao token e mitiga repetição; se foi enviado no pedido, a aplicação deve conferi-lo (Sec. 3.1.3.7). A especificação define três fluxos — **Authorization Code**, **Implicit** e **Hybrid** — conforme o `response_type`.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m06-l04-oidc-pkce.mmd"
```

<figcaption>Figura 1 — Authorization Code com PKCE e OIDC: o código volta ao endereço registrado exato; a troca exige o verificador; a aplicação valida o ID Token e chama a API com um access token restrito à audiência.</figcaption>
</figure>

## Fundamentos técnicos

### Práticas da RFC 9700 { #praticas-obrigatorias-da-rfc-9700 }

A RFC 9700 (BCP 240), de janeiro de 2025, atualiza o modelo de ameaças do OAuth 2.0. Na Sec. 2 (palavras normativas da RFC entre parênteses):

| Prática | Requisito |
|:---|:---|
| Redirecionamento | Servidores **devem** (MUST) comparar o URI de redirecionamento por correspondência exata de texto — a única exceção é a porta em URIs `localhost` (§2.1) |
| PKCE | Clientes públicos **devem** (MUST) usar PKCE e servidores **devem** (MUST) suportá-lo; para clientes confidenciais, é **recomendado** (RECOMMENDED) (§2.1.1) |
| Implicit grant | Clientes **não deveriam** (SHOULD NOT) usá-lo (§2.1.2) |
| Password grant | **Não deve** (MUST NOT) ser usado (§2.4) |
| Tokens restritos ao remetente | Servidores de autorização e de recurso **deveriam** (SHOULD) usar mecanismos como mTLS ou DPoP (§2.2.1) |
| Refresh tokens de clientes públicos | **Devem** (MUST) ser restritos ao remetente ou rotacionados (§2.2.2) |
| Audiência | Access tokens **deveriam** (SHOULD) ser restritos a um servidor de recurso específico (§2.3) |
| Autenticação de cliente | Servidores **deveriam** (SHOULD) exigi-la quando viável; **recomenda-se** (RECOMMENDED) criptografia assimétrica (§2.5) |
| Transporte | Respostas de autorização **não devem** (MUST NOT) trafegar em conexões não cifradas (§2.6) |

### Validação: onde a federação costuma falhar

| Validação | O que verificar | Falha típica |
|:---|:---|:---|
| **Assinatura** | Asserção ou token assinado com chave confiável do emissor | Aceitar token sem assinatura ou com algoritmo alterado |
| **Emissor** | `iss` / Issuer esperado | Aceitar tokens de qualquer locatário de um IdP multi-tenant |
| **Audiência** | `aud` / Audience inclui esta aplicação | Token emitido para outra aplicação aceito |
| **Validade** | `exp`, `iat`, NotBefore/NotOnOrAfter | Tokens expirados aceitos; relógios dessincronizados |
| **Repetição** | Identificador único, nonce, InResponseTo | Asserção capturada reutilizada |
| **Autorização** | Escopos e claims coerentes com a operação | Token de leitura usado para escrita |

### Escolhendo o protocolo

| Cenário | Recomendação |
|:---|:---|
| SaaS corporativo que só suporta SAML | SAML 2.0, iniciado pelo SP quando possível |
| Aplicação web nova | OIDC com Authorization Code + PKCE |
| Aplicação móvel ou SPA | OIDC com Authorization Code + PKCE; refresh tokens rotacionados ou restritos |
| Serviço chamando API sem usuário | OAuth 2.0 *client credentials* com autenticação assimétrica, ou federação de workload (Aula 07) |
| Parceiro com IdP próprio | Federação SAML ou OIDC com o IdP do parceiro, com atributos e escopo limitados |

A federação com o IdP corporativo também é o lugar de aplicar a garantia de autenticação: o IdP pode exigir MFA resistente a phishing (níveis AAL da SP 800-63B-4, Aula 01) e informar à aplicação **como** o usuário se autenticou — no OIDC, pelas claims `acr`, `amr` e `auth_time` —, para que operações sensíveis exijam o nível adequado.

## Exemplo empresarial

!!! example "Aurora Pagamentos — o token que servia para tudo"

    A API de lojistas da Aurora aceitava qualquer access token emitido pelo IdP corporativo, sem verificar a audiência. Um teste mostrou que um token emitido para o **aplicativo de marketing** — com escopo de leitura de perfil — era aceito pela **API de antecipação de recebíveis**.

    A correção combinou: audiência obrigatória por API; escopos por operação; Authorization Code com PKCE no aplicativo móvel, substituindo o fluxo implicit; refresh tokens rotacionados; e tokens restritos ao remetente (mTLS) para integrações de parceiros. A validação passou a ser feita por biblioteca padrão da empresa, com testes automatizados para cada item da tabela de validação.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Login em aplicações | Senha local por aplicação | Federação com o IdP corporativo |
| Fluxos OAuth | Implicit e password grant | Authorization Code + PKCE; client credentials com chave assimétrica |
| Tokens | Portador, válidos para qualquer API | Audiência e escopo restritos; restritos ao remetente quando possível |
| Validação | Implementada em cada aplicação | Biblioteca padrão testada |
| Redirecionamento | Curingas e prefixos | Correspondência exata |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e requisitos de padrões de federação, referências que dão nome a cada validação:

| Controle ou padrão | Objetivo na federação | Referência |
|:---|:---|:---|
| Autenticação de usuários da organização e de terceiros | Identificar e autenticar usuários internos e de parceiros, inclusive por IdP externo | SP 800-53: IA-2 e IA-8 (Identification and Authentication — Non-organizational Users) |
| Autenticadores externos aceitos | Aceitar só autenticadores externos conformes e manter a lista dos aceitos | SP 800-53: IA-8(2) (Acceptance of External Authenticators) |
| Autenticação de serviços | Identificar e autenticar serviços e aplicações antes de estabelecer comunicação (clientes OAuth) | SP 800-53: IA-9 (Service Identification and Authentication) |
| Autenticação por chave pública | Proteger a chave privada e validar o caminho de certificação (cliente com JWT assinado, mTLS) | SP 800-53: IA-5(2) (Public Key-based Authentication) |
| Resistência à repetição | Mecanismos de autenticação resistentes a repetição | SP 800-53: IA-2(8) (Access to Accounts — Replay Resistant) |
| Chaves de assinatura do IdP | Estabelecer e gerenciar as chaves criptográficas que assinam asserções e tokens | SP 800-53: SC-12 (Cryptographic Key Establishment and Management) |
| Práticas de segurança do OAuth 2.0 | Redirecionamento exato, PKCE, tokens restritos, audiência | RFC 9700 (BCP 240), Sec. 2 |
| Validação do ID Token | Emissor, audiência, assinatura, validade e `nonce` | OpenID Connect Core 1.0, Sec. 3.1.3.7 |

## Aplicabilidade: on-premises, cloud e híbrido

Aplicações on-premises legadas frequentemente só falam Kerberos ou LDAP; um proxy de aplicação pode fazer a ponte com o IdP em nuvem. Em cloud, consoles e APIs do provedor são federados com o IdP corporativo — e a configuração dessa federação é um ativo do plano de controle. Em ambientes híbridos, o mesmo usuário pode receber asserções SAML, ID Tokens e tíquetes Kerberos; a política de autenticação precisa ser coerente entre eles.

## Como especificar e implementar

- "Aplicações novas autenticam por OIDC com Authorization Code e PKCE; SAML apenas quando o produto não suportar OIDC."
- "O fluxo implicit e o password grant não são permitidos."
- "Access tokens têm audiência e escopos restritos; APIs rejeitam tokens de outra audiência."
- "A validação de tokens e asserções usa a biblioteca padrão, com testes de assinatura, emissor, audiência, validade e repetição."
- "URIs de redirecionamento são registrados e comparados por correspondência exata."

## Trade-offs, limitações e antipadrões

- **Trade-off:** tokens restritos ao remetente aumentam a segurança, mas exigem suporte do cliente e da infraestrutura.
- **Antipadrão — OAuth como login:** aceitar access token como prova de identidade sem ID Token.
- **Antipadrão — IdP multi-tenant sem verificação de emissor:** qualquer locatário consegue entrar.
- **Limitação:** a federação transfere a autenticação para o IdP; comprometer o IdP ou sua chave de assinatura compromete todas as aplicações (Aula 09).

## Como validar

- Apresentar a uma API um token válido de outra audiência e verificar a rejeição.
- Testar o redirecionamento com URI alterado.
- Repetir uma asserção SAML capturada e verificar a rejeição.
- Verificar se algum cliente ainda usa implicit ou password grant.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Toda API rejeita tokens de outra audiência, expirados, sem assinatura ou com algoritmo alterado | Testes automatizados da biblioteca padrão, executados no pipeline |
| Nenhum cliente com implicit ou password grant | Inventário de clientes registrados no servidor de autorização |
| Todo URI de redirecionamento registrado por valor exato | Configuração dos clientes, sem curinga nem prefixo |
| Refresh tokens de clientes públicos rotacionados ou restritos ao remetente | Política do servidor de autorização e teste de reutilização de refresh token |
| Asserção SAML repetida é rejeitada | Teste de repetição com a asserção capturada |

## Como apresentar e justificar

- **Para gestores:** "Hoje um token do aplicativo de marketing abre a API financeira. Com audiência obrigatória, cada token só serve para o que foi emitido."
- **Para desenvolvedores:** "Usem a biblioteca padrão de validação; ela faz as seis verificações e tem testes."

## Checklist de revisão arquitetural

- [ ] O protocolo escolhido corresponde ao cenário.
- [ ] Authorization Code com PKCE em clientes web, móveis e SPA.
- [ ] Implicit e password grant ausentes.
- [ ] Audiência, escopo, emissor, validade, assinatura e repetição validados.
- [ ] Redirecionamentos com correspondência exata.
- [ ] Refresh tokens rotacionados ou restritos ao remetente.

## Questões de compreensão

**1.** Por que um access token OAuth não deve ser usado como prova de autenticação?

??? success "Resposta comentada"

    Porque ele representa autorização para acessar um recurso, não a identidade do usuário nem o momento e a forma da autenticação. O OIDC acrescenta o ID Token, com emissor, sujeito, audiência e tempos, para esse fim.

**2.** O que o PKCE protege?

??? success "Resposta comentada"

    A troca do código de autorização: só quem gerou o verificador original consegue trocar o código por tokens. Isso impede que um código interceptado seja usado por outro cliente. A RFC 9700 o torna obrigatório para clientes públicos.

**3.** Qual o risco do fluxo SAML iniciado pelo IdP?

??? success "Resposta comentada"

    O SP recebe uma asserção sem ter feito requisição, então não pode correlacioná-la a um pedido próprio. Isso facilita repetição e injeção de asserções; exige validação rigorosa de validade, identificador único e destino.

## Exercício de tomada de decisão

!!! question "Cenário: integração de parceiro com a API de laudos da Lumen"

    O laboratório parceiro quer acessar a API de laudos da Lumen. Opções: (A) usuário e senha de uma conta da Lumen no cabeçalho de cada chamada; (B) OAuth 2.0 client credentials com segredo compartilhado; (C) OAuth 2.0 client credentials com autenticação do cliente por chave privada (JWT assinado) e tokens restritos ao remetente por mTLS, com escopo apenas de escrita no prefixo do laboratório. Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), com pesos justificados, e recomende uma.

**Objetivos avaliados:** Escolher o protocolo adequado a cada cenário e especificar a validação de tokens e asserções; aplicar as práticas da RFC 9700 — obrigatórias (PKCE para clientes públicos, redirecionamento exato) e recomendadas (tokens restritos ao remetente e à audiência).

**Entrega esperada:** Matriz ponderada e recomendação com o modelo de credencial, o escopo do token e a etapa intermediária aceitável.

**Critérios de avaliação:**

- A recomendação usa autenticação de cliente sem segredo compartilhado e tokens restritos ao remetente, conforme a RFC 9700.
- O escopo do token limita o parceiro ao próprio prefixo de laudos.
- Há caminho provisório definido, com prazo, caso o parceiro não suporte a opção recomendada.

??? success "Resolução de referência"

    | Critério | Peso | A — Usuário e senha | B — Client credentials com segredo | C — Chave privada + mTLS |
    |:---|:---|:---|:---|:---|
    | Resistência a vazamento de credencial | 3 | 1 | 2 | 3 |
    | Limitação de escopo | 3 | 1 | 3 | 3 |
    | Aderência à RFC 9700 | 2 | 1 | 2 | 3 |
    | Esforço de integração do parceiro | 1 | 3 | 3 | 2 |
    | **Total ponderado** | | **11** | **22** | **26** |

    - **Pesos:** laudos são dados de saúde; a credencial e o escopo determinam o dano possível se o parceiro for comprometido (peso 3 para ambos). A aderência à RFC 9700 pesa 2, por resumir o consenso de segurança do OAuth. O esforço do parceiro pesa 1: é custo de uma vez, negociável no contrato.
    - **Recomendação: C.** A chave privada nunca trafega, o token só funciona com o certificado do cliente e o escopo limita o dano. A opção A é equivalente a compartilhar uma senha de usuário e deve ser descartada. B é aceitável como etapa intermediária se o parceiro não suportar C, com rotação de segredo e escopo restrito.
    - **Trade-off aceito e risco residual:** o parceiro precisa gerir uma chave privada e um certificado de cliente, com renovação. O residual é o comprometimento do ambiente do laboratório, que tem a chave — mitigado por escopo mínimo, assinatura dos laudos e monitoração de volume (Módulo 4 — Aula 06).
    - **O que mudaria a decisão:** se o parceiro não tiver capacidade de operar mTLS, B com segredo forte, rotação e restrição de origem passa a ser o caminho provisório, com prazo para C; se o parceiro rodar em uma nuvem com identidade de workload federável, a federação de workload (Aula 07) elimina até a chave de longa duração.

    **Erros comuns:**

    - Usar uma conta de usuário da Lumen para uma integração entre sistemas.
    - Confundir o *client credentials* com autenticação de usuário.
    - Conceder escopo amplo de leitura e escrita para simplificar a integração.

## Pontos-chave

- SAML e OIDC autenticam; OAuth 2.0 autoriza acesso delegado a APIs.
- O ID Token tem iss, sub, aud, exp e iat obrigatórios.
- A RFC 9700 exige redirecionamento exato, PKCE para clientes públicos e proíbe o password grant.
- Valide assinatura, emissor, audiência, validade, repetição e escopo — com biblioteca padrão.
- A federação concentra confiança no IdP: protegê-lo é proteger todas as aplicações.

## Referências

### Fundamentação principal

- OASIS. *Security Assertion Markup Language (SAML) V2.0 Technical Overview*. Committee Draft 02, 2008. <https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html> — Sec. 3–5. *(Lido; documento não normativo.)*
- IETF. *RFC 9700 — Best Current Practice for OAuth 2.0 Security*. 2025. <https://www.rfc-editor.org/rfc/rfc9700.html> — Sec. 2.1 a 2.6. *(Lido; reconferido em 2026-10-29.)*
- OpenID Foundation. *OpenID Connect Core 1.0 incorporating errata set 2*. 2023. <https://openid.net/specs/openid-connect-core-1_0.html> — Sec. 2 e 3.1.3.7. *(Lido.)*
- NIST. *SP 800-63-4* e *SP 800-63B-4* — níveis de garantia de autenticação (63B lida). A SP 800-63C-4, de federação, não é fonte desta aula: nenhuma afirmação aqui depende dela, e os níveis FAL não são usados.
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles IA-2, IA-2(8), IA-5(2), IA-8, IA-8(2), IA-9 e SC-12, conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- OWASP. *ASVS 5.0* — capítulos V9 (Self-contained Tokens) e V10 (OAuth and OIDC).
- Google Cloud. *Workload Identity Federation* — troca de tokens para workloads ([Aula 07](07-workload-identity-federation.md)).

### Aplicação prática

- Escolha uma API da sua organização e verifique, com um token de teste, se ela rejeita tokens de outra audiência, expirados e com assinatura inválida.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
