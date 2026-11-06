---
id: M08-L06
title: "Aula 06 — Protocolos inseguros e dependências legadas"
public_title: "Módulo 8 — Aula 06 — Protocolos inseguros e dependências legadas"
description: Como encontrar e remover protocolos inseguros — NTLM, SMBv1, TLS 1.0 e 1.1, LDAP simples, Telnet e FTP — sem interromper a operação, por meio de auditoria de uso, correção de dependências, desabilitação gradual e monitoração de exceções.
domain: infrastructure-foundations
tier: professional
status: published
prerequisites: [M08-L03, M01-L05]
objectives:
  - Identificar os protocolos legados mais comuns e por que são inseguros.
  - Aplicar o ciclo auditar, corrigir, desabilitar e monitorar.
  - Priorizar a remoção pelo risco e pelo esforço.
  - Tratar dependências que não podem ser removidas no curto prazo.
minutes: 60
sources: [RFC-8996, MS-WINDOWS-DEPRECATED-FEATURES, PETRI-NTLM-2026, CISA-STOPRANSOMWARE-GUIDE, MS-KERBEROASTING-2024, NIST-SP800-53, CIS-CONTROLS-V8-1, MS-PROTECTED-USERS]
further_reading: [RFC-9846, NSA-NETWORK-INFRA-2022, RFC-4120]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M08
---

# Aula 06 — Protocolos inseguros e dependências legadas { #protocolos-inseguros-e-dependencias-legadas }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 8 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M08-L06</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Protocolos legados permanecem habilitados por um motivo simples: ninguém sabe o que vai quebrar se forem desligados. Enquanto isso, continuam oferecendo caminhos para roubo de credenciais, interceptação e movimento lateral. Esta aula apresenta os protocolos mais comuns nessa situação e um método repetível — auditar, corrigir, desabilitar, monitorar — que transforma "não sabemos o que quebra" em uma lista de dependências com donos.

