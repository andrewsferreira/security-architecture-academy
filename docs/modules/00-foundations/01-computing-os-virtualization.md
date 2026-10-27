---
id: M00-L01
title: "Computação, sistemas operacionais e virtualização"
description: Como CPU, memória, kernel, processos, máquinas virtuais e containers criam fronteiras de isolamento — e o que cada fronteira protege ou deixa de proteger.
domain: infrastructure-foundations
tier: fundamental
status: published
prerequisites: []
objectives:
  - Explicar a separação entre modo kernel e modo usuário e o papel do sistema operacional no isolamento entre processos.
  - Diferenciar hipervisores tipo 1 e tipo 2 e o isolamento oferecido por máquinas virtuais.
  - Comparar o isolamento de containers com o de máquinas virtuais.
  - Identificar as fronteiras de isolamento em um servidor e o impacto de comprometer cada uma.
minutes: 60
sources: [BOOK-ANDERSON-SE3, NIST-SP800-125, NIST-SP800-190]
further_reading: [K8S-SECURITY-OVERVIEW]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M00
---

# Computação, sistemas operacionais e virtualização

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 · M00-L01</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Toda arquitetura, por mais moderna, roda em processadores, memória e sistemas operacionais. A segurança de uma carga de trabalho depende de **fronteiras de isolamento** criadas por essa base: o kernel separa processos, o hipervisor separa máquinas virtuais, namespaces separam containers. Esta aula explica cada fronteira, o que ela protege e o que acontece quando é rompida — conhecimento necessário para avaliar decisões como "colocar dois sistemas no mesmo host" ou "usar containers em vez de VMs".

**Pré-requisitos:** nenhum.

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar a separação entre modo kernel e modo usuário e o papel do sistema operacional no isolamento entre processos.
- Diferenciar hipervisores tipo 1 e tipo 2 e o isolamento oferecido por máquinas virtuais.
- Comparar o isolamento de containers com o de máquinas virtuais.
- Identificar as fronteiras de isolamento em um servidor e o impacto de comprometer cada uma.

## Conceito

### O problema: muitos programas, um só hardware

Um servidor executa dezenas de programas ao mesmo tempo — o banco de dados, o agente de backup, o serviço web, o antivírus. Eles compartilham CPU, memória, disco e rede. Sem algum mecanismo de separação, qualquer programa poderia ler a memória de outro, apagar seus arquivos ou monopolizar o processador. O **sistema operacional** existe, em grande parte, para resolver esse problema: ele intermedeia o acesso ao hardware e decide quem pode fazer o quê.

A **virtualização** e os **containers** são respostas posteriores ao mesmo problema, em escalas diferentes: permitir que cargas de trabalho de donos, criticidades e níveis de confiança diferentes compartilhem infraestrutura física sem interferir umas nas outras.

### Por que isso importa para um arquiteto

Quando duas aplicações compartilham um host, a pergunta de segurança é: **qual é a fronteira entre elas, e quão forte ela é?** A resposta muda radicalmente conforme o caso:

| Cenário | Fronteira entre as cargas | Se um lado for comprometido |
|:---|:---|:---|
| Dois processos no mesmo sistema operacional | Permissões de usuário e mecanismos do kernel | Um atacante com privilégio de administrador no SO alcança ambos. |
| Dois containers no mesmo host | Namespaces, cgroups e políticas do kernel compartilhado | Uma falha no kernel ou uma configuração permissiva pode levar ao host e aos demais containers. |
| Duas VMs no mesmo hipervisor | Hipervisor e extensões de virtualização do processador | O escape de VM é raro, mas tem impacto alto: alcança todas as VMs do host. |
| Dois servidores físicos | Hardware separado; o que os une é a rede | O caminho entre eles é a rede — e a segurança passa a depender de segmentação. |

Nenhuma fronteira é absoluta. Anderson resume o ponto ao tratar de *sandboxing* e virtualização: os mecanismos dependem de hardware e kernel, e canais laterais como Spectre e Meltdown mostraram que até o isolamento entre VMs pode vazar informação (*Security Engineering*, Cap. 6, §6.2.11–6.2.12).

## Fundamentos técnicos

### CPU, memória e privilégio

Processadores modernos executam código em **níveis de privilégio**. O núcleo do sistema operacional — o **kernel** — roda no nível mais privilegiado (modo kernel) e pode acessar todo o hardware. Aplicações rodam em **modo usuário**: não acessam o hardware diretamente e precisam pedir ao kernel, por meio de **chamadas de sistema** (*system calls*), para abrir arquivos, usar a rede ou alocar memória.

