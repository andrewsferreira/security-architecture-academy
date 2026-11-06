---
id: M06-L03
title: "Aula 03 — Diretórios e autenticação corporativa: Active Directory, LDAP e Kerberos"
public_title: "Módulo 6 — Aula 03 — Diretórios e autenticação corporativa: Active Directory, LDAP e Kerberos"
description: Como o Active Directory, o LDAP e o Kerberos sustentam a autenticação corporativa, por que o AD é o ativo mais visado em ataques a ambientes Windows e quais decisões de arquitetura — tiering administrativo, contas de serviço gerenciadas, protocolos e monitoração — reduzem esse risco.
domain: iam
tier: professional
status: published
prerequisites: [M06-L01, M00-L01]
objectives:
  - Explicar as trocas do Kerberos V5 e o papel do KDC e da conta krbtgt.
  - Relacionar o funcionamento do Kerberos a ataques comuns, como Kerberoasting.
  - Diferenciar LDAP como protocolo de diretório e o AD como plano de controle.
  - Especificar controles de arquitetura para proteger o Active Directory.
minutes: 90
sources: [RFC-4120, MS-KERBEROASTING-2024, MS-ENTERPRISE-ACCESS-MODEL, MITRE-ATTACK, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [MS-AD-FOREST-RECOVERY, BOOK-ANDERSON-SE3, NSA-NETWORK-INFRA-2022]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M06
---

# Aula 03 — Diretórios e autenticação corporativa: Active Directory, LDAP e Kerberos { #diretorios-e-autenticacao-corporativa-active-directory-ldap-e-kerberos }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 6 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">90 min · ID técnico: M06-L03</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Na maioria das empresas brasileiras com ambiente Windows, o **Active Directory (AD)** é o plano de controle on-premises: autentica usuários e computadores, aplica políticas, concede acesso a servidores e, muitas vezes, alimenta a identidade em nuvem. Por isso ele aparece em quase todos os cenários de ransomware. Esta aula explica os protocolos que sustentam o AD — **LDAP** e **Kerberos** —, mostra como seu funcionamento é explorado e quais decisões de arquitetura reduzem o risco.

**Pré-requisitos:** [Disciplinas de identidade](01-identity-disciplines.md) e [Computação, sistemas operacionais e virtualização](../00-foundations/01-computing-os-virtualization.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar as trocas do Kerberos V5 e o papel do KDC e da conta krbtgt.
- Relacionar o funcionamento do Kerberos a ataques comuns, como Kerberoasting.
- Diferenciar LDAP como protocolo de diretório e o AD como plano de controle.
- Especificar controles de arquitetura para proteger o Active Directory.

## Conceito

### Diretório, LDAP e Active Directory

- Um **diretório** é um repositório hierárquico de objetos — usuários, grupos, computadores — e seus atributos.
- O **LDAP** é o protocolo padrão para consultar e alterar diretórios. Muitas aplicações autenticam usuários fazendo uma operação de *bind* LDAP com usuário e senha — o que, sem TLS, expõe credenciais na rede.
- O **Active Directory Domain Services** é o serviço de diretório da Microsoft que combina LDAP, **Kerberos**, DNS, políticas de grupo e replicação entre controladores de domínio (DCs).

No modelo de acesso corporativo da Microsoft, sistemas de identidade como o AD formam o **plano de controle**: quem os controla controla o acesso a todo o resto (Aula 01).

### Kerberos V5

O Kerberos, especificado na RFC 4120 (2005), autentica principais — usuários e serviços — por meio de um **centro de distribuição de chaves (KDC)** que mantém um banco de principais e suas chaves secretas, compartilhadas apenas entre cada principal e o KDC (Sec. 1.1 e 1.7). Os relógios dos hosts precisam estar razoavelmente sincronizados para a detecção de repetição (Sec. 1.6). Três trocas formam o protocolo:

| Troca | O que acontece |
|:---|:---|
| **AS** — Authentication Service | O cliente obtém um *ticket-granting ticket* (TGT) |
| **TGS** — Ticket-Granting Service | O cliente apresenta o TGT e obtém um tíquete para um serviço específico |
| **AP** — Client/Server | O cliente apresenta o tíquete ao serviço; opcionalmente, o serviço se autentica de volta |

No AD, os DCs são os KDCs; o TGT é protegido com a chave da conta especial **krbtgt**, e o tíquete de serviço, com a chave da conta associada ao **SPN** (*Service Principal Name*) do serviço.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m06-l03-kerberos.mmd"
```

<figcaption>Figura 1 — Trocas AS, TGS e AP do Kerberos V5 em um domínio Active Directory, com o ponto explorado pelo Kerberoasting.</figcaption>
</figure>

## Fundamentos técnicos

### Como o funcionamento vira ataque

| Característica | Abuso | Referência |
|:---|:---|:---|
| Qualquer usuário autenticado pode pedir tíquetes de serviço; eles são cifrados com chave derivada da senha da conta do serviço | **Kerberoasting**: pedir tíquetes e tentar quebrar a senha offline | Microsoft, 2024; ATT&CK T1558.003 |
| O TGT é protegido pela chave da krbtgt | Quem obtém essa chave pode forjar TGTs (**Golden Ticket**) | ATT&CK T1558.001 |
| Credenciais ficam em memória em hosts onde administradores fazem login | **Extração de credenciais** do sistema operacional | ATT&CK T1003 |
| Contas válidas abrem serviços remotos | **Movimento lateral** com credenciais | ATT&CK T1021 |

A orientação da Microsoft de 2024 sobre Kerberoasting explica que o ataque mira contas de serviço com SPN — frequentemente privilegiadas — e que o algoritmo **RC4** facilita a quebra por não usar sal nem hash iterado. As mitigações recomendadas:

- Usar **contas de serviço gerenciadas** sempre que possível — gMSA, cujas senhas têm 120 caracteres aleatórios, ou dMSA, a geração mais recente, disponível no Windows Server 2025.
- Onde não for possível, senhas longas e aleatórias, com mínimo de 14 caracteres.
- Configurar as contas de serviço para **AES** (128 e 256 bits) nos tíquetes de serviço e desabilitar RC4 nessas contas. Como prática operacional, redefina a senha de contas antigas depois da mudança: contas cuja senha não foi trocada desde a adoção do AES podem não ter chaves AES.
- **Auditar SPNs** e removê-los de contas que não precisam deles.
- Detectar pedidos com tipo de cifra incomum (especialmente RC4) e um mesmo usuário pedindo muitos tíquetes em pouco tempo.

### Decisões de arquitetura para proteger o AD

| Decisão | Efeito |
|:---|:---|
| **Separação administrativa por planos** (tiering): contas de administração do diretório só usadas em DCs e estações dedicadas | Credenciais do plano de controle não ficam expostas em servidores e estações comuns |
| **Estações de acesso privilegiado** para administração | Reduz roubo de credenciais por malware na estação do administrador |
| **Privilégio just-in-time** para grupos administrativos | Reduz a janela de exposição (Aula 06) |
| **Contas de serviço gerenciadas** e auditoria de SPNs | Reduz Kerberoasting |
| **LDAP com assinatura e TLS**; aplicações com bind sobre TLS | Evita credenciais em claro e adulteração |
| **Desabilitar protocolos legados** (NTLMv1, RC4) após inventário | Remove caminhos fracos (Módulo 8 — Aula 06) |
| **DCs em zona própria**, administrados só a partir da zona de gestão | Limita o alcance a partir de servidores comprometidos (Módulo 5) |
| **Monitoração** de alterações em grupos privilegiados, criação de contas, pedidos de tíquetes anômalos | Detecta as etapas do ataque |
| **Backup recuperável e plano de recuperação de floresta** | Permite recuperar o plano de controle (Aula 09) |

## Exemplo empresarial

!!! example "Meridiana — o administrador que logava no servidor de etiquetas"

    Na análise do cenário RSK-007, a equipe descobriu que administradores do domínio faziam login com suas contas privilegiadas em servidores de aplicação — inclusive no servidor de etiquetas, sem suporte e sem EDR. Uma extração de credenciais naquele servidor daria controle do domínio.

    Também havia 23 contas com SPN, 9 delas membros de grupos administrativos, todas com senhas definidas anos atrás e RC4 habilitado. As ações:

    1. Contas administrativas do domínio restritas a DCs e a duas estações de acesso privilegiado.
    2. Contas separadas para administrar servidores, sem direitos sobre o diretório.
    3. Migração de 17 contas de serviço para gMSA; as demais com senhas aleatórias longas e AES.
    4. Remoção de 4 SPNs sem uso e alerta para pedidos de tíquete em RC4.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Contas administrativas | Uma conta poderosa, usada em qualquer host | Contas separadas por plano, usadas só em hosts do mesmo plano |
| Contas de serviço | Senhas antigas, membros de grupos administrativos | gMSA/dMSA, privilégio mínimo, SPNs auditados |
| Protocolos | Legados habilitados por compatibilidade | AES, LDAP sobre TLS; legados removidos após inventário |
| DCs | Na rede de servidores | Zona própria, administração só pela zona de gestão |
| Monitoração | Logs de segurança locais | Eventos de diretório e de Kerberos no SIEM, com detecções |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias que correspondem às decisões de proteção do diretório:

| Controle ou padrão | Objetivo na proteção do AD | Referência |
|:---|:---|:---|
| Contas privilegiadas por plano | Administrar contas privilegiadas segundo um esquema de papéis, monitorar atribuições e revogar quando deixam de ser adequadas | SP 800-53: AC-2(7) (Privileged User Accounts) e AC-6(5) (Privileged Accounts) |
| Conta separada para uso diário | Quem tem acesso privilegiado usa conta não privilegiada para funções comuns | SP 800-53: AC-6(2) (Non-privileged Access for Nonsecurity Functions) |
| Senhas de contas de serviço | Autenticadores por senha fortes, protegidos e trocados | SP 800-53: IA-5 (Authenticator Management) e IA-5(1) (Password-based Authentication) |
| LDAP sem credenciais em claro | Proteger confidencialidade e integridade na transmissão com criptografia | SP 800-53: SC-8 e SC-8(1) (Cryptographic Protection) |
| Monitoração do diretório | Monitorar o sistema e analisar registros para detectar as etapas do ataque | SP 800-53: SI-4 (System Monitoring) e AU-6 (Audit Record Review, Analysis, and Reporting) |
| Backup do plano de controle | Backup que permita recuperar o diretório | SP 800-53: CP-9 (System Backup) |
| Gestão de contas e de acesso | Inventário de contas, inclusive de serviço, e processos de concessão e revogação | CIS v8.1: Controles 5 (Account Management) e 6 (Access Control Management) |
| Planos de controle, gestão e dados | Separar caminhos de acesso privilegiado ao plano de controle | Microsoft, modelo de acesso corporativo |

## Aplicabilidade: on-premises, cloud e híbrido

DCs em máquinas virtuais na nuvem continuam sendo DCs — e quem administra a conta de nuvem onde estão administra, na prática, o domínio. Serviços de diretório gerenciados reduzem a operação, mas não o risco de credenciais. Em ambientes híbridos, o servidor de sincronização entre AD e IdP em nuvem tem o mesmo nível de criticidade dos DCs (Aula 05).

## Como especificar e implementar

- "Contas com direitos sobre o diretório só fazem login em DCs e estações de acesso privilegiado."
- "Contas de serviço usam contas gerenciadas sempre que possível; as demais têm senhas aleatórias longas, AES e revisão periódica de SPN."
- "Aplicações autenticam no diretório por protocolos que não expõem credenciais em claro."
- "Alterações em grupos privilegiados e pedidos de tíquetes anômalos geram alertas tratados pelo SOC."

## Trade-offs, limitações e antipadrões

- **Trade-off:** desabilitar protocolos legados quebra aplicações antigas — exige inventário e janela de transição.
- **Antipadrão — conta de serviço no grupo de administradores do domínio:** "porque a instalação pedia".
- **Antipadrão — administração do domínio a partir da estação de uso diário:** um phishing basta.
- **Limitação:** proteger o AD não elimina o risco de credenciais de usuários comuns; MFA e detecção continuam necessárias.

## Como validar

- Listar onde contas privilegiadas fizeram login nos últimos 30 dias.
- Listar contas com SPN, seus grupos e os tipos de cifra permitidos.
- Simular um pedido em massa de tíquetes de serviço em ambiente de teste e verificar o alerta.
- Verificar se alguma aplicação faz bind LDAP sem TLS.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhum login de conta com direitos sobre o diretório fora de DCs e estações de acesso privilegiado | Consulta de eventos de logon dos últimos 30 dias, sem exceção não registrada |
| Nenhuma conta com SPN em grupo administrativo sem justificativa | Lista de contas com SPN, grupos e dono |
| Contas de serviço com AES e sem RC4 | Atributo de tipos de cifra suportados conferido em todas as contas com SPN |
| Pedido em massa de tíquetes e tíquetes RC4 geram alerta | Teste em ambiente controlado com o alerta registrado no SIEM |
| Nenhum bind LDAP simples sem TLS fora das exceções registradas | Eventos de bind inseguro nos DCs, comparados à lista de exceções |

## Como apresentar e justificar

- **Para a diretoria:** "Quem controla o Active Directory controla a empresa. Hoje, as senhas que dão esse controle estão em servidores sem proteção."
- **Para a operação:** "Duas contas por administrador: uma para servidores, outra para o diretório, usada só nas estações dedicadas."

## Checklist de revisão arquitetural

- [ ] Contas do plano de controle usadas apenas em hosts do mesmo plano.
- [ ] Contas de serviço gerenciadas ou com senhas fortes, AES e SPNs auditados.
- [ ] Protocolos legados inventariados, com plano de remoção.
- [ ] DCs em zona própria, administrados pela zona de gestão.
- [ ] Monitoração de grupos privilegiados e de Kerberos no SIEM.
- [ ] Plano de recuperação do diretório testado.

## Questões de compreensão

**1.** Por que qualquer usuário autenticado consegue iniciar um Kerberoasting?

??? success "Resposta comentada"

    Porque o protocolo permite que usuários autenticados peçam tíquetes para serviços registrados com SPN, e esses tíquetes são cifrados com chave derivada da senha da conta do serviço. O atacante leva o tíquete e tenta adivinhar a senha offline.

**2.** Que mitigações a Microsoft recomenda contra Kerberoasting?

??? success "Resposta comentada"

    Contas de serviço gerenciadas (gMSA/dMSA), senhas longas e aleatórias quando não for possível usá-las, AES em vez de RC4, auditoria e remoção de SPNs desnecessários e detecção de pedidos anômalos de tíquetes.

**3.** Por que o servidor de sincronização com a nuvem tem a mesma criticidade de um DC?

??? success "Resposta comentada"

    Porque tem acesso privilegiado ao diretório e à identidade em nuvem; comprometê-lo permite alterar identidades nos dois ambientes. Faz parte do plano de controle.

## Exercício de tomada de decisão

!!! question "Cenário: aplicação legada com bind LDAP em claro na Lumen"

    O sistema de faturamento da Lumen autentica usuários por bind LDAP simples na porta sem TLS, e o fornecedor diz que suporte a TLS só virá em uma versão daqui a um ano. A aplicação permite configurar o endereço e a porta do servidor LDAP. As opções para o período até a atualização são:

    - **A** — IPsec entre o servidor de aplicação e os DCs, com a comunicação em segmento dedicado;
    - **B** — túnel TLS local: um componente no servidor de aplicação recebe o bind em `localhost` e o encaminha aos DCs por LDAP sobre TLS (porta 636);
    - **C** — proxy de autenticação na frente do faturamento, autenticando pelo IdP com MFA e repassando a sessão à aplicação.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e proponha o tratamento definitivo.

**Objetivos avaliados:** Especificar controles de arquitetura para proteger o Active Directory; diferenciar LDAP como protocolo de diretório e o AD como plano de controle.

**Entrega esperada:** Matriz ponderada, recomendação para o período até a atualização e o tratamento definitivo com prazo e dono.

**Critérios de avaliação:**

- A solução elimina a senha em claro na rede sem criar risco novo nos controladores de domínio.
- O risco que permanece (senha em claro dentro do servidor de aplicação) é declarado e aceito por um dono.
- O tratamento definitivo vira exigência contratual com data e exceção registrada.

??? success "Resolução de referência"

    | Critério | Peso | A — IPsec até os DCs | B — Túnel TLS local | C — Proxy com IdP e MFA |
    |:---|:---|:---|:---|:---|
    | Senha fora da rede em claro | 3 | 3 | 3 | 2 |
    | Independência de suporte do fornecedor | 2 | 3 | 3 | 1 |
    | Esforço de implantação e operação | 2 | 2 | 2 | 1 |
    | Mudança nos DCs (plano de controle) | 2 | 1 | 2 | 3 |
    | Proteção adicional da credencial do usuário | 1 | 1 | 1 | 3 |
    | **Total ponderado** | | **22** | **24** | **19** |

    - **Pesos:** o problema é a senha atravessando a rede em claro (peso 3). Depender do fornecedor, o esforço e mexer nos DCs pesam 2: a solução precisa funcionar já, com equipe pequena, sem criar risco no plano de controle. A proteção adicional com MFA pesa 1 — é ganho, mas não o problema a resolver.
    - **Recomendação: B.** O túnel cifra todo o trecho de rede sem depender do fornecedor e exige dos DCs apenas o LDAP sobre TLS, que muitos domínios já oferecem (quando não, exige certificado de servidor nos DCs — daí a nota 2). O IPsec da opção A resolve o mesmo problema, mas exige políticas nos DCs, que são o plano de controle; a C só funciona se o produto aceitar a sessão repassada pelo proxy, e o próprio bind LDAP pode continuar existindo por trás.
    - **Medidas complementares:** monitorar binds dessa origem; senhas dos usuários do faturamento não reutilizadas em sistemas mais críticos.
    - **Definitivo:** exigir no contrato a versão com LDAP sobre TLS ou SAML/OIDC, com prazo; registrar a exceção com dono e data (Módulo 2 — Aula 04).
    - **Trade-off aceito e risco residual:** a senha continua em claro dentro do servidor de aplicação (entre a aplicação e o túnel), e o túnel é mais um componente com certificado a manter; quem compromete o servidor de aplicação captura senhas — risco baixo a médio, aceito pelo diretor financeiro até a atualização.
    - **O que mudaria a decisão:** se a aplicação não permitir trocar o endereço do servidor LDAP, B deixa de ser viável e A passa a ser a opção; se o produto aceitar sessão repassada por cabeçalho e o faturamento entrar no escopo de acesso remoto, C ganha peso, por trazer MFA.

    **Erros comuns:**

    - Aceitar o bind em claro porque a rede é interna.
    - Escolher uma opção que exige alterar os DCs sem pesar o risco no plano de controle.
    - Deixar a exceção sem prazo, transformando o provisório em permanente.

## Pontos-chave

- O AD é o plano de controle on-premises; LDAP e Kerberos são seus protocolos centrais.
- O Kerberos usa um KDC, TGT e tíquetes de serviço; a krbtgt e as contas com SPN são alvos de alto valor.
- Kerberoasting explora senhas fracas de contas de serviço; gMSA/dMSA, AES e auditoria de SPN mitigam.
- Contas administrativas do diretório só em DCs e estações dedicadas.
- Protocolos legados exigem inventário e plano de remoção.

## Referências

### Fundamentação principal

- IETF. *RFC 4120 — The Kerberos Network Authentication Service (V5)*. 2005. <https://rfc-editor.org/rfc/rfc4120.html> — Sec. 1.1, 1.6, 1.7, 3.1 e 3.2. *(Lido.)*
- D. Weston, V. Sun. *Microsoft's guidance to help mitigate Kerberoasting*. Microsoft Security Blog, 11/10/2024. <https://www.microsoft.com/security/blog/2024/10/11/microsofts-guidance-to-help-mitigate-kerberoasting>. *(Lido; recomendações reconferidas em 2026-10-29.)*
- Microsoft. *The enterprise access model*. *(Lido.)*
- MITRE. *ATT&CK v20* — T1558 Steal or Forge Kerberos Tickets (subtécnicas .001 Golden Ticket e .003 Kerberoasting), T1003 OS Credential Dumping e T1021 Remote Services. *(Páginas conferidas.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-2(7), AC-6(2), AC-6(5), IA-5, IA-5(1), SC-8, SC-8(1), SI-4, AU-6 e CP-9, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controles 5 e 6 — gratuito.

### Leitura complementar

- Microsoft. *Active Directory Forest Recovery Guide* ([Aula 09](09-identity-recovery.md)).
- R. Anderson. *Security Engineering*, 3ª ed. — capítulos sobre autenticação e controle de acesso.
- NSA. *Network Infrastructure Security Guidance* — gerenciamento fora de banda.

### Aplicação prática

- Liste, em um domínio de laboratório ou de teste, as contas com SPN, os grupos a que pertencem e os tipos de cifra permitidos. Classifique cada uma em "migrar para gMSA", "trocar senha e exigir AES" ou "remover SPN".

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
