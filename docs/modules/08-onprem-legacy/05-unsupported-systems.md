---
id: M08-L05
title: "Aula 05 — Sistemas sem suporte e controles compensatórios"
public_title: "Módulo 8 — Aula 05 — Sistemas sem suporte e controles compensatórios"
description: Como tratar sistemas operacionais, aplicações e equipamentos sem suporte do fabricante — decisão entre substituir, isolar, obter suporte alternativo ou aceitar —, desenho de controles compensatórios verificáveis e governança de exceções com dono e prazo.
domain: infrastructure-foundations
tier: architect
status: published
prerequisites: [M08-L02, M02-L04, M03-L03]
objectives:
  - Explicar o risco de componentes sem suporte e o que o controle SA-22 da SP 800-53 pede.
  - Decidir entre substituir, obter suporte alternativo, isolar e aceitar.
  - Desenhar controles compensatórios que reduzam a exposição de forma verificável.
  - Governar exceções com dono, prazo, evidência e plano de saída.
minutes: 60
sources: [NIST-SP800-53, CISA-STOPRANSOMWARE-GUIDE, NIST-SP800-41-R1, NSA-NETWORK-INFRA-2022, CIS-CONTROLS-V8-1]
further_reading: [AWS-MIGRATION-7RS, NIST-SP800-94, MITRE-ATTACK]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M08
---

# Aula 05 — Sistemas sem suporte e controles compensatórios { #sistemas-sem-suporte-e-controles-compensatorios }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 8 · Nível 2</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">60 min · ID técnico: M08-L05</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Quase toda organização tem algum sistema que não recebe mais correções: o servidor de etiquetas, o equipamento de diagnóstico, o ERP antigo de uma subsidiária. A resposta "desliga" raramente é viável; a resposta "deixa como está" é a origem de muitos incidentes. Entre as duas há uma decisão de arquitetura e de risco: substituir, obter suporte alternativo, isolar com controles compensatórios ou aceitar formalmente — sempre com dono e prazo.

