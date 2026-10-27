---
id: M00-L03
title: "Segmentação e conectividade: VLAN, roteamento, VPN, TLS e firewalls"
description: Como redes são divididas em zonas e como a comunicação entre zonas e entre locais é controlada — VLANs, roteamento entre zonas, firewalls stateful, VPN e TLS.
domain: infrastructure-foundations
tier: fundamental
status: published
prerequisites: [M00-L02]
objectives:
  - Explicar como VLANs criam domínios separados na camada 2 e por que a comunicação entre elas exige roteamento.
  - Descrever o funcionamento de um firewall stateful e a estrutura de uma política entre zonas.
  - Diferenciar VPN site-to-site, VPN de acesso remoto e TLS quanto ao que protegem.
  - Avaliar um desenho de rede quanto a zonas, pontos de controle e fluxos permitidos.
minutes: 75
sources: [NIST-SP800-41-R1, RFC-9846, NIST-SP800-215]
further_reading: [NIST-SP800-207, BOOK-ANDERSON-SE3]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M00
---

# Segmentação e conectividade: VLAN, roteamento, VPN, TLS e firewalls

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 · M00-L03</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">75 min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Uma rede plana — em que tudo alcança tudo — transforma o comprometimento de uma única estação em acesso a toda a empresa. **Segmentação** é a decisão de dividir a rede em zonas e só permitir entre elas os fluxos necessários. Esta aula explica os blocos com que isso é feito — VLANs, roteamento, firewalls — e como VPN e TLS protegem a comunicação quando ela precisa atravessar redes não confiáveis.

