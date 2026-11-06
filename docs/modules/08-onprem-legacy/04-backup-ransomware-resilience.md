---
id: M08-L04
title: "Aula 04 — Backup, recuperação e resiliência contra ransomware"
public_title: "Módulo 8 — Aula 04 — Backup, recuperação e resiliência contra ransomware"
description: Como projetar backup e recuperação que sobrevivam a um atacante com privilégios administrativos — isolamento de identidade, imutabilidade, cópias offline, ambiente de recuperação limpo, imagens de referência, testes de restauração e ordem de recuperação.
domain: security-operations
tier: professional
status: published
prerequisites: [M03-L05, M04-L05, M06-L09]
objectives:
  - Explicar por que backups tradicionais falham contra ransomware.
  - Projetar uma arquitetura de backup isolada, imutável e com cópia offline.
  - Especificar testes de restauração que provem RTO, RPO e integridade.
  - Planejar a recuperação em ambiente limpo, na ordem certa, sem reintroduzir o atacante.
minutes: 75
sources: [CISA-STOPRANSOMWARE-GUIDE, NIST-SP1800-11, AWS-DR-WHITEPAPER, NIST-SP800-34-R1, NIST-SP800-53, CIS-CONTROLS-V8-1, MITRE-ATTACK]
further_reading: [NIST-IR-8374-R1, MS-AD-FOREST-RECOVERY]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M08
---

# Aula 04 — Backup, recuperação e resiliência contra ransomware { #backup-recuperacao-e-resiliencia-contra-ransomware }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 8 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M08-L04</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Ransomware moderno não se limita a cifrar servidores: procura e destrói os backups antes, para que pagar seja a única saída. O guia #StopRansomware observa que muitas variantes tentam encontrar e apagar ou cifrar backups acessíveis. Por isso, uma arquitetura de backup precisa partir de uma premissa dura: **o atacante pode ter privilégios de administrador do domínio**. Esta aula mostra como projetar backup e recuperação que sobrevivam a essa premissa e como provar que funcionam.

