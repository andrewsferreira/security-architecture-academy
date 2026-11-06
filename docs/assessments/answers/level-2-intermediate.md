---
title: "Gabarito — Avaliação intermediária (Níveis 1 e 2)"
description: Solução de referência comentada da avaliação intermediária (Cooperativa Buriti Alimentos) — diagnóstico do As-Is, sequência ATT&CK e risk register, segmentação e acesso remoto, identidade híbrida e privilégios, Zero Trust, legados, backup e recuperação, To-Be, transição, ADR, validação e resumo executivo, com orientações de correção.
status: published
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
---

# Gabarito — Avaliação intermediária (Níveis 1 e 2)

!!! warning "Responda primeiro"

    Este é o gabarito da [avaliação intermediária](../level-2-intermediate.md). Faça a avaliação antes de ler. A solução abaixo é **uma** resposta de referência; respostas diferentes podem ser corretas se atenderem aos critérios objetivos e estiverem justificadas.

## Tarefa 1 — Diagnóstico do As-Is e riscos

**Zonas e fronteiras atuais:**

| Fronteira esperada | Situação no As-Is |
|:---|:---|
| Internet × rede corporativa | VPN com só senha leva à rede inteira — a fronteira existe, mas não restringe nada depois da autenticação |
| Fornecedores × organização | Contas compartilhadas sem dono nem prazo — não há como saber quem usa a conta |
| Usuários × servidores | Rede de escritórios alcança a VLAN de servidores; Wi-Fi com senha compartilhada dá acesso a ela |
| Servidores × plano de controle | Inexistente: controladores de domínio, ERP, etiquetas e backup na mesma VLAN, sem regras entre eles |
| Corporativo × automação | Firewall com regra irrestrita entre o historiador e a VLAN de servidores |
| Produção × backup | Inexistente: o appliance confia no domínio e grava no mesmo datacenter |
| On-premises × nuvem | Administradores globais sincronizados: quem controla o AD controla a nuvem |

**Caminhos a partir da credencial do fato 7:**

- **Historiador:** VPN → rede das unidades → historiador, diretamente (é o acesso "normal" do integrador); ou VPN → VLAN de servidores → regra irrestrita → historiador.
- **Controladores de domínio:** VPN → VLAN de servidores, sem regras → DCs. Com qualquer credencial privilegiada obtida no caminho — por exemplo, em um servidor onde um analista entrou com sua conta de Domain Admins, ou por Kerberoasting das contas de serviço com RC4 que estão em Domain Admins —, o domínio cai.
- **Backup:** com o domínio, o console do appliance (ingressado no domínio) e o NAS no mesmo datacenter ficam ao alcance; a fita semanal está na mesma sala.

**Incidente do fato 7 em ATT&CK v20:**

| Passo | Tática | Técnica | Observado ou hipótese | Controle que interromperia ou detectaria |
|:---|:---|:---|:---|:---|
| Uso da conta compartilhada do integrador | Initial Access | Valid Accounts (T1078) | Observado | Contas nominais com patrocinador e término; MFA (prevenir) |
| Conexão à VPN às 3h, a partir do exterior | Initial Access | External Remote Services (T1133) | Observado | Acesso de terceiros por serviço intermediado, sem VPN de rede, com aprovação por janela (prevenir); alerta de login fora da janela ou do país, escalado 24×7 (detectar) |
| Varredura da rede das unidades por duas horas | Discovery | Network Service Discovery (T1046) | Observado | Segmentação: a sessão do fornecedor não alcança redes, só os sistemas autorizados (prevenir); detecção de varredura com escalonamento por telefone (detectar) |
| Acesso a historiadores ou estações de engenharia com serviços remotos | Lateral Movement | Remote Services (T1021) | **Hipótese** — a investigação foi inconclusiva | Sessões só pelo serviço intermediado, gravadas; registros do historiador centralizados (detectar) |

A versão usada é a v20. A sequência não afirma movimento lateral nem coleta, porque a investigação não os confirmou; o próprio fato de não se saber o que foi acessado é um achado — faltam registros nos sistemas de destino.

