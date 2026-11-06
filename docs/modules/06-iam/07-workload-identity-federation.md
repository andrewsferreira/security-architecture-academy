---
id: M06-L07
title: "Aula 07 — Workload Identity Federation"
public_title: "Módulo 6 — Aula 07 — Workload Identity Federation"
description: Como eliminar chaves de longa duração de pipelines, clusters e integrações entre nuvens — federação de identidade de workload por troca de tokens, condições de confiança por emissor, sujeito e audiência, e os erros de configuração que transformam a federação em porta aberta.
domain: iam
tier: architect
status: published
prerequisites: [M06-L04, M06-L06]
objectives:
  - Explicar a troca de tokens que sustenta a federação de identidade de workload.
  - Especificar condições de confiança precisas por emissor, sujeito e audiência.
  - Comparar as implementações de Google Cloud, Microsoft Entra e AWS e reconhecer o padrão comum.
  - Projetar a federação para pipelines e workloads multicloud com escopo mínimo.
minutes: 60
sources: [GCP-WORKLOAD-IDENTITY-FED, MS-ENTRA-WORKLOAD-ID-FED, AWS-IAM-OIDC-ROLE, SPIFFE-CONCEPTS, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [RFC-9700, OIDC-CORE-1]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M06
---

# Aula 07 — Workload Identity Federation { #workload-identity-federation }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 6 · Nível 2</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">60 min · ID técnico: M06-L07</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Pipelines de implantação, clusters Kubernetes e integrações entre nuvens precisam se autenticar em APIs de nuvem. A forma tradicional — uma chave de acesso armazenada em uma variável — é uma das causas mais comuns de comprometimento de contas de nuvem. A **federação de identidade de workload** troca a chave por uma relação de confiança: o workload apresenta um token de curta duração emitido pela sua plataforma, e a nuvem o troca por credenciais temporárias **se** o token satisfizer condições precisas. Esta aula mostra o padrão, suas implementações e onde ele costuma falhar.

**Pré-requisitos:** [Federação](04-federation-saml-oauth-oidc.md) e [Contas privilegiadas e identidades de máquina](06-privileged-machine-identities.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar a troca de tokens que sustenta a federação de identidade de workload.
- Especificar condições de confiança precisas por emissor, sujeito e audiência.
- Comparar as implementações de Google Cloud, Microsoft Entra e AWS e reconhecer o padrão comum.
- Projetar a federação para pipelines e workloads multicloud com escopo mínimo.

## Conceito

### O padrão

1. O workload obtém da **sua plataforma** (o sistema de CI, o cluster, outra nuvem) um **token de identidade** assinado, de curta duração, com *claims* que o descrevem — repositório, ramo, ambiente, namespace, conta de serviço.
2. O workload apresenta esse token ao **serviço de tokens** da nuvem de destino.
3. O serviço valida a assinatura pelo **emissor** confiável e aplica as **condições** de confiança.
4. Se as condições forem satisfeitas, devolve **credenciais temporárias** com permissões limitadas.

No Google Cloud, a documentação descreve a troca como seguindo a especificação OAuth 2.0 de *token exchange* (a RFC 8693, para a qual a página aponta): o Security Token Service verifica a credencial externa e devolve um token federado. A configuração usa **pools** e **provedores** de identidade de workload, **mapeamento de atributos** (como derivar atributos do token externo) e **condições de atributos** — expressões em CEL (*Common Expression Language*).

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m06-l07-wif.mmd"
```

<figcaption>Figura 1 — O job recebe um token OIDC da sua plataforma, troca-o no serviço de tokens da nuvem e só recebe credenciais temporárias se a condição de atributos for satisfeita.</figcaption>
</figure>

### Por que importa

| Chave de longa duração | Federação |
|:---|:---|
| Segredo armazenado, copiado, vazável | Nenhum segredo armazenado no workload |
| Validade de meses ou anos | Credenciais de minutos ou horas |
| Rotação manual, frequentemente esquecida | Sem rotação: cada execução obtém credencial nova |
| Uso de qualquer lugar | Só a identidade que satisfaz as condições |

A documentação do Google Cloud chama chaves de conta de serviço de "credenciais poderosas" que podem representar risco se mal gerenciadas; a da Microsoft lembra que segredos e certificados precisam ser armazenados com segurança e rotacionados regularmente, e que há risco de indisponibilidade quando expiram.

## Fundamentos técnicos

### A segurança está nas condições

A federação é tão segura quanto as condições que definem **quem** pode trocar tokens. As três nuvens convergem para a mesma ideia:

| Nuvem | Onde se define a confiança | O que precisa ser preciso |
|:---|:---|:---|
| **Google Cloud** | Provedor do pool + condição de atributos (expressão CEL) + concessão de papéis a principais | Condição que restringe repositório, ramo ou conta; evitar conceder acesso a todo o pool |
| **Microsoft Entra** | Credencial de identidade federada em uma identidade gerenciada atribuída pelo usuário ou em um registro de aplicação | `issuer`, `subject` e `audience` com correspondência exata, sensível a maiúsculas |
| **AWS** | Política de confiança do papel IAM com o provedor OIDC como principal | Condições sobre `aud` e `sub`; sem `sub` restrito, repositórios de terceiros podem assumir o papel |

A documentação da AWS é explícita: se a condição `sub` do provedor do GitHub não for limitada a uma organização ou repositório, **ações de organizações ou repositórios fora do seu controle** podem assumir o papel. O IAM rejeita, ao criar ou alterar a política de confiança, condições `sub` ausentes, nulas ou formadas só por curinga (`*` ou `?`) para esse provedor — mas aceita um valor como `repo:organizacao/*`, que ainda admite qualquer repositório da organização; a própria documentação recomenda restringir a repositórios ou ramos específicos. O formato do `sub` depende do evento e da idade do repositório: com ambiente, `repo:ORG/REPO:environment:NOME`; sem ambiente, o ramo, a tag ou `pull_request`; e repositórios criados depois de 15 de julho de 2026 usam por padrão um formato imutável com os identificadores do dono e do repositório (`repo:ORG@ID/REPO@ID:...`) — a condição precisa usar o formato que o repositório de fato emite. A do Google Cloud alerta que conceder acesso a todas as identidades de um pool "pode trazer risco", recomenda um pool para cada ambiente fora do Google Cloud (desenvolvimento, homologação, produção) e condições que impeçam o uso de credenciais destinadas a outra plataforma (o problema do *confused deputy*).

### Desenho de escopo

| Dimensão | Recomendação |
|:---|:---|
| **Ambiente** | Pools ou identidades separados para produção e não produção |
| **Origem** | Repositório e ramo específicos; para produção, ramos protegidos ou ambientes com aprovação |
| **Permissão** | Papel com o mínimo necessário para aquela implantação |
| **Duração** | A menor que a operação permita |
| **Registro** | Logs de troca de token e de uso, com o sujeito federado identificável |

### Federação entre nuvens e com workloads internos

O mesmo padrão permite que um workload na AWS acesse o Google Cloud, que um cluster Kubernetes on-premises acesse a Azure, ou que workloads com identidade **SPIFFE** se autentiquem em nuvens que aceitem o emissor correspondente — a documentação da Microsoft lista, entre os cenários suportados, clusters Kubernetes em qualquer lugar (inclusive on-premises), GitHub Actions, Google Cloud, AWS e SPIFFE/SPIRE. Em arquiteturas multicloud, isso elimina a prática de copiar chaves de uma nuvem para a outra (Módulo 11).

## Exemplo empresarial

!!! example "Aurora Pagamentos — do segredo no pipeline à federação"

    Depois de revogar a chave de administrador do pipeline (Aula 06), a Aurora implantou federação para os três ambientes:

    | Ambiente | Condição de confiança | Permissão |
    |:---|:---|:---|
    | Desenvolvimento | Repositórios da organização, qualquer ramo | Implantação na conta de desenvolvimento |
    | Homologação | Repositório do serviço, ramo `main` | Implantação na conta de homologação |
    | Produção | Repositório do serviço, ambiente de implantação com aprovação humana | Papel de implantação restrito ao serviço |

    Um teste de revisão tentou trocar o token de um *fork* do repositório pelo papel de produção: a troca foi recusada pela condição de sujeito. O mesmo teste, contra a configuração inicial proposta pela equipe (condição apenas por organização), teria sido aceito.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Credencial do pipeline | Chave de longa duração em variável | Token de curta duração por execução |
| Confiança | Quem tiver a chave | Emissor + sujeito + audiência específicos |
| Produção | Mesma credencial dos demais ambientes | Identidade e condição próprias, com aprovação |
| Multicloud | Chaves copiadas entre nuvens | Federação entre emissores confiáveis |
| Auditoria | Uso de uma chave genérica | Sujeito federado identificável nos logs |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias que a federação de workload ajuda a cumprir:

| Controle ou padrão | Objetivo | Referência |
|:---|:---|:---|
| Autenticação de serviços | Identificar e autenticar o workload antes de conceder acesso à API de nuvem | SP 800-53: IA-9 (Service Identification and Authentication) |
| Nenhum segredo estático embutido | Eliminar chaves em variáveis, imagens e repositórios | SP 800-53: IA-5(7) (No Embedded Unencrypted Static Authenticators) |
| Privilégio mínimo | Papel federado com só as permissões daquela implantação ou daquele workload | SP 800-53: AC-6 (Least Privilege) |
| Chaves do emissor | Gerir as chaves que assinam os tokens do cluster, da CI ou do SPIFFE como ativos críticos | SP 800-53: SC-12 (Cryptographic Key Establishment and Management) |
| Registro das trocas | Gerar registros de troca e de uso com o sujeito federado | SP 800-53: AU-2 (Event Logging) e AU-12 (Audit Record Generation) |
| Contas de serviço | Inventário e gestão de contas de serviço e de suas credenciais | CIS v8.1: Controle 5 (Account Management) |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, a federação de workload é o padrão para pipelines e integrações. Em on-premises, workloads podem obter tokens de um emissor interno (por exemplo, um cluster Kubernetes ou uma infraestrutura SPIFFE) cuja chave de assinatura passa a ser um ativo crítico. Em ambientes híbridos, a federação substitui a prática de distribuir chaves de nuvem para servidores locais — desde que o emissor local seja protegido como parte do plano de controle.

## Como especificar e implementar

- "Workloads fora da nuvem de destino autenticam-se por federação; chaves de longa duração exigem exceção aprovada."
- "Condições de confiança restringem emissor, audiência e sujeito ao repositório, ramo, ambiente ou conta de serviço específicos."
- "Produção usa identidade e condição próprias, ligadas a um ambiente de implantação com aprovação."
- "Trocas de token e uso de credenciais federadas são registrados com o sujeito identificável."

## Trade-offs, limitações e antipadrões

- **Trade-off:** condições muito específicas exigem manutenção quando repositórios e ramos mudam; condições amplas facilitam a operação e o abuso.
- **Antipadrão — confiança por organização inteira:** qualquer repositório, inclusive de testes, alcança produção.
- **Antipadrão — um pool para todos os ambientes.**
- **Limitação:** a federação transfere a confiança para o emissor; comprometer a plataforma de CI ou o emissor do cluster permite obter tokens válidos.

## Como validar

- Tentar a troca a partir de um repositório, ramo ou *fork* não autorizado e confirmar a recusa.
- Revisar as condições de todos os provedores e políticas de confiança configurados.
- Listar chaves de longa duração remanescentes e seus donos.
- Verificar se os logs mostram o sujeito federado em cada uso.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Troca recusada a partir de repositório, ramo ou *fork* não autorizado | Registro do teste negativo para cada provedor configurado |
| Nenhuma condição de confiança só por organização ou por curinga em produção | Revisão das condições de todos os provedores e políticas de confiança |
| Produção com pool ou identidade próprios, ligados a ambiente com aprovação | Configuração dos provedores e do ambiente de implantação |
| Nenhuma chave de longa duração em pipelines fora das exceções aprovadas | Inventário de chaves com dono e prazo |
| Sujeito federado identificável em cada uso | Amostra de logs de troca e de uso |

## Como apresentar e justificar

- **Para a diretoria:** "Não existe mais uma chave capaz de implantar em produção guardada em algum lugar. Cada implantação recebe uma credencial que dura minutos e só funciona para aquele serviço."
- **Para engenharia:** "A condição de confiança é código. Ela passa por revisão como qualquer mudança de produção."

## Checklist de revisão arquitetural

- [ ] Nenhuma chave de longa duração em pipelines.
- [ ] Condições de emissor, audiência e sujeito específicas.
- [ ] Produção com identidade e aprovação próprias.
- [ ] Pools ou identidades separados por ambiente.
- [ ] Emissores locais protegidos como plano de controle.
- [ ] Logs de troca e uso com sujeito identificável.

## Questões de compreensão

**1.** O que a nuvem verifica antes de emitir credenciais na federação de workload?

??? success "Resposta comentada"

    A assinatura do token pelo emissor confiável e as condições de confiança — tipicamente emissor, audiência e sujeito, ou atributos mapeados do token, como repositório e ramo.

**2.** Qual o risco de não restringir o `sub` em uma federação com o GitHub na AWS?

??? success "Resposta comentada"

    Ações do GitHub de organizações ou repositórios fora do controle da empresa poderiam assumir o papel. Por isso o IAM rejeita, para esse provedor, políticas de confiança com `sub` ausente, nulo ou formado só por curinga — mas aceita `repo:organizacao/*`, e restringir a repositórios ou ramos específicos continua sendo responsabilidade de quem escreve a política.

**3.** A federação elimina todos os riscos de credencial do pipeline?

??? success "Resposta comentada"

    Não. Elimina segredos armazenados e de longa duração, mas transfere a confiança para a plataforma emissora. Se a plataforma de CI ou o emissor forem comprometidos, tokens válidos podem ser obtidos — por isso é preciso proteger o emissor e restringir condições e permissões.

## Exercício de tomada de decisão

!!! question "Cenário: cluster on-premises da Lumen acessando o armazenamento em nuvem"

    Um cluster Kubernetes no datacenter da Lumen processa imagens de exames e grava os resultados em armazenamento de objetos na nuvem. Hoje usa uma chave de conta de serviço montada como segredo em todos os pods. As opções são:

    - **A** — manter a chave, com rotação automática mensal e permissão reduzida a gravar no bucket de resultados;
    - **B** — federação com o emissor OIDC do próprio cluster (tokens de conta de serviço do Kubernetes), condição por namespace e conta de serviço;
    - **C** — implantar SPIFFE/SPIRE no cluster e federar a nuvem com o emissor SPIFFE.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério), recomende uma e proponha a arquitetura de federação e as condições de confiança.

**Objetivos avaliados:** Especificar condições de confiança precisas por emissor, sujeito e audiência; projetar a federação para pipelines e workloads multicloud com escopo mínimo.

**Entrega esperada:** Matriz ponderada e a arquitetura de federação: emissor, provedor na nuvem, condição de confiança, permissão e remoção da chave.

**Critérios de avaliação:**

- A condição de confiança restringe emissor, sujeito (namespace e conta de serviço) e audiência.
- A permissão concedida é a mínima necessária ao caso de uso.
- A chave estática é revogada e novas chaves são impedidas por política.

??? success "Resolução de referência"

    | Critério | Peso | A — Chave com rotação | B — Emissor OIDC do cluster | C — SPIFFE/SPIRE |
    |:---|:---|:---|:---|:---|
    | Eliminação de segredo de longa duração | 3 | 1 | 3 | 3 |
    | Precisão de quem pode obter a credencial | 2 | 1 | 3 | 3 |
    | Esforço de implantação e operação | 2 | 3 | 2 | 1 |
    | Reuso para outros workloads e nuvens | 1 | 1 | 2 | 3 |
    | **Total ponderado** | | **12** | **21** | **20** |

    - **Pesos:** o problema é a chave montada em todos os pods (peso 3). A precisão da condição e o esforço pesam 2: só o processador de imagens deve gravar resultados, e a equipe precisa operar a solução. O reuso pesa 1 — é benefício futuro, não o problema atual.
    - **Recomendação: B.** Elimina a chave usando um emissor que o cluster já tem; a condição por namespace e conta de serviço restringe o acesso ao processador de imagens. C chega perto e ganha em reuso, mas acrescenta um sistema a operar para um único caso de uso; A reduz o dano, mas a chave continua copiável de qualquer pod.

    **Arquitetura da opção B:**

    - **Emissor:** o próprio cluster, publicando a configuração OIDC e as chaves de assinatura dos tokens de conta de serviço do Kubernetes em endpoint acessível à nuvem; a chave de assinatura do cluster passa a ser ativo do plano de controle.
    - **Provedor na nuvem:** pool dedicado ao cluster de produção.
    - **Condição de confiança:** apenas tokens com o namespace e a conta de serviço do processador de imagens; audiência específica.
    - **Permissão:** gravar apenas no bucket de resultados, sem leitura de outros buckets nem administração.
    - **Remoção:** revogar a chave montada após a migração; impedir novas chaves por política.
    - **Trade-off aceito e risco residual:** a configuração OIDC e as chaves públicas do cluster precisam ficar acessíveis à nuvem, e a chave de assinatura do cluster passa a valer acesso ao bucket. O comprometimento do plano de controle do cluster permitiria emitir tokens — mitigado por endurecimento do cluster, acesso administrativo restrito e monitoração das trocas.
    - **O que mudaria a decisão:** se a Lumen tiver vários clusters e precisar também de mTLS entre workloads ou de federação com mais de uma nuvem, C ganha peso pelo reuso; se a distribuição do Kubernetes não permitir expor a configuração OIDC do emissor, B deixa de ser viável e C (ou um emissor intermediário) passa a ser o caminho.

    **Erros comuns:**

    - Federar o cluster inteiro sem condição por namespace e conta de serviço.
    - Esquecer que a chave de assinatura do emissor passa a ser ativo do plano de controle.
    - Manter a chave antiga ativa "por segurança" depois da migração.

## Pontos-chave

- A federação de workload troca segredos armazenados por tokens de curta duração e condições de confiança.
- A segurança está na precisão das condições: emissor, audiência e sujeito.
- Google Cloud, Microsoft Entra e AWS implementam o mesmo padrão com nomes diferentes.
- Separe ambientes e restrinja produção a ramos ou ambientes com aprovação.
- O emissor — plataforma de CI, cluster, SPIFFE — passa a ser parte do plano de controle.

## Referências

### Fundamentação principal

- Google Cloud. *Workload Identity Federation*. Atualizada em 26/10/2026. <https://docs.cloud.google.com/iam/docs/workload-identity-federation>. *(Lido; reconferido em 2026-10-29.)*
- Microsoft. *Workload identity federation — Microsoft Entra Workload ID*. 2025. <https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation>. *(Lido; reconferido em 2026-10-29.)*
- AWS. *Create a role for OpenID Connect federation (console)*. IAM User Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html>. *(Lido; reconferido em 2026-10-29.)*
- SPIFFE. *SPIFFE Concepts*. *(Lido.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles AC-6, AU-2, AU-12, IA-5(7), IA-9 e SC-12, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controle 5 — gratuito.

### Leitura complementar

- IETF. *RFC 9700* — práticas de segurança do OAuth 2.0.
- OpenID Foundation. *OpenID Connect Core 1.0* — estrutura do ID Token.

### Aplicação prática

- Encontre um pipeline da sua organização que use chave de nuvem armazenada e escreva a condição de confiança que o substituiria, restrita ao repositório, ao ramo e ao ambiente corretos.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
