---
id: M03-L02
title: "Aula 02 — NIST Risk Management Framework (SP 800-37)"
public_title: "Módulo 3 — Aula 02 — NIST Risk Management Framework (SP 800-37)"
description: O ciclo de vida do RMF — Prepare, Categorize, Select, Implement, Assess, Authorize e Monitor —, os papéis que ele exige, a fronteira de autorização, a herança de controles comuns e como adaptar o raciocínio a organizações fora do governo federal dos Estados Unidos.
domain: grc
tier: professional
status: published
prerequisites: [M03-L01]
objectives:
  - Descrever as sete etapas do RMF e o produto de cada uma.
  - Explicar os papéis de authorizing official e risk executive (function) e por que a autorização é uma decisão de risco.
  - Definir fronteira de autorização e controles comuns herdáveis.
  - Adaptar o RMF a uma organização privada sem transformá-lo em burocracia.
minutes: 75
sources: [NIST-SP800-37-R2, NIST-RMF, NIST-SP800-30-R1]
further_reading: [NIST-SP800-53, NIST-SP800-53B, NIST-CSF-2]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M03
---

# Aula 02 — NIST Risk Management Framework (SP 800-37) { #nist-risk-management-framework-sp-800-37 }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 3 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M03-L02</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    O CSF diz **quais resultados** a organização busca; o Risk Management Framework (RMF) descreve **como um sistema chega à produção** com riscos conhecidos e aceitos por quem tem autoridade. O RMF foi escrito para o governo federal dos Estados Unidos, mas seu raciocínio — categorizar, selecionar controles proporcionais, implementar, avaliar com independência, autorizar conscientemente e monitorar — é diretamente aplicável à arquitetura de qualquer organização. Esta aula apresenta as etapas, os papéis e os conceitos de fronteira de autorização e herança de controles.

