---
id: M00-L06
title: "Cloud computing: modelos de serviço e de implantação"
description: A definição de cloud computing do NIST — características essenciais, IaaS, PaaS, SaaS e modelos de implantação — e como cada modelo redistribui responsabilidades de segurança entre cliente e provedor.
domain: cloud-security
tier: fundamental
status: published
prerequisites: [M00-L04, M00-L05]
objectives:
  - Enunciar as cinco características essenciais de cloud computing segundo o NIST SP 800-145.
  - Diferenciar IaaS, PaaS e SaaS quanto ao que o cliente controla.
  - Diferenciar nuvem pública, privada, comunitária e híbrida.
  - Explicar o modelo de responsabilidade compartilhada e identificar o que nunca deixa de ser do cliente.
minutes: 60
sources: [NIST-SP800-145, AWS-SECURITY-PILLAR, CSA-GUIDANCE-V5]
further_reading: [AZURE-WAF-SECURITY, GCP-ENTERPRISE-FOUNDATIONS]
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
module: M00
---

# Cloud computing: modelos de serviço e de implantação

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 · M00-L06</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    "Ir para a cloud" pode significar coisas muito diferentes: alugar máquinas virtuais, usar um banco de dados gerenciado ou contratar um sistema pronto. Cada escolha muda **quem é responsável por quê**. Esta aula usa a definição do NIST — ainda a referência mais citada — para organizar o vocabulário e mostra o ponto mais importante para a segurança: dados, identidades e configuração **nunca** deixam de ser responsabilidade do cliente.

