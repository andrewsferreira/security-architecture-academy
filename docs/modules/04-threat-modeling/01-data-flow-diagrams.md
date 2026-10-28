---
id: M04-L01
title: "Aula 01 — Data Flow Diagrams e fluxos de confiança"
public_title: "Módulo 4 — Aula 01 — Data Flow Diagrams e fluxos de confiança"
description: Como modelar um sistema para threat modeling — as quatro perguntas, os elementos de um Data Flow Diagram, fronteiras de confiança, nível de detalhe adequado e os erros que tornam o modelo inútil.
domain: application-security
tier: fundamental
status: published
prerequisites: [M01-L03, M00-L07]
objectives:
  - Explicar o propósito do threat modeling pelas quatro perguntas do Threat Modeling Manifesto.
  - Desenhar um DFD com entidades externas, processos, armazenamentos, fluxos e fronteiras de confiança.
  - Escolher o nível de detalhe adequado ao objetivo da análise.
  - Identificar os fluxos que atravessam fronteiras e precisam de análise prioritária.
minutes: 60
sources: [TM-MANIFESTO, OSTERMAN-STRIDE-PER-ELEMENT-2007, NIST-SP800-160-V1R1]
further_reading: [OWASP-TM-PROJECT, BOOK-GOOGLE-BSRS]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M04
---

# Aula 01 — Data Flow Diagrams e fluxos de confiança { #data-flow-diagrams-e-fluxos-de-confianca }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 4 · Nível 1</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min · ID técnico: M04-L01</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Não é possível encontrar o que pode dar errado em um sistema que ninguém consegue descrever. O primeiro passo de qualquer threat model é uma **representação** do sistema que mostre por onde os dados passam e onde a confiança muda. O Data Flow Diagram (DFD) é a representação mais usada para isso: tem poucos elementos, é rápido de desenhar em conjunto e torna as fronteiras de confiança visíveis. Esta aula apresenta as quatro perguntas do threat modeling, os elementos do DFD e os critérios para um modelo útil.

