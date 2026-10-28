---
id: M03-L08
title: "Aula 08 — Indicadores, maturidade e reporte à governança"
public_title: "Módulo 3 — Aula 08 — Indicadores, maturidade e reporte à governança"
description: Como medir se a arquitetura de segurança está funcionando — medidas de implementação, eficácia, eficiência e impacto segundo a SP 800-55 —, como usar maturidade sem transformá-la em meta e como reportar à governança de forma que ela decida.
domain: grc
tier: architect
status: published
prerequisites: [M03-L07]
objectives:
  - Distinguir medidas e métricas e classificar medidas em implementação, eficácia, eficiência e impacto.
  - Especificar medidas documentadas, com fórmula, fonte de dados, meta e dono.
  - Usar avaliações de maturidade e Tiers do CSF como instrumentos, não como metas.
  - Estruturar um reporte à governança que mostre tendência, desvios em relação à tolerância e decisões pedidas.
minutes: 60
sources: [NIST-SP800-55-V1, NIST-CSF-2]
further_reading: [NIST-SP800-37-R2, CIS-CONTROLS-V8-1]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M03
---

# Aula 08 — Indicadores, maturidade e reporte à governança { #indicadores-maturidade-e-reporte-a-governanca }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 3 · Nível 1</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">60 min · ID técnico: M03-L08</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Uma arquitetura de segurança só é sustentável se a organização conseguir saber, com dados, se ela está funcionando. Medir mal é pior do que não medir: números sem definição geram falsa confiança e incentivos errados. Esta aula usa a SP 800-55 Volume 1, de dezembro de 2024, para distinguir medidas e métricas, classificar medidas por tipo e documentá-las de forma verificável; discute o lugar da maturidade e dos Tiers do CSF; e mostra como transformar indicadores em um reporte que leve a governança a decidir.

