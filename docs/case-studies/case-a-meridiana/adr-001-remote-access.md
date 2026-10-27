---
title: "ADR-001 — Acesso remoto por aplicação, com MFA na VPN como transição"
description: Decisão de arquitetura do Caso A sobre o acesso remoto da Meridiana Distribuidora — alternativas, matriz de decisão, consequências e risco residual.
status: published
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# ADR-001 — Acesso remoto por aplicação, com MFA na VPN como transição

**Status:** Aceita (exemplo do Caso A) · **Data:** 2026-10-23 · **Decisores:** arquiteto de segurança, gerente de TI · **Consultados:** diretoria comercial, fornecedor do ERP, corretora do seguro

## Contexto

Cerca de 150 pessoas — representantes comerciais, gestores e três fornecedores — acessam a rede da Meridiana por uma VPN SSL autenticada apenas com usuário e senha do domínio. Uma vez conectadas, alcançam toda a rede interna, que é plana. Esse é o vetor de acesso inicial mais provável de um ataque de ransomware e um item obrigatório do questionário da seguradora, cuja renovação acontece em nove meses.

Os representantes comerciais usam essencialmente três aplicações: o ERP (consulta de estoque e pedidos), o servidor de arquivos e o Microsoft 365, este já acessado diretamente pela internet. A equipe de TI tem nove pessoas e não pode absorver a operação de uma infraestrutura complexa. As identidades já estão sincronizadas com o Microsoft Entra ID, que oferece MFA e acesso condicional.

## Requisitos e riscos relacionados

- REQ-01 — acesso remoto com MFA, por aplicação.
- REQ-02 — acesso de fornecedores individual, aprovado, temporário e gravado (tratado em parte por esta decisão).
- Riscos R1, R2 e R3 da [solução do caso](solution.md#analise-de-riscos).

## Alternativas consideradas

- **A — VPN com MFA e verificação de postura:** manter a VPN, adicionar MFA pelo provedor de identidade e verificação do dispositivo, e restringir o acesso por grupos.
- **B — Acesso por aplicação (ZTNA):** cada usuário acessa apenas as aplicações autorizadas, com identidade, MFA e postura avaliadas a cada sessão; a rede interna deixa de ser alcançável como um todo.
- **C — Desktop virtual (VDI):** usuários remotos acessam um desktop hospedado no datacenter, de onde usam as aplicações.

| Critério | Peso | A — VPN + MFA | B — ZTNA | C — VDI |
|:---|:---|:---|:---|:---|
| Redução do risco de acesso inicial e movimentação | 3 | 2 | 3 | 2 |
| Prazo para atender à seguradora | 3 | 3 | 2 | 1 |
| Esforço operacional para a equipe | 2 | 3 | 2 | 1 |
| Custo no ano 1 | 1 | 3 | 2 | 1 |
| Experiência dos representantes | 1 | 2 | 3 | 1 |
| **Total ponderado** | | **26** | **24** | **13** |

A alternativa A vence na matriz por prazo e esforço, mas mantém o acesso **à rede**, e não às aplicações — o que limita a redução de risco a longo prazo. A alternativa B tem o melhor resultado de segurança, porém não cabe no prazo da seguradora se for a única medida. A alternativa C exigiria infraestrutura de virtualização de desktops que a equipe não tem capacidade de operar.

## Decisão

Vamos adotar **acesso remoto por aplicação (ZTNA) como arquitetura-alvo**, e **habilitar MFA na VPN atual como medida de transição** nos primeiros 90 dias:

1. **Até 90 dias:** MFA obrigatório na VPN e no Microsoft 365 pelo provedor de identidade, com acesso condicional; o fornecedor do ERP passa a ter identidades individuais com MFA e janelas de acesso aprovadas.
2. **Até 12 meses:** migração dos usuários para ZTNA por grupos, começando pelos representantes comerciais; desativação da VPN SSL ao final.

A combinação aproveita o ganho rápido da alternativa A e chega à redução de risco da alternativa B.

## Consequências

- **Positivas:** o principal item da seguradora é atendido em 90 dias; ao final, usuários remotos deixam de alcançar a rede interna como um todo; o acesso passa a considerar o estado do dispositivo.
- **Negativas:** durante a transição, duas soluções de acesso remoto coexistem e precisam ser operadas e monitoradas; parte das aplicações legadas pode exigir adaptação para funcionar por ZTNA; há custo de licenciamento recorrente; os representantes precisam de comunicação e suporte na mudança.
- **Neutras:** o acesso ao Microsoft 365 permanece direto pela internet, agora com MFA e acesso condicional.

## Risco residual

Até a desativação da VPN, usuários com MFA continuam alcançando a rede inteira — o risco de movimentação lateral a partir de um dispositivo comprometido permanece. **Dono do risco:** gerente de TI, até a conclusão da migração para ZTNA.

## Verificação

- Relatório mensal do provedor de identidade: 100% das autenticações de VPN com MFA.
- Teste trimestral: um usuário de ZTNA não consegue alcançar sistemas fora das aplicações autorizadas.
- Data de desativação da VPN registrada como marco do plano.

## Revisão

Ao final da migração para ZTNA, ou se o prazo de 12 meses for ultrapassado.

## Relacionamentos

- Complementa o [ADR-002](adr-002-segmentation.md): ZTNA e segmentação reduzem a movimentação lateral por caminhos diferentes.
- Eventos de acesso remoto alimentam o SIEM do [ADR-003](adr-003-logging.md).
