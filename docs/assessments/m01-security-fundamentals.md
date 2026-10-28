---
id: AS-M01
title: "Avaliação do Módulo 1 — Fundamentos de Segurança"
description: Avaliação baseada em competências do Módulo 1 — propriedades de segurança, princípios de design seguro, fronteiras de confiança, criptografia aplicada, PKI e TLS, risco e controles, modelos formais — com duas tarefas de aplicação.
status: published
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
---

# Avaliação do Módulo 1 — Fundamentos de Segurança { #avaliacao-do-modulo-01-fundamentos-de-seguranca }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Avaliação de módulo · Módulo 1</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min · 10 questões + 2 tarefas</span>
</div>

## Instruções

- **Parte 1** — dez questões de múltipla escolha, situacionais. Vale 60 pontos (6 cada).
- **Parte 2** — duas tarefas de aplicação. Vale 40 pontos (20 cada), avaliados pela rubrica do gabarito.
- **Aprovação:** 70 pontos ou mais **e** nenhuma tarefa avaliada como *Insuficiente*.
- Faça sem consultar as aulas. Confira o [gabarito comentado](answers/m01-security-fundamentals.md) somente ao final.

## Parte 1 — Questões situacionais

**1.** Uma API verifica se o usuário está autenticado, mas permite que ele consulte qualquer pedido informando o número na URL. Qual propriedade foi tratada de forma insuficiente?

- (a) Disponibilidade da API diante de um volume excessivo de consultas.
- (b) Autorização por objeto: se aquele usuário pode ver aquele pedido.
- (c) Não repúdio das consultas feitas pelo usuário.
- (d) Integridade dos dados de pedido em trânsito.

**2.** Os administradores de um sistema podem editar livremente o log de aprovações de pagamentos. Que propriedade fica comprometida em primeiro lugar?

- (a) Confidencialidade dos registros de aprovação de pagamentos.
- (b) Disponibilidade do sistema de pagamentos.
- (c) Autenticidade das sessões dos aprovadores.
- (d) Não repúdio e responsabilização das aprovações.

**3.** O serviço de autorização de uma aplicação fica indisponível. A aplicação, "para não parar o negócio", passa a aceitar todas as requisições autenticadas. Qual princípio foi violado?

- (a) *Protective failure* (*fail secure*).
- (b) *Open design*.
- (c) *Psychological acceptability* (aceitação pelos usuários).
- (d) *Economy of mechanism*.

**4.** O mesmo analista cadastra fornecedores e aprova pagamentos a eles. Qual princípio resolve diretamente o risco?

- (a) *Open design*.
- (b) *Defense in depth*.
- (c) *Separation of duties*.
- (d) *Economy of mechanism*.

**5.** Em uma revisão, qual elemento indica **onde** controles precisam ser aplicados com mais rigor?

- (a) A quantidade de servidores envolvidos na solução.
- (b) A linguagem de programação usada pelas equipes.
- (c) O fornecedor do banco de dados escolhido.
- (d) Os pontos em que dados ou comandos cruzam fronteiras de confiança.

**6.** Uma equipe propõe cifrar arquivos de 2 GB enviando-os inteiros ao serviço de chaves para cifragem assimétrica. Qual a melhor orientação?

- (a) Usar apenas hash SHA-256, que é mais rápido que cifrar.
- (b) Cifrar com chave simétrica e proteger essa chave com o serviço de chaves.
- (c) Usar um algoritmo próprio e secreto, que os atacantes não conhecem e não conseguem analisar.
- (d) Dispensar a cifragem de arquivos acima de 1 GB.

**7.** O sistema guarda senhas de usuários com SHA-256, sem sal. Qual a principal fragilidade?

- (a) Senhas iguais geram hashes iguais e tabelas pré-calculadas funcionam.
- (b) O SHA-256 é reversível para quem conhece o algoritmo e dispõe de capacidade computacional.
- (c) O hash ocupa espaço demais no banco de dados.
- (d) Nenhuma: hash é suficiente para guardar senhas.

**8.** Um cliente estabelece TLS com um servidor e o certificado é válido e emitido por uma autoridade confiável, mas o nome no certificado é de outro domínio. O que o cliente deve fazer?

- (a) Aceitar, porque a cadeia leva a uma raiz confiável.
- (b) Aceitar, desde que a conexão esteja cifrada.
- (c) Rejeitar, porque o nome não corresponde ao destino.
- (d) Pedir ao usuário que decida se ignora o aviso.

**9.** Uma vulnerabilidade crítica foi encontrada em um servidor isolado, sem dados sensíveis, sem conectividade com a internet e prestes a ser desligado. Qual afirmação é correta?

- (a) Todo achado crítico é risco crítico e deve ser corrigido antes dos demais.
- (b) O risco depende de ameaça, exposição e impacto, e pode ser baixo aqui.
- (c) Vulnerabilidades em servidores isolados não precisam ser registradas.
- (d) O risco é zero, porque o servidor será desligado em breve.

**10.** Em um sistema de pesquisa, documentos classificados como confidenciais não podem ser lidos por usuários de nível público, e usuários de nível confidencial não podem gravar em documentos públicos. Qual modelo formal descreve essa política?

- (a) Biba.
- (b) Clark-Wilson.
- (c) Brewer-Nash.
- (d) Bell-LaPadula.

## Parte 2 — Tarefas de aplicação

**Tarefa 1 — Requisitos por propriedade (20 pontos).** A diretoria da Lumen Saúde pede que "o novo sistema de agendamento seja seguro". Reescreva o pedido em quatro requisitos, cada um com a propriedade de segurança explícita, o grau esperado e como será verificado.

**Tarefa 2 — Risco e controles (20 pontos).** O portal de fornecedores da Meridiana permite alterar a conta bancária de pagamento com login e senha. Descreva: ameaça, vulnerabilidade, ativo, impacto; proponha um controle preventivo, um detectivo e um corretivo; e diga qual risco residual sobra.

## Depois da avaliação

- Confira o [gabarito comentado](answers/m01-security-fundamentals.md).
- Para ver os mecanismos funcionando, faça o [Laboratório 01](../labs/lab-01-security-mechanisms.md).
