---
id: M01-L05
title: "PKI, certificados, TLS e gerenciamento de chaves"
description: Como a infraestrutura de chaves públicas estabelece confiança, como o TLS a usa, por que certificados de validade cada vez mais curta exigem automação e como gerenciar o ciclo de vida de chaves e certificados em escala.
domain: security-foundations
tier: fundamental
status: published
prerequisites: [M01-L04, M00-L03]
objectives:
  - Explicar a cadeia de certificados, as âncoras de confiança e a validação feita pelo cliente.
  - Descrever o que o handshake TLS estabelece e o que o mTLS acrescenta.
  - Planejar a gestão do ciclo de vida de certificados diante da redução da validade máxima.
  - Definir requisitos de proteção e rotação de chaves privadas.
minutes: 75
sources: [RFC-9846, NIST-SP800-57-PT1-R5, NIST-SP1800-16, CABF-SC081]
further_reading: [BOOK-ANDERSON-SE3, NIST-FIPS-203]
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
module: M01
---

# PKI, certificados, TLS e gerenciamento de chaves

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 · M01-L05</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">75 min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    A criptografia assimétrica resolve a distribuição de chaves, mas cria outra pergunta: **como saber que esta chave pública é mesmo do meu banco?** A infraestrutura de chaves públicas (PKI) responde com certificados emitidos por autoridades em quem o cliente já confia. Esta aula explica como essa cadeia funciona, como o TLS a usa, e por que a gestão de certificados deixou de ser uma tarefa anual: a validade máxima de certificados públicos está caindo de 398 para 47 dias até 2029.

