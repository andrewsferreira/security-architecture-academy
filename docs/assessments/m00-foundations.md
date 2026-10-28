---
id: AS-M00
title: "Avaliação do Módulo Inicial — Fundamentos de Infraestrutura e Computação"
description: Avaliação baseada em competências do Módulo Inicial — questões situacionais sobre virtualização, redes, segmentação, alta disponibilidade, plataformas modernas, modelos de nuvem e leitura de diagramas, e duas tarefas de análise.
status: published
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
---

# Avaliação do Módulo Inicial — Fundamentos de Infraestrutura e Computação { #avaliacao-do-modulo-00-fundamentos-de-infraestrutura-e-computacao }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Avaliação de módulo · Módulo Inicial</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min · 10 questões + 2 tarefas</span>
</div>

## Instruções

- **Parte 1** — dez questões de múltipla escolha, situacionais. Vale 60 pontos (6 cada).
- **Parte 2** — duas tarefas de análise. Vale 40 pontos (20 cada), avaliados pela rubrica do gabarito.
- **Aprovação:** 70 pontos ou mais **e** nenhuma tarefa avaliada como *Insuficiente*.
- Faça sem consultar as aulas. Confira o [gabarito comentado](answers/m00-foundations.md) somente ao final.

## Parte 1 — Questões situacionais

**1.** Uma empresa hospeda, no mesmo hypervisor, máquinas virtuais do ambiente de pagamentos e do ambiente de testes. Qual afirmação descreve corretamente o risco?

- (a) Não há risco relevante: o hypervisor isola completamente as máquinas virtuais.
- (b) O risco existe apenas se as VMs de pagamento e de teste estiverem na mesma VLAN da rede física.
- (c) O hypervisor e quem o administra passam a integrar a fronteira de confiança dos pagamentos.
- (d) O risco é de desempenho: as VMs de teste podem consumir recursos dos pagamentos.

**2.** Um servidor tem o endereço `10.20.30.15/24`. Qual afirmação está correta?

- (a) Ele está em uma faixa privada (RFC 1918), na rede `10.20.30.0/24`, que comporta até 254 hosts.
- (b) Ele é acessível diretamente pela internet, porque todo endereço de classe A é roteado publicamente.
- (c) A máscara `/24` indica que 24 bits identificam o host.
- (d) O endereço é público, pois faixas privadas começam sempre em `192.168`.

**3.** Ao revisar uma rede, você nota que as estações usam qualquer servidor DNS da internet. Qual é a principal perda para a segurança?

- (a) Nenhuma relevante: o DNS apenas traduz nomes e não tem papel algum em segurança.
- (b) A rede fica mais lenta, o que afeta só a disponibilidade dos serviços.
- (c) Os servidores DHCP deixam de entregar endereços às estações.
- (d) Perde-se a telemetria de consultas e o bloqueio de domínios maliciosos.

**4.** Um gestor afirma: "Estamos protegidos, porque o NAT esconde nossos servidores". O que responder?

- (a) Correto: o NAT esconde os servidores e dispensa a política de firewall.
- (b) NAT protege só de forma incidental e não substitui a política de firewall.
- (c) Correto apenas em redes IPv6, nas quais o NAT é obrigatório.
- (d) Correto: o NAT também impede ataques de phishing enviados aos usuários internos.

**5.** A rede de uma filial tem usuários, servidores de arquivos e a interface de gestão do switch na mesma VLAN. Qual a melhor primeira mudança?

- (a) Instalar um antivírus mais robusto em todas as estações da filial.
- (b) Substituir os switches por modelos mais novos e com mais portas.
- (c) Separar usuários, servidores e gestão em zonas, com fluxos só onde necessário.
- (d) Desligar o DHCP e configurar endereços fixos em todas as estações.

**6.** Um sistema tem dois servidores em cluster ativo-passivo, ambos ligados ao mesmo storage e ao mesmo switch. Qual afirmação é correta?

- (a) Storage e switch seguem como pontos únicos de falha; é preciso olhar toda a cadeia.
- (b) O sistema é altamente disponível, porque há dois servidores em cluster.
- (c) O cluster também elimina a necessidade de manter backup dos dados do sistema replicado.
- (d) A replicação do storage protege contra exclusões maliciosas de dados.

**7.** Em uma arquitetura de microsserviços, o que muda de mais importante para a segurança em relação a uma aplicação monolítica?

- (a) Nada muda: os controles continuam concentrados no balanceador de carga.
- (b) A criptografia em trânsito deixa de ser necessária dentro do cluster.
- (c) Os bancos de dados de cada serviço passam a ficar expostos à internet.
- (d) Chamadas internas passam a atravessar a rede e exigem autenticação e proteção.

**8.** Uma empresa migra o e-mail para um serviço SaaS. O que **continua** sendo responsabilidade dela?

- (a) Aplicar correções no sistema operacional dos servidores de e-mail do provedor.
- (b) Identidades, permissões, configuração do serviço e os dados.
- (c) Segurança física do datacenter do provedor.
- (d) Nada; no SaaS toda a responsabilidade é do provedor.

**9.** Em um diagrama, um fluxo vai do portal na DMZ diretamente ao banco de dados na zona de dados, sem rótulo. Qual a primeira pergunta de revisão?

- (a) Que dados trafegam, com que protocolo e autenticação, e por que o acesso é direto?
- (b) Qual cor representa o banco de dados e se ela segue a legenda?
- (c) Quantos servidores o banco de dados tem e em qual versão está?
- (d) Qual é o fabricante e o modelo do firewall instalado entre a DMZ e a zona de dados?

**10.** Na leitura de um diagrama de arquitetura, quais elementos costumam estar **ausentes** e são caminhos frequentes de ataque?

- (a) Os usuários finais e os papéis de negócio que cada um exerce no sistema analisado.
- (b) O nome da aplicação e o título do diagrama.
- (c) Fluxos administrativos, de logs e de backup, e dependências compartilhadas.
- (d) A legenda de cores e o significado dos ícones.

## Parte 2 — Tarefas de análise

**Tarefa 1 — Plano de endereçamento (20 pontos).** A Meridiana usa `10.0.0.0/16` no datacenter e criou a VPC do portal B2B também em `10.0.0.0/16`. Agora quer integrar o portal ao ERP. Explique o problema, as opções (renumerar, NAT entre ambientes) com uma vantagem e uma desvantagem de cada, e proponha uma regra de endereçamento para evitar o problema no futuro.

**Tarefa 2 — Leitura de diagrama (20 pontos).** Descreva, em até dez linhas, como você aplicaria o método de quatro passagens (componentes, fluxos, dados, fronteiras) do Módulo Inicial — Aula 07 a um diagrama que mostra: usuários na internet, um balanceador, dois servidores de aplicação, um banco de dados e um provedor de pagamentos externo. Liste pelo menos três perguntas que faria aos autores.

## Depois da avaliação

- Confira o [gabarito comentado](answers/m00-foundations.md).
- Para praticar endereçamento e segmentação, faça o [Laboratório 00](../labs/lab-00-network-plan.md).
