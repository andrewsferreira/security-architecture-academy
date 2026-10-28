---
id: CS-A
title: "Caso A — Datacenter tradicional: Meridiana Distribuidora"
description: Estudo de caso completo de uma distribuidora com datacenter tradicional, Active Directory, rede plana e VPN sem MFA, que precisa reduzir o risco de ransomware, renovar o seguro cibernético e sustentar o crescimento do portal B2B.
status: published
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# Caso A — Datacenter tradicional: Meridiana Distribuidora

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Estudo de caso · CS-A</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">4 a 6 h</span>
</div>

!!! note "Cenário fictício"

    A Meridiana Distribuidora, as pessoas e todos os dados deste estudo são fictícios. Qualquer semelhança com organizações reais é coincidência.

## Resumo

Você é o primeiro arquiteto de segurança contratado pela Meridiana Distribuidora. A empresa opera com um datacenter tradicional, uma rede plana e acesso remoto protegido apenas por senha. A seguradora condicionou a renovação da apólice a melhorias de segurança, e um grande cliente exige uma avaliação de fornecedores. Sua tarefa é analisar o ambiente, propor uma arquitetura-alvo viável e defender a proposta para a diretoria.

**Pré-requisitos:** Módulo 2 completo. O caso antecipa temas de rede, identidade e ambientes legados que serão aprofundados nos Módulos 05, 06 e 08 — o nível de detalhe esperado aqui é **arquitetural**, não de configuração.

**Como fazer este caso:**

