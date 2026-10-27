---
id: M00-L07
title: "Lendo diagramas arquiteturais: componentes, fluxos e fronteiras"
description: Como ler e questionar um diagrama de arquitetura — componentes, fluxos rotulados, dados, zonas e fronteiras de confiança — e como identificar o que um diagrama omite.
domain: infrastructure-foundations
tier: fundamental
status: published
prerequisites: [M00-L03, M00-L06]
objectives:
  - Identificar componentes, fluxos, armazenamentos, atores e fronteiras de confiança em um diagrama.
  - Avaliar se um fluxo está suficientemente descrito (protocolo, autenticação, dados e sentido).
  - Encontrar os pontos em que fluxos atravessam fronteiras de confiança.
  - Listar as perguntas que um diagrama incompleto deixa sem resposta.
minutes: 60
sources: [ISO-42010-2022, NIST-SP800-160-V1R1, BOOK-ANDERSON-SE3]
further_reading: [NIST-SP800-207]
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
module: M00
---

# Lendo diagramas arquiteturais: componentes, fluxos e fronteiras

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 · M00-L07</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Diagramas são a principal forma de comunicação entre arquitetos, engenheiros e auditores. Um bom diagrama responde rapidamente a perguntas de segurança; um diagrama ruim esconde exatamente o que importa. Esta aula ensina um método de leitura — componentes, fluxos, dados, fronteiras — e um conjunto de perguntas para encontrar o que falta. É a habilidade que conecta todo o Módulo 00 com o resto da formação.

