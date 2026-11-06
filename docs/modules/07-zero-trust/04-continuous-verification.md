---
id: M07-L04
title: "Aula 04 — Verificação contínua, postura de dispositivo e acesso adaptativo"
public_title: "Módulo 7 — Aula 04 — Verificação contínua, postura de dispositivo e acesso adaptativo"
description: Como transformar sinais de identidade, autenticação, dispositivo, localização e comportamento em decisões de acesso que mudam ao longo da sessão — algoritmos de confiança por critérios e por pontuação, postura de dispositivo, autenticação adicional e revogação.
domain: zero-trust
tier: professional
status: published
prerequisites: [M07-L02, M06-L01]
objectives:
  - Diferenciar algoritmos de confiança por critérios e por pontuação, e singulares e contextuais.
  - Selecionar sinais de decisão e avaliar sua confiabilidade.
  - Desenhar respostas graduais — permitir, restringir, exigir autenticação adicional, negar, revogar.
  - Especificar reavaliação durante a sessão e seus limites técnicos.
minutes: 75
sources: [NIST-SP800-207, NIST-SP800-63-4, NIST-SP800-215, CISA-ZTMM-2, NIST-SP800-53]
further_reading: [RFC-9700, MS-ENTRA-HYBRID-AUTHN]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M07
---

# Aula 04 — Verificação contínua, postura de dispositivo e acesso adaptativo { #verificacao-continua-postura-de-dispositivo-e-acesso-adaptativo }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 7 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M07-L04</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Autenticar uma vez de manhã e manter acesso o dia inteiro, mesmo depois de o dispositivo ter sido infectado ou de a sessão aparecer em outro país, contradiz o sexto princípio da SP 800-207: autenticação e autorização dinâmicas, aplicadas antes de cada acesso. Esta aula trata do **algoritmo de confiança** que transforma sinais em decisões, da **postura de dispositivo** como sinal central e das respostas graduais que tornam o acesso **adaptativo** sem tornar a vida do usuário impossível.

