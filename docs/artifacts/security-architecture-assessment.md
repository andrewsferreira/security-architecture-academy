---
id: ART-SAA
title: "Modelo: Security Architecture Assessment"
description: Modelo editável de avaliação de arquitetura de segurança de uma organização ou ambiente — escopo, contexto e tolerância, método e critérios, As-Is, avaliação por domínio com evidência, caminhos de ataque, achados classificados, To-Be, lacunas, plano em ondas, riscos residuais e decisões pedidas —, com critérios de qualidade e exemplo preenchido.
status: published
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
---

# Modelo: Security Architecture Assessment

A avaliação de arquitetura de segurança (*Security Architecture Assessment*) responde, para uma organização ou um ambiente inteiro: **onde estamos**, **o que isso permite a um atacante**, **para onde devemos ir** e **em que ordem**. Ela é mais ampla que a revisão de uma solução ([Módulo 4 — Aula 07](../modules/04-threat-modeling/07-architecture-review-validation.md), com o [Architecture Review Checklist](architecture-review-checklist.md)): cobre rede, identidade, acesso remoto, Zero Trust, legados e recuperação, e termina em um plano. O estudo de caso integrado do [Módulo 5 — Aula 07](../modules/05-network-security/07-secure-enterprise-network.md) e o plano em ondas do [Módulo 7 — Aula 07](../modules/07-zero-trust/07-progressive-deployment.md) mostram o raciocínio aplicado.

## Quando usar

- Ao assumir a arquitetura de segurança de uma organização ou de uma unidade de negócio.
- Antes de um programa de modernização (Zero Trust, migração para cloud, substituição de legados).
- Depois de um incidente relevante, para separar a correção pontual das causas estruturais.

## Modelo

```markdown
# Security Architecture Assessment — <Organização ou ambiente>

**Versão:** <N> · **Período da avaliação:** <datas> · **Avaliador:** <papel>
**Patrocinador:** <papel> · **Destinatários:** <comitê, diretoria>

## 1. Escopo
- Dentro: <ambientes, unidades, sistemas, processos>
- Fora: <o que não foi avaliado e por quê>

## 2. Contexto
- Objetivos de negócio: <...>
- Processos críticos e objetivos de recuperação (BIA): <processo, MTD, RPO>
- Apetite e tolerância a risco aprovados: <declaração e data>
- Obrigações: <lei | contrato | adoção voluntária — quais>
- Restrições: <orçamento, equipe, janelas, prazos>

## 3. Método e critérios
- Fontes: <entrevistas, documentos, configurações, testes>
- Critérios: <padrões internos, arquiteturas de referência, catálogos de controles>
- Métodos de validação: <examinar | entrevistar | testar — por domínio>

## 4. Arquitetura atual (As-Is)
<Diagrama com zonas, fronteiras de confiança e fluxos críticos.>

## 5. Avaliação por domínio

| Domínio | Situação | Resultado | Evidência e método | Achados |
|:---|:---|:---|:---|:---|
| Segmentação e fluxos | <descrição factual> | <Atende / Parcial / Não atende> | <evidência; testar/examinar/entrevistar> | <SAA-NN> |
| Perímetro e inspeção | | | | |
| Acesso remoto e de terceiros | | | | |
| Identidade e autenticação | | | | |
| Privilégios e identidades de máquina | | | | |
| Ciclo de vida e segregação de funções | | | | |
| Zero Trust (decisão por recurso) | | | | |
| Legados e protocolos | | | | |
| Backup e recuperação | | | | |
| Monitoração e resposta | | | | |

## 6. Caminhos de ataque críticos (MITRE ATT&CK <versão>)

| Cenário | Passos (tática — técnica) | Onde o As-Is interrompe | Onde o To-Be interromperá |
|:---|:---|:---|:---|

## 7. Achados

| ID | Domínio | Achado | Evidência | Severidade | Cenário de risco | Recomendação | Dono | Prazo |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| SAA-<NN> | <domínio> | <fato> | <como foi verificado> | <Bloqueante / Condição / Recomendação> | <RSK-...> | <ação> | <papel> | <data> |

## 8. Arquitetura-alvo (To-Be) e lacunas
<Diagrama To-Be.>

| Lacuna | Risco no As-Is | To-Be | Etapa |
|:---|:---|:---|:---|

## 9. Plano em ondas

| Onda | Escopo | Pré-requisitos | Critério de aceite | Cenários interrompidos |
|:---|:---|:---|:---|:---|

## 10. Riscos residuais e decisões pedidas
- Residuais: <risco, nível, dono, prazo de revisão>
- Decisões pedidas: <o que a governança precisa decidir>

## Anexos
- <Risk register> · <Security Control Matrix> · <Threat models> · <ADRs> · <evidências>
```

## Orientação por seção