**Pré-requisito:** [Catálogo de controles e arquitetura baseada em risco](07-control-catalog-risk-architecture.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Distinguir medidas e métricas e classificar medidas em implementação, eficácia, eficiência e impacto.
- Especificar medidas documentadas, com fórmula, fonte de dados, meta e dono.
- Usar avaliações de maturidade e Tiers do CSF como instrumentos, não como metas.
- Estruturar um reporte à governança que mostre tendência, desvios em relação à tolerância e decisões pedidas.

## Conceito

### Medidas e métricas

A SP 800-55 Vol. 1 diferencia (Sec. 1.4, p. 2; Sec. 2.4, pp. 9–11):

- **Medida:** valor quantificável e objetivo resultante de medição — por exemplo, "98% das contas pertencem a funcionários ativos".
- **Métrica:** medidas e resultados de avaliação desenhados para acompanhar progresso e apoiar decisões, comparados a uma **meta**.

O documento também distingue avaliação **quantitativa** (números que mantêm o significado fora do contexto), **semiquantitativa** (um "nível 3" que representa um conjunto de qualidades) e **qualitativa** (alto, médio, baixo; mapas de calor), e não trata as duas últimas como medição (Sec. 2.2, pp. 7–8). Isso tem uma consequência prática: uma nota de maturidade é uma **avaliação**, não uma **medida** — útil, mas de outra natureza.

### Quatro tipos de medida

| Tipo (Sec. 3.3, pp. 17–18) | O que mostra | Exemplo |
|:---|:---|:---|
| **Implementação** | Progresso da implantação de controles, em geral em porcentagem | % de contas privilegiadas com MFA resistente a phishing |
| **Eficácia** | Se controles e processos alcançam o resultado desejado | % de testes de phishing simulado que resultam em credencial capturada |
| **Eficiência** | Quão oportunos são os controles — rapidez de retorno e de correção | Tempo mediano para corrigir vulnerabilidade crítica exposta à internet |
| **Impacto** | Efeito da segurança na missão — custos, multas, confiança | Horas de parada de processos críticos por incidentes de segurança |

O documento observa que eficácia e eficiência, juntas, costumam ser chamadas de **resultados do programa**. Programas imaturos medem quase só implementação; a pergunta da governança, porém, é sobre eficácia e impacto.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m03-l08-metrics-layers.mmd"
```

<figcaption>Figura 1 — Dos dados operacionais validados ao reporte à governança, passando pelos quatro tipos de medida.</figcaption>
</figure>

## Fundamentos técnicos

### Documentar uma medida

A SP 800-55 Vol. 1 recomenda documentar medidas em formato padronizado, com campos como objetivo, escopo, medida, tipo, fórmula, meta e fonte de dados, e sugere que a medida comece com uma expressão numérica como "porcentagem de" ou "número de" (Sec. 3.1.1, pp. 12–14). Um exemplo no catálogo da organização:

| Campo | Valor |
|:---|:---|
| **ID** | MET-IAM-01 |
| **Objetivo** | Acesso administrativo resistente a phishing (CTL-IAM-03; RSK-007) |
| **Medida** | Porcentagem de contas privilegiadas ativas com apenas métodos resistentes a phishing habilitados |
| **Tipo** | Implementação |
| **Fórmula** | contas privilegiadas com FIDO2 e sem fallback ÷ contas privilegiadas ativas × 100 |
| **Fonte de dados** | Exportação diária do IdP cruzada com o inventário de contas privilegiadas |
| **Meta** | 100% até 2027-03-31; tolerância: nenhuma conta nova sem FIDO2 por mais de 7 dias |
| **Dono** | Gerente de identidade |
| **Frequência** | Semanal |

### Qualidade dos dados

Boas medidas são exatas, precisas, consistentes, replicáveis, com referência temporal e unidade padronizada (Sec. 3.2, pp. 16–17); o documento recomenda definir claramente coleta e repositórios e validar integridade e estrutura dos dados antes da análise (pp. 15–16). Para o arquiteto, isso se traduz em requisitos:

- **Inventário confiável é pré-requisito** — "% de servidores com EDR" é inútil se o denominador vem de um inventário incompleto.
- **Coleta automática** sempre que possível, a partir dos próprios building blocks (IdP, plataforma de cloud, pipeline).
- **Denominador explícito** — "100% dos servidores" de qual escopo?

### Selecionar poucas medidas

O documento recomenda medidas obteníveis, repetíveis e viáveis, ligadas às prioridades declaradas, e lembra que, com métricas quantitativas, "menos costuma ser mais" (pp. 9–11). Para priorizar, cita fatores como valor do ativo, custo do controle, avaliações de risco e requisitos legais (Sec. 3.4, pp. 20–22). Uma regra prática: cada cenário crítico do register deve ter **uma medida de eficácia ou de impacto**, não apenas de implementação.

### Maturidade e Tiers

Modelos de maturidade e os **Tiers** do CSF 2.0 (Aula 01) caracterizam a forma como práticas são conduzidas — de ad hoc a adaptativas. São úteis para:

- Planejar a evolução de processos (por exemplo, de gestão de vulnerabilidades reativa a orientada a risco).
- Comparar unidades de negócio com o mesmo instrumento.

E são perigosos quando viram meta: "chegar ao nível 4" incentiva produzir documentos e cerimônias, não reduzir risco. A melhor combinação é **maturidade para orientar a evolução** e **medidas de eficácia e impacto para provar resultado**.

### O reporte à governança

Um reporte que leva a decisões responde a quatro perguntas:

1. **Onde estamos em relação à tolerância?** — desvios em destaque.
2. **Para onde estamos indo?** — tendência, não fotografia.
3. **O que mudou no ambiente de ameaças ou no negócio?** — contexto.
4. **O que precisamos que vocês decidam?** — aceites, orçamento, prioridades.

## Exemplo empresarial

!!! example "Meridiana — de 47 indicadores a uma página"

    O relatório mensal de segurança da Meridiana tinha 47 indicadores, quase todos de implementação ("% de patches aplicados", "nº de treinamentos"). A diretoria não lia.

    O arquiteto propôs uma página com:

    | Cenário | Medida principal | Tipo | Valor | Tolerância | Tendência |
    |:---|:---|:---|:---|:---|:---|
    | RSK-007 Ransomware | Tempo medido de recuperação da expedição no último exercício | Impacto | 11 h | ≤ 8 h | Melhorando (era 30 h antes das mudanças da BIA) |
    | RSK-007 Ransomware | % de acessos remotos com MFA resistente a phishing | Implementação | 92% | 100% até março | Melhorando |
    | RSK-011 Fraude de fornecedores | Alterações bancárias sem dupla aprovação | Eficácia | 0 | 0 | Estável |
    | RSK-014 Vulnerabilidades expostas | Mediana de dias para corrigir crítica exposta | Eficiência | 9 dias | ≤ 7 dias | Piorando |

    E uma seção "Decisões pedidas": aprovar orçamento para automatizar a recuperação do Active Directory — o exercício mostrou que o procedimento manual ainda consome a maior parte das 11 horas e impede o RTO de 8 horas definido na BIA ([Aula 05](05-bia-rto-rpo.md)) — e aceitar formalmente o atraso na correção de vulnerabilidades por 60 dias enquanto a equipe é reforçada. As duas decisões foram tomadas na mesma reunião.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Tipo de medida | Quase só implementação | Implementação, eficácia, eficiência e impacto |
| Definição | Nome do indicador | Medida documentada com fórmula, fonte, meta e dono |
| Coleta | Manual, em planilha | Automática a partir dos building blocks |
| Maturidade | Meta em si | Instrumento de evolução, combinado com medidas de resultado |
| Reporte | Lista de números | Tolerância, tendência, contexto e decisões pedidas |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, muitas medidas de implementação podem ser obtidas continuamente de serviços de postura e de inventário do provedor; o desafio passa a ser o **denominador** em ambientes efêmeros (contar recursos que existiram por minutos). Em on-premises, a qualidade do inventário costuma ser o gargalo. Em ambientes híbridos, a mesma medida precisa ser calculada da mesma forma nos dois lados, ou a comparação engana — por exemplo, "cobertura de EDR" medida por agentes no datacenter e por política na cloud.

## Como especificar e implementar

- "Toda medida do programa de segurança é documentada com objetivo, fórmula, fonte de dados, meta, tolerância, dono e frequência."
- "Cada cenário crítico do register tem ao menos uma medida de eficácia, eficiência ou impacto."
- "Building blocks de referência expõem os dados necessários às medidas dos controles que implementam."
- "O reporte à governança destaca desvios em relação à tolerância e as decisões necessárias."

## Trade-offs, limitações e antipadrões

- **Trade-off:** medidas de impacto são as mais relevantes e as mais difíceis de obter; comece com aproximações honestas e declare a limitação.
- **Antipadrão — melancia:** verde por fora, vermelho por dentro; indicadores de implementação em 100% enquanto a eficácia é desconhecida.
- **Antipadrão — métrica como meta (lei de Goodhart):** "fechar chamados de vulnerabilidade" incentiva fechar sem corrigir.
- **Limitação:** medidas mostram sintomas; a explicação exige análise e contexto.

## Como validar

- Recalcular uma medida a partir dos dados brutos e comparar com o valor reportado.
- Verificar se o denominador corresponde ao inventário real.
- Conferir se cada cenário crítico tem medida de eficácia ou impacto.
- Perguntar à governança que decisões foram tomadas com base no último reporte.

## Como apresentar e justificar

- **Para a diretoria:** "Uma página: onde estamos fora da tolerância, para onde estamos indo e o que precisamos que vocês decidam hoje."
- **Para engenharia:** "A medida é calculada a partir dos dados da plataforma. Se a plataforma não expuser o dado, o controle não tem evidência."

## Checklist de revisão arquitetural

- [ ] As medidas estão documentadas com fórmula, fonte, meta e dono.
- [ ] Há medidas dos quatro tipos para os cenários críticos.
- [ ] Os dados são coletados automaticamente e validados.
- [ ] Denominadores vêm de inventário confiável.
- [ ] Maturidade é usada como instrumento, não como meta.
- [ ] O reporte termina com decisões pedidas.

## Questões de compreensão

**1.** Qual a diferença entre uma medida de implementação e uma de eficácia? Dê um exemplo de cada para backup.

??? success "Resposta comentada"

    Implementação mostra se o controle foi implantado: "% de sistemas críticos com cópia imutável". Eficácia mostra se ele alcança o resultado: "% de restaurações de teste concluídas dentro do RTO com dados íntegros". É possível ter 100% de implementação e baixa eficácia.

**2.** Por que uma nota de maturidade não é uma medida, segundo a SP 800-55?

??? success "Resposta comentada"

    Porque é uma avaliação semiquantitativa: o "nível 3" representa um conjunto de qualidades, e o número não mantém significado fora do contexto da avaliação. O documento não trata avaliações qualitativas e semiquantitativas como medição — elas são úteis, mas de natureza diferente.

**3.** O que deve conter a última seção de um reporte à governança?

??? success "Resposta comentada"

    As decisões pedidas: aceites de risco, orçamento, mudanças de prioridade. Sem isso, o reporte informa mas não governa.

## Exercício de tomada de decisão

!!! question "Cenário: indicadores do portal do paciente da Lumen"

    O diretor clínico da Lumen, dono do risco do portal do paciente, pede "três indicadores que me digam se os dados dos pacientes estão protegidos". O time propõe o conjunto **A**: (1) % de servidores com antivírus; (2) número de treinamentos realizados; (3) número de alertas do SIEM. Um segundo grupo sugere o conjunto **B**, só com medidas de implementação ligadas ao portal (MFA, cifragem em repouso, cobertura de logs). Avalie a proposta A, construa um conjunto **C** com três medidas melhores — indicando o tipo e a fonte de dados de cada uma — e compare A, B e C com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho).

??? success "Resolução de referência"

    - **Avaliação:** as três propostas de A são de implementação ou atividade e não dizem nada sobre a proteção dos dados do portal: o portal roda em plataforma gerenciada (antivírus pouco relevante), treinamentos não medem comportamento e número de alertas não indica se ataques foram contidos.
    - **Sugestões:**
        1. **Eficácia:** % de acessos a prontuários fora do padrão (volume, horário, localização) investigados e encerrados em até 24 horas — fonte: detecções do SIEM e sistema de chamados.
        2. **Implementação ligada a risco:** % de contas com acesso a dados de pacientes protegidas por MFA resistente a phishing — fonte: IdP cruzado com o inventário de perfis.
        3. **Impacto:** número de incidentes com dados de pacientes que exigiram avaliação de comunicação à ANPD, por trimestre — fonte: registro de incidentes.
    - **Comparação dos conjuntos:**

        | Critério | Peso | A — Proposta do time | B — Só implementação | C — Eficácia, implementação e impacto |
        |:---|:---|:---|:---|:---|
        | Responde à pergunta do dono do risco | 3 | 1 | 2 | 3 |
        | Resistência a incentivos errados (lei de Goodhart) | 2 | 1 | 2 | 3 |
        | Dados disponíveis e confiáveis hoje | 2 | 3 | 3 | 2 |
        | Custo de coleta (3 = menor) | 1 | 3 | 3 | 2 |
        | **Total ponderado** | | **14** | **19** | **21** |

        **Pesos:** a pergunta do dono do risco define a utilidade do reporte (peso 3); incentivos e disponibilidade dos dados pesam 2; o custo de coleta pesa 1 porque a maior parte dos dados já existe no IdP, no SIEM e no registro de incidentes. **Recomendação: C.**
    - **Meta e tolerância** de cada medida aprovadas pelo diretor clínico; reporte trimestral com tendência e decisões pedidas.
    - **Risco residual:** a medida de eficácia depende da qualidade das detecções do SIEM; até que sejam testadas, o reporte declara essa limitação.
    - **O que mudaria a decisão:** se as detecções de acesso anômalo a prontuários ainda não existirem, B serve como transição por um trimestre, com a construção da fonte de dados de C como ação do plano.

## Pontos-chave

- Medidas são valores quantitativos e objetivos; métricas as comparam a metas para apoiar decisões.
- Use os quatro tipos de medida — implementação, eficácia, eficiência e impacto — e não só o primeiro.
- Documente cada medida com fórmula, fonte, meta e dono; sem inventário confiável não há denominador.
- Maturidade orienta a evolução; medidas de resultado provam que ela reduz risco.
- O reporte à governança mostra desvios, tendência e decisões pedidas.

<!-- next-steps:start -->

!!! tip "Próximos passos"

    Você concluiu a última aula do **Módulo 3** — [voltar ao módulo](index.md).

    Em seguida: [Módulo 4 — Métodos de Design e Threat Modeling](../../modules/04-threat-modeling/index.md).

<!-- next-steps:end -->

## Referências

### Fundamentação principal

- NIST. *SP 800-55 Vol. 1 — Measurement Guide for Information Security: Identifying and Selecting Measures*. K. Schroeder, H. Trinh, V. Pillitteri, 2024. <https://csrc.nist.gov/pubs/sp/800/55/v1/final> — Sec. 1.4 e 2.2–2.4 (pp. 2–11), Sec. 3.1–3.4 (pp. 12–22). *(Lido.)*
- NIST. *CSF 2.0* — Tiers (Sec. 3.2 e Apêndice B) e GV.OV, supervisão.

### Leitura complementar

- NIST. *SP 800-55 Vol. 2 — Developing an Information Security Measurement Program*. 2024 — programa de medição (não lido nesta revisão).
- NIST. *SP 800-37 Rev. 2* — monitoração contínua e autorização contínua.
- CIS. *CIS Controls v8.1* — safeguards com resultados objetivos, fáceis de medir.

### Aplicação prática

- Escolha um cenário crítico do seu register e documente uma medida de cada tipo no formato desta aula; depois, redija a seção "Decisões pedidas" de um reporte de uma página.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
