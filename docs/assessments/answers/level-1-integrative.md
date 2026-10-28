---
title: "Gabarito — Avaliação integradora do Nível 1"
description: Solução de referência comentada da avaliação integradora do Nível 1 (Rede Jacarandá Farmácias) — contexto e ativos, DFD, threat modeling, risk register, controles e requisitos, matriz de decisão, As-Is e To-Be, ADR, evidências e resumo executivo, com orientações de correção.
status: published
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
---

# Gabarito — Avaliação integradora do Nível 1

!!! warning "Responda primeiro"

    Este é o gabarito da [avaliação integradora do Nível 1](../level-1-integrative.md). Faça a avaliação antes de ler. A solução abaixo é **uma** resposta de referência; respostas diferentes podem ser corretas se atenderem aos critérios objetivos e estiverem justificadas.

## Tarefa 1 — Contexto, partes interessadas e ativos

**Objetivos de negócio:** lançar o envio de receitas em 90 dias; proteger dados que revelam saúde de 600 mil clientes; manter as lojas vendendo (MTD de 4 horas); preservar a relação com o parceiro de entregas.

**Restrições:** nove pessoas em TI, duas em segurança; no máximo três iniciativas estruturais no semestre; preferência por serviços gerenciados; regra sanitária de retenção ainda não confirmada.

**Responsabilidades (exemplo):**

| Decisão | Decide | Executa | Consultado |
|:---|:---|:---|:---|
| Aceite de risco alto com dados de saúde | Diretor de operações (até 60 dias) | Coordenador de segurança registra | Encarregado de dados |
| Validação de receitas | Farmacêutica responsável técnica | Farmacêuticos | Diretora comercial |
| Regra de retenção das receitas | Farmacêutica responsável técnica, com o jurídico | TI configura a retenção | Encarregado de dados |
| Resposta a incidente com dados pessoais | Diretor de operações, em nome do controlador | Coordenador de segurança e TI; a comunicação à ANPD é feita por meio do encarregado (Resolução CD/ANPD nº 15/2024, art. 6º, § 5º) | Jurídico |
| Operação da integração com o parceiro | Gerente de TI | Equipe de integração | Parceiro de entregas |

**Ativos e classificação:**

| Ativo | Classificação | Processo da BIA |
|:---|:---|:---|
| Fotos de receitas | Dado pessoal que pode revelar saúde — tratar como sensível | Validação de receitas |
| Base de fidelidade e histórico de compras | Dado pessoal; o histórico de medicamentos pode revelar saúde | Loja virtual e app |
| Pedidos (nome, endereço, itens) | Dado pessoal | Loja virtual e app |
| Credenciais de farmacêuticos e da integração | Dado de autenticação | Validação; loja virtual |
| ERP e estoque | Dado operacional | Vendas nas lojas |
| Dados de cartão | Não armazenados pela Jacarandá no fluxo online (página hospedada); nas lojas, terminais do adquirente | — |