A **memória virtual** dá a cada processo a ilusão de ter um espaço de endereçamento só seu. A unidade de gerenciamento de memória (MMU) do processador traduz endereços virtuais em físicos usando tabelas mantidas pelo kernel; um processo não consegue nem endereçar a memória de outro. É essa combinação — privilégio de CPU mais memória virtual — que permite ao kernel ser o **mediador obrigatório** de todo acesso a recursos.

### O sistema operacional como controle de acesso

Sobre essa base, o SO aplica controle de acesso:

- **Identidade de execução:** todo processo roda sob uma conta (usuário humano ou conta de serviço).
- **Permissões:** arquivos, chaves de registro e dispositivos têm listas de quem pode ler, escrever ou executar.
- **Privilégio administrativo:** `root` (Linux) ou administradores locais (Windows) podem alterar praticamente tudo — inclusive as regras de controle de acesso.

Por isso **contas de serviço com privilégio administrativo** são um problema arquitetural recorrente: uma falha no serviço web vira controle total do servidor. Rodar cada serviço com uma conta dedicada e o mínimo de permissões é a aplicação mais básica de *least privilege*.

### Virtualização

Um **hipervisor** permite que vários sistemas operacionais completos — as **máquinas virtuais (VMs)** — compartilhem o mesmo hardware. Cada VM tem seu próprio kernel e acredita estar sozinha na máquina.

| Tipo | Como funciona | Uso típico |
|:---|:---|:---|
| **Tipo 1 (*bare metal*)** | Roda diretamente sobre o hardware; é o componente mais privilegiado do host. | Datacenters e provedores de cloud. |
| **Tipo 2 (*hosted*)** | Roda como aplicação sobre um SO hospedeiro. | Laboratórios e estações de desenvolvimento. |

Extensões de virtualização do processador (Intel VT-x, AMD-V e equivalentes em Arm) permitem ao hipervisor isolar as VMs com apoio do hardware. A interface de gestão do hipervisor — o console que liga, desliga, copia e reconfigura VMs — é tão sensível quanto o próprio hipervisor: quem a controla controla todas as VMs. O NIST SP 800-125 trata segurança de virtualização completa e destaca a proteção do hipervisor e de sua interface de gestão como prioridade.

### Containers

Um **container** empacota uma aplicação com suas bibliotecas e a executa como um conjunto de processos isolados **sobre o kernel do host**. O isolamento vem de mecanismos do kernel:

- **Namespaces** — cada container vê sua própria árvore de processos, interfaces de rede, pontos de montagem e usuários.
- **cgroups** — limitam CPU, memória e outros recursos que o container pode consumir.
- **Filtros e perfis** — seccomp, AppArmor ou SELinux restringem as chamadas de sistema e os acessos permitidos.

