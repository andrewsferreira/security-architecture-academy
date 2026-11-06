---
id: M05-L04
title: "Aula 04 — Acesso remoto: VPN, ZTNA e bastion hosts"
public_title: "Módulo 5 — Aula 04 — Acesso remoto: VPN, ZTNA e bastion hosts"
description: Os padrões de acesso remoto — VPN, portais de aplicação, ZTNA e bastion/acesso privilegiado —, o que cada um expõe, como posicioná-los e como migrar de acesso de rede para acesso por aplicação sem interromper a operação.
domain: network-security
tier: professional
status: published
prerequisites: [M05-L02, M01-L02]
objectives:
  - Comparar VPN, portais de aplicação, ZTNA e bastion pelo que concedem e pelo que expõem.
  - Aplicar as premissas da SP 800-46 Rev. 2 sobre ambientes externos hostis.
  - Desenhar acesso administrativo remoto com bastion ou acesso privilegiado.
  - Planejar a migração de VPN de rede para acesso por aplicação.
minutes: 75
sources: [NIST-SP800-46-R2, NIST-SP800-215, NSA-NETWORK-INFRA-2022, MITRE-ATTACK, NIST-SP800-63-4, NIST-SP800-53]
further_reading: [NIST-SP800-207, CISA-ZTMM-2]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M05
---

# Aula 04 — Acesso remoto: VPN, ZTNA e bastion hosts { #acesso-remoto-vpn-ztna-e-bastion-hosts }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 5 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M05-L04</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Acesso remoto é um dos vetores iniciais mais usados em ataques — no ATT&CK, **External Remote Services (T1133)** aparece nas táticas Initial Access e Persistence. A decisão de arquitetura não é "VPN ou não", mas **que tipo de acesso conceder**: acesso à **rede** ou acesso a **aplicações específicas**, com que verificação de identidade e dispositivo, e com que registro. Esta aula compara os padrões e mostra como migrar de um para outro.