1. Leia este enunciado inteiro.
2. Produza os entregáveis da seção [Tarefas](#tarefas) **sem consultar a solução**.
3. Autoavalie-se com a [rubrica](#rubrica).
4. Compare com a [solução de referência](solution.md) e com os ADRs.

## Contexto e objetivos de negócio

A Meridiana distribui materiais elétricos e de construção para revendas e construtoras. Tem cerca de 600 funcionários, uma matriz e três centros de distribuição (CDs) que operam 24 horas por dia, sete dias por semana.

| Indicador | Valor |
|:---|:---|
| Pedidos pelo portal B2B | 35% do faturamento, com meta de crescer 40% em 18 meses |
| Equipe de TI | 9 pessoas; uma analista dedica metade do tempo à segurança |
| Custo estimado de uma parada dos três CDs | Perda de faturamento e multas contratuais de entrega; a diretoria considera inaceitável uma parada superior a 24 horas |
| Dados tratados | Cadastro e histórico de compras de clientes B2B, incluindo dados pessoais de contatos; dados de funcionários; tabelas de preços e margens |

**Objetivos declarados pela diretoria:**

1. **Renovar o seguro cibernético** em nove meses. O questionário da seguradora pergunta, entre outros itens, sobre MFA no acesso remoto, proteção de endpoints, backups offline ou imutáveis e gestão de contas privilegiadas.
2. **Passar na avaliação de segurança de fornecedores** de uma grande construtora, cliente estratégico, em seis meses.
3. **Reduzir o risco de uma parada prolongada dos CDs** por ransomware — um concorrente regional ficou onze dias parado no último ano.
4. **Sustentar o crescimento do portal B2B** sem aumentar o risco sobre os dados do ERP.

## Restrições

| Tipo | Restrição |
|:---|:---|
| Financeira | Orçamento aprovado de R$ 1,2 milhão para 12 meses, somando investimento e custos recorrentes do primeiro ano. Valores ilustrativos. |
| Operacional | Os CDs não podem parar. Janelas de mudança apenas aos domingos, das 2h às 6h. |
| Equipe | Nove pessoas de TI, sem SOC próprio. Contratações adicionais: no máximo uma pessoa de segurança. |
| Contratual | O ERP permanece no datacenter por pelo menos 18 meses (contrato de suporte). O fornecedor do ERP exige acesso remoto para suporte. |
| Tecnológica | O aplicativo de etiquetas dos CDs só roda em Windows Server 2012 R2; o fornecedor promete uma versão nova em dez meses. |
| Regulatória | LGPD para dados pessoais de contatos de clientes e de funcionários. |

## Arquitetura As-Is

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/case-a-as-is.mmd"
```

<figcaption>Figura 1 — Arquitetura As-Is da Meridiana Distribuidora.</figcaption>
</figure>

### Inventário e observações

| Componente | Situação atual |
|:---|:---|
| **Rede interna** | Plana: estações, servidores, controladores de domínio, ERP, servidor de arquivos, servidor de etiquetas e NAS de backup no mesmo segmento. Os CDs se conectam por VPN site-to-site diretamente a esse segmento. |
| **Firewall de borda** | NGFW com regras de entrada para o portal B2B e a VPN SSL. Sem filtragem interna. |
| **Acesso remoto** | VPN SSL com usuário e senha do domínio. Cerca de 150 usuários: representantes comerciais, gestores e três fornecedores. O fornecedor do ERP usa **uma conta compartilhada** com permissão de administrador local nos servidores do ERP. |
| **Active Directory** | Um domínio, dois controladores de domínio. **Onze contas** no grupo Domain Admins, todas usadas também para e-mail e navegação. Sincronização de identidades com o Microsoft 365, sem MFA habilitado. |
| **Portal B2B** | Aplicação Java em servidor Linux na DMZ; conecta-se **diretamente ao banco Oracle do ERP** com uma conta de banco de privilégios amplos, cuja senha está em arquivo de configuração. |
| **Estações** | Antivírus tradicional por assinatura; usuários com privilégio de administrador local por padrão. |
| **Backup** | Diário, para um NAS na mesma sala do datacenter, **ingressado no domínio**. Desde 2023 não há cópia fora do site. Restaurações nunca foram testadas de ponta a ponta. |
| **Logs** | Mantidos apenas localmente em cada servidor, por cerca de sete dias. Nenhum monitoramento centralizado. |
| **Legado** | Servidor de etiquetas em Windows Server 2012 R2 (sem suporte estendido desde outubro de 2023), acessado pelos coletores dos CDs. |

### Problemas e ameaças observados

- Um atacante que obtenha a senha de **qualquer** usuário da VPN chega à rede interna inteira.
- Contas de Domain Admins usadas para e-mail e navegação são alvo direto de phishing e roubo de credenciais.
- Um comprometimento do servidor do portal B2B entrega acesso amplo ao banco do ERP.
- O backup está ao alcance de um atacante com privilégios de domínio — exatamente o que um ransomware busca antes de criptografar.
- Sem logs centralizados, a empresa provavelmente não perceberia uma intrusão em andamento.
- O servidor de etiquetas não recebe correções de segurança e está no mesmo segmento de todos os ativos críticos.

## Tarefas

Produza os entregáveis abaixo. Tempo total sugerido: 4 a 6 horas.

| # | Entregável | Competências | Referência |
|:---|:---|:---|:---|
| 1 | **Análise do As-Is** usando o [Architecture Review Checklist](../../artifacts/architecture-review-checklist.md), com os cinco achados mais graves | C3 | Módulo 2 — Aulas 03 e 04 |
| 2 | **Cinco riscos principais em linguagem de negócio**, com probabilidade e impacto qualitativos | C4 | Módulo 2 — Aula 07 |
| 3 | **Requisitos de segurança** — ao menos dez, classificados e rastreáveis — usando a [Security Requirements Specification](../../artifacts/security-requirements-specification.md) | C2 | Módulo 2 — Aula 07 |
| 4 | **Alternativas** para três decisões: acesso remoto, segmentação interna e centralização de logs — com matriz de decisão para cada uma | C5 | Módulo 2 — Aulas 01 a 08 |
| 5 | **Arquitetura To-Be** nas visões conceitual e lógica | C6 | Módulo 2 — Aula 03 |
| 6 | **Três ADRs**, um para cada decisão do item 4 | C8 | Módulo 2 — Aula 08 |
| 7 | **Controles recomendados** por camada, com referência a frameworks | C7 | Módulo 2 — Aulas 04 e 06 |
| 8 | **Plano de implementação** em 90 dias, 6 meses e 12 meses, respeitando as restrições | C9 | — |
| 9 | **Indicadores de sucesso** e **riscos residuais** com dono | C8 | Módulo 2 — Aula 04 |
| 10 | **Resumo executivo** de uma página para a diretoria | C10 | Módulo 2 — Aula 07 |

## Rubrica

Use a [rubrica padrão de projetos](../../assessments/rubrics.md). Expectativas específicas deste caso:

| Critério | O que diferencia *Excelente* de *Adequado* |
|:---|:---|
| Segurança | Trata a cadeia do ransomware de ponta a ponta — acesso inicial, escalada de privilégio, movimentação lateral, destruição do backup — e não apenas o acesso remoto. |
| Cobertura de requisitos | Requisitos cobrem os quatro objetivos da diretoria, incluindo o crescimento do portal. |
| Justificativas | As matrizes de decisão consideram a equipe de nove pessoas e a restrição de janelas de mudança. |
| Viabilidade operacional | O plano não depende de um SOC próprio e respeita a operação 24x7 dos CDs. |
| Resiliência | A proposta de backup sobrevive a um atacante com privilégios de domínio e tem testes de restauração. |
| Custo | As escolhas cabem no orçamento ilustrativo e diferenciam investimento de custo recorrente. |
| Documentação | ADRs com consequências negativas; resumo executivo legível por quem não é técnico. |

## Referências

- CIS. *CIS Critical Security Controls v8.1 — Implementation Groups*. <https://www.cisecurity.org/controls/implementation-groups> — gratuito.
- NIST. *The NIST Cybersecurity Framework (CSF) 2.0*. 2024. <https://doi.org/10.6028/NIST.CSWP.29> — gratuito.
- NIST. *SP 800-53 Rev. 5* (Release 5.2.0). 2025. <https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls> — gratuito.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