**Pré-requisitos:** [Componentes lógicos](02-logical-components.md) e [Disciplinas de identidade](../06-iam/01-identity-disciplines.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Diferenciar algoritmos de confiança por critérios e por pontuação, e singulares e contextuais.
- Selecionar sinais de decisão e avaliar sua confiabilidade.
- Desenhar respostas graduais — permitir, restringir, exigir autenticação adicional, negar, revogar.
- Especificar reavaliação durante a sessão e seus limites técnicos.

## Conceito

### O algoritmo de confiança

A SP 800-207 descreve o algoritmo de confiança como o processo pelo qual o PE decide, ponderando entradas como o pedido de acesso, a base de dados de sujeitos, a base de ativos e seu estado observável, os requisitos do recurso e a inteligência de ameaças (§3.3, pp. 17–19). Duas dimensões o classificam (§3.3.1, pp. 19–20):

| Dimensão | Opções | Característica |
|:---|:---|:---|
| **Forma de decisão** | **Por critérios** | Todas as condições precisam ser atendidas |
| | **Por pontuação** | Um nível de confiança é calculado a partir de cada fonte de dados e de pesos configurados pela organização |
| **Contexto** | **Singular** | Cada pedido é avaliado isoladamente |
| | **Contextual** | O comportamento recente do sujeito é considerado |

O documento afirma que, idealmente, o algoritmo deveria ser **contextual**, reconhecendo que isso nem sempre é possível com a infraestrutura disponível (§3.3.1, p. 20) — e registra que um algoritmo contextual tem mais chance de detectar e responder rapidamente a credenciais roubadas e ameaça interna (§5.3, p. 29).

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m07-l04-continuous.mmd"
```

<figcaption>Figura 1 — Sinais alimentam a decisão, que pode permitir, restringir, exigir autenticação adicional ou negar; novos sinais durante a sessão disparam reavaliação.</figcaption>
</figure>

### Sinais e sua confiabilidade

| Sinal | Exemplo | Confiabilidade | Observação |
|:---|:---|:---|:---|
| **Identidade e grupos** | Cargo, departamento | Alta, se a fonte for autoritativa | Módulo 6 — Aula 08 |
| **Método de autenticação** | Resistente a phishing ou não | Alta | SP 800-63B-4 (Módulo 6 — Aula 01) |
| **Postura do dispositivo** | Gerenciado, EDR ativo, disco cifrado, sistema atualizado | Média a alta, se atestada pelo MDM/EDR | Postura autodeclarada pelo dispositivo é fraca |
| **Localização / rede** | País, endereço IP | Baixa a média | Fácil de mascarar; útil como sinal complementar |
| **Risco da sessão** | Viagem impossível, credencial vazada | Média | Depende do provedor |
| **Comportamento** | Volume de acesso a dados acima do usual | Média | Exige linha de base |

O modelo de maturidade da CISA, no pilar de identidade, descreve a evolução da autenticação de senha ou MFA com acesso estático (estágio *Traditional*) até **revalidação contínua com MFA resistente a phishing** (*Optimal*), segundo reprodução consultada do documento.

## Fundamentos técnicos

### Respostas graduais

| Resposta | Quando | Exemplo |
|:---|:---|:---|
| **Permitir** | Todos os critérios atendidos | Dispositivo conforme, autenticação forte, contexto usual |
| **Permitir com restrições** | Confiança parcial | Somente leitura, sem download, a partir de dispositivo não gerenciado |
| **Exigir autenticação adicional** (*step-up*) | Ação sensível ou risco moderado | Aprovar pagamento exige autenticação resistente a phishing recente |
| **Negar** | Critério obrigatório não atendido | Dispositivo sem EDR acessando dados de saúde |
| **Revogar** | Novo sinal de risco durante a sessão | Credencial detectada em vazamento |

### Reavaliação durante a sessão

Reavaliar é mais difícil do que decidir no início, porque tokens e sessões já foram emitidos:

- **Tokens de curta duração** forçam reavaliação periódica (minutos a uma hora).
- **Revogação de sessões e de refresh tokens** no IdP precisa propagar para aplicações — nem todas suportam.
- **Tokens restritos ao remetente** reduzem o valor de tokens roubados (RFC 9700, Módulo 6 — Aula 04).
- **Sinais de risco compartilhados** entre IdP, EDR e aplicações permitem que um evento em um sistema dispare ação em outro.

A arquitetura deve ser honesta sobre o **intervalo** entre um sinal de risco e o efeito no acesso, e reduzi-lo onde o risco justifica.

### Postura de dispositivo na prática

| Elemento | Como obter | Cuidado |
|:---|:---|:---|
| Dispositivo gerenciado | Registro no MDM, certificado de dispositivo | Distinguir dispositivo corporativo de BYOD registrado |
| EDR ativo e saudável | Integração do EDR com o IdP ou ZTNA | Falsos negativos quando o agente é desativado |
| Sistema atualizado | Relatório do MDM | Janela de tolerância para atualizações recém-publicadas |
| Disco cifrado | Relatório do MDM | — |

A SP 800-215 inclui a autenticação de dispositivos por certificado e verificações de saúde — versão do sistema, correções, software de segurança, geolocalização — entre as configurações básicas de segurança (Sec. 4.4, p. 16).

## Exemplo empresarial

!!! example "Aurora Pagamentos — políticas por sensibilidade"

    A Aurora definiu três níveis de política no IdP e no ZTNA:

    | Nível | Recursos | Exigências | Reavaliação |
    |:---|:---|:---|:---|
    | Padrão | E-mail, intranet | MFA; dispositivo gerenciado ou acesso restrito | Token de 1 hora |
    | Sensível | CRM, BI com dados de lojistas | MFA resistente a phishing; dispositivo conforme | Token de 1 hora + revogação por risco |
    | Crítico | Antecipação de recebíveis, consoles | Resistente a phishing nos últimos 15 min para ações de alto valor; dispositivo conforme com EDR | Revogação imediata por risco; *step-up* por operação |

    Na primeira semana, 7% dos acessos ao nível sensível foram bloqueados por dispositivos sem EDR saudável — a maioria por agentes desatualizados, um problema operacional que antes passava despercebido.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Momento da decisão | Login | Login, cada sessão e eventos de risco |
| Sinais | Senha | Identidade, autenticação, postura, contexto, comportamento |
| Resposta | Permitir ou negar | Gradual, com restrições e *step-up* |
| Sessões | Longas | Tokens curtos, revogação propagada |
| Política | Uma para tudo | Por sensibilidade do recurso |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0), referências voluntárias para a verificação contínua:

| Controle ou padrão | Objetivo na verificação contínua | Referência |
|:---|:---|:---|
| Autenticação adaptativa | Exigir mecanismos adicionais de autenticação em situações definidas | SP 800-53: IA-10 (Adaptive Authentication) |
| Reautenticação | Exigir reautenticação nas condições definidas (*step-up*, ação sensível) | SP 800-53: IA-11 (Re-authentication) |
| Encerramento de sessão | Encerrar sessões automaticamente nas condições definidas | SP 800-53: AC-12 (Session Termination) |
| Uso atípico | Monitorar contas para uso atípico e reportá-lo | SP 800-53: AC-2(12) (Account Monitoring for Atypical Usage) |
| Dispositivos móveis | Requisitos de configuração e conexão para dispositivos, inclusive fora das áreas controladas | SP 800-53: AC-19 (Access Control for Mobile Devices) |
| Identificação de dispositivos | Identificar e autenticar o dispositivo antes da conexão | SP 800-53: IA-3 (Device Identification and Authentication) |
| Algoritmo de confiança | Por critérios ou por pontuação, singular ou contextual | NIST SP 800-207, §3.3 |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud e SaaS, o acesso condicional do IdP é o principal mecanismo de acesso adaptativo. Aplicações on-premises legadas raramente reavaliam sessões; ZTNA e gateways podem impor reavaliação na conexão. Em ambientes híbridos, a postura do dispositivo deve ser a mesma para acessos a recursos dos dois lados — duas fontes de postura com resultados diferentes geram incoerência e contornos.

## Como especificar e implementar

- "Recursos são classificados por sensibilidade, e cada nível tem exigências de autenticação, postura e reavaliação."
- "Sinais de postura vêm de fontes atestadas (MDM/EDR), não de autodeclaração."
- "Ações de alto impacto exigem autenticação recente resistente a phishing."
- "Eventos de risco revogam sessões e tokens, com propagação às aplicações suportadas; o intervalo máximo está documentado."
- "Decisões e sinais são registrados para investigação e ajuste."

## Trade-offs, limitações e antipadrões

- **Trade-off:** segurança versus atrito — *step-up* em excesso ensina os usuários a aprovar sem ler.
- **Antipadrão — bloqueio por país como controle principal:** fácil de contornar com VPN comercial.
- **Antipadrão — pontuação de risco opaca:** ninguém sabe por que um acesso foi negado.
- **Limitação:** reavaliação contínua depende de suporte das aplicações; muitas só verificam no login.

## Como validar

- Desativar o EDR em um dispositivo de teste e medir o tempo até o bloqueio.
- Simular um evento de risco e verificar a revogação nas aplicações críticas.
- Executar uma ação de alto valor sem autenticação recente e verificar o *step-up*.
- Revisar uma amostra de negações para verificar se são explicáveis.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Dispositivo com EDR desativado perde acesso ao nível sensível dentro do intervalo documentado | Teste cronometrado com dispositivo de referência |
| Evento de risco revoga sessões nas aplicações críticas que suportam revogação | Teste com o evento simulado e a lista de aplicações sem suporte |
| Ação de alto valor sem autenticação recente exige *step-up* | Teste da operação com sessão antiga |
| Toda negação da amostra é explicável pela regra e pelos sinais | Revisão de amostra de negações com a regra aplicada |

## Como apresentar e justificar

- **Para a diretoria:** "Se um computador for infectado depois do login, o acesso aos sistemas críticos cai em minutos — hoje ele continuaria até o fim do dia."
- **Para usuários:** "Para o dia a dia, nada muda. Para aprovar operações de alto valor, a chave de segurança é pedida de novo."

## Checklist de revisão arquitetural

- [ ] Recursos classificados por sensibilidade, com política por nível.
- [ ] Sinais de postura atestados.
- [ ] Respostas graduais definidas, inclusive *step-up*.
- [ ] Tokens curtos e revogação propagada onde possível.
- [ ] Intervalo entre sinal de risco e efeito documentado.
- [ ] Decisões registradas e explicáveis.

## Questões de compreensão

**1.** Qual a diferença entre algoritmo de confiança por critérios e por pontuação?

??? success "Resposta comentada"

    Por critérios, todas as condições precisam ser atendidas para o acesso ser concedido. Por pontuação, os sinais compõem um nível de confiança ponderado, comparado a um limiar.

**2.** Por que a localização de rede é um sinal fraco?

??? success "Resposta comentada"

    Porque é fácil de mascarar (VPNs comerciais, proxies) e não diz nada sobre a identidade ou o estado do dispositivo. É útil como sinal complementar, não como critério principal.

**3.** O que limita a reavaliação contínua na prática?

??? success "Resposta comentada"

    Tokens e sessões já emitidos continuam válidos até expirar ou serem revogados, e muitas aplicações não recebem nem aplicam revogações. Tokens curtos, revogação propagada e tokens restritos ao remetente reduzem esse intervalo.

## Exercício de tomada de decisão

!!! question "Cenário: política para o sistema de prontuários da Lumen"

    Defina a política de acesso adaptativo para o sistema de prontuários da Lumen, considerando médicos nas clínicas (dispositivos gerenciados), médicos em teleconsulta de casa (dispositivos gerenciados fora da rede) e acesso emergencial a partir de dispositivo pessoal. Antes, escolha a forma do algoritmo de confiança:

    - **A** — por critérios e singular: regras explícitas por situação, cada pedido avaliado isoladamente;
    - **B** — por pontuação e contextual: a pontuação de risco do provedor, comparada a um limiar;
    - **C** — critérios obrigatórios explícitos, com sinais contextuais (volume, comportamento) que disparam reautenticação, alerta ou revogação por regras também explícitas.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e escreva a política.

**Objetivos avaliados:** Diferenciar algoritmos de confiança por critérios e por pontuação, e singulares e contextuais; desenhar respostas graduais — permitir, restringir, exigir autenticação adicional, negar, revogar.

**Entrega esperada:** Matriz ponderada, a forma do algoritmo de confiança e a política por situação (clínica, teleconsulta, emergência).

**Critérios de avaliação:**

- Cada decisão continua explicável: a regra e os sinais que a determinaram ficam registrados.
- A política tem respostas graduais (restringir, reautenticar, alertar, revogar), não só permitir ou negar.
- O acesso por dispositivo pessoal tem restrições e alerta proporcionais.

??? success "Resolução de referência"

    | Critério | Peso | A — Critérios, singular | B — Pontuação, contextual | C — Critérios com gatilhos contextuais |
    |:---|:---|:---|:---|:---|
    | Explicabilidade das negações e dos acessos | 3 | 3 | 1 | 3 |
    | Detecção de abuso com credencial válida | 2 | 1 | 3 | 3 |
    | Esforço de implantação e ajuste | 2 | 3 | 2 | 2 |
    | Atrito para os médicos | 1 | 2 | 3 | 2 |
    | **Total ponderado** | | **19** | **16** | **21** |

    - **Pesos:** acessos a dados de saúde precisam ser explicáveis ao titular e à auditoria (peso 3). A detecção de abuso pesa 2, porque o vínculo médico–paciente já limita o alcance; o esforço também pesa 2. O atrito pesa 1, porque as exigências fortes recaem só nas situações de maior risco.
    - **Recomendação: C.** Mantém cada decisão explicável e acrescenta o que a SP 800-207 considera ideal — considerar o histórico recente do sujeito — por regras conhecidas, não por uma pontuação opaca. A política resultante:

    | Situação | Exigências | Resposta |
    |:---|:---|:---|
    | Clínica, dispositivo gerenciado e conforme | Autenticação resistente a phishing; ABAC por vínculo (Módulo 6 — Aula 02) | Permitir; token de 1 hora |
    | Teleconsulta, dispositivo gerenciado fora da rede | Mesmas exigências + postura atual do EDR | Permitir; revogação imediata se a postura mudar |
    | Dispositivo pessoal, emergência | Autenticação resistente a phishing + justificativa | Permitir com restrições: somente leitura, sem download, sessão de 30 minutos, alerta à coordenação |
    | Qualquer situação, volume de consultas anômalo | — | Exigir reautenticação e alertar o SOC; revogar se confirmado |

    - **Registro:** toda decisão com sinais e resultado, para auditoria e para a avaliação de incidentes com dados de saúde (Módulo 3 — Aula 04).
    - **Trade-off aceito e risco residual:** regras contextuais explícitas detectam só os padrões previstos (volume, horário); abuso discreto dentro do vínculo continua possível e depende da revisão periódica. O acesso emergencial por dispositivo pessoal é aceito com restrições e alerta.
    - **O que mudaria a decisão:** se o provedor oferecer pontuação de risco com explicação dos sinais por decisão, B perde a desvantagem de explicabilidade; se a Lumen não tiver equipe para manter as regras contextuais, A é o ponto de partida, com a revisão de volume feita por relatório.

    **Erros comuns:**

    - Adotar uma pontuação de risco opaca para decisões que precisam ser explicadas a titulares e auditores.
    - Tratar a verificação contínua como reautenticação constante, aumentando o atrito sem ganho.
    - Usar sinais sem avaliar sua confiabilidade (por exemplo, localização por IP).

## Pontos-chave

- O algoritmo de confiança pode ser por critérios ou por pontuação, singular ou contextual; contextual é o ideal onde viável.
- Postura de dispositivo atestada é um dos sinais mais valiosos; localização é complementar.
- Respostas graduais equilibram segurança e atrito.
- Reavaliar durante a sessão exige tokens curtos, revogação propagada e tokens restritos.
- Seja explícito sobre o intervalo entre sinal de risco e efeito.

## Referências

### Fundamentação principal

- NIST. *SP 800-207* — §3.3 (pp. 17–20) e §5.3 (p. 29). *(Lido; algoritmo de confiança reconferido no PDF em 2026-10-29.)*
- NIST. *SP 800-63B-4* — autenticação resistente a phishing. *(Lido.)*
- NIST. *SP 800-215* — Sec. 4.4 (p. 16). *(Lido.)*
- CISA. *Zero Trust Maturity Model 2.0* — pilar de identidade (reprodução consultada; o PDF oficial não abriu na ferramenta).
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-2(12), AC-12, AC-19, IA-3, IA-10 e IA-11, conferidos no catálogo OSCAL oficial — gratuito.

### Leitura complementar

- IETF. *RFC 9700* — tokens restritos ao remetente e rotação.
- Microsoft. *Authentication for Microsoft Entra hybrid identity* — detecção de credenciais vazadas com PHS.

### Aplicação prática

- Classifique cinco aplicações da sua organização em três níveis de sensibilidade e escreva a política de cada nível: exigência de autenticação, postura, duração do token e respostas a risco.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
