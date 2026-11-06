---
id: M06-L01
title: "Aula 01 — Disciplinas de identidade: IAM, IGA, PAM e PIM"
public_title: "Módulo 6 — Aula 01 — Disciplinas de identidade: IAM, IGA, PAM e PIM"
description: As disciplinas que compõem a segurança de identidades — gerenciamento de identidade e acesso, governança de identidades, gerenciamento de acesso privilegiado e de identidade privilegiada —, o que cada uma resolve, como se integram e por que identidade se tornou o principal plano de controle.
domain: iam
tier: fundamental
status: published
prerequisites: [M01-L01, M01-L02]
objectives:
  - Diferenciar IAM, IGA, PAM e PIM pelo problema que cada disciplina resolve.
  - Explicar por que a identidade é o plano de controle das arquiteturas modernas.
  - Identificar os tipos de identidade — humanas, de máquina, de workload, privilegiadas — e seus riscos.
  - Relacionar as disciplinas a níveis de garantia de autenticação da SP 800-63B-4.
minutes: 60
sources: [NIST-SP800-63-4, MS-ENTERPRISE-ACCESS-MODEL, NIST-SP800-53, CISA-MFA-GUIDANCE-2022, CIS-CONTROLS-V8-1]
further_reading: [NIST-SP800-162]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M06
---

# Aula 01 — Disciplinas de identidade: IAM, IGA, PAM e PIM { #disciplinas-de-identidade-iam-iga-pam-e-pim }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 6 · Nível 2</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min · ID técnico: M06-L01</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Quando usuários, aplicações e dados saem do datacenter, a rede deixa de ser o lugar onde se decide quem acessa o quê — essa decisão passa para a **identidade**. Por isso ataques modernos visam credenciais, tokens e contas privilegiadas, e por isso a arquitetura de identidade se tornou o centro da arquitetura de segurança. Esta aula organiza o domínio em quatro disciplinas complementares e apresenta o vocabulário usado no restante do módulo.

