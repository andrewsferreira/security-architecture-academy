---
id: M04-L05
title: "Aula 05 — Pontos únicos de falha e análise de dependências"
public_title: "Módulo 4 — Aula 05 — Pontos únicos de falha e análise de dependências"
description: Como encontrar pontos únicos de falha e dependências ocultas — técnicas, organizacionais e de segurança — e como usar domínios de falha, compartimentalização e controle de raio de impacto para que um único problema não derrube processos críticos nem comprometa o ambiente inteiro.
domain: enterprise-architecture
tier: professional
status: published
prerequisites: [M04-L01, M03-L05]
objectives:
  - Construir um mapa de dependências de um processo crítico e identificar pontos únicos de falha.
  - Reconhecer dependências ocultas de segurança — identidade, chaves, DNS, administração — que anulam redundâncias.
  - Aplicar domínios de falha, compartimentalização e degradação controlada para limitar o raio de impacto.
  - Priorizar a remoção de pontos únicos de falha pelo impacto no MTD e no risco.
minutes: 60
sources: [BOOK-GOOGLE-BSRS, NIST-SP800-34-R1, AWS-DR-WHITEPAPER]
further_reading: [AWS-WA-RELIABILITY, NIST-SP800-160-V1R1]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M04
---

# Aula 05 — Pontos únicos de falha e análise de dependências { #pontos-unicos-de-falha-e-analise-de-dependencias }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 4 · Nível 1</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min · ID técnico: M04-L05</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Muitos incidentes graves não exploram uma vulnerabilidade sofisticada: exploram — ou simplesmente sofrem — uma **dependência que ninguém mapeou**. Um sistema com duas instâncias continua parado se o único servidor de etiquetas cair; um ambiente com backup em outro site continua refém se a chave do backup estiver no domínio comprometido. Esta aula trata da análise de dependências como parte do threat modeling: encontrar pontos únicos de falha, técnicos e de segurança, e limitar o raio de impacto com domínios de falha e compartimentalização.