**Pré-requisitos:** [Datacenters e alta disponibilidade](04-datacenter-high-availability.md) e [Containers, APIs e serverless](05-containers-apis-serverless.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Enunciar as cinco características essenciais de cloud computing segundo o NIST SP 800-145.
- Diferenciar IaaS, PaaS e SaaS quanto ao que o cliente controla.
- Diferenciar nuvem pública, privada, comunitária e híbrida.
- Explicar o modelo de responsabilidade compartilhada e identificar o que nunca deixa de ser do cliente.

## Conceito

### A definição do NIST

O NIST SP 800-145 (2011) define cloud computing como um modelo de acesso sob demanda, pela rede, a um conjunto compartilhado de recursos configuráveis, provisionados e liberados rapidamente com mínimo esforço de gestão. A definição tem três partes (seção 2, pp. 2–3):

**Cinco características essenciais**

| Característica | Significado | Consequência para segurança |
|:---|:---|:---|
| *On-demand self-service* | O cliente provisiona recursos sozinho, sem pedir ao provedor | Qualquer pessoa com permissão cria infraestrutura — inclusive insegura. Governança precisa ser automática. |
| *Broad network access* | Recursos acessíveis pela rede, de vários tipos de dispositivo | As interfaces de gestão estão na internet; a identidade vira o perímetro. |
| *Resource pooling* | Recursos compartilhados entre clientes (*multi-tenancy*) | O isolamento entre clientes é responsabilidade do provedor; o cliente precisa confiar e verificar. |
| *Rapid elasticity* | Capacidade cresce e diminui rapidamente | O inventário muda a cada minuto; controles manuais não acompanham. |
| *Measured service* | Uso medido e cobrado | Abuso de recursos (por exemplo, mineração de criptomoeda com credenciais vazadas) vira custo direto. |

**Três modelos de serviço:** IaaS, PaaS e SaaS.

**Quatro modelos de implantação:** nuvem privada, comunitária, pública e híbrida.

### Por que essa definição ainda importa

A lista de serviços dos provedores mudou completamente desde 2011, mas as características continuam explicando por que a segurança em cloud é diferente: tudo é programável, tudo é acessível pela rede e tudo muda rápido. Os controles precisam acompanhar essas três propriedades.

## Fundamentos técnicos

### Modelos de serviço

| Modelo | O cliente recebe | O cliente controla | Exemplos de categoria |
|:---|:---|:---|:---|
| **IaaS** | Capacidade de computação, armazenamento e rede | Sistema operacional, aplicações, rede virtual, dados | Máquinas virtuais, redes virtuais, discos |
| **PaaS** | Plataforma para implantar aplicações | Aplicação, configuração da plataforma, dados | Bancos gerenciados, plataformas de aplicação, serverless |
| **SaaS** | Aplicação pronta | Configuração do serviço, usuários, dados | E-mail, CRM, colaboração |

Na prática, os limites são difusos — um banco gerenciado é PaaS, mas o cliente ainda escolhe a rede, a cifragem e quem acessa. O valor da classificação é perguntar, em cada serviço: **o que eu configuro?**

### Modelos de implantação

| Modelo | Infraestrutura usada por | Observação |
|:---|:---|:---|
| **Privada** | Uma única organização | Pode ser operada pela própria organização ou por terceiros, no local ou fora dele. Virtualização sem autosserviço e elasticidade não é nuvem privada segundo a definição. |
| **Comunitária** | Um grupo de organizações com interesses comuns | Ex.: nuvens setoriais, governamentais. |
| **Pública** | O público em geral | Operada por um provedor. |
| **Híbrida** | Composição de duas ou mais das anteriores | Unidas por tecnologia que permite portabilidade de dados e aplicações. |

O termo **multicloud**, comum hoje, não aparece na definição de 2011: descreve o uso de mais de um provedor público, com ou sem integração entre eles. É tratado no M11.

### Responsabilidade compartilhada

O **modelo de responsabilidade compartilhada** divide a segurança entre provedor e cliente. A AWS, no Security Pillar, resume a ideia: como o provedor protege fisicamente a infraestrutura que sustenta os serviços, o cliente pode concentrar-se em usar os serviços para atingir seus objetivos — mas continua responsável por como os usa.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m00-l06-shared-responsibility.mmd"
```

<figcaption>Figura 1 — Divisão de responsabilidades por modelo de serviço. Contorno azul: cliente; contorno ciano: provedor.</figcaption>
</figure>

A leitura da figura de cima para baixo mostra o padrão: à medida que se passa de IaaS para SaaS, o provedor assume mais camadas. Mas a primeira linha não muda: **dados, identidades e acessos são sempre do cliente**. Incidentes de cloud amplamente divulgados envolvem com frequência justamente essas camadas — buckets públicos, chaves de acesso vazadas, permissões excessivas —, e não falhas na parte operada pelo provedor.

## Exemplo empresarial

!!! example "Lumen Saúde — três formas de "ir para a cloud" o agendamento"

    | Opção | Modelo | O que a Lumen continua fazendo |
    |:---|:---|:---|
    | Mover a VM atual para IaaS | IaaS | Corrigir o SO, configurar firewall da VM e rede virtual, proteger o banco, gerenciar contas, backup |
    | Reescrever em plataforma gerenciada com banco gerenciado | PaaS | Proteger o código, configurar rede e cifragem do banco, gerenciar identidades e acessos |
    | Contratar um sistema de agendamento SaaS | SaaS | Configurar o serviço, gerenciar usuários (idealmente federados ao IdP corporativo), avaliar o fornecedor, definir o que fazer com os dados ao fim do contrato |

    Em todas as opções, a Lumen continua respondendo pela proteção dos dados de pacientes perante a legislação. Mudar de modelo muda o **trabalho**, não a **responsabilidade** pelos dados.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Mentalidade | "O provedor cuida da segurança" | Responsabilidades mapeadas por serviço, com dono interno para cada uma |
| Provisionamento | Cada equipe cria recursos como quiser | Autosserviço com guardrails automáticos (políticas, contas separadas) |
| Identidade | Contas locais em cada serviço | Identidade federada a partir do IdP corporativo |
| Inventário | Planilha atualizada manualmente | Inventário consultado diretamente nas APIs do provedor |

## Aplicabilidade: on-premises, cloud e híbrido

| Ambiente | Ponto de atenção |
|:---|:---|
| **On-premises tradicional** | Toda a pilha é do cliente; a "nuvem privada" só existe com autosserviço e elasticidade de fato. |
| **Cloud pública** | Responsabilidade compartilhada; controles programáveis e automação são a regra. |
| **Híbrido** | Cada parte da arquitetura tem uma divisão diferente de responsabilidades — documentá-la evita lacunas onde "cada lado achava que era do outro". |

## Como especificar e implementar

- "Para cada serviço de cloud contratado, a matriz de responsabilidade identifica as camadas sob responsabilidade da organização e o dono interno de cada uma."
- "Acesso administrativo a provedores de cloud usa identidade federada com MFA; contas locais administrativas são proibidas, exceto contas de emergência controladas."
- "Recursos de cloud são criados a partir de contas, projetos ou assinaturas governados por políticas preventivas."

## Trade-offs, limitações e antipadrões

- **Menos operação, mais dependência.** SaaS reduz trabalho, mas aumenta a dependência do fornecedor e reduz o controle sobre logs, localização dos dados e mudanças.
- **Elasticidade sem governança gera custo e exposição.**
- **Antipadrão — *lift and shift* sem revisão:** levar a VM para IaaS e manter senhas fracas, SO desatualizado e portas abertas, agora acessíveis de qualquer lugar.
- **Antipadrão — confiar em certificações do provedor como se cobrissem a configuração do cliente.**

## Como validar

- Para cada serviço, conferir a matriz de responsabilidade e se existe dono interno para cada camada do cliente.
- Verificar se o acesso administrativo ao console do provedor exige identidade federada e MFA.
- Consultar, pelas APIs ou ferramentas do provedor, recursos públicos, chaves de acesso antigas e permissões amplas.

## Como apresentar e justificar

- **Para engenharia:** "Escolher PaaS elimina a correção do sistema operacional, mas continuamos responsáveis por rede, cifragem e acesso ao banco."
- **Para gestores:** "A cloud reduz o trabalho de manter servidores, mas não transfere a responsabilidade pelos dados dos pacientes. O provedor cuida do prédio; nós cuidamos das chaves."

## Checklist de revisão arquitetural

- [ ] O modelo de serviço de cada componente está identificado.
- [ ] As responsabilidades do cliente estão mapeadas e têm dono.
- [ ] Dados, identidades e configuração têm controles definidos em todos os modelos.
- [ ] O provisionamento é governado por políticas automáticas.
- [ ] O plano de saída (dados e contrato) está definido para serviços SaaS críticos.

## Questões de compreensão

**1.** Uma empresa virtualizou seu datacenter, mas novos servidores levam três semanas para serem entregues após aprovação. É uma nuvem privada segundo o NIST?

??? success "Resposta comentada"

    Não. Faltam características essenciais, como o autosserviço sob demanda e a elasticidade rápida. Virtualização é uma tecnologia; nuvem é um modelo de entrega com características específicas.

**2.** O que permanece responsabilidade do cliente em todos os modelos de serviço?

??? success "Resposta comentada"

    Os dados, as identidades e os acessos, e a configuração dos serviços que ele usa.

**3.** Por que a característica *on-demand self-service* tem impacto de segurança?

??? success "Resposta comentada"

    Porque qualquer pessoa com permissão pode criar infraestrutura instantaneamente, inclusive mal configurada. Controles manuais de aprovação não acompanham; a governança precisa ser automática (políticas preventivas e detecção contínua).

## Exercício de tomada de decisão

!!! question "Cenário: e-mail corporativo da Meridiana"

    O servidor de e-mail da Meridiana roda em um servidor próprio, sem atualização há meses, administrado por uma pessoa que deixará a empresa. A diretoria quer saber se vale migrar para um serviço SaaS. Compare (A) manter o servidor próprio, contratando suporte externo para atualizá-lo; (B) migrar para SaaS, com usuários federados ao diretório, MFA e configuração revisada; (C) migrar o servidor como VM para IaaS (*lift and shift*), pelos critérios redução de risco, dependência de pessoas internas e custo da migração. Para a alternativa escolhida, liste o que a Meridiana deixaria de fazer, o que continuaria fazendo e o principal risco novo.

??? success "Resolução de referência"

    | Critério | Peso | A — Servidor próprio com suporte externo | B — SaaS com federação e MFA | C — *Lift and shift* para IaaS |
    |:---|:---|:---|:---|:---|
    | Redução de risco | 3 | 1 | 3 | 1 |
    | Dependência de pessoas internas | 2 | 1 | 3 | 1 |
    | Custo da migração | 1 | 3 | 2 | 2 |
    | **Total ponderado** | | **8** | **17** | **7** |

    **Recomendação: B.** A alternativa C muda o servidor de lugar sem mudar o problema: o software desatualizado continua sob responsabilidade da Meridiana, agora em outra infraestrutura.

    - **Deixaria de fazer:** manter hardware, sistema operacional e software de e-mail, aplicar correções, garantir disponibilidade da infraestrutura.
    - **Continuaria fazendo:** gerenciar usuários e grupos (idealmente federados ao diretório), configurar MFA, políticas de retenção, regras antiphishing e encaminhamento, monitorar acessos e configurar a proteção dos dados.
    - **Risco novo:** dependência do fornecedor e da configuração do serviço — uma conta administrativa do SaaS sem MFA, por exemplo, expõe todas as caixas de correio pela internet.

    Para uma empresa sem capacidade de manter o servidor, a migração tende a **reduzir** o risco total — desde que identidade e configuração recebam a atenção que antes ia para o servidor.

## Pontos-chave

- O NIST SP 800-145 define cloud por cinco características essenciais, três modelos de serviço e quatro modelos de implantação.
- Cada característica tem consequência de segurança: autosserviço, acesso pela rede, multi-tenancy, elasticidade e medição.
- Quanto mais alto o modelo de serviço, mais camadas o provedor assume.
- Dados, identidades, acessos e configuração são sempre do cliente.
- Mudar de modelo muda o trabalho, não a responsabilidade pelos dados.

## Referências

### Fundamentação principal

- P. Mell e T. Grance. *SP 800-145 — The NIST Definition of Cloud Computing*. NIST, 2011. Seção 2, pp. 2–3. <https://csrc.nist.gov/pubs/sp/800/145/final> — características essenciais, modelos de serviço e de implantação.
- AWS. *Security Pillar — AWS Well-Architected Framework*. 2024; seção *Definition*. <https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html> — modelo de responsabilidade compartilhada e áreas de boas práticas.
- Cloud Security Alliance. *Security Guidance for Critical Areas of Focus in Cloud Computing v5*. 2024. <https://cloudsecurityalliance.org/artifacts/security-guidance-v5> — domínio 1, *Cloud Computing Concepts and Architectures*. *(Domínios conferidos; texto não lido.)*

### Leitura complementar

- Microsoft. *Azure Well-Architected Framework — Security*. <https://learn.microsoft.com/en-us/azure/well-architected/security/>.
- Google Cloud. *Enterprise foundations blueprint*. <https://docs.cloud.google.com/architecture/blueprints/security-foundations> — como organizar uma fundação de cloud com guardrails desde o início.

### Aplicação prática

- Monte a matriz de responsabilidade dos serviços de cloud que sua organização usa, uma linha por camada, com o dono interno de cada uma.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
