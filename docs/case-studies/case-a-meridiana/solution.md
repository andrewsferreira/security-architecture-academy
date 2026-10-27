---
title: "Caso A — Solução de referência"
description: Solução de referência do Caso A (Meridiana Distribuidora) — análise do As-Is, riscos de negócio, requisitos, alternativas, arquitetura To-Be, controles, plano de 90 dias a 12 meses, indicadores e riscos residuais.
status: published
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# Caso A — Solução de referência

!!! warning "Faça o caso antes de ler"

    Esta página contém a solução de referência do [Caso A](index.md). Ela é **uma** solução defensável, não a única: propostas diferentes podem ser igualmente boas se estiverem bem justificadas. Use-a para comparar raciocínios, não para conferir respostas literais.

## Análise do As-Is

Revisão com o [Architecture Review Checklist](../../artifacts/architecture-review-checklist.md). Itens selecionados:

| # | Item | Resultado | Evidência ou achado |
|:---|:---|:---|:---|
| A1 | Objetivo, ativos e apetite a risco registrados | Atende parcialmente | Objetivos declarados pela diretoria; apetite a risco implícito ("parada > 24 h é inaceitável") — precisa ser formalizado |
| B3 | Visão física corresponde ao ambiente | Não atende | Não há documentação; o As-Is foi levantado em entrevistas e inspeção |
| C1 | Zonas de confiança definidas | **Não atende** | Rede interna plana; CDs conectados ao mesmo segmento |
| C2 | Fluxos entre fronteiras autenticados | **Não atende** | VPN somente com senha; portal acessa o banco com conta ampla |
| C4 | Interfaces administrativas protegidas | **Não atende** | Administração a partir de qualquer estação, com contas de uso diário |
| D2 | Acesso privilegiado temporário e registrado | **Não atende** | 11 Domain Admins permanentes; fornecedor do ERP com conta compartilhada |
| D3 | Autorização verificada no recurso | Não atende | Portal usa uma única conta de banco com privilégios amplos |
| F1 | Pontos únicos de falha tratados | Não atende | Backup e produção na mesma sala; NAS no domínio |
| F2 | Recuperação compatível com o requisito | **Não atende** | Restauração nunca testada; meta de 24 h não demonstrada |
| G1 | Eventos enviados ao SIEM | **Não atende** | Logs locais por sete dias |
| H3 | Exceções com prazo e dono | Não atende | Servidor sem suporte sem exceção registrada |

### Cinco achados mais graves

| ID | Achado | Por que é grave |
|:---|:---|:---|
| ACH-01 | VPN com senha dá acesso à rede inteira | É o vetor de acesso inicial mais comum em incidentes de ransomware em empresas desse perfil, e a rede plana amplifica o impacto |
| ACH-02 | Contas Domain Admins usadas no dia a dia | Um único phishing bem-sucedido pode entregar o controle do domínio |
| ACH-03 | Backup alcançável a partir do domínio, sem cópia isolada | O atacante pode destruir a capacidade de recuperação antes de criptografar |
| ACH-04 | Ausência de detecção centralizada | A intrusão provavelmente só seria percebida no momento da criptografia |
| ACH-05 | Portal B2B com acesso direto e amplo ao banco do ERP | Um comprometimento do portal expõe e permite alterar dados de todo o ERP |

## Análise de riscos

Escala qualitativa: probabilidade e impacto em Baixa/Média/Alta. Os riscos estão escritos **em linguagem de negócio**.

| ID | Risco de negócio | Achados | Probabilidade | Impacto | Nível |
|:---|:---|:---|:---|:---|:---|
| R1 | Ransomware paralisa os três CDs por mais de 24 horas, com perda de faturamento, multas de entrega e dano à reputação junto a construtoras | ACH-01 a ACH-04 | Alta | Alto | **Crítico** |
| R2 | Não renovação do seguro cibernético, deixando a empresa sem cobertura para incidentes | ACH-01 a ACH-04 | Alta | Alto | **Crítico** |
| R3 | Reprovação na avaliação de fornecedores da construtora, com perda de um cliente estratégico | ACH-01, ACH-02, ACH-04 | Média | Alto | **Alto** |
| R4 | Vazamento ou adulteração de dados de clientes e de preços a partir do portal B2B, com exposição à LGPD e perda de vantagem comercial | ACH-05 | Média | Alto | **Alto** |
| R5 | Comprometimento pelo fornecedor de suporte do ERP, cuja conta compartilhada não identifica quem acessou | ACH-02 | Média | Médio | **Médio** |

