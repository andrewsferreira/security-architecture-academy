---
id: M00-L04
title: "Aula 04 — Datacenters, armazenamento, clusters e alta disponibilidade"
public_title: "Módulo Inicial — Aula 04 — Datacenters, armazenamento, clusters e alta disponibilidade"
description: Como datacenters, storage, clusters, replicação e backup sustentam a disponibilidade — e como identificar pontos únicos de falha e diferenciar alta disponibilidade de recuperação.
domain: infrastructure-foundations
tier: fundamental
status: published
prerequisites: [M00-L01]
objectives:
  - Identificar pontos únicos de falha em uma arquitetura de aplicação.
  - Diferenciar redundância, replicação síncrona, replicação assíncrona e backup quanto ao que protegem.
  - Explicar RTO e RPO e relacioná-los às escolhas de arquitetura.
  - Reconhecer por que alta disponibilidade não substitui backup isolado.
minutes: 60
sources: [NIST-SP800-34-R1, AWS-WA-RELIABILITY, BOOK-ANDERSON-SE3]
further_reading: [BOOK-GOOGLE-BSRS]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M00
---

# Aula 04 — Datacenters, armazenamento, clusters e alta disponibilidade { #datacenters-armazenamento-clusters-e-alta-disponibilidade }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo Inicial · Nível 0</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min · ID técnico: M00-L04</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Disponibilidade é uma das três propriedades clássicas de segurança, e é a que a diretoria percebe primeiro: quando o sistema para, o negócio para. Esta aula mostra como datacenters, storage, clusters e replicação mantêm sistemas no ar, como encontrar **pontos únicos de falha** e por que duas perguntas — *quanto tempo posso ficar parado?* e *quantos dados posso perder?* — orientam todas as decisões. Também mostra o erro mais caro dessa área: confundir alta disponibilidade com capacidade de recuperação.

