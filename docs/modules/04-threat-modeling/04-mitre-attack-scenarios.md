---
id: M04-L04
title: "Aula 04 — MITRE ATT&CK para cenários de ataque"
public_title: "Módulo 4 — Aula 04 — MITRE ATT&CK para cenários de ataque"
description: Como usar o MITRE ATT&CK v20 — táticas, técnicas e a estrutura da matriz Enterprise — para descrever cenários de ataque realistas, avaliar a cobertura de controles preventivos e detectivos ao longo da cadeia e priorizar decisões de arquitetura.
domain: application-security
tier: professional
status: published
prerequisites: [M04-L03, M01-L06]
objectives:
  - Explicar a estrutura do ATT&CK — táticas, técnicas e subtécnicas — e a reorganização recente das táticas Enterprise.
  - Descrever um cenário de risco como sequência de táticas e técnicas.
  - Avaliar a cobertura de controles preventivos, detectivos e de recuperação ao longo do cenário.
  - Reconhecer os limites do ATT&CK como ferramenta de arquitetura.
minutes: 75
sources: [MITRE-ATTACK, BOOK-GOOGLE-BSRS, NIST-SP800-30-R1]
further_reading: [MITRE-CAPEC, NIST-CSF-2]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M04
---

# Aula 04 — MITRE ATT&CK para cenários de ataque { #mitre-attck-para-cenarios-de-ataque }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 4 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M04-L04</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    STRIDE e árvores de ataque ajudam a imaginar o que pode dar errado. O **MITRE ATT&CK** ajuda a descrever o que **adversários reais fazem**, em uma linguagem comum entre arquitetura, SOC, red team e threat intelligence. Para o arquiteto, seu maior valor é transformar um cenário de risco do register em uma **sequência de passos concretos** e perguntar, para cada passo: que controle impede, que controle detecta e como recuperamos? Esta aula usa a versão v20 da matriz Enterprise.

