---
id: M02-L01
title: "Aula 01 — O papel do Security Architect"
public_title: "Módulo 2 — Aula 01 — O papel do Security Architect"
description: O que um arquiteto de segurança faz, quais artefatos produz, como se diferencia de engenheiros, analistas e CISO, e como se integra ao ciclo de vida dos projetos.
domain: enterprise-architecture
tier: fundamental
status: published
prerequisites: [M01-L02, M01-L06]
objectives:
  - Explicar o que é arquitetura de segurança e por que ela existe como disciplina.
  - Diferenciar as responsabilidades de Security Architect, Security Engineer, analista de segurança e CISO.
  - Identificar os artefatos que um arquiteto produz e o público de cada um.
  - Propor um modelo de engajamento proporcional ao risco para uma organização.
minutes: 60
sources: [ISO-42010-2022, NIST-SP800-160-V1R1, NIST-CSF-2, ISC2-ISSAP-2025]
further_reading: [BOOK-ANDERSON-SE3, NIST-SP800-160-V1R1, ARC42-ISO42010-SUMMARY]
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
module: M02
---

# Aula 01 — O papel do Security Architect { #o-papel-do-security-architect }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 2 · Nível 1</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min · ID técnico: M02-L01</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Você vai entender o que faz um arquiteto de segurança: não é quem configura o firewall nem quem audita o controle, mas quem garante que as decisões de segurança de uma organização sejam **coerentes entre si, proporcionais ao risco e compreensíveis por quem precisa executá-las**. A aula termina com um exercício para desenhar o modelo de atuação de um arquiteto em uma empresa real.

**Pré-requisitos:** princípios de design seguro (Módulo 1 — Aula 02) e os conceitos de ameaça, vulnerabilidade, risco e controle (Módulo 1 — Aula 06).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar o que é arquitetura de segurança e por que ela existe como disciplina.
- Diferenciar as responsabilidades de Security Architect, Security Engineer, analista de segurança e CISO.
- Identificar os artefatos que um arquiteto produz e o público de cada um.
- Propor um modelo de engajamento proporcional ao risco para uma organização.

## Conceito

### O que é arquitetura

Todo sistema tem uma arquitetura, documentada ou não. A ISO/IEC/IEEE 42010 trata a arquitetura como os **conceitos ou propriedades fundamentais** de uma entidade — na prática, seus elementos, os relacionamentos entre eles e os princípios que orientam seu desenho e sua evolução — e distingue essa arquitetura da **descrição de arquitetura**, que é o conjunto de artefatos que a expressa. *(Definição conferida em resumo público da norma no arc42 Quality Model; o texto da norma, pago, não foi consultado.)*

Essa distinção tem consequência prática: quando um sistema cresce sem que ninguém decida sobre sua estrutura, ele *ainda assim* tem uma arquitetura. Ela apenas foi definida por acidente, pela soma de decisões locais tomadas sob pressão de prazo. Grande parte do trabalho de um arquiteto de segurança em uma organização madura é tornar explícita uma arquitetura que já existe e decidir conscientemente como ela deve evoluir.

### O que é arquitetura de segurança

Arquitetura de segurança é a parte da arquitetura que trata de **como o sistema — ou a organização — atinge seus objetivos de segurança**: quais ativos importam, quais fronteiras de confiança existem, onde ficam os controles, como as decisões de acesso são tomadas e como o ambiente se recupera quando algo falha.

Ela não é uma camada adicionada depois. O NIST SP 800-160 Vol. 1 Rev. 1 trata a segurança como uma **propriedade emergente** do sistema: ela resulta da forma como os componentes são combinados, e não da soma de controles isolados. Um sistema com bons controles mal posicionados pode ser menos seguro do que um sistema com menos controles, bem posicionados.

### Por que a disciplina existe

Três problemas recorrentes justificam que alguém cuide explicitamente da arquitetura de segurança:

1. **Decisões tardias são caras.** Uma falha de desenho descoberta em um pentest antes da produção — por exemplo, um serviço interno que confia em qualquer requisição vinda da rede corporativa — raramente se corrige com uma configuração. Exige mudar fluxos, contratos de API e às vezes o modelo de identidade.
2. **Otimizações locais criam inconsistência.** Cada equipe escolhe sua própria forma de autenticar serviços, guardar segredos e registrar logs. Cada escolha isolada parece razoável; o conjunto é impossível de operar, auditar e defender.
3. **Risco de negócio e controle técnico falam línguas diferentes.** A diretoria aprova apetite a risco; a engenharia implementa regras de firewall. Sem alguém que traduza uma coisa na outra, ou o investimento em segurança não tem justificativa, ou a justificativa não se converte em controles.

