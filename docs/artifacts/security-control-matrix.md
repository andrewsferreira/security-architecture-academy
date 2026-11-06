---
id: ART-SCM
title: "Modelo: Security Control Matrix"
description: Modelo editável de matriz de controles de segurança — controles do catálogo interno ligados a riscos, requisitos, building blocks, donos, evidências, métodos de validação, indicadores, exceções e mapeamentos a referências como NIST CSF 2.0, SP 800-53 e CIS Controls —, com visões de cobertura, critérios de qualidade e exemplo preenchido.
status: published
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
---

# Modelo: Security Control Matrix

A matriz de controles mostra, em um só lugar, **quais controles existem**, **por que existem** (riscos e requisitos), **como são implementados** (building blocks da arquitetura), **quem responde** por eles, **como provar** que funcionam e **a que referências** correspondem. Fundamentos na [Aula 03 do Módulo 3](../modules/03-governance-risk/03-control-selection-tailoring.md) (seleção e tailoring) e na [Aula 07 do Módulo 3](../modules/03-governance-risk/07-control-catalog-risk-architecture.md) (catálogo interno e rastreabilidade); as seções "Controles e padrões relevantes" das aulas dos Módulos 5 a 8 trazem controles por domínio.

## Quando usar

- Para consolidar os controles de uma arquitetura-alvo e mostrar que cada risco relevante está coberto.
- Para responder a auditorias e questionários (clientes, seguradoras) com uma evidência por controle, mapeada a várias referências.
- Em revisões de arquitetura, para identificar controles sem dono, sem evidência ou sem risco que os justifique.

## Modelo

```markdown
# Security Control Matrix — <Organização ou escopo>

**Versão:** <N> · **Data:** <AAAA-MM-DD> · **Responsável:** <papel>
**Referências mapeadas:** <por exemplo, NIST CSF 2.0; SP 800-53 Rev. 5 (Release); CIS Controls v8.1>

## Matriz principal

| ID | Objetivo do controle | Escopo | Implementação de referência | Tipo e função | Dono | Evidência | Método de validação | Indicador | Riscos | Requisitos | Status | Exceções | Mapeamentos |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| CTL-<DOM>-<NN> | <resultado esperado> | <onde vale> | <building block> | <técnico/processual; preventivo/detectivo/corretivo> | <papel> | <o que prova> | <examinar/entrevistar/testar> | <medida> | <RSK-...> | <SR-...> | <implementado/parcial/planejado/herdado> | <EXC-...> | <CSF; SP 800-53; CIS> |

## Visão de cobertura por risco

| Risco | Nível | Preventivos | Detectivos | Corretivos ou de recuperação | Lacuna |
|:---|:---|:---|:---|:---|:---|
| RSK-<NNN> | <nível> | <CTL-...> | <CTL-...> | <CTL-...> | <o que falta> |

## Controles herdados

| Controle | Provedor | Evidência do provedor | O que continua com a organização |
|:---|:---|:---|:---|
```

## Orientação por campo

| Campo | Pergunta que responde | Erro comum |
|:---|:---|:---|
| ID | Como referenciar o controle em ADRs, riscos e auditorias? | IDs que mudam a cada versão |
| Objetivo | Que resultado o controle garante? | Nomear a ferramenta ("firewall X") em vez do resultado |
| Escopo | Onde vale? | Escopo implícito, que esconde exceções |
| Implementação de referência | Que building block entrega o controle? | Controle sem ligação com a arquitetura |
| Tipo e função | É técnico ou processual? Previne, detecta ou corrige? | Só controles preventivos para um risco crítico |
| Dono | Quem responde pela eficácia? | "TI" como dona |
| Evidência e método | Como provar que funciona? | Examinar a configuração de um controle crítico, sem testar |
| Indicador | Como acompanhar ao longo do tempo? | Só indicadores de implementação ("% instalado") |
| Riscos e requisitos | Por que o controle existe? | Controle sem risco nem requisito — candidato a aposentadoria |
| Status | Está em operação? | "Implementado" sem evidência |
| Exceções | Onde o controle não vale, e até quando? | Exceções fora da matriz |
| Mapeamentos | A que referências corresponde? | Copiar o texto do framework como se fosse o controle |

## Regras de construção