**Pré-requisitos:** [Redes TCP/IP](02-tcp-ip-networking.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar como VLANs criam domínios separados na camada 2 e por que a comunicação entre elas exige roteamento.
- Descrever o funcionamento de um firewall stateful e a estrutura de uma política entre zonas.
- Diferenciar VPN site-to-site, VPN de acesso remoto e TLS quanto ao que protegem.
- Avaliar um desenho de rede quanto a zonas, pontos de controle e fluxos permitidos.

## Conceito

### Segmentar é limitar o alcance

O problema que a segmentação resolve é o **movimento lateral**: depois de comprometer uma máquina (por phishing, por exemplo), o atacante procura alcançar servidores, contas privilegiadas e backups. Em uma rede plana, todos estão a um passo. Em uma rede segmentada, cada passo exige atravessar um ponto de controle que pode bloquear, registrar e alertar.

Uma **zona** é um conjunto de sistemas com nível de confiança e função semelhantes — usuários, servidores de aplicação, bancos de dados, gestão, DMZ. A **fronteira** entre zonas é onde a política é aplicada. A pergunta de arquitetura deixa de ser "esse servidor está protegido?" e passa a ser "**quem pode alcançar esse servidor, por qual caminho, e quem decidiu isso?**".

### Proteger o caminho versus proteger o conteúdo

Segmentação controla **quem alcança quem**. Quando a comunicação precisa passar por redes que a organização não controla — a internet, um link de operadora —, é preciso também proteger o **conteúdo**: confidencialidade, integridade e autenticação das pontas. É o papel de VPN e TLS.

## Fundamentos técnicos

### VLANs: separação na camada 2

Uma **VLAN** divide um switch físico em vários domínios lógicos de broadcast. Estações na VLAN 20 não "enxergam" diretamente as da VLAN 30: para se comunicarem, o tráfego precisa passar por um equipamento de camada 3 — roteador ou firewall. **É justamente esse ponto que torna a VLAN útil para segurança**: ele é onde a política entre zonas pode ser aplicada.

Duas ressalvas importantes:

- Se o roteamento entre VLANs for feito por um switch de camada 3 **sem filtragem**, a separação em VLANs não restringe nada — ela apenas organiza.
- Configurações incorretas (portas de *trunk* mal configuradas, VLAN nativa compartilhada) permitem saltos entre VLANs. VLAN é uma ferramenta de engenharia, não uma garantia.

### Firewalls stateful e política entre zonas

Um **firewall stateful** acompanha o estado de cada conexão: se a política permite que a VLAN de usuários inicie conexões HTTPS para a aplicação, as respostas são aceitas automaticamente, e nada é aceito no sentido inverso sem regra própria. A política é uma lista ordenada de regras do tipo:

| Origem | Destino | Serviço | Ação | Justificativa |
|:---|:---|:---|:---|:---|
| VLAN 20 — Usuários | Aplicação (VLAN 30) | HTTPS 443 | Permitir | Uso do sistema |
| Aplicação | Banco de dados | Porta do SGBD | Permitir | Persistência |
| VLAN 99 — Gestão | VLAN 30 | SSH 22, RDP 3389 | Permitir | Administração |
| Qualquer | Qualquer | Qualquer | **Negar e registrar** | Negar por padrão |

O NIST SP 800-41 recomenda exatamente essa disciplina: política de **negação por padrão**, regras justificadas, revisão periódica e registro. A coluna *justificativa* é o que transforma uma lista de regras em uma política auditável — regras sem dono e sem motivo são o principal sintoma de firewalls que "ninguém tem coragem de mexer".

### Firewalls de próxima geração e inspeção

Além de endereço e porta, firewalls modernos podem identificar aplicações, usuários e conteúdo, e decifrar TLS para inspeção. Isso aumenta a precisão das regras ("permitir o aplicativo X para o grupo Y"), ao custo de desempenho, complexidade e da necessidade de gerenciar certificados para decifrar tráfego — com implicações de privacidade que precisam ser decididas pela organização.

### VPN

Uma **VPN** cria um túnel cifrado sobre uma rede não confiável.

| Tipo | Liga | Uso | Ponto de atenção |
|:---|:---|:---|:---|
| **Site-to-site** | Duas redes (matriz e filial, datacenter e cloud) | Interconexão permanente | O túnel conecta redes inteiras; a política de quais fluxos atravessam continua necessária. |
| **Acesso remoto** | Um usuário a uma rede | Trabalho remoto, fornecedores | Coloca o dispositivo do usuário "dentro" da rede; sem MFA e restrição de destinos, vira porta de entrada para invasões. |

A VPN protege o **trânsito**. Ela não diz nada sobre a confiabilidade do dispositivo na outra ponta — é por isso que abordagens como ZTNA, tratadas na M05-L04 e no M07, restringem o acesso a aplicações específicas em vez de redes inteiras.

### TLS

O **TLS** protege uma conexão entre duas aplicações — navegador e servidor, ou serviço e serviço. Ele oferece confidencialidade, integridade e **autenticação do servidor** por certificado; com **mTLS** (TLS mútuo), o cliente também se autentica por certificado. A versão vigente do TLS 1.3 está especificada no **RFC 9846** (julho de 2026), que tornou obsoleto o RFC 8446 mantendo o mesmo número de versão e a compatibilidade.

Diferença essencial em relação à VPN: o TLS protege **uma conversa entre duas aplicações**, de ponta a ponta, enquanto a VPN protege o caminho entre dois pontos da rede. Em arquiteturas modernas, o TLS é usado inclusive **dentro** da rede corporativa, porque não se presume que a rede interna seja segura.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m00-l03-segmented-network.mmd"
```

<figcaption>Figura 1 — Rede segmentada com VLANs, firewall entre zonas e VPN de acesso remoto.</figcaption>
</figure>

Na figura, todo tráfego entre zonas converge para o **firewall interno**. A DMZ abriga o que é alcançável pela internet; a VLAN de gestão é a única origem permitida para protocolos administrativos; a VPN termina na borda, e o tráfego dos usuários remotos ainda passa pela política interna antes de chegar aos servidores.

## Exemplo empresarial

!!! example "Meridiana — do plano para as zonas"

    A rede da Meridiana é plana: estações, servidores, coletores dos centros de distribuição e o NAS de backup estão no mesmo segmento. Um teste de intrusão mostrou que, a partir de uma estação comprometida, era possível alcançar diretamente o banco do ERP e a interface de administração do backup.

    A primeira etapa da segmentação, proposta pelo arquiteto:

    | Zona | Conteúdo | Pode iniciar conexões para |
    |:---|:---|:---|
    | Usuários | Estações | Aplicações (HTTPS), serviços de diretório |
    | Aplicações | ERP, servidor de arquivos | Banco de dados, diretório |
    | Dados | Banco do ERP | — (apenas responde) |
    | Gestão | Estações de administração | Todas as zonas, protocolos administrativos |
    | Backup | NAS de backup | — (apenas recebe dos agentes, por porta específica) |
    | Coletores | Coletores e servidor de etiquetas | Apenas o servidor de etiquetas e o ERP, em portas definidas |

    O ganho imediato: o backup deixa de ser alcançável a partir das estações — o que, num ataque de ransomware, separa um incidente grave de uma perda total. O tema é aprofundado no [Caso A](../../case-studies/case-a-meridiana/index.md).

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Estrutura | Rede plana, ou VLANs roteadas sem filtragem | Zonas por função e confiança, com política entre elas |
| Política | Regras "permitir tudo" entre redes internas | Negar por padrão; cada regra com justificativa e dono |
| Administração | Protocolos administrativos de qualquer origem | Apenas a partir da zona de gestão |
| Acesso remoto | VPN para a rede inteira, só com senha | MFA e restrição aos destinos necessários |
| Tráfego interno | Em claro, "porque é rede interna" | TLS também entre serviços internos |

## Aplicabilidade: on-premises, cloud e híbrido

| Ambiente | Mecanismos equivalentes |
|:---|:---|
| **On-premises** | VLANs, firewalls internos, ACLs em switches e roteadores. |
| **Cloud** | Sub-redes, tabelas de rotas, security groups ou regras de rede por recurso, firewalls gerenciados. A segmentação pode ser aplicada **por instância**, não só por sub-rede. |
| **Híbrido** | VPN site-to-site ou links dedicados entre datacenter e cloud; a política precisa definir quais zonas de cada lado se comunicam, em vez de "unir as redes". |

## Como especificar e implementar

- "A rede é dividida nas zonas definidas no padrão de segmentação; todo tráfego entre zonas atravessa um ponto de controle com política de negação por padrão."
- "Cada regra de firewall registra origem, destino, serviço, justificativa, dono e data de revisão; regras sem uso por 90 dias são revisadas."
- "Protocolos administrativos são permitidos apenas a partir da zona de gestão."
- "Comunicação entre serviços que transporta dados confidenciais usa TLS 1.2 ou superior, preferencialmente TLS 1.3."

## Trade-offs, limitações e antipadrões

- **Granularidade × operação.** Zonas demais geram milhares de regras difíceis de manter; zonas de menos não contêm movimento lateral. Comece por poucas zonas com alto ganho (usuários, servidores, dados, gestão, backup).
- **Segmentação não substitui autenticação.** Dentro de uma zona permitida, ainda é preciso controlar quem acessa o quê.
- **Antipadrão — "regra temporária" permanente:** liberações de emergência que nunca são revogadas.
- **Antipadrão — VPN como confiança total:** tratar quem está na VPN como se estivesse no escritório.

## Como validar

- A partir de uma estação de usuário, testar a conectividade para o banco de dados, o backup e as interfaces de gestão — deve falhar.
- Revisar a política de firewall buscando regras amplas ("any-any"), sem justificativa ou sem uso.
- Confirmar que a VPN exige MFA e que usuários remotos recebem acesso apenas aos destinos necessários.
- Verificar versões de TLS aceitas pelos serviços expostos e internos.

## Como apresentar e justificar

- **Para engenharia:** "Vamos criar seis zonas e concentrar a política no firewall interno; as regras atuais serão migradas com dono e justificativa."
- **Para gestores:** "Hoje, um computador infectado alcança o backup. Com a segmentação, esse caminho deixa de existir — e um ataque de ransomware não consegue destruir a nossa capacidade de recuperação."

## Checklist de revisão arquitetural

- [ ] As zonas e seus níveis de confiança estão definidos e representados nos diagramas.
- [ ] Todo fluxo entre zonas passa por um ponto de controle com negação por padrão.
- [ ] Cada regra tem justificativa, dono e data de revisão.
- [ ] Administração ocorre apenas a partir da zona de gestão.
- [ ] VPN de acesso remoto exige MFA e limita destinos.
- [ ] Dados confidenciais trafegam com TLS também na rede interna.

## Questões de compreensão

**1.** Duas VLANs foram criadas, mas o roteamento entre elas é feito por um switch de camada 3 sem listas de acesso. A segmentação reduz o movimento lateral?

??? success "Resposta comentada"

    Não. Os hosts das duas VLANs se alcançam livremente pelo roteamento. VLANs só contribuem para a segurança quando o ponto de roteamento entre elas aplica uma política.

**2.** Por que um firewall stateful não precisa de uma regra explícita para as respostas de uma conexão permitida?

??? success "Resposta comentada"

    Porque ele registra o estado das conexões iniciadas de acordo com a política e aceita automaticamente os pacotes de resposta pertencentes a elas. Conexões novas no sentido inverso continuam exigindo regra própria.

**3.** Uma empresa já usa VPN site-to-site entre o datacenter e a cloud. Ainda faz sentido usar TLS entre a aplicação na cloud e o banco no datacenter?

??? success "Resposta comentada"

    Sim. A VPN protege o trânsito entre as redes, mas o tráfego volta a circular em claro dentro de cada rede e em qualquer equipamento que termine o túnel. O TLS protege a conversa de ponta a ponta entre as duas aplicações e autentica o servidor.

**4.** O que torna uma regra de firewall "auditável"?

??? success "Resposta comentada"

    Ter origem, destino e serviço específicos, além de justificativa, dono e data de revisão. Isso permite saber por que a regra existe e se ainda é necessária.

## Exercício de tomada de decisão

!!! question "Cenário: acesso de fornecedores ao ERP da Meridiana"

    O fornecedor do ERP precisa acessar mensalmente o servidor de aplicação para aplicar atualizações. Hoje ele usa a mesma VPN dos funcionários, com uma conta compartilhada, e tem acesso a toda a rede.

    Avalie três alternativas: (A) manter a VPN, mas criar contas individuais com MFA; (B) VPN com MFA, contas individuais e política que limite o fornecedor ao servidor do ERP, só por protocolos administrativos e apenas a partir da zona de gestão via estação intermediária; (C) suspender o acesso remoto e exigir que o fornecedor atue presencialmente. Critérios: limitação de alcance, identificação e rastreabilidade, custo operacional e agilidade das correções.

??? success "Resolução de referência"

    | Critério | Peso | A — VPN com MFA | B — VPN com MFA e alcance limitado | C — Só presencial |
    |:---|:---|:---|:---|:---|
    | Limitação de alcance | 3 | 1 | 3 | 3 |
    | Identificação e rastreabilidade | 2 | 3 | 3 | 2 |
    | Custo operacional e agilidade das correções | 2 | 3 | 2 | 1 |
    | **Total ponderado** | | **15** | **19** | **15** |

    **Recomendação: B.**

    - **A** resolve a identificação (contas individuais, MFA), mas mantém o alcance: um dispositivo comprometido do fornecedor continua com acesso a toda a rede.
    - **B** combina identificação forte com **limitação de alcance**: o fornecedor só chega ao servidor necessário, por um caminho controlado e registrado.
    - **C** reduz o risco, mas tem custo operacional alto e atrasa correções — o que também é um risco. Pode ser usada como medida temporária.

    O critério central é que **autenticar quem entra não substitui limitar até onde se pode ir**.

## Pontos-chave

- Segmentação limita o movimento lateral; VLANs só ajudam quando o roteamento entre elas aplica política.
- Políticas de firewall devem negar por padrão, e cada regra deve ter justificativa, dono e revisão.
- VPN protege o trânsito entre pontos; TLS protege a conversa entre aplicações. Um não substitui o outro.
- VPN de acesso remoto sem MFA e sem limitação de destinos é uma das portas de entrada mais exploradas.
- A versão vigente do TLS 1.3 é especificada pelo RFC 9846 (2026).

## Referências

### Fundamentação principal

- NIST. *SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy*. 2009. <https://csrc.nist.gov/pubs/sp/800/41/r1/final> — tipos de firewall e disciplina de política. *(Página oficial conferida.)*
- E. Rescorla. *RFC 9846 — The Transport Layer Security (TLS) Protocol Version 1.3*. IETF, julho de 2026. <https://www.rfc-editor.org/rfc/rfc9846.html> — especificação vigente do TLS 1.3; §1.2 descreve a relação com o RFC 8446.
- NIST. *SP 800-215 — Guide to a Secure Enterprise Network Landscape*. 2022. <https://csrc.nist.gov/News/2022/sp-800-215-secure-enterprise-network-landscape> — limites de VPN e firewall no cenário atual. *(Escopo conferido no anúncio oficial.)*

### Leitura complementar

- NIST. *SP 800-207 — Zero Trust Architecture*. 2020. §2.1 (p. 6) — o princípio de que estar na rede interna não confere confiança, base das aulas de Zero Trust.
- R. Anderson. *Security Engineering*, 3ª ed. Cap. 21 *Network Attack and Defence*. *(Localizado pelo sumário.)*

### Aplicação prática

- O [Laboratório 00](../../labs/lab-00-network-plan.md) aplica esta aula a um plano de rede da Meridiana: separar usuários, servidores e gestão e documentar fluxos mínimos.
- Use a tabela de zonas do exemplo da Meridiana como ponto de partida do exercício de segmentação do [Laboratório 02](../../labs/lab-02-architecture-modeling.md).

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