### Qual problema o arquiteto resolve

O arquiteto de segurança resolve o problema da **coerência**: garante que as decisões de segurança sejam rastreáveis até um objetivo de negócio, consistentes entre sistemas, proporcionais ao risco e documentadas de forma que possam ser revisadas. Ele faz isso principalmente por meio de três alavancas:

| Alavanca | O que é | Exemplo |
|:---|:---|:---|
| **Padronização** | Definir princípios, padrões e arquiteturas de referência que as equipes reutilizam. | Um padrão único de autenticação entre serviços, com implementação de referência. |
| **Revisão** | Avaliar soluções novas ou alteradas contra requisitos, ameaças e padrões. | Design review de uma nova API exposta a parceiros. |
| **Decisão documentada** | Registrar escolhas significativas, suas alternativas e consequências. | ADR justificando por que o acesso remoto usará ZTNA e não VPN. |

## Fundamentos técnicos

### O que o arquiteto faz, na prática

As atividades se distribuem ao longo do ciclo de vida de uma solução:

| Etapa | Atividade do arquiteto | Artefato típico |
|:---|:---|:---|
| Concepção | Classificar o risco da iniciativa e decidir o nível de envolvimento | Ficha de triagem de risco |
| Requisitos | Traduzir objetivos de negócio e obrigações em requisitos de segurança | Security Requirements Specification |
| Desenho | Modelar ameaças, posicionar controles, avaliar alternativas | Threat model, diagramas, ADRs |
| Construção | Orientar a implementação dos padrões e aprovar desvios | Padrões, guardrails, registros de exceção |
| Transição | Verificar se o que foi construído corresponde ao que foi desenhado | Checklist de revisão arquitetural |
| Operação | Acompanhar indicadores e incorporar lições aprendidas | Métricas, revisão de exceções, atualização de padrões |

Note que o arquiteto **não executa a maior parte desses controles**. Ele define o que precisa ser verdade, onde, e como se verifica — e garante que quem implementa tenha o necessário para fazê-lo.

### Papéis vizinhos: onde termina a responsabilidade

Confusão de papéis é uma das principais fontes de atrito. A tabela abaixo descreve as responsabilidades típicas; organizações reais variam, mas a distinção conceitual se mantém.

| Papel | Pergunta central | Horizonte | Entrega típica |
|:---|:---|:---|:---|
| **CISO** | *Quanto risco a organização aceita e onde investir?* | Estratégico (anos) | Estratégia, orçamento, apetite a risco, reporte ao conselho |
| **Enterprise Security Architect** | *Quais princípios, padrões e capacidades valem para toda a organização?* | Tático-estratégico (1–3 anos) | Princípios, padrões, arquiteturas de referência, roadmap de capacidades |
| **Solution Security Architect** | *Esta solução específica atende aos requisitos de segurança com risco aceitável?* | Projeto (meses) | Requisitos, threat model, desenho de controles, ADRs |
| **Security Engineer** | *Como implementar e operar este controle corretamente?* | Implementação (semanas) | Configurações, automações, pipelines, integrações |
| **Analista de segurança / SOC** | *O que está acontecendo agora e como responder?* | Operacional (horas a dias) | Detecção, investigação, resposta |
| **GRC / Auditoria** | *Os controles exigidos existem e funcionam?* | Ciclo de auditoria | Avaliações de conformidade, evidências |

Essa tabela materializa a distinção **estratégia × operação**. Estratégia decide *o que* proteger e *quanto* investir; arquitetura decide *como estruturar* a proteção; engenharia decide *como implementar*; operação garante que *funcione no dia a dia*. Um arquiteto que passa a maior parte do tempo implementando controles está, na prática, atuando como engenheiro — o que pode ser necessário em equipes pequenas, mas deixa a função arquitetural sem dono.

### Perfis de arquiteto

