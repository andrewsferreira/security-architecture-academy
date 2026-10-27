---
title: "ADR-002 — Segmentação da rede interna em zonas de confiança"
description: Decisão de arquitetura do Caso A sobre a segmentação da rede plana da Meridiana Distribuidora — alternativas, matriz de decisão, consequências e risco residual.
status: published
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# ADR-002 — Segmentação da rede interna em zonas de confiança

**Status:** Aceita (exemplo do Caso A) · **Data:** 2026-10-23 · **Decisores:** arquiteto de segurança, gerente de TI · **Consultados:** operações dos CDs, equipe de infraestrutura

## Contexto

A rede interna da Meridiana é plana: estações, servidores, controladores de domínio, ERP, servidor de arquivos, NAS de backup, o servidor de etiquetas sem suporte e os três CDs estão no mesmo segmento. Um atacante que comprometa qualquer estação alcança todos os ativos críticos. Os CDs operam 24x7 e só admitem mudanças aos domingos, das 2h às 6h. A equipe de infraestrutura tem quatro pessoas e experiência com o NGFW de borda, mas nenhuma com ferramentas de microssegmentação. Não há inventário completo de fluxos entre sistemas.

## Requisitos e riscos relacionados

- REQ-05 — zonas com comunicação negada por padrão entre elas.
- REQ-11 — isolamento do servidor de etiquetas.
- Riscos R1 e R4 da [solução do caso](solution.md#analise-de-riscos).

## Alternativas consideradas

- **A — Zonas com firewall interno:** dividir a rede em zonas (usuários, aplicações, dados, gestão, CDs e legados) em VLANs distintas, com um firewall interno em alta disponibilidade aplicando a política entre zonas.
- **B — Microssegmentação por agente:** instalar agentes nos servidores e controlar o tráfego host a host, sem redesenhar a rede.
- **C — Manter a rede plana e reforçar a detecção:** compensar com EDR e monitoramento.

| Critério | Peso | A — Zonas | B — Microssegmentação | C — Plana + detecção |
|:---|:---|:---|:---|:---|
| Contenção de movimentação lateral | 3 | 2 | 3 | 1 |
| Risco para a operação 24x7 dos CDs | 3 | 2 | 1 | 3 |
| Capacidade da equipe para operar | 2 | 3 | 1 | 3 |
| Cobertura de dispositivos sem agente (coletores, legado, NAS) | 2 | 3 | 1 | 1 |
| Custo no ano 1 | 1 | 2 | 1 | 3 |
| **Total ponderado** | | **26** | **17** | **23** |

A microssegmentação (B) oferece a melhor contenção, mas exige agentes que não rodam nos coletores dos CDs, no NAS e possivelmente no servidor legado — justamente ativos críticos —, além de conhecimento de fluxos que a empresa ainda não tem. Manter a rede plana (C) deixa o risco principal sem tratamento preventivo; detecção sozinha não impede a propagação de um ransomware em minutos.

## Decisão

Vamos segmentar a rede interna em **seis zonas de confiança** — usuários, aplicações, dados, gestão, centros de distribuição e legados —, com um **firewall interno em alta disponibilidade** aplicando a política entre zonas com negação por padrão. A migração ocorrerá **zona a zona**, nas janelas de domingo, com as regras inicialmente em modo de registro por duas semanas para mapear os fluxos reais antes do bloqueio. As zonas de gestão, dados e legados são as primeiras.

## Consequências

- **Positivas:** um comprometimento na zona de usuários não alcança diretamente dados, gestão nem legados; o servidor sem suporte fica isolado; os fluxos entre sistemas passam a ser documentados — o que beneficia futuras decisões.
- **Negativas:** novo componente crítico (o firewall interno), que precisa de alta disponibilidade e monitoramento; risco de interrupções por fluxos não mapeados durante a migração; aumento do trabalho de gestão de regras; a contenção dentro de cada zona continua limitada.
- **Neutras:** o firewall de borda permanece como está.

## Risco residual

Movimentação lateral **dentro** de uma mesma zona, em especial na zona de dados. **Dono do risco:** gerente de TI. Avaliar microssegmentação apenas para a zona de dados no ano 2, quando os fluxos estiverem documentados.

## Verificação

- 100% dos fluxos entre zonas com regra documentada e dono.
- Teste semestral: a partir de uma estação da zona de usuários, nenhum serviço administrativo das zonas de dados e de gestão é alcançável.
- Relatório mensal de regras sem uso, para remoção.

## Revisão

Após a migração da última zona, ou se houver incidente de disponibilidade causado pela segmentação.

## Relacionamentos

- Complementa o [ADR-001](adr-001-remote-access.md).
- Logs do firewall interno alimentam o SIEM do [ADR-003](adr-003-logging.md).
- O isolamento do servidor de etiquetas está associado a uma exceção ao padrão de sistemas suportados, com prazo até a substituição.
