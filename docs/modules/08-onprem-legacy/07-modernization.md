---
id: M08-L07
title: "Aula 07 — Integração com ambientes modernos e modernização gradual"
public_title: "Módulo 8 — Aula 07 — Integração com ambientes modernos e modernização gradual"
description: Como integrar sistemas on-premises e legados a nuvem, SaaS e serviços modernos com segurança, e como modernizá-los gradualmente — estratégias de migração, padrão strangler fig, camadas anticorrupção e fachadas — sem herdar dívidas de segurança nem criar novos caminhos de ataque.
domain: infrastructure-foundations
tier: architect
status: published
prerequisites: [M08-L05, M08-L06, M07-L07]
objectives:
  - Comparar estratégias de migração (7 Rs) do ponto de vista de segurança.
  - Aplicar o padrão strangler fig com uma fachada que melhora a segurança desde a primeira etapa.
  - Projetar integrações entre legado e serviços modernos sem expor o legado.
  - Planejar a modernização com marcos de redução de risco.
minutes: 75
sources: [FOWLER-STRANGLER-FIG, AWS-MIGRATION-7RS, NIST-SP800-207, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [MS-ENTRA-HYBRID-AUTHN, NIST-SP800-207A, AWS-SRA]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M08
---

# Aula 07 — Integração com ambientes modernos e modernização gradual { #integracao-com-ambientes-modernos-e-modernizacao-gradual }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 8 · Nível 2</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">75 min · ID técnico: M08-L07</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    O legado não desaparece porque a organização decidiu ir para a nuvem: ele precisa conversar com SaaS, APIs e serviços novos — e cada integração é uma oportunidade de expor o que estava protegido apenas por estar isolado. Ao mesmo tempo, substituições completas costumam fracassar. Esta aula combina estratégias de migração e o padrão **strangler fig** para modernizar em etapas, com uma regra de arquitetura: **cada etapa deve deixar o ambiente mais seguro do que estava**.

**Pré-requisitos:** [Sistemas sem suporte](05-unsupported-systems.md), [Protocolos inseguros](06-insecure-protocols.md) e [Implantação progressiva de Zero Trust](../07-zero-trust/07-progressive-deployment.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Comparar estratégias de migração (7 Rs) do ponto de vista de segurança.
- Aplicar o padrão strangler fig com uma fachada que melhora a segurança desde a primeira etapa.
- Projetar integrações entre legado e serviços modernos sem expor o legado.
- Planejar a modernização com marcos de redução de risco.

## Conceito

### As estratégias de migração e seus efeitos de segurança

A AWS descreve sete estratégias de migração — os **7 Rs**. Do ponto de vista de segurança:

| Estratégia | O que é | Efeito de segurança |
|:---|:---|:---|
| **Retire** | Desativar ou arquivar | Elimina superfície; a AWS cita reduzir riscos de componentes sem suporte como caso de uso |
| **Retain** | Manter no ambiente atual | Mantém o risco; exige compensatórios (Aula 05) |
| **Rehost** (*lift and shift*) | Mover sem alterar | Leva vulnerabilidades e configurações junto; ganha controles da nuvem ao redor |
| **Relocate** | Mover em bloco para a versão em nuvem da plataforma | Semelhante ao rehost |
| **Repurchase** | Trocar por outro produto, frequentemente SaaS | Transfere parte da responsabilidade; exige avaliação do fornecedor e integração com a identidade |
| **Replatform** | Mover com otimizações (por exemplo, banco gerenciado) | Elimina parte da operação insegura (sistema operacional, correções) |
| **Refactor** | Redesenhar para cloud-native | Maior oportunidade de segurança, maior custo e risco de projeto |

O guia recomenda, em grandes migrações, preferir rehost, replatform ou relocate e **modernizar depois** — o que, para a segurança, significa planejar desde o início os controles que acompanharão o legado durante esse intervalo.

### O padrão strangler fig

Martin Fowler descreve o **strangler fig** como uma abordagem gradual: funcionalidades novas são construídas ao lado do legado, e o comportamento migra pedaço por pedaço até que o legado possa ser desligado. O texto atribui a Cartwright, Horn e Lewis quatro atividades — entender os resultados desejados, decidir como dividir o problema, entregar as partes e mudar a organização para que isso aconteça de forma contínua — e observa que substituições completas aparentemente simples "na maior parte das vezes" fracassam, enquanto componentes pequenos envolvem menos risco.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m08-l07-strangler.mmd"
```

<figcaption>Figura 1 — Fachada com autenticação moderna roteia cada funcionalidade para o legado ou para o novo serviço; a camada anticorrupção traduz entre eles; o legado encolhe até ser desligado.</figcaption>
</figure>

## Fundamentos técnicos

### A fachada como primeiro ganho de segurança

A fachada (um gateway de API ou proxy) é o primeiro componente do strangler fig — e já traz benefícios antes de qualquer funcionalidade migrar:

| Benefício | Como |
|:---|:---|
| **Autenticação moderna** na frente do legado | A fachada exige o IdP, MFA e postura (Módulo 7), mesmo que o legado só conheça usuário e senha |
| **Ponto único de política e registro** | Todas as chamadas passam por um lugar observável |
| **Ocultação do legado** | O legado deixa de ser alcançável diretamente; fica em segmento isolado (Aula 05) |
| **Proteção de aplicação** | Limites de taxa, validação de entrada e WAF na fachada (Módulo 5 — Aula 02) |

É a aplicação do requisito de rede da SP 800-207 de que recursos não devem ser alcançáveis sem passar por um ponto de aplicação de política (§3.4.1; Módulo 7 — Aula 02).

### Camada anticorrupção

Serviços novos não devem herdar os modelos de dados e os protocolos inseguros do legado. A **camada anticorrupção** traduz entre os dois mundos — e é o lugar de concentrar credenciais e protocolos legados, em vez de espalhá-los por cada serviço novo.

### Integrações sem expor o legado

| Integração | Risco | Padrão recomendado |
|:---|:---|:---|
| SaaS precisa de dados do ERP legado | Abrir o ERP para a internet | Exportação por serviço intermediário que publica só o necessário |
| Serviço em nuvem chama o legado | VPN ampla e confiança implícita | Gateway no datacenter com mTLS e identidade de workload (Módulo 7 — Aula 05) |
| Legado envia arquivos a parceiros | SFTP com conta compartilhada | Gateway de integração com identidade por parceiro (Módulo 4 — Aula 07) |
| Usuários acessam o legado de fora | VPN para a rede | ZTNA ou fachada com autenticação moderna (Módulo 5 — Aula 04) |

### Marcos de redução de risco

Cada etapa da modernização deve ter um marco de segurança mensurável:

| Etapa | Marco |
|:---|:---|
| Fachada em produção | 100% do acesso ao legado pela fachada, com autenticação moderna |
| Isolamento do legado | Legado sem acesso direto de usuários nem de internet |
| Primeiras funcionalidades migradas | Dados sensíveis dessas funcionalidades fora do legado |
| Desligamento | Legado desativado; credenciais e regras removidas |

## Exemplo empresarial

!!! example "Meridiana — o portal de fornecedores e o ERP antigo"

    O ERP da Meridiana tem 15 anos e só aceita autenticação local. O novo portal de fornecedores precisava consultar pedidos e pagamentos. A primeira proposta abria uma conexão do portal em nuvem diretamente ao banco do ERP.

    O arquiteto propôs strangler fig: uma **API de integração** no datacenter como fachada, com mTLS e identidade de workload para o portal, expondo apenas três operações de leitura; o ERP passou para a zona de aplicações sem acesso de usuários fora da fachada e do cliente interno; a camada anticorrupção concentrou a credencial do ERP em um cofre. No segundo semestre, o cadastro de fornecedores migrou para um serviço novo — com dupla aprovação de dados bancários (Módulo 4 — Aula 06) —, e o ERP deixou de ter essa função. Cada etapa foi registrada em ADR com o marco de segurança atingido.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Modernização | Substituição completa ou nada | Strangler fig com marcos |
| Integração com nuvem | Conexão direta ao banco do legado | Fachada com autenticação moderna e operações mínimas |
| Legado durante a transição | Exposto às novas integrações | Isolado atrás da fachada |
| Protocolos e credenciais legados | Espalhados pelos serviços novos | Concentrados na camada anticorrupção |
| Fim | Indefinido | Desligamento com remoção de credenciais e regras |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias para a modernização gradual:

| Controle ou padrão | Objetivo na modernização | Referência |
|:---|:---|:---|
| Arquitetura e princípios | Arquitetura-alvo e de transição descritas; princípios de engenharia aplicados a cada etapa | SP 800-53: PL-8 (Security and Privacy Architectures) e SA-8 (Security and Privacy Engineering Principles) |
| Fachada como fronteira | Legado alcançável só pela fachada, com fluxos controlados | SP 800-53: SC-7 (Boundary Protection) e AC-4 (Information Flow Enforcement) |
| Autenticação de serviços | Serviços novos autenticados pela fachada | SP 800-53: IA-9 (Service Identification and Authentication) |
| Componentes sem suporte | Substituição planejada, com compensatórios durante a transição | SP 800-53: SA-22 (Unsupported System Components) |
| Aquisição e SaaS | Requisitos de segurança no contrato e nos serviços externos | SP 800-53: SA-4 (Acquisition Process) e SA-9 (External System Services); CIS v8.1: Controle 15 (Service Provider Management) |
| Estratégias de migração | Efeito de segurança de cada R | AWS Prescriptive Guidance, 7 Rs |

## Aplicabilidade: on-premises, cloud e híbrido

A modernização gradual é, por definição, híbrida: durante meses ou anos, funcionalidades vivem nos dois lados. O hub de conectividade e a identidade de workload (Módulo 6 — Aula 07, Módulo 11) são o que permite que o legado no datacenter e os serviços em nuvem conversem sem voltar à confiança implícita de rede.

## Como especificar e implementar

- "Integrações novas com sistemas legados ocorrem por fachada com autenticação moderna, operações mínimas e registro."
- "Sistemas legados em modernização ficam isolados; o acesso direto de usuários e de internet é removido."
- "Credenciais e protocolos legados ficam concentrados na camada anticorrupção."
- "Cada etapa de modernização tem marco de segurança mensurável registrado em ADR."
- "O desligamento do legado inclui remoção de credenciais, regras de firewall e integrações."

## Trade-offs, limitações e antipadrões

- **Trade-off:** a fachada adiciona um componente e latência; o ganho de controle e visibilidade costuma compensar.
- **Antipadrão — strangler fig sem fim:** a fachada vira mais uma camada permanente sobre um legado que nunca encolhe.
- **Antipadrão — rehost como modernização:** mover o legado para a nuvem sem compensatórios.
- **Limitação:** algumas funcionalidades são muito acopladas para extração gradual; o padrão exige identificar costuras.

## Como validar

- Verificar se existe algum caminho ao legado que não passe pela fachada.
- Conferir o marco de segurança de cada etapa concluída.
- Após o desligamento, verificar se credenciais e regras foram removidas.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhum caminho ao legado fora da fachada | Varredura e teste de acesso direto, negados |
| Marco de segurança de cada etapa concluída atingido | ADR da etapa com a evidência do marco |
| Credenciais do legado só na camada anticorrupção | Inventário de segredos sem credencial do legado em outros serviços |
| Desligamento com credenciais, regras e integrações removidas | Checklist de desligamento com evidências |

## Como apresentar e justificar

- **Para a diretoria:** "Não vamos trocar o ERP de uma vez — isso costuma dar errado. Cada etapa entrega uma funcionalidade nova e deixa o ERP mais isolado."
- **Para a engenharia:** "O serviço novo nunca fala direto com o banco do ERP; fala com a API de integração."

## Checklist de revisão arquitetural

- [ ] Estratégia de migração escolhida por aplicação, com efeito de segurança considerado.
- [ ] Fachada com autenticação moderna antes de qualquer integração nova.
- [ ] Legado isolado durante a transição.
- [ ] Camada anticorrupção para credenciais e protocolos legados.
- [ ] Marcos de segurança por etapa e plano de desligamento.

## Questões de compreensão

**1.** Por que a fachada já melhora a segurança antes de qualquer funcionalidade migrar?

??? success "Resposta comentada"

    Porque passa a exigir autenticação moderna, concentra política e registro em um ponto e permite isolar o legado, que deixa de ser alcançável diretamente.

**2.** Qual o risco de segurança do rehost?

??? success "Resposta comentada"

    Levar para a nuvem as vulnerabilidades, configurações e protocolos legados sem alterá-los. Se for a estratégia escolhida, os compensatórios precisam acompanhar o sistema.

**3.** Para que serve a camada anticorrupção do ponto de vista de segurança?

??? success "Resposta comentada"

    Para concentrar as credenciais e os protocolos legados em um único componente, impedindo que os serviços novos herdem esses riscos.

## Exercício de tomada de decisão

!!! question "Cenário: sistema de faturamento da Lumen"

    O sistema de faturamento da Lumen (o mesmo do bind LDAP em claro, Módulo 6 — Aula 03) precisa ser integrado ao novo portal do paciente para exibir boletos. O fornecedor oferecerá uma versão SaaS em 18 meses. As opções são:

    - **A** — *retain* com fachada: API de integração no datacenter até a migração para o SaaS;
    - **B** — *rehost* do faturamento na nuvem agora, com integração direta ao portal;
    - **C** — o portal consulta diretamente o banco do faturamento até o SaaS.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e proponha a estratégia de migração e a integração até lá.

**Objetivos avaliados:** Aplicar o padrão strangler fig com uma fachada que melhora a segurança desde a primeira etapa; projetar integrações entre legado e serviços modernos sem expor o legado.

**Entrega esperada:** Matriz ponderada e a estratégia de migração com a integração provisória, o isolamento e os marcos.

**Critérios de avaliação:**

- A integração isola o legado atrás de uma fachada com autorização por objeto.
- A estratégia combina o tratamento provisório com o destino (SaaS) e marcos de remoção do acesso direto.
- O risco residual do legado durante o período é declarado e limitado.

??? success "Resolução de referência"

    | Critério | Peso | A — Retain com fachada | B — Rehost agora | C — Portal direto no banco |
    |:---|:---|:---|:---|:---|
    | Exposição do legado e dos dados | 3 | 3 | 2 | 1 |
    | Autorização por objeto (cada paciente vê só os próprios boletos) | 3 | 3 | 2 | 1 |
    | Esforço e custo até o SaaS | 2 | 2 | 1 | 3 |
    | Reuso na migração para o SaaS | 1 | 3 | 1 | 1 |
    | **Total ponderado** | | **25** | **15** | **13** |

    - **Pesos:** boletos são dados pessoais e financeiros de pacientes — exposição e autorização por objeto pesam 3. Esforço pesa 2, porque a solução vale por 18 meses. O reuso pesa 1.
    - **Recomendação: A.** A fachada isola o legado, concentra a autorização por objeto e depois aponta para o SaaS sem mudar o portal. B gasta uma migração em um sistema que será substituído e leva junto o bind LDAP em claro; C abre o banco ao portal e espalha a regra de autorização.

    - **Estratégia:** **retain** com compensatórios por 18 meses e **repurchase** (SaaS) depois, com avaliação de segurança do fornecedor e federação com o IdP.
    - **Integração até lá:** API de integração no datacenter como fachada, com mTLS e identidade de workload para o portal, expondo apenas a operação "boletos do paciente" com autorização por objeto (o paciente só vê os próprios boletos).
    - **Isolamento:** faturamento acessível apenas pela fachada e pelos usuários internos via ZTNA; tráfego LDAP isolado e cifrado conforme a Aula 03 do Módulo 6.
    - **Marcos:** fachada em produção; acesso direto removido; migração para SaaS com desligamento do sistema antigo e remoção de credenciais e regras.
    - **Trade-off aceito e risco residual:** o legado continua com suas vulnerabilidades e com o bind LDAP tratado por compensatório durante 18 meses; a fachada é um componente novo a operar. O residual é o comprometimento do servidor do faturamento por usuário interno, limitado pelo ZTNA e pela monitoração.
    - **O que mudaria a decisão:** atraso do SaaS para além de 18 meses ou fim de suporte do sistema atual antes disso tornaria a modernização própria (*replatform* ou *refactor* de partes) uma opção a avaliar; se o SaaS chegar antes, a fachada passa a ser apenas a camada de integração com ele.

    **Erros comuns:**

    - Migrar para a nuvem um sistema que será substituído, levando junto suas fragilidades.
    - Dar ao portal acesso direto ao banco do legado.
    - Não planejar o desligamento e a remoção de credenciais e regras ao fim da migração.

## Pontos-chave

- Escolha a estratégia de migração considerando o efeito de segurança de cada R.
- Strangler fig moderniza em etapas e reduz o risco de projeto.
- A fachada traz autenticação moderna e isolamento desde o início.
- A camada anticorrupção concentra credenciais e protocolos legados.
- Cada etapa tem marco de segurança; o fim inclui desligamento e limpeza.

<!-- next-steps:start -->

!!! tip "Próximos passos"

    Você concluiu a última aula do **Módulo 8** — [voltar ao módulo](index.md).

<!-- next-steps:end -->

## Referências

### Fundamentação principal

- M. Fowler. *Strangler Fig*. 2024. <https://www.martinfowler.com/bliki/StranglerFigApplication.html>. *(Lido.)*
- AWS. *About the migration strategies (7 Rs)* — Prescriptive Guidance. <https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html>. *(Lido.)*
- NIST. *SP 800-207* — §3.4.1, recursos alcançáveis apenas via PEP. *(Lido.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-4, IA-9, PL-8, SA-4, SA-8, SA-9, SA-22 e SC-7, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controle 15 — gratuito.

### Leitura complementar

- Microsoft. *Authentication for Microsoft Entra hybrid identity*.
- NIST. *SP 800-207A*.
- AWS. *Security Reference Architecture*.

### Aplicação prática

- Escolha um sistema legado da sua organização e escreva o plano strangler fig: a fachada, as três primeiras funcionalidades a migrar e o marco de segurança de cada etapa.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