| Perfil | Foco | Profundidade típica |
|:---|:---|:---|
| Enterprise Security Architect | Coerência de toda a organização, governança e capacidades | Ampla, com visão de negócio |
| Solution Security Architect | Projetos e produtos específicos | Ampla, com profundidade nas tecnologias do projeto |
| Domain Architect (identidade, rede, dados, aplicações) | Um domínio técnico em toda a organização | Profunda em um domínio |
| Cloud / Hybrid Security Architect | Plataformas cloud e sua integração com o ambiente existente | Profunda em provedores e integração |
| Security Architecture Consultant | Avaliações e desenhos para clientes | Ampla, com forte comunicação |

O novo outline do ISSAP, vigente desde agosto de 2025, organiza o conhecimento esperado de um arquiteto em quatro domínios — governança, risco e conformidade; modelagem de arquitetura; arquitetura de infraestrutura e sistemas; e arquitetura de identidade — o que reflete bem a combinação de visão de governança com profundidade técnica que o papel exige.

### Competências do papel

O arquiteto precisa de **largura** suficiente para entender todos os domínios envolvidos em uma solução e **profundidade** em pelo menos um ou dois deles, para que suas recomendações sejam tecnicamente críveis. Além disso:

- **Pensamento em sistemas:** enxergar dependências, efeitos colaterais e pontos únicos de falha.
- **Raciocínio de risco:** comparar cenários pela probabilidade e pelo impacto no negócio, não pela gravidade técnica isolada.
- **Comunicação em múltiplos registros:** o mesmo desenho precisa ser explicado a um engenheiro, a um gerente de produto e a um diretor financeiro.
- **Negociação:** quase toda decisão de arquitetura troca segurança por custo, prazo, desempenho ou experiência do usuário.

### Como o papel se relaciona com outros conceitos

- Com **governança** (Módulo 3): o arquiteto transforma políticas em padrões aplicáveis. O CSF 2.0 introduziu a função *Govern*, que inclui a definição de papéis, responsabilidades e autoridades de cibersegurança — o lugar formal onde o papel do arquiteto deve estar descrito.
- Com **threat modeling** (Módulo 4): é a principal ferramenta analítica do arquiteto de soluções.
- Com **engenharia de segurança**: o arquiteto define o *quê* e o *porquê*; o engenheiro, o *como*. A qualidade depende do diálogo entre os dois.

## Exemplo empresarial

!!! example "Aurora Pagamentos — nova API para parceiros"

    A Aurora Pagamentos decide expor uma API para que lojistas parceiros consultem o status de transações. O time de produto quer lançar em oito semanas.

    **Sem um arquiteto envolvido desde o início**, o time desenvolve a API reutilizando o serviço interno de consultas, que confia em qualquer chamada vinda da rede corporativa. Um gateway é colocado na frente "para segurança". Na revisão final, o pentest mostra que um parceiro autenticado consegue consultar transações de outros parceiros alterando um identificador na URL — uma falha de autorização em nível de objeto. Corrigir exige mudar o serviço interno, que é usado por outros quatro sistemas. O lançamento atrasa cinco semanas.

    **Com o arquiteto envolvido na concepção**, a triagem classifica a iniciativa como de alto risco: dados financeiros, exposição externa, novo tipo de identidade (parceiros). Em duas sessões de desenho, o arquiteto e o time registram três decisões:

    1. A autorização por parceiro será feita no próprio serviço, a partir de um identificador de parceiro presente no token — e não apenas no gateway.
    2. Parceiros terão identidades emitidas por um provedor dedicado, separado do diretório de funcionários.
    3. Toda consulta será registrada com o identificador do parceiro, para detecção de enumeração.

    O custo foi de cerca de duas semanas de desenho e ajustes; o pentest final encontrou apenas achados de baixa severidade.

O exemplo mostra o padrão mais comum: o problema não era a falta de um controle (havia um gateway), mas o **posicionamento** do controle e uma premissa de confiança que ninguém tinha examinado.

