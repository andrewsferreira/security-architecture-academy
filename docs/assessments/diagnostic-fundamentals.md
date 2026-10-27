---
id: AS-DIAG
title: "Avaliação diagnóstica de fundamentos"
description: Diagnóstico dos fundamentos de infraestrutura, segurança, risco e controles necessários para o Módulo 02, com indicação de estudo por seção.
status: published
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
---

# Avaliação diagnóstica de fundamentos

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Diagnóstico · M00 e M01</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">45 a 60 min · 18 questões</span>
</div>

## Para que serve

Esta avaliação verifica se você domina os fundamentos que o [Módulo 02](../modules/02-security-architecture/index.md) pressupõe. Ela **não é eliminatória**: o resultado indica o que revisar antes de seguir.

!!! tip "Como fazer"

    - Responda sem consultar materiais, anotando suas respostas.
    - Marque as questões em que você **chutou** — elas contam como erro para fins de estudo.
    - Confira no [gabarito comentado](answers/diagnostic-fundamentals.md) somente ao final.
    - **Critério:** 70% ou mais **em cada seção** (pelo menos 5 de 6). Abaixo disso, o gabarito indica as aulas de M00 ou M01 a estudar.

## Seção A — Infraestrutura e redes

**A1.** Um servidor na rede `10.20.30.0/24` precisa acessar a internet, e o firewall de borda traduz seu endereço privado para um endereço público. Que função é essa?

- (a) DHCP
- (b) NAT
- (c) DNS
- (d) VLAN

**A2.** Duas VLANs foram criadas no mesmo switch, uma para estações e outra para servidores. O que é necessário para que hosts das duas VLANs se comuniquem — e onde, portanto, faz sentido aplicar uma política de filtragem?

- (a) Nada: VLANs no mesmo switch se comunicam livremente.
- (b) Uma VPN site-to-site entre as VLANs.
- (c) Um servidor DNS em cada VLAN.
- (d) Um dispositivo de camada 3 (roteador ou firewall) entre elas.

**A3.** Em um modelo de serviço de cloud **PaaS**, qual destas responsabilidades normalmente continua sendo do cliente?

- (a) Aplicar correções no sistema operacional dos servidores do serviço.
- (b) Proteger fisicamente o datacenter.
- (c) Configurar quem pode acessar os dados e a aplicação implantada.
- (d) Manter o hipervisor.

**A4.** Uma aplicação de três camadas tem um balanceador, servidores de aplicação e um banco de dados. Os servidores de aplicação estão duplicados; o banco roda em uma única instância. Qual é o ponto único de falha?

- (a) O balanceador, sempre.
- (b) Os servidores de aplicação.
- (c) O banco de dados.
- (d) Não há ponto único de falha.

**A5.** O que diferencia um container de uma máquina virtual, do ponto de vista de isolamento?

- (a) Containers compartilham o kernel do sistema operacional hospedeiro; máquinas virtuais têm kernel próprio sobre um hipervisor.
- (b) Containers sempre oferecem isolamento mais forte que máquinas virtuais.
- (c) Máquinas virtuais não podem ser executadas em cloud.
- (d) Containers não podem acessar a rede.

**A6.** Em um diagrama, um fluxo vai da "Internet" para "Portal Web" e do "Portal Web" para "Banco de Clientes". Quantas fronteiras de confiança esse caminho cruza, no mínimo, se o portal está em uma DMZ e o banco em uma zona interna?

- (a) Nenhuma
- (b) Uma
- (c) Duas
- (d) Depende do protocolo

## Seção B — Princípios e mecanismos de segurança

**B1.** Um sistema registra quem aprovou cada pagamento, com assinatura digital vinculada ao aprovador, de forma que ele não possa negar a aprovação depois. Que propriedade está sendo garantida principalmente?

- (a) Disponibilidade
- (b) Confidencialidade
- (c) Não repúdio
- (d) Autorização

**B2.** Em caso de falha do serviço de autorização, uma API passa a **negar** todas as requisições até que o serviço volte. Que princípio está sendo aplicado?

- (a) Fail secure (fail closed)
- (b) Defense in depth
- (c) Security by obscurity
- (d) Open design

**B3.** Um analista pode cadastrar fornecedores **e** aprovar pagamentos para eles. Que princípio é violado?

- (a) Least privilege
- (b) Separation of duties
- (c) Fail secure
- (d) Defense in depth

**B4.** Para garantir que um arquivo não foi alterado e que veio de um emissor específico, o mecanismo mais adequado é:

- (a) Criptografia simétrica do arquivo com uma chave compartilhada.
- (b) Hash SHA-256 publicado junto com o arquivo no mesmo servidor.
- (c) Assinatura digital com a chave privada do emissor, verificada com sua chave pública.
- (d) Compactação do arquivo com senha.

**B5.** O certificado TLS de um serviço interno expirou e as integrações começaram a falhar. Qual capacidade de arquitetura teria evitado o problema?

- (a) Desabilitar a validação de certificados nos clientes.
- (b) Uso de HTTP em vez de HTTPS internamente.
- (c) Aumentar a validade de todos os certificados para dez anos.
- (d) Gestão do ciclo de vida de certificados, com inventário e renovação automatizada.

**B6.** O modelo Bell-LaPadula foi formulado principalmente para proteger qual propriedade?

- (a) Integridade
- (b) Confidencialidade
- (c) Disponibilidade
- (d) Não repúdio

## Seção C — Risco e controles

**C1.** Qual afirmação descreve corretamente a relação entre ameaça, vulnerabilidade e risco?

- (a) Risco é sinônimo de vulnerabilidade.
- (b) Risco combina a probabilidade de uma ameaça explorar uma vulnerabilidade e o impacto resultante.
- (c) Toda vulnerabilidade gera o mesmo nível de risco.
- (d) Ameaça é uma falha no software.

**C2.** Um alerta no SIEM avisa sobre logins de um mesmo usuário em dois países com dez minutos de diferença. Qual o tipo principal desse controle?

- (a) Preventivo
- (b) Corretivo
- (c) Dissuasório
- (d) Detectivo

**C3.** Um sistema legado não suporta MFA. Como medida temporária, ele foi isolado em um segmento acessível apenas a partir de um bastion que exige MFA. Como se classifica essa medida em relação ao requisito de MFA?

- (a) Controle compensatório
- (b) Controle corretivo
- (c) Aceitação de risco sem controle
- (d) Controle diretivo

**C4.** Qual opção representa **transferência** de risco?

- (a) Desligar o serviço vulnerável.
- (b) Implantar um WAF.
- (c) Documentar que o risco é conhecido e não será tratado.
- (d) Contratar seguro cibernético para cobrir parte das perdas financeiras de um incidente.

**C5.** Uma vulnerabilidade crítica foi publicada em um componente usado em um servidor que não está exposto à internet, não processa dados sensíveis e fica em segmento isolado. Comparado a um servidor exposto à internet com o mesmo componente, o risco é:

- (a) Normalmente menor, porque exposição e impacto são diferentes.
- (b) Igual, porque a vulnerabilidade é a mesma.
- (c) Sempre zero.
- (d) Maior, porque servidores internos são menos monitorados.

**C6.** Uma empresa conclui que, depois dos controles implementados, um risco continua em nível médio e a diretoria responsável decide aceitá-lo por seis meses. Como se chama o risco que permanece?

- (a) Risco inerente
- (b) Risco transferido
- (c) Risco residual
- (d) Risco operacional

## Depois de responder

Confira o [gabarito comentado](answers/diagnostic-fundamentals.md) e use a tabela de interpretação para decidir os próximos passos.