## Tarefa 2 — DFD e fronteiras (referência)

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/as-n1-dfd.mmd"
```

<figcaption>Figura 1 — DFD de referência do envio e da validação de receitas, já com o desenho proposto: imagens acessadas só por link temporário, farmacêuticos autenticados com MFA e consulta ao histórico restrita ao cliente da receita em validação.</figcaption>
</figure>

**Fronteiras e fluxos que as atravessam:** internet × borda (1, 2, 6, 8 e 12); borda × aplicação (3, 13, 14 e 17); aplicação × dados (4, 5, 11, 15 e 16); organização × parceiro (8); nuvem × datacenter (9). O fluxo 7 fica dentro da zona de aplicação, mas carrega um link que dá acesso a dado sensível — por isso tem validade curta. O fluxo 15 é o caminho do incidente do fato 4: no desenho proposto, o painel só lê o histórico do cliente da receita em validação.

**Problemas do As-Is visíveis no DFD:** o armazenamento de receitas era alcançável sem passar por nenhum processo (link público); a API de pedidos aceitava uma chave única e devolvia o histórico; a sincronização atravessava a fronteira nuvem × datacenter com credencial administrativa do ERP; o painel autenticava só com senha e lia qualquer histórico de compras, sem vínculo com uma receita.

## Tarefa 3 — Threat modeling (referência)

**STRIDE por elemento:**

| ID | Elemento | Cat. | Ameaça | Resposta e decisão |
|:---|:---|:---|:---|:---|
| TM-01 | Armazenamento de receitas | I | Qualquer pessoa com o link lê a receita; links vazam em logs, e-mails e históricos de navegação | Eliminar o acesso público; links temporários emitidos após autorização — mitigar |
| TM-02 | Painel de validação | S | Credencial de farmacêutico obtida por phishing é usada por terceiro | MFA resistente a phishing — mitigar |
| TM-03 | Painel de validação | R | Sem registro de quem abriu qual receita ou histórico, o abuso não é provado nem detectado | Eventos de acesso no SIEM, imutáveis — mitigar |
| TM-04 | Fluxo 8 (parceiro) | I | O parceiro recebe o histórico do cliente, além do necessário para a entrega | Eliminar campos: só nome, endereço e itens liberados — mitigar |
| TM-05 | API de pedidos | S | A chave única permite que qualquer loja, ou quem a obtiver, consulte pedidos de todas | Credencial por loja com escopo — mitigar |
| TM-06 | Sincronização | E | Comprometida, a credencial administrativa dá controle total do banco do ERP | Conta de serviço com privilégio mínimo — mitigar |
| TM-07 | Serviço de receitas | D | Envio em massa de imagens esgota o armazenamento e atrasa a validação | Limites por cliente no gateway — mitigar; residual aceito |
| TM-08 | Fluxo 1 | T | Imagem alterada em trânsito | TLS já presente; hash registrado na gravação — aceitar o residual |

**Abuse case AC-N1-01 — receita falsificada para obter medicamento:**

| Campo | Conteúdo |
|:---|:---|
| Ator malicioso | Cliente fraudador com conta legítima; recursos: editor de imagens e várias contas; objetivo: obter medicamento que exige receita |
| Faixa de privilégio | Usa só a funcionalidade legítima de envio de receitas |
| Interação | Envia a mesma receita adulterada a lojas diferentes, com contas diferentes, até uma validação passar |
| Dano | Dispensação indevida; risco à saúde do cliente; exposição da farmácia a sanções |
| Refutação desejada | Validação conforme o procedimento definido pela farmacêutica responsável; detecção de imagens repetidas entre contas e lojas; limite de envios por CPF |
| Casos de teste | Mesma imagem enviada por duas contas gera alerta; o terceiro envio do mesmo CPF no dia exige revisão adicional |

**Incidente do fato 4 em ATT&CK v20:**

| Passo | Tática | Técnica | Controle |
|:---|:---|:---|:---|
| E-mail falso captura a senha do farmacêutico | Reconnaissance | Phishing for Information (T1598) | Filtragem de e-mail e treinamento direcionado (detectar); MFA resistente a phishing torna a senha insuficiente (prevenir) |
| Login no painel com a senha capturada | Initial Access | Valid Accounts (T1078) | MFA resistente a phishing (prevenir); alerta de login de dispositivo não gerenciado (detectar) |
| Consulta a históricos de clientes | Collection | Data from Information Repositories (T1213) | Alerta de volume e de padrão anômalo de consultas; consulta exige vínculo com receita em validação (prevenir e detectar) |
| Uso da mesma credencial por três semanas, sem detecção | Persistence | Valid Accounts (T1078) | Revisão de sessões e de dispositivos; alerta de acesso fora do turno do farmacêutico (detectar) |

O fato 4 não informa se os dados saíram do painel; se houvesse cópia para fora da organização, a sequência ganharia um passo de Exfiltration. O mesmo método aplicado ao link público das receitas usaria *Data from Cloud Storage* (T1530), da tática Collection.

## Tarefa 4 — Risk register (referência)

Escala qualitativa (baixo, médio, alto, crítico); tolerância do fato 10.

| ID | Cenário | Vulnerabilidades e condições | Prob. | Impacto | Inerente | Tratamento | Residual esperado | Dono | Obrigações |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| RSK-N1-01 | Exposição de receitas por link público | Armazenamento público; links reutilizáveis | Alta — links vazam por canais comuns | Muito alto — dado de saúde exposto | Crítico | Conter em até 24 horas — bloquear o acesso público ou suspender o piloto, preservar e analisar os logs de acesso aos objetos e avaliar com o encarregado e o jurídico se houve incidente com risco ou dano relevante (Resolução CD/ANPD nº 15/2024, arts. 5º e 10); depois, antes do lançamento: armazenamento privado, links temporários, eventos de acesso | Baixo | Farmacêutica responsável técnica | LGPD (lei); fora da tolerância — a exposição pública já existe no piloto e não pode continuar |
| RSK-N1-02 | Abuso de credencial de farmacêutico para consultar históricos | Só senha; sem detecção (três semanas) | Alta — já ocorreu | Alto | Alto | Mitigar: MFA resistente a phishing, alertas de consulta, consulta vinculada à receita | Médio | Diretor de operações | LGPD (lei); prazos da Resolução CD/ANPD nº 15/2024 dependem de detectar e investigar a tempo; o abuso de dois meses atrás precisa ser avaliado como incidente (relevância, comunicação e registro) — a confirmar com o encarregado e o jurídico |
| RSK-N1-03 | Parceiro recebe dados em excesso por chave única | Chave compartilhada; resposta com histórico | Média | Alto | Alto | Mitigar em 30 dias: credencial por loja, minimização da resposta | Baixo | Diretor de operações (tratamento: gerente de TI) | LGPD (lei); contrato com o parceiro (referência voluntária à ISO/IEC 27001) |
| RSK-N1-04 | Vazamento a partir do ambiente de testes com dados reais | Cópia da produção, com histórico de medicamentos; desenvolvedores com acesso administrativo | Média | Alto | Alto | Mitigar em duas etapas: em 30 dias, retirar ou mascarar CPF e histórico de medicamentos da cópia e restringir o acesso a ela; em 90 dias, conta de testes separada com dados sintéticos | Médio em 30 dias; baixo em 90 | Diretor de operações (tratamento: gerente de TI) | LGPD (lei) |
| RSK-N1-05 | Ransomware alcança o ERP e o backup | Backup no domínio; sincronização com credencial administrativa | Média | Muito alto — lojas acima do MTD de 4 h | Crítico | Mitigar em duas etapas: agora, privilégio mínimo da sincronização e cópia diária offline com restauração ensaiada; no próximo semestre, cópia horária imutável fora do domínio | Alto no semestre (fora da tolerância de parada); baixo depois | Diretor de operações; a exceção à tolerância é aprovada pela diretoria, que a definiu | Continuidade (decisão de governança); PCI DSS só se o ambiente do PDV entrar no escopo — confirmar com o assessor |

**Comentários:** RSK-N1-02, RSK-N1-03 e RSK-N1-04 são altos e envolvem dados que podem revelar saúde, portanto não podem ficar aceitos por mais de 60 dias, e só o diretor de operações pode aceitá-los: o RSK-N1-02 é tratado em 60 dias, o RSK-N1-03 em 30 dias e o RSK-N1-04 cai para médio em 30 dias, com a separação completa na Iniciativa 3. O RSK-N1-01 nem pode ser aceito — a governança não tolera exposição pública —, por isso a exposição que já existe no piloto é contida em até 24 horas e a solução estrutural vem antes do lançamento. O RSK-N1-05 fica **fora da tolerância** "parada das lojas acima de 4 horas é inaceitável" durante o semestre, porque a restauração a partir da cópia diária offline não garante 4 horas nem o RPO de 1 hora: com a restrição de três iniciativas, isso só é possível como **exceção formal da diretoria**, que definiu a tolerância, por seis meses e com controles compensatórios (privilégio mínimo da sincronização, cópia diária offline testada, alerta de alteração ou exclusão em massa no NAS).

## Tarefa 5 — Controles e requisitos (referência)

**Baseline:** CIS Controls v8.1 IG1 como piso para a conta de nuvem e o datacenter, com controles adicionais para dados de saúde: cifragem com chave gerenciada pela organização, registro de acesso a receitas e históricos, minimização na API do parceiro. A equipe de dois analistas de segurança não sustentaria a SP 800-53 em todos os sistemas.

| Ajuste | Decisão | Justificativa |
|:---|:---|:---|
| Segurança física e de infraestrutura da nuvem | Herdado do provedor | Relatórios de auditoria do provedor; a configuração da conta continua com a Jacarandá |
| Autenticação de farmacêuticos e administradores | Adicional: MFA resistente a phishing | Incidente do fato 4; RSK-N1-02 |
| Retenção de receitas | Parâmetro a definir | Regra sanitária a confirmar; até lá, nenhuma exclusão automática e acesso restrito |
| Rede sem fio nas lojas | Fora do escopo do envio de receitas | Não participa dos fluxos do DFD |

**Requisitos verificáveis:**

- **SR-N1-01 (TM-01, RSK-N1-01):** "Imagens de receitas só são acessíveis por links emitidos pelo serviço de receitas após autorização, com validade máxima de 5 minutos e vínculo ao usuário que pediu." *Aceite:* link expirado ou usado por outra sessão retorna erro; nenhum objeto do armazenamento responde a acesso anônimo.
- **SR-N1-02 (TM-02, RSK-N1-02):** "O painel de validação exige MFA resistente a phishing para todos os farmacêuticos." *Aceite:* login só com senha ou com fator por SMS é recusado.
- **SR-N1-03 (TM-03, RSK-N1-02 — detecção):** "Consultas a históricos acima de 30 clientes por hora por farmacêutico, ou sem receita em validação, geram alerta tratado em até 4 horas." *Aceite:* simulação de 31 consultas gera alerta e chamado.
- **SR-N1-04 (RSK-N1-05 — recuperação):** "O ERP tem cópia a cada hora fora do domínio, em repositório imutável, com restauração ensaiada a cada semestre dentro do MTD de 4 horas." *Aceite:* relatório do ensaio com tempos medidos e RPO de 1 hora atingido. **Até o próximo semestre**, vale a etapa transitória registrada na exceção: cópia diária offline, com restauração ensaiada e tempo medido.

## Tarefa 6 — Alternativas, As-Is e To-Be (referência)

**Decisão mais importante:** como armazenar e servir as imagens de receitas antes do lançamento.

| Critério | Peso | A — Link público com URL longa | B — Armazenamento privado com links temporários | C — Serviço especializado de terceiros |
|:---|:---|:---|:---|:---|
| Elimina a exposição pública de dados de saúde | 3 | 1 | 3 | 3 |
| Cabe no prazo de 90 dias | 3 | 3 | 3 | 1 |
| Esforço da equipe (3 = menor) | 2 | 3 | 2 | 2 |
| Dependência de terceiros (3 = menor) | 2 | 3 | 3 | 1 |
| Custo (3 = menor) | 1 | 3 | 2 | 1 |
| **Total ponderado** | | **27** | **30** | **19** |

**Pesos:** eliminar a exposição e cumprir o prazo recebem 3 — são as condições do lançamento; esforço e dependência recebem 2; custo recebe 1, porque as diferenças são pequenas diante do risco.

**Critério eliminatório antes da soma:** a governança declarou que nenhum dado de saúde pode ser exposto publicamente. A opção A viola essa tolerância e sai da comparação, mesmo somando 27 — perto de B. A matriz ajuda a comparar B e C; não autoriza uma opção que a governança proibiu.

**Recomendação: B**, com eventos de acesso enviados ao SIEM. **O que mudaria a decisão:** se a regra sanitária exigir um tipo de guarda que o armazenamento próprio não atende, C volta a ser considerada.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/as-n1-to-be.mmd"
```

