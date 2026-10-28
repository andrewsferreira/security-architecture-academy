---
title: "Gabarito — Avaliação integradora do Módulo Inicial ao Módulo 2"
description: Solução de referência comentada da avaliação integradora de Fundamentals (Livraria Ipê), com respostas por tarefa, arquitetura-alvo, ADR de exemplo e orientações de correção.
status: published
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
---

# Gabarito — Avaliação integradora do Módulo Inicial ao Módulo 2 { #gabarito-avaliacao-final-de-fundamentals }

!!! warning "Responda primeiro"

    Este é o gabarito da [avaliação integradora do Módulo Inicial ao Módulo 2](../fundamentals-final.md). Faça a avaliação antes de ler. A solução abaixo é **uma** resposta de referência; respostas diferentes podem ser corretas se atenderem aos critérios objetivos.

## Tarefa 1 — Leitura da arquitetura

**Componentes presentes:** clientes; VM da loja (aplicação + banco + backup); provedor de pagamentos; administradores; estações; servidor de arquivos; Wi-Fi de visitantes.

**Componentes ausentes que deveriam aparecer:** DNS do domínio da loja; identidade dos usuários do painel e dos administradores (onde estão as contas?); destino dos logs (não existe); cópia de backup fora da VM (não existe); conexão do escritório com a internet (firewall/roteador); repositório do código, onde a chave de API está.

**Fluxos:**

| Fluxo | Protocolo | Dado |
|:---|:---|:---|
| Clientes → loja | HTTPS 443 | Cadastro, pedidos, dados pessoais |
| Loja → provedor de pagamentos | HTTPS com chave de API | Dados da transação |
| Administradores → VM | RDP 3389 pela internet | Sessão administrativa completa |
| Estações → painel administrativo | HTTPS, só senha | Dados de clientes e pedidos |
| Estações ↔ servidor de arquivos | SMB (provável) | Notas fiscais e contratos |
| Visitantes ↔ estações | Qualquer (rede única) | — |

**Fronteiras de confiança:** internet ↔ VM na nuvem (clientes, administradores e atendimento cruzam); internet ↔ escritório; visitantes ↔ funcionários (não existe fronteira hoje — esse é o problema); organização ↔ provedor de pagamentos; e, dentro da VM, aplicação ↔ banco (também inexistente).

## Tarefa 2 — Riscos (referência)

| # | Ameaça | Vulnerabilidade | Ativo | Impacto | Estimativa |
|:---|:---|:---|:---|:---|:---|
| 1 | Grupo de ransomware ou invasor oportunista | RDP exposto com conta compartilhada | VM inteira: loja, banco e backup | Parada das vendas, vazamento de 120 mil clientes, perda dos backups | **Alta** |
| 2 | Ransomware ou falha de disco | Backup no mesmo disco da VM | Dados de clientes e pedidos | Perda irreversível dos dados; empresa sem como voltar | **Alta** |
| 3 | Atacante que explora falha na aplicação web | Banco na mesma VM exposta à internet | Base de clientes (dados pessoais) | Vazamento, comunicação à ANPD e aos titulares, reputação | **Alta** |
| 4 | Fraudador com senha obtida por phishing | Painel administrativo só com senha | Pedidos e dados de clientes | Fraude em pedidos, exposição de dados | **Média** |
| 5 | Visitante mal-intencionado ou dispositivo infectado | Rede única com Wi-Fi de visitantes | Estações e servidor de arquivos | Movimento lateral, vazamento de contratos e notas | **Média** |

Também aceitáveis: chave de API no código (uso indevido da conta de pagamentos), ausência de logs (incidentes não detectados e não investigáveis). A ordem privilegia o que afeta ao mesmo tempo dados pessoais e continuidade.

## Tarefa 3 — Controles (referência)