**Pré-requisitos:** [Hardening e baselines](02-hardening-baselines.md), [Princípios, padrões, baselines e exceções](../02-security-architecture/04-principles-standards-baselines-exceptions.md) e [Seleção e tailoring de controles](../03-governance-risk/03-control-selection-tailoring.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar o risco de componentes sem suporte e o que o controle SA-22 da SP 800-53 pede.
- Decidir entre substituir, obter suporte alternativo, isolar e aceitar.
- Desenhar controles compensatórios que reduzam a exposição de forma verificável.
- Governar exceções com dono, prazo, evidência e plano de saída.

## Conceito

### O risco

Sem suporte, vulnerabilidades novas não são corrigidas, e as conhecidas acumulam exploits públicos. O controle **SA-22 (Unsupported System Components)** da SP 800-53 Rev. 5 pede que a organização **substitua** componentes quando o suporte do desenvolvedor, fornecedor ou fabricante deixa de existir, ou que **ofereça fontes alternativas** de suporte. A discussão do controle admite exceções à substituição para sistemas que oferecem capacidades críticas quando não há tecnologia mais nova disponível, ou quando os sistemas são tão isolados que instalar componentes substitutos não é opção; prevê suporte alternativo interno (correções próprias) ou por contrato com terceiros; e registra que o risco pode ser reduzido proibindo a conexão desses componentes a redes públicas ou não controladas, ou isolando-os de outra forma.

### Quatro decisões

| Decisão | Quando | Exige |
|:---|:---|:---|
| **Substituir** | Há alternativa e orçamento | Plano de migração (Aula 07) |
| **Suporte alternativo** | O fornecedor original saiu, mas há terceiros ou suporte estendido pago | Contrato, verificação de que as correções chegam |
| **Isolar com compensatórios** | A substituição é inviável no curto prazo | Controles verificáveis, exceção registrada |
| **Aceitar** | Risco residual baixo, mesmo sem compensações significativas | Decisão do dono do risco, prazo de revisão |

A AWS lista, entre os casos de uso para **aposentar** uma aplicação em uma migração, reduzir os riscos de operar sistemas com componentes sem suporte — lembrando que "retirar" também é uma opção.

## Fundamentos técnicos

### Controles compensatórios que funcionam

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m08-l05-legacy-isolation.mmd"
```

<figcaption>Figura 1 — Sistema sem suporte em segmento isolado, acessível só por serviço intermediário e bastion, com fluxos documentados, IPS, lista de aplicações permitidas e monitoração.</figcaption>
</figure>

| Controle | O que reduz | Como verificar |
|:---|:---|:---|
| **Segmento isolado** com fluxos documentados | Alcance do sistema e a partir dele | Testes de conectividade a partir de fora e de dentro |
| **Sem saída para a internet** | Comando e controle e exfiltração | Tentativa de conexão externa |
| **Acesso de usuários por intermediário** (aplicação publicada, proxy com autenticação forte) | Exposição direta do sistema; credenciais fracas | Tentativa de acesso direto |
| **Administração só via bastion** | Uso indevido de credenciais administrativas | Revisão de sessões |
| **Proteção virtual** (IPS com assinaturas das vulnerabilidades conhecidas) | Exploração de falhas conhecidas | Teste com tráfego de exploração em ambiente controlado |
| **Lista de aplicações permitidas** | Execução de malware | Tentativa de executar binário não autorizado |
| **Monitoração** (logs, integridade de arquivos) | Tempo até a detecção | Simulação de alteração |
| **Backup verificado** | Perda de dados e de configuração | Restauração testada |

O #StopRansomware Guide recomenda lista de aplicações permitidas e/ou EDR em todos os ativos, e antivírus gerenciado centralmente — e, quando o sistema não suporta EDR, a combinação de isolamento e monitoração de rede passa a carregar mais peso.

### O que torna um compensatório legítimo

Um controle compensatório é legítimo quando:

1. Trata **o mesmo risco** que o controle original trataria (Módulo 3 — Aula 03).
2. É **verificável** — há como testar que funciona.
3. Tem **dono** e **evidência** periódica.
4. Está registrado em uma **exceção com prazo**, revista pelo dono do risco.

"Monitoramos manualmente" sem frequência, dono nem evidência não é compensatório; é esperança.

### Equipamentos que não aceitam nada

Equipamentos médicos, de automação industrial e coletores antigos frequentemente não aceitam agente, atualização ou configuração. Para eles, os controles migram para **a rede ao redor**: NAC com perfilamento (Módulo 5 — Aula 06), segmento dedicado, fluxos mínimos, monitoração de rede e, quando possível, gateway de protocolo.

## Exemplo empresarial

!!! example "Meridiana — o servidor de etiquetas"

    O servidor de etiquetas da Meridiana roda um sistema operacional sem suporte há quatro anos, com software de impressão que o fabricante não porta para versões novas. A substituição depende de um projeto de troca das impressoras, previsto para daqui a 10 meses.

    Decisão registrada:

    | Item | Definição |
    |:---|:---|
    | Decisão | Isolar com compensatórios por 10 meses; substituir no projeto de impressoras |
    | Compensatórios | Zona de legados com 4 fluxos (WMS → servidor; servidor → 3 impressoras); sem internet; administração só via bastion; IPS com proteção virtual; lista de aplicações permitidas; backup diário verificado; logs de rede no SIEM |
    | Dono | Diretor de operações |
    | Evidência | Teste trimestral de fluxos e de bloqueio de execução |
    | Residual | Exploração de vulnerabilidade sem assinatura a partir do WMS — médio |
    | Revisão | Trimestral; vencimento da exceção junto com o projeto de impressoras |

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Sistema sem suporte | Na rede comum, "funciona" | Decisão explícita entre substituir, suporte alternativo, isolar ou aceitar |
| Compensatórios | Genéricos, sem teste | Específicos ao risco, verificáveis, com dono |
| Exceção | Implícita e eterna | Registrada, com prazo e revisão |
| Inventário | Desconhecido | Ciclo de vida de suporte monitorado |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias para sistemas sem suporte:

| Controle ou padrão | Objetivo para sistemas sem suporte | Referência |
|:---|:---|:---|
| Componentes sem suporte | Substituir ou dar suporte alternativo; isolar para reduzir o risco | SP 800-53: SA-22 (Unsupported System Components) |
| Isolamento | Isolar componentes por mecanismos de fronteira, negando por padrão | SP 800-53: SC-7(21) (Isolation of System Components) e SC-7(5) (Deny by Default — Allow by Exception) |
| Fluxos mínimos | Controlar os fluxos de e para o segmento isolado | SP 800-53: AC-4 (Information Flow Enforcement) |
| Lista de aplicações permitidas | Executar só software autorizado | SP 800-53: CM-7(5) (Authorized Software — Allow-by-exception) |
| Manutenção remota | Acesso remoto do fabricante controlado e registrado | SP 800-53: MA-4 (Nonlocal Maintenance) |
| Exceções com prazo | Plano de ação com marcos para as deficiências aceitas temporariamente | SP 800-53: CA-5 (Plan of Action and Milestones) |
| Inventário de software | Saber o que existe e se ainda tem suporte | CIS v8.1: Controle 2 (Inventory and Control of Software Assets) |

## Aplicabilidade: on-premises, cloud e híbrido

O problema é mais comum on-premises, mas também existe em cloud: imagens de sistema operacional antigas em máquinas virtuais, runtimes descontinuados em funções, versões de banco gerenciado no fim do suporte estendido. Em cloud, isolar significa redes virtuais e grupos de segurança específicos; o raciocínio é o mesmo. Em ambientes híbridos, a migração de um legado para a nuvem sem modernizar (rehost) pode levar o problema junto — e precisa levar também os compensatórios.

## Como especificar e implementar

- "O inventário registra o fim de suporte de cada componente; componentes a menos de 12 meses do fim têm plano de substituição."
- "Componentes sem suporte são substituídos, recebem suporte alternativo verificável ou são isolados com compensatórios testáveis, mediante exceção registrada."
- "Compensatórios incluem, no mínimo, segmento isolado com fluxos documentados, ausência de saída para a internet e administração via bastion."
- "Exceções têm dono, prazo, evidência periódica e revisão pelo dono do risco."

## Trade-offs, limitações e antipadrões

- **Trade-off:** compensatórios custam operação contínua; quanto mais longo o prazo, mais a substituição se paga.
- **Antipadrão — exceção que se renova sozinha.**
- **Antipadrão — isolamento com "uma regra temporária" que libera tudo.**
- **Limitação:** compensatórios reduzem probabilidade e alcance, mas não eliminam vulnerabilidades — o risco residual precisa ser aceito explicitamente.

## Como validar

- Testar os fluxos do segmento isolado a partir de fora e de dentro.
- Tentar executar um binário não autorizado no sistema.
- Conferir se a exceção está dentro do prazo e se a evidência mais recente existe.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Todo componente sem suporte tem decisão registrada | Inventário com fim de suporte e decisão por componente |
| Só os fluxos documentados funcionam no segmento isolado | Teste de conectividade de fora para dentro e de dentro para fora |
| Execução de binário não autorizado bloqueada | Teste no sistema, com o registro do bloqueio |
| Nenhuma exceção vencida e evidência periódica em dia | Lista de exceções com data da última evidência |

## Como apresentar e justificar

- **Para a diretoria:** "Não dá para trocar o servidor de etiquetas antes das impressoras. Até lá, ele fica em uma ilha com quatro conexões, sem internet, e o risco é revisto a cada trimestre."
- **Para a operação:** "Toda exceção tem data de vencimento. Se o projeto atrasar, a decisão volta para o dono do risco."

## Checklist de revisão arquitetural

- [ ] Fim de suporte monitorado no inventário.
- [ ] Decisão explícita para cada componente sem suporte.
- [ ] Compensatórios específicos ao risco e verificáveis.
- [ ] Exceção com dono, prazo e evidência.
- [ ] Plano de saída definido.

## Questões de compreensão

**1.** O que o controle SA-22 pede?

??? success "Resposta comentada"

    Substituir componentes quando o suporte do fabricante deixa de existir ou oferecer fontes alternativas de suporte; a discussão admite isolamento como forma de reduzir o risco quando a substituição não é possível.

**2.** O que diferencia um compensatório legítimo de um de fachada?

??? success "Resposta comentada"

    O legítimo trata o mesmo risco, é verificável, tem dono e evidência periódica e está registrado em exceção com prazo. O de fachada é genérico, sem teste nem responsável.

**3.** Como proteger um equipamento que não aceita agentes nem atualizações?

??? success "Resposta comentada"

    Levando os controles para a rede ao redor: NAC com perfilamento, segmento dedicado com fluxos mínimos, monitoração de rede e, quando possível, gateways de protocolo.

## Exercício de tomada de decisão

!!! question "Cenário: equipamento de imagem da Lumen"

    Um equipamento de ressonância de uma clínica da Lumen roda um sistema operacional embarcado sem suporte. O fabricante só certifica atualizações no próximo modelo, a ser adquirido em três anos. O equipamento envia imagens a um servidor de imagens e recebe listas de pacientes do sistema de agendamento. As opções são:

    - **A** — antecipar a substituição pelo novo modelo;
    - **B** — isolar com compensatórios por três anos, com substituição no ciclo de compra;
    - **C** — contratar suporte alternativo de terceiros que aplique correções ao sistema embarcado.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e proponha a decisão e os compensatórios.

**Objetivos avaliados:** Decidir entre substituir, obter suporte alternativo, isolar e aceitar; desenhar controles compensatórios que reduzam a exposição de forma verificável.

**Entrega esperada:** Matriz ponderada, a decisão com prazo e os controles compensatórios verificáveis.

**Critérios de avaliação:**

- Os compensatórios reduzem a exposição de forma verificável (fluxos permitidos, monitoração de fluxo novo).
- A exceção tem dono, prazo, revisão e plano de saída, como pede o SA-22.
- A resposta pesa segurança clínica e certificação do fabricante, não só segurança da informação.

??? success "Resolução de referência"

    | Critério | Peso | A — Antecipar a substituição | B — Isolar com compensatórios | C — Suporte alternativo de terceiros |
    |:---|:---|:---|:---|:---|
    | Redução do risco de exploração | 3 | 3 | 2 | 2 |
    | Segurança clínica e certificação do equipamento | 2 | 2 | 3 | 1 |
    | Custo | 2 | 1 | 2 | 2 |
    | Prazo até o efeito | 1 | 1 | 3 | 2 |
    | **Total ponderado** | | **16** | **19** | **14** |

    - **Pesos:** a exploração do equipamento é o risco tratado (peso 3). Segurança clínica e custo pesam 2: alterar software de equipamento médico sem certificação do fabricante pode afetar o funcionamento e a regularidade do equipamento, e a compra antecipada consome orçamento de outro ciclo. O prazo pesa 1.
    - **Recomendação: B.** A reduz mais o risco, mas custa a antecipação de um investimento de capital e leva meses de aquisição; C aplica correções que o fabricante não certifica em um equipamento médico.

    - **Decisão:** isolar com compensatórios por três anos, com revisão semestral; substituição planejada no ciclo de compra.
    - **Compensatórios:** segmento de equipamentos médicos com NAC por perfilamento (Módulo 5 — Aula 06); fluxos apenas equipamento ↔ servidor de imagens e agendamento → equipamento, nos protocolos usados; sem internet; acesso remoto do fabricante apenas via acesso privilegiado com aprovação e gravação (Módulo 5 — Aula 04); monitoração de rede com alerta para qualquer fluxo novo; IPS com proteção virtual quando houver assinaturas para o sistema.
    - **Contratual:** exigir do fabricante notificação de vulnerabilidades e suporte de segurança no contrato do próximo modelo.
    - **Trade-off aceito e risco residual:** o equipamento continua vulnerável por três anos; o residual é a exploração a partir do servidor de imagens ou do sistema de agendamento, os dois únicos com fluxo até ele — aceito pela diretoria clínica, com dono e revisão semestral.
    - **O que mudaria a decisão:** vulnerabilidade com exploração ativa contra esse modelo, ou incidente na rede de equipamentos médicos, elevaria A; se o fabricante passar a oferecer correções certificadas para o modelo atual, a opção vira suporte do próprio fabricante e deixa de ser exceção.

    **Erros comuns:**

    - Aplicar correções não certificadas em equipamento médico.
    - Isolar sem definir os fluxos mínimos necessários à operação.
    - Aceitar o risco sem dono e sem prazo.

## Pontos-chave

- Componentes sem suporte acumulam vulnerabilidades; o SA-22 pede substituição ou suporte alternativo.
- Decida entre substituir, suporte alternativo, isolar ou aceitar — explicitamente.
- Compensatórios legítimos tratam o mesmo risco, são verificáveis e têm dono.
- Equipamentos fechados são protegidos pela rede ao redor.
- Exceções vencem; o plano de saída faz parte da decisão.

## Referências

### Fundamentação principal

- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — SA-22 (enunciado e discussão), SC-7(5), SC-7(21), AC-4, CM-7(5), MA-4 e CA-5, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controle 2 — gratuito.
- CISA, FBI, NSA, MS-ISAC. *#StopRansomware Guide*. 2023. *(Lido.)*
- NIST. *SP 800-41 Rev. 1* — política de firewall. *(Lido.)*
- NSA. *Network Infrastructure Security Guidance* — agrupamento e isolamento de sistemas. *(Lido.)*

### Leitura complementar

- AWS. *Migration strategies (7 Rs)* — retirar como opção.
- NIST. *SP 800-94* — IDPS.
- MITRE. *ATT&CK v20*.

### Aplicação prática

- Liste os componentes sem suporte do seu ambiente e, para o mais crítico, escreva a exceção completa: decisão, compensatórios, dono, evidência, residual e prazo.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
