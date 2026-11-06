---
id: M08-L03
title: "Aula 03 — Arquitetura para Windows Server, Linux e Active Directory"
public_title: "Módulo 8 — Aula 03 — Arquitetura para Windows Server, Linux e Active Directory"
description: Decisões de arquitetura para ambientes de servidores Windows e Linux integrados ao Active Directory — separação administrativa por planos, credenciais locais e de serviço, acesso remoto administrativo, registro e detecção, e as escolhas de integração de Linux ao diretório.
domain: infrastructure-foundations
tier: professional
status: published
prerequisites: [M06-L03, M06-L06, M08-L02]
objectives:
  - Aplicar a separação administrativa por planos a servidores Windows e Linux.
  - Especificar o tratamento de credenciais locais, de serviço e de acesso remoto administrativo.
  - Decidir como integrar servidores Linux à identidade corporativa.
  - Definir registro e detecção mínimos para servidores e controladores de domínio.
minutes: 90
sources: [MS-ENTERPRISE-ACCESS-MODEL, MS-KERBEROASTING-2024, CISA-STOPRANSOMWARE-GUIDE, MITRE-ATTACK, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [MS-WINDOWS-DEPRECATED-FEATURES, PETRI-NTLM-2026, NIST-SP800-128, MS-AD-FOREST-RECOVERY]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M08
---

# Aula 03 — Arquitetura para Windows Server, Linux e Active Directory { #arquitetura-para-windows-server-linux-e-active-directory }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 8 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">90 min · ID técnico: M08-L03</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    É comum que ambientes on-premises combinem servidores Windows integrados ao Active Directory com servidores Linux, muitas vezes administrados de formas muito diferentes. Ataques exploram exatamente essas diferenças: a credencial administrativa esquecida em um servidor, a senha local igual em todos os hosts, a chave SSH copiada para dezenas de máquinas. Esta aula aplica os princípios de identidade (Módulo 6) e de hardening (Aula 02) a decisões concretas de arquitetura de servidores.

**Pré-requisitos:** [AD, LDAP e Kerberos](../06-iam/03-directories-kerberos.md), [Contas privilegiadas](../06-iam/06-privileged-machine-identities.md) e [Hardening e baselines](02-hardening-baselines.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Aplicar a separação administrativa por planos a servidores Windows e Linux.
- Especificar o tratamento de credenciais locais, de serviço e de acesso remoto administrativo.
- Decidir como integrar servidores Linux à identidade corporativa.
- Definir registro e detecção mínimos para servidores e controladores de domínio.

## Conceito

### Separação por planos aplicada a servidores

O modelo de acesso corporativo da Microsoft pede que planos inferiores **não controlem** planos superiores e que nenhuma conta acumule privilégios em vários planos (Módulo 6 — Aula 06). Em um ambiente de servidores, isso se traduz em três grupos de sistemas, cada um administrado por contas próprias:

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m08-l03-server-tiers.mmd"
```

<figcaption>Figura 1 — Plano de controle administrado por estações de acesso privilegiado; servidores Windows e Linux pelo bastion; estações por contas de suporte; acessos de planos inferiores aos superiores proibidos.</figcaption>
</figure>

| Grupo | Exemplos | Administrado por | De onde |
|:---|:---|:---|:---|
| **Plano de controle** | DCs, PKI, sincronização de identidade, console do EDR, servidor de backup | Contas do plano de controle | Estações de acesso privilegiado |
| **Servidores** | Aplicação, banco, arquivos — Windows e Linux | Contas de administração de servidores | Bastion / acesso privilegiado |
| **Estações** | Desktops e notebooks | Contas de suporte | Ferramentas de suporte |

O console do EDR e o servidor de backup aparecem no plano de controle porque quem os controla pode desativar proteções em todos os hosts ou apagar todas as cópias — as técnicas Disable or Modify Tools (T1685) e Inhibit System Recovery (T1490) do ATT&CK (Módulo 4 — Aula 04).

## Fundamentos técnicos

### Credenciais em servidores

| Credencial | Risco | Decisão de arquitetura |
|:---|:---|:---|
| **Administrador local** com a mesma senha em todos os servidores | Uma senha extraída abre todos | Senha única e gerenciada por servidor, rotacionada automaticamente — o #StopRansomware Guide recomenda o LAPS onde possível |
| **Contas de serviço** de domínio | Kerberoasting, privilégios excessivos | Contas gerenciadas (gMSA/dMSA), AES, SPNs auditados (Módulo 6 — Aula 03) |
| **Logins interativos de administradores do domínio** em servidores | Credenciais em memória extraíveis (T1003) | Proibidos; administração de servidores por contas sem direitos sobre o diretório |
| **Chaves SSH** copiadas entre servidores Linux | Uma chave comprometida abre muitos hosts | Certificados SSH de curta duração emitidos por autoridade central, ou acesso via bastion |
| **Senhas em scripts** | Leitura por qualquer um com acesso ao arquivo | Cofre de segredos, identidade de workload (Módulo 6 — Aula 07) |

### Acesso remoto administrativo

O #StopRansomware Guide (setembro de 2023) recomenda não expor serviços como RDP à internet e limitar seu uso, com MFA e registro das tentativas de login; separar contas administrativas e de usuário, usando para administração só contas designadas; aplicar privilégio mínimo; e monitorar tentativas de login contra força bruta e *password spraying*. Na arquitetura:

- RDP, SSH e protocolos de gerenciamento aceitos **somente a partir do bastion ou da zona de gestão** (Módulo 5 — Aula 03).
- **Autenticação resistente a phishing** no bastion; sessões gravadas para servidores críticos.
- Nenhuma ferramenta de acesso remoto de terceiros instalada diretamente em servidores (Módulo 5 — Aula 04).

### Integração de Linux à identidade

| Opção | Como funciona | Quando |
|:---|:---|:---|
| **Ingresso no domínio AD** (via Kerberos/LDAP) | Contas e grupos do AD; política centralizada | Ambientes majoritariamente Windows; necessidade de grupos corporativos |
| **Certificados SSH de curta duração** emitidos por autoridade integrada ao IdP | Usuário obtém certificado após autenticação forte | Ambientes com muitos servidores Linux; bastions modernos |
| **Contas locais** gerenciadas por automação | Contas e chaves distribuídas por gerência de configuração | Poucos servidores, ambientes isolados |

Ingressar Linux no AD estende o plano de controle a esses servidores: um comprometimento do AD passa a valer também para eles, e eles passam a guardar tíquetes Kerberos. A decisão deve ser registrada em ADR com esse trade-off.

### Registro e detecção mínimos

| Fonte | Eventos essenciais |
|:---|:---|
| Controladores de domínio | Alterações em grupos privilegiados; criação de contas; pedidos de tíquetes com cifra incomum ou em volume (Kerberoasting); alterações em políticas de grupo |
| Servidores Windows | Logons administrativos e sua origem; criação de serviços e tarefas agendadas; desativação de proteções |
| Servidores Linux | Uso de sudo; logins SSH e origem; alterações em arquivos de configuração críticos |
| Bastion e PAM | Sessões, comandos e aprovações |

A orientação da Microsoft sobre Kerberoasting sugere detectar pedidos de tíquetes com tipos de cifra incomuns, especialmente RC4, e um mesmo usuário pedindo muitos tíquetes em pouco tempo.

### Protocolos e serviços

O mesmo guia da CISA recomenda desabilitar SMBv1 e migrar para SMBv3, bloqueando o acesso externo ao SMB (porta TCP 445, de entrada e de saída); a Microsoft declarou todas as versões do NTLM obsoletas em junho de 2024 e removeu o NTLMv1 a partir do Windows 11 24H2 e do Windows Server 2025, segundo a lista oficial de recursos obsoletos do Windows; a desabilitação do NTLM por padrão em versões futuras foi anunciada depois e é tratada na Aula 06. A baseline de servidores (Aula 02) deve refletir essas decisões.

## Exemplo empresarial

!!! example "Lumen Saúde — 140 servidores Linux e uma chave"

    A Lumen descobriu que uma mesma chave SSH de um administrador antigo estava autorizada em 140 servidores Linux, e que servidores Windows tinham o mesmo administrador local com a mesma senha.

    Decisões:

    1. **Linux:** autoridade de certificados SSH integrada ao IdP, com certificados de 8 horas emitidos após autenticação resistente a phishing; acesso apenas via bastion; remoção de todas as chaves autorizadas estáticas por automação.
    2. **Windows:** senhas de administrador local únicas por servidor, gerenciadas e rotacionadas; contas de administração de servidores sem direitos sobre o diretório.
    3. **Plano de controle:** console do EDR, servidor de backup e PKI movidos para a zona de gestão, administrados apenas por estações de acesso privilegiado.
    4. **Detecção:** eventos de DCs, servidores e bastion no SIEM, com cinco detecções iniciais.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Administração | Mesma conta poderosa em tudo | Contas por plano, usadas só em sistemas do mesmo plano |
| Senhas locais | Iguais em todos os hosts | Únicas e gerenciadas |
| SSH | Chaves estáticas copiadas | Certificados de curta duração ou bastion |
| Acesso administrativo | De qualquer estação | Somente via bastion ou zona de gestão |
| EDR e backup | "Ferramentas de TI" | Plano de controle |
| Registro | Local, sem análise | Central, com detecções |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias para a administração de servidores:

| Controle ou padrão | Objetivo na administração de servidores | Referência |
|:---|:---|:---|
| Contas privilegiadas por plano | Contas privilegiadas segundo esquema de papéis, restritas a quem precisa | SP 800-53: AC-2(7) (Privileged User Accounts) e AC-6(5) (Privileged Accounts) |
| Contas separadas | Conta não privilegiada para funções comuns | SP 800-53: AC-6(2) (Non-privileged Access for Nonsecurity Functions) |
| Senhas locais e de serviço | Autenticadores únicos, protegidos e trocados | SP 800-53: IA-5 (Authenticator Management) e IA-5(1) (Password-based Authentication) |
| Acesso remoto administrativo | Restrições e autorização por tipo de acesso remoto, pontos de acesso gerenciados | SP 800-53: AC-17 (Remote Access) e AC-17(3) (Managed Access Control Points) |
| MFA para administradores | Autenticação multifator em contas privilegiadas | SP 800-53: IA-2(1) |
| Registro e análise | Eventos definidos registrados e analisados | SP 800-53: AU-2 (Event Logging) e AU-6 (Audit Record Review, Analysis, and Reporting) |
| Gestão de contas e de acesso | Contas administrativas dedicadas e processos de acesso | CIS v8.1: Controles 5 (Account Management) e 6 (Access Control Management) |
| Ameaças de referência | Extração de credenciais, desativação de proteções, inibição da recuperação | MITRE ATT&CK v20: T1003, T1685, T1490 |

## Aplicabilidade: on-premises, cloud e híbrido

Os mesmos princípios valem para máquinas virtuais em cloud — com a diferença de que o **plano de gestão** inclui o console e a API da nuvem, e serviços de sessão gerenciada podem substituir o bastion. Em ambientes híbridos, DCs em nuvem e servidores de sincronização devem seguir as regras do plano de controle, e a identidade usada para administrar a conta de nuvem não pode ser uma conta sincronizada do AD (Módulo 6 — Aula 05).

## Como especificar e implementar

- "Sistemas são classificados em plano de controle, servidores e estações; cada grupo é administrado por contas próprias, a partir de origens definidas."
- "Senhas de administrador local são únicas por host e gerenciadas; contas de serviço usam contas gerenciadas sempre que possível."
- "Acesso administrativo a servidores ocorre via bastion com autenticação resistente a phishing; RDP e SSH não são expostos fora da zona de gestão."
- "Servidores Linux usam certificados SSH de curta duração ou acesso via bastion; chaves estáticas autorizadas são proibidas."
- "Console do EDR, backup, PKI e sincronização de identidade são tratados como plano de controle."

## Trade-offs, limitações e antipadrões

- **Trade-off:** ingressar Linux no AD simplifica a gestão de identidade, mas amplia o raio de impacto de um comprometimento do diretório.
- **Antipadrão — "conta de serviço para tudo"** com direitos de administrador em todos os servidores.
- **Antipadrão — exceção permanente de RDP direto** para um fornecedor.
- **Limitação:** separação por planos exige disciplina operacional e ferramentas; sem estações dedicadas, vira regra no papel.

## Como validar

- Listar logins de contas do plano de controle fora de DCs e estações dedicadas.
- Verificar se senhas de administrador local são únicas em uma amostra de hosts.
- Procurar chaves SSH autorizadas estáticas nos servidores Linux.
- Tentar RDP ou SSH a partir de uma estação de usuário e confirmar o bloqueio.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhum login de conta do plano de controle fora de DCs e estações dedicadas | Consulta de eventos de logon do período |
| Senhas de administrador local únicas e rotacionadas | Amostra de hosts com o registro da solução de gestão de senhas |
| Nenhuma chave SSH estática autorizada fora das exceções | Varredura de `authorized_keys` nos servidores Linux |
| RDP e SSH bloqueados a partir de estações de usuário | Teste de conexão negado |
| Console do EDR e servidor de backup administrados só pelo plano de controle | Regras de acesso e eventos de logon desses sistemas |

## Como apresentar e justificar

- **Para a diretoria:** "Uma única chave de um ex-administrador abria 140 servidores. Agora cada acesso exige autenticação forte e dura um turno."
- **Para a operação:** "Três tipos de conta, três origens. O bastion é a porta de entrada para servidores."

## Checklist de revisão arquitetural

- [ ] Sistemas classificados por plano; EDR, backup e PKI no plano de controle.
- [ ] Contas administrativas separadas por plano.
- [ ] Senhas locais únicas e gerenciadas.
- [ ] Contas de serviço gerenciadas e SPNs auditados.
- [ ] SSH sem chaves estáticas; acesso via bastion.
- [ ] Eventos essenciais no SIEM com detecções.

## Questões de compreensão

**1.** Por que o console do EDR e o servidor de backup pertencem ao plano de controle?

??? success "Resposta comentada"

    Porque quem os controla pode desativar a proteção de todos os hosts ou apagar todas as cópias de recuperação — exatamente o que ransomware tenta fazer antes do impacto.

**2.** Qual o risco de ingressar servidores Linux no Active Directory?

??? success "Resposta comentada"

    Estende o plano de controle a esses servidores: um comprometimento do AD passa a dar acesso a eles, e eles passam a armazenar credenciais Kerberos. É um trade-off a registrar, não um impedimento automático.

**3.** Por que senhas de administrador local iguais em todos os hosts são perigosas?

??? success "Resposta comentada"

    Porque a extração da senha (ou do hash) em um único host permite acessar todos os outros com o mesmo privilégio, facilitando o movimento lateral.

## Exercício de tomada de decisão

!!! question "Cenário: Linux no AD na Aurora"

    A Aurora tem 300 servidores Linux e quer centralizar a identidade. Opções: (A) ingressar todos no AD; (B) autoridade de certificados SSH integrada ao IdP, com acesso via bastion; (C) manter contas locais distribuídas por gerência de configuração. Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e recomende uma.

**Objetivos avaliados:** Decidir como integrar servidores Linux à identidade corporativa; aplicar a separação administrativa por planos a servidores Windows e Linux.

**Entrega esperada:** Matriz ponderada e a recomendação de integração dos servidores Linux, com as exceções e o acesso de emergência.

**Critérios de avaliação:**

- A solução usa credenciais de curta duração e revogação centralizada.
- A autoridade de certificados SSH é tratada como ativo do plano de controle, com proteção da chave.
- Há exceção registrada para servidores que precisam de grupos do AD e acesso de emergência ao console.

??? success "Resolução de referência"

    | Critério | Peso | A — Ingresso no AD | B — Certificados SSH + bastion | C — Contas locais automatizadas |
    |:---|:---|:---|:---|:---|
    | Raio de impacto de comprometimento da identidade | 3 | 1 | 2 | 2 |
    | Força da autenticação e duração das credenciais | 3 | 2 | 3 | 1 |
    | Revogação e ciclo de vida | 2 | 3 | 3 | 1 |
    | Esforço de implantação | 1 | 2 | 2 | 3 |
    | **Total ponderado** | | **17** | **23** | **14** |

    - **Pesos:** o raio de impacto de um comprometimento da identidade e a força e duração das credenciais são os riscos centrais (peso 3). Revogação pesa 2: importa em desligamentos e incidentes. O esforço pesa 1.
    - **Recomendação: B.** Credenciais de curta duração emitidas após autenticação forte, sem estender o AD aos servidores e com revogação centralizada pelo IdP. A opção A é aceitável para servidores que precisam de grupos do AD (por exemplo, compartilhamentos de arquivos), registrada como exceção; C não escala para 300 servidores.
    - **Trade-off aceito e risco residual:** a autoridade de certificados SSH passa a ser um ativo do plano de controle — quem a controla emite acesso a todos os servidores — e o bastion vira dependência de disponibilidade. O residual é tratado protegendo a chave da autoridade (HSM ou serviço gerenciado), administrando-a por estações dedicadas e definindo acesso de emergência ao console dos servidores.
    - **O que mudaria a decisão:** se a maioria dos servidores Linux precisar de grupos do AD para autorização em aplicações (Samba, NFS com Kerberos), A ganha peso para esse grupo; se a Aurora não tiver IdP capaz de emitir certificados SSH nem bastion, B começa com o bastion e C de transição.

    **Erros comuns:**

    - Ingressar todos os servidores no AD sem avaliar o aumento do raio de impacto do domínio.
    - Distribuir chaves SSH de longa duração por gerência de configuração.
    - Esquecer o acesso de emergência quando o bastion ou o IdP estiverem indisponíveis.

## Pontos-chave

- Separe a administração em plano de controle, servidores e estações, com contas e origens próprias.
- EDR, backup, PKI e sincronização de identidade são plano de controle.
- Senhas locais únicas, contas de serviço gerenciadas e SSH sem chaves estáticas.
- Acesso administrativo só pelo bastion ou zona de gestão.
- Registre e detecte nos DCs, servidores e bastion.

## Referências

### Fundamentação principal

- Microsoft. *The enterprise access model*. *(Lido.)*
- D. Weston, V. Sun. *Microsoft's guidance to help mitigate Kerberoasting*. 2024. *(Lido.)*
- CISA, FBI, NSA, MS-ISAC. *#StopRansomware Guide*. 2023. <https://www.cisa.gov/stopransomware/ransomware-guide>. *(Lido; recomendações reconferidas em 2026-10-29.)*
- MITRE. *ATT&CK v20* — T1003, T1685, T1490. *(Páginas conferidas.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-2(7), AC-6(2), AC-6(5), AC-17, AC-17(3), AU-2, AU-6, IA-2(1), IA-5 e IA-5(1), conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controles 5 e 6 — gratuito.

### Leitura complementar

- Microsoft. *Deprecated features for Windows client*. Microsoft Learn. <https://learn.microsoft.com/en-us/windows/whats-new/deprecated-features> — linha NTLM (junho de 2024; atualização de novembro de 2024). *(Lido em 2026-11-05.)*
- R. Noureen. *Microsoft Details NTLM Phase-Out Plan in Windows*. Petri, 2026.
- NIST. *SP 800-128* — gestão de configuração.
- Microsoft. *Active Directory Forest Recovery Guide*.

### Aplicação prática

- Classifique os servidores de um ambiente que você conhece em plano de controle, servidores e estações, e verifique se as contas que administram cada grupo são diferentes.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