<figcaption>Figura 2 — Arquitetura-alvo de referência da Rede Jacarandá.</figcaption>
</figure>

**Lacunas e transição (três iniciativas estruturais no semestre):**

| Etapa | Prazo | Entrega | Lacunas fechadas |
|:---|:---|:---|:---|
| Contenção | 24 horas | Acesso público às fotos do piloto bloqueado ou piloto suspenso; logs de acesso preservados e analisados; avaliação de incidente com o encarregado e o jurídico | Exposição atual do RSK-N1-01 |
| Ajustes imediatos (sem iniciativa estrutural) | 30 dias | Credencial por loja e resposta mínima na API do parceiro; conta de serviço com privilégio mínimo na sincronização; cópia diária offline do ERP, testada; CPF e histórico de medicamentos retirados ou mascarados da cópia de testes, com acesso restrito | RSK-N1-03; parte do RSK-N1-04 e do RSK-N1-05 |
| Iniciativa 1 | Antes do lançamento | Receitas em armazenamento privado e cifrado, links temporários, eventos de acesso | RSK-N1-01 |
| Iniciativa 2 | 60 dias | IdP corporativo com MFA resistente a phishing para farmacêuticos e administradores; alertas de consulta | RSK-N1-02 |
| Iniciativa 3 | 90 dias | Conta de testes separada com dados sintéticos; acesso administrativo à produção só por acesso privilegiado | Restante do RSK-N1-04 |
| Próximo semestre | — | Cópia horária imutável do ERP com identidade própria (SR-N1-04); segmentação das lojas | RSK-N1-05 |