**Pré-requisitos:** [Windows, Linux e AD](03-windows-linux-ad.md) e [PKI, TLS e gestão de chaves](../01-security-fundamentals/05-pki-tls-key-management.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Identificar os protocolos legados mais comuns e por que são inseguros.
- Aplicar o ciclo auditar, corrigir, desabilitar e monitorar.
- Priorizar a remoção pelo risco e pelo esforço.
- Tratar dependências que não podem ser removidas no curto prazo.

## Conceito

### Os suspeitos de sempre

| Protocolo | Problema | Substituto | Referência |
|:---|:---|:---|:---|
| **NTLM** | Vetor persistente de roubo de credenciais e movimento lateral, segundo a Microsoft citada pela imprensa especializada | Kerberos (via Negotiate) | Recurso obsoleto do Windows desde junho de 2024; NTLMv1 removido no Windows 11 24H2 e no Windows Server 2025 (Microsoft Learn) |
| **SMBv1** | Protocolo antigo; o guia recomenda desabilitá-lo, migrar para SMBv3 e bloquear o acesso externo ao SMB (porta TCP 445) | SMBv3 | #StopRansomware Guide |
| **TLS 1.0 e 1.1** | Integridade do handshake e autenticação dependentes de SHA-1; sem cifras AEAD; formalmente descontinuados | TLS 1.2 e 1.3 | RFC 8996 |
| **RC4 no Kerberos** | Facilita a quebra de senhas de contas de serviço | AES | Microsoft, 2024 |
| **LDAP simples sem TLS** | Credenciais em claro na rede | LDAP sobre TLS ou com assinatura | Módulo 6 — Aula 03 |
| **Telnet, FTP, HTTP** | Credenciais e dados em claro | SSH, SFTP, HTTPS | Módulo Inicial — Aula 02 |

A RFC 8996 (BCP 195), de março de 2021, estabelece que **TLS 1.0 e TLS 1.1 não devem ser usados** (*MUST NOT*, Sec. 4 e 5), citando na Sec. 1 a dependência de SHA-1 para a integridade do handshake e a autenticação, a ausência de cifras AEAD, cifras obrigatórias que já não são desejáveis e o risco de configurações erradas ao manter várias versões. A versão atual do TLS 1.3 é a RFC 9846 (Módulo 1 — Aula 05).

Sobre NTLM, a evidência oficial é a lista de recursos obsoletos do Windows: todas as versões (LANMAN, NTLMv1 e NTLMv2) estão obsoletas desde junho de 2024 e não recebem desenvolvimento de novos recursos; o uso continua funcionando, e a orientação é substituir chamadas a NTLM por Negotiate, que tenta Kerberos e só recorre a NTLM quando necessário; desde novembro de 2024, a mesma página registra a remoção do NTLMv1 a partir do Windows 11 24H2 e do Windows Server 2025. Depois disso, segundo imprensa especializada que relatou um post da Microsoft (o texto original não pôde ser conferido nesta revisão), a empresa anunciou um plano em fases — auditoria aprimorada, novos recursos de Kerberos para cenários que hoje recorrem a NTLM e bloqueio do NTLM de rede por padrão em versões futuras do Windows —, ressaltando que desabilitar por padrão ainda não significa remover o protocolo.

## Fundamentos técnicos

### O ciclo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m08-l06-protocol-migration.mmd"
```

<figcaption>Figura 1 — Auditar o uso, corrigir dependências, desabilitar com reversão e monitorar exceções.</figcaption>
</figure>

| Etapa | Atividades | Saída |
|:---|:---|:---|
| **1. Auditar** | Habilitar registro de uso do protocolo; coletar por semanas, incluindo fechamentos mensais | Lista de origens, destinos e aplicações |
| **2. Corrigir** | Atualizar configuração, aplicação ou equipamento; envolver donos e fornecedores | Dependências eliminadas ou com plano |
| **3. Desabilitar** | Piloto, depois produção, por ondas; reversão preparada | Protocolo desligado nos escopos prontos |
| **4. Monitorar** | Alertas para tentativas de uso; exceções com dono e prazo | Garantia de que não volta |

O artigo sobre o plano da Microsoft lista exatamente essas ações para NTLM: ativar a auditoria para mapear o uso, inventariar aplicações e dispositivos dependentes, priorizar a migração para Kerberos, atualizar ou substituir sistemas que não suportam protocolos seguros e testar configurações com NTLM desabilitado em ambientes controlados.

### Priorização

| Critério | Pergunta |
|:---|:---|
| **Exposição** | O protocolo é alcançável de redes menos confiáveis? |
| **Credenciais** | Ele expõe ou facilita o roubo de credenciais privilegiadas? |
| **Uso real** | A auditoria mostra pouco ou nenhum uso legítimo? |
| **Esforço** | As dependências são de configuração (rápidas) ou de produto (lentas)? |

Em geral, a ordem que mais reduz risco por esforço é: protocolos **sem uso** (desligar já), protocolos com **credenciais em claro** em redes compartilhadas, protocolos ligados a **credenciais privilegiadas** (NTLM, RC4), e por fim os que dependem de troca de produto.

### Dependências que ficam

Quando um sistema não pode deixar o protocolo no curto prazo:

- **Restringir** o uso ao par origem-destino necessário (por política e por firewall).
- **Cifrar o canal** (por exemplo, IPsec entre os dois hosts) quando o protocolo é em claro.
- **Monitorar** o uso, com alerta para qualquer origem nova.
- **Registrar a exceção** com dono e prazo (Aula 05).

## Exemplo empresarial

!!! example "Aurora Pagamentos — TLS 1.0 no parceiro"

    A Aurora decidiu desabilitar TLS 1.0 e 1.1 em todos os endpoints. A auditoria de 30 dias mostrou que 99,6% das conexões já usavam TLS 1.2 ou 1.3; o restante vinha de dois parceiros com sistemas antigos e de um monitor de disponibilidade interno.

    O monitor foi atualizado em um dia. Os parceiros receberam comunicação com 90 dias de prazo; um migrou, o outro recebeu um endpoint dedicado com TLS 1.2 obrigatório e suporte técnico da Aurora para atualizar a biblioteca. Na data marcada, as versões antigas foram desligadas; a monitoração registrou três tentativas na semana seguinte, todas do mesmo parceiro atrasado, já em contato.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Decisão | "Não mexe, pode quebrar" | Auditoria de uso, depois decisão |
| Remoção | Big bang ou nunca | Ondas com piloto e reversão |
| Dependências | Desconhecidas | Listadas, com dono e plano |
| Exceções | Permanentes | Restritas, monitoradas, com prazo |
| Pós-remoção | Sem acompanhamento | Alertas para tentativas de uso |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias para a remoção de protocolos legados:

| Controle ou padrão | Objetivo na remoção de protocolos | Referência |
|:---|:---|:---|
| Funcionalidade mínima | Proibir ou restringir protocolos e serviços desnecessários ou inseguros | SP 800-53: CM-7 (Least Functionality) |
| Parâmetros de configuração | Protocolos permitidos definidos na baseline, com desvios aprovados | SP 800-53: CM-6 (Configuration Settings) |
| Comunicação protegida | Confidencialidade e integridade na transmissão por criptografia | SP 800-53: SC-8 e SC-8(1) (Cryptographic Protection) |
| Criptografia adequada | Usar os tipos de criptografia definidos — sem SHA-1 no handshake nem RC4 | SP 800-53: SC-13 (Cryptographic Protection) |
| Autenticação resistente a repetição | Mecanismos de autenticação resistentes a repetição e retransmissão | SP 800-53: IA-2(8) (Access to Accounts — Replay Resistant) |
| Proteção de dados em trânsito | Cifrar dados sensíveis em trânsito | CIS v8.1: Controle 3 (Data Protection) |
| TLS 1.0 e 1.1 | Não usar TLS 1.0 nem 1.1 | RFC 8996 (BCP 195), Sec. 4 e 5 |

## Aplicabilidade: on-premises, cloud e híbrido

Protocolos legados concentram-se on-premises, mas aparecem em cloud em balanceadores com políticas de TLS antigas, bancos gerenciados com versões permissivas e máquinas virtuais migradas sem mudança. Serviços de cloud costumam oferecer políticas de segurança de TLS predefinidas — escolha as que excluem versões antigas. Em ambientes híbridos, integrações entre datacenter e nuvem são um lugar comum para protocolos legados "temporários".

## Como especificar e implementar

- "TLS 1.0 e 1.1 não são aceitos em nenhum endpoint; exceções exigem aprovação, escopo restrito e prazo."
- "SMBv1 está desabilitado em todos os sistemas; portas SMB são bloqueadas no perímetro."
- "O uso de NTLM e de RC4 no Kerberos é auditado e reduzido em ondas, com meta de desabilitação."
- "Protocolos que transmitem credenciais em claro não são permitidos fora de canais cifrados."
- "Tentativas de uso de protocolos desabilitados geram alertas."

## Trade-offs, limitações e antipadrões

- **Trade-off:** auditorias longas aumentam a confiança, mas adiam a redução de risco; 30 dias cobrindo um fechamento mensal costuma bastar.
- **Antipadrão — desabilitar sem auditar:** quebra uma integração crítica e gera a reversão total.
- **Antipadrão — exceção global para um sistema.**
- **Limitação:** alguns equipamentos só falam protocolos legados; restam o isolamento e o monitoramento.

## Como validar

- Verificar a configuração de TLS dos endpoints públicos e internos.
- Consultar os registros de auditoria de NTLM e SMBv1 após a desabilitação.
- Testar uma conexão com protocolo antigo e verificar o alerta.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhum endpoint aceita TLS 1.0 ou 1.1 fora das exceções | Varredura de configuração TLS de endpoints públicos e internos |
| SMBv1 desabilitado fora das exceções restritas | Consulta de configuração e de registros de auditoria |
| Uso de NTLM abaixo da meta da onda | Registros de auditoria de NTLM comparados à meta |
| Tentativa de uso de protocolo desabilitado gera alerta | Teste com o alerta registrado |
| Toda exceção com dono, par origem-destino e prazo | Lista de exceções revisada |

## Como apresentar e justificar

- **Para a diretoria:** "Esses protocolos facilitam o roubo de senhas e o avanço de ataques. Removemos em etapas, com auditoria antes, para não interromper o negócio."
- **Para a operação:** "Primeiro medimos quem usa. Só desligamos o que tem dono avisado e alternativa pronta."

## Checklist de revisão arquitetural

- [ ] Inventário de protocolos legados e seu uso real.
- [ ] Dependências com dono e plano.
- [ ] Desabilitação por ondas, com reversão.
- [ ] Exceções restritas, monitoradas e com prazo.
- [ ] Alertas para tentativas de uso.

## Questões de compreensão

**1.** Por que TLS 1.0 e 1.1 foram descontinuados?

??? success "Resposta comentada"

    Segundo a RFC 8996, porque sua integridade depende de SHA-1, exigem cifras legadas sem suporte a cifras AEAD modernas e manter várias versões aumenta o risco de configuração incorreta.

**2.** Qual a primeira etapa antes de desabilitar NTLM?

??? success "Resposta comentada"

    Auditar o uso para mapear quais sistemas e aplicações ainda dependem dele, inventariar essas dependências e testar configurações com NTLM desabilitado em ambiente controlado.

**3.** O que fazer com um sistema que não pode deixar um protocolo em claro no curto prazo?

??? success "Resposta comentada"

    Restringir o uso ao par origem-destino necessário, cifrar o canal (por exemplo, com IPsec), monitorar o uso e registrar a exceção com dono e prazo.

## Exercício de tomada de decisão

!!! question "Cenário: SMBv1 e NTLM na Meridiana"

    A auditoria da Meridiana encontrou SMBv1 em uso apenas pelo servidor de etiquetas (legado) e NTLM em 18% das autenticações, concentrado em três aplicações antigas e em impressoras multifuncionais. Para o NTLM, as estratégias em discussão são:

    - **A** — desabilitar o NTLM em todo o domínio de uma vez, com exceções por política para o que quebrar;
    - **B** — ondas: contas privilegiadas primeiro (grupo Protected Users, que não autentica por NTLM), depois por aplicação, e por fim a restrição do NTLM no domínio, com exceções restritas;
    - **C** — manter o NTLM e só monitorar até as aplicações antigas serem trocadas.

    Compare as estratégias com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e proponha a sequência de ações para SMBv1 e NTLM.

**Objetivos avaliados:** Aplicar o ciclo auditar, corrigir, desabilitar e monitorar; priorizar a remoção pelo risco e pelo esforço.

**Entrega esperada:** Matriz ponderada e a sequência de ações para SMBv1 e NTLM, com os critérios de cada onda.

**Critérios de avaliação:**

- A sequência começa por auditoria de uso e corrige dependências antes de desabilitar.
- As contas privilegiadas saem do NTLM primeiro; a restrição no domínio inteiro fica por último.
- As exceções são restritas a pares origem-destino e monitoradas.

??? success "Resolução de referência"

    | Critério | Peso | A — Desabilitar de uma vez | B — Ondas, privilegiadas primeiro | C — Só monitorar |
    |:---|:---|:---|:---|:---|
    | Redução do risco sobre credenciais privilegiadas | 3 | 3 | 3 | 1 |
    | Risco de interrupção (impressoras, aplicações) | 3 | 1 | 3 | 3 |
    | Tempo até o efeito | 2 | 3 | 2 | 1 |
    | Esforço | 1 | 2 | 1 | 3 |
    | **Total ponderado** | | **20** | **23** | **17** |

    - **Pesos:** NTLM preocupa pelo roubo e reaproveitamento de credenciais privilegiadas (peso 3), e uma quebra em impressoras e aplicações antigas leva à reversão (peso 3). O tempo pesa 2; o esforço, 1.
    - **Recomendação: B**, na sequência a seguir.

    1. **SMBv1:** desabilitar em todos os sistemas exceto o servidor de etiquetas e o único destino com que ele conversa; dentro da zona de legados (Aula 05), restringir o fluxo SMBv1 a esse par e monitorar; remover junto com a substituição do servidor.
    2. **NTLM — impressoras:** atualizar firmware e configurar autenticação Kerberos ou digitalização para destino sem autenticação NTLM; onde não for possível, segmento próprio e conta de serviço dedicada sem privilégios.
    3. **NTLM — aplicações:** com donos e fornecedores, corrigir configurações (nomes de serviço, SPNs) que forçam NTLM; para a aplicação que não suporta Kerberos, exceção restrita.
    4. **Reduzir o NTLM em ondas:** primeiro as contas privilegiadas (Protected Users); depois as aplicações corrigidas, com o NTLM de entrada restrito nos servidores de cada onda; a restrição no domínio inteiro, a partir dos controladores de domínio, fica por último, porque é a de maior impacto.
    5. **Monitorar** tentativas de NTLM e SMBv1 com alertas, e revisar a meta trimestralmente.

    - **Trade-off aceito e risco residual:** enquanto as ondas avançam, contas não privilegiadas e as aplicações em exceção continuam usando NTLM; o residual é tratado pela restrição das exceções a pares origem-destino e pelo alerta para usos novos.
    - **O que mudaria a decisão:** um incidente com retransmissão de credenciais NTLM aceleraria a onda de contas privilegiadas e aproximaria A; se a versão do Windows adotada passar a bloquear o NTLM de rede por padrão, o plano precisa terminar as exceções antes da atualização.

    **Erros comuns:**

    - Desabilitar o NTLM no domínio de uma vez, sem inventário de dependências.
    - Manter o protocolo indefinidamente "até trocar as aplicações", sem meta.
    - Esquecer impressoras e dispositivos que autenticam por NTLM.

## Pontos-chave

- NTLM, SMBv1, TLS 1.0/1.1, RC4, LDAP simples e protocolos em claro são os alvos mais comuns.
- O ciclo é auditar, corrigir, desabilitar e monitorar.
- Priorize por exposição, relação com credenciais, uso real e esforço.
- Dependências que ficam são restritas, cifradas, monitoradas e têm prazo.
- Desabilitar sem auditar provoca reversões que atrasam tudo.

## Referências

### Fundamentação principal

- IETF. *RFC 8996 — Deprecating TLS 1.0 and TLS 1.1*. 2021. <https://www.rfc-editor.org/rfc/rfc8996.html> — Sec. 1, 4 e 5. *(Lido; reconferido em 2026-10-29.)*
- Microsoft. *Deprecated features for Windows client*. Microsoft Learn. <https://learn.microsoft.com/en-us/windows/whats-new/deprecated-features> — linha NTLM: obsolescência (junho de 2024), substituição por Negotiate e remoção do NTLMv1 no Windows 11 24H2 e no Windows Server 2025 (atualização de novembro de 2024). *(Lido em 2026-11-05; fonte primária.)*
- R. Noureen. *Microsoft Details NTLM Phase-Out Plan in Windows: How IT Teams Can Prepare*. Petri, 02/02/2026. *(Lido; fonte secundária para o plano em fases.)*
- CISA, FBI, NSA, MS-ISAC. *#StopRansomware Guide*. 2023 — SMBv1. *(Lido.)*
- D. Weston, V. Sun. *Microsoft's guidance to help mitigate Kerberoasting*. 2024 — RC4. *(Lido.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles CM-6, CM-7, IA-2(8), SC-8, SC-8(1) e SC-13, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controle 3 — gratuito.
- Microsoft. *Protected Users Security Group*. Microsoft Learn, 2025. <https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group> — membros não autenticam por NTLM nem usam RC4; não incluir contas de serviço ou de computador. *(Lido.)*

### Leitura complementar

- IETF. *RFC 9846 — TLS 1.3*.
- NSA. *Network Infrastructure Security Guidance* — protocolos de gerenciamento.
- IETF. *RFC 4120 — Kerberos V5*.

### Aplicação prática

- Escolha um protocolo legado do seu ambiente, habilite a auditoria por 30 dias (em ambiente de teste, se necessário) e produza a lista de dependências com dono e ação proposta.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