| Seção | Pergunta que responde | Erro comum |
|:---|:---|:---|
| Escopo | O que foi e o que não foi avaliado? | Esconder o que ficou de fora, dando a impressão de cobertura total |
| Contexto | Contra o que a arquitetura é comparada? | Avaliar sem tolerância nem BIA — tudo vira "alto" |
| Método e critérios | Como cheguei às conclusões? | Conclusões sem dizer se a evidência foi testada ou só relatada |
| Avaliação por domínio | Onde estamos em cada área? | Notas sem evidência; média que esconde o domínio crítico |
| Caminhos de ataque | O que um atacante consegue hoje? | Lista de vulnerabilidades sem a sequência que as liga |
| Achados | O que precisa mudar, com que urgência? | Achados sem dono, prazo ou ligação com risco |
| To-Be e lacunas | Para onde vamos? | To-Be descrito por produtos, não por resultados |
| Plano em ondas | Em que ordem, dentro das restrições? | Plano que ignora orçamento, equipe e janelas |
| Residuais e decisões | O que sobra e quem decide? | Terminar em recomendações sem pedir decisões |

## Critérios de qualidade

- [ ] Escopo e exclusões explícitos.
- [ ] A avaliação usa a BIA, a tolerância aprovada e as obrigações classificadas (lei, contrato, adoção voluntária).
- [ ] Cada resultado por domínio tem evidência e o método usado; controles críticos foram testados.
- [ ] Pelo menos um caminho de ataque crítico está descrito com a versão do ATT&CK e os pontos de interrupção.
- [ ] Achados têm severidade, cenário de risco, dono e prazo; bloqueantes aparecem primeiro.
- [ ] O plano cabe nas restrições declaradas e cada onda tem critério de aceite testável.
- [ ] O documento termina com decisões que a governança pode tomar.

## Exemplo preenchido

Trecho da avaliação da **Meridiana Distribuidora** (organização fictícia do [Caso A](../case-studies/case-a-meridiana/index.md)), feita antes do plano de melhoria, com fatos já trabalhados nos Módulos 5, 6 e 8. A [matriz de controles](security-control-matrix.md#exemplo-preenchido) e o [risk register](risk-register.md#exemplo-preenchido) mostram a situação depois das primeiras etapas.

**Avaliação por domínio (parcial):**

| Domínio | Situação | Resultado | Evidência e método | Achados |
|:---|:---|:---|:---|:---|
| Acesso remoto e de terceiros | VPN só com senha, acesso à rede inteira | Não atende | Política da VPN exportada (examinar); tentativa de alcançar o ERP a partir de conta de vendas (testar) | SAA-01 |
| Privilégios | Administradores do domínio fazem login em servidores comuns, inclusive no servidor de etiquetas | Não atende | Eventos de logon dos últimos 30 dias (examinar) | SAA-02 |
| Backup e recuperação | Appliance integrado ao AD; fita na sala de servidores | Não atende | Teste de isolamento: cópias apagadas em dois minutos com credencial do domínio (testar) | SAA-03 |
| Legados | Servidor de etiquetas sem suporte, na rede comum | Parcial | Exceção registrada, compensatórios ainda não implantados (examinar) | SAA-04 |

**Achados (parcial):**

| ID | Achado | Severidade | Cenário | Recomendação | Dono | Prazo |
|:---|:---|:---|:---|:---|:---|:---|
| SAA-01 | Credencial roubada da VPN dá acesso à rede inteira | Bloqueante | RSK-007 | MFA resistente a phishing e acesso por aplicação | Gerente de TI | Etapa 1 |
| SAA-03 | Backup não sobrevive a um atacante com privilégio no domínio | Bloqueante | RSK-007 | Identidade própria, repositório imutável e cópia isolada | Gerente de infraestrutura | Etapa 1 |
| SAA-02 | Credenciais do domínio expostas em servidores sem proteção | Condição | RSK-007 | Separação de contas por plano e estações dedicadas | Coordenador de segurança | Etapa 2 |
| SAA-04 | Sistema sem suporte sem compensatórios | Condição | Servidor de etiquetas | Zona de legados com quatro fluxos, sem internet | Diretor de operações | 90 dias |

**Caminho de ataque (ATT&CK v20):** VPN com credencial roubada (Initial Access — T1133, T1078) → extração de credenciais no servidor de etiquetas (Credential Access — T1003) → movimento lateral por serviços remotos (Lateral Movement — T1021) → exclusão das cópias e cifragem (Impact — T1490, T1486). No As-Is, nenhum passo é interrompido; o plano em ondas do [Módulo 7 — Aula 07](../modules/07-zero-trust/07-progressive-deployment.md) mostra como o número de pontos de interrupção sobe a cada onda.

**Decisões pedidas:** aprovar as etapas 1 e 2; aceitar formalmente, com prazo, o risco do servidor de etiquetas até a troca das impressoras.