## Tarefa 7 — ADR (referência)

**ADR-N1-001 — Armazenamento e acesso às imagens de receitas**

- **Status:** aceito.
- **Contexto:** lançamento em 90 dias; receitas revelam dados de saúde; a governança não tolera exposição pública; equipe pequena.
- **Alternativas:** (A) link público com URL longa; (B) armazenamento privado com links temporários emitidos após autorização; (C) serviço especializado de terceiros.
- **Critérios:** exposição de dados de saúde (eliminatório), prazo, esforço, dependência, custo — matriz da Tarefa 6.
- **Decisão:** B.
- **Consequências positivas:** nenhum acesso anônimo às receitas; todo acesso fica registrado e vinculado a um usuário; base para cumprir prazos de comunicação de incidentes.
- **Consequências negativas:** o serviço de receitas passa a ser dependência crítica da validação (MTD de 24 horas); a equipe precisa operar a emissão de links e a chave de cifragem.
- **Riscos residuais:** farmacêutico autorizado que abusa do acesso — tratado por alertas de consulta (dono: diretor de operações, revisão trimestral); regra de retenção ainda indefinida — sem exclusão automática até a confirmação (dona: farmacêutica responsável técnica, prazo de 30 dias).
- **Cenários tratados:** RSK-N1-01; parcialmente RSK-N1-02.

