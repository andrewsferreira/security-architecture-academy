---
id: M03-L04
title: "Aula 04 — ISO/IEC 27001/27002, LGPD e PCI DSS: propósito e escopo"
public_title: "Módulo 3 — Aula 04 — ISO/IEC 27001/27002, LGPD e PCI DSS: propósito e escopo"
description: A natureza, o escopo e o efeito na arquitetura das referências mais citadas em projetos no Brasil — a ISO/IEC 27001 como sistema de gestão certificável, a ISO/IEC 27002 como guia de controles, a LGPD como lei e o PCI DSS como padrão contratual do setor de cartões.
domain: grc
tier: fundamental
status: published
prerequisites: [M03-L01]
objectives:
  - Classificar uma referência como obrigação legal, obrigação contratual ou adoção voluntária e explicar a consequência para a arquitetura.
  - Descrever a estrutura da ISO/IEC 27001:2022, a Declaração de Aplicabilidade e a relação com a ISO/IEC 27002.
  - Identificar os dispositivos da LGPD que mais afetam decisões de arquitetura.
  - Explicar por que a redução de escopo é a principal decisão de arquitetura em PCI DSS.
minutes: 75
sources: [ISO-27001-2022, ISO-27002-2022, LGPD-L13709, ANPD-RES-15-2024, PCI-DSS-401, ISACA-ISO27001-TRANSITION-2024]
further_reading: [NIST-CSF-INFORMATIVE-REFS, NIST-SP800-53]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M03
---

# Aula 04 — ISO/IEC 27001/27002, LGPD e PCI DSS: propósito e escopo { #isoiec-2700127002-lgpd-e-pci-dss-proposito-e-escopo }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 3 · Nível 1</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">75 min · ID técnico: M03-L04</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Em reuniões de projeto, "a ISO exige", "a LGPD exige" e "o PCI exige" aparecem como se fossem a mesma coisa. Não são. A LGPD é **lei**; o PCI DSS é um padrão que se torna obrigatório **por contrato** para quem lida com dados de cartão; a ISO/IEC 27001 é uma norma **voluntária** de sistema de gestão, que pode ser certificada. Cada natureza tem consequências diferentes para escopo, evidência e decisão de arquitetura. Esta aula apresenta o propósito de cada referência, o que ela pede da arquitetura e como evitar controles duplicados.

!!! warning "Esta aula não é aconselhamento jurídico"

    O conteúdo explica a estrutura das referências para apoiar decisões de arquitetura. A interpretação de obrigações legais e contratuais de um caso concreto cabe ao jurídico e ao encarregado de dados da organização.