**Pré-requisito:** [Governança de segurança e o NIST CSF 2.0](01-governance-csf.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Descrever as sete etapas do RMF e o produto de cada uma.
- Explicar os papéis de authorizing official e risk executive (function) e por que a autorização é uma decisão de risco.
- Definir fronteira de autorização e controles comuns herdáveis.
- Adaptar o RMF a uma organização privada sem transformá-lo em burocracia.

## Conceito

### O problema que o RMF resolve

Em muitas organizações, sistemas entram em produção porque "a data chegou". A segurança aparece como uma revisão no fim, os achados viram exceções sem dono e ninguém consegue dizer, depois de dois anos, por que um sistema crítico foi aceito com determinada fraqueza. O RMF responde a isso com três ideias:

1. **Proporcionalidade:** os controles dependem do impacto que a perda de confidencialidade, integridade ou disponibilidade causaria.
2. **Separação de funções:** quem implementa não é quem avalia, e quem avalia não é quem aceita o risco — com um grau de independência do avaliador proporcional ao impacto do sistema, decidido pela organização.
3. **Decisão explícita:** um sistema só opera depois que alguém com autoridade **aceita o risco residual**, com base em evidências — e essa decisão é revista quando o contexto muda.

### As sete etapas

A SP 800-37 Rev. 2, de dezembro de 2018, descreve uma etapa preparatória e seis etapas principais (Sec. 2.2, pp. 9–10):

| Etapa | Pergunta | Produto típico |
|:---|:---|:---|
| **Prepare** | A organização e o sistema estão prontos para gerenciar risco? | Papéis, estratégia de risco, controles comuns, fronteira do sistema |
| **Categorize** | Qual o impacto da perda de C, I e D deste sistema e de suas informações? | Categoria de segurança documentada |
| **Select** | Que controles reduzem o risco a um nível aceitável? | Baseline ajustada (tailoring) e plano de segurança |
| **Implement** | Os controles estão implantados e documentados? | Controles em operação e descrição de como foram implementados |
| **Assess** | Os controles foram implementados corretamente e produzem o resultado esperado? | Relatório de avaliação e deficiências |
| **Authorize** | O risco residual é aceitável? | Decisão de autorização e plano de ação para deficiências |
| **Monitor** | O sistema continua dentro do risco aceito? | Monitoração de controles, mudanças e postura |

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m03-l02-rmf-cycle.mmd"
```

<figcaption>Figura 1 — Etapas do RMF, com realimentação a partir da monitoração e do plano de ação para deficiências.</figcaption>
</figure>

## Fundamentos técnicos

### Prepare: o que muitas organizações pulam

A etapa Prepare existe nos níveis da organização e do sistema. No nível da organização, a Tabela 1 da Sec. 3.1 (pp. 12–13) lista tarefas como definir papéis de gestão de riscos (P-1), a estratégia de gestão de riscos (P-2), a avaliação de riscos da organização (P-3), baselines ajustadas pela organização e perfis CSF (P-4, opcional), a identificação de controles comuns (P-5), a priorização por nível de impacto (P-6, opcional) e a estratégia de monitoração contínua (P-7).

Para o arquiteto, duas tarefas têm efeito direto na arquitetura:

- **Controles comuns (P-5):** controles fornecidos uma vez e **herdados** por muitos sistemas — identidade corporativa, logging central, landing zone de cloud, proteção física do datacenter. Bem desenhados, eles reduzem o custo de cada novo sistema; mal documentados, criam a ilusão de que "a plataforma cuida disso".
- **Fronteira:** a SP 800-37 usa **authorization boundary** para o conjunto de elementos do sistema que está sendo autorizado (nota 36, p. 16). Definir a fronteira é uma decisão de arquitetura: o que está dentro herda a decisão de autorização; o que está fora precisa de interface controlada.

### Categorize

A categorização expressa o **impacto** — baixo, moderado ou alto — da perda de cada propriedade para as informações e o sistema. Ela guia a seleção da baseline (Aula 03). Dois erros comuns:

- Categorizar pela **tecnologia** ("é só um servidor web") em vez de pelo **impacto no negócio**.
- Categorizar tudo como alto "por segurança", o que torna a baseline cara e as exceções inevitáveis.

### Assess e Authorize: separação de funções

O **avaliador** verifica se cada controle foi implementado corretamente, opera como pretendido e produz o resultado desejado. O **authorizing official** — um executivo com autoridade e responsabilidade sobre a missão — decide se aceita o risco residual em nome da organização. A SP 800-37 descreve autorizações para **operar** ou **usar** um sistema e autorizações de **controles comuns** que outros sistemas herdam. Quando a decisão é negativa, o sistema volta à seleção ou implementação; quando é positiva com deficiências, elas entram em um **plano de ação com marcos**, cada uma com prazo.

A **risk executive (function)** conecta as decisões de sistemas à visão de risco da organização, para que dez autorizações aceitáveis individualmente não somem um risco inaceitável.

### Monitor e autorização contínua

A Rev. 2 dá prioridade à transição para a **autorização contínua** (*ongoing authorization*) (Sumário Executivo, p. viii): em vez de reautorizar periodicamente com uma pilha de documentos, a organização monitora os controles e as mudanças continuamente e revisita a decisão quando algo relevante muda. Isso só funciona se houver telemetria confiável — tema de [Aula 08](08-metrics-maturity-reporting.md) e do Módulo 15.

## Exemplo empresarial

!!! example "Lumen Saúde — RMF leve para o portal do paciente"

    A Lumen adaptou o RMF para lançar o portal do paciente, sem a carga documental do governo norte-americano:

    | Etapa | O que a Lumen fez |
    |:---|:---|
    | Prepare | Diretor clínico nomeado como dono do risco do portal; identidade, logging e landing zone declarados como controles comuns herdados, com responsável na equipe de plataforma |
    | Categorize | Confidencialidade alta (dados de saúde), integridade alta (laudos), disponibilidade moderada (há canal alternativo por telefone) |
    | Select | Baseline interna "alta-C/alta-I", com tailoring documentado em uma página |
    | Implement | Controles implementados como código na pipeline |
    | Assess | Avaliação pela equipe de segurança de aplicações, independente do time do portal |
    | Authorize | Diretor clínico autorizou com duas deficiências no plano de ação: rate limiting da API em 30 dias e teste de restauração em 60 dias |
    | Monitor | Painel com cobertura de controles e mudanças; qualquer nova integração com laboratório volta à categorização |

    O processo inteiro levou três semanas e gerou oito documentos curtos, rastreáveis até a decisão.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Momento | Revisão de segurança no fim | Categorização e seleção no desenho |
| Quem aceita o risco | Ninguém — ou o próprio time | Executivo com autoridade sobre a missão |
| Controles de plataforma | Assumidos sem documentação | Controles comuns declarados e herdados formalmente |
| Deficiências | Exceções sem prazo | Plano de ação com marcos |
| Reavaliação | A cada N anos | Autorização contínua orientada a mudanças |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, a herança de controles é explícita: o provedor implementa controles físicos e de infraestrutura, a landing zone corporativa implementa outros, e o workload implementa o restante. Um bom pacote de autorização mostra essas três camadas. Em ambientes híbridos, a fronteira de autorização precisa decidir se o conector entre ambientes (VPN, link dedicado, agente de sincronização de identidade) está dentro do sistema ou é um controle comum de outro dono — deixar isso indefinido é uma fonte frequente de lacunas.

## Como especificar e implementar

- "Todo sistema novo ou com mudança relevante passa por categorização de impacto antes da seleção de controles."
- "Controles comuns são documentados uma vez, com dono e evidência, e herdados formalmente pelos sistemas."
- "A avaliação de controles é feita por equipe independente da que implementou."
- "A entrada em produção exige decisão registrada do dono do risco; deficiências têm prazo no plano de ação."
- "Mudanças que alteram a fronteira, a categoria ou controles comuns disparam reavaliação."

## Trade-offs, limitações e antipadrões

- **Trade-off:** rigor versus velocidade. A adaptação proporcional — pacotes curtos para sistemas de impacto baixo — evita que o RMF vire gargalo.
- **Antipadrão — autorização de papel:** documentos extensos que ninguém lê, assinados sem entendimento do risco.
- **Antipadrão — herança presumida:** "está na cloud, então a criptografia é do provedor", sem verificar configuração.
- **Limitação:** o RMF não substitui threat modeling (Módulo 4); ele diz quando e como decidir, não quais ameaças analisar.

## Como validar

- Para um sistema autorizado, pedir a categorização, o conjunto de controles com justificativas, o relatório de avaliação e a decisão do dono do risco.
- Conferir se cada controle herdado tem um dono e uma evidência vigente.
- Verificar se as deficiências do plano de ação estão dentro do prazo.
- Escolher uma mudança recente e verificar se ela disparou reavaliação.

## Como apresentar e justificar

- **Para executivos:** "Antes de entrar em produção, o dono do processo decide se aceita o risco que sobra. Nós entregamos a ele a evidência para decidir, não a decisão pronta."
- **Para engenharia:** "Se vocês usarem a plataforma padrão, herdam 40% dos controles já avaliados. Só precisam evidenciar os do próprio sistema."

## Checklist de revisão arquitetural

- [ ] A fronteira de autorização está desenhada e inclui conectores entre ambientes.
- [ ] A categorização se baseia em impacto no negócio, não em tecnologia.
- [ ] Controles comuns estão documentados, com dono, e a herança é explícita.
- [ ] Avaliador e implementador são independentes.
- [ ] O dono do risco registrou a decisão; deficiências têm prazo.
- [ ] Há gatilhos de reavaliação para mudanças relevantes.

## Questões de compreensão

**1.** Por que o RMF separa avaliador e authorizing official?

??? success "Resposta comentada"

    Porque são decisões de natureza diferente. O avaliador responde a uma pergunta técnica — o controle funciona? O authorizing official responde a uma pergunta de negócio — o risco que sobra é aceitável para a missão? Misturar os papéis faz com que o risco seja aceito por quem não responde pelas consequências.

**2.** O que é um controle comum e qual o risco de documentá-lo mal?

??? success "Resposta comentada"

    É um controle implementado uma vez e herdado por vários sistemas, como a identidade corporativa ou o logging central. Mal documentado, cada sistema presume que está protegido sem que ninguém verifique se a configuração realmente cobre o seu caso.

**3.** O que muda com a autorização contínua?

??? success "Resposta comentada"

    A decisão deixa de ser um evento periódico baseado em documentos e passa a ser revista a partir de monitoração e de mudanças. Exige telemetria confiável sobre controles e gatilhos claros de reavaliação.

## Exercício de tomada de decisão

!!! question "Cenário: o conector de identidade da Meridiana"

    A Meridiana vai autorizar o novo portal de fornecedores, hospedado em cloud. O portal autentica usuários pelo diretório corporativo, sincronizado do Active Directory on-premises por um agente instalado em um servidor do datacenter. A equipe do portal quer declarar o agente "fora da fronteira". Outros dois sistemas em cloud vão usar a mesma sincronização no próximo ano. As opções são:

    - **A** — deixar o agente fora da fronteira, sem outro tratamento (proposta da equipe do portal);
    - **B** — incluir o agente e o servidor que o hospeda na fronteira de autorização do portal, sob responsabilidade da equipe do portal;
    - **C** — declarar a identidade corporativa (diretório, agente e servidor) como controle comum, de responsabilidade da equipe de identidade, herdado formalmente pelo portal.

    Você concorda com a equipe do portal? Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho) e proponha a decisão de arquitetura e de responsabilidade.

??? success "Resolução de referência"

    | Critério | Peso | A — Fora da fronteira | B — Dentro da fronteira do portal | C — Controle comum herdado |
    |:---|:---|:---|:---|:---|
    | Responsabilidade clara, com dono que responde pela eficácia | 3 | 1 | 2 | 3 |
    | Avaliação proporcional a um caminho de confiança crítico | 3 | 1 | 3 | 3 |
    | Reaproveitamento pelos próximos sistemas | 2 | 1 | 1 | 3 |
    | Esforço para a equipe do portal (3 = menor esforço) | 1 | 3 | 1 | 2 |
    | **Total ponderado** | | **11** | **18** | **26** |

    - **Pesos:** dono e avaliação recebem 3 porque o agente é um caminho de confiança crítico — comprometido, permite criar ou alterar identidades usadas pelo portal. Reaproveitamento recebe 2 porque outros sistemas usarão a mesma sincronização. O esforço da equipe do portal importa, mas não pode decidir sozinho a fronteira (peso 1).
    - **Discordância com a equipe do portal:** deixar o agente fora da fronteira **sem** tratá-lo como controle comum avaliado cria uma lacuna sem dono.
    - **Recomendação: C.** Declarar a identidade corporativa — diretório, agente de sincronização e servidor que o hospeda — como **controle comum** de responsabilidade da equipe de identidade, com avaliação própria (endurecimento do servidor, tiering administrativo, monitoração de alterações). O portal **herda** formalmente esse controle e o pacote de autorização referencia a evidência.
    - **Residual:** comprometimento do AD on-premises continua afetando o portal; o risco é registrado e associado ao programa de identidade (Módulo 6).
    - **O que mudaria a decisão:** se a equipe de identidade não puder assumir o controle comum antes da entrada em produção, B serve como solução transitória, registrada em ADR com prazo; se o portal passar a usar um provedor de identidade próprio, sem sincronização com o AD, a fronteira precisa ser redesenhada.

## Pontos-chave

- O RMF organiza a entrada e a permanência de um sistema em produção em sete etapas.
- Categorização por impacto torna os controles proporcionais.
- Implementar, avaliar e aceitar risco são funções separadas.
- Fronteira de autorização e controles comuns herdáveis são decisões de arquitetura.
- A autorização contínua depende de monitoração e de gatilhos de mudança.

## Referências

### Fundamentação principal

- NIST. *SP 800-37 Rev. 2 — Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy*. Joint Task Force, 2018. DOI 10.6028/NIST.SP.800-37r2. <https://csrc.nist.gov/pubs/sp/800/37/r2/final> — Sumário Executivo (p. viii), Sec. 2.2 (pp. 9–10), Sec. 3.1 (pp. 12–13), nota 36 (p. 16). *(Lido até a Sec. 3.1.)*
- NIST. *Risk Management Framework — projeto*. <https://csrc.nist.gov/projects/risk-management> — etapas e materiais de apoio.
- NIST. *SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments*. 2012 — Sec. 2.4: níveis de organização, processo e sistema.

### Leitura complementar

- NIST. *SP 800-53 Rev. 5* e *SP 800-53B* — catálogo e baselines usados na etapa Select ([Aula 03](03-control-selection-tailoring.md)).
- NIST. *CSF 2.0* — perfis e o uso opcional na etapa Prepare (P-4).

### Aplicação prática

- Escolha um sistema da sua organização e desenhe a fronteira de autorização, separando controles próprios, herdados de plataformas internas e herdados do provedor de cloud.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