## Arquitetura tradicional versus recomendada

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m02-l01-engagement.mmd"
```

<figcaption>Figura 1 — Segurança como etapa final versus arquitetura integrada ao ciclo de vida.</figcaption>
</figure>

| Aspecto | Segurança como portão final | Arquitetura integrada ao ciclo de vida |
|:---|:---|:---|
| Momento da participação | Antes da produção | Desde a concepção, proporcional ao risco |
| Custo de corrigir achados | Alto: muda código, contratos e dependências | Baixo: muda desenho e requisitos |
| Relação com as equipes | Auditor que aprova ou reprova | Parceiro que fornece padrões e decide junto |
| Escalabilidade | Fila de revisões; o arquiteto vira gargalo | Padrões reutilizáveis; revisões reservadas para o que é novo ou de alto risco |
| Rastreabilidade | Achados em relatório de pentest | Requisitos, ameaças e decisões registrados |

O modelo integrado não elimina a revisão final — ele a torna uma **verificação** do que foi desenhado, em vez de uma descoberta tardia.

## Controles e padrões relevantes

O arquiteto raramente "possui" um controle técnico, mas é responsável por um conjunto de **controles de governança da arquitetura**:

| Elemento | Objetivo | Referência |
|:---|:---|:---|
| Papéis e responsabilidades de arquitetura definidos | Evitar lacunas e sobreposição entre arquitetura, engenharia e operação | NIST CSF 2.0, função Govern (papéis, responsabilidades e autoridades) |
| Processo de engajamento e triagem por risco | Garantir que iniciativas de alto risco passem por desenho e revisão | Prática de mercado; detalhado em Módulo 16 — Aula 06 |
| Princípios e padrões de segurança publicados | Dar às equipes regras reutilizáveis e verificáveis | Aula 04 |
| Registro de decisões (ADRs) | Tornar decisões rastreáveis e revisáveis | Aula 08 |
| Processo de exceções com prazo e responsável | Aceitar desvios de forma consciente e temporária | Aula 04 |
| Engenharia de segurança no ciclo de vida | Integrar segurança aos processos de engenharia de sistemas | NIST SP 800-160 Vol. 1 Rev. 1 |

## Aplicabilidade: on-premises, cloud e híbrido

O papel é o mesmo nos três ambientes, mas o **ponto de alavancagem** muda.

| Aspecto | On-premises | Cloud | Híbrido |
|:---|:---|:---|:---|
| Onde as decisões se materializam | Topologia de rede, zonas, servidores e janelas de mudança | Contas e assinaturas, políticas como código, serviços gerenciados | Pontos de integração: identidade, conectividade, DNS, logs |
| Velocidade de mudança | Lenta; mudanças passam por comitês | Rápida; equipes criam recursos em minutos | Desigual; o lado mais lento limita o mais rápido |
| Forma mais eficaz de influência | Padrões de configuração e revisão de mudanças | **Guardrails** automatizados e "caminhos pavimentados" (paved roads) | Políticas que valem para os dois lados e um dono claro para cada integração |
| Responsabilidade | Quase toda da organização | Compartilhada com o provedor, conforme o modelo de serviço | Compartilhada **e** fragmentada: o risco se concentra nas fronteiras |
| Risco típico de arquitetura | Rede plana e confiança implícita na rede interna | Permissões excessivas e configurações públicas por engano | Identidade e confiança atravessando ambientes sem controle equivalente |
| Dependência crítica | Disponibilidade do datacenter | Disponibilidade do provedor e da conta de gestão | Conectividade e sincronização de identidade entre ambientes |

**Particularidade do ambiente híbrido:** em uma empresa híbrida, o arquiteto frequentemente descobre que *ninguém* é dono da integração. A equipe de infraestrutura cuida do datacenter, a equipe de cloud cuida das contas, e o túnel, a sincronização de identidades e o encaminhamento de DNS entre os dois ficam sem responsável. Nomear um dono para cada ponto de integração é uma das primeiras e mais valiosas ações de arquitetura nesse cenário.

## Como especificar e implementar

Para estruturar o papel em uma organização, o arquiteto precisa definir **quando** é envolvido e **com que profundidade**. Um modelo de engajamento proporcional ao risco funciona melhor do que revisar tudo com o mesmo rigor.

### Gatilhos de engajamento

Uma iniciativa deve envolver arquitetura de segurança quando apresenta pelo menos um dos gatilhos abaixo:

- Nova exposição externa (internet, parceiros, clientes).
- Processamento de dados classificados como confidenciais ou regulados (dados de cartão, dados pessoais sensíveis).
- Novo provedor de identidade, novo tipo de identidade ou mudança no modelo de autorização.
- Nova integração com terceiros ou novo fornecedor SaaS com acesso a dados.
- Novo ambiente de hospedagem (nova conta cloud, novo datacenter, nova região).
- Desvio de um padrão corporativo.

### Níveis de revisão

| Nível | Quando | Atividades | Prazo de referência |
|:---|:---|:---|:---|
| **Autoatendimento** | Nenhum gatilho; solução segue padrões existentes | Equipe preenche checklist e usa arquiteturas de referência | Sem espera |
| **Revisão leve** | Um gatilho de risco moderado | Sessão de 1 h, revisão de diagrama, registro de decisões | Até 5 dias úteis |
| **Revisão completa** | Gatilhos de alto risco ou combinação de gatilhos | Requisitos, threat model, ADRs, revisão antes da produção | Acompanha o projeto |

Os prazos são exemplos para calibrar expectativas; cada organização define os seus. O ponto essencial é que o modelo **reserve a atenção do arquiteto para o que é novo ou arriscado** e torne o restante autoatendido por meio de padrões.

## Trade-offs, limitações e antipadrões

| Antipadrão | Sintoma | Consequência | Correção |
|:---|:---|:---|:---|
| **Torre de marfim** | Padrões escritos sem contato com quem implementa | Padrões ignorados ou contornados | Padrões construídos com engenharia, com implementação de referência |
| **Portão burocrático** | Toda mudança espera aprovação do arquiteto | O arquiteto vira gargalo; equipes evitam envolvê-lo | Triagem por risco e autoatendimento |
| **Arquiteto ferramenta** | Toda resposta começa com um produto | Soluções caras que não tratam o risco real | Começar por requisitos e ameaças; produto é consequência |
| **Arquitetura de slides** | Diagramas bonitos que não correspondem ao ambiente | Decisões baseadas em ficção | Diagramas versionados e verificados contra o ambiente |
| **Arquiteto de checklist** | Revisão limitada a conformidade | Sistemas conformes e inseguros | Avaliar ameaças e fluxos, não apenas a presença de controles |
| **Herói sem registro** | Decisões vivem na cabeça de uma pessoa | Ninguém sabe por que algo é como é; decisões são refeitas | ADRs e documentação de padrões |
| **Excesso de engenharia** | Controles máximos em tudo | Custo e atrito desproporcionais; perda de credibilidade | Proporcionalidade ao risco e ao valor do ativo |

**Limitação estrutural do papel:** o arquiteto influencia, mas raramente tem autoridade direta sobre orçamento ou equipes. Sua efetividade depende de credibilidade técnica, de patrocínio da liderança e de processos de governança que deem peso às decisões de arquitetura.

## Como validar

O valor da função de arquitetura pode ser medido. Indicadores úteis:

| Indicador | O que revela | Sinal de alerta |
|:---|:---|:---|
| % de iniciativas de alto risco com arquiteto envolvido na concepção | Se o engajamento acontece cedo | Envolvimento concentrado na semana anterior à produção |
| Tempo de resposta das revisões | Se o arquiteto é gargalo | Fila crescente; equipes "pulando" a revisão |
| Achados de pentest atribuíveis a falhas de desenho | Qualidade do desenho | Repetição da mesma classe de falha em projetos diferentes |
| Adoção de arquiteturas de referência | Se os padrões são úteis | Cada equipe reinventa sua solução |
| Exceções abertas e vencidas | Se desvios são temporários e controlados | Exceções sem prazo ou renovadas indefinidamente |
| Decisões registradas por projeto de alto risco | Se há rastreabilidade | Projetos críticos sem nenhum ADR |

## Como apresentar e justificar

A mesma proposta — por exemplo, criar um modelo de engajamento por risco — precisa de argumentos diferentes para cada público:

| Público | O que importa | Como apresentar |
|:---|:---|:---|
| CISO e diretoria | Risco, custo e previsibilidade | "Hoje 40% dos achados críticos de pentest vêm de falhas de desenho, corrigidas com atraso médio de quatro semanas. Envolver arquitetura na concepção dos projetos de alto risco reduz retrabalho e protege prazos de lançamento." |
| Engenharia | Autonomia e velocidade | "Projetos sem gatilho de risco passam a ser autoatendidos com padrões e implementações de referência; a revisão fica reservada para o que é realmente novo." |
| Produto | Prazo e previsibilidade | "Duas sessões de desenho no início custam menos do que cinco semanas de correção no fim." |

Use números da própria organização sempre que possível. Os percentuais acima são ilustrativos.

## Checklist de revisão arquitetural

Use para avaliar se a função de arquitetura de segurança está bem estruturada em uma organização:

- [ ] Existe uma descrição formal do papel de arquitetura de segurança, com responsabilidades e limites em relação a engenharia, operação e GRC.
- [ ] Há critérios objetivos (gatilhos) que determinam quando uma iniciativa envolve arquitetura.
- [ ] Os níveis de revisão são proporcionais ao risco e têm prazos conhecidos.
- [ ] Princípios e padrões estão publicados e acessíveis às equipes.
- [ ] Decisões significativas são registradas em ADRs.
- [ ] Exceções têm responsável, prazo e controle compensatório.
- [ ] Cada ponto de integração entre ambientes (on-premises e cloud) tem um dono nomeado.
- [ ] Indicadores da função são acompanhados e reportados.

## Questões de compreensão

**1.** Uma empresa não tem nenhum diagrama atualizado de seus sistemas. É correto dizer que ela "não tem arquitetura"?

??? success "Resposta comentada"

    Não. Todo sistema tem uma arquitetura — elementos, relacionamentos e princípios que de fato orientam sua estrutura. O que falta é a **descrição** dessa arquitetura. A ISO/IEC/IEEE 42010 faz exatamente essa distinção. Na prática, a arquitetura dessa empresa foi definida implicitamente por decisões locais, e o primeiro trabalho do arquiteto é torná-la explícita.

**2.** Em uma reunião, o gerente de infraestrutura pede ao arquiteto de segurança que configure as regras do novo firewall de datacenter. Por que essa tarefa não deveria, idealmente, ser do arquiteto? O que o arquiteto deveria entregar?

??? success "Resposta comentada"

    Configurar regras é implementação, papel de engenharia. O arquiteto deveria entregar o **modelo de zonas e a política de comunicação entre zonas** (quais zonas existem, quais fluxos são permitidos entre elas, com que protocolos e controles), além dos critérios de verificação. Em equipes pequenas o arquiteto pode acumular a implementação, mas, se isso virar regra, a função arquitetural fica sem dono.

**3.** Por que o modelo de "segurança como portão final" tende a transformar o arquiteto em gargalo?

??? success "Resposta comentada"

    Porque concentra todas as decisões em um único ponto, no momento em que mudanças são mais caras. Cada achado gera retrabalho e negociação, a fila cresce e as equipes passam a evitar o processo. O modelo integrado distribui as decisões ao longo do ciclo e torna autoatendido o que segue padrões.

**4.** Em um ambiente híbrido, qual é o risco de arquitetura mais característico, e qual ação simples o mitiga?

??? success "Resposta comentada"

    A falta de dono para os pontos de integração (identidade sincronizada, conectividade, DNS e logs entre ambientes), onde a confiança atravessa fronteiras sem controle equivalente nos dois lados. Nomear um responsável para cada ponto de integração, com requisitos e indicadores, é uma ação simples e de alto impacto.

**5.** Qual é a diferença entre a pergunta central do CISO e a do Enterprise Security Architect?

??? success "Resposta comentada"

    O CISO decide **quanto risco aceitar e onde investir** (estratégia). O Enterprise Security Architect decide **quais princípios, padrões e capacidades estruturam a proteção** em toda a organização para que essa estratégia se realize (arquitetura). Um define o destino e o orçamento; o outro, a estrutura que leva até lá.

## Exercício de tomada de decisão

!!! question "Cenário: um arquiteto para quarenta projetos"

    A Aurora Pagamentos contratou seu primeiro Security Architect. A empresa tem seis squads de produto, uma equipe de infraestrutura e uma equipe de cloud, e prevê cerca de quarenta iniciativas no próximo ano — dez delas com exposição externa ou dados de cartão. O CISO pede uma proposta de modelo de atuação. Há três alternativas:

    - **A — Revisão universal:** toda iniciativa passa por revisão completa antes da produção.
    - **B — Triagem por risco com autoatendimento:** gatilhos de risco definem o nível de revisão; iniciativas sem gatilho usam padrões e checklist.
    - **C — Arquiteto embarcado:** o arquiteto participa das cerimônias de dois squads críticos por trimestre, alternando ao longo do ano.

    Compare as alternativas usando os critérios cobertura de risco, escalabilidade, custo para as equipes e rastreabilidade. Recomende uma e declare o risco residual.

??? success "Resolução de referência"

    **Matriz de decisão** (1 = fraco, 3 = forte; pesos refletem as prioridades declaradas pelo CISO):

    | Critério | Peso | A — Universal | B — Triagem | C — Embarcado |
    |:---|:---|:---|:---|:---|
    | Cobertura de risco | 3 | 3 | 3 | 1 |
    | Escalabilidade | 2 | 1 | 3 | 1 |
    | Custo para as equipes | 2 | 1 | 2 | 3 |
    | Rastreabilidade | 1 | 2 | 3 | 1 |
    | **Total ponderado** | | **15** | **22** | **12** |

    **Recomendação: B.** Com uma única pessoa, a revisão universal (A) cria uma fila incompatível com quarenta iniciativas e incentiva as equipes a contornar o processo. O modelo embarcado (C) dá profundidade, mas deixa as dez iniciativas de alto risco descobertas em boa parte do ano. A triagem concentra a atenção nas dez iniciativas de maior risco e torna as demais autoatendidas.

    **Condições para B funcionar:** gatilhos publicados; checklist de autoatendimento; ao menos duas arquiteturas de referência no primeiro trimestre (por exemplo, API externa e integração com SaaS).

    **Risco residual:** iniciativas que se classificam incorretamente como "sem gatilho". Mitigação: amostragem trimestral de 20% das iniciativas autoatendidas e revisão dos gatilhos a cada semestre.

    Uma resposta que combine B com elementos de C — por exemplo, embarcar o arquiteto no squad de pagamentos durante a construção da API de parceiros — também é defensável, desde que a cobertura das demais iniciativas de alto risco seja preservada.

## Pontos-chave

- Todo sistema tem arquitetura; o trabalho do arquiteto é torná-la explícita e conduzir sua evolução de forma consciente.
- Segurança é uma propriedade emergente: o posicionamento dos controles importa tanto quanto sua existência.
- O arquiteto decide o *quê*, o *onde* e o *porquê*; a engenharia decide o *como*; a operação garante o funcionamento contínuo.
- Envolvimento proporcional ao risco, com autoatendimento por padrões, evita que o arquiteto vire gargalo.
- Em ambientes híbridos, os maiores riscos ficam nas integrações — e cada uma precisa de um dono.

## Referências

- ISO/IEC/IEEE. *42010:2022 — Software, systems and enterprise — Architecture description*. Edição 2, 2022. <https://committee.iso.org/standard/74393.html> — norma paga, não consultada na íntegra; a descrição usada nesta aula se apoia na página oficial da norma e em resumos públicos.
- G. Starke. *ISO/IEC/IEEE 42010:2022 — Architecture Description* (resumo). arc42 Quality Model. <https://quality.arc42.org/standards/iso-42010>. *(Lido em 2026-10-23; fonte secundária.)*
- NIST. *SP 800-160 Vol. 1 Rev. 1 — Engineering Trustworthy Secure Systems*. Novembro de 2022. <https://csrc.nist.gov/news/2022/guidance-on-engineering-trustworthy-secure-systems> — gratuito.
- NIST. *The NIST Cybersecurity Framework (CSF) 2.0*, CSWP 29. Fevereiro de 2024. <https://doi.org/10.6028/NIST.CSWP.29> — gratuito.
- ISC2. *New exam outlines for ISC2 advanced certifications* (ISSAP vigente desde 01/08/2025). <https://www.isc2.org/insights/2025/07/new-exam-outlines-for-isc2-advanced-certifications> — gratuito.

### Leituras de aprofundamento

Incluídas na revisão bibliográfica de 2026-10-23, **depois** da escrita desta aula: complementam e permitem conferir o conteúdo, mas não foram a base original do texto. A situação de cada leitura está entre parênteses.

- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020, Cap. 1, §1.2 *A framework* (p. 4) — as quatro perspectivas de um controle: policy, mechanism, assurance e incentive. *(lido.)*
- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020, Cap. 1, §1.7 *Definitions* (p. 11) — a diferença entre componente *trusted* e *trustworthy*. *(lido.)*
- NIST. *SP 800-160 Vol. 1 Rev. 1*, 2022, Apêndice D.2 *Design Considering Emergence* (p. 73) e Apêndice F *Trustworthiness and Assurance* (p. 102) — segurança como propriedade emergente e o papel da evidência. *(localizado pelo sumário.)*

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
| Revisão bibliográfica | 2026-10-23 — [registro da revisão retroativa](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/retroactive-review-m02.md) |