**Pré-requisitos:** [BIA, RTO e RPO](../03-governance-risk/05-bia-rto-rpo.md), [Pontos únicos de falha](../04-threat-modeling/05-single-points-of-failure.md) e [Recuperação de identidade](../06-iam/09-identity-recovery.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar por que backups tradicionais falham contra ransomware.
- Projetar uma arquitetura de backup isolada, imutável e com cópia offline.
- Especificar testes de restauração que provem RTO, RPO e integridade.
- Planejar a recuperação em ambiente limpo, na ordem certa, sem reintroduzir o atacante.

## Conceito

### Por que backups tradicionais falham

| Falha | Como o atacante explora | ATT&CK |
|:---|:---|:---|
| Servidor de backup no domínio | Credenciais do domínio dão acesso ao console e ao repositório | T1078 |
| Repositório gravável pela rede | Cópias apagadas ou cifradas junto com a produção | T1490, T1486 |
| Cópias de sombra e pontos de restauração locais | Removidos antes da cifragem | T1490 |
| Retenção curta | O ponto limpo mais recente é anterior ao início do comprometimento | — |
| Restauração nunca testada | Descobre-se no incidente que não funciona | — |

A NIST SP 1800-11 enfatiza que, na recuperação, as organizações precisam ter confiança de que os dados recuperados são **precisos, completos e livres de malware** — não basta restaurar.

### Princípios de arquitetura

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m08-l04-backup.mmd"
```

<figcaption>Figura 1 — Servidor de backup com identidade própria, repositório imutável, cópia isolada, ambiente de recuperação limpo e imagens de referência.</figcaption>
</figure>

1. **Isolamento de identidade:** o sistema de backup não confia no domínio corporativo; administração com contas próprias e autenticação resistente a phishing, a partir da zona de gestão.
2. **Imutabilidade:** o repositório impede exclusão e alteração dentro da retenção, mesmo por administradores do backup.
3. **Cópia isolada ou offline:** pelo menos uma cópia fora do alcance da rede de produção. O #StopRansomware Guide recomenda backups **offline e cifrados**, com disponibilidade e integridade testadas regularmente; o mesmo guia menciona armazenamento imutável como opção, a ser usada com cautela porque não atende aos critérios de conformidade de certas regulações.
4. **Ambiente de recuperação limpo:** restaurar primeiro em ambiente isolado, verificar integridade e ausência de malware, só então devolver à produção.
5. **Reconstrução em vez de restauração:** o guia recomenda manter **imagens de referência** e infraestrutura como código versionada, para reconstruir sistemas rapidamente.

## Fundamentos técnicos

### Retenção e RPO contra comprometimento

O whitepaper de recuperação de desastres da AWS lembra que replicação contínua pode não proteger contra corrupção de dados ou exclusão maliciosa, e que nesses casos o ponto de recuperação será sempre anterior à descoberta do problema (Módulo 3 — Aula 05). Para ransomware, a retenção precisa cobrir o **tempo entre o comprometimento inicial e a descoberta** — que pode ser de semanas. Uma estratégia comum combina:

| Camada | Frequência | Retenção | Proteção |
|:---|:---|:---|:---|
| Cópias frequentes | De hora em hora a diária | Dias | Imutável |
| Cópias de médio prazo | Diária a semanal | Semanas a meses | Imutável |
| Cópia isolada/offline | Semanal | Meses | Fora da rede |

### Testes que provam

| Teste | O que prova | Frequência sugerida |
|:---|:---|:---|
| Restauração de arquivo ou VM aleatória | Que as cópias são legíveis | Mensal |
| Restauração completa de um sistema crítico em ambiente isolado | RTO real e integridade | Semestral |
| Recuperação de processo crítico com dependências (identidade, DNS, aplicação) | Que a ordem funciona e o MTD é atendido | Anual |
| Tentativa de apagar cópia com credencial administrativa do domínio | Isolamento e imutabilidade | Anual |

A SP 800-34 Rev. 1 inclui testes, treinamento e exercícios como etapa do planejamento de contingência; sem eles, os objetivos de recuperação são apenas declarados.

### Ordem de recuperação

A recuperação segue as dependências mapeadas (Módulo 4 — Aula 05) e começa pela identidade (Módulo 6 — Aula 09):

1. Ambiente isolado, canal fora de banda, contas de emergência.
2. Identidade (diretório recuperado ou limpo, credenciais privilegiadas redefinidas).
3. Serviços de infraestrutura (DNS, PKI, backup).
4. Dados e aplicações críticas, conforme prioridade da BIA.
5. Demais sistemas.

O guia da CISA, em sua lista de resposta, recomenda restaurar a partir de backups offline **em ordem de prioridade**, tomando cuidado para não reinfectar sistemas limpos, e reconstruir sistemas a partir de imagens padrão.

## Exemplo empresarial

!!! example "Meridiana — o teste que derrubou a premissa"

    A Meridiana acreditava estar protegida: backup diário para um appliance no datacenter, com cópia semanal em fita. O teste de isolamento (tentar apagar cópias com credencial de administrador do domínio) apagou as cópias do appliance em dois minutos — o console estava integrado ao AD. A fita estava guardada na própria sala de servidores.

    Arquitetura nova: servidor de backup com contas locais próprias e chave de segurança física, na zona de gestão; repositório imutável com retenção de 30 dias; cópia semanal isolada em outro site; ambiente de recuperação com rede própria; imagens de referência para os servidores de aplicação. O exercício semestral passou a medir o RTO real da expedição (Módulo 3 — Aula 05) e, na segunda execução, ficou em 7 horas.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Identidade do backup | Integrada ao domínio | Própria, com autenticação resistente a phishing |
| Repositório | Gravável pela rede | Imutável durante a retenção |
| Cópia externa | Fita na mesma sala | Isolada ou offline em outro local |
| Restauração | Direto em produção | Ambiente limpo, com verificação de integridade e malware |
| Retenção | Dias | Cobre o tempo provável até a descoberta |
| Prova | Relatório de job bem-sucedido | Testes de restauração com tempos medidos |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias para a resiliência a ransomware:

| Controle ou padrão | Objetivo no backup e na recuperação | Referência |
|:---|:---|:---|
| Backup | Cópias com confiabilidade e integridade testadas, protegidas por criptografia | SP 800-53: CP-9 (System Backup), CP-9(1) (Testing for Reliability and Integrity) e CP-9(8) (Cryptographic Protection) |
| Cópia em outro local | Local alternativo de armazenamento e transferência das cópias para ele | SP 800-53: CP-6 (Alternate Storage Site) e CP-9(5) (Transfer to Alternate Storage Site) |
| Recuperação a estado conhecido | Recuperar e reconstituir após interrupção, comprometimento ou falha | SP 800-53: CP-10 (System Recovery and Reconstitution) |
| Teste do plano | Testes que medem eficácia e prontidão | SP 800-53: CP-4 (Contingency Plan Testing) |
| Restauração limpa | Verificar integridade e ausência de código malicioso antes de devolver à produção | SP 800-53: SI-7 (Software, Firmware, and Information Integrity) e SI-3 (Malicious Code Protection) |
| Recuperação de dados | Processo de recuperação, backups automatizados, protegidos, isolados e testados | CIS v8.1: Controle 11 (Data Recovery) |
| Ameaças de referência | Inibição da recuperação e cifragem para impacto | MITRE ATT&CK v20: T1490 e T1486 |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, imutabilidade e cópias entre contas e regiões são recursos nativos, mas a identidade que administra o backup precisa estar separada da que administra a produção — idealmente em conta distinta. Em on-premises, appliances com imutabilidade e cópias isoladas cumprem o papel. Em ambientes híbridos, uma prática comum é usar a nuvem como local da cópia isolada do datacenter — desde que a identidade e as chaves dessa cópia não dependam do domínio local.

## Como especificar e implementar

- "O sistema de backup não usa identidades do domínio corporativo e é administrado pela zona de gestão com autenticação resistente a phishing."
- "Cópias de sistemas críticos são imutáveis durante a retenção, e ao menos uma cópia é mantida isolada ou offline."
- "A retenção cobre o tempo provável entre comprometimento e descoberta, definido com a equipe de resposta."
- "Restaurações são testadas em ambiente isolado com verificação de integridade, com frequência proporcional à criticidade."
- "A ordem de recuperação segue as dependências mapeadas, começando pela identidade."

## Trade-offs, limitações e antipadrões

- **Trade-off:** retenção longa e cópias múltiplas aumentam custo; proporcione ao MTD e ao risco.
- **Antipadrão — "temos backup":** sem teste de isolamento e de restauração.
- **Antipadrão — imutabilidade com administrador capaz de reduzir a retenção.**
- **Limitação:** backup recupera disponibilidade e integridade, mas não desfaz vazamento — extorsão por exposição de dados exige outras medidas (Módulo 13).

## Como validar

- Tentar apagar ou alterar cópias com credencial de administrador do domínio.
- Restaurar um sistema crítico em ambiente isolado e medir o tempo.
- Verificar a idade da cópia limpa mais antiga disponível.
- Conferir se a cópia isolada está realmente fora do alcance da rede.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhuma cópia apagável ou alterável com credencial administrativa do domínio | Registro do teste de isolamento |
| Sistema crítico restaurado em ambiente isolado dentro do RTO | Registro do exercício com tempo medido |
| Cópia limpa mais antiga cobre a janela de retenção definida | Inventário de pontos de recuperação |
| Cópia isolada inalcançável a partir da rede de produção | Teste de conectividade e de credenciais a partir da produção, negado |

## Como apresentar e justificar

- **Para a diretoria:** "O teste mostrou que um atacante com acesso ao domínio apagaria nossos backups em dois minutos. A nova arquitetura resiste a isso, e já provamos a recuperação da expedição em 7 horas."
- **Para a operação:** "O backup tem contas próprias, fora do domínio. É o último recurso — e precisa sobreviver quando todo o resto cair."

## Checklist de revisão arquitetural

- [ ] Identidade do backup isolada do domínio.
- [ ] Repositório imutável e cópia isolada ou offline.
- [ ] Retenção dimensionada ao tempo provável de descoberta.
- [ ] Ambiente de recuperação limpo disponível.
- [ ] Testes de restauração e de isolamento com resultados registrados.
- [ ] Ordem de recuperação documentada, começando pela identidade.

## Questões de compreensão

**1.** Por que um servidor de backup integrado ao domínio é um risco?

??? success "Resposta comentada"

    Porque um atacante com credenciais do domínio obtém acesso ao console e ao repositório e pode apagar ou cifrar as cópias antes do impacto, eliminando a recuperação.

**2.** Por que restaurar em ambiente limpo antes de devolver à produção?

??? success "Resposta comentada"

    Para verificar que os dados estão íntegros e livres de malware e para não reintroduzir o atacante ou o mecanismo de persistência. A SP 1800-11 enfatiza dados precisos, completos e livres de malware.

**3.** Como dimensionar a retenção contra ransomware?

??? success "Resposta comentada"

    Pela janela provável entre o comprometimento inicial e a descoberta, que pode ser de semanas, de modo que exista um ponto anterior ao comprometimento.

## Exercício de tomada de decisão

!!! question "Cenário: cópia isolada da Lumen"

    A Lumen precisa de uma cópia isolada dos sistemas do datacenter. Opções: (A) fitas levadas semanalmente a um cofre de terceiros; (B) armazenamento de objetos imutável em nuvem, em conta dedicada com identidade separada; (C) segundo appliance de backup em outra clínica, na mesma rede corporativa. Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e recomende uma.

**Objetivos avaliados:** Projetar uma arquitetura de backup isolada, imutável e com cópia offline; especificar testes de restauração que provem RTO, RPO e integridade.

**Entrega esperada:** Matriz ponderada, recomendação da cópia isolada e a forma de provar o isolamento e o tempo de restauração.

**Critérios de avaliação:**

- A opção que não cumpre o requisito de isolamento é eliminada antes da soma.
- O isolamento da opção escolhida independe da identidade e da rede corporativas, e isso é testado.
- O tempo de restauração é comparado ao RTO, com teste que o comprove.

??? success "Resolução de referência"

    | Critério | Peso | A — Fitas em cofre de terceiros | B — Nuvem imutável em conta dedicada | C — Appliance em outra clínica |
    |:---|:---|:---|:---|:---|
    | Isolamento contra atacante com privilégio no domínio | 3 | 3 | 3 | 1 |
    | Tempo de restauração | 3 | 1 | 2 | 3 |
    | Custo e operação | 2 | 2 | 2 | 2 |
    | Baixa dependência de configuração correta | 1 | 3 | 2 | 2 |
    | **Total ponderado** | | **19** | **21** | **18** |

    - **Pesos:** a cópia isolada existe para sobreviver a um atacante com privilégio no domínio, e a Lumen precisa voltar a atender — isolamento e tempo de restauração pesam 3. Custo pesa 2; a dependência de configuração, 1.
    - **Atenção à soma:** C fica perto de A no total, mas não cumpre o requisito que define uma cópia isolada — alcançável pela rede e pela identidade corporativa, ela é eliminada antes de qualquer soma. O total de C aparece na tabela só para mostrar que, perto de A, a soma poderia enganar; a comparação que decide é entre A e B.

    - **A — Fitas:** isolamento físico forte; restauração lenta (dias), dependente de logística e de leitores compatíveis. Adequada como camada final de baixo custo, não como única.
    - **B — Nuvem imutável em conta dedicada:** isolamento lógico forte se a conta e as chaves não dependerem do domínio local; restauração mais rápida; custo recorrente e necessidade de governança da retenção.
    - **C — Appliance em outra clínica na mesma rede:** isolamento fraco — alcançável pela rede e pela identidade corporativa; protege contra falha física do site, não contra ransomware.
    - **Recomendação: B** como cópia isolada principal, com identidade própria e autenticação resistente a phishing; **A** opcional como camada adicional para dados de longa retenção. **C** só se tratada como réplica de disponibilidade, não como cópia isolada.
    - **Trade-off aceito e risco residual:** o isolamento de B é lógico — depende de que a conta, as chaves e a política de retenção não sejam alcançáveis a partir do domínio e de que ninguém consiga reduzir a retenção. O residual é tratado com conta em organização separada, autenticação resistente a phishing, alerta para mudanças de política e teste anual de isolamento.
    - **O que mudaria a decisão:** se a conectividade com a nuvem não suportar o volume de restauração dentro do RTO, B perde a nota de tempo e A com restauração inicial a partir das cópias imutáveis locais passa a ser a combinação; uma exigência regulatória que a imutabilidade em nuvem não atenda, como alerta o guia da CISA, favorece A.

    **Erros comuns:**

    - Chamar de cópia isolada uma réplica alcançável pela mesma rede e pela mesma identidade.
    - Confiar na imutabilidade sem verificar quem pode reduzir a retenção.
    - Não testar a restauração dentro do RTO.

## Pontos-chave

- Projete o backup supondo que o atacante tem privilégios de administrador do domínio.
- Isolamento de identidade, imutabilidade e cópia offline são a base.
- Restaure em ambiente limpo e verifique integridade e malware.
- Dimensione a retenção ao tempo provável até a descoberta.
- Teste restauração, isolamento e ordem de recuperação — e meça.

## Referências

### Fundamentação principal

- CISA, FBI, NSA, MS-ISAC. *#StopRansomware Guide*. 2023. <https://www.cisa.gov/stopransomware/ransomware-guide>. *(Lido; recomendações reconferidas em 2026-10-29.)*
- NIST NCCoE. *SP 1800-11 — Data Integrity: Recovering from Ransomware and Other Destructive Events*. <https://www.nccoe.nist.gov/projects/building-blocks/data-integrity/recover>. *(Página do projeto conferida.)*
- AWS. *Disaster Recovery of Workloads on AWS* — replicação versus cópias pontuais. *(Lido.)*
- NIST. *SP 800-34 Rev. 1* — testes e exercícios. *(Lido.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles CP-4, CP-6, CP-9, CP-9(1), CP-9(5), CP-9(8), CP-10, SI-3 e SI-7, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controle 11 — gratuito.
- MITRE. *ATT&CK v20* — T1490 e T1486. *(Páginas conferidas.)*

### Leitura complementar

- NIST. *IR 8374 Rev. 1 — Ransomware Risk Management: A CSF 2.0 Community Profile*. 2026.
- Microsoft. *Active Directory Forest Recovery Guide*.

### Aplicação prática

- Execute (em ambiente de teste ou com a equipe de backup) o teste de isolamento: com uma credencial de administrador do domínio, verifique se é possível apagar ou alterar alguma cópia. Registre o resultado e as ações.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
