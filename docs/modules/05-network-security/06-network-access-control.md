---
id: M05-L06
title: "Aula 06 — Network Access Control"
public_title: "Módulo 5 — Aula 06 — Network Access Control"
description: Como controlar quais dispositivos entram na rede local e em que segmento — 802.1X com EAP-TLS, verificação de postura, quarentena e tratamento de dispositivos que não suportam autenticação — e o papel do NAC em uma arquitetura que caminha para Zero Trust.
domain: network-security
tier: professional
status: published
prerequisites: [M05-L01]
objectives:
  - Explicar o fluxo 802.1X com suplicante, autenticador e servidor de autenticação.
  - Comparar autenticação por certificado e por endereço MAC.
  - Desenhar políticas de atribuição de segmento e de quarentena com base em identidade e postura.
  - Tratar dispositivos sem suporte a 802.1X sem abrir exceções permanentes.
minutes: 45
sources: [NSA-NETWORK-INFRA-2022, NIST-SP800-41-R1, RFC-9190, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [NIST-SP800-215, NIST-SP800-207]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M05
---

# Aula 06 — Network Access Control { #network-access-control }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 5 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">45 min · ID técnico: M05-L06</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Em muitas redes corporativas, qualquer dispositivo ligado a uma tomada ou à rede sem fio recebe endereço e acesso. **Network Access Control (NAC)** responde a duas perguntas antes de conceder conectividade: **que dispositivo é este** e **em que estado ele está** — e, com base nisso, coloca-o no segmento certo ou em quarentena. Esta aula apresenta o fluxo 802.1X, as escolhas de autenticação e o tratamento de dispositivos que não suportam o padrão.

**Pré-requisito:** [Zonas de confiança, segmentação e microsegmentação](01-zones-segmentation.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar o fluxo 802.1X com suplicante, autenticador e servidor de autenticação.
- Comparar autenticação por certificado e por endereço MAC.
- Desenhar políticas de atribuição de segmento e de quarentena com base em identidade e postura.
- Tratar dispositivos sem suporte a 802.1X sem abrir exceções permanentes.

## Conceito

### O que o NAC faz

A SP 800-41 Rev. 1 descreve o NAC como tecnologia que concede acesso com base nas **credenciais** do usuário e em **verificações de saúde** do dispositivo (p. 2-8). A NSA recomenda implementar NAC e observa que a solução mais robusta usa **802.1X**, autenticando dispositivos com certificados digitais em vez de confiar em endereços MAC (Sec. 2.5).

### Os três papéis do 802.1X

| Papel | Quem é | O que faz |
|:---|:---|:---|
| **Suplicante** | O dispositivo | Apresenta credenciais (de preferência, certificado) |
| **Autenticador** | Switch ou ponto de acesso | Mantém a porta bloqueada, exceto para autenticação, e aplica o resultado |
| **Servidor de autenticação** | Servidor RADIUS com o motor de política | Valida credenciais, consulta postura e devolve a política (segmento, listas de acesso) |

O método de autenticação mais forte é o **EAP-TLS**, que, segundo a RFC 9190, oferece autenticação mútua baseada em certificados pelo handshake TLS e é amplamente suportado em redes IEEE 802.11 e 802.1AE que usam 802.1X; a RFC 9190 (2022) especifica seu uso com TLS 1.3.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m05-l06-nac.mmd"
```

<figcaption>Figura 1 — Fluxo 802.1X com EAP-TLS e consulta de postura: acesso ao segmento autorizado ou quarentena.</figcaption>
</figure>

## Fundamentos técnicos

### Certificado versus MAC

| | Certificado (EAP-TLS) | Endereço MAC (MAB) |
|:---|:---|:---|
| **Prova de identidade** | Posse de chave privada | Apenas um identificador que trafega em claro |
| **Falsificação** | Exige roubar a chave do dispositivo | Trivial: basta copiar o MAC |
| **Gestão** | PKI e emissão automatizada (MDM) | Inventário de endereços |
| **Uso recomendado** | Dispositivos corporativos | Somente para dispositivos que não suportam 802.1X, em segmento restrito |

### Política de atribuição

O resultado do NAC é uma **decisão de segmento** coerente com as zonas da Aula 01:

| Situação | Resultado |
|:---|:---|
| Estação corporativa, certificado válido, postura conforme | Zona de usuários |
| Estação corporativa, postura não conforme (EDR desligado, sistema desatualizado) | Quarentena com acesso à remediação |
| Dispositivo pessoal ou visitante | Rede de visitantes, só internet |
| Impressora, câmera, coletor (MAB) | Segmento específico com fluxos mínimos |
| Desconhecido | Nenhum acesso, ou rede de visitantes |

### Postura

A verificação de postura consulta fontes como MDM e EDR: sistema atualizado, agente de proteção ativo, disco cifrado. Ela não precisa ser só na conexão — reavaliações periódicas permitem mover para quarentena um dispositivo que deixou de estar conforme.

### Dispositivos sem 802.1X

Coletores antigos, impressoras e equipamentos de OT frequentemente não suportam 802.1X. O tratamento recomendado:

1. **Inventário** com dono e justificativa.
2. **MAB** apenas para colocá-los em um **segmento restrito** com fluxos mínimos (Aula 01).
3. **Perfilamento** (tipo de dispositivo observado) para detectar um MAC clonado usado por um computador.
4. **Plano de substituição** por modelos com 802.1X, com prazo.

## Exemplo empresarial

!!! example "Meridiana — o notebook ligado à tomada do CD"

    Em uma visita a um centro de distribuição, um técnico de um fornecedor ligou o notebook pessoal a uma tomada de rede e recebeu acesso à mesma rede dos coletores e do WMS. O episódio motivou o NAC:

    - Estações corporativas com **EAP-TLS** e certificados emitidos pelo MDM.
    - Coletores sem suporte a 802.1X via **MAB** em segmento próprio, com fluxos apenas para o WMS e **perfilamento** para detectar MAC clonado.
    - Dispositivos desconhecidos na **rede de visitantes**.
    - Postura: estação sem EDR ativo vai para **quarentena** com acesso apenas ao servidor de atualização.

    O projeto começou em **modo monitor** (registrando sem bloquear) por três semanas, o que revelou 37 dispositivos sem inventário — 9 deles sem dono identificado e desligados.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Entrada na rede | Qualquer dispositivo conectado | 802.1X com certificados |
| Identificação | MAC ou nada | Certificado; MAB só para exceções em segmento restrito |
| Segmento | Fixo por porta | Atribuído por identidade e postura |
| Não conformes | Acesso normal | Quarentena com remediação |
| Implantação | Bloqueio imediato | Modo monitor, inventário, depois bloqueio |

## Controles e padrões relevantes

| Controle ou padrão | Objetivo no NAC | Referência |
|:---|:---|:---|
| Identificação e autenticação de dispositivos | Identificar e autenticar o dispositivo antes da conexão | SP 800-53 Rev. 5: IA-3 (Device Identification and Authentication) |
| Autenticação bidirecional criptográfica | Autenticação mútua baseada em criptografia, como no EAP-TLS | SP 800-53 Rev. 5: IA-3(1); RFC 9190 |
| Acesso sem fio | Requisitos por tipo de acesso sem fio, com autenticação e cifragem | SP 800-53 Rev. 5: AC-18 e AC-18(1) |
| Inventário de componentes | Inventário completo e preciso, base para MAB e perfilamento | SP 800-53 Rev. 5: CM-8; CIS Controls v8.1: Controle 1 (Inventory and Control of Enterprise Assets) |
| Gestão da infraestrutura de rede | Arquitetura e acesso à rede geridos | CIS Controls v8.1: Controle 12 (Network Infrastructure Management) |
| NAC com 802.1X | Autenticar dispositivos com certificados, não com MAC | NSA, Sec. 2.5 |

Os controles da SP 800-53 e dos CIS Controls são referências voluntárias; títulos conferidos no catálogo OSCAL da Release 5.2.0 e na lista oficial da v8.1.

## Aplicabilidade: on-premises, cloud e híbrido

NAC é um controle de **rede local** — escritórios, centros de distribuição, clínicas. Em cloud não há "tomada"; o equivalente é o controle de quem cria recursos e com que identidade de workload. Em uma arquitetura Zero Trust (Módulo 7), o NAC continua útil para limitar o que dispositivos não gerenciados alcançam localmente, mas a decisão de acesso a aplicações migra para identidade e postura avaliadas por aplicação.

## Como especificar e implementar

- "Dispositivos corporativos autenticam-se na rede local por 802.1X com EAP-TLS e certificados gerenciados."
- "A atribuição de segmento considera identidade e postura; dispositivos não conformes vão para quarentena."
- "MAB é permitido apenas para dispositivos inventariados que não suportam 802.1X, em segmento restrito, com perfilamento."
- "A implantação começa em modo monitor e passa a bloqueio após o inventário."

## Trade-offs, limitações e antipadrões

- **Trade-off:** segurança versus operação — certificados exigem PKI e MDM maduros; quarentenas indevidas geram chamados.
- **Antipadrão — MAB para tudo:** NAC que aceita qualquer MAC cadastrado é facilmente contornado.
- **Antipadrão — modo monitor eterno:** o projeto nunca chega ao bloqueio.
- **Limitação:** NAC controla a entrada na rede, não o que o dispositivo faz depois; segmentação e detecção continuam necessárias.

## Como validar

- Conectar um dispositivo desconhecido e verificar o destino (visitantes ou nenhum acesso).
- Clonar o MAC de uma impressora em um notebook e verificar se o perfilamento detecta.
- Desligar o EDR de uma estação de teste e verificar a quarentena.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Dispositivo desconhecido não chega a segmentos corporativos | Teste em tomada e Wi-Fi corporativo, com destino rede de visitantes ou nenhum acesso |
| Toda entrada de MAB corresponde a um ativo inventariado com dono | Relatório do NAC cruzado com o inventário |
| MAC clonado é detectado | Teste com notebook usando o MAC de uma impressora, com alerta |
| Estação não conforme vai para quarentena | Teste com EDR desligado; acesso apenas à remediação |
| Modo monitor encerrado com data | Registro da passagem a bloqueio por local |

## Como apresentar e justificar

- **Para a diretoria:** "Hoje, qualquer notebook ligado a uma tomada entra na rede dos CDs. Com NAC, ele vai para a rede de visitantes."
- **Para a operação:** "Três semanas em modo monitor antes de bloquear; aproveitamos para limpar o inventário."

## Checklist de revisão arquitetural

- [ ] Dispositivos corporativos usam EAP-TLS com certificados.
- [ ] MAB restrito a dispositivos inventariados, em segmento próprio, com perfilamento.
- [ ] Política de quarentena com caminho de remediação.
- [ ] Rede de visitantes isolada.
- [ ] Plano de substituição para dispositivos sem 802.1X.

## Questões de compreensão

**1.** Quais são os três papéis do 802.1X?

??? success "Resposta comentada"

    Suplicante (o dispositivo), autenticador (switch ou ponto de acesso) e servidor de autenticação (RADIUS com a política).

**2.** Por que a autenticação por MAC é fraca?

??? success "Resposta comentada"

    Porque o MAC é apenas um identificador visível na rede, que pode ser copiado facilmente; não prova a posse de nenhum segredo. Certificados exigem a chave privada do dispositivo.

**3.** O que o NAC não resolve?

??? success "Resposta comentada"

    O comportamento do dispositivo depois de entrar na rede. Um dispositivo autorizado e comprometido continua alcançando o que seu segmento permite — por isso NAC se combina com segmentação, detecção e controles de identidade.

## Exercício de tomada de decisão

!!! question "Cenário: NAC nas clínicas da Lumen"

    As 20 clínicas da Lumen têm estações, impressoras, equipamentos de diagnóstico (alguns sem suporte a 802.1X e sem atualização do fabricante) e Wi-Fi para pacientes. Proponha a política de NAC e os segmentos resultantes e justifique-a perante a diretoria comparando três alternativas com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério):

    - **A** — 802.1X com EAP-TLS para estações, MAB com perfilamento em segmentos restritos para equipamentos e impressoras, rede de visitantes isolada;
    - **B** — MAB para todos os dispositivos, sem certificados;
    - **C** — sem NAC: VLAN fixa por porta, inventário e segmentação.

**Objetivos avaliados:** Desenhar políticas de atribuição de segmento e de quarentena com base em identidade e postura; tratar dispositivos sem suporte a 802.1X sem abrir exceções permanentes.

**Entrega esperada:** Matriz ponderada, tabela de segmentos resultantes por tipo de dispositivo e o plano de implantação por clínica.

**Critérios de avaliação:**

- Cada classe de dispositivo tem segmento, método de autenticação e fluxos permitidos definidos.
- Dispositivos sem 802.1X ficam em segmento restrito, com perfilamento, dono e plano de substituição.
- A implantação começa em modo monitor, com clínica-piloto, antes de aplicar quarentena.

??? success "Resolução de referência"

    - **Estações corporativas:** EAP-TLS, postura via MDM/EDR; conformes na zona de usuários; não conformes em quarentena.
    - **Equipamentos de diagnóstico sem 802.1X:** MAB com perfilamento, em segmento de equipamentos médicos com fluxos apenas para o servidor de imagens; sem acesso à internet; inventário com dono clínico e acompanhamento das atualizações do fabricante (controles compensatórios, Módulo 8 — Aula 05).
    - **Impressoras:** MAB em segmento próprio, aceitando impressão apenas do servidor de impressão.
    - **Wi-Fi de pacientes:** rede de visitantes isolada, só internet, com isolamento entre clientes.
    - **Implantação:** modo monitor por clínica, começando por uma clínica-piloto.

    Matriz das três alternativas do enunciado:

    | Critério | Peso | A — 802.1X + MAB restrito | B — MAB para tudo | C — VLAN fixa por porta |
    |:---|:---|:---|:---|:---|
    | Impedir dispositivos não autorizados nos segmentos clínicos | 3 | 3 | 1 | 1 |
    | Compatibilidade com equipamentos de diagnóstico sem suporte | 2 | 2 | 3 | 3 |
    | Esforço de implantação nas 20 clínicas | 2 | 1 | 2 | 3 |
    | Detecção de MAC clonado e de postura não conforme | 2 | 3 | 1 | 1 |
    | **Total ponderado** | | **21** | **15** | **17** |

    - **Pesos:** o problema é impedir que qualquer dispositivo chegue aos equipamentos clínicos (peso 3). Compatibilidade, esforço e detecção pesam 2: são restrições reais, mas nenhuma isolada define a segurança.
    - **Recomendação: A.** É a única que impede um dispositivo desconhecido de entrar em um segmento clínico e detecta um MAC copiado. O esforço maior (PKI e MDM nas estações) é absorvido pela implantação gradual, clínica a clínica.
    - **Trade-off aceito e risco residual:** equipamentos de diagnóstico continuam autenticados só por MAC; um atacante com acesso físico pode imitar um deles se o perfilamento falhar — o segmento restrito, sem internet e com fluxos só para o servidor de imagens, limita o que ele alcança.
    - **O que mudaria a decisão:** se as clínicas não tivessem MDM nem PKI e não pudessem tê-los no ano, C com inventário rigoroso e portas desativadas quando sem uso seria o primeiro passo, com A planejado; se os fabricantes oferecessem 802.1X nos equipamentos, o MAB deixaria de ser necessário nesse segmento.

    **Erros comuns:**

    - Usar MAB como método principal, tratando o endereço MAC como prova de identidade.
    - Deixar equipamentos clínicos sem 802.1X em uma exceção permanente, sem segmento próprio.
    - Esquecer o isolamento entre clientes na rede de visitantes.

## Pontos-chave

- NAC decide quem entra na rede local e em que segmento.
- 802.1X com EAP-TLS e certificados é a forma robusta; MAB é exceção restrita.
- Postura permite quarentena de dispositivos não conformes.
- Dispositivos sem 802.1X vão para segmentos restritos, com perfilamento e plano de substituição.
- NAC controla a entrada, não o comportamento — combine com segmentação e detecção.

## Referências

### Fundamentação principal

- NSA. *Network Infrastructure Security Guidance*. 2022 — Sec. 2.5, NAC com 802.1X. *(Lido.)*
- NIST. *SP 800-41 Rev. 1* — NAC (p. 2-8). *(Lido.)*
- IETF. *RFC 9190 — EAP-TLS 1.3*. 2022. <https://www.rfc-editor.org/rfc/rfc9190.html>. *(Introdução lida.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles IA-3, IA-3(1), AC-18, AC-18(1) e CM-8, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controles 1 e 12 — gratuito.

### Leitura complementar

- NIST. *SP 800-215* — Sec. 4.4, autenticação e saúde de dispositivos.
- NIST. *SP 800-207 — Zero Trust Architecture*.

### Aplicação prática

- Faça o inventário dos tipos de dispositivo que se conectam a um escritório da sua organização e classifique cada um em "802.1X com certificado", "MAB em segmento restrito" ou "rede de visitantes".

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
