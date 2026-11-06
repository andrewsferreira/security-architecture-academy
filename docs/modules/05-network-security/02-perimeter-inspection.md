---
id: M05-L02
title: "Aula 02 — Perímetro e inspeção: DMZ, WAF, NGFW, IDS/IPS e proxies"
public_title: "Módulo 5 — Aula 02 — Perímetro e inspeção: DMZ, WAF, NGFW, IDS/IPS e proxies"
description: O papel atual do perímetro — DMZ, firewalls de próxima geração, WAF e WAAP, IDS/IPS, proxies reversos e de saída — e como posicionar cada controle sem confundir inspeção com proteção nem depender de um único ponto.
domain: network-security
tier: professional
status: published
prerequisites: [M05-L01]
objectives:
  - Posicionar DMZ, NGFW, WAF/WAAP, IPS e proxies em fluxos de entrada e de saída.
  - Explicar o que cada controle inspeciona e o que não consegue ver.
  - Definir política de saída (egress) para usuários e para servidores.
  - Avaliar trade-offs da inspeção de tráfego cifrado.
minutes: 75
sources: [NIST-SP800-41-R1, NIST-SP800-215, NSA-NETWORK-INFRA-2022, NIST-SP800-94, NIST-SP800-53, RFC-9846]
further_reading: [OWASP-ASVS-5, PCI-DSS-401]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M05
---

# Aula 02 — Perímetro e inspeção: DMZ, WAF, NGFW, IDS/IPS e proxies { #perimetro-e-inspecao-dmz-waf-ngfw-idsips-e-proxies }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 5 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M05-L02</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    A NIST SP 800-215 fala no "desaparecimento do conceito de perímetro" — e, mesmo assim, toda organização continua tendo pontos onde o tráfego entra e sai. O perímetro deixou de ser **a** defesa e passou a ser **uma** camada: importante para reduzir exposição, filtrar ataques comuns e controlar a saída, mas insuficiente sozinho. Esta aula mostra o que cada controle de perímetro faz, onde posicioná-lo e o que ele não vê.