## Tarefa 8 — Evidências, validação e comunicação (referência)

| Controle crítico | Método | Evidência | Critério de aceite |
|:---|:---|:---|:---|
| Armazenamento sem acesso anônimo | Testar | Tentativa de leitura anônima e com link expirado | Ambas recusadas; evento registrado |
| MFA resistente a phishing no painel | Testar + examinar | Login sem o fator; política exportada do IdP | Login recusado; política sem exceções |
| Alerta de consulta anômala | Testar | Simulação de 31 consultas em uma hora | Alerta e chamado em até 4 horas |
| Restauração do ERP | Testar | Ensaio com tempos medidos | Neste semestre: restauração da cópia diária offline com tempo e perda de dados medidos e comparados ao MTD de 4 horas, como evidência da exceção; depois da cópia imutável: restauração em até 4 horas, com no máximo 1 hora de dados perdidos |

**Medida de eficácia (RSK-N1-02):** porcentagem de alertas de consulta anômala a históricos investigados e encerrados em até 4 horas, por mês. Fórmula: alertas encerrados no prazo ÷ alertas gerados × 100. Fonte: SIEM e sistema de chamados. Meta: 95% a partir do terceiro mês.

**Resumo executivo (referência, cerca de 180 palavras):**

> Hoje mesmo, as fotos de receitas do piloto deixam de ficar públicas, e avaliamos com o jurídico se houve incidente. O envio de receitas pelo app pode ser lançado em 90 dias com segurança, desde que três mudanças venham antes ou junto do lançamento. Primeiro, as fotos das receitas deixam de ficar acessíveis por link público: só o farmacêutico autorizado as vê, e cada acesso fica registrado. Segundo, os farmacêuticos passam a entrar com uma chave física ou equivalente, que um e-mail falso não consegue roubar — o golpe de dois meses atrás não se repetiria. Terceiro, o ambiente de testes deixa de usar dados reais de clientes. Nos próximos 30 dias, o parceiro de entregas passa a receber só o necessário para entregar. A proteção do backup contra ransomware fica para o próximo semestre; até lá, um ataque ainda pode parar as lojas por mais de 4 horas, e mantemos uma cópia diária desconectada. **Decisões pedidas:** aprovar as três iniciativas; aceitar formalmente, por seis meses, a exceção ao limite de parada das lojas; definir com o jurídico a regra de guarda das receitas em 30 dias.

## Orientações de correção

- Aceite outras decisões principais na Tarefa 6 (por exemplo, MFA dos farmacêuticos ou separação de testes), desde que a matriz esteja correta, os pesos justificados e o critério eliminatório da governança tenha sido aplicado.
- A exposição das receitas já existe no piloto (fato 3): propostas que só a resolvem no lançamento, sem contenção imediata, ficam no máximo em *Adequado* nas Tarefas 4 e 6.
- Penalize propostas que ultrapassem três iniciativas estruturais sem justificar o que sai do semestre — a viabilidade é critério explícito.
- Respostas que tratem a ISO/IEC 27001 ou o PCI DSS como lei ficam, no máximo, em *Adequado* na Tarefa 4.
- Na Tarefa 3, aceite outras sequências ATT&CK coerentes com o fato 4, desde que registrem a versão e usem táticas e técnicas existentes nela.
- Prazos legais citados devem corresponder à Resolução CD/ANPD nº 15/2024 (Módulo 3 — Aula 04); afirmações jurídicas além disso precisam ser apresentadas como pontos a confirmar com o jurídico.