**Pré-requisitos:** [Computação, sistemas operacionais e virtualização](01-computing-os-virtualization.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Identificar pontos únicos de falha em uma arquitetura de aplicação.
- Diferenciar redundância, replicação síncrona, replicação assíncrona e backup quanto ao que protegem.
- Explicar RTO e RPO e relacioná-los às escolhas de arquitetura.
- Reconhecer por que alta disponibilidade não substitui backup isolado.

## Conceito

### Falhas são certas; a questão é o impacto

Discos falham, fontes queimam, links caem, atualizações dão errado, pessoas apagam o banco errado, atacantes cifram servidores. Uma arquitetura não evita todas as falhas — ela decide **quais falhas o sistema tolera sem parar**, **quanto tempo leva para voltar** quando para, e **quantos dados se perdem**.

Dois indicadores traduzem isso em requisitos:

- **RTO (*Recovery Time Objective*)** — tempo máximo aceitável até o serviço voltar.
- **RPO (*Recovery Point Objective*)** — quantidade máxima aceitável de dados perdidos, medida em tempo ("posso perder os últimos 15 minutos").

Esses valores **vêm do negócio**, por meio de uma análise de impacto (*Business Impact Analysis*, tratada na Aula 05 do Módulo 3 e no NIST SP 800-34). A arquitetura é a forma de atingi-los com custo proporcional.

### Ponto único de falha

Um **ponto único de falha** (*single point of failure*, SPOF) é um componente cuja falha derruba o serviço inteiro. Encontrá-los é um exercício de leitura de diagrama: para cada componente, pergunte "se este parar, o que acontece?". Componentes de segurança também podem ser SPOFs — um firewall sem par redundante ou um provedor de identidade único param tudo o que depende deles.

## Fundamentos técnicos

### Redundância em camadas

| Camada | Mecanismo | Protege contra |
|:---|:---|:---|
| Energia e refrigeração | Fontes duplas, nobreaks, geradores, circuitos independentes | Falha elétrica e térmica |
| Rede | Links e switches redundantes, roteamento com rotas alternativas | Falha de equipamento ou de operadora |
| Servidores | Vários servidores atrás de balanceador; clusters com failover | Falha de um servidor |
| Armazenamento | RAID, controladoras redundantes, replicação entre arrays | Falha de disco ou controladora |
| Site | Segundo datacenter ou região de cloud | Desastre no site primário |

Datacenters também são instalações físicas, com controle de acesso, câmeras e procedimentos de entrada — um tema retomado na Aula 01 do Módulo 8.

### Balanceamento e clusters

Um **balanceador de carga** distribui requisições entre vários servidores e retira de circulação os que falham nos testes de saúde. Servidores **sem estado** (que não guardam dados de sessão localmente) escalam e se recuperam facilmente — por isso o princípio da AWS *Scale horizontally to increase aggregate workload availability*.

Um **cluster** de alta disponibilidade mantém um nó ativo e outro pronto para assumir (*ativo-passivo*) ou vários nós ativos (*ativo-ativo*). O mecanismo de detecção de falha — o *heartbeat* — precisa evitar o *split brain*: dois nós acreditando ser o primário ao mesmo tempo e corrompendo dados.

### Replicação: síncrona e assíncrona

- **Síncrona:** a gravação só é confirmada quando a réplica também gravou. RPO próximo de zero, mas exige baixa latência — normalmente no mesmo site ou em sites próximos.
- **Assíncrona:** a réplica recebe as gravações com algum atraso. Funciona a grandes distâncias, mas o atraso **é** o RPO em caso de perda do primário.

### Backup

**Replicação copia tudo — inclusive o erro.** Se um operador apaga uma tabela ou um ransomware cifra o banco, a réplica recebe a alteração em segundos. **Backup** é uma cópia em um ponto no tempo, guardada separadamente, que permite voltar a um estado anterior. Para cumprir esse papel diante de atacantes, o backup precisa ser:

- **Isolado:** administrado com credenciais separadas do domínio corporativo e em rede própria.
- **Imutável ou offline:** impossível de alterar ou apagar durante o período de retenção.
- **Testado:** restaurações periódicas comprovam que funciona e medem o RTO real — o princípio *Test recovery procedures* da AWS.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m00-l04-ha-datacenter.mmd"
```

<figcaption>Figura 1 — Aplicação de três camadas com alta disponibilidade em dois sites e backup isolado.</figcaption>
</figure>

A figura combina os mecanismos: balanceadores em par, aplicação em racks diferentes, banco com réplica síncrona local (falha de servidor, RPO zero) e réplica assíncrona remota (desastre no site, RPO igual ao atraso da replicação) e, separado de tudo, um repositório de backup isolado — o único que protege contra corrupção ou destruição intencional dos dados.

## Exemplo empresarial

!!! example "Meridiana — "temos réplica, não precisamos de backup""

    O ERP da Meridiana roda com o banco replicado para um segundo servidor na mesma sala. Ao discutir o orçamento de backup, um gerente argumentou: "Já temos o banco duplicado".

    O arquiteto apresentou três cenários:

    | Evento | A réplica ajuda? | O backup isolado ajuda? |
    |:---|:---|:---|
    | Falha do servidor do banco | Sim — failover em minutos | Sim, mas com restauração mais lenta |
    | Exclusão acidental de dados | Não — a exclusão é replicada | Sim — volta ao ponto anterior |
    | Ransomware cifra o banco e o NAS de backup atual, que usa contas do domínio | Não | Só se for isolado e imutável |
    | Incêndio na sala | Não — mesma sala | Sim, se houver cópia fora do site |

    A conclusão foi manter a réplica (para o RTO) e investir em backup isolado, imutável e com cópia fora do site (para o RPO diante de erros e ataques). As duas coisas resolvem problemas diferentes.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Requisitos | "O sistema tem que ficar no ar" | RTO e RPO definidos pelo negócio para cada sistema |
| Redundância | Duplicar servidores, esquecendo rede, firewall e identidade | Análise de SPOF em todas as camadas, inclusive controles de segurança |
| Backup | NAS na rede corporativa, administrado com contas do domínio | Repositório isolado, imutável, com cópia fora do site |
| Testes | Backup "configurado" sem restauração | Testes periódicos de restauração com medição do tempo |

## Aplicabilidade: on-premises, cloud e híbrido

| Ambiente | O que muda |
|:---|:---|
| **On-premises** | A organização projeta e paga energia, salas, hardware duplicado e segundo site. |
| **Cloud** | Zonas de disponibilidade (datacenters independentes na mesma região) e regiões permitem redundância sem construir sites; serviços gerenciados de banco oferecem réplicas e backups automáticos. O cliente continua responsável por **projetar** o uso dessas opções. |
| **Híbrido** | É comum usar a cloud como site de recuperação do datacenter — com atenção a credenciais, conectividade e dependências (como o diretório) que precisam existir no site de recuperação. |

## Como especificar e implementar

- "Cada sistema tem RTO e RPO aprovados pelo dono do negócio; a arquitetura documenta como os atinge."
- "Componentes de segurança dos quais o serviço depende (firewall, provedor de identidade, DNS) atendem ao mesmo RTO do serviço."
- "Backups de sistemas críticos são imutáveis por no mínimo 30 dias, administrados com credenciais fora do domínio corporativo, com cópia fora do site e teste de restauração trimestral."

## Trade-offs, limitações e antipadrões

- **Disponibilidade custa.** Cada "nove" adicional (99,9% → 99,99%) exige redundância, automação e testes mais caros. O valor deve vir do impacto da parada.
- **Complexidade gera falhas.** Clusters mal configurados causam indisponibilidades que um servidor único não teria.
- **Antipadrão — redundância compartilhando a mesma dependência:** dois servidores no mesmo rack, na mesma fonte ou dependendo do mesmo DNS.
- **Antipadrão — backup alcançável por quem ataca a produção.**

## Como validar

- Percorrer o diagrama componente a componente perguntando "se este falhar, o que acontece?".
- Executar testes de failover e de restauração e comparar o tempo medido com o RTO.
- Verificar se as credenciais e a rede do backup são independentes das da produção.
- Conferir se o site de recuperação tem as dependências necessárias (identidade, DNS, certificados).

## Como apresentar e justificar

- **Para engenharia:** "A réplica atende ao RTO de falha de servidor; o backup imutável atende ao RPO diante de exclusão e ransomware. Precisamos dos dois."
- **Para gestores:** "Hoje, se um ataque cifrar o ERP, não temos uma cópia que o atacante não consiga apagar. O investimento garante que conseguimos voltar a operar."

## Checklist de revisão arquitetural

- [ ] RTO e RPO estão definidos e aprovados pelo negócio.
- [ ] Não há ponto único de falha não aceito formalmente, incluindo controles de segurança.
- [ ] Componentes redundantes não compartilham a mesma dependência física ou lógica.
- [ ] Backup é isolado, imutável, com cópia fora do site e testes de restauração.
- [ ] O site de recuperação tem as dependências necessárias para operar.

## Questões de compreensão

**1.** Qual a diferença entre RTO e RPO? Dê um exemplo de cada.

??? success "Resposta comentada"

    RTO é o tempo máximo até o serviço voltar (por exemplo, "o ERP deve voltar em 4 horas"); RPO é a quantidade máxima de dados que se aceita perder, medida em tempo (por exemplo, "podemos perder no máximo os últimos 15 minutos de pedidos").

**2.** Por que a replicação síncrona costuma ser usada em distâncias curtas?

??? success "Resposta comentada"

    Porque cada gravação espera a confirmação da réplica; em distâncias grandes, a latência torna as gravações lentas demais para a aplicação.

**3.** Um banco tem réplica assíncrona em outro site com atraso médio de 10 minutos. Qual é, aproximadamente, o RPO em caso de perda do site primário?

??? success "Resposta comentada"

    Cerca de 10 minutos: as gravações ainda não replicadas no momento da perda são perdidas.

**4.** Por que a alta disponibilidade não protege contra ransomware?

??? success "Resposta comentada"

    Porque replica imediatamente as alterações — inclusive a cifragem feita pelo ransomware. Só um backup isolado e imutável preserva um estado anterior ao ataque.

## Exercício de tomada de decisão

!!! question "Cenário: RTO e RPO do agendamento da Lumen Saúde"

    O negócio definiu para o agendamento online: **RTO de 1 hora e RPO de 5 minutos**. Hoje o sistema roda em um único servidor com banco local e backup diário em fita. Compare três propostas — (A) manter o servidor único e passar o backup para disco a cada hora; (B) dois servidores de aplicação atrás de balanceador, banco com réplica síncrona, backup frequente, isolado e imutável, com logs de transação, e teste de restauração; (C) um segundo datacenter ativo-ativo, com replicação síncrona do banco entre os sites e sem mudança no backup — pelos critérios RTO, RPO (inclusive diante de ataque) e custo. Depois, diga qual requisito cada mudança da proposta escolhida atende.

??? success "Resolução de referência"

    | Critério | Peso | A — Backup horário | B — Redundância local e backup imutável | C — Dois sites ativos |
    |:---|:---|:---|:---|:---|
    | Atende ao RTO de 1 hora | 3 | 1 | 3 | 3 |
    | Atende ao RPO de 5 minutos, inclusive diante de ataque | 3 | 1 | 3 | 1 |
    | Custo e complexidade | 2 | 3 | 2 | 1 |
    | **Total ponderado** | | **12** | **22** | **14** |

    **Recomendação: B.** A alternativa A não atende a nenhum dos dois requisitos: perde até uma hora de dados e depende de reconstruir o servidor. A C resolve a falha de um site inteiro e atende ao RPO de 5 minutos para falhas de hardware, mas a replicação síncrona copia também a corrupção ou a cifragem feita por um atacante — replicação não é backup —, e, sem mudança no backup, a recuperação de um ataque volta à fita diária; além disso, custa muito mais.

    - **Dois ou mais servidores de aplicação atrás de balanceador** — atende ao RTO para falha de servidor.
    - **Banco com réplica síncrona (no mesmo site ou em zona de disponibilidade próxima)** — atende ao RPO de 5 minutos para falha de servidor ou de storage.
    - **Backup frequente (por exemplo, a cada hora, com logs de transação para recuperação a um ponto no tempo), isolado e imutável** — atende ao RPO diante de corrupção ou ataque; o backup diário em fita não atende, pois perderia até 24 horas de agendamentos.
    - **Teste de restauração** — comprova que o RTO de 1 hora é atingível também no cenário de restauração, não só no de failover.

    Ponto de atenção: com RPO de 5 minutos diante de ataque, a recuperação a um ponto no tempo exige que os logs de transação também estejam protegidos contra o atacante.

## Pontos-chave

- RTO e RPO vêm do negócio e orientam as escolhas de arquitetura.
- Pontos únicos de falha podem estar em qualquer camada — inclusive nos controles de segurança.
- Replicação síncrona dá RPO próximo de zero a curta distância; assíncrona funciona longe, com RPO igual ao atraso.
- Replicação copia o erro; só backup isolado, imutável e testado permite voltar a um estado anterior.
- Disponibilidade custa: cada nível deve ser justificado pelo impacto da parada.

## Referências

### Fundamentação principal

- NIST. *SP 800-34 Rev. 1 — Contingency Planning Guide for Federal Information Systems*. 2010. <https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final> — planejamento de contingência, Business Impact Analysis e estratégias de recuperação. *(Página oficial conferida.)*
- AWS. *Reliability Pillar — Design principles*. <https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html> — princípios *Automatically recover from failure*, *Test recovery procedures* e *Scale horizontally to increase aggregate workload availability*.

### Leitura complementar

- H. Adkins *et al.* *Building Secure and Reliable Systems*. O'Reilly, 2020. Cap. 8 *Design for Resilience* e Cap. 9 *Design for Recovery*. <https://google.github.io/building-secure-and-reliable-systems/raw/toc.html> *(capítulos localizados pelo sumário)*.
- R. Anderson. *Security Engineering*, 3ª ed. Cap. 27, §27.3.4 *Failure modes and effects analysis* (p. 972) — técnica de engenharia para encontrar falhas e seus efeitos.

### Aplicação prática

- Os achados RS-01 (ponto único de falha) e RS-02/RS-03 (backup) da ferramenta do [Laboratório 02](../../labs/lab-02-architecture-modeling.md) aplicam exatamente estes conceitos ao modelo da Meridiana.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