| Risco | Preventivo | Detectivo | Corretivo | Princípio | Camada |
|:---|:---|:---|:---|:---|:---|
| 1 | Fechar RDP; acesso por VPN ou bastion com MFA; contas individuais | Alerta de login administrativo e de falhas repetidas | Procedimento de resposta e reconstrução da VM a partir de imagem | *Least privilege*, *defense in depth*, responsabilização | Identidade, rede |
| 2 | Backup diário em outra conta/armazenamento, imutável | Alerta de falha de backup | Restauração testada trimestralmente | *Defense in depth* | Dados, operação |
| 3 | Separar banco em sub-rede privada aceitando só a aplicação; WAF no balanceador | Logs do WAF e do banco | Plano de resposta a vazamento (LGPD) | *Defense in depth*, *fail-safe defaults* | Rede, aplicação |
| 4 | MFA no painel; papéis por função | Alerta de acesso de local incomum | Revogação de sessões | *Least privilege*, *psychological acceptability* (MFA por aplicativo) | Identidade |
| 5 | Zonas separadas: funcionários, servidores, visitantes (só internet) | Logs do firewall do escritório | Isolamento de estação infectada | *Defense in depth*, *fail-safe defaults* | Rede |
| Chave de API | Cofre de segredos; remover do código e rotacionar | Varredura de segredos no repositório | Rotação imediata em caso de exposição | *Open design* (segredo só na chave), *least privilege* | Aplicação |

## Tarefa 4 — Requisitos (referência)

| Objetivo de negócio | Risco | Requisito | Propriedade | Verificação |
|:---|:---|:---|:---|:---|
| Vender continuamente | 2 | A loja tem RTO de 8 h e RPO de 24 h; backups ficam em armazenamento separado e imutável, com restauração testada a cada trimestre. | Disponibilidade | Teste de restauração com tempo medido |
| Proteger clientes (LGPD) | 3 | Dados pessoais de clientes só são acessíveis pela aplicação e por papéis autorizados; o banco não aceita conexões de outra origem. | Confidencialidade | Teste de conexão ao banco a partir de fora da aplicação |
| Evitar fraude em pedidos | 4 | Acesso ao painel administrativo exige MFA e é registrado por usuário individual. | Autenticidade, responsabilização | Tentativa de acesso sem MFA; revisão de logs |
| Saber o que acontece | 1, ausência de logs | Logins administrativos e falhas de autenticação são enviados a um serviço central e geram alerta acima de limiar definido. | Responsabilização, detecção | Simulação de falhas de login |

## Tarefa 5 — Arquitetura-alvo e ADR (referência)

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/as-fund-to-be.mmd"
```

<figcaption>Figura 1 — Arquitetura-alvo de referência da Livraria Ipê: balanceador com WAF como único ponto exposto, aplicação e banco em sub-redes privadas, cofre de segredos, backup imutável em outra conta, administração por bastion com MFA, escritório segmentado e logs centralizados.</figcaption>
</figure>

**ADR-001 — Onde rodar o banco de dados da loja**

- **Contexto:** banco na mesma VM exposta, backup no mesmo disco, equipe de três pessoas, orçamento limitado.
- **Alternativas:** (A) manter na VM e só fechar portas; (B) banco em VM separada em sub-rede privada; (C) banco gerenciado pelo provedor em sub-rede privada.
- **Critérios:** redução de exposição, esforço de operação, backup e restauração, custo.
- **Decisão:** **C — banco gerenciado**, porque transfere ao provedor patch e execução de backup (Módulo 9 — Aula 01 aprofunda a responsabilidade compartilhada) e a equipe é pequena.
- **Consequências negativas:** custo mensal maior que o da VM; menos controle sobre versão e janelas de manutenção; dependência do provedor.
- **Risco residual:** falha na aplicação ainda pode expor dados que ela acessa legitimamente — tratado pelo WAF, testes de segurança da aplicação e privilégio mínimo no usuário do banco.

## Tarefa 6 — Mensagem à diretoria (referência)

> Hoje, uma única senha compartilhada abre a loja virtual, o banco com os dados de 120 mil clientes e o próprio backup. Se alguém a descobrir — e esse tipo de acesso é muito procurado por criminosos —, podemos perder vendas, dados e a cópia de segurança de uma vez. Nas próximas quatro semanas, fechamos esse acesso, criamos contas individuais com verificação em duas etapas e levamos o backup para um local que um invasor não consegue apagar. Em seguida, separamos o banco de dados da parte exposta à internet e a rede de visitantes da rede de trabalho. A centralização de registros vem por último, já usando serviços gerenciados para não exigir novas contratações antes da segunda loja.

## Orientações de correção

- Aceite soluções diferentes que eliminem os mesmos riscos (por exemplo, VPN em vez de bastion; banco em VM separada em vez de gerenciado), desde que justificadas.
- Penalize propostas que exijam equipe ou orçamento incompatíveis com o cenário — a viabilidade é critério explícito.
- Respostas que listam controles sem ligá-los a riscos ficam, no máximo, em *Adequado* na Tarefa 3.
