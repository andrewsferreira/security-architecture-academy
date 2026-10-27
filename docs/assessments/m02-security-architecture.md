---
id: AS-M02
title: "Avaliação do Módulo 02 — Introdução à Arquitetura de Segurança"
description: Avaliação baseada em competências do Módulo 02 — questões situacionais, análise de diagrama, classificação de níveis, reescrita de requisitos e defesa de decisão sob restrição de orçamento.
status: published
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
---

# Avaliação do Módulo 02 — Introdução à Arquitetura de Segurança

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Avaliação de módulo · M02</span>
<span class="saa-tier saa-tier--professional">Professional → Architect</span>
<span class="saa-meta">90 min · 10 questões + 4 tarefas</span>
</div>

## Instruções

- **Parte 1** — dez questões de múltipla escolha, situacionais. Vale 50 pontos (5 cada).
- **Parte 2** — quatro tarefas de competência. Vale 50 pontos, avaliados pela rubrica descrita no gabarito.
- **Aprovação:** 70 pontos ou mais **e** nenhuma tarefa da Parte 2 avaliada como *Insuficiente*.
- Faça sem consultar as aulas. Confira o [gabarito comentado](answers/m02-security-architecture.md) somente ao final.

## Parte 1 — Questões situacionais

**1.** A Aurora Pagamentos tem um único arquiteto de segurança e cerca de quarenta projetos por ano. A diretoria quer que ele "aprove todos os projetos antes da produção". Qual é a principal consequência provável dessa decisão?

- (a) Maior cobertura de risco em todos os projetos, sem efeitos colaterais relevantes.
- (b) Fila, envolvimento tardio e incentivo para contornar o processo.
- (c) Redução do custo de corrigir falhas de desenho.
- (d) Dispensa de padrões corporativos de segurança.

**2.** Uma equipe de projeto decide usar um provedor de identidade próprio para os clientes de um novo portal, enquanto a organização não tem padrão para identidade de clientes. Onde essa decisão deve ser tomada?

- (a) Na equipe do projeto, porque ainda não há padrão.
- (b) Com o fornecedor do portal, que conhece o produto.
- (c) Na auditoria interna, que avalia os riscos.
- (d) No fórum de arquitetura corporativa, pois a questão se repetirá.

**3.** Qual frase pertence à **visão lógica** de uma arquitetura?

- (a) "O gateway de APIs valida tokens OAuth 2.0 e encaminha as chamadas por mTLS aos serviços internos."
- (b) "Clientes consultam seus pedidos por um canal digital autenticado."
- (c) "O gateway roda em três instâncias, em três zonas da região sa-east-1, atrás do balanceador de carga."
- (d) "A empresa quer reduzir o tempo de atendimento em 20%."

**4.** Uma organização tem o padrão "serviços internos usam TLS 1.2 ou superior com autenticação mútua". Um sistema legado não suporta mTLS. Qual é a resposta arquiteturalmente correta?

- (a) Ignorar o padrão para esse sistema, por ser legado.
- (b) Desligar o sistema imediatamente até que suporte mTLS.
- (c) Exceção com prazo, compensatórios e aprovação do dono do risco.
- (d) Alterar o padrão para aceitar comunicação sem criptografia em sistemas legados.

**5.** O padrão de criptografia da organização exige HSM para todas as chaves. Nos últimos seis meses, 85% dos projetos pediram exceção. O que isso indica com mais probabilidade?

- (a) Que as equipes de projeto estão sendo negligentes.
- (b) Que o padrão é desproporcional e deve variar por classificação.
- (c) Que é preciso comprar mais HSMs para atender à demanda crescente dos projetos.
- (d) Que o processo de exceções deve ser abolido.

**6.** Uma empresa de 40 funcionários quer implantar integralmente a arquitetura de referência multi-account de um provedor cloud, com todos os serviços de segurança descritos. Qual é a principal preocupação?

- (a) Nenhuma, porque a referência do provedor é gratuita.
- (b) Referências de provedores são inseguras por definição.
- (c) A referência só se aplica a empresas do setor financeiro.
- (d) A estrutura pode exceder a capacidade da equipe de operá-la.

