---
title: "Gabarito — Avaliação do Módulo 00"
description: Gabarito comentado da avaliação do Módulo 00, com justificativa das alternativas incorretas, respostas de referência das tarefas e rubrica de correção.
status: published
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
---

# Gabarito — Avaliação do Módulo 00

!!! warning "Responda primeiro"

    Este é o gabarito da [avaliação do Módulo 00](../m00-foundations.md). Faça a avaliação antes de ler.

## Parte 1 — Respostas comentadas

| Questão | Resposta | Aula |
|:---|:---|:---|
| 1 | **c** | M00-L01 |
| 2 | **a** | M00-L02 |
| 3 | **d** | M00-L02 |
| 4 | **b** | M00-L02 |
| 5 | **c** | M00-L03 |
| 6 | **a** | M00-L04 |
| 7 | **d** | M00-L05 |
| 8 | **b** | M00-L06 |
| 9 | **a** | M00-L07 |
| 10 | **c** | M00-L07 |

**1 — (c).** Virtualização isola cargas, mas o hypervisor e quem o administra ficam dentro da fronteira de confiança de todas as VMs que ele hospeda. (a) ignora o hypervisor e sua administração; (b) a VLAN trata da rede, não da camada de virtualização; (d) há impacto de segurança, não só de desempenho.

**2 — (a).** `10.0.0.0/8` é faixa privada do RFC 1918; `/24` indica que 24 bits identificam a rede, sobrando 8 bits para hosts (254 utilizáveis). (b) faixas privadas não são roteadas na internet; (c) inverte o significado da máscara; (d) há três faixas privadas, não apenas `192.168.0.0/16`.

**3 — (d).** O resolvedor corporativo é ponto de telemetria e de controle (bloqueio de domínios maliciosos, detecção de comando e controle e exfiltração por DNS). (a) DNS é uma das melhores fontes de detecção; (b) o efeito principal não é desempenho; (c) DHCP independe do resolvedor usado.

**4 — (b).** NAT não é controle desenhado para segurança: protege incidentalmente conexões iniciadas de fora e deixa de proteger ao publicar serviços. (a) NAT não substitui política de firewall; (c) NAT é típico de IPv4, e IPv6 tende a dispensá-lo — não é obrigatório; (d) phishing não tem relação com NAT.

**5 — (c).** Segmentar por função cria fronteiras onde controles podem atuar, e a gestão do switch nunca deve estar acessível a partir de estações comuns. (a) não trata a ausência de fronteira; (b) o problema é de desenho, não de equipamento; (d) DHCP não é a causa.

**6 — (a).** Redundância de servidores não elimina pontos únicos de falha no storage e no switch. (b) olha apenas um elo; (c) cluster protege contra falha, não contra exclusão ou corrupção; (d) replicação copia também exclusões e corrupções.

**7 — (d).** A decomposição transforma chamadas internas em chamadas de rede, multiplicando pontos que exigem autenticação, autorização e proteção em trânsito. (a) o balanceador não enxerga as chamadas entre serviços; (b) a criptografia em trânsito fica mais necessária; (c) a decomposição não expõe bancos à internet por si só.

**8 — (b).** Em qualquer modelo de serviço, dados, identidades, permissões e configuração permanecem com o cliente. (a) e (c) são do provedor no SaaS; (d) é o erro mais comum em análises de risco de SaaS.

**9 — (a).** Fluxos não rotulados que atravessam fronteiras precisam de dados, protocolo, autenticação e justificativa — e um acesso direto da DMZ ao banco é um sinal de alerta. (b), (c) e (d) não respondem a nenhuma pergunta de segurança relevante nesse momento.

**10 — (c).** Administração, logs, backup e dependências compartilhadas são omissões frequentes e caminhos privilegiados de ataque. (a), (b) e (d) costumam estar presentes e não são as omissões perigosas.

## Parte 2 — Respostas de referência

**Tarefa 1 — Plano de endereçamento.**

- **Problema:** os mesmos endereços existem nos dois ambientes; o roteamento entre eles é ambíguo e a interconexão não funciona sem tradução. Regras de firewall e investigações passam a depender do contexto de cada endereço.
- **Renumerar** a VPC (ou o datacenter): resolve definitivamente e mantém endereços únicos; exige esforço e janela de mudança, mais fácil enquanto a VPC é nova.
- **NAT entre ambientes:** rápido de implantar; esconde a origem real, complica regras e investigações e tende a se tornar permanente.
- **Regra proposta:** "Cada ambiente — datacenter, filiais, cada nuvem e cada região — recebe um bloco reservado de um plano corporativo de endereçamento, sem sobreposição; nenhuma rede é criada fora do plano."

**Tarefa 2 — Leitura de diagrama.**

- **Componentes:** usuários (internet), balanceador, dois servidores de aplicação, banco, provedor de pagamentos — e os ausentes: administração, logs, backup, DNS, identidade.
- **Fluxos:** internet → balanceador; balanceador → aplicação; aplicação → banco; aplicação → provedor de pagamentos. Cada um com protocolo, porta, autenticação e criptografia.
- **Dados:** dados pessoais e de pagamento em quais fluxos e onde ficam armazenados.
- **Fronteiras:** internet/DMZ, DMZ/aplicação, aplicação/dados, organização/terceiro.
- **Perguntas:** como a aplicação se autentica no provedor de pagamentos e onde ficam as credenciais? Por onde os administradores acessam os servidores? Para onde vão os logs, e eles contêm dados de pagamento? Há backup do banco, onde e com qual proteção?

## Rubrica das tarefas

| Nível | Pontos | Descrição |
|:---|:---|:---|
| **Excelente** | 20 | Responde a tudo o que foi pedido, usa os conceitos corretamente, considera o cenário e declara trade-offs. |
| **Adequado** | 14 | Correto, mas sem trade-offs ou sem uma das partes pedidas. |
| **Insuficiente** | 6 | Incorreto, genérico ("seguir boas práticas") ou ignora o cenário. |

## Se você não atingiu o mínimo

| Questões ou tarefa com erro | Revise |
|:---|:---|
| 1 | [M00-L01](../../modules/00-foundations/01-computing-os-virtualization.md) |
| 2, 3, 4, Tarefa 1 | [M00-L02](../../modules/00-foundations/02-tcp-ip-networking.md) e o [Laboratório 00](../../labs/lab-00-network-plan.md) |
| 5 | [M00-L03](../../modules/00-foundations/03-segmentation-connectivity.md) |
| 6 | [M00-L04](../../modules/00-foundations/04-datacenter-high-availability.md) |
| 7 | [M00-L05](../../modules/00-foundations/05-containers-apis-serverless.md) |
| 8 | [M00-L06](../../modules/00-foundations/06-cloud-computing-models.md) |
| 9, 10, Tarefa 2 | [M00-L07](../../modules/00-foundations/07-reading-architecture-diagrams.md) |