**Pré-requisitos:** [Perímetro e inspeção](02-perimeter-inspection.md) e [Princípios de design seguro](../01-security-fundamentals/02-secure-design-principles.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Comparar VPN, portais de aplicação, ZTNA e bastion pelo que concedem e pelo que expõem.
- Aplicar as premissas da SP 800-46 Rev. 2 sobre ambientes externos hostis.
- Desenhar acesso administrativo remoto com bastion ou acesso privilegiado.
- Planejar a migração de VPN de rede para acesso por aplicação.

## Conceito

### A premissa: o ambiente externo é hostil

A NIST SP 800-46 Rev. 2 recomenda planejar políticas e controles de teletrabalho supondo que **ambientes externos contêm ameaças hostis**: redes externas podem ser interceptadas e dispositivos clientes podem ser infectados por malware (Sumário executivo). A consequência para a arquitetura é direta: o acesso remoto deve conceder **o mínimo necessário** e verificar **identidade e dispositivo**.

### Quatro métodos clássicos

A SP 800-46 Rev. 2 descreve quatro métodos de acesso remoto (Sec. 2.2, subseções 2.2.1 a 2.2.4):

| Método | Como funciona | Observação do documento |
|:---|:---|:---|
| **Tunneling (VPN)** | Túnel cifrado (IPsec, TLS ou SSH) até um gateway | A aplicação e os dados ficam no dispositivo, que precisa de proteção própria |
| **Portais de aplicação** | Aplicações executadas no servidor do portal (web, terminal, VDI) | Dados ficam majoritariamente transitórios no cliente |
| **Acesso remoto a desktop** | Cliente controla uma estação interna específica | "Deve ser usado apenas em casos excepcionais, após análise cuidadosa dos riscos" (Sec. 2.2.3) |
| **Acesso direto à aplicação** | A própria aplicação provê cifragem e autenticação | Aceitável quando o servidor está no perímetro, na DMZ ou em nuvem pública |

O documento também recomenda que servidores de acesso remoto fiquem, em geral, **no perímetro da rede**, como ponto único de entrada (p. viii; Sec. 3.2, pp. 15–16).

### Acesso de rede versus acesso por aplicação

| | VPN de rede | ZTNA |
|:---|:---|:---|
| **O que concede** | Endereço na rede interna; alcance a um segmento | Sessão para aplicações específicas |
| **Visibilidade da rede** | O usuário (e o malware no dispositivo) vê o segmento | A rede permanece invisível; só aplicações autorizadas respondem |
| **Decisão** | Em geral, na conexão | Por aplicação, com contexto (identidade, dispositivo, risco) |
| **Tráfego para cloud** | Frequentemente volta pela sede (*hair-pinning*) | Direto ao serviço de acesso |

A SP 800-215 aponta limitações da VPN tradicional: o tráfego para serviços em nuvem é levado de volta aos concentradores da sede, aumentando latência e criando gargalos; vulnerabilidades em VPNs já foram divulgadas; hardware limita a escala; e agentes complicam o acesso de terceiros (Sec. 2.2, pp. 5–6). O mesmo documento descreve o ZTNA com três blocos — **cliente ou navegador**, **controlador** (ponto de decisão de política) e **gateway** (ponto de aplicação de política) (Sec. 5, p. 17).

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m05-l04-remote-access.mmd"
```

<figcaption>Figura 1 — VPN concede acesso de rede; ZTNA concede sessões por aplicação após decisão de política; bastion intermedia e grava o acesso administrativo.</figcaption>
</figure>

## Fundamentos técnicos

### Endurecendo a VPN que continua existindo

Quando a VPN permanece — por legado, custo ou casos específicos —, a NSA recomenda **desabilitar recursos desnecessários** e aplicar **filtragem de tráfego estrita** no gateway, limitar o acesso às portas e protocolos necessários e, quando possível, a pares conhecidos, e configurar explicitamente políticas IKEv2 com parâmetros criptográficos fortes (Sec. 2.6). A essas recomendações somam-se:

- **MFA resistente a phishing** (o cenário RSK-007 da Meridiana começou por uma VPN só com senha). A SP 800-63B-4 exige autenticador resistente a phishing no nível AAL3 e pede que o AAL2 ofereça ao menos uma opção resistente a phishing; para acesso remoto a uma organização, essa é a referência para escolher o fator — senha mais código por SMS não atende.
- **Postura do dispositivo** antes de conceder acesso.
- **Segmentação pós-VPN:** o pool de endereços da VPN é uma zona, com matriz de fluxos própria — nunca "acesso à rede inteira".
- **Correção prioritária** do concentrador, por ser exposto à internet.

### Bastion e acesso privilegiado remoto

Administradores e fornecedores precisam de acesso a sistemas, não a redes. O padrão recomendado:

1. Autenticação forte no **bastion** ou na solução de **acesso privilegiado** (PAM), a partir de dispositivo confiável.
2. **Aprovação** e, quando possível, **acesso just-in-time**.
3. Sessão **intermediada** — o administrador não recebe a credencial do sistema-alvo.
4. **Gravação** da sessão e registro dos comandos.
5. Sistemas-alvo aceitam protocolos administrativos **apenas a partir do bastion** (Aula 03).

A NSA, para equipamentos de rede, recomenda restringir o acesso de gerência a sistemas de administradores, preferir SSH versão 2 e limitar sessões administrativas a cinco minutos de inatividade ou menos (Sec. 7.3–7.5).

### Migração gradual

| Etapa | Ação | Efeito |
|:---|:---|:---|
| 1 | MFA resistente a phishing e postura na VPN atual | Reduz o risco imediato |
| 2 | Zona e matriz de fluxos para o pool da VPN | Limita o alcance |
| 3 | Publicar as aplicações web mais usadas via ZTNA | Tira a maioria dos usuários da VPN |
| 4 | Administração via bastion/PAM | Separa acesso privilegiado |
| 5 | VPN residual para casos documentados, com dono e prazo | Exceções explícitas |

## Exemplo empresarial

!!! example "Meridiana — da VPN só com senha ao acesso por aplicação"

    A VPN da Meridiana, só com senha e acesso a toda a rede, era o primeiro passo do cenário RSK-007. A migração levou quatro meses:

    - **Mês 1:** MFA resistente a phishing para todos os usuários da VPN e restrição do pool a uma zona com 14 fluxos permitidos.
    - **Mês 2:** ERP web, intranet e portal de RH publicados via ZTNA; 80% dos usuários deixaram a VPN.
    - **Mês 3:** fornecedores de manutenção do WMS passaram a acessar apenas por acesso privilegiado com aprovação e gravação.
    - **Mês 4:** VPN mantida para 12 usuários de TI com ferramentas que não funcionam via ZTNA, com revisão trimestral.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Tipo de acesso | Rede inteira | Aplicações específicas |
| Autenticação | Senha | MFA resistente a phishing + postura do dispositivo |
| Decisão | Uma vez, na conexão | Por aplicação, com contexto |
| Fornecedores | Conta VPN permanente | Acesso privilegiado com aprovação e gravação |
| Administração | De qualquer lugar | Apenas via bastion/PAM |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referência voluntária:

| Controle ou padrão | Objetivo no acesso remoto | Referência |
|:---|:---|:---|
| Acesso remoto autorizado por tipo | Documentar restrições e requisitos de cada tipo de acesso remoto e autorizá-lo antes do uso | SP 800-53: AC-17 (Remote Access) |
| Monitoramento e controle automatizados | Monitorar e controlar os métodos de acesso remoto | SP 800-53: AC-17(1) |
| Sessões cifradas | Proteger confidencialidade e integridade das sessões | SP 800-53: AC-17(2) |
| Pontos de controle gerenciados | Encaminhar o acesso remoto por pontos de controle autorizados — o gateway no perímetro | SP 800-53: AC-17(3); SP 800-46 Rev. 2, Sec. 3.2 |
| Comandos privilegiados com evidência | Permitir acesso privilegiado remoto só em formato que gere evidência avaliável — a gravação do bastion | SP 800-53: AC-17(4) |
| MFA | MFA para contas privilegiadas e não privilegiadas | SP 800-53: IA-2(1) e IA-2(2); SP 800-63B-4 para resistência a phishing |
| Split tunneling | Impedir túnel dividido, salvo quando provisionado com segurança | SP 800-53: SC-7(7) |
| Encerramento de sessão | Encerrar sessões inativas | SP 800-53: AC-12; NSA, Sec. 7 (gerência de equipamentos de rede) |

## Aplicabilidade: on-premises, cloud e híbrido

Para aplicações em cloud, o ZTNA ou o acesso direto à aplicação com identidade federada evita o *hair-pinning* pela sede. Para administração de cloud, serviços de sessão gerenciada do provedor cumprem o papel de bastion sem expor portas na internet. Em ambientes híbridos, um mesmo serviço de ZTNA pode publicar aplicações dos dois lados, unificando a política — desde que os conectores nos dois ambientes sejam tratados como componentes críticos.

## Como especificar e implementar

- "Acesso remoto de usuários é concedido por aplicação; acesso de rede é exceção documentada, com dono e prazo."
- "Todo acesso remoto exige MFA resistente a phishing e verificação de postura do dispositivo."
- "Acesso administrativo e de fornecedores ocorre via bastion ou acesso privilegiado, com aprovação, intermediação e gravação."
- "Concentradores e gateways de acesso remoto ficam no perímetro, com correção prioritária e registro no SIEM."

## Trade-offs, limitações e antipadrões

- **Trade-off:** ZTNA melhora a granularidade, mas depende de um serviço e de conectores críticos; sua indisponibilidade bloqueia o acesso.
- **Antipadrão — ZTNA como VPN renomeada:** publicar "a rede inteira" como uma aplicação.
- **Antipadrão — conta de fornecedor permanente:** usada por várias pessoas, sem aprovação.
- **Limitação:** acesso por aplicação não resolve dispositivos comprometidos com credenciais válidas; postura e detecção continuam necessárias.

## Como validar

- A partir de um dispositivo remoto autorizado, verificar que só as aplicações concedidas respondem.
- Tentar acesso com dispositivo não gerenciado e confirmar o bloqueio.
- Revisar gravações de sessões de fornecedores por amostragem.
- Varrer o endereço público do concentrador e verificar versão e serviços expostos.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhum acesso remoto só com senha | Relatório do provedor de identidade: 100% dos logins remotos com MFA resistente a phishing |
| Dispositivo não gerenciado é bloqueado | Teste com dispositivo sem postura, negado e registrado |
| O pool da VPN residual alcança só os fluxos da matriz | Teste de alcance a partir do pool |
| Toda sessão de fornecedor tem aprovação e gravação | Amostra de sessões do mês com aprovação, gravação e conta nominal |
| Exceções de VPN com dono e prazo | Lista de exceções revisada no trimestre |

## Como apresentar e justificar

- **Para a diretoria:** "O ataque mais provável começa pelo acesso remoto. Trocamos 'entrar na rede' por 'entrar na aplicação', com MFA e checagem do dispositivo."
- **Para usuários:** "Vocês acessam as mesmas aplicações, sem conectar a VPN, e o acesso a nuvem fica mais rápido."

## Checklist de revisão arquitetural

- [ ] O acesso remoto é por aplicação, salvo exceções documentadas.
- [ ] MFA resistente a phishing e postura são exigidos.
- [ ] O pool da VPN residual é uma zona com fluxos mínimos.
- [ ] Acesso administrativo e de fornecedores passa por bastion/PAM com gravação.
- [ ] Gateways de acesso remoto têm correção prioritária e logs no SIEM.

## Questões de compreensão

**1.** Qual a diferença essencial entre VPN de rede e ZTNA?

??? success "Resposta comentada"

    A VPN concede acesso à rede (um segmento), e a partir dali o dispositivo alcança o que a rede permitir. O ZTNA concede sessões para aplicações específicas, após decisão de política com contexto; a rede permanece invisível.

**2.** Que premissa a SP 800-46 Rev. 2 recomenda adotar no planejamento de teletrabalho?

??? success "Resposta comentada"

    Que ambientes externos contêm ameaças hostis — redes externas podem ser interceptadas e dispositivos podem estar infectados —, o que exige acesso mínimo e verificação de identidade e dispositivo.

**3.** Por que o administrador não deveria receber a credencial do sistema-alvo ao usar o bastion?

??? success "Resposta comentada"

    Porque a credencial exposta pode ser reutilizada fora do bastion, contornando aprovação, intermediação e gravação. Com a sessão intermediada, o acesso só existe pelo caminho controlado.

## Exercício de tomada de decisão

!!! question "Cenário: acesso remoto de fornecedores do WMS da Meridiana"

    Três fornecedores fazem manutenção remota do WMS. Opções: (A) contas VPN individuais com acesso à zona dos CDs; (B) acesso privilegiado com aprovação just-in-time, sessão intermediada e gravação; (C) ferramenta de acesso remoto instalada pelo fornecedor nos servidores. Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), com pesos justificados, e recomende uma.

**Objetivos avaliados:** Desenhar acesso administrativo remoto com bastion ou acesso privilegiado; comparar VPN, portais de aplicação, ZTNA e bastion pelo que concedem e pelo que expõem.

**Entrega esperada:** Matriz ponderada, recomendação e as condições operacionais do acesso de terceiros (contas, aprovação, revisão).

**Critérios de avaliação:**

- A recomendação concede acesso a sistemas específicos, não a segmentos de rede.
- Há rastreabilidade das ações do terceiro (sessão intermediada e gravada) e revisão por amostragem.
- A resposta trata a ferramenta instalada pelo fornecedor como canal de entrada não controlado (T1133).

??? success "Resolução de referência"

    | Critério | Peso | A — VPN individual | B — Acesso privilegiado | C — Ferramenta do fornecedor |
    |:---|:---|:---|:---|:---|
    | Limitação do alcance | 3 | 1 | 3 | 2 |
    | Rastreabilidade das ações | 3 | 1 | 3 | 1 |
    | Controle da organização sobre o acesso | 2 | 2 | 3 | 1 |
    | Facilidade para o fornecedor | 1 | 2 | 2 | 3 |
    | **Total ponderado** | | **12** | **26** | **14** |

    - **Pesos:** o risco é de terceiros com acesso a sistemas que param os CDs; limitar o alcance e rastrear as ações são o que reduz esse risco, e pesam 3. O controle da organização sobre quando o acesso existe pesa 2. A facilidade para o fornecedor importa para a adesão, mas não define a segurança (peso 1).
    - **Recomendação: B.** Concede acesso apenas aos servidores do WMS, quando aprovado, com gravação. A opção C cria um canal de entrada controlado pelo fornecedor — um caminho clássico de comprometimento da cadeia de suprimentos (técnica External Remote Services, T1133, no ATT&CK) — e deve ser removida.
    - **Condições:** contas nominais por técnico; aprovação pelo dono do WMS; revisão mensal das gravações por amostragem.
    - **Trade-off aceito e risco residual:** a aprovação acrescenta minutos a cada chamado e depende de alguém disponível no plantão; um técnico autorizado ainda pode errar ou agir mal durante a sessão — a gravação e a revisão por amostragem tornam isso detectável, não impossível.
    - **O que mudaria a decisão:** se o contrato exigir atendimento emergencial 24 horas sem aprovador disponível, a aprovação prévia pode virar acesso emergencial com aprovação posterior e alerta imediato; se o WMS migrar para um serviço gerenciado do fornecedor, a questão passa a ser o acordo de responsabilidades, e não o acesso à rede.

    **Erros comuns:**

    - Aceitar contas VPN compartilhadas por fornecedor, sem nome por técnico.
    - Ignorar o acesso emergencial fora do horário e deixar a exceção sem regra.
    - Confundir gravação de sessão com prevenção: ela torna o abuso detectável, não impossível.

## Pontos-chave

- Acesso remoto é vetor frequente de ataque inicial; trate o ambiente externo como hostil.
- Prefira acesso por aplicação (ZTNA, portais) a acesso de rede (VPN).
- O ZTNA tem cliente, controlador (decisão) e gateway (aplicação de política).
- Acesso administrativo e de fornecedores passa por bastion ou PAM, com aprovação e gravação.
- Migre em etapas: endureça a VPN, limite seu alcance, publique aplicações, isole a administração.

## Referências

### Fundamentação principal

- NIST. *SP 800-46 Rev. 2 — Guide to Enterprise Telework, Remote Access, and BYOD Security*. K. Scarfone, M. Souppaya, 2016. <https://csrc.nist.gov/pubs/sp/800/46/r2/final> — Sumário executivo, Sec. 2.2 (2.2.1–2.2.4) e Sec. 3.2. Referências por seção, não por página. *(Lido.)*
- NIST. *SP 800-215* — Sec. 2.2 (pp. 5–6) e Sec. 5 (p. 17). *(Lido; página do ZTNA reconferida em 2026-10-29.)*
- NSA. *Network Infrastructure Security Guidance*. 2022 — Sec. 2.6 e 7. *(Lido.)*
- MITRE. *ATT&CK v20* — T1133 External Remote Services.
- NIST. *SP 800-63B-4 — Authentication and Authenticator Management*. 2025. <https://csrc.nist.gov/pubs/sp/800/63/4/final> — níveis de garantia e resistência a phishing. *(Lido até a Sec. 3.2.)* — gratuito.
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-17, AC-17(1) a (4), IA-2(1), IA-2(2), SC-7(7) e AC-12, conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- NIST. *SP 800-207 — Zero Trust Architecture* — componentes lógicos aprofundados na Aula 02 do Módulo 7.
- CISA. *Zero Trust Maturity Model 2.0* — pilar de redes.

### Aplicação prática

- Liste quem usa a VPN da sua organização e para quê. Classifique cada caso em "aplicação web", "administração", "fornecedor" e "outro", e proponha o padrão de acesso para cada grupo.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