**Pré-requisitos:** [Trust boundaries e attack surface](../01-security-fundamentals/03-trust-boundaries-attack-surface.md) e [Leitura de diagramas de arquitetura](../00-foundations/07-reading-architecture-diagrams.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar o propósito do threat modeling pelas quatro perguntas do Threat Modeling Manifesto.
- Desenhar um DFD com entidades externas, processos, armazenamentos, fluxos e fronteiras de confiança.
- Escolher o nível de detalhe adequado ao objetivo da análise.
- Identificar os fluxos que atravessam fronteiras e precisam de análise prioritária.

## Conceito

### O que é threat modeling

O **Threat Modeling Manifesto**, escrito por um grupo de praticantes reconhecidos, define threat modeling como **analisar representações de um sistema para destacar preocupações sobre características de segurança e privacidade**, e o organiza em quatro perguntas:

1. **O que estamos construindo?** — a representação do sistema.
2. **O que pode dar errado?** — as ameaças.
3. **O que vamos fazer a respeito?** — as respostas.
4. **Fizemos um bom trabalho?** — a validação.

O manifesto também declara valores que mudam a forma de praticar: uma cultura de encontrar e corrigir problemas de design acima da conformidade de checklist; pessoas e colaboração acima de processos e ferramentas; refinamento contínuo acima de uma entrega única. E um princípio: o melhor uso do threat modeling é melhorar a segurança e a privacidade **por meio de análise cedo e frequente**.

Esta aula trata da primeira pergunta. As Aulas 02 a 05 tratam da segunda, a Aula 06 da terceira e a Aula 07 da quarta.

### Por que DFD

Um DFD mostra **dados em movimento** e **onde a confiança muda** — exatamente o que importa para encontrar ameaças. Diagramas de infraestrutura mostram servidores e redes, mas não por que um dado vai de A para B; diagramas de sequência mostram ordem, mas escondem fronteiras. Um DFD bem feito cabe em uma página e pode ser desenhado com a equipe em uma hora.

## Fundamentos técnicos

### Elementos

| Elemento | Notação usual | O que representa | Pergunta a fazer |
|:---|:---|:---|:---|
| **Entidade externa** | Retângulo ou forma arredondada | Pessoa ou sistema fora do controle da equipe | Como sabemos que é quem diz ser? |
| **Processo** | Círculo ou retângulo | Código que transforma dados | Com que privilégio roda? Que entradas aceita? |
| **Armazenamento** | Duas linhas paralelas ou cilindro | Dados em repouso: banco, fila, arquivo, cache | Quem lê e quem escreve? |
| **Fluxo de dados** | Seta rotulada | Dados em movimento entre elementos | O que trafega, por qual canal, autenticado como? |
| **Fronteira de confiança** | Linha ou caixa tracejada | Mudança de nível de confiança ou de dono | O que é validado ao atravessar? |

Os fluxos sempre ligam um processo a outro elemento: dados não saem sozinhos de um banco para outro banco — algum processo os move, e esse processo precisa aparecer.

### Fronteiras de confiança

Uma **fronteira de confiança** marca onde o nível de confiança muda (Módulo 1 — Aula 03): internet e borda, borda e aplicação, aplicação e dados, organização e parceiro, usuário comum e administrador. Os fluxos que atravessam fronteiras concentram as ameaças, porque é ali que o sistema precisa decidir em quem e em que confiar.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m04-l01-dfd.mmd"
```

<figcaption>Figura 1 — DFD do agendamento da Lumen Saúde, com fronteiras de confiança entre internet, borda, aplicação e dados, e fluxos numerados.</figcaption>
</figure>

Na Figura 1, os fluxos 2, 3 e 8 atravessam a fronteira entre a internet e o ambiente da Lumen; os fluxos 4, 5 e 9 atravessam fronteiras internas; o fluxo 7 sai da organização para um provedor externo. O fluxo 1 acontece no dispositivo do paciente, fora do controle da Lumen: o app roda em ambiente não confiável, e por isso tudo o que ele envia é validado do lado de dentro. Uma análise com tempo limitado começa pelos fluxos que vêm de fora.

### Nível de detalhe

| Nível | Mostra | Bom para |
|:---|:---|:---|
| **Contexto** | O sistema como um processo e suas entidades externas | Escopo, fronteira com parceiros, conversa com o negócio |
| **Nível 1** | Principais processos, armazenamentos e fronteiras internas | A maioria das revisões de arquitetura |
| **Nível 2 ou mais** | Componentes de um processo específico | Partes críticas: autenticação, pagamento, integração com parceiro |

A regra prática: detalhar **onde há fronteira, dado sensível ou mudança de privilégio**; manter agregado o restante. Um DFD com 80 elementos não é lido por ninguém.

### O modelo como artefato vivo

O manifesto prefere refinamento contínuo a uma entrega única. Na prática:

- O DFD mora junto da documentação de arquitetura e é atualizado em mudanças relevantes (nova integração, novo armazenamento, nova fronteira).
- Ferramentas de modelagem como código — o OWASP lista projetos como pytm e Threat Dragon — permitem versionar o modelo e revisá-lo como se revisa código.
- A pergunta "o que mudou desde o último modelo?" é mais barata do que refazer o modelo inteiro.

## Exemplo empresarial

!!! example "Lumen Saúde — o fluxo que não estava no diagrama de infraestrutura"

    O diagrama de infraestrutura do agendamento mostrava a VPC, as sub-redes e os bancos. Ao desenhar o DFD com a equipe, o arquiteto perguntou, para cada armazenamento, "quem escreve aqui?". A resposta sobre o repositório de laudos revelou um processo esquecido: a **integração de laudos** do laboratório parceiro, mantida por outra equipe, que gravava direto no repositório com uma credencial estática.

    O fluxo 8 da Figura 1 — de uma entidade externa diretamente para a zona de aplicação, sem passar pelo gateway — tornou-se a prioridade da análise. O DFD levou 50 minutos para ser desenhado; o fluxo encontrado justificou o resto do trabalho.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Representação | Diagrama de rede ou nenhum | DFD com fronteiras de confiança |
| Quem desenha | Especialista de segurança sozinho | Equipe do sistema com o arquiteto |
| Momento | Antes da entrada em produção | No desenho e a cada mudança relevante |
| Detalhe | Tudo ou nada | Detalhe onde há fronteira, dado sensível ou privilégio |
| Armazenamento | Imagem em apresentação | Fonte versionada junto da arquitetura |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, fronteiras de confiança não são só redes: **contas, assinaturas e projetos**, **papéis de identidade** e **serviços gerenciados** são fronteiras. Um fluxo de uma função serverless para um bucket em outra conta atravessa uma fronteira mesmo sem sair da rede do provedor. Em ambientes híbridos, o canal entre ambientes (VPN, link dedicado, agente de sincronização) deve aparecer como fluxo explícito, com sua própria análise.

## Como especificar e implementar

- "Todo sistema novo ou com mudança relevante tem um DFD com fronteiras de confiança, mantido junto da documentação de arquitetura."
- "O DFD identifica, para cada fluxo que atravessa fronteira, os dados, o canal e a forma de autenticação."
- "Mudanças que adicionam fluxos, armazenamentos ou fronteiras atualizam o DFD antes da revisão de segurança."

## Trade-offs, limitações e antipadrões

- **Trade-off:** detalhe versus velocidade. Um DFD de nível 1 feito hoje vale mais que um nível 3 perfeito daqui a um mês.
- **Antipadrão — DFD de infraestrutura:** caixas de servidores e sub-redes sem dados nem fluxos.
- **Antipadrão — modelo feito sozinho:** a equipe do sistema sabe dos fluxos que a documentação esqueceu.
- **Limitação:** o DFD representa fluxos de dados; comportamentos temporais (ordem, concorrência) e fluxos de controle de plataforma podem exigir diagramas complementares.

## Como validar

- Para cada armazenamento, perguntar quem lê e quem escreve, e conferir se todos os processos aparecem.
- Comparar o DFD com logs de rede ou de API para encontrar fluxos não desenhados.
- Pedir a alguém de fora da equipe que explique o sistema a partir do DFD.

## Como apresentar e justificar

- **Para a equipe:** "Vamos desenhar juntos por onde os dados passam. Em uma hora saímos com a lista de fluxos que precisam de atenção."
- **Para gestores:** "O modelo encontrou uma integração que gravava dados de pacientes sem passar pelos controles de borda. Corrigir agora custa dias; depois de um incidente, muito mais."

## Checklist de revisão arquitetural

- [ ] Todas as entidades externas estão representadas.
- [ ] Todo armazenamento tem os processos que leem e escrevem.
- [ ] Fronteiras de confiança estão desenhadas, inclusive contas e identidades em cloud.
- [ ] Fluxos que atravessam fronteiras estão rotulados com dados, canal e autenticação.
- [ ] O nível de detalhe é maior onde há dado sensível ou privilégio.
- [ ] A fonte do DFD está versionada.

## Questões de compreensão

**1.** Quais são as quatro perguntas do threat modeling e qual delas o DFD responde?

??? success "Resposta comentada"

    O que estamos construindo? O que pode dar errado? O que vamos fazer a respeito? Fizemos um bom trabalho? O DFD responde à primeira: é a representação do sistema sobre a qual as demais perguntas são feitas.

**2.** Por que um fluxo de dados nunca liga dois armazenamentos diretamente?

??? success "Resposta comentada"

    Porque algum processo precisa ler de um e escrever no outro. Esconder esse processo esconde quem tem as credenciais e o privilégio para mover os dados — exatamente o que interessa para encontrar ameaças.

**3.** Em cloud, cite duas fronteiras de confiança que não são fronteiras de rede.

??? success "Resposta comentada"

    Contas, assinaturas ou projetos diferentes; papéis de identidade com privilégios diferentes; a fronteira entre o cliente e um serviço gerenciado do provedor.

## Exercício de tomada de decisão

!!! question "Cenário: escopo do DFD do portal de fornecedores da Meridiana"

    O portal de fornecedores da Meridiana tem 14 microsserviços, um banco, uma fila, integração com o ERP on-premises e autenticação pelo diretório corporativo sincronizado (Módulo 3 — Aula 02). A equipe tem duas horas para a primeira sessão de threat modeling. Há três propostas de escopo para o DFD:

    - **A** — nível 2 completo, com os 14 microsserviços;
    - **B** — nível 1 com os microsserviços agregados por função, detalhando em nível 2 só os fluxos mais sensíveis;
    - **C** — apenas o diagrama de contexto, com o portal como um único processo.

    Compare as propostas com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho), escolha o nível de detalhe e indique quais fluxos você priorizaria.

??? success "Resolução de referência"

    | Critério | Peso | A — Nível 2 completo | B — Nível 1 + detalhe seletivo | C — Só contexto |
    |:---|:---|:---|:---|:---|
    | Cobertura dos fluxos de maior risco | 3 | 3 | 3 | 1 |
    | Cabe na sessão de duas horas | 3 | 1 | 3 | 3 |
    | Utilidade para aplicar STRIDE na próxima etapa | 2 | 2 | 3 | 1 |
    | Esforço de manutenção do modelo (3 = menor) | 1 | 1 | 2 | 3 |
    | **Total ponderado** | | **17** | **26** | **17** |

    **Pesos:** cobertura e tempo recebem 3 porque o objetivo da primeira sessão é sair com os fluxos que precisam de atenção, dentro do tempo disponível; a utilidade para STRIDE recebe 2; a manutenção recebe 1 porque o modelo será refinado nas sessões seguintes. **Recomendação: B.**

    - **Nível:** um DFD de nível 1 com os microsserviços agregados por função (borda, cadastro, pagamentos, integração), detalhando em nível 2 apenas o fluxo de **alteração de dados bancários** e a **integração com o ERP**.
    - **Prioridades:** (1) fluxos que vêm da internet até o gateway; (2) o fluxo de alteração de dados bancários, por estar ligado ao cenário de fraude (Módulo 1 — Aula 06); (3) o canal entre o portal em cloud e o ERP on-premises, que atravessa ambientes; (4) a dependência do diretório sincronizado.
    - **Deixado para depois (risco residual do modelo):** detalhes internos de serviços sem dado sensível, registrados como pendência no modelo.
    - **O que mudaria a decisão:** com uma sessão de um dia inteiro, ou se a equipe já tiver um modelo como código dos 14 serviços, o nível 2 completo deixa de ser caro; se o objetivo da sessão for só definir escopo com o negócio, o diagrama de contexto basta.

## Pontos-chave

- Threat modeling analisa representações do sistema; o DFD é a mais usada.
- Entidades externas, processos, armazenamentos, fluxos e fronteiras de confiança bastam para a maioria das análises.
- Fluxos que atravessam fronteiras concentram as ameaças.
- Detalhe onde há fronteira, dado sensível ou privilégio; agregue o resto.
- O modelo é vivo: versionado, desenhado com a equipe e atualizado a cada mudança relevante.

## Referências

### Fundamentação principal

- Threat Modeling Manifesto Working Group. *Threat Modeling Manifesto*. <https://threatmodelingmanifesto.org/> — definição, quatro perguntas, valores e princípios. CC BY 4.0. *(Lido.)*
- L. Osterman. *Threat Modeling Again, STRIDE per Element*. Microsoft, 2007. <https://learn.microsoft.com/ru-ru/archive/blogs/larryosterman/threat-modeling-again-stride-per-element> — elementos de DFD e categorias aplicáveis.
- NIST. *SP 800-160 Vol. 1 Rev. 1* — §3.8, pontos de vista de segurança do sistema.

### Leitura complementar

- OWASP. *Developer Guide — Threat Modeling Project*. <https://devguide.owasp.org/en/04-design/01-threat-modeling/01-threat-modeling-project/> — pytm, Threat Dragon e Cornucopia.
- H. Adkins et al. *Building Secure and Reliable Systems*. O'Reilly, 2020 — Cap. 6, *Design for Understandability*.

### Aplicação prática

- Desenhe, com a equipe de um sistema real, um DFD de nível 1 em até uma hora. Liste os fluxos que atravessam fronteiras e marque os três que serão analisados primeiro.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
