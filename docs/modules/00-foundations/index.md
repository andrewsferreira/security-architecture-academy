---
id: M00
title: "Módulo 00 — Fundamentos de Infraestrutura e Computação"
description: A base técnica para ler e discutir qualquer arquitetura — computação e virtualização, redes TCP/IP, segmentação, datacenter e alta disponibilidade, plataformas modernas, cloud e leitura de diagramas.
stage: n0
status: published
prerequisites: []
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# Módulo 00 — Fundamentos de Infraestrutura e Computação

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 — Fundamentos de Tecnologia e Segurança</span>
<span class="saa-meta">7 aulas · cerca de 8 h de aulas</span>
<span class="saa-status saa-status--published">Published</span>
</div>

## Resumo

!!! abstract "Sobre este módulo"

    Arquitetos de segurança passam boa parte do tempo **lendo e questionando** arquiteturas desenhadas por outras pessoas: um diagrama de rede, uma proposta de migração para cloud, um cluster Kubernetes. Este módulo dá o vocabulário técnico mínimo para isso. Ele não forma administradores de rede ou de sistemas — forma alguém capaz de entender o que cada componente faz, **onde estão as fronteiras de isolamento** e que perguntas fazer quando uma delas é atravessada.

Ao concluir o módulo, você será capaz de:

- Explicar como sistemas operacionais, máquinas virtuais e containers isolam (ou não) cargas de trabalho.
- Acompanhar o caminho de uma requisição pela rede: endereçamento, DNS, roteamento, NAT e portas.
- Descrever como VLANs, roteamento, firewalls, VPN e TLS criam e protegem zonas de rede.
- Identificar pontos únicos de falha e entender como redundância, replicação e backup se combinam.
- Reconhecer os componentes de plataformas modernas: APIs, microsserviços, containers, Kubernetes e serverless.
- Diferenciar modelos de serviço e de implantação de cloud e o que cada um transfere ao provedor.
- Ler um diagrama arquitetural identificando componentes, fluxos, dados e fronteiras de confiança.

## Para quem é

| Perfil | Como usar o módulo |
|:---|:---|
| Vindo de segurança (GRC, SOC, AppSec) sem formação em infraestrutura | Estude todas as aulas na ordem. |
| Vindo de infraestrutura ou desenvolvimento | Faça a [avaliação diagnóstica](../../assessments/diagnostic-fundamentals.md); estude as aulas indicadas nas questões em que errar, e a [L07](07-reading-architecture-diagrams.md), que é o elo com o resto da formação. |

## Aulas

| Aula | Tema | Duração |
|:---|:---|:---|
| [L01](01-computing-os-virtualization.md) | Computação, sistemas operacionais e virtualização | 60 min |
| [L02](02-tcp-ip-networking.md) | Redes TCP/IP: modelo OSI, endereçamento, DNS, DHCP e NAT | 75 min |
| [L03](03-segmentation-connectivity.md) | Segmentação e conectividade: VLAN, roteamento, VPN, TLS e firewalls | 75 min |
| [L04](04-datacenter-high-availability.md) | Datacenters, armazenamento, clusters e alta disponibilidade | 60 min |
| [L05](05-containers-apis-serverless.md) | Containers, Kubernetes, APIs, microsserviços e serverless | 75 min |
| [L06](06-cloud-computing-models.md) | Cloud computing: modelos de serviço e de implantação | 60 min |
| [L07](07-reading-architecture-diagrams.md) | Lendo diagramas arquiteturais: componentes, fluxos e fronteiras | 60 min |

## Mapa do módulo

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m00-module-map.mmd"
```

<figcaption>Figura 1 — Mapa do Módulo 00.</figcaption>
</figure>

## Fio condutor

Todas as aulas voltam à mesma pergunta: **onde está a fronteira, e o que acontece quando algo a atravessa?** Um processo e o kernel, uma VM e o hipervisor, uma VLAN e outra, a rede interna e a internet, o cliente e o provedor de cloud. Segurança de arquitetura é, em grande parte, decidir onde essas fronteiras ficam e como cada travessia é controlada — e isso só é possível quando se entende a tecnologia por baixo delas.

## Atividades

- [Avaliação diagnóstica de fundamentos](../../assessments/diagnostic-fundamentals.md) — Seção A cobre este módulo; faça antes de começar, para identificar lacunas.
- [Laboratório 00 — Plano de endereçamento e segmentação](../../labs/lab-00-network-plan.md) — revisão de um plano de rede com sobreposição de endereços, rede plana e fluxos amplos (1 h 30 min a 2 h, sem custo).
- [Avaliação do Módulo 00](../../assessments/m00-foundations.md) — dez questões situacionais e duas tarefas de análise, com gabarito comentado.
- Exercícios de decisão ao final de cada aula, com resolução de referência.

## Organizações fictícias usadas no módulo

| Organização | Perfil |
|:---|:---|
| **Meridiana Distribuidora** | Distribuidora com três centros de distribuição e datacenter próprio (a mesma do [Caso A](../../case-studies/case-a-meridiana/index.md)). |
| **Lumen Saúde** | Rede de clínicas que está modernizando um sistema de agendamento. |
| **Aurora Pagamentos** | Empresa de meios de pagamento com ambiente híbrido. |

## Referências principais do módulo

- NIST. *SP 800-145 — The NIST Definition of Cloud Computing*. 2011. <https://csrc.nist.gov/pubs/sp/800/145/final>.
- NIST. *SP 800-125 — Guide to Security for Full Virtualization Technologies*. 2011. <https://csrc.nist.gov/pubs/sp/800/125/final>.
- NIST. *SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy*. 2009. <https://csrc.nist.gov/pubs/sp/800/41/r1/final>.
- NIST. *SP 800-190 — Application Container Security Guide*. 2017. <https://csrc.nist.gov/pubs/sp/800/190/final>.
- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020. <https://www.cl.cam.ac.uk/archive/rja14/book.html>.