**Pré-requisitos:** [Attack trees e abuse cases](03-attack-trees-abuse-cases.md) e [Ameaça, vulnerabilidade, risco e controle](../01-security-fundamentals/06-threat-vulnerability-risk.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar a estrutura do ATT&CK — táticas, técnicas e subtécnicas — e a reorganização recente das táticas Enterprise.
- Descrever um cenário de risco como sequência de táticas e técnicas.
- Avaliar a cobertura de controles preventivos, detectivos e de recuperação ao longo do cenário.
- Reconhecer os limites do ATT&CK como ferramenta de arquitetura.

## Conceito

### Táticas e técnicas

O ATT&CK organiza o comportamento de adversários em:

- **Táticas** — o **porquê**: o objetivo do adversário naquele momento (obter acesso, mover-se lateralmente, causar impacto).
- **Técnicas** e **subtécnicas** — o **como**: a forma concreta de alcançar a tática (usar serviços remotos externos, extrair credenciais do sistema operacional).

Uma mesma técnica pode servir a várias táticas. **Valid Accounts (T1078)**, por exemplo, aparece em Stealth, Persistence, Privilege Escalation e Initial Access.

### A matriz Enterprise na v20

A versão atual é a **v20**, em vigor desde 13/10/2026, segundo a página de versões do ATT&CK. A página de táticas Enterprise lista **15 táticas**:

| ID | Tática | Objetivo do adversário |
|:---|:---|:---|
| TA0043 | Reconnaissance | Coletar informações para planejar operações |
| TA0042 | Resource Development | Estabelecer recursos para apoiar operações |
| TA0001 | Initial Access | Entrar na rede-alvo |
| TA0002 | Execution | Executar código ou instruções maliciosas |
| TA0003 | Persistence | Manter o acesso |
| TA0004 | Privilege Escalation | Obter permissões mais altas |
| TA0005 | Stealth | Esconder ações para que pareçam comportamento normal |
| TA0112 | Defense Impairment | Quebrar mecanismos e ferramentas de segurança para que os defensores percam visibilidade ou confiança |
| TA0006 | Credential Access | Roubar nomes de contas e senhas |
| TA0007 | Discovery | Conhecer o ambiente |
| TA0008 | Lateral Movement | Mover-se pelo ambiente |
| TA0009 | Collection | Reunir dados de interesse |
| TA0011 | Command and Control | Comunicar-se com sistemas comprometidos |
| TA0010 | Exfiltration | Roubar dados |
| TA0040 | Impact | Manipular, interromper ou destruir sistemas e dados |

!!! warning "Atenção a materiais desatualizados"

    Muitos cursos e ferramentas ainda mostram 14 táticas e a tática *Defense Evasion*. Na matriz atual, o ID TA0005 aparece como **Stealth**, e **Defense Impairment (TA0112)** é uma tática própria, com 18 técnicas — entre elas Disable or Modify Tools (T1685). A página da TA0112 registra sua criação em 14/04/2026, antes da v20; a v20 mantém essa organização. Ao usar o ATT&CK em documentos de arquitetura, registre a versão.

## Fundamentos técnicos

### Do cenário do register à sequência de técnicas

O cenário RSK-007 da Meridiana — ransomware a partir do acesso remoto — pode ser descrito assim (técnicas conferidas na v20):

| Passo | Tática | Técnica | Condição predisponente na Meridiana |
|:---|:---|:---|:---|
| 1 | Initial Access | External Remote Services (T1133) com Valid Accounts (T1078) | VPN só com senha |
| 2 | Credential Access | OS Credential Dumping (T1003) | Administradores do domínio logam em servidores comuns |
| 3 | Discovery | Account Discovery (T1087) | Sem detecção de enumeração |
| 4 | Lateral Movement | Remote Services (T1021) | Rede plana; RDP aberto entre servidores |
| 5 | Defense Impairment | Disable or Modify Tools (T1685) | Agente de proteção sem proteção contra adulteração |
| 6 | Impact | Inhibit System Recovery (T1490) e Data Encrypted for Impact (T1486) | Backups apagáveis com credenciais do domínio |

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m04-l04-attack-flow.mmd"
```

<figcaption>Figura 1 — Cenário de ransomware da Meridiana mapeado a táticas e técnicas do ATT&CK v20, com o controle de arquitetura que bloqueia, limita, detecta ou recupera cada passo.</figcaption>
</figure>

### Avaliar cobertura ao longo da cadeia

A pergunta-chave não é "temos um controle para cada técnica?" — isso é impossível —, mas **"em quantos pontos da cadeia conseguimos impedir, detectar ou recuperar?"**. Uma tabela simples basta:

| Passo | Prevenir | Detectar | Recuperar | Situação |
|:---|:---|:---|:---|:---|
| 1 — Acesso pela VPN | MFA resistente a phishing | Login de local ou dispositivo incomum | Revogação de sessões | Hoje: nenhum |
| 2 — Credenciais | Tiering administrativo | Acesso à memória de processos de autenticação | Rotação de credenciais privilegiadas | Hoje: nenhum |
| 4 — Movimento lateral | Segmentação e bloqueio de RDP entre servidores | Conexões administrativas fora do padrão | Isolamento de hosts | Hoje: nenhum |
| 6 — Impacto | Backup imutável fora do domínio | Exclusão em massa de cópias | Restauração ensaiada | Hoje: nenhum |

Uma cadeia em que só um passo tem controle é frágil; a arquitetura busca **interromper o cenário em vários pontos** (defesa em profundidade, Módulo 1 — Aula 02), priorizando os passos **mais cedo** e os **de recuperação**.

### Usos do ATT&CK pelo arquiteto

| Uso | Como |
|:---|:---|
| Tornar cenários concretos | Descrever riscos do register como sequências de técnicas |
| Avaliar arquiteturas | Verificar onde a arquitetura proposta interrompe cada cenário relevante |
| Priorizar detecções | Dar ao SOC as técnicas que a arquitetura não consegue prevenir |
| Comunicar com red team e threat intel | Linguagem comum para planejar exercícios e ler relatórios |

O capítulo 2 de *Building Secure and Reliable Systems* cita catálogos de táticas, técnicas e procedimentos como o ATT&CK como forma de construir defesas contra métodos específicos e recomenda focar em métodos antes de identidades de atacantes, já que atribuição é difícil.

### Limites

- O ATT&CK descreve comportamentos **observados**; técnicas novas aparecem antes de serem catalogadas.
- Não descreve **fraude de negócio** nem abuso de funcionalidade legítima — para isso, abuse cases (Aula 03).
- **Cobertura não é eficácia**: "temos detecção para T1003" não diz se ela funciona no seu ambiente.
- Mapas de calor de cobertura induzem a perseguir quantidade de técnicas, não interrupção de cenários.

## Exemplo empresarial

!!! example "Meridiana — da lista de compras ao cenário"

    A primeira proposta de investimento da Meridiana era uma lista de ferramentas. O arquiteto reescreveu a proposta a partir do cenário RSK-007 mapeado no ATT&CK e mostrou que, na arquitetura atual, **nenhum dos seis passos tinha controle preventivo ou de recuperação**.

    A proposta revisada tinha quatro decisões de arquitetura — MFA resistente a phishing na VPN, tiering administrativo, segmentação entre servidores e backup imutável fora do domínio — e duas detecções prioritárias para o SOC (enumeração e desativação de ferramentas de proteção). Com isso, o cenário passou a ser interrompido em pelo menos quatro pontos, e o risco residual caiu de crítico para médio.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Uso do ATT&CK | Mapa de calor de cobertura | Cenários do register como sequências de técnicas |
| Objetivo | Cobrir o máximo de técnicas | Interromper cenários em vários pontos |
| Controles | Ferramentas por técnica | Decisões de arquitetura + detecções para o que não se previne |
| Versão | Implícita | Registrada nos documentos |

## Aplicabilidade: on-premises, cloud e híbrido

A matriz Enterprise cobre plataformas on-premises e de cloud: técnicas como Valid Accounts e External Remote Services aparecem em ambos, e a tática Defense Impairment inclui, por exemplo, modificações na hierarquia de recursos e na infraestrutura de computação em cloud. Em ambientes híbridos, cenários frequentemente começam on-premises e terminam em cloud (ou o inverso) pela identidade sincronizada — a sequência de técnicas deixa esse caminho explícito e mostra onde a fronteira entre ambientes deveria interromper o ataque.

## Como especificar e implementar

- "Os cenários críticos do risk register são descritos como sequências de táticas e técnicas do ATT&CK, com a versão registrada."
- "Revisões de arquitetura verificam em que pontos a solução interrompe cada cenário crítico."
- "Técnicas que a arquitetura não previne são entregues ao SOC como requisitos de detecção."
- "Cobertura é avaliada por cenário, com testes, e não por contagem de técnicas."

## Trade-offs, limitações e antipadrões

- **Trade-off:** detalhar por subtécnica aumenta a precisão, mas consome tempo; para arquitetura, técnica costuma bastar.
- **Antipadrão — mapa de calor verde:** cobertura declarada sem teste.
- **Antipadrão — ATT&CK como threat model completo:** perde fraude, abuso e dependências.
- **Limitação:** a matriz evolui; versões diferentes têm nomes e IDs diferentes.

## Como validar

- Executar o cenário em exercício de purple team e verificar quais passos foram impedidos ou detectados.
- Conferir se as técnicas entregues ao SOC têm detecção testada.
- Revisar o mapeamento a cada nova versão do ATT&CK.

## Como apresentar e justificar

- **Para a diretoria:** "Este é o caminho que grupos de ransomware usam. Hoje não temos como impedir nenhum dos seis passos. Com quatro decisões, interrompemos o ataque em quatro pontos."
- **Para o SOC:** "Estas duas técnicas a arquitetura não consegue prevenir; precisamos de detecção confiável para elas."

## Checklist de revisão arquitetural

- [ ] Os cenários críticos estão descritos como sequências de técnicas, com a versão do ATT&CK.
- [ ] Cada cenário tem controles de prevenção, detecção e recuperação em mais de um ponto.
- [ ] Técnicas não prevenidas viraram requisitos de detecção.
- [ ] A cobertura foi testada, não apenas declarada.
- [ ] Fraude e abuso de funcionalidade foram tratados por outros métodos.

## Questões de compreensão

**1.** Qual a diferença entre tática e técnica no ATT&CK?

??? success "Resposta comentada"

    A tática é o objetivo do adversário em um momento (o porquê), como Lateral Movement. A técnica é a forma de alcançá-lo (o como), como Remote Services (T1021). Uma técnica pode servir a várias táticas.

**2.** O que mudou na matriz Enterprise atual em relação a materiais que mostram 14 táticas?

??? success "Resposta comentada"

    A matriz Enterprise passou a ter 15 táticas: o ID TA0005 aparece como Stealth, e Defense Impairment (TA0112), criada em abril de 2026, é uma tática própria, voltada a enfraquecer ou desativar controles e monitoração. A v20 mantém essa organização. Documentos devem registrar a versão usada.

**3.** Por que "cobrir o máximo de técnicas" não é um bom objetivo de arquitetura?

??? success "Resposta comentada"

    Porque cobertura declarada não é eficácia, e técnicas não têm o mesmo peso em todos os cenários. O objetivo é interromper os cenários críticos em vários pontos — preferencialmente cedo e com capacidade de recuperação.

## Exercício de tomada de decisão

!!! question "Cenário: exfiltração de dados de pacientes da Lumen"

    Descreva o cenário "exfiltração de prontuários a partir de uma credencial de funcionário roubada" como sequência de pelo menos cinco táticas do ATT&CK v20 e indique, para cada passo, um controle de prevenção ou detecção. Depois escolha os dois controles que você implementaria primeiro e justifique.

??? success "Resolução de referência"

    | Passo | Tática | Controle |
    |:---|:---|:---|
    | Phishing obtém a credencial | Reconnaissance (Phishing for Information, T1598) | MFA resistente a phishing torna a senha insuficiente (prevenção) |
    | Login no portal interno com a credencial roubada | Initial Access (Valid Accounts, T1078) | Detecção de login de dispositivo não gerenciado |
    | Consulta em massa a prontuários | Collection | Limite de consultas por usuário e alerta de volume anômalo (detecção) |
    | Envio a um serviço externo | Exfiltration (Exfiltration Over Web Service, T1567) | Bloqueio de upload para destinos não aprovados; DLP (prevenção e detecção) |
    | Apagar rastros | Stealth (Indicator Removal, T1070) | Logs enviados a repositório imutável fora do alcance do usuário (detecção) |

    **Comparação para escolher os dois primeiros** (notas de 1 a 3; 3 = melhor desempenho):

    | Critério | Peso | A — MFA resistente a phishing | B — Alerta de volume anômalo | C — Bloqueio de upload e DLP | D — Logs imutáveis |
    |:---|:---|:---|:---|:---|:---|
    | Interrompe o cenário cedo na cadeia | 3 | 3 | 2 | 1 | 1 |
    | Cobre também o abuso por funcionário legítimo | 2 | 1 | 3 | 2 | 1 |
    | Eficácia demonstrável por teste | 2 | 3 | 2 | 2 | 3 |
    | Custo e esforço (3 = menor) | 1 | 2 | 2 | 1 | 3 |
    | **Total ponderado** | | **19** | **18** | **12** | **14** |

    **Pesos:** interromper cedo recebe 3 porque cada passo evitado elimina os seguintes; cobrir o abuso interno recebe 2 porque é o caminho mais barato da árvore da Aula 03; a eficácia testável recebe 2; o custo recebe 1.

    **Recomendação — primeiros controles A e B:** (1) **MFA resistente a phishing**, porque interrompe o cenário no primeiro passo; (2) **alerta de volume anômalo de consultas**, porque cobre também o abuso por funcionário legítimo (caminho mais barato da árvore da Aula 03). As demais medidas vêm em seguida.

    **Risco residual:** um funcionário legítimo que consulte poucos prontuários por vez fica abaixo do limiar do alerta; a revisão periódica de acessos com justificativa reduz esse resíduo. **O que mudaria a decisão:** se o MFA resistente a phishing já estivesse implantado, os dois primeiros passariam a ser B e D — o alerta e a preservação dos registros que sustentam a investigação.

## Pontos-chave

- Táticas são o porquê; técnicas, o como; uma técnica pode servir a várias táticas.
- A v20 da matriz Enterprise tem 15 táticas, com Stealth e Defense Impairment; registre a versão.
- Descreva cenários do register como sequências de técnicas e verifique onde a arquitetura os interrompe.
- Busque prevenção, detecção e recuperação em vários pontos, e não cobertura máxima de técnicas.
- O ATT&CK não cobre fraude de negócio nem garante eficácia de controles.

## Referências

### Fundamentação principal

- MITRE. *ATT&CK — Enterprise Tactics*, conteúdo v20.0. <https://attack.mitre.org/tactics/enterprise/> — táticas e técnicas T1133, T1078, T1003, T1087, T1021, T1685, T1490 e T1486 conferidas em 2026-10-23; lista de táticas, T1078, T1133, T1490 e a página da TA0112 (criação em 14/04/2026, 18 técnicas) conferidas de novo em 2026-10-28, assim como T1003 (Credential Access), T1685 (Defense Impairment), T1070 *Indicator Removal* (Stealth), T1213 e T1530 (Collection), T1566 (Initial Access), T1567 (Exfiltration) e T1598 *Phishing for Information* (Reconnaissance).
- MITRE. *ATT&CK Versions*. <https://attack.mitre.org/resources/versions/> — v20.0 em vigor desde 13/10/2026; v19.2 de 28/04/2026 a 12/10/2026.
- H. Adkins et al. *Building Secure and Reliable Systems*. O'Reilly, 2020 — Cap. 2, *Attacker Methods*.
- NIST. *SP 800-30 Rev. 1* — eventos de ameaça e abordagem orientada a ameaça (Sec. 2.3.3).

### Leitura complementar

- MITRE. *CAPEC* — padrões de ataque complementares ao ATT&CK.
- NIST. *CSF 2.0* — funções DETECT, RESPOND e RECOVER, para organizar a cobertura além da prevenção.

### Aplicação prática

- Escolha o cenário mais crítico do seu register e monte a tabela de prevenção, detecção e recuperação por passo. Conte em quantos pontos o cenário é interrompido hoje.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