**Pré-requisito:** [Zonas de confiança, segmentação e microsegmentação](01-zones-segmentation.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Posicionar DMZ, NGFW, WAF/WAAP, IPS e proxies em fluxos de entrada e de saída.
- Explicar o que cada controle inspeciona e o que não consegue ver.
- Definir política de saída (egress) para usuários e para servidores.
- Avaliar trade-offs da inspeção de tráfego cifrado.

## Conceito

### Os controles e o que inspecionam

| Controle | O que faz | Referência |
|:---|:---|:---|
| **Firewall stateful** | Acompanha conexões em uma tabela de estado e filtra por endereços, portas e protocolos | SP 800-41 Rev. 1, Sec. 2.1 |
| **NGFW** | Acrescenta consciência de aplicação, decifragem TLS e IPS | SP 800-215, p. 10 |
| **IDS/IPS** | Detecta (IDS) ou bloqueia (IPS) padrões de ataque; a SP 800-94 classifica IDPS em baseados em rede, sem fio, análise de comportamento de rede e baseados em host | SP 800-94 |
| **WAF** | Firewall de aplicação especializado, à frente do servidor web, contra injeção, XSS e similares | SP 800-41 Rev. 1, p. 2-9; SP 800-215, p. 10 |
| **WAAP** | Amplia o WAF para APIs, bots e DDoS, como suíte ou serviço em nuvem | SP 800-215, p. 10 |
| **Proxy reverso** | Intermediário que recebe conexões em nome dos servidores; nenhuma conexão direta entre cliente e servidor | SP 800-41 Rev. 1, p. 2-6 |
| **Secure web gateway (SWG)** | Filtro de tráfego de saída dos usuários, com inspeção HTTPS | SP 800-215, pp. 10–11 |
| **Proxy de saída de servidores** | Limita os destinos que servidores podem alcançar | Prática de arquitetura |

A SP 800-41 Rev. 1 registra um ponto que ainda gera confusão: **NAT não é funcionalidade de segurança** do firewall, e sim de roteamento, e não deve ser tratado como controle (Sec. 3, p. 3-3).

### DMZ

A **DMZ** é uma zona para sistemas que precisam ser alcançados de fora — tipicamente servidores web e de e-mail — separada da rede protegida, de modo que o tráfego entre DMZ e rede interna também passe pelo firewall e por sua política (SP 800-41 Rev. 1, Sec. 3, p. 3-2). A NSA recomenda colocar sistemas acessíveis publicamente e proxies de saída em uma ou mais sub-redes de DMZ e usar múltiplas camadas de defesa no perímetro, de fornecedores diferentes, para que uma única falha não exponha a rede interna (Sec. 2.1).

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m05-l02-perimeter.mmd"
```

<figcaption>Figura 1 — Controles no tráfego de entrada (DDoS, WAF/WAAP, NGFW, proxy reverso na DMZ) e de saída (SWG para usuários, proxy com lista de destinos para servidores).</figcaption>
</figure>

## Fundamentos técnicos

### Política de entrada

- **Negar por padrão** e permitir apenas os serviços publicados (SP 800-41 Rev. 1, Sec. 4).
- **Nenhum acesso direto** da internet à rede interna: tudo termina na DMZ ou em um serviço de borda.
- **WAF ou WAAP** à frente de aplicações e APIs públicas; a SP 800-41 Rev. 1 recomenda firewalls de aplicação e proxies à frente de servidores que não tenham proteção suficiente própria (p. 4-5).
- **Remover conexões ocultas** — a NSA recomenda eliminar conexões de "porta dos fundos", como um roteador de borda também ligado diretamente à rede de gerência (Sec. 2.3).

### Política de saída

A saída é onde muitas organizações são mais permissivas — e onde ataques fazem comando e controle e exfiltração (táticas Command and Control e Exfiltration do ATT&CK, Módulo 4 — Aula 04).

| Origem | Política recomendada |
|:---|:---|
| Estações de usuários | Saída apenas pelo SWG, com filtragem por categoria e inspeção de conteúdo conforme a política |
| Servidores | Sem saída direta; destinos permitidos explicitamente (atualizações, APIs de parceiros) via proxy |
| Zona de gestão | Saída apenas para repositórios de atualização e serviços de administração aprovados |
| DMZ | Saída apenas para destinos necessários ao serviço publicado |

### O que o perímetro não vê

- **Tráfego east-west** dentro da rede (Aula 03).
- **Acesso a SaaS** de dispositivos fora da rede corporativa (Aula 05).
- **Abuso de credenciais válidas** em fluxos permitidos.
- **Conteúdo cifrado** que não for inspecionado.

### Inspeção de tráfego cifrado

NGFWs e SWGs oferecem decifragem TLS (SP 800-215, pp. 10–11). A decisão tem trade-offs:

| A favor | Contra |
|:---|:---|
| Visibilidade de malware e exfiltração em HTTPS | O dispositivo de inspeção vira alvo de alto valor (tem as chaves) |
| Aplicação de DLP e filtragem de conteúdo | Quebra aplicações com certificate pinning |
| | Questões de privacidade (bancos, saúde) e de LGPD a avaliar com o jurídico |
| | Custo de desempenho |

Uma política comum é decifrar por categoria, com exceções documentadas (saúde, financeiro pessoal) e sem inspeção de tráfego de servidores para destinos já restritos por lista.

No TLS 1.3, todas as mensagens do handshake depois do ServerHello são cifradas (RFC 9846, Sec. 1.3, que substituiu a RFC 8446) — inclusive o certificado do servidor. Por isso, um sensor que apenas observa o tráfego já não vê o certificado, e a inspeção de conteúdo exige que o dispositivo **termine a sessão TLS** como proxy, apresentando ao cliente um certificado emitido por uma autoridade certificadora interna, confiável nos dispositivos gerenciados. Na visão desta formação, essa é a principal consequência de arquitetura: inspecionar é operar um intermediário com chaves de alto valor, não "escutar" a rede, e dispositivos não gerenciados (sem a CA instalada) ficam fora da inspeção.

## Exemplo empresarial

!!! example "Aurora Pagamentos — o WAF que não protegia a API"

    A Aurora tinha um WAF na frente do site institucional, mas a **API de parceiros** era publicada por um balanceador diretamente na internet, sem WAF nem limites de taxa. Ao revisar o perímetro, o arquiteto:

    - Colocou a API atrás de um serviço WAAP, com validação de esquema e limite de taxa por parceiro.
    - Moveu o balanceador para a DMZ, com política no NGFW permitindo apenas o WAAP como origem.
    - Bloqueou toda saída direta dos servidores de processamento; apenas o proxy de saída, com lista de três destinos (adquirentes e atualizações), foi permitido.

    No mês seguinte, o proxy de saída registrou tentativas de conexão de um servidor de testes para um domínio desconhecido — o primeiro sinal de um comprometimento que, antes, teria saído pela internet sem registro.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Papel do perímetro | Única defesa | Uma camada entre várias |
| Entrada | Portas abertas por pedido | Negar por padrão; tudo termina na DMZ ou em serviço de borda |
| Aplicações e APIs | Publicadas diretamente | Atrás de WAF/WAAP, com limites e validação |
| Saída | Livre para servidores | Servidores sem saída direta; destinos permitidos |
| NAT | Tratado como proteção | Função de roteamento, não controle |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referência voluntária para especificar e auditar o perímetro:

| Controle ou padrão | Objetivo no perímetro | Referência |
|:---|:---|:---|
| Proteção de fronteira | Controlar a comunicação nas interfaces externas e separar componentes públicos da rede interna (DMZ) | SP 800-53: SC-7 (Boundary Protection) |
| Proxy autenticado na saída | Encaminhar o tráfego de saída por proxies autenticados nas interfaces gerenciadas | SP 800-53: SC-7(8) (Route Traffic to Authenticated Proxy Servers) |
| Prevenção de exfiltração | Impedir a saída indevida de informação e testar periodicamente esse controle | SP 800-53: SC-7(10) (Prevent Exfiltration) |
| Monitoramento de entrada e saída | Definir o que é tráfego incomum e monitorá-lo nos dois sentidos | SP 800-53: SI-4(4) (Inbound and Outbound Communications Traffic) |
| Proteção contra negação de serviço | Limitar os efeitos de ataques de negação de serviço nos serviços publicados | SP 800-53: SC-5 (Denial-of-service Protection) |
| Fluxo de informação cifrada | Impedir que o tráfego cifrado contorne os mecanismos de controle definidos | SP 800-53: AC-4(4) (Flow Control of Encrypted Information) |
| Política de firewall | Negar por padrão e permitir só os serviços publicados | SP 800-41 Rev. 1, Sec. 4 |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, WAF, proteção DDoS e firewalls gerenciados são serviços nativos, e a "DMZ" costuma ser uma rede virtual pública com balanceadores, enquanto os workloads ficam em redes privadas. A política de saída exige atenção especial: muitas contas cloud permitem saída irrestrita por padrão. Em ambientes híbridos, é comum haver dois perímetros (datacenter e nuvem) com políticas diferentes — o ideal é uma política de saída consistente, aplicada no hub de conectividade ou em um serviço SSE (Aula 05).

## Como especificar e implementar

- "Firewalls de borda aplicam negar por padrão; a internet não alcança a rede interna diretamente."
- "Aplicações e APIs públicas são publicadas atrás de WAF ou WAAP, com limites de taxa e validação de esquema quando aplicável."
- "Servidores não têm saída direta para a internet; destinos são permitidos explicitamente via proxy."
- "A inspeção de TLS segue política por categoria, com exceções documentadas e avaliação de privacidade."
- "Os dispositivos de perímetro registram eventos no SIEM."

## Trade-offs, limitações e antipadrões

- **Trade-off:** inspeção profunda aumenta visibilidade e latência, custo e superfície de ataque.
- **Antipadrão — WAF em modo de detecção para sempre:** gera alertas que ninguém trata.
- **Antipadrão — exceções de saída permanentes:** "liberar a internet para o servidor X" durante uma instalação e esquecer.
- **Limitação:** a SP 800-41 Rev. 1 e a SP 800-94 são de 2009 e 2007; os conceitos continuam úteis, mas produtos e ameaças evoluíram.

## Como validar

- Varrer o endereço público da organização e comparar com a lista de serviços publicados.
- Testar, a partir de um servidor, conexões para destinos não permitidos.
- Executar testes de aplicação contra a API pelo caminho público e verificar a ação do WAF.
- Revisar regras de perímetro sem uso e exceções vencidas.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Só os serviços publicados respondem no endereço público | Varredura externa comparada à lista de serviços publicados, sem divergência |
| Toda aplicação e API pública passa pelo WAF ou WAAP | Teste pelo caminho público com payload de teste bloqueado e registrado; nenhuma rota direta ao balanceador |
| Servidores não têm saída direta | Conexão de teste a um destino fora da lista, negada no proxy e registrada |
| Política de TLS aplicada como documentada | Amostra de categorias decifradas e de exceções conferida no SWG |
| Eventos do perímetro no SIEM | Fontes WAF/WAAP, NGFW e proxies presentes, com eventos recentes |

## Como apresentar e justificar

- **Para a diretoria:** "O perímetro reduz exposição e é onde vemos dados saindo. Não é suficiente sozinho, mas sem ele não sabemos o que sai."
- **Para engenharia:** "Toda API pública passa pelo WAAP. Servidores saem só pelo proxy, com lista de destinos que vocês definem."

## Checklist de revisão arquitetural

- [ ] Nenhum serviço interno é alcançável diretamente da internet.
- [ ] Aplicações e APIs públicas estão atrás de WAF ou WAAP.
- [ ] Servidores não têm saída direta para a internet.
- [ ] A política de inspeção de TLS está documentada, com exceções.
- [ ] Não existem conexões ocultas entre borda e redes internas ou de gerência.
- [ ] Eventos do perímetro chegam ao SIEM.

## Questões de compreensão

**1.** Por que NAT não deve ser tratado como controle de segurança?

??? success "Resposta comentada"

    Porque é uma função de roteamento: traduz endereços, mas não aplica política de acesso. A SP 800-41 Rev. 1 afirma explicitamente que NAT não faz parte da funcionalidade de segurança do firewall.

**2.** Qual a diferença entre WAF e WAAP?

??? success "Resposta comentada"

    O WAF protege aplicações web de ataques como injeção e XSS. O WAAP amplia essa proteção para APIs, bots e DDoS, normalmente como suíte ou serviço em nuvem.

**3.** Por que restringir a saída de servidores?

??? success "Resposta comentada"

    Porque servidores raramente precisam acessar a internet de forma ampla, e a saída é o caminho de comando e controle e de exfiltração. Uma lista de destinos permitidos reduz esses caminhos e torna tentativas indevidas visíveis.

## Exercício de tomada de decisão

!!! question "Cenário: inspeção de TLS na Lumen"

    A Lumen quer inspecionar o tráfego HTTPS de saída das estações para detectar exfiltração de dados de pacientes. O jurídico teme a inspeção de acessos pessoais dos funcionários (bancos, saúde do próprio funcionário). O SWG da empresa suporta decifragem por categoria, e o sistema de prontuários tem um aplicativo de desktop que usa certificate pinning. Há três propostas:

    - **A** — decifrar todo o tráfego HTTPS das estações;
    - **B** — decifrar por categoria: armazenamento de arquivos, webmail, compartilhamento e destinos desconhecidos, com DLP para padrões de dados de pacientes; categorias sensíveis para o funcionário e o aplicativo de prontuários ficam como exceções documentadas;
    - **C** — não decifrar; usar só a reputação dos destinos (nome do servidor e DNS) e DLP instalada nas estações.

    Compare as propostas com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e recomende uma política.

**Objetivos avaliados:** Avaliar trade-offs da inspeção de tráfego cifrado; definir política de saída (egress) para usuários e para servidores.

**Entrega esperada:** Matriz ponderada, política de inspeção por categoria com exceções nomeadas e as medidas que protegem o próprio inspetor.

**Critérios de avaliação:**

- A política separa o que é decifrado do que fica como exceção, com justificativa de privacidade e de compatibilidade (pinning).
- A resposta trata o SWG e a chave da CA de inspeção como ativos de alto valor, com proteção explícita.
- O risco residual inclui o tráfego não inspecionado e os dispositivos não gerenciados, com mitigação proporcional.

??? success "Resolução de referência"

    | Critério | Peso | A — Decifrar tudo | B — Decifrar por categoria | C — Sem decifragem |
    |:---|:---|:---|:---|:---|
    | Detecção de exfiltração de dados de pacientes | 3 | 3 | 2 | 1 |
    | Proporcionalidade e privacidade dos funcionários | 3 | 1 | 3 | 2 |
    | Risco de quebrar aplicações (pinning) | 2 | 1 | 2 | 3 |
    | Custo de desempenho e exposição do inspetor | 1 | 1 | 2 | 3 |
    | **Total ponderado** | | **15** | **21** | **18** |

    - **Pesos:** a detecção de exfiltração é o objetivo da iniciativa, e a proporcionalidade é a condição para que ela seja aceitável — os dois pesam 3. A quebra de aplicações é um risco operacional sério, mas tratável por exceção (peso 2). Custo e exposição do inspetor existem nas opções A e B e são mitigáveis (peso 1).
    - **Recomendação: B.** Concentra a decifragem onde a exfiltração é provável e deixa de fora o que é pessoal e sensível para o funcionário. Complementos: bloqueio de upload de arquivos para as categorias não inspecionadas, sem necessidade de negócio; política comunicada aos funcionários; avaliação de impacto à proteção de dados com o encarregado; acesso restrito aos registros de inspeção.
    - **Proteção do inspetor:** chave da autoridade certificadora de inspeção em HSM e administração do SWG pela zona de gestão — o SWG passa a ser um alvo de alto valor.
    - **Trade-off aceito e risco residual:** exfiltração pelas categorias não inspecionadas e por dispositivos não gerenciados; mitigada pelo bloqueio de upload e por controles no próprio sistema de prontuários (exportações registradas e limitadas).
    - **O que mudaria a decisão:** se o volume de dados de pacientes nas estações fosse muito pequeno e o acesso ocorresse só por aplicação web com exportação bloqueada, C seria suficiente; uma exigência contratual de inspeção integral pesaria a favor de A, desde que validada pelo jurídico.

    A matriz não decide sozinha: uma restrição legal identificada pelo jurídico elimina uma opção antes de qualquer soma.

    **Erros comuns:**

    - Supor que decifrar tudo é sempre mais seguro, ignorando proporcionalidade, LGPD e quebra de aplicações.
    - Esquecer que inspecionar exige terminar a sessão TLS com uma CA interna — e que isso cria um alvo novo.
    - Não envolver o jurídico e o encarregado de dados na definição das categorias sensíveis.

## Pontos-chave

- O perímetro é uma camada, não a defesa; ainda reduz exposição e controla a saída.
- DMZ separa o que é publicado do que é interno; o tráfego entre elas também passa pela política.
- WAF/WAAP protegem aplicações e APIs; IPS e NGFW inspecionam protocolos e aplicações.
- Política de saída restritiva para servidores é uma das medidas de maior efeito.
- Inspeção de TLS traz visibilidade e riscos; decida por categoria, com governança.

## Referências

### Fundamentação principal

- NIST. *SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy*. 2009 — Sec. 2.1, 3 e 4. *(Lido.)*
- NIST. *SP 800-215 — Guide to a Secure Enterprise Network Landscape*. 2022 — Sec. 3 (pp. 8–13). *(Lido.)*
- NSA. *Network Infrastructure Security Guidance*. 2022 — Sec. 2.1, 2.3 e 2.4. *(Lido.)*
- NIST. *SP 800-94 — Guide to Intrusion Detection and Prevention Systems*. 2007. <https://csrc.nist.gov/pubs/sp/800/94/final> — quatro classes de IDPS. *(Página oficial conferida.)*
- IETF. *RFC 9846 — The Transport Layer Security (TLS) Protocol Version 1.3*. Julho de 2026. <https://www.rfc-editor.org/rfc/rfc9846.html> — Sec. 1.3 (*Major Differences from TLS 1.2*); substitui a RFC 8446 — gratuito.
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles SC-7, SC-7(8), SC-7(10), SI-4(4), SC-5 e AC-4(4), conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- OWASP. *ASVS 5.0* — requisitos de aplicação que o WAF não substitui.
- PCI SSC. *PCI DSS v4.0.1* — controles de rede para o CDE.

### Aplicação prática

- Liste os serviços publicados na internet pela sua organização e, para cada um, indique se passa por WAF/WAAP, se termina na DMZ e qual a política de saída do servidor que o hospeda.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
