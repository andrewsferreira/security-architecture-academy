---
title: "Gabarito — Avaliação do Módulo 02"
description: Gabarito comentado da avaliação do Módulo 02, com justificativa das alternativas incorretas, respostas de referência das tarefas e rubrica de correção.
status: published
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# Gabarito — Avaliação do Módulo 02

!!! warning "Responda primeiro"

    Este é o gabarito da [avaliação do Módulo 02](../m02-security-architecture.md). Faça a avaliação antes de ler.

## Parte 1 — Respostas comentadas

| Questão | Resposta | Aula |
|:---|:---|:---|
| 1 | **b** | M02-L01 |
| 2 | **d** | M02-L02 |
| 3 | **a** | M02-L03 |
| 4 | **c** | M02-L04 |
| 5 | **b** | M02-L04 |
| 6 | **d** | M02-L05 |
| 7 | **a** | M02-L06 |
| 8 | **c** | M02-L07 |
| 9 | **d** | M02-L03 |
| 10 | **c** | M02-L08 |

**1 — (b).** Com um único arquiteto, a aprovação universal concentra decisões no fim do ciclo, gera fila e incentiva o contorno do processo. (a) ignora o efeito de gargalo; (c) é o oposto — o envolvimento tardio *aumenta* o custo de correção; (d) a aprovação universal não substitui padrões, e padrões são justamente o que permite o autoatendimento.

**2 — (d).** A pergunta "como autenticamos clientes?" vai se repetir em outras soluções; por isso a decisão é corporativa. (a) decidir localmente cria precedente sem análise de alcance; (b) o fornecedor não responde pelo risco da organização; (c) a auditoria avalia, não decide arquitetura.

**3 — (a).** Define mecanismos e protocolos (OAuth 2.0, mTLS) sem produtos nem topologia. (b) é conceitual; (c) é física; (d) é objetivo de negócio.

**4 — (c).** Desvios conscientes são exceções com prazo, compensatórios ligados ao mesmo risco e aprovação de quem responde por ele. (a) é desvio silencioso; (b) ignora o impacto no negócio; (d) rebaixa o padrão para todos por causa de um caso.

**5 — (b).** Taxa alta de exceções é o sinal clássico de complexidade desnecessária: o mesmo rigor para ativos de valor diferente. (a) culpa as equipes sem analisar o padrão; (c) trata o sintoma; (d) remove o mecanismo que tornou o problema visível.

**6 — (d).** Referências de provedores pressupõem escala e capacidade operacional; adotar tudo pode gerar alertas sem dono e custo sem ganho proporcional. (a) ignora o custo de operar; (b) generalização falsa; (c) não há tal restrição.

**7 — (a).** O CSF 2.0 é uma taxonomia de resultados com perfis atual e alvo, adequada para comunicar postura e prioridades. (b) é um catálogo de controles, não uma linguagem de governança; (c) é um mapa de competências profissionais; (d) é configuração técnica.

**8 — (c).** Propriedade mensurável do comportamento do sistema. (a) é requisito funcional; (b) é restrição; (d) não é requisito — é uma escolha de produto.

**9 — (d).** Em ambientes híbridos, o risco está nas diferenças entre realizações físicas de um mesmo componente lógico. (a), (b) e (c) não se relacionam com a garantia de segurança.

**10 — (c).** ADRs aceitos são imutáveis no conteúdo; um novo ADR substitui o anterior. (a) perde o histórico; (b) quebra a numeração e o histórico; (d) a decisão deixa de ser rastreável.

## Parte 2 — Respostas de referência

### Tarefa 1 — Análise de diagrama

| # | Problema | Risco de negócio | Recomendação lógica |
|:---|:---|:---|:---|
| 1 | Gateway → serviço de pedidos por HTTP **sem autenticação** e sem criptografia, cruzando da DMZ para a zona de aplicações | Quem comprometer o gateway ou qualquer componente da DMZ consegue criar, alterar ou consultar pedidos sem identificação | Autenticação mútua entre gateway e serviço (mTLS) e verificação do token do usuário também no serviço |
| 2 | Painel administrativo **publicado diretamente na internet**, com usuário e senha | Um ataque de força bruta ou phishing contra o suporte dá acesso administrativo aos dados pessoais de todos os clientes | Acesso administrativo apenas por canal controlado (acesso por aplicação ou bastion), com MFA, e painel fora da superfície pública |
| 3 | Serviço de pedidos e painel usam **o mesmo tipo de acesso amplo ao banco** | Um comprometimento de qualquer um dos dois expõe o banco inteiro | Identidades de banco separadas, com privilégios mínimos por função |
| 4 | Logs do gateway **apenas locais** | Incidentes não seriam detectados nem investigados; a evidência pode ser apagada por quem comprometer o gateway | Envio de eventos do gateway, do serviço e do painel ao monitoramento central, com retenção definida |

Outros achados aceitáveis: ausência de autorização em nível de objeto no serviço de pedidos (o token é validado só no gateway); dados pessoais sem indicação de classificação e retenção.

### Tarefa 2 — Níveis e hierarquia

| Item | Nível | Tipo |
|:---|:---|:---|
| 1 | Conceitual | Princípio (negar por padrão) |
| 2 | Físico | Controle |
| 3 | Físico (configuração de uma tecnologia) | Baseline |
| 4 | — | Exceção |
| 5 | — | Diretriz |

