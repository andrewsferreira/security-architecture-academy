---
id: M06
title: "Módulo 6 — Identity & Access Management"
description: Arquitetura de identidade como plano de controle — disciplinas IAM, IGA, PAM e PIM, modelos de autorização, Active Directory e Kerberos, federação com SAML, OAuth e OIDC, identidade híbrida, contas privilegiadas e identidades de máquina, federação de workload, ciclo de vida e segregação de funções, e recuperação de identidade em incidentes.
stage: n2
status: published
prerequisites: [M01, M02]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
---

# Módulo 6 — Identity & Access Management { #modulo-06-identity-access-management }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 2 — Arquiteturas de Infraestrutura</span>
<span class="saa-meta">9 aulas · cerca de 11 h de aulas</span>
<span class="saa-status saa-status--published">Published</span>
</div>

## Resumo

!!! abstract "Sobre este módulo"

    Quando aplicações e dados estão em qualquer lugar, a decisão de quem acessa o quê passa a ser tomada pela identidade — e é por isso que credenciais, tokens e contas privilegiadas são o alvo preferido dos ataques. Este módulo trata a identidade como **plano de controle**: como autenticar com garantia adequada, autorizar com modelos auditáveis, federar com segurança, ligar o Active Directory à nuvem sem propagar comprometimentos, proteger privilégios e identidades de máquina, governar acessos ao longo do tempo e recuperar a identidade quando tudo mais falhou.

Ao concluir o módulo, você será capaz de:

- Organizar o domínio em IAM, IGA, PAM e PIM e aplicar os níveis de garantia da SP 800-63B-4.
- Projetar autorização com papéis, atributos e contexto, com PDP, PEP, PIP e PAP.
- Proteger o Active Directory contra os abusos mais comuns de Kerberos e credenciais.
- Escolher e configurar SAML, OAuth 2.0 e OIDC conforme a RFC 9700.
- Decidir o método de identidade híbrida e evitar a propagação de comprometimento entre ambientes.
- Desenhar caminhos de acesso privilegiado e governar identidades de máquina.
- Substituir chaves de longa duração por federação de identidade de workload.
- Governar o ciclo de vida e a segregação de funções.
- Planejar e ensaiar a recuperação de identidade.

## Aulas

<!-- lessons:start -->

| Aula | Tema | Profundidade | Duração |
|:---|:---|:---|:---|
| [Aula 01](01-identity-disciplines.md) | Disciplinas de identidade: IAM, IGA, PAM e PIM | Fundamental | 60 min |
| [Aula 02](02-authorization-models.md) | Modelos de autorização: RBAC, ABAC e acesso contextual | Professional | 75 min |
| [Aula 03](03-directories-kerberos.md) | Diretórios e autenticação corporativa: Active Directory, LDAP e Kerberos | Professional | 90 min |
| [Aula 04](04-federation-saml-oauth-oidc.md) | Federação: SAML 2.0, OAuth 2.0 e OpenID Connect | Professional | 90 min |
| [Aula 05](05-hybrid-identity.md) | Identidade híbrida: Active Directory, Microsoft Entra ID e provedores cloud | Architect | 90 min |
| [Aula 06](06-privileged-machine-identities.md) | Contas privilegiadas e identidades de máquina | Professional | 75 min |
| [Aula 07](07-workload-identity-federation.md) | Workload Identity Federation | Architect | 60 min |
| [Aula 08](08-lifecycle-sod.md) | Ciclo de vida de identidades e segregação de funções | Professional | 60 min |
| [Aula 09](09-identity-recovery.md) | Recuperação de identidade em incidentes | Architect | 75 min |

<!-- lessons:end -->

## Mapa do módulo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m06-module-map.mmd"
```

<figcaption>Figura 1 — Mapa do Módulo 6.</figcaption>
</figure>

## Pré-requisitos

| Pré-requisito | Por quê | Como validar |
|:---|:---|:---|
| [Módulo 1](../01-security-fundamentals/index.md) | Propriedades, princípios, criptografia, PKI e modelos formais | Seções B e C da [avaliação diagnóstica](../../assessments/diagnostic-fundamentals.md) |
| [Módulo 2](../02-security-architecture/index.md) | Padrões, exceções e ADRs | [Avaliação do Módulo 2](../../assessments/m02-security-architecture.md) |
| [Módulo 3 — Aula 05](../03-governance-risk/05-bia-rto-rpo.md) (recomendado) | Objetivos de recuperação usados na Aula 09 | Questões da aula |

## Atividades

- Exercício de decisão ao final de cada aula, com matriz de decisão ponderada, pesos justificados, risco residual e as condições que mudariam a escolha. A matriz organiza a comparação; a decisão continua dependendo do julgamento profissional e da análise de riscos — uma obrigação legal ou um limite de tolerância elimina uma opção antes de qualquer soma.
- As Aulas 06, 07 e 09 formam um percurso de redução de credenciais de longa duração e de recuperação do plano de controle.

## Organizações fictícias usadas no módulo

| Organização | Perfil |
|:---|:---|
| **Meridiana Distribuidora** | Active Directory com administradores logando em servidores comuns, autenticação de passagem e exercício de recuperação. |
| **Lumen Saúde** | Inventário de identidades, autorização de prontuários e cluster on-premises acessando a nuvem. |
| **Aurora Pagamentos** | Explosão de papéis, tokens sem audiência, chave de administrador em pipeline e federação legada. |

## Referências principais do módulo

- NIST. *SP 800-63-4 — Digital Identity Guidelines*. 2025. <https://csrc.nist.gov/pubs/sp/800/63/4/final>.
- NIST. *SP 800-162 — Guide to ABAC*. 2014. <https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-162.pdf>.
- IETF. *RFC 9700 — Best Current Practice for OAuth 2.0 Security*. 2025. <https://www.rfc-editor.org/rfc/rfc9700.html>.
- IETF. *RFC 4120 — Kerberos V5*. 2005. <https://rfc-editor.org/rfc/rfc4120.html>.
- OpenID Foundation. *OpenID Connect Core 1.0*. <https://openid.net/specs/openid-connect-core-1_0.html>.
- OASIS. *SAML V2.0 Technical Overview*. <https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html>.
- Microsoft Learn. *Enterprise access model*, *Hybrid identity authentication*, *AD Forest Recovery Guide*, *Workload identity federation*.
- Google Cloud. *Workload Identity Federation*. AWS. *IAM — OIDC federation*.
