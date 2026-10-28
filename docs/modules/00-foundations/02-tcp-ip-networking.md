---
id: M00-L02
title: "Aula 02 — Redes TCP/IP: modelo OSI, endereçamento, DNS, DHCP e NAT"
public_title: "Módulo Inicial — Aula 02 — Redes TCP/IP: modelo OSI, endereçamento, DNS, DHCP e NAT"
description: Como uma requisição atravessa a rede — camadas, endereçamento IP, portas, DNS, DHCP, roteamento e NAT — e onde cada etapa cria oportunidades de controle e de ataque.
domain: infrastructure-foundations
tier: fundamental
status: published
prerequisites: [M00-L01]
objectives:
  - Relacionar as camadas do modelo OSI e da pilha TCP/IP aos componentes de uma rede corporativa.
  - Interpretar endereços IPv4, máscaras, faixas privadas e portas em um diagrama.
  - Descrever o papel de DHCP, DNS, gateway padrão e NAT no caminho de uma requisição.
  - Identificar os pontos do caminho em que controles de segurança podem ser aplicados.
minutes: 75
sources: [RFC-1918, NIST-SP800-41-R1, BOOK-ANDERSON-SE3]
further_reading: [NIST-SP800-215]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M00
---

# Aula 02 — Redes TCP/IP: modelo OSI, endereçamento, DNS, DHCP e NAT { #redes-tcpip-modelo-osi-enderecamento-dns-dhcp-e-nat }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo Inicial · Nível 0</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">75 min · ID técnico: M00-L02</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Quase toda decisão de arquitetura de segurança envolve um fluxo de rede: quem fala com quem, por qual porta, atravessando qual fronteira. Esta aula acompanha uma requisição desde a estação de um usuário até um site na internet, explicando cada etapa — endereço, nome, rota, tradução — e mostrando onde estão os pontos naturais de controle e as fragilidades exploradas por atacantes.