### Tarefa 3 — Requisitos verificáveis (exemplos)

| Original | Reescrita possível | Categoria | Origem |
|:---|:---|:---|:---|
| "Seguro contra ataques" | "O serviço de pedidos verifica, a cada requisição, se o pedido consultado pertence ao cliente autenticado e rejeita a requisição caso contrário." | Funcional | Ameaça de acesso a pedidos de terceiros; atributo *Confidencial* |
| "Logs adequados" | "O gateway, o serviço de pedidos e o painel registram autenticações, falhas de autorização e operações administrativas, com usuário, origem e horário, e enviam os eventos ao SIEM em até 5 minutos, com retenção de 12 meses." | Qualidade | Atributo *Rastreável*; necessidade de investigação |
| "Firewall da marca Y" | "O banco de pedidos aceita conexões apenas dos serviços autorizados da zona de aplicações, na porta do banco, com autenticação por identidade de serviço." | Restrição | Princípio de negar por padrão; ameaça de acesso direto ao banco |

Valores como 5 minutos e 12 meses são exemplos; o essencial é que sejam mensuráveis e justificados.

### Tarefa 4 — Decisão sob restrição

Para o cálculo, o item "MFA, acesso condicional e ZTNA" do orçamento original foi separado em **MFA e acesso condicional (R$ 60 mil)** e **ZTNA (R$ 80 mil)** — valores ilustrativos.

| Critério | Peso | MFA | Backup isolado | EDR | MDR | Firewall interno | ZTNA |
|:---|:---|:---|:---|:---|:---|:---|:---|
| Redução do risco crítico (ransomware) | 3 | 3 | 3 | 3 | 2 | 3 | 2 |
| Exigência da seguradora | 3 | 3 | 3 | 3 | 2 | 1 | 1 |
| Custo (3 = menor) | 1 | 3 | 2 | 2 | 1 | 2 | 2 |
| Esforço da equipe (3 = menor) | 2 | 3 | 2 | 2 | 3 | 1 | 2 |
| **Total ponderado** | | **27** | **24** | **24** | **19** | **16** | **15** |

**Seleção para o ano 1 (R$ 700 mil):** MFA e acesso condicional (60) + backup isolado e imutável (150) + EDR (160) + MDR (280) = **R$ 650 mil**, com R$ 50 mil para serviços de implantação.

**Ano 2:** firewall interno e segmentação, ZTNA, broker de acesso privilegiado de fornecedores e a contratação adicional.

**Risco residual:** movimentação lateral na rede plana e acesso remoto ainda em nível de rede (com MFA). **Dono proposto:** diretoria de operações, com revisão semestral. Mitigação parcial: EDR com MDR detecta e contém movimentação lateral, e o backup isolado garante a recuperação.

**Parágrafo para a diretoria (exemplo, 96 palavras):**

> Com R$ 700 mil, priorizamos o que impede um ransomware de parar os CDs e o que a seguradora exige: autenticação multifator em todo acesso remoto, proteção e monitoramento 24 horas de estações e servidores, e um backup que um invasor não consegue apagar. Adiamos para o ano 2 a divisão da rede interna e a troca da VPN. O risco que permanece é um invasor circular pela rede antes de ser detectado; o monitoramento contínuo reduz esse risco, e o backup isolado garante a retomada. Pedimos que a diretoria de operações aceite formalmente esse risco até a próxima revisão.

## Rubrica da Parte 2

| Tarefa | Excelente | Adequado | Insuficiente |
|:---|:---|:---|:---|
| **1 (12 pt)** | 4 problemas corretos, com risco de negócio e recomendação lógica (12) | 3 problemas corretos, ou recomendações em nível de produto (8) | 2 ou menos, ou sem relação com fronteiras e fluxos (3) |
| **2 (10 pt)** | 5 itens corretos nos dois eixos (10) | 4 itens corretos (7) | 3 ou menos (3) |
| **3 (12 pt)** | 3 requisitos específicos, verificáveis, rastreáveis e neutros (12) | 2 requisitos corretos, ou um sem origem (8) | Reescritas ainda vagas ou com produto (3) |
| **4 (16 pt)** | Matriz com pesos coerentes ao cenário, seleção dentro do orçamento, risco residual com dono e parágrafo claro para não técnicos (16) | Seleção defensável, mas sem pesos explícitos ou sem dono do risco (11) | Seleção acima do orçamento, ignora a seguradora ou não declara risco residual (5) |

Seleções diferentes da referência na Tarefa 4 são aceitas quando a matriz justifica a escolha e o orçamento é respeitado — por exemplo, trocar parte do MDR por um SIEM com cobertura em horário comercial, desde que o risco de detecção fora do expediente seja declarado.

## Interpretação

| Resultado | O que fazer |
|:---|:---|
| ≥ 70 e nenhuma tarefa *Insuficiente* | Siga para o Caso A ou para o Módulo 03. |
| ≥ 70 com alguma tarefa *Insuficiente* | Revise a aula correspondente e refaça a tarefa. |
| < 70 | Revise as aulas indicadas na Parte 1 e refaça o exercício de decisão de cada uma. |