## Requisitos de segurança

Extrato da especificação, no formato da [Security Requirements Specification](../../artifacts/security-requirements-specification.md).

**Apetite a risco proposto à diretoria (a confirmar):** nenhuma tolerância a paralisação dos CDs superior a 24 horas; tolerância baixa a exposição de dados de clientes; tolerância moderada a esforço operacional adicional, limitada pela equipe atual mais uma contratação.

| ID | Requisito | Categoria | Origem |
|:---|:---|:---|:---|
| REQ-01 | Todo acesso remoto exige autenticação multifator e é concedido por aplicação, não à rede inteira. | Funcional | R1, R2, R3 |
| REQ-02 | Fornecedores acessam apenas os sistemas contratados, com identidade individual, aprovação prévia, tempo limitado e gravação de sessão. | Funcional | R5 |
| REQ-03 | Contas com privilégios de administração do domínio não são usadas para e-mail nem navegação e só se autenticam a partir de estações administrativas dedicadas. | Restrição | R1 |
| REQ-04 | O número de contas permanentes com privilégio de administração do domínio não excede três, todas com MFA. | Restrição | R1 |
| REQ-05 | A rede interna é dividida em zonas de usuários, aplicações, dados, gestão, centros de distribuição e legados; a comunicação entre zonas é negada por padrão e liberada por fluxo documentado. | Restrição | R1, R4 |
| REQ-06 | O portal B2B acessa dados do ERP somente por uma API de integração autenticada, com permissões limitadas às operações do portal. | Funcional | R4 |
| REQ-07 | Os backups dos sistemas críticos são imutáveis por no mínimo 30 dias e possuem cópia isolada fora do site, inacessível por credenciais do domínio. | Restrição | R1, R2 |
| REQ-08 | A restauração completa dos sistemas que sustentam os CDs é testada a cada trimestre e concluída em até 24 horas. | Qualidade | R1 |
| REQ-09 | Estações e servidores possuem proteção de endpoint com capacidade de detecção e resposta (EDR), com eventos monitorados 24x7. | Funcional | R1, R2, R3 |
| REQ-10 | Eventos de autenticação, de acesso remoto, de administração, de EDR e do Microsoft 365 chegam ao SIEM em até 15 minutos e são retidos por 12 meses. | Qualidade | R1, R3 |
| REQ-11 | O servidor de etiquetas permanece em zona isolada, acessível apenas pelos coletores dos CDs na porta da aplicação, até sua substituição. | Restrição | R1 |
| REQ-12 | Em caso de falha da conexão com um CD, a operação local de expedição continua por pelo menos 8 horas. | Qualidade | R1 |
| REQ-13 | Dados pessoais de contatos de clientes têm retenção definida pela área jurídica e são acessados apenas por perfis autorizados. | Restrição | R4 |
| REQ-14 | Usuários não possuem privilégio de administrador local nas estações por padrão. | Restrição | R1 |

!!! note "Valores dos requisitos"

    Prazos como 15 minutos, 12 meses e 30 dias são propostas do arquiteto, coerentes com o apetite a risco e o orçamento ilustrativos. Em um caso real, devem ser confirmados com o negócio, o jurídico e a seguradora.

## Alternativas e trade-offs

Três decisões estruturais foram analisadas com matriz de decisão. As análises completas estão nos ADRs.

