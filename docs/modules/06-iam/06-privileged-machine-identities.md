---
id: M06-L06
title: "Aula 06 — Contas privilegiadas e identidades de máquina"
public_title: "Módulo 6 — Aula 06 — Contas privilegiadas e identidades de máquina"
description: Como proteger os acessos que mais importam — contas privilegiadas humanas e identidades de máquina — com separação por planos, estações dedicadas, privilégio just-in-time, intermediação de sessões, contas de emergência e credenciais de curta duração para serviços.
domain: iam
tier: professional
status: published
prerequisites: [M06-L03, M06-L05]
objectives:
  - Aplicar os princípios de separação por planos, just-in-time, aprovação e escopo mínimo a papéis privilegiados.
  - Desenhar caminhos de acesso privilegiado com estações dedicadas, PAM e gravação.
  - Inventariar e reduzir o risco de identidades de máquina — contas de serviço, chaves, certificados.
  - Projetar contas de emergência que não se tornem pontos únicos de comprometimento.
minutes: 75
sources: [MS-ENTERPRISE-ACCESS-MODEL, MS-KERBEROASTING-2024, NIST-SP800-63-4, SPIFFE-CONCEPTS, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [MITRE-ATTACK, BOOK-GOOGLE-BSRS]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M06
---

# Aula 06 — Contas privilegiadas e identidades de máquina { #contas-privilegiadas-e-identidades-de-maquina }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 6 · Nível 2</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">75 min · ID técnico: M06-L06</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Quase todo incidente grave passa por uma conta privilegiada ou por uma credencial de máquina esquecida. As primeiras dão controle; as segundas são numerosas, raramente rotacionadas e quase nunca têm MFA. Esta aula trata das duas: como desenhar **caminhos de acesso privilegiado** que resistam a phishing e a roubo de credenciais, e como trazer **identidades de máquina** para o mesmo nível de governança das humanas.

**Pré-requisitos:** [AD, LDAP e Kerberos](03-directories-kerberos.md) e [Identidade híbrida](05-hybrid-identity.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Aplicar os princípios de separação por planos, just-in-time, aprovação e escopo mínimo a papéis privilegiados.
- Desenhar caminhos de acesso privilegiado com estações dedicadas, PAM e gravação.
- Inventariar e reduzir o risco de identidades de máquina — contas de serviço, chaves, certificados.
- Projetar contas de emergência que não se tornem pontos únicos de comprometimento.

## Conceito

### Princípios para papéis privilegiados

O modelo de acesso corporativo da Microsoft propõe princípios de desenho para papéis privilegiados:

| Princípio | Significado |
|:---|:---|
| **Separação de funções entre planos** | Nenhuma conta acumula privilégios em vários planos (controle, gestão, dados) |
| **Ativação just-in-time** | Papéis ativados por tempo limitado, não atribuídos permanentemente |
| **Aprovação** | Papéis de alto impacto exigem aprovação para ativação |
| **Escopo mínimo** | Papéis atribuídos no menor escopo necessário (unidades administrativas, assinaturas, projetos) |
| **Acesso de emergência** | Contas de emergência protegidas por credenciais únicas e chaves físicas |

O mesmo modelo pede que se imponha a **hierarquia entre planos**, impedindo que planos inferiores controlem os superiores por ataque ou por abuso de processos legítimos: uma conta que administra servidores não deve ter direitos sobre o IdP. Estações dedicadas e intermediação de sessões, a seguir, são práticas complementares desta trilha, não descritas nessa página.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m06-l06-planes.mmd"
```

<figcaption>Figura 1 — Planos de controle, gestão e dados; administradores chegam aos planos superiores apenas por estação dedicada e ativação just-in-time.</figcaption>
</figure>

### Caminho de acesso privilegiado

Um caminho de acesso privilegiado protege **cada elo** entre o administrador e o sistema:

1. **Dispositivo** — estação de acesso privilegiado, endurecida, sem e-mail nem navegação geral.
2. **Identidade** — conta administrativa separada da conta de uso diário, com autenticação resistente a phishing (exigida em AAL3 pela SP 800-63B-4).
3. **Elevação** — ativação just-in-time, com aprovação para papéis do plano de controle.
4. **Intermediação** — sessão por PAM ou bastion, sem expor a credencial do sistema-alvo, com gravação (Módulo 5 — Aula 04).
5. **Monitoração** — ativações, uso e alterações enviados ao SIEM.

Um elo fraco anula os demais: MFA forte em uma estação comprometida por malware ainda entrega a sessão ao atacante.

## Fundamentos técnicos

### Identidades de máquina

| Tipo | Exemplos | Problema típico | Direção |
|:---|:---|:---|:---|
| **Contas de serviço** | Contas no AD para serviços Windows, bancos, agendadores | Senhas antigas, privilégios excessivos, SPN exposto | Contas gerenciadas (gMSA/dMSA), privilégio mínimo (Aula 03) |
| **Chaves de API e segredos** | Tokens de integração, senhas de banco em arquivos | Embutidas em código, sem dono, sem rotação | Cofre de segredos; credenciais de curta duração |
| **Chaves de acesso de nuvem** | Chaves de usuários IAM, chaves de contas de serviço | Longa duração, vazam em repositórios | Federação de workload (Aula 07) |
| **Certificados** | TLS de servidores, mTLS entre serviços | Expiração inesperada, chaves sem proteção | Emissão e renovação automatizadas (Módulo 1 — Aula 05) |
| **Identidades de workload** | Pods, funções, jobs | Credenciais estáticas em variáveis | Identidade emitida pela plataforma (SPIFFE, identidades gerenciadas) |

O projeto **SPIFFE** é um exemplo de padrão aberto para identidade de workload: cada workload recebe um identificador (`spiffe://dominio-de-confianca/identificador-do-workload`) e um documento de identidade (SVID) em formato X.509 ou JWT, entregue por uma Workload API que não exige do workload conhecimento prévio da própria identidade — a aplicação não precisa ser implantada com segredos de autenticação. A documentação recomenda X.509-SVID sempre que possível, porque tokens são suscetíveis a repetição (JWT pode ser a única opção quando há um proxy de camada 7 entre os workloads), e aconselha manter em domínios de confiança distintos ambientes com práticas de segurança diferentes, como homologação e produção.

### Ciclo de vida da credencial de máquina

| Etapa | Prática |
|:---|:---|
| **Criação** | Por pedido com dono, finalidade e escopo; nunca manual em produção |
| **Armazenamento** | Cofre de segredos ou identidade gerenciada; nunca em código ou imagem |
| **Uso** | Escopo mínimo; preferir credenciais de curta duração |
| **Rotação** | Automática; frequência proporcional ao risco |
| **Revogação** | Imediata em caso de suspeita; testada |
| **Descomissionamento** | Quando o serviço sai, a credencial sai junto |

### Contas de emergência (*break-glass*)

Contas de emergência existem para quando o IdP, o MFA ou o PIM falham (Módulo 4 — Aula 05). Para não virarem ponto único de comprometimento:

- Poucas (tipicamente duas), sem uso no dia a dia.
- Autenticação forte por chave física, guardada em locais separados, com dupla custódia.
- **Excluídas** das políticas que poderiam bloqueá-las na emergência, mas **incluídas** em alertas: qualquer uso dispara notificação imediata.
- Testadas periodicamente, com troca de credencial após o teste.

## Exemplo empresarial

!!! example "Aurora Pagamentos — o pipeline com chave de administrador"

    Um inventário de identidades de máquina na Aurora encontrou 412 segredos, dos quais 61 em repositórios de código, 18 chaves de acesso de nuvem com mais de dois anos e **uma chave de administrador da conta de produção** usada pelo pipeline de implantação.

    O plano:

    1. Revogar imediatamente a chave do pipeline e substituí-la por **federação de identidade de workload** com escopo por repositório e ramo (Aula 07).
    2. Migrar segredos de repositórios para o cofre, com rotação automática.
    3. Criar política impedindo a emissão de novas chaves de longa duração na nuvem, salvo exceção aprovada.
    4. Varredura de segredos na pipeline para bloquear novos commits com credenciais.

    Em paralelo, os 22 administradores permanentes da nuvem foram reduzidos a 3 contas de emergência e papéis just-in-time.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Administradores | Conta poderosa permanente | Contas separadas por plano, just-in-time, aprovação |
| Estação | A de uso diário | Estação de acesso privilegiado |
| Sessões | Diretas, com credencial conhecida | Intermediadas e gravadas |
| Segredos de máquina | Em código, sem dono | Cofre, curta duração, dono, rotação automática |
| Emergência | Senha em envelope esquecido | Contas testadas, chaves físicas, dupla custódia, alerta de uso |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias para o caminho privilegiado e as identidades de máquina:

| Controle ou padrão | Objetivo | Referência |
|:---|:---|:---|
| Contas privilegiadas | Restringir contas privilegiadas a quem precisa, segundo esquema de papéis, com atribuições monitoradas | SP 800-53: AC-6(5) (Privileged Accounts) e AC-2(7) (Privileged User Accounts) |
| Contas temporárias e de emergência | Desabilitar ou remover automaticamente, após prazo definido, contas criadas para uma situação temporária ou emergência específica (acesso de crise concedido a alguém); as contas *break-glass* permanentes desta aula são exceção documentada, controlada por custódia, alerta e teste | SP 800-53: AC-2(2) (Automated Temporary and Emergency Account Management) |
| MFA resistente a phishing | MFA para contas privilegiadas | SP 800-53: IA-2(1); SP 800-63B-4 (AAL3) |
| Registro e auditoria de sessão | Registrar a execução de funções privilegiadas e auditar o conteúdo de sessões | SP 800-53: AC-6(9) (Log Use of Privileged Functions) e AU-14 (Session Audit) |
| Segredos fora do código | Nenhum autenticador estático sem cifra embutido em aplicações ou armazenamento | SP 800-53: IA-5(7) (No Embedded Unencrypted Static Authenticators) |
| Identidade de serviços e certificados | Autenticar serviços antes da comunicação; certificados emitidos sob política aprovada | SP 800-53: IA-9 (Service Identification and Authentication) e SC-17 (Public Key Infrastructure Certificates) |
| Gestão de contas, inclusive de serviço | Inventário de contas, contas administrativas dedicadas e processos de acesso | CIS v8.1: Controles 5 (Account Management) e 6 (Access Control Management) |

## Aplicabilidade: on-premises, cloud e híbrido

Em on-premises, PAM e tiering administrativo protegem o AD e servidores. Em cloud, a ativação just-in-time de papéis e as identidades gerenciadas eliminam a maioria das chaves estáticas; a política de bloquear chaves de longa duração é um guardrail essencial (Módulos 9 e 10). Em ambientes híbridos, o mesmo administrador costuma ter papéis nos dois lados — e o caminho de acesso privilegiado precisa cobrir ambos.

## Como especificar e implementar

- "Papéis privilegiados são ativados just-in-time; papéis do plano de controle exigem aprovação."
- "Acesso privilegiado parte de estações dedicadas e usa autenticação resistente a phishing."
- "Sessões administrativas em sistemas críticos são intermediadas e gravadas."
- "Identidades de máquina têm dono, finalidade, escopo mínimo e rotação automática; credenciais de longa duração exigem exceção."
- "Contas de emergência são testadas periodicamente e seu uso gera alerta imediato."

## Trade-offs, limitações e antipadrões

- **Trade-off:** just-in-time adiciona atrito à operação; aprovação automática para papéis de baixo impacto e aprovação humana para os de alto impacto equilibram o custo.
- **Antipadrão — PAM como cofre de senhas compartilhadas:** sem intermediação nem gravação, apenas centraliza o risco.
- **Antipadrão — conta de serviço com MFA desabilitado "porque é serviço"** e privilégios de administrador.
- **Limitação:** credenciais de curta duração reduzem a janela, mas não impedem abuso durante a validade; detecção continua necessária.

## Como validar

- Contar contas com privilégio permanente por plano.
- Verificar de quais dispositivos partiram as últimas 100 sessões privilegiadas.
- Varrer repositórios por segredos e comparar com o inventário.
- Testar uma conta de emergência e confirmar o alerta.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhuma conta acumula privilégios em mais de um plano | Relatório de atribuições por plano, sem sobreposição |
| Privilégio permanente limitado às contas de emergência | Relatório do PIM: papéis privilegiados atribuídos de forma permanente |
| Sessões privilegiadas partem de estações dedicadas | Amostra das últimas 100 sessões, todas de dispositivos da lista de estações privilegiadas |
| Nenhum segredo em repositório fora do inventário | Varredura de segredos sem achado não tratado |
| Uso de conta de emergência gera alerta imediato | Registro do último teste periódico com o alerta recebido |

## Como apresentar e justificar

- **Para a diretoria:** "Encontramos uma chave que dava controle total da produção dentro de um pipeline. Substituímos por credenciais que duram minutos e só funcionam para aquele repositório."
- **Para a operação:** "Vocês continuam administrando; só que ativam o papel quando precisam, a partir da estação dedicada."

## Checklist de revisão arquitetural

- [ ] Nenhuma conta acumula privilégios em vários planos.
- [ ] Papéis privilegiados ativados just-in-time, com aprovação nos de alto impacto.
- [ ] Estações de acesso privilegiado em uso.
- [ ] Sessões críticas intermediadas e gravadas.
- [ ] Identidades de máquina inventariadas, com dono e rotação.
- [ ] Contas de emergência testadas, com alerta de uso.

## Questões de compreensão

**1.** Por que separar privilégios por plano?

??? success "Resposta comentada"

    Para que o comprometimento de uma conta de um plano inferior (por exemplo, administração de servidores) não dê controle de um plano superior (o IdP ou o diretório). É a aplicação do princípio de que planos inferiores não devem controlar os superiores.

**2.** Qual a vantagem de identidades de workload emitidas pela plataforma sobre chaves estáticas?

??? success "Resposta comentada"

    Não há segredo de longa duração para vazar, armazenar ou rotacionar: a plataforma atesta o workload e emite credenciais de curta duração. No SPIFFE, por exemplo, o workload obtém seu SVID pela Workload API sem precisar de um segredo prévio.

**3.** Como evitar que contas de emergência se tornem ponto único de comprometimento?

??? success "Resposta comentada"

    Mantendo-as poucas e sem uso diário, com autenticação forte por chave física em dupla custódia, alerta imediato de uso e testes periódicos com troca de credencial.

## Exercício de tomada de decisão

!!! question "Cenário: suporte do fornecedor do ERP na Meridiana"

    O fornecedor do ERP pede uma conta de administrador do domínio "para suporte", alegando que precisa instalar atualizações em vários servidores. As opções são:

    - **A** — conceder a conta de administrador do domínio, com monitoração reforçada;
    - **B** — grupo administrativo local apenas nos servidores do ERP, com acesso do fornecedor por acesso privilegiado intermediado, aprovação just-in-time por janela de manutenção e sessão gravada;
    - **C** — a equipe interna instala as atualizações, com o fornecedor orientando remotamente, sem acesso próprio.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e recomende uma alternativa que atenda à necessidade sem conceder privilégio do plano de controle.

**Objetivos avaliados:** Aplicar os princípios de separação por planos, just-in-time, aprovação e escopo mínimo a papéis privilegiados; desenhar caminhos de acesso privilegiado com estações dedicadas, PAM e gravação.

**Entrega esperada:** Matriz ponderada e a alternativa recomendada com escopo, ativação, intermediação, gravação e validação.

**Critérios de avaliação:**

- A resposta identifica a necessidade real e o plano a que ela pertence (gestão dos servidores do ERP, não o diretório).
- O acesso é nominal, por janela de manutenção, intermediado e gravado.
- A validação prova que a conta não alcança DCs nem altera grupos.

??? success "Resolução de referência"

    | Critério | Peso | A — Administrador do domínio | B — Admin local + acesso intermediado | C — Equipe interna executa |
    |:---|:---|:---|:---|:---|
    | Plano de controle fora do alcance do fornecedor | 3 | 1 | 3 | 3 |
    | Atendimento da necessidade de suporte nas janelas | 2 | 3 | 3 | 1 |
    | Rastreabilidade das ações | 2 | 1 | 3 | 2 |
    | Esforço de implantação e operação | 1 | 3 | 2 | 2 |
    | **Total ponderado** | | **14** | **23** | **17** |

    - **Necessidade real:** instalar atualizações nos servidores do ERP — privilégio do **plano de gestão**, restrito a esses servidores.
    - **Pesos:** manter o plano de controle fora do alcance de terceiros é o objetivo da decisão (peso 3). Atender o suporte e rastrear as ações pesam 2: o ERP precisa ser atualizado, e o que um terceiro faz precisa ser reconstituível. O esforço pesa 1, porque é custo de implantação de uma vez.
    - **Recomendação: B.** Atende à necessidade com privilégio do plano de gestão restrito aos servidores do ERP: conta nominal por técnico, ativação na janela de manutenção, sessão intermediada e gravada e nenhum direito sobre o diretório. A opção C protege o plano de controle, mas transfere à equipe interna um trabalho que ela não domina e atrasa as atualizações.
    - **Validação:** a conta não consegue fazer login em DCs nem alterar grupos; a sessão é revisada por amostragem.
    - **Trade-off aceito e risco residual:** o fornecedor mantém privilégio administrativo nos servidores do ERP durante as janelas; um técnico comprometido pode afetar o ERP e os dados dele, mas não o domínio. O residual é tratado com a revisão das gravações e a cláusula contratual sobre o modelo de acesso, registrados em ADR com a recusa da conta de administrador do domínio.
    - **O que mudaria a decisão:** se o ERP exigir de fato direitos no diretório (por exemplo, extensão de esquema na instalação), a operação vira uma mudança pontual executada pela equipe interna, com o fornecedor orientando (elementos de C), e não uma conta permanente; se a organização não tiver solução de acesso intermediado, a implantação dela entra no plano, e até lá C é a opção.

    **Erros comuns:**

    - Conceder administrador do domínio e compensar com monitoração.
    - Confundir a necessidade do fornecedor (atualizar servidores) com o privilégio pedido (domínio inteiro).
    - Não prever o caso de uma operação que realmente exija direitos no diretório.

## Pontos-chave

- Separe privilégios por plano; planos inferiores não controlam os superiores.
- Proteja cada elo do caminho privilegiado: dispositivo, identidade, elevação, intermediação e monitoração.
- Privilégio just-in-time com aprovação para os papéis de maior impacto.
- Identidades de máquina precisam de dono, cofre, curta duração e rotação automática.
- Contas de emergência existem, são testadas e alertam quando usadas.

## Referências

### Fundamentação principal

- Microsoft. *The enterprise access model*. Microsoft Learn. *(Lido; princípios para papéis privilegiados e hierarquia entre planos reconferidos em 2026-10-29.)*
- D. Weston, V. Sun. *Microsoft's guidance to help mitigate Kerberoasting*. 2024 — contas de serviço gerenciadas. *(Lido.)*
- NIST. *SP 800-63B-4* — AAL3 e autenticação resistente a phishing. *(Lido.)*
- SPIFFE. *SPIFFE Concepts*. <https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/>. *(Lido; reconferido em 2026-10-29.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-2(2), AC-2(7), AC-6(5), AC-6(9), AU-14, IA-2(1), IA-5(7), IA-9 e SC-17, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controles 5 e 6 — gratuito.

### Leitura complementar

- MITRE. *ATT&CK v20* — T1078 Valid Accounts.
- H. Adkins et al. *Building Secure and Reliable Systems* — Cap. 5, *Design for Least Privilege*.

### Aplicação prática

- Faça um inventário rápido de identidades de máquina de um sistema: contas de serviço, chaves de API, chaves de nuvem e certificados. Para cada uma, registre dono, onde está armazenada, idade e próximo passo.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