Como todos os containers de um host **compartilham o kernel**, uma vulnerabilidade no kernel ou uma configuração permissiva (container privilegiado, montagem do socket do runtime, execução como root sem restrições) pode permitir que um processo escape para o host. Containers são uma excelente unidade de **empacotamento e implantação**; como fronteira de segurança entre cargas de confiança muito diferente, são mais fracos que VMs.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m00-l01-isolation.mmd"
```

<figcaption>Figura 1 — Fronteiras de isolamento entre processos, máquinas virtuais e containers.</figcaption>
</figure>

A figura mostra as três camadas: o hipervisor separa as VMs; dentro da VM 1, o kernel Linux é compartilhado pelos containers A e B; na VM 2, processos são separados apenas por contas e permissões. Ler um diagrama de infraestrutura com essa pergunta em mente — *qual é a fronteira entre estes dois componentes?* — é a habilidade central desta aula.

## Exemplo empresarial

!!! example "Lumen Saúde — onde colocar o novo agendamento online"

    A Lumen Saúde vai expor na internet um sistema de agendamento de consultas. O time de infraestrutura propõe rodá-lo como container no **mesmo host Docker** que hoje executa o sistema interno de prontuários, para aproveitar capacidade ociosa.

    O arquiteto de segurança compara as fronteiras:

    | Opção | Fronteira entre agendamento (exposto) e prontuários (dados de saúde) | Avaliação |
    |:---|:---|:---|
    | A — Mesmo host, containers lado a lado | Kernel compartilhado | Uma falha explorada no agendamento pode alcançar os prontuários pelo host. Risco alto para dados sensíveis. |
    | B — VMs separadas no mesmo cluster de virtualização | Hipervisor | Isolamento muito mais forte; custo marginal de uma VM. |
    | C — VM separada em segmento de rede próprio | Hipervisor + rede | Isolamento de execução e de rede; permite política de firewall entre as duas cargas. |

    **Decisão:** opção C. O custo adicional é pequeno, e a separação de rede será necessária de qualquer forma quando o agendamento consultar a agenda dos médicos — o fluxo passará por um ponto de controle em vez de ocorrer dentro do mesmo kernel.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Contas de serviço | Serviços rodando como `root` ou administrador local | Conta dedicada por serviço, com permissões mínimas |
| Consolidação | Cargas de qualquer criticidade no mesmo host para economizar | Agrupar por nível de confiança e exposição; separar cargas expostas de cargas com dados sensíveis |
| Gestão da virtualização | Console do hipervisor acessível da rede corporativa | Interface de gestão em rede de gestão dedicada, com MFA e registro |
| Containers | Containers privilegiados "porque funcionam" | Execução sem root, sem privilégios extras, com perfis de restrição de chamadas de sistema |
| Atualização | Kernel e hipervisor atualizados quando "der tempo" | Ciclo de correção definido, pois são as fronteiras mais críticas |

## Aplicabilidade: on-premises, cloud e híbrido

| Ambiente | O que muda |
|:---|:---|
| **On-premises** | A organização opera hipervisores, consoles de gestão e hardware; a fronteira entre VMs é responsabilidade dela. |
| **Cloud (IaaS)** | O provedor opera o hipervisor e o hardware; o cliente controla o SO das VMs e as contas. Serviços de "host dedicado" existem para quando política ou licenciamento exigem não compartilhar hardware. |
| **Containers gerenciados e serverless** | O provedor opera também o host do container; o cliente define imagem, permissões e configuração. |
| **Híbrido** | A mesma carga pode ter fronteiras diferentes em cada ambiente — e a política deve exigir o mesmo nível de isolamento, não o mesmo produto. |

## Como especificar e implementar

Requisitos de isolamento devem ser **verificáveis**. Exemplos:

- "Cargas expostas à internet não compartilham sistema operacional com cargas que processam dados classificados como confidenciais."
- "Serviços executam com contas dedicadas, sem privilégio administrativo local; exceções são registradas com prazo."
- "A interface de gestão dos hipervisores só é alcançável a partir da rede de gestão, com autenticação multifator."
- "Containers em produção não executam como root nem em modo privilegiado."

## Trade-offs, limitações e antipadrões

- **Densidade × isolamento.** Containers permitem mais cargas por servidor; VMs isolam melhor. A escolha depende da diferença de confiança entre as cargas, não de preferência tecnológica.
- **Isolamento não é segmentação.** Duas VMs bem isoladas na mesma rede plana continuam se alcançando pela rede.
- **Antipadrão — "é só um container":** tratar containers como se fossem VMs leves, sem restringir privilégios.
- **Antipadrão — hipervisor esquecido:** endurecer as VMs e deixar o console de gestão na rede de usuários.

## Como validar

- Inventariar, por host, quais cargas compartilham kernel ou hipervisor e qual a classificação de cada uma.
- Verificar as contas de execução dos serviços críticos e seus privilégios.
- Conferir de onde a interface de gestão da virtualização é alcançável (teste de conectividade a partir da rede de usuários deve falhar).
- Em plataformas de containers, listar containers privilegiados ou executando como root.

## Como apresentar e justificar

- **Para engenharia:** "O agendamento ficará em VM separada porque a fronteira de kernel compartilhado não é suficiente entre uma carga exposta e dados de saúde."
- **Para gestores:** "Pagamos o custo de uma VM a mais para que uma falha no site de agendamento não dê acesso aos prontuários dos pacientes."

## Checklist de revisão arquitetural

- [ ] Para cada par de cargas no mesmo host, a fronteira de isolamento é conhecida e adequada à diferença de confiança.
- [ ] Serviços rodam com contas dedicadas e sem privilégios administrativos desnecessários.
- [ ] A gestão de hipervisores e orquestradores está isolada, com MFA e registro.
- [ ] Containers de produção não são privilegiados nem executam como root sem justificativa.
- [ ] Kernel, hipervisor e firmware têm ciclo de atualização definido.

## Questões de compreensão

**1.** Por que um processo em modo usuário não consegue ler diretamente a memória de outro processo?

??? success "Resposta comentada"

    Porque cada processo tem seu próprio espaço de endereçamento virtual, traduzido pela MMU segundo tabelas que só o kernel mantém. O processo não tem como endereçar a memória do outro, e o acesso ao hardware exige chamadas de sistema mediadas pelo kernel.

**2.** Qual a diferença essencial de isolamento entre dois containers e duas VMs no mesmo servidor?

??? success "Resposta comentada"

    Containers compartilham o kernel do host; VMs têm kernels próprios, separados pelo hipervisor. Uma falha no kernel compromete todos os containers do host, enquanto comprometer uma VM normalmente exige um escape do hipervisor, que é mais raro.

**3.** Uma equipe diz que os servidores estão seguros porque "todas as VMs estão atualizadas". Que componente pode ter ficado de fora dessa avaliação?

??? success "Resposta comentada"

    O hipervisor e sua interface de gestão. Quem controla o console de virtualização pode desligar, copiar ou reconfigurar qualquer VM — independentemente de como cada VM está configurada.

**4.** Em IaaS, quem responde pelo hipervisor? E pela conta com a qual o serviço web roda dentro da VM?

??? success "Resposta comentada"

    O provedor responde pelo hipervisor e pelo hardware. A conta de execução do serviço web, o sistema operacional da VM e sua configuração são responsabilidade do cliente.

## Exercício de tomada de decisão

!!! question "Cenário: consolidação de servidores na Meridiana"

    A Meridiana quer desligar três servidores físicos antigos e consolidar as cargas em um único host de virtualização novo. As cargas são: (1) o ERP, com dados financeiros; (2) o servidor de etiquetas dos centros de distribuição, que roda um sistema operacional sem suporte do fabricante; (3) o servidor de arquivos dos usuários. O orçamento permite um host, não dois.

    Compare três formas de distribuir as cargas — (A) as três cargas em uma única VM, com um só sistema operacional; (B) uma VM por carga, cada uma em um segmento de rede próprio, com firewall entre eles; (C) uma VM por carga, todas no mesmo segmento de rede — usando como critérios o isolamento do ERP, a contenção do sistema sem suporte e o custo de operação. Depois, indique que controles acrescentar e qual risco permanece.

??? success "Resolução de referência"

    | Critério | Peso | A — Uma VM | B — VMs segmentadas | C — VMs no mesmo segmento |
    |:---|:---|:---|:---|:---|
    | Isolamento do ERP | 3 | 1 | 3 | 2 |
    | Contenção do sistema sem suporte | 3 | 1 | 3 | 1 |
    | Custo de operação | 2 | 3 | 2 | 2 |
    | **Total ponderado** | | **12** | **22** | **13** |

    **Recomendação: B.** A alternativa A economiza administração, mas um comprometimento do sistema sem suporte vira comprometimento do ERP. Na C, as VMs separam os sistemas operacionais, mas o servidor de etiquetas continua alcançando o ERP e o servidor de arquivos pela rede.

    - **Distribuição:** cada carga em uma **VM separada** — nunca o ERP e o servidor de etiquetas no mesmo sistema operacional.
    - **Rede:** cada VM em um segmento próprio, com firewall entre eles; o servidor de etiquetas só alcança o que os coletores e o ERP exigem, por portas específicas.
    - **Gestão:** console do hipervisor em rede de gestão, com MFA.
    - **Risco residual:** um escape de VM a partir do servidor sem suporte alcançaria o ERP no mesmo host. Como a probabilidade é baixa mas o impacto é alto, registrar como exceção com prazo e prever, no orçamento seguinte, um segundo host ou a substituição do sistema de etiquetas.

    O ponto central é que **consolidar hardware não obriga a consolidar sistemas operacionais**, e que a fronteira mais fraca (o sistema sem suporte) deve ser compensada com segmentação.

## Pontos-chave

- O kernel é o mediador obrigatório do acesso ao hardware; privilégio administrativo no SO equivale a controlar tudo o que roda nele.
- VMs têm kernels próprios e são separadas pelo hipervisor; containers compartilham o kernel do host.
- A interface de gestão da virtualização é tão crítica quanto o hipervisor.
- A escolha entre container e VM deve considerar a diferença de confiança entre as cargas, não só eficiência.
- Nenhuma fronteira é absoluta: isolamento de execução se complementa com segmentação de rede.

## Referências

### Fundamentação principal

- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020. Cap. 6 *Access Control*, §6.2 (controles do sistema operacional, pp. 209–226), §6.2.11 *Sandboxing* (p. 224) e §6.2.12 *Virtualisation* (p. 225). <https://www.cl.cam.ac.uk/archive/rja14/book.html> — base para camadas de controle de acesso e limites do isolamento.
- NIST. *SP 800-125 — Guide to Security for Full Virtualization Technologies*. 2011. <https://csrc.nist.gov/pubs/sp/800/125/final> — segurança de hipervisores e de sua gestão. *(Página oficial conferida; conteúdo usado como referência geral.)*

### Leitura complementar

- NIST. *SP 800-190 — Application Container Security Guide*. 2017. <https://csrc.nist.gov/pubs/sp/800/190/final> — riscos específicos de containers, imagens e orquestradores; retomado na L05.
- Kubernetes. *Overview of Cloud Native Security*. <https://kubernetes.io/docs/concepts/security/overview/> — segurança em camadas para workloads em containers.

### Aplicação prática

- Use o exercício de consolidação acima como modelo para revisar qualquer proposta de "aproveitar capacidade ociosa" de um host existente.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