| Decisão | Alternativas | Escolha | ADR |
|:---|:---|:---|:---|
| Acesso remoto | VPN com MFA e postura · acesso por aplicação (ZTNA) · desktop virtual | ZTNA, com MFA na VPN atual como transição | [ADR-001](adr-001-remote-access.md) |
| Segmentação interna | Zonas com firewall interno · microssegmentação por agente · manter rede plana com EDR | Zonas com firewall interno | [ADR-002](adr-002-segmentation.md) |
| Centralização de logs e detecção | SIEM próprio · SIEM com serviço gerenciado de detecção e resposta (MDR) · pilha open source própria | SIEM com MDR | [ADR-003](adr-003-logging.md) |

O fio condutor das três escolhas é a **capacidade da equipe**: com nove pessoas e sem SOC, alternativas que exigem operação intensiva perdem, mesmo quando são tecnicamente superiores.

## Arquitetura To-Be

### Visão conceitual

| Serviço | Objetivo | Requisitos |
|:---|:---|:---|
| Acesso remoto controlado | Acesso por aplicação, com identidade verificada | REQ-01 |
| Acesso de terceiros | Acesso individual, aprovado, temporário e gravado | REQ-02 |
| Administração protegida | Privilégios separados e usados apenas a partir de ambiente dedicado | REQ-03, REQ-04 |
| Zonas de confiança | Contenção de movimentação lateral | REQ-05, REQ-11 |
| Integração controlada | Portal acessa o ERP por interface específica | REQ-06 |
| Recuperação resiliente | Backup que sobrevive a um atacante com privilégios de domínio | REQ-07, REQ-08 |
| Detecção e resposta | Visibilidade e reação 24x7 | REQ-09, REQ-10 |