**Pré-requisitos:** [Segmentação e conectividade](03-segmentation-connectivity.md) e [Cloud computing](06-cloud-computing-models.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Identificar componentes, fluxos, armazenamentos, atores e fronteiras de confiança em um diagrama.
- Avaliar se um fluxo está suficientemente descrito (protocolo, autenticação, dados e sentido).
- Encontrar os pontos em que fluxos atravessam fronteiras de confiança.
- Listar as perguntas que um diagrama incompleto deixa sem resposta.

## Conceito

### Um diagrama é uma visão, não o sistema

A ISO/IEC/IEEE 42010 distingue a **arquitetura** de um sistema da sua **descrição**, e organiza a descrição em **visões** que atendem às preocupações de partes interessadas específicas. Um diagrama de rede, um diagrama de fluxo de dados e um diagrama de implantação mostram o mesmo sistema sob ângulos diferentes. O NIST SP 800-160 Vol. 1 Rev. 1 define três *System Security Viewpoints* (§3.8, p. 27): a **função do sistema**, que dá o contexto; a **função de segurança**, com aspectos passivos (arquitetura e design) e ativos (controles e mecanismos); e os **ativos do ciclo de vida** — sistemas com que interage, dados associados e capacidades de desenvolvimento e operação —, que podem causar perdas ou servir de caminho para elas. Diagramas costumam mostrar a primeira perspectiva e omitir a terceira.

Consequência prática: **nenhum diagrama mostra tudo**. A primeira pergunta de leitura é *para que serve este diagrama e quem é o público?* — e a segunda é *o que ele deixou de fora?*.

### O que um arquiteto de segurança procura

| Elemento | Pergunta |
|:---|:---|
| **Componentes** | O que cada caixa faz? Quem a opera? Onde roda? |
| **Atores** | Quem usa o sistema — clientes, funcionários, parceiros, outros sistemas? |
| **Fluxos** | Quem inicia a comunicação? Por qual protocolo? Como o chamador se autentica? Que dados trafegam? |
| **Armazenamentos** | Que dados ficam onde? Qual a classificação? Quem acessa? |
| **Fronteiras** | Onde muda o nível de confiança? Qual controle existe em cada travessia? |

Anderson trata fronteiras como algo que depende tanto de governança e incentivos quanto de tecnologia (*Security Engineering*, Cap. 10 *Boundaries*). Por isso uma fronteira num diagrama deve vir acompanhada da resposta a *quem garante que ela existe*.

## Fundamentos técnicos

### Um método de leitura em quatro passagens

1. **Contexto.** Qual o objetivo do sistema? Quem são os atores? O que está fora do escopo?
2. **Componentes e dados.** Liste os componentes e os armazenamentos, e marque onde ficam dados sensíveis.
3. **Fluxos.** Numere os fluxos. Para cada um, registre: origem, destino, sentido de iniciação, protocolo, autenticação e dados.
4. **Fronteiras.** Desenhe (ou confira) as zonas. Destaque os fluxos que **atravessam** fronteiras — são eles que merecem mais controles e mais atenção na revisão.

### Fluxos bem e mal descritos

| Fluxo mal descrito | Fluxo bem descrito |
|:---|:---|
| Portal → API | ② Portal → API de pedidos · HTTPS com mTLS · token de serviço · dados de pedido |
| App → Banco | ③ API → Banco · SQL sobre TLS · conta de serviço dedicada · dados pessoais |
| Integra com fornecedor | ④ API → SaaS de e-mail · HTTPS · chave de API · nome e e-mail do cliente |

A coluna da direita permite responder, sem reunião adicional, às perguntas de revisão: há autenticação? Há criptografia? Que dados saem da empresa?

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m00-l07-reading-example.mmd"
```

<figcaption>Figura 1 — Diagrama com componentes, fluxos numerados e rotulados e fronteiras de confiança.</figcaption>
</figure>

Aplicando o método à figura: há quatro zonas internas, mais um terceiro externo; dados pessoais estão no banco da zona de dados e trafegam nos fluxos ①, ③ e ④. Todos os fluxos atravessam fronteiras, e o fluxo ④ **sai da organização** — exige avaliação do fornecedor, contrato e base legal para compartilhar dados. Esse tipo de conclusão só é possível porque os fluxos estão rotulados.

### Convenções que ajudam

- **Zonas como contornos** que agrupam componentes do mesmo nível de confiança.
- **Setas no sentido de quem inicia** a comunicação (importante para regras de firewall).
- **Legenda** para cores, ícones e tipos de linha — como nos diagramas desta formação, em que contornos indicam identidade, controles, atores e componentes não confiáveis.
- **Numeração dos fluxos**, para referência no texto e nos requisitos.
- **Data e versão** — diagramas envelhecem; um diagrama sem data é um diagrama de confiabilidade desconhecida.

### O que diagramas costumam omitir

- Fluxos administrativos (quem administra cada componente e de onde).
- Fluxos de logs e monitoramento.
- Dependências de serviços compartilhados: DNS, identidade, NTP, gerenciador de segredos.
- Fluxos de backup e de replicação.
- Integrações "temporárias" com terceiros.

Essas omissões não são detalhes: o acesso administrativo e as dependências compartilhadas são caminhos frequentes de ataque.

## Exemplo empresarial

!!! example "Aurora Pagamentos — o diagrama aprovado que não mostrava o essencial"

    Um projeto chegou ao comitê de arquitetura com um diagrama limpo: aplicativo, API, banco. Ao aplicar as quatro passagens, o arquiteto perguntou:

    - Quem administra o banco e de onde? *(Não estava no diagrama: um prestador acessava por VPN própria.)*
    - Para onde vão os logs da API? *(Para um serviço SaaS de observabilidade, incluindo o corpo das requisições — com dados de cartão.)*
    - Como a API obtém a senha do banco? *(Arquivo de configuração no próprio servidor.)*

    Nenhum desses fluxos aparecia, e todos atravessavam fronteiras. O projeto voltou com um diagrama de fluxo de dados completo e três requisitos novos: acesso administrativo pelo bastion corporativo, mascaramento de dados sensíveis nos logs e uso do gerenciador de segredos.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Fluxos | Setas sem rótulo | Fluxos numerados, com protocolo, autenticação e dados |
| Fronteiras | Implícitas ou ausentes | Zonas explícitas com nível de confiança |
| Escopo | Apenas o caminho principal | Inclui administração, logs, backup e dependências compartilhadas |
| Manutenção | Diagrama feito uma vez, para aprovação | Diagrama versionado, atualizado a cada mudança relevante |

## Aplicabilidade: on-premises, cloud e híbrido

| Ambiente | Ponto de atenção ao ler |
|:---|:---|
| **On-premises** | Zonas de rede e firewalls costumam estar desenhados; identidade e dados, nem sempre. |
| **Cloud** | Fronteiras incluem contas, projetos e assinaturas, não só redes; serviços gerenciados precisam aparecer como componentes com suas próprias permissões. |
| **Híbrido** | A conexão entre ambientes (VPN, link dedicado) e as dependências de identidade e DNS são frequentemente omitidas — e são críticas. |

## Como especificar e implementar

- "Toda solução submetida à revisão de arquitetura inclui diagrama com zonas de confiança e fluxos numerados, cada um com protocolo, autenticação e dados."
- "Diagramas incluem fluxos administrativos, de logs, de backup e integrações com terceiros."
- "Diagramas são versionados com a solução e revisados a cada mudança de fluxo ou fronteira."

## Trade-offs, limitações e antipadrões

- **Detalhe × legibilidade.** Um diagrama com tudo vira ilegível. Use várias visões: contexto, fluxo de dados, implantação.
- **Antipadrão — diagrama de marketing:** ícones bonitos, nenhuma informação sobre fluxos.
- **Antipadrão — diagrama como verdade:** o ambiente real diverge; validar com inventário e configuração (tema do [Laboratório 02](../../labs/lab-02-architecture-modeling.md)).

## Como validar

- Aplicar as quatro passagens e listar perguntas sem resposta.
- Comparar o diagrama com regras de firewall, inventário e configurações reais.
- Perguntar ao time que opera o sistema quais fluxos existem e não estão desenhados.

## Como apresentar e justificar

- **Para engenharia:** "Precisamos dos fluxos administrativos e de logs no diagrama; sem eles não conseguimos avaliar as fronteiras."
- **Para gestores:** "O desenho aprovado não mostrava que dados de cartão iam para um fornecedor externo. Diagramas completos evitam que decisões de risco sejam tomadas sem informação."

## Checklist de revisão arquitetural

- [ ] O diagrama tem propósito, data e versão.
- [ ] Zonas e níveis de confiança estão explícitos.
- [ ] Fluxos estão numerados, com sentido, protocolo, autenticação e dados.
- [ ] Armazenamentos indicam a classificação dos dados.
- [ ] Administração, logs, backup, dependências compartilhadas e terceiros aparecem.
- [ ] Fluxos que atravessam fronteiras têm controles identificados.

## Questões de compreensão

**1.** Por que a seta de um fluxo deve indicar quem inicia a comunicação?

??? success "Resposta comentada"

    Porque controles como firewalls stateful decidem com base em quem inicia a conexão, e porque iniciar uma conexão de uma zona menos confiável para uma mais confiável é um sinal de risco que precisa de controle específico.

**2.** Cite três tipos de fluxo frequentemente omitidos em diagramas e por que importam.

??? success "Resposta comentada"

    Fluxos administrativos (são caminhos privilegiados de ataque), fluxos de logs (podem levar dados sensíveis para terceiros) e dependências compartilhadas como identidade e DNS (a falha ou o comprometimento delas afeta todo o sistema). Backup e integrações com terceiros também costumam faltar.

**3.** O que significa dizer que um diagrama é uma "visão"?

??? success "Resposta comentada"

    Que ele representa o sistema a partir de uma perspectiva, para atender às preocupações de um público específico. Nenhuma visão mostra tudo; por isso se usa mais de uma e se pergunta sempre o que ficou de fora.

## Exercício de tomada de decisão

!!! question "Cenário: revisão do diagrama da Figura 1"

    Você recebeu o diagrama da Figura 1 para aprovação. Liste: (a) duas perguntas que ele responde bem; (b) três perguntas que ele não responde; (c) qual fluxo você analisaria primeiro e por quê; (d) decida entre (A) aprovar como está, (B) aprovar com condições, registrando as perguntas sem resposta como pendências com prazo, e (C) devolver para complementação antes de nova revisão, pelos critérios risco de aprovar sem entender os fluxos de dados pessoais, qualidade da documentação para operação e auditoria e agilidade do projeto.

??? success "Resolução de referência"

    - **(a)** Quais fluxos atravessam fronteiras e com qual autenticação; onde ficam os dados pessoais.
    - **(b)** Quem administra cada componente e de onde; para onde vão os logs; como a API obtém credenciais (token de serviço, chave de API do SaaS); onde fica o backup do banco.
    - **(c)** O fluxo **④**, porque leva dados pessoais para fora da organização — exige avaliação do fornecedor, base contratual e legal, e proteção da chave de API. Em seguida, o fluxo **①**, por ser o único iniciado a partir da zona não confiável.
    - **(d)**

        | Critério | Peso | A — Aprovar | B — Aprovar com condições | C — Devolver |
        |:---|:---|:---|:---|:---|
        | Risco de aprovar sem entender os fluxos de dados pessoais | 3 | 1 | 2 | 3 |
        | Qualidade da documentação para operação e auditoria | 2 | 1 | 2 | 3 |
        | Agilidade do projeto | 1 | 3 | 3 | 1 |
        | **Total ponderado** | | **8** | **13** | **16** |

        **Recomendação: C.** As lacunas incluem justamente o fluxo que leva dados pessoais para fora da organização; aprovar antes de entendê-lo transfere a análise para depois da implantação. A alternativa B seria adequada se as pendências fossem apenas operacionais, como o destino dos logs.

## Pontos-chave

- Um diagrama é uma visão do sistema, feita para um público; nenhum mostra tudo.
- Leia em quatro passagens: contexto, componentes e dados, fluxos, fronteiras.
- Fluxos bem descritos têm número, sentido, protocolo, autenticação e dados.
- Fluxos que atravessam fronteiras são os que mais exigem controles.
- Administração, logs, backup, dependências compartilhadas e terceiros são as omissões mais comuns — e as mais perigosas.

## Referências

### Fundamentação principal

- ISO/IEC/IEEE. *42010:2022 — Software, systems and enterprise — Architecture description*. <https://committee.iso.org/standard/74393.html> — distinção entre arquitetura e descrição, visões e preocupações — norma paga, não consultada na íntegra; a descrição usada nesta aula se apoia na página oficial da norma e em resumos públicos.
- NIST. *SP 800-160 Vol. 1 Rev. 1 — Engineering Trustworthy Secure Systems*. 2022. §3.8 *System Security Viewpoints* (p. 27). <https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final> — as três perspectivas de análise de segurança.
- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020. Cap. 10 *Boundaries*, §10.1 (p. 341). <https://www.cl.cam.ac.uk/archive/rja14/book.html> — fronteiras dependem de governança e incentivos, não só de tecnologia.

### Leitura complementar

- NIST. *SP 800-207 — Zero Trust Architecture*. 2020. §2.1 *Tenets of Zero Trust* (p. 6) — por que a localização na rede não deve conferir confiança, o que muda a forma de ler fronteiras.

### Aplicação prática

- O [Laboratório 02](../../labs/lab-02-architecture-modeling.md) gera diagramas a partir de um modelo com zonas e fluxos rotulados — o mesmo método desta aula, automatizado.
- O M04 transforma este método em **Data Flow Diagrams** para threat modeling.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