**Pré-requisito:** [Governança de segurança e o NIST CSF 2.0](01-governance-csf.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Classificar uma referência como obrigação legal, obrigação contratual ou adoção voluntária e explicar a consequência para a arquitetura.
- Descrever a estrutura da ISO/IEC 27001:2022, a Declaração de Aplicabilidade e a relação com a ISO/IEC 27002.
- Identificar os dispositivos da LGPD que mais afetam decisões de arquitetura.
- Explicar por que a redução de escopo é a principal decisão de arquitetura em PCI DSS.

## Conceito

### Três naturezas de obrigação

| Natureza | Exemplo | A quem se aplica | Consequência do descumprimento |
|:---|:---|:---|:---|
| **Legal** | LGPD e resoluções da ANPD | Todo tratamento de dados pessoais no escopo da lei | Sanções administrativas, responsabilização civil |
| **Contratual** | PCI DSS | Quem armazena, processa ou transmite dados de cartão, por contrato com adquirentes e bandeiras | Penalidades previstas no contrato com o adquirente ou nos programas das bandeiras — conforme cada contrato |
| **Voluntária** | ISO/IEC 27001, NIST CSF, CIS Controls | Quem decide adotar — às vezes por exigência de clientes | Perda de certificação ou de contrato que a exija |

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m03-l04-obligation-types.mmd"
```

<figcaption>Figura 1 — Obrigações legais, contratuais e voluntárias convergem para um único programa de segurança.</figcaption>
</figure>

A consequência prática para o arquiteto: uma obrigação **legal** define limites que a arquitetura não pode negociar; uma obrigação **contratual** pode ser reduzida diminuindo o escopo; uma referência **voluntária** é uma escolha de método, que deve servir ao risco e não o contrário.

## Fundamentos técnicos

### ISO/IEC 27001:2022 — sistema de gestão

A ISO/IEC 27001 especifica requisitos para um **sistema de gestão de segurança da informação (SGSI)**. A edição atual foi publicada em 25/10/2022, e o período de transição das certificações da edição de 2013 terminou em 31/10/2025, segundo o ISACA Journal. Dois blocos se destacam:

- **Cláusulas 4 a 10** — contexto da organização, liderança, planejamento, apoio, operação, avaliação de desempenho e melhoria. Quem declara conformidade não pode excluí-las.
- **Anexo A** — 93 controles organizados em quatro temas: organizacionais (37), pessoas (8), físicos (14) e tecnológicos (34). A edição de 2013 tinha 114 controles em 14 domínios.

O artefato que liga a gestão de riscos aos controles é a **Declaração de Aplicabilidade** (*Statement of Applicability*), que registra quais controles do Anexo A foram incluídos ou excluídos e por quê. Para o arquiteto, ela é o equivalente ISO do tailoring estudado na [Aula 03](03-control-selection-tailoring.md): cada controle incluído deve ser rastreável até um risco e um tratamento.

!!! tip "O que a certificação prova — e o que não prova"

    Uma certificação ISO/IEC 27001 atesta que o SGSI, **dentro do escopo certificado**, atende aos requisitos da norma. Ela não garante que todos os sistemas do fornecedor estejam protegidos. Ao avaliar um fornecedor, leia o **escopo do certificado** antes de concluir qualquer coisa.

### ISO/IEC 27002:2022 — orientação de controles

A ISO/IEC 27002, publicada em 15/02/2022, detalha propósito e orientação de implementação de cada controle correspondente ao Anexo A. Entre os 11 controles novos estão o uso de serviços de cloud (5.23), a prontidão de TIC para continuidade de negócios (5.30), o mascaramento de dados (8.11), a prevenção de vazamento de dados (8.12) e o secure coding (8.28). Cada controle recebe **atributos** — tipo de controle (preventivo, detectivo, corretivo), propriedade de segurança, conceito de cibersegurança, capacidade operacional e domínio de segurança —, que permitem filtrar o catálogo por diferentes visões.

### LGPD — o que afeta a arquitetura

A Lei nº 13.709/2018 se aplica ao tratamento de dados pessoais e está em vigor com alterações posteriores (o texto compilado do Planalto registra alterações até 2026). Os dispositivos com maior efeito em decisões de arquitetura são:

| Dispositivo | Conteúdo | Efeito na arquitetura |
|:---|:---|:---|
| **Art. 5º, II** | Define dado pessoal sensível (saúde, biometria, origem racial ou étnica, entre outros) | Classificação de dados e controles reforçados |
| **Art. 6º** | Princípios: finalidade, adequação, **necessidade**, livre acesso, qualidade, transparência, **segurança**, **prevenção**, não discriminação, responsabilização e prestação de contas | Minimização de dados, segregação por finalidade, evidências |
| **Art. 7º** | Bases legais para o tratamento | Registro da base legal por fluxo de dados |
| **Art. 11** | Hipóteses em que dados pessoais sensíveis podem ser tratados | Base legal própria para dados sensíveis, registrada por fluxo |
| **Art. 37** | Registro das operações de tratamento pelo controlador e pelo operador | Inventário de dados e fluxos mantido como artefato da arquitetura |
| **Art. 46** | Medidas de segurança técnicas e administrativas contra acessos não autorizados e situações acidentais ou ilícitas; o § 2º manda observá-las desde a fase de concepção do produto ou do serviço | Requisito de segurança de todo sistema que trata dados pessoais, considerado já no desenho |
| **Art. 48** | Comunicação de incidente de segurança que possa acarretar risco ou dano relevante à ANPD e ao titular | Detecção, investigação e registro capazes de cumprir prazos |
| **Art. 49** | Sistemas usados no tratamento devem ser estruturados para atender aos requisitos de segurança, às boas práticas e à governança | Segurança como requisito de estrutura do sistema, não só de operação |
| **Art. 50** | Faculdade de formular regras de boas práticas e de governança e de implementar programa de governança em privacidade | Integração entre governança de segurança e de privacidade |

A **Resolução CD/ANPD nº 15, de 24 de abril de 2024**, publicada no Diário Oficial da União em 26/04/2024, aprova o Regulamento de Comunicação de Incidente de Segurança. Os pontos com efeito direto na arquitetura são:

- **Relevância (art. 5º):** o incidente pode acarretar risco ou dano relevante quando puder afetar significativamente interesses e direitos fundamentais dos titulares **e**, cumulativamente, envolver ao menos um destes fatores: dados sensíveis; dados de crianças, adolescentes ou idosos; dados financeiros; dados de autenticação em sistemas; dados protegidos por sigilo legal, judicial ou profissional; ou dados em larga escala.
- **Prazos (arts. 6º e 9º):** comunicação à ANPD e aos titulares em **três dias úteis**, contados do conhecimento pelo controlador de que o incidente afetou dados pessoais — para a ANPD, ressalvado prazo previsto em legislação específica; complementação das informações à ANPD em até 20 dias úteis da comunicação; prazos em dobro para agentes de tratamento de pequeno porte, conforme o enquadramento da Resolução CD/ANPD nº 2/2022 — a confirmar no caso concreto.
- **Quem comunica (art. 6º, § 5º):** o controlador, por meio do encarregado. A orientação da ANPD indica o peticionamento eletrônico no SEI!ANPD.
- **Registro (art. 10):** o controlador mantém o registro do incidente — inclusive do que não foi comunicado à ANPD nem aos titulares — por no mínimo cinco anos.

O texto foi conferido na cópia integral mantida pela Biblioteca Digital do Ministério da Justiça, que declara não substituir o original publicado no Diário Oficial; em um documento formal, cite o DOU.

Para a arquitetura, três dias úteis significam que **logs, inventário de dados e classificação precisam existir antes do incidente**: sem saber onde estão os dados pessoais e quem os acessou, não há como avaliar a relevância a tempo.

### PCI DSS v4.0.1 — escopo é tudo

O **PCI DSS** é mantido pelo PCI Security Standards Council e se aplica a entidades que armazenam, processam ou transmitem dados de portadores de cartão ou dados sensíveis de autenticação, e também às que podem afetar a segurança do ambiente desses dados. Segundo o próprio PCI SSC, a exigência de conformidade fica a critério das organizações que mantêm programas de conformidade, como as bandeiras e os adquirentes — daí a natureza **contratual** da obrigação. A versão 4.0.1, publicada em 11/06/2024, é uma revisão limitada, sem requisitos novos ou removidos; a v4.0 foi retirada em 31/12/2024, e os requisitos da v4.0 com data futura passaram a valer em 31/03/2025. O padrão define 12 requisitos agrupados em 6 objetivos, que cobrem de controles de segurança de rede a políticas e resposta a incidentes (estrutura conferida em fonte secundária; o documento oficial exige aceite de licença).

A decisão de arquitetura mais importante em PCI DSS é a **redução de escopo**: o ambiente de dados de cartão (*cardholder data environment*, CDE) e tudo que se conecta a ele estão no escopo. Técnicas como **tokenização**, **páginas de pagamento hospedadas pelo provedor** e **segmentação** reduzem o número de sistemas sujeitos aos requisitos — e, com isso, custo e risco.

## Exemplo empresarial

!!! example "Aurora Pagamentos — um conjunto de controles, três evidências"

    A Aurora precisava atender ao PCI DSS (contrato com adquirentes), à LGPD (dados pessoais de lojistas e portadores) e manter a certificação ISO/IEC 27001 exigida por clientes corporativos. O primeiro levantamento encontrou três equipes produzindo evidências diferentes para o mesmo controle de gestão de acessos.

    O arquiteto de segurança propôs:

    1. **Um catálogo interno** de controles (Aula 07), cada um mapeado ao requisito PCI DSS, ao controle do Anexo A e ao dispositivo da LGPD que ele ajuda a atender.
    2. **Redução de escopo PCI** com tokenização na borda: só o cofre de tokens e o serviço de autorização ficaram no CDE.
    3. **Inventário de dados pessoais** com classificação e base legal por fluxo, alimentando o processo de resposta a incidentes para cumprir os prazos da ANPD.

    Resultado: o CDE caiu de 140 para 18 servidores, e a mesma evidência de revisão de acessos passou a servir às três auditorias.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Programas | Um por referência, com equipes separadas | Um catálogo, várias evidências |
| PCI DSS | Proteger tudo como CDE | Reduzir escopo por tokenização e segmentação |
| LGPD | Tratada só pelo jurídico | Requisitos de arquitetura: inventário, minimização, logs, resposta |
| ISO/IEC 27001 | Certificado como objetivo | SGSI como forma de gerir riscos; escopo declarado |
| Linguagem | "Framework X exige" para tudo | Natureza da obrigação explícita: lei, contrato ou escolha |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, o provedor oferece atestados (certificações, relatórios de auditoria) que cobrem a parte dele; a organização continua responsável pela configuração e pelos dados. Para PCI DSS, um serviço de cloud dentro do CDE amplia o escopo para a configuração da conta; tokenização e serviços de pagamento gerenciados reduzem esse escopo. Para a LGPD, transferências internacionais e o uso de suboperadores precisam ser mapeados — questão a validar com o jurídico em cada caso. Em ambientes híbridos, o inventário de dados pessoais precisa atravessar os dois lados, ou a resposta a incidentes não consegue cumprir prazos.

## Como especificar e implementar

- "Todo requisito de segurança registra sua origem: lei, contrato, norma adotada ou decisão de risco."
- "Sistemas que tratam dados pessoais registram as categorias de dados, a base legal e os fluxos; dados sensíveis recebem controles reforçados."
- "Logs e inventário de dados permitem determinar, em até 24 horas, quais dados pessoais foram afetados por um incidente."
- "Dados de cartão são tokenizados na entrada; nenhum sistema fora do CDE armazena PAN."
- "A Declaração de Aplicabilidade é derivada do catálogo interno e revisada a cada mudança de escopo."

## Trade-offs, limitações e antipadrões

- **Trade-off — tokenização:** reduz escopo PCI, mas cria dependência de um provedor de tokens e exige desenho cuidadoso da detokenização.
- **Antipadrão — "temos ISO, então estamos seguros":** ignora o escopo certificado.
- **Antipadrão — conformidade como teto:** cumprir o mínimo de cada referência sem olhar o risco real.
- **Limitação:** mapeamentos entre referências ajudam, mas não são equivalências; cada auditoria tem seus critérios.

## Como validar

- Para cada requisito do backlog de segurança, verificar se a origem está registrada.
- Testar a segmentação do CDE a partir de redes fora do escopo.
- Simular um incidente e medir quanto tempo leva para identificar quais dados pessoais foram afetados.
- Conferir se a Declaração de Aplicabilidade corresponde aos controles realmente implementados.

## Como apresentar e justificar

- **Para a diretoria:** "A LGPD é lei; o PCI é contrato; a ISO é escolha nossa, exigida por clientes. Um único programa atende às três, com uma equipe e uma evidência por controle."
- **Para engenharia:** "Se o sistema não tocar no número do cartão — só no token —, ele sai do escopo PCI. Isso economiza meses de controles."

## Checklist de revisão arquitetural

- [ ] A natureza de cada obrigação (lei, contrato, voluntária) está identificada.
- [ ] O escopo PCI foi minimizado e a segmentação é testada.
- [ ] Dados pessoais estão inventariados, classificados e com base legal registrada.
- [ ] A capacidade de investigação suporta os prazos de comunicação de incidentes.
- [ ] Controles são mapeados a várias referências a partir de um único catálogo.
- [ ] O escopo de certificações de fornecedores foi lido antes de confiar nelas.

## Questões de compreensão

**1.** Por que é incorreto dizer que "o NIST CSF é obrigatório no Brasil"?

??? success "Resposta comentada"

    Porque o CSF é uma referência voluntária fora do governo federal dos Estados Unidos. Pode ser exigido por um contrato ou adotado por decisão da organização, mas não é lei no Brasil. Apresentá-lo como obrigação confunde a governança e distorce prioridades.

**2.** O que é a Declaração de Aplicabilidade e por que importa para a arquitetura?

??? success "Resposta comentada"

    É o registro dos controles do Anexo A da ISO/IEC 27001 incluídos ou excluídos, com justificativa, ligando a avaliação de riscos ao tratamento. Para a arquitetura, funciona como o tailoring: cada controle precisa ser rastreável até um risco e uma decisão.

**3.** Qual a principal alavanca de arquitetura para reduzir o custo do PCI DSS?

??? success "Resposta comentada"

    Reduzir o escopo do ambiente de dados de cartão — com tokenização, páginas de pagamento hospedadas pelo provedor e segmentação —, de modo que menos sistemas armazenem, processem ou transmitam dados de cartão.

## Exercício de tomada de decisão

!!! question "Cenário: novo app de agendamento da Lumen com pagamento"

    A Lumen Saúde vai cobrar consultas particulares pelo app de agendamento. Opções: (A) o app coleta os dados do cartão e o backend da Lumen os envia ao adquirente; (B) o app usa um componente do provedor de pagamentos que devolve um token à Lumen; (C) o paciente é redirecionado a uma página de pagamento hospedada pelo provedor. O app também armazena dados de saúde (agendamentos por especialidade), e a equipe de produto observou que cada etapa a mais no pagamento faz pacientes desistirem do agendamento. Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho), indique a recomendação e os efeitos sobre PCI DSS e LGPD.

??? success "Resolução de referência"

    | Critério | Peso | A — App coleta o cartão | B — Componente com token | C — Página hospedada |
    |:---|:---|:---|:---|:---|
    | Redução do escopo PCI DSS | 3 | 1 | 2 | 3 |
    | Experiência do paciente no app | 2 | 3 | 3 | 1 |
    | Esforço de implementação e operação (3 = menor) | 2 | 1 | 2 | 3 |
    | Controle da Lumen sobre o fluxo de agendamento | 1 | 3 | 2 | 1 |
    | **Total ponderado** | | **14** | **18** | **18** |

    - **Pesos:** o escopo PCI pesa 3 porque define custo e risco por anos; experiência e esforço pesam 2 porque afetam receita e equipe; controle do fluxo pesa 1 porque pode ser recuperado com bom desenho de integração.
    - **Empate entre B e C — a matriz não decide sozinha:** C reduz mais o escopo, mas piora a experiência; B mantém o paciente no app. **Recomendação: B**, se o componente do provedor for executado de forma que os dados do cartão não passem pelos sistemas da Lumen — ponto a confirmar com o provedor e o assessor de conformidade. A opção A coloca app e backend no CDE — escopo amplo e caro.
    - **LGPD:** a especialidade agendada pode revelar condição de saúde e, por isso, deve ser tratada como potencial dado pessoal sensível (dado referente à saúde, art. 5º, II) — enquadramento a confirmar com o encarregado e o jurídico. Exige base legal própria para dados sensíveis registrada (art. 11), minimização (o dado de pagamento não precisa da especialidade), medidas de segurança desde o desenho (art. 46) e capacidade de investigar incidentes a tempo de cumprir a regulamentação da ANPD.
    - **Separação de domínios:** o serviço de pagamentos não recebe dados clínicos; o de agendamento não recebe dados de cartão.
    - **Risco residual:** dependência do provedor de pagamentos e do desenho correto do componente; incidentes no provedor continuam afetando os pacientes.
    - **O que mudaria a decisão:** se o provedor não garantir que os dados do cartão nunca transitam pelos sistemas da Lumen, B perde a redução de escopo e C passa a ser a recomendação.

## Pontos-chave

- LGPD é lei, PCI DSS é contrato, ISO/IEC 27001 é escolha — e isso muda a estratégia.
- A Declaração de Aplicabilidade liga riscos a controles na ISO/IEC 27001.
- A LGPD gera requisitos de arquitetura concretos: inventário, minimização, segurança e capacidade de resposta a incidentes.
- Em PCI DSS, reduzir escopo é a decisão de maior impacto.
- Um catálogo único, mapeado a várias referências, evita controles e evidências duplicados.

## Referências

### Fundamentação principal

- Brasil. *Lei nº 13.709, de 14 de agosto de 2018 — LGPD*, texto compilado. <https://planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm> — arts. 5º, 6º, 7º, 11, 37, 46, 48, 49 e 50. *(Texto oficial lido.)*
- ISO/IEC. *ISO/IEC 27001:2022* e *ISO/IEC 27002:2022*. Normas pagas, não lidas; estrutura conferida em fontes secundárias.
- ISACA Journal. *Navigating the ISO/IEC 27001:2022 Transition: A 90-Day Challenge*. 2024, vol. 3. <https://www.isaca.org/resources/isaca-journal/issues/2024/volume-3/navigating-the-iso-iec-27001-2022-transition-a-90-day-challenge> — transição, cláusulas 4–10 e Declaração de Aplicabilidade. *(Lido.)*
- PCI Security Standards Council. *PCI DSS v4.0.1*. 2024. <https://www.pcisecuritystandards.org/document_library/> — aplicabilidade e programas de conformidade conferidos na página oficial do padrão (<https://www.pcisecuritystandards.org/standards/pci-dss/>); data, natureza da revisão e retirada da v4.0 conferidas no anúncio oficial (<https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1>); estrutura de requisitos em fonte secundária.
- ANPD. *Resolução CD/ANPD nº 15, de 24 de abril de 2024 — Regulamento de Comunicação de Incidente de Segurança*. DOU de 26/04/2024, Seção 1, p. 114–115 — arts. 5º (caput e incisos), 6º (caput e §§ 1º, 3º, 5º e 8º), 9º (caput e § 6º) e 10 (caput), conferidos no texto integral da Biblioteca Digital do Ministério da Justiça: <https://bibliotecadigital.mj.gov.br/bitstream/1/12879/2/RES_ANPD_2024_15.html>. *(Lido; data, seção e páginas do DOU conferidas no registro do item na mesma biblioteca.)*
- ANPD. *Comunicado de incidente de segurança (CIS)* — orientação ao agente de tratamento. <https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis> — prazos, complementação e canal de comunicação. *(Lido.)*

### Leitura complementar

- NIST. *CSF 2.0 Informative References* — mapeamentos para ISO/IEC 27001:2022 e outras referências.
- NIST. *SP 800-53 Rev. 5* — crosswalk com a ISO/IEC 27001:2022 entre os materiais suplementares.

### Aplicação prática

- Pegue cinco requisitos de segurança de um projeto real e classifique a origem de cada um: lei, contrato, norma adotada ou decisão de risco. Para os que não têm origem clara, decida com o dono do sistema se devem continuar.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