### Visão lógica

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/case-a-to-be.mmd"
```

<figcaption>Figura 1 — Arquitetura To-Be lógica da Meridiana Distribuidora.</figcaption>
</figure>

### Comparação As-Is × To-Be

| Aspecto | As-Is | To-Be | Nível da lacuna |
|:---|:---|:---|:---|
| Acesso remoto | VPN com senha para a rede inteira | Acesso por aplicação, MFA e postura | Lógica |
| Fornecedores | Conta compartilhada permanente | Acesso individual just-in-time, gravado | Conceitual — nova capacidade |
| Administração | 11 Domain Admins de uso diário | ≤ 3 contas permanentes, estações dedicadas, tiering | Lógica |
| Rede interna | Plana | Seis zonas com política entre zonas | Lógica |
| Portal → ERP | Conexão direta ao banco | API de integração com permissões limitadas | Lógica |
| Backup | NAS no domínio, mesma sala | Imutável + cópia isolada fora do site, restauração testada | Conceitual e física |
| Detecção | Logs locais, 7 dias | SIEM com MDR 24x7, retenção de 12 meses | Conceitual — nova capacidade |
| Legado | Servidor sem suporte na rede plana | Zona isolada, exceção registrada, substituição planejada | Física |

## Controles recomendados

| Camada | Controle | Requisitos | CIS Controls v8.1 | NIST SP 800-53 Rev. 5 |
|:---|:---|:---|:---|:---|
| Identidade | MFA em todo acesso remoto e no Microsoft 365 | REQ-01 | 6 | IA-2 |
| Identidade | Tiering de administração e estações administrativas dedicadas | REQ-03, REQ-04 | 5, 6 | AC-6 |
| Identidade | Acesso privilegiado just-in-time para fornecedores, com gravação | REQ-02 | 6, 15 | AC-17, AU-12 |
| Rede | Zonas com firewall interno e negação por padrão | REQ-05, REQ-11 | 12, 13 | SC-7 |
| Rede | Acesso remoto por aplicação (ZTNA) | REQ-01 | 6, 12 | AC-17 |
| Aplicação | API de integração com permissões mínimas para o portal | REQ-06 | 16 | AC-6 |
| Endpoint | EDR em estações e servidores; remoção do administrador local | REQ-09, REQ-14 | 10, 5 | SI-3, SI-4 |
| Dados | Backup imutável e cópia isolada; testes trimestrais de restauração | REQ-07, REQ-08 | 11 | CP-9, CP-10 |
| Monitoramento | SIEM com MDR; retenção de 12 meses | REQ-10 | 8, 13 | AU-6, SI-4 |
| Legado | Isolamento e exceção formal até a substituição | REQ-11 | 2, 12 | SA-22 |
| Processo | Plano de resposta a incidentes alinhado com o MDR e a seguradora | — | 17 | IR-4 |

## Plano de implementação

O plano prioriza o que reduz o risco crítico mais rápido e o que a seguradora exige, respeitando as janelas de domingo e a capacidade da equipe.

### Primeiros 90 dias — fechar o acesso inicial e proteger a recuperação

| Entrega | Requisitos | Dependência | Observação |
|:---|:---|:---|:---|
| MFA na VPN atual e no Microsoft 365 | REQ-01 (transição) | Licenciamento de identidade | Ganho rápido; não depende da escolha do ZTNA |
| Fornecedor do ERP com identidade individual, MFA e janela aprovada | REQ-02 (transição) | — | Elimina a conta compartilhada |
| Redução de Domain Admins para ≤ 3 e separação de contas administrativas | REQ-03, REQ-04 | Inventário de uso | Uma semana de observação antes de remover |
| Cópia de backup isolada fora do site e primeiro teste de restauração | REQ-07, REQ-08 | Contratação do serviço | Teste em ambiente separado |
| EDR em servidores críticos e contratação do MDR | REQ-09, REQ-10 | Processo de compra | Começa pelos controladores de domínio e pelo ERP |

### Até 6 meses — conter a movimentação lateral e ganhar visibilidade

| Entrega | Requisitos | Observação |
|:---|:---|:---|
| Firewall interno e zonas de gestão, dados e legados | REQ-05, REQ-11 | Migração por zonas, em janelas de domingo, com regras inicialmente em modo de registro |
| EDR em todas as estações; remoção do administrador local | REQ-09, REQ-14 | Exceções pontuais com prazo |
| Todos os logs previstos no SIEM, com casos de uso iniciais do MDR | REQ-10 | Prioridade: autenticação, administração, VPN, EDR |
| Backup imutável na origem | REQ-07 | Substitui o NAS ingressado no domínio |
| **Marco:** avaliação de fornecedores da construtora | — | Evidências a partir dos controles implantados |

### Até 12 meses — consolidar e reduzir exceções

| Entrega | Requisitos | Observação |
|:---|:---|:---|
| ZTNA para todos os usuários remotos; desativação da VPN SSL | REQ-01 | Por grupos de usuários |
| Acesso de fornecedores por broker just-in-time com gravação | REQ-02 | Substitui a solução de transição |
| API de integração do portal com o ERP | REQ-06 | Desenvolvida com o time do portal |
| Zonas de usuários, aplicações e CDs | REQ-05 | Completa a segmentação |
| Substituição do servidor de etiquetas | REQ-11 | Depende da nova versão do fornecedor |
| **Marco:** renovação do seguro (mês 9) e teste de restauração completo dentro de 24 h | REQ-08 | — |

### Orçamento ilustrativo

| Item | Valor estimado no ano 1 (R$) |
|:---|:---|
| EDR para estações e servidores | 160.000 |
| SIEM com serviço gerenciado de detecção e resposta (MDR) | 280.000 |
| MFA, acesso condicional e ZTNA | 140.000 |
| Backup imutável e cópia isolada fora do site | 150.000 |
| Firewall interno em alta disponibilidade | 140.000 |
| Acesso privilegiado de fornecedores | 70.000 |
| Serviços de implantação | 80.000 |
| Contratação de um analista de segurança | 160.000 |
| **Total** | **1.180.000** |

Valores fictícios, apenas para exercitar a priorização dentro do orçamento. Em um caso real, use cotações e separe investimento de custo recorrente.

## Indicadores de sucesso

| Indicador | Meta | Objetivo atendido |
|:---|:---|:---|
| Usuários remotos com MFA | 100% em 90 dias | Seguro, avaliação de fornecedores |
| Contas permanentes com privilégio de domínio | ≤ 3 em 90 dias | Ransomware |
| Restauração completa testada | Dentro de 24 h, a cada trimestre | Ransomware, seguro |
| Ativos críticos com EDR | 100% em 6 meses | Seguro, ransomware |
| Fontes de log previstas no SIEM | 100% em 6 meses | Detecção |
| Fluxos entre zonas documentados e filtrados | 100% em 12 meses | Movimentação lateral |
| Exceções vencidas | Zero | Disciplina de risco |
| Questionário da seguradora atendido | Todos os itens obrigatórios até o mês 9 | Seguro |

## Decisões

- [ADR-001 — Acesso remoto por aplicação, com MFA na VPN como transição](adr-001-remote-access.md)
- [ADR-002 — Segmentação da rede interna em zonas de confiança](adr-002-segmentation.md)
- [ADR-003 — Centralização de logs com SIEM e serviço gerenciado de detecção e resposta](adr-003-logging.md)

## Riscos residuais

| Risco residual | Por que permanece | Dono proposto | Revisão |
|:---|:---|:---|:---|
| Servidor de etiquetas sem suporte até a substituição | Depende do fornecedor | Diretor de Operações | Mensal até a substituição |
| Movimentação lateral dentro de uma mesma zona | A segmentação é por zonas, não por host | Gerente de TI | Avaliar microssegmentação para a zona de dados no ano 2 |
| Dependência do provedor de MDR para detecção | Não há SOC próprio | Gerente de TI | Revisão contratual anual com indicadores de resposta |
| Janela de transição da VPN com MFA (até o ZTNA) | Acesso ainda é à rede, não por aplicação | Gerente de TI | Até a desativação da VPN |
| Ameaça interna com credenciais legítimas | Controles reduzem, mas não eliminam | Diretoria | Anual |

## Resumo executivo

!!! abstract "Para a diretoria da Meridiana — uma página"

    **Situação.** Hoje, a senha de qualquer um dos 150 usuários de acesso remoto abre caminho para toda a rede, inclusive para os backups. Um ataque de ransomware como o que parou um concorrente por onze dias tem alta probabilidade de causar uma parada dos CDs superior a 24 horas — o limite que a diretoria considera inaceitável. Nas condições atuais, a renovação do seguro e a avaliação da construtora também estão em risco.

    **Proposta.** Em 12 meses e dentro do orçamento de R$ 1,2 milhão:

    1. **Fechar a porta de entrada:** MFA em todo acesso remoto em 90 dias e acesso por aplicação em 12 meses.
    2. **Proteger as chaves do reino:** reduzir de 11 para no máximo 3 as contas com controle total da rede.
    3. **Garantir a volta:** backup que o atacante não consegue apagar, com restauração testada dentro de 24 horas.
    4. **Enxergar e reagir:** monitoramento 24x7 por um serviço especializado.
    5. **Conter danos:** dividir a rede para que um incidente em uma área não alcance as demais.

    **Resultado esperado.** Os itens obrigatórios do questionário da seguradora atendidos até o mês 9; evidências para a avaliação da construtora no mês 6; capacidade demonstrada de retomar os CDs em até 24 horas.

    **Decisões necessárias da diretoria.** Aprovar o apetite a risco proposto; nomear os donos dos riscos residuais; autorizar a contratação de um analista de segurança.

## Autoavaliação desta solução pela rubrica

| Critério | Nível | Justificativa |
|:---|:---|:---|
| Segurança | Excelente | Trata acesso inicial, privilégio, movimentação lateral, recuperação e detecção |
| Cobertura de requisitos | Excelente | Requisitos rastreados aos quatro objetivos |
| Justificativas | Excelente | Três ADRs com matrizes e consequências negativas |
| Viabilidade operacional | Adequado | Depende de uma contratação e de um provedor de MDR; o plano de 6 meses é exigente para a equipe |
| Resiliência | Excelente | Backup isolado, imutabilidade e testes trimestrais |
| Custo | Adequado | Orçamento estimado, sem separar investimento e recorrente |
| Documentação | Excelente | Visões, ADRs, riscos residuais e resumo executivo |

A solução de referência não é perfeita: o critério *Viabilidade operacional* está em *Adequado* porque o plano concentra muitas entregas nos primeiros seis meses. Uma alternativa defensável seria adiar a zona de usuários para o ano 2.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
