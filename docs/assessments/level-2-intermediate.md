---
id: AS-MID
title: "Avaliação intermediária — Cooperativa Buriti Alimentos"
description: Avaliação intermediária dos Níveis 1 e 2 — o estudante diagnostica a arquitetura de uma cooperativa agroindustrial fictícia, redesenha segmentação e acesso remoto, decide a identidade híbrida e o modelo de privilégios, aplica Zero Trust a recursos reais, trata sistemas legados, projeta backup resistente a ransomware, propõe To-Be, transição e ADR e define validação e comunicação, com rubrica e critérios objetivos de correção.
status: published
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
---

# Avaliação intermediária — Cooperativa Buriti Alimentos

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Avaliação intermediária · Níveis 1 e 2 · Módulos 3 a 8</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">6 a 8 h · 8 tarefas · 100 pontos</span>
</div>

## Instruções

- Esta avaliação encerra o **Nível 2 — Arquiteturas de Infraestrutura** (Módulos 5 a 8) e usa o que você aprendeu no Nível 1 sobre risco, governança e threat modeling (Módulos 3 e 4). Ela não repete a [avaliação integradora do Nível 1](level-1-integrative.md): lá o foco era identificar riscos e escolher controles; aqui é **projetar a infraestrutura** — rede, identidade, Zero Trust, legados e recuperação — sob restrições reais de operação.
- Faça as oito tarefas em um documento próprio. Diagramas podem ser desenhados à mão, em Mermaid ou em qualquer ferramenta.
- **Aprovação:** 70 pontos ou mais **e** nenhuma tarefa avaliada como *Insuficiente*.
- Use os modelos do portal quando ajudarem: [ADR](../artifacts/architecture-decision-record.md), [Security Architecture Assessment](../artifacts/security-architecture-assessment.md), [Risk Register](../artifacts/risk-register.md), [Security Control Matrix](../artifacts/security-control-matrix.md) e [Threat Model](../artifacts/threat-model.md).
- A correção usa os **critérios objetivos** de cada tarefa e a [rubrica](#rubrica). Confira o [gabarito comentado](answers/level-2-intermediate.md) somente ao final.
- Esta avaliação não é aconselhamento jurídico: quando uma tarefa envolver LGPD, contratos ou exigências de seguradora, indique a natureza da obrigação e o que precisa ser confirmado com o jurídico ou com o encarregado de dados.

## Cenário

A **Cooperativa Buriti Alimentos** (organização fictícia) processa leite e grãos de 9 mil cooperados — a maioria pessoas físicas, produtores rurais. Tem uma sede administrativa com datacenter, **três unidades fabris** (laticínio, esmagamento de soja e ração) e um centro de distribuição. São 2.400 colaboradores; a TI tem 14 pessoas, três delas em segurança, e um provedor de serviços gerenciados de segurança monitora alertas em horário comercial, avisando por e-mail fora dele. O conselho de administração quer lançar em **seis meses** o **portal do cooperado**, em nuvem pública, onde o produtor consultará entregas, análises de qualidade e pagamentos.

Fatos levantados em entrevistas e na documentação:

1. **Rede.** O datacenter da sede tem uma única VLAN de servidores, sem regras entre eles. As unidades fabris e o centro de distribuição ligam-se à sede por MPLS, com VPN IPsec de contingência. Cada unidade fabril tem uma **rede de automação** (CLPs, supervisório SCADA e historiador), separada da rede corporativa por um firewall com uma regra que libera **qualquer tráfego** entre o historiador e a VLAN de servidores "para os relatórios de produção". O Wi-Fi corporativo usa senha compartilhada e dá acesso à rede de escritórios.
2. **Identidade.** Um domínio Active Directory, com dois controladores de domínio na sede e um em cada unidade, sincronizado com um provedor de identidade em nuvem por **autenticação de passagem** (dois agentes, nos controladores da sede). E-mail, portal de RH (SaaS) e o futuro portal do cooperado autenticam no provedor em nuvem. Os dois **administradores globais** da nuvem são contas **sincronizadas** do AD que também são administradoras do domínio. Os cinco analistas de infraestrutura usam a **própria conta de domínio, membro de Domain Admins**, no dia a dia. Há seis contas de serviço com SPN, quatro delas em Domain Admins, todas com RC4 habilitado. MFA (notificação no celular) existe só para o e-mail, e só fora da rede corporativa.
3. **Acesso remoto.** Uma VPN SSL autenticada com usuário e senha do AD, **sem MFA**, atende 420 usuários (vendas, gestores e TI) e dá acesso à rede inteira. Três fornecedores — do ERP, da automação (integrador do SCADA) e da folha de pagamento — usam **contas de VPN compartilhadas**, com senhas que não mudam há anos. O integrador do SCADA acessa os historiadores e as estações de engenharia das unidades.
4. **Legados.** O **ERP** roda em Windows Server 2012 R2, sem suporte, com banco SQL Server 2014; a troca por um ERP em SaaS está prevista para daqui a **24 meses**. O **servidor de etiquetas**, no datacenter da sede, atende o centro de distribuição e depende de **SMBv1**. O **historiador** da unidade 1 roda Windows Server 2008 R2, certificado pelo integrador, que não admite agentes nem atualizações. O **MES** das unidades autentica usuários no AD por **bind LDAP simples sem TLS**.
5. **Portal do cooperado.** Exibirá entregas, análises e pagamentos, com dados bancários do cooperado; precisa de dados do ERP. A equipe de desenvolvimento propôs que o portal consulte o banco do ERP por meio da VPN site a site com a nuvem.
6. **Backup.** Um appliance de backup **ingressado no domínio** grava em um NAS no próprio datacenter; uma fita semanal fica na sala de servidores. Nunca houve restauração completa testada.
7. **Incidente.** Há quatro meses, a conta compartilhada do integrador do SCADA conectou-se à VPN às 3h, a partir de um endereço no exterior, e **varreu a rede das unidades por duas horas**. O provedor de segurança gerou um alerta por e-mail, que só foi lido **nove dias depois**. Não há evidência de alteração em sistemas; a investigação foi inconclusiva sobre o que foi acessado.
8. **BIA** (aprovada pelos donos dos processos):

    | Processo | Dono | MTD | RPO |
    |:---|:---|:---|:---|
    | Recebimento e produção nas unidades fabris | Diretor industrial | 8 h (o MES opera até 4 h sem o ERP) | 4 h |
    | Faturamento e expedição | Diretora comercial | 24 h | 1 h |
    | Pagamento aos cooperados | Diretor financeiro | 72 h | 24 h |
    | Portal do cooperado (após o lançamento) | Diretor de relacionamento com cooperados | 48 h | 24 h |

9. **Governança.** O conselho aprovou como apetite e tolerância: "nenhum terceiro com acesso amplo à rede; risco alto que possa parar a produção só pode ser aceito pelo diretor industrial, por no máximo 90 dias; dados pessoais e bancários de cooperados não podem ser acessíveis pela internet sem autenticação multifator".
10. **Obrigações e contratos.** A cooperativa é controladora de dados pessoais de cooperados e de colaboradores (LGPD). O contrato com uma grande rede varejista exige "MFA em todo acesso remoto e plano de resposta a incidentes testado anualmente". A renovação do **seguro cibernético**, em **cinco meses**, depende de MFA no acesso remoto e de cópia de backup offline ou imutável, segundo o questionário da seguradora. O plano estratégico adota o NIST CSF 2.0 como referência.
11. **Restrições.** Orçamento para no máximo **quatro iniciativas estruturais em 12 meses**; as unidades fabris só param em **janelas de manutenção mensais de 6 horas, aos domingos**; os sistemas de automação certificados não aceitam agentes; duas pessoas administram o AD; a diretoria prefere serviços gerenciados. O projeto do portal e o contrato com o provedor de serviços gerenciados de segurança têm orçamentos próprios, fora das quatro iniciativas.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/as-mid-as-is.mmd"
```

<figcaption>Figura 1 — Arquitetura atual da Cooperativa Buriti (As-Is).</figcaption>
</figure>

### Partes interessadas

| Parte | Interesse principal |
|:---|:---|
| Diretor industrial | Produção sem paradas; dono dos aceites de risco que possam parar a produção |
| Diretora comercial | Faturamento e expedição; contrato com a rede varejista |
| Diretor financeiro | Pagamento aos cooperados; custo do seguro |
| Diretor de relacionamento com cooperados | Lançar o portal em seis meses, com boa experiência para produtores rurais |
| Encarregado de dados | Dados pessoais e bancários de cooperados e colaboradores |
| Coordenador de segurança e gerente de TI | Viabilidade com 14 pessoas; operação das soluções |
| Integrador do SCADA | Continuar dando suporte às unidades, com o mínimo de mudança |

## Tarefa 1 — Diagnóstico do As-Is e riscos (15 pontos)

Entregue: (a) as **zonas e fronteiras de confiança** atuais e os **caminhos** pelos quais quem tivesse a credencial do fato 7 alcançaria o historiador, os controladores de domínio e o backup; (b) o incidente do fato 7 como **sequência do MITRE ATT&CK** (com a versão usada), com pelo menos quatro passos — os que a investigação não confirmou marcados como hipótese — e, para cada um, o controle que o teria interrompido ou detectado; (c) os **cinco cenários de risco** mais relevantes no formato do risk register (Módulo 3 — Aula 06), com dono, natureza da obrigação envolvida e comparação com a tolerância do fato 9.

**Critérios objetivos:** reconhece como fronteiras inexistentes ou fracas a rede plana de servidores, a regra irrestrita do historiador, a VPN com acesso à rede inteira e as contas compartilhadas; os caminhos usam fatos do cenário; a sequência ATT&CK registra a versão, usa técnicas existentes nela e é coerente com o fato 7, distinguindo o que foi observado do que é hipótese; pelo menos três dos cinco cenários estão entre acesso de terceiro, ransomware alcançando o backup pelo domínio, credenciais privilegiadas expostas, legados sem suporte e exposição de dados de cooperados pelo portal; os donos seguem a governança; a LGPD é tratada como lei, as exigências da rede varejista e da seguradora como obrigações contratuais e o CSF como adoção voluntária.

## Tarefa 2 — Segmentação e acesso remoto (15 pontos)

Entregue: (a) o **modelo de zonas To-Be**, incluindo a separação entre a rede de automação e a corporativa, com os **fluxos permitidos** do historiador e dos controladores de domínio; (b) o desenho do **acesso remoto** de colaboradores e de fornecedores, com uma **matriz ponderada** comparando pelo menos três alternativas para o acesso do integrador do SCADA (critérios, pesos justificados, notas e total); (c) a política para o Wi-Fi corporativo.

**Critérios objetivos:** introduz uma zona intermediária entre automação e corporativo, eliminando a regra irrestrita; nenhum terceiro recebe acesso à rede — o acesso é nominal, com MFA, por aplicação ou sessão intermediada, com aprovação e gravação; a matriz está correta aritmeticamente, tem pesos justificados e aplica **antes da soma** o critério eliminatório da governança ("nenhum terceiro com acesso amplo à rede"); colaboradores remotos passam a ter MFA, com autenticação resistente a phishing para contas privilegiadas; o Wi-Fi deixa de usar senha compartilhada para a rede corporativa (802.1X ou rede isolada).

## Tarefa 3 — Identidade híbrida e privilégios (15 pontos)

Entregue: (a) a decisão sobre o **método de autenticação híbrida**, ligada à BIA e ao cenário de ransomware; (b) o desenho das **contas administrativas por plano** — separação de contas, administradores da nuvem, privilégio just-in-time, estações dedicadas e contas de emergência; (c) o plano para as **contas de serviço** com SPN e RC4; (d) o **ciclo de vida** das contas de fornecedores.

**Critérios objetivos:** mantém a sincronização de hash de senha ao menos como contingência, justificando pela indisponibilidade do datacenter; administradores da nuvem passam a ser contas somente em nuvem, com autenticação resistente a phishing; nenhuma conta de uso diário pertence a Domain Admins; contas de serviço saem de Domain Admins, migram para contas gerenciadas quando possível, usam AES e têm SPNs auditados; contas de fornecedor são nominais, com patrocinador interno, data de término e revisão; a sequência cabe em uma equipe de duas pessoas de AD.

## Tarefa 4 — Zero Trust no portal, no ERP e no historiador (10 pontos)

Entregue: (a) para o portal do cooperado, o ERP e o historiador, o **PDP** (motor e administrador de política), o **PEP** e as **fontes de dados** da decisão; (b) a **política de acesso** do portal para cooperados e para funcionários do atendimento, com o **modo de falha** do PDP; (c) como o portal obtém dados do ERP **sem expô-lo**.

**Critérios objetivos:** cada recurso tem PEP identificado e não contornável; a política usa identidade, método de autenticação (MFA, conforme a governança), contexto e autorização por objeto — o cooperado vê só os próprios dados; o modo de falha é justificado pelo MTD; a integração usa uma fachada ou API no datacenter, com autenticação do serviço (mTLS ou identidade de workload) e operações mínimas, e rejeita a proposta de consultar o banco do ERP pela VPN.

## Tarefa 5 — Sistemas legados (10 pontos)

Para o ERP, o historiador, o servidor de etiquetas e o MES, entregue a **decisão** (substituir, suporte alternativo, isolar com compensatórios ou aceitar), os **compensatórios verificáveis**, o **dono**, o **prazo** e a **evidência periódica**; e a sequência para desligar o SMBv1 e reduzir NTLM e RC4.

**Critérios objetivos:** as decisões são específicas por sistema (não "isolar tudo"); os compensatórios tratam o mesmo risco que o controle ausente e têm teste; exceções que possam parar a produção respeitam a governança (diretor industrial, até 90 dias, renováveis só por nova decisão); o historiador é protegido pela rede ao redor, sem agente; o bind LDAP tem o canal cifrado ou contornado até a correção; a remoção de protocolos começa pela auditoria de uso.

## Tarefa 6 — Backup e recuperação (10 pontos)

Entregue: (a) a **arquitetura de backup** resistente a um atacante com privilégio no domínio; (b) a **ordem de recuperação** para o cenário "domínio comprometido e servidores cifrados", começando pela identidade e coerente com a BIA; (c) **dois testes** com critério de aceite.

**Critérios objetivos:** o backup tem identidade fora do domínio, cópias imutáveis e uma cópia isolada ou offline (exigência da seguradora); a retenção considera o tempo até a descoberta — no fato 7, nove dias; a recuperação ocorre em ambiente isolado; a ordem começa por canal fora de banda e contas de emergência, segue pela identidade e respeita o MTD de 8 horas da produção (o MES opera 4 horas sem o ERP); os testes incluem o de isolamento (tentar apagar cópias com credencial do domínio) e o de restauração com tempo medido.

## Tarefa 7 — To-Be, transição e ADR (15 pontos)

Entregue: (a) o **diagrama To-Be**; (b) a **transição** em no máximo quatro iniciativas estruturais em 12 meses, respeitando as janelas de manutenção, com critério de aceite por etapa e o que fica para depois; (c) um **ADR** para a decisão mais importante, com matriz ponderada de pelo menos três alternativas, consequências negativas e riscos residuais com dono.

**Critérios objetivos:** o To-Be é coerente com as Tarefas 2 a 6; a transição tem no máximo quatro iniciativas estruturais e entrega em até cinco meses o que o seguro exige (MFA no acesso remoto e cópia offline ou imutável); mudanças na rede de automação ficam em janelas de manutenção; o ADR segue o modelo do Módulo 2 — Aula 08, com matriz correta, critérios eliminatórios tratados antes da soma, pelo menos uma consequência negativa real e residual com dono conforme a governança.

## Tarefa 8 — Validação e comunicação (10 pontos)

Entregue: (a) para quatro controles críticos do To-Be, o **método de validação** (examinar, entrevistar ou testar), a **evidência** e o **critério de aceite**; (b) uma **medida** de eficácia para o cenário de risco mais crítico, com fórmula, fonte de dados e meta; (c) um **resumo executivo** de no máximo 200 palavras para o conselho, com a recomendação, a ordem das ações e as **decisões pedidas**.

**Critérios objetivos:** controles críticos são validados por teste; a evidência é verificável por terceiros; a medida não é só de implementação; o resumo é compreensível sem jargão, liga as ações a consequências de negócio (produção, seguro, contrato, cooperados) e termina com decisões que o conselho pode tomar.

## Rubrica

| Tarefa | Pontos | Excelente | Adequado | Insuficiente | Resultados de aprendizagem verificados |
|:---|:---|:---|:---|:---|:---|
| 1 | 15 | 15 | 11 | 4 | 1, 2 |
| 2 | 15 | 15 | 11 | 4 | 1, 3, 13 |
| 3 | 15 | 15 | 11 | 4 | 4, 5, 6, 7 |
| 4 | 10 | 10 | 7 | 3 | 8, 9 |
| 5 | 10 | 10 | 7 | 3 | 10 |
| 6 | 10 | 10 | 7 | 3 | 11 |
| 7 | 15 | 15 | 11 | 4 | 12, 13 |
| 8 | 10 | 10 | 7 | 3 | 14, 15 |

**Excelente:** atende a todos os critérios objetivos da tarefa e declara trade-offs. **Adequado:** atende à maioria dos critérios, sem trade-offs ou com uma lacuna menor. **Insuficiente:** atende a menos da metade dos critérios, é genérico ou ignora o cenário; quem atende exatamente à metade fica em *Adequado* se não houver lacuna grave. Quem obtém *Adequado* em todas as tarefas soma 72 pontos e é aprovado, como na rubrica padrão. A [rubrica padrão](rubrics.md) detalha os níveis; para as Tarefas 2 e 7, aplique também o critério *Justificativas* da rubrica padrão.

### Resultados de aprendizagem do Nível 2

| Nº | Ao concluir o Nível 2, o estudante é capaz de… | Onde é trabalhado |
|:---|:---|:---|
| 1 | Projetar zonas, segmentação e microsegmentação proporcionais ao risco | Módulo 5 — Aulas 01, 03 e 07 |
| 2 | Analisar caminhos de ataque north-south e east-west e os controles que os interrompem | Módulo 5 — Aulas 02 e 03; Módulo 4 — Aula 04 |
| 3 | Projetar acesso remoto e de terceiros sem acesso amplo à rede | Módulo 5 — Aula 04; Módulo 7 — Aula 03 |
| 4 | Escolher autenticação e garantia adequadas, inclusive MFA resistente a phishing | Módulo 6 — Aulas 01 e 04 |
| 5 | Decidir a identidade híbrida e conter a propagação de comprometimento entre ambientes | Módulo 6 — Aulas 03 e 05 |
| 6 | Proteger privilégios e identidades de máquina | Módulo 6 — Aulas 06 e 07; Módulo 8 — Aula 03 |
| 7 | Governar o ciclo de vida de identidades, inclusive de terceiros, e a segregação de funções | Módulo 6 — Aula 08 |
| 8 | Aplicar princípios e componentes de Zero Trust a recursos reais | Módulo 7 — Aulas 01 a 04 |
| 9 | Proteger integrações serviço a serviço sem confiança implícita de rede | Módulo 7 — Aula 05; Módulo 8 — Aula 07 |
| 10 | Tratar sistemas legados com decisões explícitas e compensatórios verificáveis | Módulo 8 — Aulas 05 e 06 |
| 11 | Projetar backup e recuperação resistentes a ransomware, começando pela identidade | Módulo 6 — Aula 09; Módulo 8 — Aula 04 |
| 12 | Planejar a evolução em ondas, com As-Is, To-Be e critérios de aceite | Módulo 7 — Aulas 06 e 07; Módulo 8 — Aula 07 |
| 13 | Comparar alternativas com matriz ponderada e registrar decisões | Exercícios de decisão dos Módulos 5 a 8; Módulo 2 — Aula 08 |
| 14 | Definir validação, evidências e medidas | Seções "Como validar" das aulas; Módulo 3 — Aula 08 |
| 15 | Comunicar uma recomendação de infraestrutura ao negócio | Seções "Como apresentar e justificar" das aulas |

## Depois da avaliação

- Confira o [gabarito comentado](answers/level-2-intermediate.md), que traz uma solução de referência — não a única possível.
- Para cada tarefa *Insuficiente*, revise as aulas indicadas na tabela de resultados de aprendizagem e refaça somente aquela parte.