**Pré-requisitos:** [Criptografia aplicada](04-applied-cryptography.md) e [Segmentação e conectividade](../00-foundations/03-segmentation-connectivity.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar a cadeia de certificados, as âncoras de confiança e a validação feita pelo cliente.
- Descrever o que o handshake TLS estabelece e o que o mTLS acrescenta.
- Planejar a gestão do ciclo de vida de certificados diante da redução da validade máxima.
- Definir requisitos de proteção e rotação de chaves privadas.

## Conceito

### Certificados e autoridades

Um **certificado X.509** vincula uma chave pública a uma identidade (um nome de domínio, um serviço, uma pessoa), com prazo de validade, e é **assinado por uma autoridade certificadora (CA)**. Quem confia na CA pode confiar no vínculo.

As CAs formam uma **cadeia**: uma **CA raiz**, cuja chave fica guardada com o máximo de proteção (frequentemente offline, em HSM), assina **CAs intermediárias**, que emitem os certificados de servidores e usuários. O cliente confia na raiz porque ela está no seu **repositório de confiança** (*trust store*) — a **âncora de confiança**.

| Tipo de PKI | Quem confia | Uso típico |
|:---|:---|:---|
| **Pública** | Navegadores e sistemas operacionais do mundo inteiro | Sites e APIs públicas |
| **Privada (corporativa)** | Apenas os dispositivos em que a organização instala sua raiz | mTLS entre serviços internos, VPN, Wi-Fi corporativo, assinatura interna |

### O que o cliente valida

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m01-l05-pki-tls.mmd"
```

<figcaption>Figura 1 — Cadeia de certificados e validação durante o handshake TLS.</figcaption>
</figure>

Ao receber o certificado, o cliente verifica: (1) que a cadeia leva a uma raiz confiável; (2) que o nome no certificado corresponde ao servidor acessado; (3) que está dentro da validade; (4) que não foi revogado. Só então confia na chave pública apresentada.

Muitos incidentes vêm de **desligar** essas verificações — por exemplo, em integrações em que a validação foi desativada "para funcionar" em homologação e chegou à produção. Um cliente que não valida o certificado aceita qualquer servidor, inclusive um atacante no meio do caminho.

## Fundamentos técnicos

### TLS e mTLS

O **TLS 1.3** é especificado hoje pelo RFC 9846 (julho de 2026), que substituiu o RFC 8446. No caso mais comum — o handshake completo com **autenticação por certificado** —, cliente e servidor negociam os parâmetros e fazem uma **troca de chaves Diffie-Hellman efêmera**; o servidor envia seu certificado e prova que possui a chave privada correspondente **assinando todo o handshake** (mensagem *CertificateVerify*). Os dois lados derivam então **chaves de sessão** que cifram e autenticam o tráfego.

Como a troca de chaves é efêmera, esse modo tem **forward secrecy**: se a chave privada do certificado do servidor for comprometida no futuro, sessões gravadas no passado continuam protegidas, porque as chaves de sessão não podem ser recalculadas a partir dela. Observe que a chave do certificado serve para **autenticar** o servidor, não para cifrar o tráfego.

!!! note "Aprofundamento — modos com chave pré-compartilhada (PSK)"

    O TLS 1.3 também aceita uma **chave pré-compartilhada (PSK)** — normalmente obtida em uma conexão anterior, para retomar a sessão sem repetir a autenticação por certificado. O RFC 9846 (§2.2) descreve três modos de troca de chaves: assimétrica (Diffie-Hellman), PSK sozinha e PSK combinada com Diffie-Hellman. Usada sozinha, a PSK **perde a forward secrecy** para os dados da aplicação; combinada com a troca efêmera, a mantém. Os dados enviados logo na primeira mensagem (*0-RTT*, §2.3) não têm garantia de forward secrecy e podem ser **reenviados por um atacante** (*replay*). Por isso, forward secrecy é uma propriedade do **modo** de troca de chaves configurado, e não do TLS 1.3 em qualquer circunstância.

No **mTLS**, o servidor também pede um certificado ao cliente (*CertificateRequest*), e o cliente prova a posse da chave privada da mesma forma. A autenticação do cliente é opcional no protocolo; quando usada, o mTLS se torna um dos mecanismos mais adotados para autenticar serviços entre si e parceiros, porque não depende de segredos compartilhados.

### Revogação e validade curta

Quando uma chave privada vaza, o certificado precisa ser **revogado** antes do vencimento. Os mecanismos de revogação (listas de revogação e consulta online) têm limitações práticas de disponibilidade e privacidade — e muitos clientes não os verificam de forma rigorosa. A resposta da indústria tem sido **reduzir a validade**: um certificado que vale poucas semanas limita a janela de abuso de uma chave vazada.

Em abril de 2025, o CA/Browser Forum aprovou a **Ballot SC081v3**, que reduz a validade máxima de certificados TLS públicos de 398 para **47 dias**, em etapas de março de 2026 a março de 2029. Segundo a base de conhecimento da DigiCert, as etapas são: 200 dias a partir de 15/03/2026, 100 dias a partir de 15/03/2027 e 47 dias a partir de 15/03/2029. Na data desta aula (outubro de 2026), a validade máxima de um certificado público é de **200 dias**.

A consequência arquitetural é direta: **renovação manual deixa de ser viável**. Emissão, instalação e renovação precisam ser automatizadas, e o inventário de certificados precisa ser completo.

### Gestão do ciclo de vida

O NIST SP 1800-16 (NCCoE, 2020) trata exatamente o problema de organizações com milhares de certificados TLS: inventário, propriedade, automação e resposta a incidentes. As etapas do ciclo:

| Etapa | Pergunta | Falha típica |
|:---|:---|:---|
| Inventário | Quais certificados existem, onde e quem é o dono? | Certificado desconhecido vence e derruba integração |
| Emissão | De qual CA, com quais parâmetros? | Certificados com algoritmos fracos ou nomes coringa amplos demais |
| Instalação | Como a chave privada chega ao servidor? | Chave enviada por e-mail |
| Renovação | Automática? Com quanta antecedência? | Renovação manual esquecida |
| Revogação | Como revogar e substituir rápido? | Ninguém sabe onde a chave vazada foi usada |

### Chaves privadas

O NIST SP 800-57 Part 1 Rev. 5 orienta o gerenciamento de chaves ao longo do ciclo de vida, incluindo o **cryptoperiod** de cada tipo de chave. Requisitos usuais:

- Chaves de CA raiz e de assinatura de alto valor em **HSM**, com controle de múltiplas pessoas.
- Chaves de servidores geradas no próprio servidor (ou no KMS) e **nunca** transmitidas.
- Rotação compatível com o cryptoperiod e a validade dos certificados.
- Uma chave por finalidade: a mesma chave não deve cifrar e assinar.

## Exemplo empresarial

!!! example "Meridiana — a madrugada em que as entregas pararam"

    Numa segunda-feira, os coletores dos três centros de distribuição deixaram de registrar entregas. A causa: o certificado do servidor de integração com a transportadora venceu no domingo. Ninguém sabia que ele existia; tinha sido instalado por um consultor três anos antes.

    A recuperação levou nove horas — descobrir o problema, achar quem tinha acesso ao painel da CA, emitir, instalar e reiniciar. O arquiteto propôs:

    1. **Inventário automático** de certificados por varredura de rede e consulta às CAs.
    2. **Dono** para cada certificado, com alerta a 30, 15 e 7 dias.
    3. **Renovação automática** via protocolo ACME para certificados públicos e para a PKI interna.
    4. Plano para os sistemas que não suportam automação: proxy reverso que termina TLS e é renovado automaticamente.

    Com a validade máxima caindo para 200 dias em 2026 e 47 dias em 2029, a mesma falha se repetiria várias vezes por ano sem essas mudanças.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Inventário | Planilha incompleta | Descoberta automática e dono por certificado |
| Renovação | Manual, anual | Automática (ACME ou integração com a CA) |
| Validação | Desativada em integrações problemáticas | Sempre ativa; problemas corrigidos na causa |
| Autenticação entre serviços | Senha ou chave de API compartilhada | mTLS com PKI interna |
| Chaves de CA | Em servidor comum | Em HSM, raiz offline, controle de múltiplas pessoas |

## Aplicabilidade: on-premises, cloud e híbrido

| Ambiente | O que muda |
|:---|:---|
| **On-premises** | PKI interna (por exemplo, integrada ao diretório) e HSMs próprios. |
| **Cloud** | Serviços gerenciados de certificados e de CA privada; balanceadores renovam certificados automaticamente; meshes emitem certificados de vida curtíssima para workloads. |
| **Híbrido** | É preciso decidir quais raízes cada ambiente confia; serviços em cloud chamando o datacenter por mTLS precisam confiar na PKI interna, e vice-versa. |

## Como especificar e implementar

- "Todo certificado tem dono, está no inventário e é renovado automaticamente; certificados que não suportam automação são exceções registradas."
- "Validação de certificados é obrigatória em todos os clientes TLS; desativá-la é proibido em qualquer ambiente."
- "Serviços internos que trocam dados confidenciais autenticam-se com mTLS emitido pela PKI corporativa."
- "Chaves de CA e de assinatura de alto valor são mantidas em HSM com controle de dupla custódia."

## Trade-offs, limitações e antipadrões

- **Automação concentra risco:** a conta que emite certificados automaticamente é uma credencial poderosa e precisa de proteção forte.
- **Certificados coringa** (`*.example.com`) simplificam, mas ampliam o impacto de um vazamento.
- **Antipadrão — "pinning" rígido** de certificados de servidor em aplicativos, que quebra a cada renovação.
- **Antipadrão — PKI interna sem dono**, com raiz em um servidor qualquer.

## Como validar

- Comparar o inventário de certificados com uma varredura das portas TLS da organização.
- Listar certificados que vencem nos próximos 30 dias e verificar se a renovação é automática.
- Testar clientes com um certificado inválido em ambiente de teste — a conexão deve falhar.
- Verificar onde estão as chaves privadas das CAs e quem pode usá-las.

## Como apresentar e justificar

- **Para engenharia:** "Com validade de 200 dias hoje e 47 em 2029, só a automação via ACME é viável; vamos começar pelo inventário."
- **Para gestores:** "A parada de nove horas nos centros de distribuição foi causada por um certificado esquecido. Com as novas regras do mercado, isso aconteceria várias vezes por ano. A automação elimina esse risco."

## Checklist de revisão arquitetural

- [ ] Inventário completo de certificados, com dono.
- [ ] Renovação automática e alertas de vencimento.
- [ ] Validação de certificados ativa em todos os clientes.
- [ ] mTLS nas integrações entre serviços que trocam dados sensíveis.
- [ ] Chaves de CA e de alto valor em HSM.
- [ ] Processo de revogação e substituição testado.

## Questões de compreensão

**1.** Por que o cliente confia em um certificado emitido por uma CA intermediária que ele não conhece?

??? success "Resposta comentada"

    Porque a CA intermediária tem um certificado assinado pela CA raiz, que está no repositório de confiança do cliente. O cliente valida a cadeia até essa âncora.

**2.** O que é forward secrecy e por que é importante?

??? success "Resposta comentada"

    É a propriedade de que o comprometimento futuro da chave privada de longo prazo do servidor não permite decifrar sessões passadas, porque as chaves de sessão foram derivadas de trocas efêmeras. Protege o tráfego gravado por um atacante. No TLS 1.3, ela existe nos modos com troca efêmera (o handshake completo por certificado e a PSK combinada com Diffie-Hellman), mas não quando uma PSK é usada sozinha nem para dados *0-RTT*.

**3.** Por que a redução da validade de certificados é, ao mesmo tempo, uma melhoria de segurança e um risco operacional?

??? success "Resposta comentada"

    Melhora a segurança porque limita a janela de uso de uma chave vazada, compensando as limitações da revogação. É um risco operacional porque multiplica as renovações; sem inventário e automação, aumenta a chance de vencimentos que derrubam serviços.

## Exercício de tomada de decisão

!!! question "Cenário: autenticação entre a API de pedidos e o serviço de pagamentos da Aurora"

    Hoje, a API de pedidos chama o serviço de pagamentos enviando uma chave de API fixa no cabeçalho. Opções: (A) manter a chave, guardando-a no gerenciador de segredos e rotacionando-a a cada 90 dias; (B) mTLS com certificados emitidos pela PKI interna, renovados automaticamente a cada 30 dias; (C) tokens de curta duração emitidos pelo provedor de identidade para a identidade do serviço (OAuth 2.0 client credentials), sobre TLS. A Aurora já tem um provedor de identidade com suporte a OAuth 2.0, mas ainda não tem PKI interna com emissão automatizada. Critérios: eliminação de segredo compartilhado de longa duração, autorização com escopo e esforço de implantação com a infraestrutura atual.

??? success "Resolução de referência"

    | Critério | Peso | A — Chave no cofre, rotação de 90 dias | B — mTLS com PKI interna | C — Tokens OAuth 2.0 de curta duração |
    |:---|:---|:---|:---|:---|
    | Eliminação de segredo compartilhado de longa duração | 3 | 1 | 3 | 2 |
    | Autorização com escopo | 2 | 1 | 1 | 3 |
    | Esforço de implantação com a infraestrutura atual | 2 | 3 | 1 | 2 |
    | **Total ponderado** | | **11** | **13** | **16** |

    **Recomendação: C agora; B e C combinadas como destino.** C recebe 2 no primeiro critério porque o serviço ainda usa uma credencial de cliente para obter tokens — mas ela fica só entre o serviço e o provedor de identidade, e o que trafega até o serviço de pagamentos expira em minutos. A é uma melhoria mínima.

    - **A** reduz a exposição da chave, mas mantém um segredo compartilhado de longa duração.
    - **B** autentica os dois lados sem segredo compartilhado e protege o canal; exige PKI interna e automação.
    - **C** traz autorização com escopo (o token diz o que o serviço pode fazer) e integra com a identidade corporativa; exige que o serviço de pagamentos valide tokens.

    Em arquiteturas maduras, **B e C se combinam**: mTLS autentica o canal e a identidade do workload; o token carrega a autorização. A escolha inicial depende da infraestrutura já disponível — o tema volta no M06 e no M12.

## Pontos-chave

- Certificados vinculam chaves públicas a identidades; a confiança vem de uma cadeia até a âncora no trust store.
- O cliente valida cadeia, nome, validade e revogação — desligar essa validação anula o TLS.
- No TLS 1.3 (RFC 9846), o handshake completo por certificado usa troca de chaves efêmera e tem forward secrecy; modos só com PSK e dados 0-RTT não têm essa garantia. O mTLS autentica também o cliente.
- A validade máxima de certificados públicos cai para 47 dias até 2029 (200 dias em 2026): automação e inventário são obrigatórios.
- Chaves de alto valor ficam em HSM, com controle de múltiplas pessoas.

## Referências

### Fundamentação principal

- E. Rescorla. *RFC 9846 — The Transport Layer Security (TLS) Protocol Version 1.3*. IETF, julho de 2026 (obsoleta o RFC 8446). <https://www.rfc-editor.org/rfc/rfc9846.html> — §2 *Protocol Overview* (autenticação do servidor e, opcionalmente, do cliente; *CertificateVerify* como assinatura de todo o handshake), §2.2 (PSK sozinha perde a forward secrecy) e §2.3 (dados 0-RTT sem forward secrecy e sem proteção contra replay). *(Seções lidas em 2026-10-27.)*
- NIST. *SP 800-57 Part 1 Rev. 5*. 2020. <https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final> — ciclo de vida e cryptoperiods. *(Página oficial conferida.)*
- NIST NCCoE. *SP 1800-16 — Securing Web Transactions: TLS Server Certificate Management*. 2020. <https://csrc.nist.gov/pubs/sp/1800/16/final> — gestão de certificados em escala. *(Página oficial conferida.)*
- CA/Browser Forum. *Ballot SC081v3*. Aprovada em 11/04/2025. <https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/> — redução da validade para 47 dias até 2029. Etapas intermediárias conferidas em DigiCert, *Public TLS certificates: 199-day validity* <https://knowledge.digicert.com/alerts/public-tls-certificates-199-day-validity> (fonte secundária).

### Leitura complementar

- R. Anderson. *Security Engineering*, 3ª ed. Cap. 4 *Protocols* e Cap. 5 *Cryptography* *(localizados pelo sumário)*.
- NIST. *FIPS 203, 204 e 205* (2024) — algoritmos pós-quânticos que serão incorporados a certificados e ao TLS.

### Aplicação prática

- Comece pelo inventário: uma varredura das portas TLS da rede, cruzada com os registros das CAs usadas, mostra os certificados sem dono.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-27 |