**Risk register (escalas e matriz de probabilidade × impacto do modelo [Risk Register](../../artifacts/risk-register.md#escalas); tolerância do fato 9):**

| ID | Cenário | Vulnerabilidades e condições | Prob. | Impacto | Inerente | Tratamento | Residual esperado | Dono | Obrigações e tolerância |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| RSK-MID-01 | Terceiro (ou quem tiver a credencial dele) manipula ou para a automação das unidades | Conta compartilhada; VPN com acesso amplo; regra irrestrita do historiador; alerta lido em nove dias | Alta — já ocorreu acesso indevido | Muito alto — produção | Crítico | Conter em até 7 dias: contas de VPN compartilhadas desativadas; até o acesso intermediado, suporte dos fornecedores só por sessão acompanhada, iniciada por técnico da cooperativa (opção C da Tarefa 2); alertas críticos escalados por telefone; depois, acesso intermediado (Iniciativa 1, entrega para fornecedores em 60 dias) | Baixo | Diretor industrial | Fora da tolerância ("nenhum terceiro com acesso amplo") — não pode ser aceito; contrato com a varejista (plano de resposta testado) |
| RSK-MID-02 | Ransomware a partir de credencial de VPN alcança o domínio e o backup e para as unidades além do MTD de 8 h | VPN sem MFA; Domain Admins no uso diário; contas de serviço em Domain Admins com RC4; backup no domínio; rede plana | Alta | Muito alto — produção, faturamento e pagamentos | Crítico | Mitigar: MFA na VPN, contas administrativas separadas, backup com identidade própria e cópia isolada (Iniciativas 1 a 3); segmentação (Iniciativa 4) | Médio em 5 meses; baixo em 12 | Diretor industrial | Seguro (contrato) exige MFA e cópia offline ou imutável em 5 meses; contrato com a varejista; LGPD se houver dados pessoais afetados; acima da tolerância até o fim da Iniciativa 2 — aceite formal do diretor industrial por até 90 dias, renovável só com nova decisão |
| RSK-MID-03 | Comprometimento da nuvem a partir do AD (e-mail, RH, futuro portal) | Administradores globais sincronizados e administradores do domínio; PTA sem PHS | Média | Alto | Alto | Mitigar em 30 dias: administradores somente em nuvem com chave física; PHS habilitado | Baixo | Diretor financeiro (área administrativa) | LGPD (dados de colaboradores no RH) — lei |
| RSK-MID-04 | Exploração do historiador e do ERP sem suporte a partir da rede plana | Sistemas sem suporte; sem agente no historiador; rede plana | Média | Muito alto (historiador) e alto (ERP) | Alto (historiador e ERP) | Isolar com compensatórios (Tarefa 5); substituir o ERP com o SaaS | Médio | Diretor industrial (historiador); diretora comercial (ERP) | Riscos que podem parar a produção: aceites do diretor industrial por até 90 dias, renovados por nova decisão |
| RSK-MID-05 | Exposição de dados pessoais e bancários de cooperados pelo portal | Proposta de acesso direto ao banco do ERP pela VPN; autorização por objeto ainda não definida; MFA não previsto | Média | Alto | Alto | Evitar a proposta atual; API de integração com operações mínimas, MFA e autorização por objeto antes do lançamento | Baixo | Diretor de relacionamento com cooperados | LGPD (lei); a governança exige MFA para dados de cooperados pela internet |

O NIST CSF 2.0 aparece como referência de adoção voluntária do plano estratégico — útil para organizar o programa, sem natureza de obrigação.

## Tarefa 2 — Segmentação e acesso remoto

**Zonas To-Be e fluxos principais:**

| Zona | Conteúdo | Fluxos permitidos (exemplos) |
|:---|:---|:---|
| Usuários | Estações e Wi-Fi corporativo com 802.1X | Para a zona de aplicações, nas portas das aplicações; nunca direto ao plano de controle por protocolos de administração |
| Convidados | Wi-Fi de visitantes | Só internet |
| Gestão | Acesso privilegiado intermediado, estações dedicadas | Para todas as zonas, nos protocolos de administração, a partir de sessões autorizadas |
| Plano de controle | Controladores de domínio | Autenticação (Kerberos, LDAP sobre TLS) a partir das zonas que precisam; administração só da zona de gestão |
| Aplicações | ERP, API de integração | ERP só a partir da API, dos servidores de aplicação e dos usuários do ERP |
| Legados | Servidor de etiquetas | Só o par que depende do SMBv1 e as impressoras |
| Backup | Appliance e repositório | Backup inicia a cópia; produção não alcança o repositório |
| Intermediária industrial | Réplica dos dados do historiador, servidor de relatórios | Historiador → réplica (sentido único, protocolo do fabricante); corporativo → réplica para relatórios |
| Automação | CLPs, supervisório, historiador | Nenhum fluxo direto com a rede corporativa; suporte só pela zona de gestão |

A regra irrestrita entre o historiador e a VLAN de servidores é substituída pela réplica na zona intermediária — os relatórios leem a réplica. A mudança no firewall da rede de automação entra na janela de manutenção mensal.

**Acesso remoto de colaboradores:** VPN com MFA e regras por perfil (Tarefa 7, ADR); autenticação resistente a phishing para TI e administradores; nenhuma regra de VPN alcança o plano de controle nem a automação.

**Acesso do integrador do SCADA:**

**Critério eliminatório, antes da soma:** a governança não admite terceiro com acesso amplo à rede. A opção A, mesmo com conta nominal e MFA, entrega a rede e é eliminada antes da comparação; o total dela aparece na tabela só para mostrar que, perto dos demais, a soma poderia enganar. A comparação que decide é entre B e C.

| Critério | Peso | A — VPN com conta nominal e MFA | B — Acesso intermediado na zona de gestão | C — Sessão acompanhada, iniciada por técnico da cooperativa |
|:---|:---|:---|:---|:---|
| Alcance limitado aos sistemas autorizados | 3 | 1 | 3 | 3 |
| Rastreabilidade (conta nominal, gravação) | 2 | 2 | 3 | 2 |
| Suporte disponível, inclusive emergências noturnas | 2 | 3 | 3 | 1 |
| Esforço e custo | 1 | 3 | 1 | 2 |
| **Total ponderado** | | **16** | **22** | **17** |

- **Pesos:** limitar o alcance é o objetivo (3); rastrear e manter o suporte pesam 2, porque o incidente ficou sem explicação e as unidades operam à noite; o esforço pesa 1.
- **Recomendação: B.** Conta nominal por técnico, MFA, aprovação do diretor industrial (ou de quem ele delegar) por janela, sessão gravada até o historiador e as estações de engenharia autorizadas. C fica como procedimento de contingência.
- **Trade-off e residual:** o serviço intermediado vira dependência para o suporte de emergência; o técnico autorizado ainda pode errar ou agir mal dentro da sessão — tratado pela gravação e pela revisão por amostragem.

**Wi-Fi corporativo:** 802.1X com certificado de dispositivo para estações gerenciadas; dispositivos pessoais na rede de convidados; a senha compartilhada é extinta.

## Tarefa 3 — Identidade híbrida e privilégios

**Método de autenticação:** habilitar a **sincronização de hash de senha** já, e adotá-la como método principal, desligando os agentes de PTA depois do período de convivência. Justificativa: com o datacenter cifrado (RSK-MID-02), a PTA deixaria e-mail, RH e o portal sem login — inclusive para a equipe de resposta; a documentação da Microsoft recomenda PHS em qualquer cenário, como contingência e para a detecção de credenciais vazadas (Módulo 6 — Aula 05). Residual registrado: hashes passam a residir no provedor em nuvem.

**Contas administrativas por plano:**

| Plano | Contas | Onde são usadas | Ativação |
|:---|:---|:---|:---|
| Nuvem | Dois administradores **somente em nuvem**, com chave física; papéis por PIM | Estações dedicadas | Just-in-time, com aprovação para administrador global |
| Plano de controle (AD) | Contas `adm-ctrl` separadas para as duas pessoas de AD | Só em DCs e nas estações dedicadas | Grupos privilegiados sem membros permanentes, além das contas de emergência |
| Servidores | Contas `adm-srv`, sem direitos sobre o diretório | Pela zona de gestão | Por grupo de servidores |
| Uso diário | Contas comuns, **fora** de Domain Admins | Estações comuns | — |
| Emergência | Duas contas da nuvem e uma do domínio, com chaves físicas em dupla custódia | Só em incidente | Alerta a cada uso; teste semestral |

**Contas de serviço:** inventariar as seis; retirar as quatro de Domain Admins, concedendo só os direitos necessários; migrar para contas gerenciadas (gMSA) onde a aplicação suportar; nas demais, senhas longas e aleatórias, AES e troca da senha depois da mudança; remover SPNs sem uso; alertar para pedidos de tíquete com RC4 ou em volume (Módulo 6 — Aula 03).

**Ciclo de vida de fornecedores:** contas nominais por técnico, criadas pelo patrocinador interno, com data de término igual à do contrato, revisão trimestral pelo patrocinador e desativação automática no término; nenhuma conta compartilhada. As contas só funcionam no serviço intermediado.

**Ordem compatível com duas pessoas:** em 30 dias, PHS, administradores somente em nuvem e contas comuns fora de Domain Admins (mudanças de configuração); na Iniciativa 3, estações dedicadas, PIM, contas de serviço e a camada de servidores.

## Tarefa 4 — Zero Trust no portal, no ERP e no historiador

| Recurso | PDP (motor e administrador de política) | PEP | Fontes de dados |
|:---|:---|:---|:---|
| Portal do cooperado | Acesso condicional do provedor de identidade; regras de autorização da API | Gateway do portal e a própria API, que aplica a autorização por objeto | Diretório de cooperados, método de autenticação, risco da sessão, cadastro de cooperados (vínculo com os dados) |
| ERP | Política da VPN por perfil e papéis do ERP; para administração, a aprovação do acesso privilegiado | Concentrador da VPN e regras da zona de aplicações; serviço intermediado para administração | Grupos do diretório, MFA, aprovações |
| Historiador | Aprovação no serviço de acesso privilegiado | Serviço intermediado e firewall da zona intermediária | Agenda de janelas, cadastro de técnicos, aprovação do diretor industrial |

**Política do portal:**

| Situação | Exigência | Resposta |
|:---|:---|:---|
| Cooperado consulta entregas, análises e pagamentos | MFA (passkey ou aplicativo autenticador) | Permitir só os dados do próprio cooperado |
| Cooperado sem smartphone | Código por SMS como alternativa restrita — a SP 800-63B-4 trata a rede telefônica como autenticador restrito —, aceita pelo dono do risco | Permitir só consulta; alterações exigem atendimento presencial |
| Alteração de dados bancários | *Step-up* e confirmação fora do canal (ligação para o número cadastrado) | Alteração só depois da confirmação, com registro |
| Funcionário do atendimento | SSO corporativo com MFA, dispositivo gerenciado | Consulta só dos cooperados com atendimento aberto, registrada |

**Modo de falha:** se o provedor de identidade cair, o portal **fecha** — o MTD é de 48 horas, e não há como cumprir a governança sem MFA; o atendimento por telefone segue com procedimento de confirmação. Registrar em ADR.

**Integração com o ERP:** rejeitar a consulta ao banco pela VPN. O portal chama uma **API de integração no datacenter** (fachada), que autentica o serviço do portal por mTLS com identidade de workload e expõe três operações de leitura (entregas, análises e pagamentos de um cooperado), validando que o cooperado da sessão é o dono dos dados. A credencial do banco do ERP fica só na API (camada anticorrupção, Módulo 8 — Aula 07). A VPN site a site pode continuar como transporte, mas deixa de ser o mecanismo de confiança.

## Tarefa 5 — Sistemas legados

| Sistema | Decisão | Compensatórios verificáveis | Dono e prazo | Evidência periódica |
|:---|:---|:---|:---|:---|
| ERP (2012 R2) | Verificar se há suporte estendido pago disponível; se não houver, isolar com compensatórios até o SaaS | Zona de aplicações com acesso só pela API, pelos servidores de aplicação e pelos usuários do ERP; administração só pela zona de gestão; EDR e lista de aplicações permitidas; backup testado | Diretora comercial; como pode afetar a produção, aceite do diretor industrial por 90 dias, renovado por nova decisão até o SaaS | Teste trimestral de fluxos e de bloqueio de execução; relatório do EDR |
| Historiador (2008 R2) | Isolar com compensatórios; substituição negociada com o integrador na próxima modernização da unidade | Sem fluxo direto com o corporativo; réplica na zona intermediária; suporte só pelo serviço intermediado; monitoração passiva da rede de automação, com alerta para fluxo novo | Diretor industrial; 90 dias, renovados por nova decisão | Teste de conectividade a partir do corporativo, negado; revisão das sessões gravadas |
| Servidor de etiquetas (SMBv1) | Isolar e substituir o software de impressão em 6 meses | Zona de legados; SMBv1 restrito ao único par que depende dele; sem internet | Diretora comercial; 6 meses | Consulta de registros de SMBv1 mostrando só o par permitido |
| MES (bind LDAP sem TLS) | Corrigir com o fornecedor; até lá, cifrar o canal | Túnel TLS local até os DCs ou IPsec entre o MES e os DCs (Módulo 6 — Aula 03); monitoração de binds inseguros | Diretor industrial; prazo contratual com o fornecedor | Eventos de bind inseguro nos DCs, limitados às exceções |

**Sequência para protocolos:** (1) auditoria de SMBv1 e NTLM por 30 dias, cobrindo um fechamento mensal; (2) SMBv1 desabilitado em tudo, exceto o par do servidor de etiquetas; (3) contas de serviço com AES e sem RC4, com troca de senha; (4) NTLM reduzido em ondas: primeiro as contas administrativas no grupo Protected Users (que não autentica por NTLM; nunca contas de serviço), depois as aplicações corrigidas e, por último, a restrição no domínio a partir dos DCs, com exceções restritas; (5) alertas para tentativas de uso.

## Tarefa 6 — Backup e recuperação

**Arquitetura:**

- Appliance de backup com **contas locais próprias** e chave física, fora do domínio, administrado só pela zona de gestão.
- Repositório **imutável**, com retenção de 30 dias — o fato 7 mostra nove dias até a descoberta, e a margem cobre detecções mais lentas.
- **Cópia isolada** fora do site: armazenamento imutável em nuvem, em conta separada com identidade própria, ou fitas levadas semanalmente a um local externo — a fita deixa a sala de servidores.
- Imagens de referência dos servidores e ambiente de recuperação isolado.

**Ordem de recuperação (domínio comprometido e servidores cifrados):**

1. Canal fora de banda e contas de emergência da nuvem; contenção na nuvem (revogar sessões, suspender a sincronização).
2. **Identidade:** decidir entre limpar e recuperar a floresta (Módulo 6 — Aula 09); recuperar em isolamento um DC por domínio, redefinir contas privilegiadas e a krbtgt.
3. Infraestrutura: DNS, DHCP e o próprio backup.
4. **ERP e integração com o MES** — o MES opera 4 horas sem o ERP, e o MTD da produção é de 8 horas; faturamento (24 horas) logo depois.
5. Portal (48 horas) e pagamento aos cooperados (72 horas).

**Dependência a resolver:** o MES autentica operadores no AD. Para que as unidades continuem produzindo com o domínio fora do ar, cada unidade precisa de um procedimento de contingência com contas locais do MES, sob custódia do supervisor de turno — senão o MTD de 8 horas não é atingível nesse cenário.

**Testes:**

| Teste | Critério de aceite |
|:---|:---|
| Isolamento: tentar apagar ou alterar cópias com credencial de administrador do domínio | Nenhuma cópia apagada ou alterada; tentativa registrada e alertada |
| Restauração do ERP e de um DC em ambiente isolado | ERP disponível em até 4 horas depois da identidade recuperada, com perda de dados dentro do RPO de 4 horas da produção e de 1 hora do faturamento — o que exige backup do banco com logs de transação a cada 15 minutos; tempos registrados. Se o ensaio mostrar que o alvo não é atingível, o resultado volta à BIA e ao diretor industrial, em vez de ficar só no plano |

## Tarefa 7 — To-Be, transição e ADR

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/as-mid-to-be.mmd"
```

<figcaption>Figura 1 — Arquitetura-alvo de referência da Cooperativa Buriti.</figcaption>
</figure>

**Transição (quatro iniciativas estruturais em 12 meses):**

| Etapa | Prazo | Entrega | Critério de aceite | Riscos tratados |
|:---|:---|:---|:---|:---|
| Contenção | 7 dias | Contas de VPN compartilhadas desativadas; suporte de fornecedores por sessão acompanhada, iniciada por técnico da cooperativa; alertas críticos escalados por telefone 24×7 | Nenhum fornecedor com conta de VPN; alerta de teste atendido em 30 minutos | RSK-MID-01 (contenção) |
| Ajustes de 30 dias (sem iniciativa estrutural) | 30 dias | PHS; administradores somente em nuvem; contas comuns fora de Domain Admins; auditoria de SMBv1 e NTLM; fita fora do site | Relatório de papéis sem contas sincronizadas; Domain Admins só com contas de emergência e `adm-ctrl` | RSK-MID-03; parte do RSK-MID-02 |
| Iniciativa 1 — Acesso remoto | 60 dias (fornecedores e MFA na VPN); 5 meses (regras por perfil) | Acesso de fornecedores intermediado e gravado, com contas nominais; MFA em toda conexão de VPN, uma mudança de configuração entregue cedo para deixar margem ao seguro; regras por perfil (ADR-MID-001) | 100% das conexões remotas com MFA; fornecedores só pelo serviço intermediado | RSK-MID-01, RSK-MID-02 |
| Iniciativa 2 — Backup resiliente | 5 meses | Identidade própria, repositório imutável, cópia isolada, testes | Testes de isolamento e de restauração aprovados | RSK-MID-02 |
| Iniciativa 3 — Privilégios | 9 meses | Estações dedicadas, PIM, contas de serviço, camada de servidores, contas de emergência | Nenhum logon de conta do plano de controle fora das estações dedicadas | RSK-MID-02 |
| Iniciativa 4 — Segmentação | 12 meses | Zonas do datacenter; zona intermediária industrial com a réplica do historiador, nas janelas de manutenção; zona de legados | Testes de fluxo por zona; nenhum fluxo direto corporativo × automação | RSK-MID-01, RSK-MID-04 |
| Projeto do portal (orçamento próprio — fato 11) | 6 meses | API de integração, MFA e autorização por objeto | Teste de acesso a dados de outro cooperado negado | RSK-MID-05 |
| Depois dos 12 meses | — | ZTNA para as aplicações web; substituição do historiador; ERP em SaaS | — | — |

As Iniciativas 1 e 2 terminam em cinco meses, antes da renovação do seguro. As mudanças no firewall da automação usam as janelas mensais de domingo.

**ADR-MID-001 — Acesso remoto de colaboradores**

- **Status:** aceito.
- **Contexto:** VPN com só senha e acesso à rede inteira (fato 3); seguro e contrato exigem MFA em todo acesso remoto em cinco meses; ERP com cliente pesado e MES sem suporte a protocolos modernos; equipe de 14 pessoas.
- **Requisitos e riscos:** RSK-MID-02; exigência da seguradora; contrato com a varejista.
- **Alternativas:**

    | Critério | Peso | A — VPN atual com MFA | B — ZTNA por aplicação | C — VPN com MFA e regras por perfil |
    |:---|:---|:---|:---|:---|
    | Redução do alcance de uma credencial roubada | 3 | 1 | 3 | 2 |
    | Entrega em até cinco meses (seguro) | 3 | 3 | 2 | 3 |
    | Compatibilidade com o ERP de cliente pesado e o MES | 2 | 3 | 2 | 3 |
    | Esforço para a equipe | 1 | 3 | 2 | 2 |
    | **Total ponderado** | | **21** | **21** | **23** |

- **Pesos:** o alcance de uma credencial roubada é o risco a reduzir, e o prazo do seguro é uma condição do negócio — peso 3 para ambos; compatibilidade pesa 2; esforço, 1. O prazo entra como critério ponderado, e não como eliminatório, porque as três opções incluem o MFA exigido; o que varia é o risco de não entregá-lo a tempo — e o MFA na VPN é antecipado para 60 dias em qualquer opção.
- **Decisão:** C — vamos exigir MFA em toda conexão de VPN (resistente a phishing para TI e administradores) e limitar cada perfil às aplicações de que precisa.
- **Consequências positivas:** cumpre o seguro e o contrato no prazo; uma credencial roubada deixa de alcançar a rede inteira.
- **Consequências negativas:** a VPN continua dando acesso de rede às aplicações do perfil — ainda há alcance lateral dentro desse conjunto; as regras por perfil precisam de manutenção.
- **Risco residual:** comprometimento de um dispositivo de usuário com sessão ativa alcança as aplicações do perfil. **Dono do risco:** diretor industrial, por envolver a produção; revisão no início do segundo ano, com ZTNA para as aplicações web.
- **Verificação:** tentativa de conexão sem MFA recusada; teste de alcance por perfil.
- **O que mudaria a decisão:** se o fornecedor de ZTNA suportar o cliente do ERP e o prazo do seguro for estendido, B passa a ser preferível.

## Tarefa 8 — Validação e comunicação

| Controle crítico | Método | Evidência | Critério de aceite |
|:---|:---|:---|:---|
| MFA em todo acesso remoto | Testar e examinar | Tentativa de conexão sem MFA; política exportada | Conexão recusada; política sem exceções |
| Acesso de fornecedor intermediado | Testar | Tentativa de alcançar a rede das unidades a partir da sessão do fornecedor; gravação de sessão | Só os sistemas autorizados alcançáveis; sessão gravada |
| Backup isolado | Testar | Teste de isolamento com credencial do domínio | Nenhuma cópia alterada |
| Sem fluxo direto corporativo × automação | Testar | Varredura a partir da VLAN de servidores | Nenhum serviço da automação alcançável |

**Medida de eficácia (RSK-MID-01):** porcentagem de alertas críticos de acesso remoto triados em até 30 minutos, 24×7. Fórmula: alertas críticos triados em até 30 minutos ÷ alertas críticos gerados × 100, por mês. Fonte: plataforma do provedor de segurança e registro de escalonamento. Meta: 95% a partir do segundo mês — o alerta do fato 7 levou nove dias.

**Resumo executivo (referência, cerca de 195 palavras):**

> Há quatro meses, alguém usou a conta compartilhada de um fornecedor para entrar na nossa rede de madrugada, e só soubemos nove dias depois. Hoje, a mesma senha alcançaria as fábricas, as contas de administração e os backups. Um ransomware pararia a produção por dias. Esta semana, desligamos as contas compartilhadas dos fornecedores — o suporte passa a ser feito com um técnico nosso acompanhando — e os alertas graves passam a ser atendidos por telefone a qualquer hora. Em dois meses, todo acesso remoto exige um segundo fator e os fornecedores entram só por um canal gravado, sem acesso à rede. Em cinco meses, antes da renovação do seguro, os backups ficam fora do alcance de quem invadir o domínio. Em doze meses, separamos a rede das fábricas da rede de escritório e protegemos as contas de administração. O portal do cooperado será lançado com segundo fator e sem acesso direto ao ERP. **Decisões pedidas:** aprovar as quatro iniciativas e o orçamento da monitoração 24×7; registrar que o risco de ransomware fica acima do tolerado até os backups ficarem prontos, em cinco meses, aceito pelo diretor industrial em dois períodos de até 90 dias.

## Orientações de correção

- Aceite outras decisões principais na Tarefa 7 (por exemplo, o método de autenticação híbrida ou o backup), desde que a matriz esteja correta, os pesos justificados e os critérios eliminatórios da governança tenham sido aplicados antes da soma.
- Na Tarefa 2, propostas que mantenham VPN de rede para fornecedores — mesmo com MFA — ficam no máximo em *Adequado*: violam a tolerância "nenhum terceiro com acesso amplo à rede".
- Na Tarefa 1, sequências ATT&CK que afirmem movimento lateral, coleta ou exfiltração como fatos ficam no máximo em *Adequado*; aceite-os como hipótese declarada.
- Na Tarefa 6, respostas que não percebam a dependência do MES em relação ao AD ainda podem ser *Adequado*; para *Excelente*, a ordem de recuperação precisa ser compatível com o MTD de 8 horas.
- Propostas com mais de quatro iniciativas estruturais, ou que entreguem MFA e backup isolado depois de cinco meses, ficam no máximo em *Adequado* na Tarefa 7 — prazo e orçamento são critérios explícitos.
- Respostas que tratem a exigência da seguradora ou da varejista como lei, ou o NIST CSF como obrigação, ficam no máximo em *Adequado* na Tarefa 1.
- Na Tarefa 4, SMS como único segundo fator para cooperados sem smartphone pode ser aceito se for tratado como alternativa restrita, com o risco declarado e limites ao que pode ser feito com ele; senha sozinha, sem segundo fator, viola a governança.