**Pré-requisitos:** [Data Flow Diagrams e fluxos de confiança](01-data-flow-diagrams.md) e [BIA, RTO e RPO](../03-governance-risk/05-bia-rto-rpo.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Construir um mapa de dependências de um processo crítico e identificar pontos únicos de falha.
- Reconhecer dependências ocultas de segurança — identidade, chaves, DNS, administração — que anulam redundâncias.
- Aplicar domínios de falha, compartimentalização e degradação controlada para limitar o raio de impacto.
- Priorizar a remoção de pontos únicos de falha pelo impacto no MTD e no risco.

## Conceito

### Ponto único de falha

Um **ponto único de falha** (*single point of failure*, SPOF) é um componente — técnico, humano ou organizacional — cuja falha interrompe um processo, sem alternativa. Para a segurança, há um segundo sentido igualmente importante: um **ponto único de comprometimento**, cuja violação dá ao atacante controle sobre muitos sistemas (um domínio administrativo único, uma chave mestra, uma conta de serviço com acesso a tudo).

### Raio de impacto, domínios de falha e compartimentalização

O capítulo 8 de *Building Secure and Reliable Systems* (*Design for Resilience*) oferece o vocabulário:

- **Controlar o raio de impacto** (*blast radius*) é compartimentalizar o impacto de um evento, para que um problema em uma área não se espalhe.
- **Compartimentalização** é estruturar o sistema em unidades isoladas, com acesso limitado de e para cada uma; os limites podem ser por **função** (papel), **localização** ou **tempo**.
- **Domínios de falha** particionam o sistema em cópias equivalentes e independentes; para seus clientes, cada domínio parece um sistema único.

O mesmo capítulo alerta que um domínio de falha pode falhar por completo se **um único componente crítico** falhar, que uma dependência crítica de um backend presente em um só datacenter pode anular um serviço multirregião, e que componentes alternativos **não devem compartilhar domínio de falha** com os componentes que eles substituem.

## Fundamentos técnicos

### Mapear dependências

Partindo de um processo crítico da BIA (Módulo 3 — Aula 05), pergunte para cada componente: **de que ele precisa para funcionar e para ser recuperado?** Continue até chegar a infraestrutura comum. As categorias que mais escondem SPOFs:

| Categoria | Exemplos de dependência oculta |
|:---|:---|
| **Identidade** | Diretório, IdP, sincronização, contas de serviço |
| **Nomes e rede** | DNS interno, NTP, link de internet, roteamento entre sites |
| **Chaves e segredos** | KMS, HSM, cofre de segredos, certificados com mesma CA ou mesma data de expiração |
| **Administração** | Estação de administração única, bastion único, uma pessoa que sabe o procedimento |
| **Fornecedores** | Provedor de SaaS, provedor de pagamentos, operadora |
| **Plataforma** | Plano de controle do provedor de cloud, pipeline de deploy, repositório de artefatos |

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m04-l05-dependencies.mmd"
```

<figcaption>Figura 1 — Mapa de dependências da expedição da Meridiana; contornos tracejados indicam pontos únicos de falha.</figcaption>
</figure>

Na Figura 1, o WMS tem duas instâncias, mas a expedição continua dependente de um **servidor de etiquetas único**, de controladores de domínio **no mesmo datacenter** (que também servem o DNS) e de um **link de internet único**. A redundância do WMS é real, mas não protege o processo.

### Dependências que anulam a segurança

Algumas dependências não derrubam o serviço, mas **anulam controles**:

- **Backup administrado com credenciais do domínio** — um atacante com privilégio no domínio apaga as cópias (o passo T1490 da Aula 04).
- **Monitoração que depende do próprio ambiente monitorado** — os logs somem junto com o servidor.
- **Recuperação que depende do sistema comprometido** — o procedimento de restauração precisa do AD que está cifrado.
- **Controles de acesso que dependem de um único IdP** — sem um caminho de emergência (*break-glass*) seguro e testado, a indisponibilidade do IdP bloqueia até a resposta ao incidente.

### Técnicas para reduzir o raio de impacto

| Técnica | O que faz | Exemplo |
|:---|:---|:---|
| **Redundância em domínio de falha diferente** | Evita que a mesma causa derrube original e cópia | Controlador de domínio em outro site, com energia e rede independentes |
| **Compartimentalização por função** | Limita o que cada identidade alcança | Tiering administrativo; contas separadas por ambiente |
| **Compartimentalização por localização** | Limita o alcance geográfico ou lógico | Segmentos por centro de distribuição |
| **Compartimentalização por tempo** | Limita a validade do acesso | Credenciais e privilégios temporários |
| **Degradação controlada** | Mantém o essencial funcionando | Expedição com etiquetas pré-impressas por algumas horas |
| **Isolamento da recuperação** | Garante que a recuperação não dependa do ambiente comprometido | Cofre de backup com identidade e rede próprias |

O capítulo também destaca a **validação contínua**: observar o sistema em circunstâncias realistas, porém controladas, para confirmar que os mecanismos de resiliência continuam funcionando.

### Priorizar

Nem todo SPOF precisa ser eliminado. Priorize pelo efeito no **MTD** dos processos críticos e no **risco** do register:

1. SPOFs que fazem o RTO real ultrapassar o MTD.
2. Pontos únicos de comprometimento que permitem a um atacante alcançar vários processos críticos.
3. Dependências que anulam a recuperação.
4. Os demais, tratados com degradação controlada ou aceitos com dono.

## Exemplo empresarial

!!! example "Meridiana — três SPOFs e uma decisão"

    O mapa de dependências da expedição encontrou três SPOFs e uma dependência que anulava a recuperação (backup no domínio). A equipe priorizou:

    | Item | Efeito | Tratamento | Custo |
    |:---|:---|:---|:---|
    | Backup administrado pelo domínio | Anula a recuperação no cenário de ransomware | Cofre isolado, identidade própria | Médio |
    | DCs no mesmo datacenter | Falha do site derruba identidade e DNS | Terceiro DC em nuvem, em domínio de falha diferente | Médio |
    | Servidor de etiquetas único | Expedição parada mesmo com WMS ativo | Segunda instância + etiquetas pré-impressas para 4 horas | Baixo |
    | Link de internet único dos CDs | CDs isolados do WMS | **Aceito** por 12 meses, com operação offline limitada; dono: diretor de operações | — |

    A degradação controlada (etiquetas pré-impressas) foi a medida mais barata e a que mais protegeu o MTD no curto prazo.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Redundância | Duplicar servidores da aplicação | Redundância em domínios de falha independentes, incluindo dependências |
| Identidade e chaves | Infraestrutura "sempre disponível" | Mapeadas como dependências críticas, com caminho de emergência |
| Recuperação | Depende do ambiente de produção | Isolada do ambiente que pode estar comprometido |
| Falha parcial | Tudo ou nada | Degradação controlada definida com o negócio |
| Validação | Teste no comissionamento | Validação contínua e exercícios |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, zonas e regiões oferecem domínios de falha prontos, mas dependências globais — **identidade, DNS, plano de controle, faturamento da conta** — podem ser comuns a todos eles. O whitepaper de recuperação de desastres da AWS lembra que estratégias de replicação precisam de cópias pontuais para resistir a corrupção de dados; o mesmo vale para a configuração da conta. Em ambientes híbridos, o **link entre ambientes** e a **sincronização de identidade** são candidatos frequentes a SPOF — e a ponto único de comprometimento.

## Como especificar e implementar

- "Processos críticos têm mapa de dependências até identidade, DNS, chaves, administração, fornecedores e plataforma."
- "Componentes redundantes ficam em domínios de falha independentes, inclusive de energia, rede e identidade."
- "A recuperação de sistemas críticos não depende de identidades ou redes do ambiente de produção."
- "Cada processo crítico tem um modo de degradação controlada acordado com o dono."
- "Há procedimento de acesso de emergência, protegido e testado, para indisponibilidade do IdP."

## Trade-offs, limitações e antipadrões

- **Trade-off:** independência custa — sites, identidades e redes separadas aumentam custo e complexidade operacional.
- **Antipadrão — redundância ilusória:** duas instâncias atrás do mesmo balanceador, no mesmo rack, com o mesmo DNS.
- **Antipadrão — conta de emergência esquecida:** existe, mas a senha expirou ou ninguém sabe onde está.
- **Limitação:** mapas de dependência envelhecem rápido; sem validação contínua, voltam a esconder SPOFs.

## Como validar

- Exercícios de falha controlada: desligar uma dependência em janela planejada e medir o efeito.
- Restaurar um sistema crítico supondo o domínio comprometido.
- Testar o acesso de emergência ao menos duas vezes por ano.
- Comparar o mapa com dados de observabilidade (chamadas reais entre serviços).

## Como apresentar e justificar

- **Para a diretoria:** "Investimos em duplicar o WMS, mas a expedição ainda para se um servidor de etiquetas cair. Com R$ X e etiquetas pré-impressas, resolvemos o que mais ameaça o limite de 24 horas."
- **Para engenharia:** "Redundância só conta se a cópia não depender do mesmo DNS, da mesma identidade e da mesma energia."

## Checklist de revisão arquitetural

- [ ] O processo crítico tem mapa de dependências completo.
- [ ] Redundâncias estão em domínios de falha independentes.
- [ ] Pontos únicos de comprometimento estão identificados.
- [ ] A recuperação é independente do ambiente comprometido.
- [ ] Há degradação controlada acordada com o negócio.
- [ ] O acesso de emergência está protegido e testado.

## Questões de compreensão

**1.** Qual a diferença entre ponto único de falha e ponto único de comprometimento?

??? success "Resposta comentada"

    O ponto único de falha interrompe um processo quando falha. O ponto único de comprometimento, quando violado, dá ao atacante controle sobre muitos sistemas — por exemplo, um domínio administrativo único ou uma chave mestra. Os dois precisam ser mapeados.

**2.** Por que componentes alternativos não devem compartilhar domínio de falha com os originais?

??? success "Resposta comentada"

    Porque a mesma causa raiz — queda de energia, falha de DNS, comprometimento da identidade — derrubaria original e alternativa ao mesmo tempo, anulando a redundância.

**3.** O que é degradação controlada e por que é útil?

??? success "Resposta comentada"

    É manter funcionando o essencial do processo, de forma reduzida, quando parte dos componentes falha — por exemplo, etiquetas pré-impressas ou leitura sem escrita. Protege o MTD a custo baixo enquanto a recuperação completa acontece.

## Exercício de tomada de decisão

!!! question "Cenário: dependência de IdP único na Aurora"

    Todas as aplicações da Aurora Pagamentos, inclusive o console do SIEM e o acesso privilegiado, autenticam pelo mesmo IdP em SaaS. Em uma indisponibilidade de 3 horas do IdP, ninguém conseguiu acessar o SIEM durante um alerta. A equipe considera três opções: (A) contas de emergência locais, fora do IdP, com chave física guardada sob dupla custódia; (B) um segundo IdP, de outro provedor, sincronizado e ativo em paralelo; (C) aceitar o risco e depender do SLA do provedor. Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho), proponha a arquitetura de acesso de emergência e explique como ela evita criar um novo ponto único de comprometimento.

??? success "Resolução de referência"

    | Critério | Peso | A — Contas de emergência locais | B — Segundo IdP ativo | C — Aceitar e depender do SLA |
    |:---|:---|:---|:---|:---|
    | Restabelece o acesso ao SIEM e ao acesso privilegiado durante a falha | 3 | 3 | 3 | 1 |
    | Não cria novo ponto único de comprometimento | 3 | 2 | 1 | 3 |
    | Custo e complexidade (3 = menor) | 2 | 3 | 1 | 3 |
    | Facilidade de testar periodicamente | 1 | 3 | 2 | 1 |
    | **Total ponderado** | | **24** | **16** | **19** |

    **Pesos:** restabelecer o acesso e não criar um novo ponto de comprometimento recebem 3 — são os dois lados do problema; custo e complexidade recebem 2; testabilidade recebe 1. **Recomendação: A.** C soma mais que B porque B duplica a superfície de identidade privilegiada e o custo; ainda assim, C deixa a resposta a incidentes cega durante a falha — e por isso é descartada como estado final.

    - **Contas de emergência** em número mínimo (por exemplo, duas), locais aos sistemas críticos (SIEM, acesso privilegiado, console de cloud), **fora** do IdP, com autenticação forte por chave física guardada em cofre com dupla custódia.
    - **Não criar novo ponto de comprometimento:** as contas não são usadas no dia a dia; qualquer uso gera alerta imediato ao SOC e à diretoria; as credenciais ficam em locais separados; o uso exige duas pessoas.
    - **Validação:** teste semestral registrado, com troca das credenciais após o teste.
    - **Residual aceito:** comprometimento simultâneo das chaves físicas e da custódia — improvável e detectável pelo alerta de uso.
    - **O que mudaria a decisão:** se os sistemas críticos não aceitassem contas locais (por exemplo, um SIEM em SaaS que só autentica pelo IdP), a opção B, restrita às contas de emergência, passaria a ser a alternativa; uma exigência regulatória de disponibilidade contínua do acesso privilegiado também favoreceria B.

## Pontos-chave

- SPOFs se escondem em identidade, DNS, chaves, administração, fornecedores e plataforma.
- Redundância só vale em domínios de falha independentes.
- Pontos únicos de comprometimento são tão importantes quanto pontos únicos de falha.
- Compartimentalização por função, localização e tempo limita o raio de impacto.
- A recuperação precisa ser independente do ambiente que pode estar comprometido.

## Referências

### Fundamentação principal

- H. Adkins et al. *Building Secure and Reliable Systems*. O'Reilly, 2020 — Cap. 8, *Design for Resilience*. <https://google.github.io/building-secure-and-reliable-systems/raw/toc.html>. *(Lido.)*
- NIST. *SP 800-34 Rev. 1* — Sec. 3.2.2, requisitos de recursos na BIA.
- AWS. *Disaster Recovery of Workloads on AWS: Recovery in the Cloud* — replicação versus cópias pontuais.

### Leitura complementar

- AWS. *Well-Architected Framework — Reliability Pillar*, princípios de design.
- NIST. *SP 800-160 Vol. 1 Rev. 1* — princípios de engenharia de sistemas confiáveis.

### Aplicação prática

- Mapeie as dependências de um processo crítico até identidade, DNS e chaves. Marque os SPOFs e os pontos únicos de comprometimento e proponha um modo de degradação controlada.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