- O **controle é da organização**; frameworks entram como **mapeamento**. Um controle pode atender a várias referências, e uma referência pode exigir vários controles.
- Todo risco **alto ou crítico** do [register](risk-register.md) precisa de pelo menos um controle preventivo e um detectivo ou de recuperação — ou de uma decisão explícita de aceite.
- Controles críticos são validados por **teste**; examinar a configuração mostra que existe, não que funciona ([Módulo 4 — Aula 07](../modules/04-threat-modeling/07-architecture-review-validation.md)).
- Controles **herdados** de provedores registram a evidência recebida e a parte que continua com a organização.
- Catálogos como a SP 800-53 e os CIS Controls são referências voluntárias, salvo quando um contrato ou norma os torna exigíveis — registre essa diferença no mapeamento.

## Critérios de qualidade

- [ ] Cada controle tem objetivo verificável, dono, evidência e método de validação.
- [ ] Cada controle aponta para pelo menos um risco ou requisito.
- [ ] A visão de cobertura não deixa risco alto ou crítico sem controle detectivo ou de recuperação.
- [ ] Exceções aparecem ao lado do controle, com prazo.
- [ ] Mapeamentos citam a referência com versão (por exemplo, SP 800-53 Rev. 5, CIS Controls v8.1).
- [ ] Indicadores incluem pelo menos uma medida de eficácia para os controles críticos.

## Exemplo preenchido

Trecho da matriz da **Meridiana Distribuidora** (organização fictícia do [Caso A](../case-studies/case-a-meridiana/index.md)) para o cenário RSK-007 — ransomware a partir do acesso remoto —, na situação depois das primeiras etapas do plano. A [avaliação de arquitetura](security-architecture-assessment.md#exemplo-preenchido) registra o estado anterior, em que esses controles ainda não existiam.

| ID | Objetivo | Implementação | Tipo e função | Dono | Evidência e método | Indicador | Riscos | Status | Mapeamentos |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| CTL-IAM-03 | Acesso remoto e administrativo exige autenticação resistente a phishing | IdP com FIDO2; gateway de acesso por aplicação que exige o IdP | Técnico, preventivo | Gerente de identidade | Relatório de métodos por conta; tentativa de login sem o fator (testar) | % de contas do escopo com FIDO2 | RSK-007 | Parcial — MFA resistente a phishing em toda a VPN desde o mês 1; acesso por aplicação em implantação | CSF 2.0 PR.AA; SP 800-53 IA-2(1), IA-2(2), AC-17; CIS v8.1 Controle 6 |
| CTL-NET-02 | Servidores críticos só alcançáveis por fluxos documentados | Zonas do datacenter; firewall interno com negar por padrão | Técnico, preventivo | Coordenador de redes | Varredura a partir da rede de usuários (testar) | Fluxos fora da matriz de fluxos | RSK-007 | Planejado — etapa 3 | SP 800-53 SC-7, SC-7(5), AC-4; CIS v8.1 Controle 12 |
| CTL-DET-04 | Uso anômalo de credenciais privilegiadas é detectado e tratado | Eventos de DCs e do acesso privilegiado no SIEM, com casos de uso | Técnico, detectivo | Coordenador do SOC | Simulação de logon fora das estações dedicadas (testar) | % de alertas críticos triados em até 30 min | RSK-007 | Implementado | CSF 2.0 DE.CM; SP 800-53 SI-4, AU-6; CIS v8.1 Controle 8 |
| CTL-BKP-02 | Cópias de recuperação sobrevivem a um atacante com privilégio no domínio | Backup com identidade própria, repositório imutável, cópia isolada | Técnico, corretivo | Gerente de infraestrutura | Teste de isolamento com credencial do domínio; restauração com tempo medido (testar) | Tempo de restauração da expedição comparado ao MTD | RSK-007 | Implementado | CSF 2.0 RC.RP; SP 800-53 CP-9, CP-9(1), CP-10; CIS v8.1 Controle 11 |

**Visão de cobertura:** RSK-007 (crítico) tem preventivos (CTL-IAM-03, CTL-NET-02), detectivo (CTL-DET-04) e de recuperação (CTL-BKP-02). A lacuna registrada é o CTL-NET-02 ainda planejado — por isso o residual continua médio até a etapa 3.