**Pré-requisitos:** [Propriedades de segurança](../01-security-fundamentals/01-security-properties.md) e [Princípios de design seguro](../01-security-fundamentals/02-secure-design-principles.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Diferenciar IAM, IGA, PAM e PIM pelo problema que cada disciplina resolve.
- Explicar por que a identidade é o plano de controle das arquiteturas modernas.
- Identificar os tipos de identidade — humanas, de máquina, de workload, privilegiadas — e seus riscos.
- Relacionar as disciplinas a níveis de garantia de autenticação da SP 800-63B-4.

## Conceito

### Quatro disciplinas

| Disciplina | Problema que resolve | Componentes típicos |
|:---|:---|:---|
| **IAM** — Identity and Access Management | Autenticar e autorizar o uso diário | Diretório, provedor de identidade (IdP), SSO, MFA, acesso condicional |
| **IGA** — Identity Governance and Administration | Garantir que cada identidade tenha os acessos certos ao longo do tempo | Ciclo de vida, solicitações e aprovações, revisões de acesso, segregação de funções |
| **PAM** — Privileged Access Management | Proteger o uso de credenciais e sessões administrativas | Cofre de credenciais, intermediação e gravação de sessões, rotação |
| **PIM** — Privileged Identity Management | Evitar privilégio permanente | Ativação just-in-time, aprovação, tempo limitado, alertas |

As fronteiras entre PAM e PIM variam conforme o fornecedor; o importante é cobrir as duas necessidades: **proteger o uso** de privilégio e **reduzir a existência** de privilégio permanente.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m06-l01-disciplines.mmd"
```

<figcaption>Figura 1 — A fonte autoritativa alimenta a IGA, que provisiona no IAM; PIM ativa papéis privilegiados por tempo limitado; PAM intermedia sessões administrativas; todas geram evidências.</figcaption>
</figure>

### Identidade como plano de controle

O modelo de acesso corporativo da Microsoft descreve três planos — **controle** (sistemas de identidade corporativa que dão controle de acesso consistente a todo o resto), **gestão** (ferramentas que administram workloads e infraestrutura) e **dados/workloads** (onde está o valor de negócio) — e alerta que quem controla os planos superiores tem um caminho atraente para abusar dos inferiores. Comprometer o IdP equivale a comprometer todas as aplicações que confiam nele.

## Fundamentos técnicos

### Tipos de identidade

| Tipo | Exemplos | Risco característico |
|:---|:---|:---|
| **Humana — força de trabalho** | Funcionários, terceiros | Phishing, reutilização de senha, acúmulo de acessos |
| **Humana — clientes (CIAM)** | Pacientes, lojistas | Escala, fraude, privacidade |
| **Privilegiada** | Administradores de domínio, de nuvem, de banco | Impacto máximo se comprometida |
| **De máquina / serviço** | Contas de serviço, chaves de API, certificados | Credenciais estáticas, sem dono, sem MFA |
| **De workload** | Containers, funções, pipelines | Credenciais embutidas em código ou variáveis |

Identidades não humanas costumam ser mais numerosas que as humanas e menos governadas — tema das Aulas 06 e 07 deste módulo e, na formação avançada, do complemento C01.

### Garantia de autenticação

A NIST SP 800-63-4, publicada em julho de 2025, organiza a identidade digital em prova de identidade (63A), autenticação (63B) e federação (63C). A SP 800-63B-4 define três níveis de garantia de autenticação (Sec. 2):

| Nível | Exigência principal |
|:---|:---|
| **AAL1** | Um ou mais fatores; o verificador deveria oferecer opções de MFA e incentivar seu uso (Sec. 2.1) |
| **AAL2** | Dois fatores distintos; o verificador **deve oferecer** ao menos uma opção resistente a phishing (Sec. 2.2.2) |
| **AAL3** | Autenticador criptográfico **resistente a phishing**, com chave privada não exportável (Sec. 2.3.2) |

O documento afirma que senhas, *look-up secrets*, códigos de uso único (OTP) e métodos fora de banda **não são resistentes a phishing** (Sec. 3.1.1 a 3.1.5) — só autenticadores criptográficos que atendem aos requisitos da Sec. 3.2.5 podem ser. Autenticadores sincronizáveis (como passkeys sincronizadas) **não podem ser usados em AAL3**, porque exigem chave exportável (Sec. 2.3.2). A CISA, em orientação de 2022, recomenda que todas as organizações adotem MFA resistente a phishing e usem *number matching* como medida intermediária para MFA por notificação.

Para a arquitetura, isso se traduz em uma regra prática: **contas privilegiadas e acesso remoto exigem autenticação resistente a phishing**; usuários comuns devem ter essa opção e ser migrados progressivamente.

### Onde cada disciplina entra na arquitetura

| Decisão de arquitetura | Disciplina |
|:---|:---|
| Qual IdP é a fonte de autenticação das aplicações? | IAM |
| Como um acesso é concedido, revisado e removido? | IGA |
| Como administradores acessam produção? | PAM e PIM |
| Como um serviço prova quem é a outro serviço? | IAM de workload (Aula 07) |
| Quem pode alterar o próprio IdP? | PIM, plano de controle |

## Exemplo empresarial

!!! example "Lumen Saúde — o mapa das identidades"

    Ao planejar o programa de identidade, a Lumen contou suas identidades: 2.100 funcionários e terceiros, 180 mil pacientes no portal, 46 administradores, **1.340 identidades não humanas** — contas de serviço, chaves de API de integrações, certificados e credenciais de pipeline — e nenhum inventário destas últimas.

    O arquiteto organizou o programa pelas quatro disciplinas: IAM (SSO e MFA para todos os funcionários), PIM (eliminar 31 dos 46 administradores permanentes), PAM (sessões administrativas intermediadas) e IGA (ciclo de vida a partir do RH e revisões trimestrais). As identidades não humanas ganharam um projeto próprio, com inventário e dono para cada uma.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Centro da decisão de acesso | Rede | Identidade, com contexto |
| Autenticação | Senha; MFA opcional | MFA para todos; resistente a phishing para privilegiados e acesso remoto |
| Privilégio | Permanente | Ativado por tempo limitado |
| Acessos | Concedidos e esquecidos | Ciclo de vida e revisões |
| Identidades não humanas | Fora do programa | Inventariadas, com dono e credenciais de curta duração |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias que dão vocabulário comum às quatro disciplinas:

| Controle ou padrão | Disciplina e objetivo | Referência |
|:---|:---|:---|
| Gestão de contas | IGA: criar, modificar, desabilitar e remover contas com base em autorização | SP 800-53: AC-2 (Account Management); CIS v8.1: Controle 5 (Account Management) |
| Gestão de identificadores e autenticadores | IAM: identificador único e autenticadores protegidos durante todo o ciclo | SP 800-53: IA-4 e IA-5 |
| MFA | IAM: MFA para contas privilegiadas e não privilegiadas | SP 800-53: IA-2(1) e IA-2(2); SP 800-63B-4 para os níveis AAL |
| Contas privilegiadas | PAM/PIM: restringir contas privilegiadas a quem precisa | SP 800-53: AC-6(5) (Privileged Accounts) |
| Revisão de privilégios | IGA: revisar periodicamente os privilégios e removê-los quando desnecessários | SP 800-53: AC-6(7) (Review of User Privileges) |
| Gestão do controle de acesso | Processos para conceder, revisar e revogar acessos | CIS v8.1: Controle 6 (Access Control Management) |
| Planos de controle, gestão e dados | Separar e proteger quem administra o IdP | Microsoft, modelo de acesso corporativo |

## Aplicabilidade: on-premises, cloud e híbrido

Em on-premises, o Active Directory costuma ser o plano de controle (Aula 03). Em cloud, o IdP e o IAM do provedor cumprem esse papel — e o IAM de cada nuvem é, na prática, o perímetro da conta (Módulos 9 e 10). Em ambientes híbridos, a identidade é o que conecta os ambientes: a sincronização entre AD e IdP em nuvem torna o comprometimento de um lado um risco para o outro (Aula 05).

## Como especificar e implementar

- "Todas as aplicações autenticam pelo IdP corporativo; exceções têm dono e prazo."
- "Contas privilegiadas e acesso remoto exigem autenticação resistente a phishing."
- "Privilégios administrativos são ativados por tempo limitado, com aprovação para papéis do plano de controle."
- "Toda identidade — humana ou não humana — tem dono, fonte autoritativa e ciclo de vida."

## Trade-offs, limitações e antipadrões

- **Trade-off:** centralizar no IdP simplifica controle e auditoria, mas o torna alvo e ponto único de falha — exigindo resiliência e contas de emergência (Módulo 4 — Aula 05).
- **Antipadrão — MFA por SMS para administradores:** a SP 800-63B-4 classifica PSTN como autenticador restrito.
- **Antipadrão — programa só de humanos:** ignora a maior parte das identidades.
- **Limitação:** a SP 800-63-4 foi escrita para sistemas do governo federal dos EUA; seus níveis são uma referência útil, não obrigação para organizações brasileiras.

## Como validar

- Contar contas privilegiadas permanentes e comparar com a meta.
- Verificar o método de MFA usado por cada administrador.
- Amostrar identidades não humanas e verificar dono e data da última rotação.
- Listar aplicações que não autenticam pelo IdP corporativo.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Contas privilegiadas permanentes dentro da meta | Relatório do PIM comparado à meta definida |
| 100% dos administradores com autenticação resistente a phishing | Relatório de métodos de autenticação do IdP |
| Toda identidade não humana com dono e data de rotação | Amostra do inventário sem item órfão |
| Aplicações fora do IdP com dono e prazo | Lista de exceções revisada |
| Administração do IdP restrita e monitorada | Lista de quem pode alterar o IdP, com alertas para mudanças de configuração |

## Como apresentar e justificar

- **Para a diretoria:** "Hoje, um e-mail de phishing bem feito pode dar a um atacante acesso de administrador. Com MFA resistente a phishing e privilégio temporário, isso deixa de ser suficiente."
- **Para a engenharia:** "Toda identidade tem dono. As 1.340 identidades de máquina também."

## Checklist de revisão arquitetural

- [ ] Há um IdP corporativo como fonte de autenticação.
- [ ] Privilegiados e acesso remoto usam autenticação resistente a phishing.
- [ ] O privilégio permanente foi minimizado.
- [ ] Ciclo de vida e revisões de acesso existem.
- [ ] Identidades não humanas estão inventariadas, com dono.
- [ ] Quem administra o IdP está identificado e protegido.

## Questões de compreensão

**1.** Qual a diferença entre IAM e IGA?

??? success "Resposta comentada"

    IAM autentica e autoriza o uso diário (diretório, IdP, SSO, MFA). IGA governa os acessos ao longo do tempo: concessão, aprovação, revisão, segregação de funções e remoção.

**2.** O que a SP 800-63B-4 exige em AAL3 que não exige em AAL2?

??? success "Resposta comentada"

    Um autenticador resistente a phishing, com chave não exportável. Em AAL2, o verificador deve oferecer ao menos uma opção resistente a phishing, mas ela não é obrigatória para todos os usuários; autenticadores sincronizáveis não são aceitos em AAL3.

**3.** Por que o IdP é considerado parte do plano de controle?

??? success "Resposta comentada"

    Porque controla o acesso a todos os sistemas que confiam nele. Quem compromete o IdP pode emitir acesso a qualquer aplicação federada, o que o coloca no nível mais alto de criticidade.

## Exercício de tomada de decisão

!!! question "Cenário: por onde começar na Meridiana"

    A Meridiana tem orçamento para uma iniciativa de identidade neste ano e uma equipe de três pessoas. O cenário que motivou o programa é o RSK-007: ransomware a partir de credencial roubada na VPN, com escalada por credenciais privilegiadas do domínio (Módulo 4 — Aula 04). As opções são:

    - **A** — IGA completa, com ciclo de vida a partir do RH e revisões de acesso;
    - **B** — MFA resistente a phishing para administradores e VPN, com PIM para os papéis do domínio;
    - **C** — SSO para todas as aplicações.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e recomende uma.

**Objetivos avaliados:** Diferenciar IAM, IGA, PAM e PIM pelo problema que cada disciplina resolve; explicar por que a identidade é o plano de controle das arquiteturas modernas.

**Entrega esperada:** Matriz ponderada e recomendação que liga a disciplina escolhida aos passos do cenário RSK-007.

**Critérios de avaliação:**

- A resposta mostra quais passos do cenário cada opção interrompe, e não só o que cada disciplina faz.
- A recomendação é viável para uma equipe de três pessoas no prazo de um ano.
- O risco residual inclui o que fica sem governança (acessos acumulados, desligados) e como será tratado depois.

??? success "Resolução de referência"

    | Critério | Peso | A — IGA completa | B — MFA resistente a phishing + PIM | C — SSO para todas as aplicações |
    |:---|:---|:---|:---|:---|
    | Interrupção dos passos do cenário RSK-007 | 3 | 1 | 3 | 2 |
    | Tempo até reduzir o risco | 2 | 1 | 3 | 2 |
    | Esforço para uma equipe de três pessoas | 2 | 1 | 2 | 2 |
    | Base para a governança dos anos seguintes | 1 | 3 | 2 | 2 |
    | **Total ponderado** | | **10** | **21** | **16** |

    - **Pesos:** o programa existe por causa do cenário de ransomware (peso 3). Tempo e esforço pesam 2, porque o orçamento é anual e a equipe é pequena. A base para a governança futura pesa 1: importa, mas pode ser construída depois.
    - **Recomendação: B.** MFA resistente a phishing no acesso remoto e para administradores, com eliminação de privilégio permanente, interrompe os passos 1 e 2 do cenário. A opção C traz usabilidade e visibilidade, mas não ataca diretamente o cenário; a A é valiosa, mas lenta para reduzir o risco imediato.
    - **Trade-off aceito e risco residual:** sem IGA, acessos acumulados e contas de desligados continuam dependendo de processos manuais no primeiro ano; o inventário feito na implantação do PIM reduz esse risco e prepara a IGA do ano seguinte.
    - **O que mudaria a decisão:** uma auditoria com achados sobre contas de desligados ou uma exigência de cliente por revisões de acesso documentadas elevaria o peso da governança e anteciparia parte de A; se a VPN fosse substituída por acesso por aplicação ainda neste ano, o SSO de C ganharia peso, por ser pré-requisito dessa migração.

    **Erros comuns:**

    - Começar pela disciplina mais abrangente (IGA) sem relação direta com o risco que motivou o programa.
    - Tratar SSO como controle contra roubo de credencial — ele melhora a experiência, mas não exige fator resistente a phishing por si só.
    - Confundir MFA por push com MFA resistente a phishing.

## Pontos-chave

- IAM autentica e autoriza; IGA governa; PAM protege o uso de privilégio; PIM reduz sua existência.
- A identidade é o plano de controle: comprometer o IdP compromete tudo que confia nele.
- Identidades não humanas são numerosas e frequentemente sem governança.
- A SP 800-63B-4 exige autenticação resistente a phishing em AAL3 e sua oferta em AAL2.
- Privilegiados e acesso remoto são a prioridade para MFA resistente a phishing.

## Referências

### Fundamentação principal

- NIST. *SP 800-63-4 — Digital Identity Guidelines* e *SP 800-63B-4*. 2025. <https://csrc.nist.gov/pubs/sp/800/63/4/final>; <https://pages.nist.gov/800-63-4/sp800-63b.html> — Sec. 2 e 3.1. *(Lido.)*
- Microsoft. *The enterprise access model*. Microsoft Learn. <https://learn.microsoft.com/en-us/training/modules/design-solutions-secure-privileged-access/2-enterprise-access-model>. *(Lido.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-2, AC-6(5), AC-6(7), IA-2(1), IA-2(2), IA-4 e IA-5, conferidos no catálogo OSCAL oficial — gratuito.
- CISA. *Guidance on Phishing-Resistant and Numbers Matching MFA*. 2022 — alerta que resume os fact sheets *(lido)*; fact sheet primário *Implementing Phishing-Resistant MFA*, outubro de 2022, <https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf> *(lido em 2026-11-04)*.
- CIS. *CIS Critical Security Controls v8.1* — Controles 5 e 6 — gratuito.

### Leitura complementar

- NIST. *SP 800-162 — ABAC* ([Aula 02](02-authorization-models.md)).

### Aplicação prática

- Monte o inventário de identidades de um ambiente que você conhece, separando humanas, privilegiadas, de máquina e de workload, e indique o dono de cada categoria.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