**7.** O conselho pede "um framework que mostre a postura de segurança de cada subsidiária e as prioridades de investimento, em linguagem de negócio". Qual é o mais adequado como ponto de partida?

- (a) NIST CSF 2.0, com perfis atual e alvo por subsidiária.
- (b) NIST SP 800-53, porque é o catálogo mais completo.
- (c) O outline do CISSP.
- (d) Um benchmark de configuração de sistemas operacionais.

**8.** Qual opção é um **requisito de qualidade** relacionado à segurança, e não um requisito funcional nem uma restrição?

- (a) "O sistema exige um segundo fator para alterar a conta bancária do lojista."
- (b) "Dados de cartão não são armazenados fora do ambiente de dados de cartão."
- (c) "Eventos de autenticação chegam ao SIEM em até 5 minutos."
- (d) "Usar o produto X de WAF."

**9.** Em uma solução híbrida, o acesso administrativo usa um bastion no datacenter e um serviço gerenciado de sessão na cloud. Qual verificação é mais importante na revisão?

- (a) Se os dois produtos são do mesmo fabricante.
- (b) Se o bastion do datacenter tem mais memória e CPU que o serviço gerenciado da cloud.
- (c) Se o diagrama físico segue as cores corporativas.
- (d) Se as duas realizações atendem aos requisitos do componente lógico.

**10.** Uma decisão registrada em um ADR aceito precisa mudar porque surgiu um serviço novo. O que fazer?

- (a) Editar o ADR original com a nova decisão.
- (b) Apagar o ADR original e criar outro com o mesmo número e a nova decisão.
- (c) Escrever um novo ADR que substitui o anterior e marcar o original.
- (d) Registrar a mudança apenas na ata da reunião.

## Parte 2 — Tarefas de competência

### Tarefa 1 — Análise de diagrama (12 pontos)

A equipe de uma varejista propõe a arquitetura abaixo para um novo serviço de pedidos.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/assessment-m02-task1.mmd"
```

<figcaption>Figura 1 — Arquitetura proposta para análise na avaliação do Módulo 02.</figcaption>
</figure>

Identifique **quatro problemas de arquitetura de segurança**. Para cada um, indique a fronteira ou o componente afetado, o risco em linguagem de negócio e uma recomendação **no nível lógico**.

### Tarefa 2 — Níveis e hierarquia (10 pontos)

Classifique cada item em **dois eixos**: (i) nível de abstração — conceitual, lógico ou físico — quando aplicável; (ii) tipo — política, princípio, padrão, baseline, diretriz, controle ou exceção.

1. "Nenhum acesso é concedido sem autorização explícita."
2. "A regra 412 do firewall interno permite apenas o bastion acessar a porta 22 da zona PCI."
3. "Servidores Linux seguem o benchmark CIS nível 1, com os desvios do anexo B."
4. "O sistema de conciliação está dispensado do mTLS até 30/06, com segmento dedicado e verificação de integridade dos arquivos."
5. "Prefira serviços gerenciados de gestão de segredos."

### Tarefa 3 — Requisitos verificáveis (12 pontos)

Reescreva os três requisitos abaixo para que sejam específicos, verificáveis, rastreáveis e neutros em produto. Indique a categoria de cada um (funcional, qualidade ou restrição) e uma origem plausível.

1. "O sistema deve ser seguro contra ataques."
2. "Os logs devem ser adequados."
3. "Usar o firewall da marca Y para proteger o banco."

### Tarefa 4 — Decisão sob restrição (16 pontos)

A Meridiana Distribuidora (Caso A) teve o orçamento do ano 1 **reduzido de R$ 1,2 milhão para R$ 700 mil**. A renovação do seguro continua em nove meses. Com base na solução de referência do Caso A ou na sua:

1. Monte uma matriz de decisão para **priorizar** as iniciativas que cabem no novo orçamento, com critérios e pesos explícitos.
2. Indique o que fica para o ano 2 e o **risco residual** resultante, com dono proposto.
3. Escreva um parágrafo de no máximo 120 palavras para a diretoria explicando a escolha.

## Depois de responder

Confira o [gabarito comentado](answers/m02-security-architecture.md), aplique a rubrica às tarefas e registre as aulas a revisar.