**Pré-requisitos:** [Computação, sistemas operacionais e virtualização](01-computing-os-virtualization.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Relacionar as camadas do modelo OSI e da pilha TCP/IP aos componentes de uma rede corporativa.
- Interpretar endereços IPv4, máscaras, faixas privadas e portas em um diagrama.
- Descrever o papel de DHCP, DNS, gateway padrão e NAT no caminho de uma requisição.
- Identificar os pontos do caminho em que controles de segurança podem ser aplicados.

## Conceito

### Camadas: um vocabulário, não uma lei

Redes são descritas em **camadas**, cada uma resolvendo um problema e oferecendo serviços à de cima. O **modelo OSI** tem sete camadas; a pilha **TCP/IP**, usada na prática, agrupa-as em quatro. O valor do modelo para um arquiteto é o vocabulário: quando alguém diz "firewall de camada 7" ou "segmentação em camada 2", está dizendo **o que o controle consegue ver e decidir**.

| OSI | TCP/IP | O que trata | Exemplos | O que um controle nessa camada enxerga |
|:---|:---|:---|:---|:---|
| 7 Aplicação · 6 Apresentação · 5 Sessão | Aplicação | Significado da comunicação | HTTP, DNS, SMTP, TLS | URLs, métodos, cabeçalhos, conteúdo |
| 4 Transporte | Transporte | Entrega entre processos | TCP, UDP | Portas, estado da conexão |
| 3 Rede | Internet | Entrega entre redes | IP, ICMP | Endereços de origem e destino |
| 2 Enlace · 1 Física | Acesso à rede | Entrega no meio local | Ethernet, Wi-Fi, VLAN | Endereços MAC, VLAN |

Um firewall que filtra por endereço e porta decide nas camadas 3 e 4; um WAF que bloqueia uma injeção de SQL precisa entender HTTP, na camada 7. Quanto mais alta a camada, mais contexto o controle tem — e mais caro e complexo ele é.

### Por que entender o caminho

Atacantes exploram cada etapa do caminho: falsificam respostas de DNS, oferecem um servidor DHCP malicioso, abusam de portas expostas sem necessidade. Defensores também usam cada etapa: DNS é uma das melhores fontes de telemetria de uma rede, o gateway é um ponto natural de inspeção, o NAT esconde a estrutura interna. Conhecer o caminho permite escolher **onde** colocar cada controle.

## Fundamentos técnicos

### Endereçamento IPv4 e faixas privadas

Um endereço IPv4 tem 32 bits, escritos em quatro números de 0 a 255. A **máscara** — ou o sufixo em notação CIDR, como `/24` — indica quantos bits identificam a rede. Em `10.20.30.15/24`, os primeiros 24 bits (`10.20.30`) identificam a rede, e o último número identifica o host: até 254 hosts utilizáveis.

O RFC 1918 reserva três faixas para redes privadas, que não são roteadas na internet:

| Faixa | Notação CIDR | Uso típico |
|:---|:---|:---|
| 10.0.0.0 – 10.255.255.255 | `10.0.0.0/8` | Grandes redes corporativas e VPCs em cloud |
| 172.16.0.0 – 172.31.255.255 | `172.16.0.0/12` | Redes médias, DMZs |
| 192.168.0.0 – 192.168.255.255 | `192.168.0.0/16` | Redes domésticas e pequenas filiais |

Um ponto prático para arquitetos: **sobreposição de faixas**. Quando duas empresas se fundem, ou quando uma VPC em cloud usa a mesma faixa que o datacenter, a interconexão exige tradução de endereços ou renumeração. Planejar o endereçamento é uma decisão arquitetural, não um detalhe operacional.

O **IPv6**, com endereços de 128 bits, elimina a escassez e, em princípio, a necessidade de NAT. Isso muda um hábito comum: hosts IPv6 podem ser globalmente endereçáveis, e a proteção passa a depender explicitamente de firewall, não do "efeito colateral" do NAT.

### Portas e transporte

Um endereço IP identifica um host; uma **porta** identifica o serviço dentro dele. O **TCP** estabelece conexões com o *three-way handshake* (SYN, SYN-ACK, ACK), garante entrega ordenada e retransmite perdas. O **UDP** envia datagramas sem conexão, útil para DNS, voz e streaming. Algumas portas conhecidas:

| Porta | Serviço | Observação de segurança |
|:---|:---|:---|
| 443/TCP | HTTPS | O tráfego padrão da web; criptografado com TLS. |
| 53/UDP e TCP | DNS | Essencial; frequentemente usado para exfiltração e comando e controle. |
| 22/TCP | SSH | Administração de sistemas Unix; nunca deve estar exposto sem restrição. |
| 3389/TCP | RDP | Administração Windows; alvo frequente de força bruta quando exposto. |
| 389, 636/TCP | LDAP, LDAPS | Diretório; LDAP sem TLS transmite dados em claro. |

### DHCP: como a estação ganha identidade na rede

Ao ser ligada, a estação não tem endereço. Ela envia um pedido em broadcast, e o servidor **DHCP** responde com endereço IP, máscara, **gateway padrão** (o roteador para outras redes) e servidores DNS. Como a estação aceita a primeira resposta, um servidor DHCP malicioso na mesma rede pode indicar um gateway ou DNS controlado pelo atacante. Switches gerenciados oferecem proteção (*DHCP snooping*) que aceita respostas apenas de portas autorizadas.

### DNS: nomes, confiança e telemetria

O **DNS** traduz nomes como `www.example.com` em endereços. A estação consulta um resolvedor — normalmente o DNS interno da empresa —, que consulta a hierarquia da internet e guarda a resposta em cache. Pontos de atenção:

- **Integridade:** respostas falsificadas desviam usuários; DNSSEC permite validar a autenticidade de zonas que o adotam.
- **Exfiltração e C2:** malware codifica dados em consultas DNS porque esse tráfego raramente é bloqueado.
- **Telemetria:** registrar as consultas no resolvedor interno revela máquinas comprometidas que contatam domínios maliciosos. Por isso muitas arquiteturas obrigam as estações a usar apenas o DNS corporativo.

### Roteamento e NAT

Se o destino está em outra rede, a estação envia o pacote ao gateway. Roteadores escolhem o próximo salto pela **tabela de rotas**. Na borda, o firewall aplica **NAT** (*Network Address Translation*): troca o endereço privado de origem por um endereço público e registra a conexão numa **tabela de estados** para desfazer a tradução na resposta.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m00-l02-packet-path.mmd"
```

<figcaption>Figura 1 — Caminho de uma requisição web: DHCP, DNS, gateway e NAT.</figcaption>
</figure>

Repare que o NAT permite, por padrão, apenas conexões **iniciadas de dentro** — o que dá uma proteção incidental. Mas NAT **não é um controle de segurança desenhado como tal**: não inspeciona conteúdo, não autentica ninguém e deixa de proteger assim que alguém cria uma regra de encaminhamento de porta ("port forwarding") para publicar um serviço. A proteção real vem da política do firewall, como trata o NIST SP 800-41.

## Exemplo empresarial

!!! example "Meridiana — o servidor que "não estava exposto""

    Um fornecedor pediu acesso remoto a um servidor de integração da Meridiana. A equipe criou uma regra de *port forwarding* no firewall: a porta 3389 de um IP público passou a encaminhar para o RDP do servidor. "Ele continua com IP privado, então não está exposto", argumentou o técnico.

    Três semanas depois, o servidor registrava milhares de tentativas de login por hora vindas de vários países. O endereço privado não importava: **o serviço estava alcançável pela internet** por meio da tradução.

    A correção arquitetural não foi trocar a porta, e sim mudar o padrão: acesso de terceiros passa a ocorrer por um canal autenticado com MFA e restrito às aplicações necessárias (tema da Aula 04 do Módulo 5), e nenhuma regra de encaminhamento para protocolos administrativos é permitida na borda.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Endereçamento | Faixas escolhidas ad hoc em cada projeto | Plano de endereçamento corporativo, incluindo cloud, evitando sobreposição |
| DNS | Estações usam qualquer resolvedor | Uso obrigatório do resolvedor corporativo, com registro das consultas |
| Publicação de serviços | *Port forwarding* direto para servidores internos | Publicação via proxy reverso ou gateway na DMZ, com política explícita |
| NAT | Tratado como "firewall" | Tratado como tradução; a proteção é a política de filtragem |
| DHCP | Qualquer porta pode responder | DHCP snooping e proteção contra servidores não autorizados |

## Aplicabilidade: on-premises, cloud e híbrido

| Ambiente | O que muda |
|:---|:---|
| **On-premises** | A organização opera switches, roteadores, DHCP, DNS e NAT. |
| **Cloud** | Redes virtuais (VPC, VNet) têm endereçamento escolhido pelo cliente; DHCP e roteamento básico são fornecidos pelo provedor; gateways de NAT e resolvedores DNS são serviços gerenciados. |
| **Híbrido** | O plano de endereçamento e a resolução de nomes precisam ser **unificados**: sobreposição de faixas e DNS que não resolve nomes do outro ambiente são as falhas mais comuns de integração (tema da Aula 02 do Módulo 11). |

## Como especificar e implementar

- "Toda rede, on-premises ou em cloud, recebe faixa do plano de endereçamento corporativo; sobreposições exigem aprovação de arquitetura."
- "Estações e servidores resolvem nomes exclusivamente pelos resolvedores corporativos; consultas são registradas e retidas por 90 dias."
- "Nenhum protocolo administrativo (SSH, RDP, interfaces de gestão) é publicado na internet por encaminhamento de porta."

## Trade-offs, limitações e antipadrões

- **Mais inspeção, mais latência e custo.** Inspecionar na camada 7 exige decifrar TLS e mais processamento.
- **IPv6 ignorado.** Redes que "não usam IPv6" frequentemente o têm habilitado por padrão nos sistemas; controles só para IPv4 deixam um caminho paralelo.
- **Antipadrão — confiar no IP de origem:** endereços podem ser falsificados ou compartilhados por NAT; IP é um sinal, não uma identidade.

## Como validar

- Verificar, de fora, quais portas respondem nos endereços públicos da organização.
- Conferir se estações conseguem resolver nomes usando resolvedores externos diretamente.
- Revisar regras de NAT e encaminhamento de porta na borda, com justificativa e dono de cada uma.
- Testar se uma porta de switch não autorizada consegue responder como servidor DHCP.

## Como apresentar e justificar

- **Para engenharia:** "O RDP do servidor de integração está alcançável da internet pelo encaminhamento de porta; precisamos removê-lo e oferecer acesso por canal autenticado."
- **Para gestores:** "Um servidor da empresa estava recebendo milhares de tentativas de invasão por hora. Vamos fechar esse acesso e substituí-lo por um caminho controlado para o fornecedor."

## Checklist de revisão arquitetural

- [ ] Os fluxos do diagrama indicam protocolo e porta.
- [ ] O plano de endereçamento evita sobreposição entre ambientes.
- [ ] A resolução de nomes passa por resolvedores controlados e registrados.
- [ ] Não há serviços administrativos publicados por NAT.
- [ ] IPv6 está tratado explicitamente (habilitado com controles ou desabilitado).

## Questões de compreensão

**1.** Um firewall que decide por endereço e porta consegue bloquear uma injeção de SQL enviada por HTTPS? Por quê?

??? success "Resposta comentada"

    Não. Ele decide nas camadas 3 e 4 e só vê endereços e portas. A injeção está no conteúdo HTTP — camada 7 — e, além disso, está cifrada por TLS. Para tratá-la é preciso um controle que entenda HTTP após decifrar o tráfego (um WAF ou a própria aplicação).

**2.** Por que um servidor com endereço `10.x.x.x` pode estar exposto à internet?

??? success "Resposta comentada"

    Porque uma regra de NAT ou de encaminhamento de porta na borda pode traduzir um endereço público para ele. O endereço privado não é roteado na internet, mas a tradução cria o caminho.

**3.** Que valor de segurança há em obrigar todas as estações a usar o DNS corporativo?

??? success "Resposta comentada"

    Visibilidade e controle: as consultas podem ser registradas e analisadas para detectar máquinas que contatam domínios maliciosos, e é possível bloquear a resolução de domínios conhecidos como maliciosos.

**4.** Duas empresas do mesmo grupo usam `10.0.0.0/16` e precisam se conectar. Que problema surge?

??? success "Resposta comentada"

    Sobreposição de endereços: os roteadores não conseguem distinguir para qual rede encaminhar um destino que existe nas duas. A solução exige renumeração ou tradução de endereços entre as redes — o que deveria ter sido evitado por um plano de endereçamento corporativo.

## Exercício de tomada de decisão

!!! question "Cenário: publicar o portal de agendamento da Lumen Saúde"

    O portal de agendamento precisa ficar acessível pela internet em HTTPS. Há três propostas:

    - **A** — Encaminhar a porta 443 de um IP público diretamente para o servidor do portal na rede interna.
    - **B** — Colocar um proxy reverso na DMZ, que recebe as conexões da internet e encaminha ao portal na zona de aplicações, apenas na porta da aplicação.
    - **C** — Hospedar o portal em um serviço gerenciado de cloud, com acesso ao banco de agendas no datacenter por um túnel.

    Qual proposta você recomendaria, considerando que o portal acessa dados de pacientes e que a equipe de infraestrutura ainda não opera serviços em cloud? Critérios: proteção dos dados de pacientes, capacidade de operação pela equipe atual e custo.

??? success "Resolução de referência"

    | Critério | Peso | A — Porta encaminhada | B — Proxy na DMZ | C — Serviço gerenciado em cloud |
    |:---|:---|:---|:---|:---|
    | Proteção dos dados de pacientes | 3 | 1 | 3 | 2 |
    | Capacidade de operação pela equipe atual | 2 | 3 | 2 | 1 |
    | Custo | 1 | 3 | 2 | 2 |
    | **Total ponderado** | | **12** | **15** | **10** |

    **Recomendação: B**, com C como alternativa válida se a organização já tiver maturidade em cloud — nesse caso, a nota de operação de C sobe e a comparação muda.

    - **A** coloca um servidor da rede interna diretamente alcançável pela internet; qualquer falha no portal dá ao atacante uma posição dentro da rede interna.
    - **B** cria uma fronteira: o que fica exposto é o proxy na DMZ, e o fluxo para o portal passa por uma política explícita (uma porta, um destino). O proxy também é o lugar natural para terminar TLS e aplicar inspeção de camada 7.
    - **C** desloca a exposição para o provedor, mas cria um túnel entre cloud e datacenter que precisa ser tratado com o mesmo rigor de uma fronteira — tema das aulas de cloud e de ambientes híbridos.

    O critério que decide é **onde fica a fronteira entre o que é alcançável pela internet e os dados de pacientes**.

## Pontos-chave

- As camadas descrevem o que cada controle consegue ver: quanto mais alto, mais contexto e mais custo.
- Faixas do RFC 1918 não são roteadas na internet, mas NAT e encaminhamento de porta podem expor hosts privados.
- NAT é tradução, não política de segurança; a proteção vem do firewall.
- DNS é infraestrutura crítica, vetor de ataque e excelente fonte de telemetria.
- Planejar endereçamento e resolução de nomes é decisão de arquitetura, sobretudo em ambientes híbridos.

## Referências

### Fundamentação principal

- Y. Rekhter *et al.* *RFC 1918 — Address Allocation for Private Internets* (BCP 5). IETF, 1996. <https://www.rfc-editor.org/info/rfc1918> — faixas de endereços privados.
- NIST. *SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy*. 2009. <https://csrc.nist.gov/pubs/sp/800/41/r1/final> — tecnologias de filtragem e política de firewall. *(Página oficial conferida.)*

### Leitura complementar

- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020. Cap. 21 *Network Attack and Defence*. <https://www.cl.cam.ac.uk/archive/rja14/book.html> — ataques e defesas de rede em perspectiva de engenharia. *(Capítulo localizado pelo sumário.)*
- NIST. *SP 800-215 — Guide to a Secure Enterprise Network Landscape*. 2022. <https://csrc.nist.gov/News/2022/sp-800-215-secure-enterprise-network-landscape> — como o fim do perímetro tradicional muda o desenho de redes corporativas.

### Aplicação prática

- Ferramentas como `ip addr`, `nslookup`/`dig`, `traceroute` e `ss`/`netstat` permitem observar, em qualquer máquina, os elementos desta aula: endereço, resolvedor, rota e conexões abertas.
- O [Laboratório 00](../../labs/lab-00-network-plan.md) põe em prática endereçamento e faixas privadas: você revisa um plano com sobreposição entre datacenter e nuvem.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
