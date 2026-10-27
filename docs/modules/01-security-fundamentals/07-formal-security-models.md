---
id: M01-L07
title: "Modelos formais: Bell-LaPadula, Biba, Clark-Wilson e Brewer-Nash"
description: Os modelos formais clássicos de segurança — confidencialidade multinível, integridade, integridade comercial e conflito de interesses —, o que ensinam sobre controle de acesso e onde aparecem em sistemas atuais.
domain: security-foundations
tier: professional
status: published
prerequisites: [M01-L02, M01-L06]
objectives:
  - Explicar as regras de Bell-LaPadula e Biba e o objetivo de cada modelo.
  - Descrever os elementos do modelo Clark-Wilson e sua relação com controles internos.
  - Explicar o modelo Brewer-Nash (Chinese Wall) e quando aplicá-lo.
  - Relacionar os modelos a controles presentes em sistemas e processos atuais, e reconhecer suas limitações.
minutes: 60
sources: [BOOK-ANDERSON-SE3]
further_reading: [NIST-SP800-160-V1R1, SALTZER-SCHROEDER-1975]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M01
---

# Modelos formais: Bell-LaPadula, Biba, Clark-Wilson e Brewer-Nash

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 · M01-L07</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">60 min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Modelos formais de segurança parecem distantes da prática — matemática dos anos 1970 e 1980 para sistemas militares e bancários. Mas eles formalizam ideias que aparecem em todo sistema moderno: rótulos de classificação, níveis de integridade, transações controladas com dupla aprovação, barreiras entre clientes concorrentes. Esta aula apresenta os quatro modelos clássicos com base em Anderson, mostra onde cada um aparece hoje e o que suas limitações ensinam a um arquiteto.

**Pré-requisitos:** [Princípios de design seguro](02-secure-design-principles.md) e [Ameaça, vulnerabilidade e risco](06-threat-vulnerability-risk.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar as regras de Bell-LaPadula e Biba e o objetivo de cada modelo.
- Descrever os elementos do modelo Clark-Wilson e sua relação com controles internos.
- Explicar o modelo Brewer-Nash (Chinese Wall) e quando aplicá-lo.
- Relacionar os modelos a controles presentes em sistemas e processos atuais, e reconhecer suas limitações.

## Conceito

### O que é um modelo de política de segurança

Um **modelo de política de segurança** é uma descrição precisa — frequentemente formal — das propriedades que um sistema deve garantir (*Security Engineering*, Cap. 9, §9.2, p. 316). Seu valor está em permitir raciocinar sobre o sistema: provar que certas violações são impossíveis se as regras forem respeitadas, ou mostrar onde as regras são insuficientes.

Os modelos se distinguem pela propriedade que priorizam:

| Modelo | Propriedade | Contexto de origem |
|:---|:---|:---|
| **Bell-LaPadula** | Confidencialidade | Classificação militar |
| **Biba** | Integridade | Proteção contra contaminação por dados não confiáveis |
| **Clark-Wilson** | Integridade comercial | Contabilidade e bancos |
| **Brewer-Nash** | Conflito de interesses | Consultorias e bancos de investimento |

## Fundamentos técnicos

### Bell-LaPadula: confidencialidade multinível

Sujeitos (usuários, processos) e objetos (documentos) recebem **níveis** — por exemplo, Confidencial, Secreto, Ultrassecreto — e, opcionalmente, compartimentos. O modelo tem duas regras centrais (§9.3.2, pp. 320–321):

- **Propriedade de segurança simples — *no read up*:** um sujeito não lê objetos de nível superior ao seu.
- **Propriedade estrela (*-property) — *no write down*:** um sujeito não escreve em objetos de nível inferior ao seu.

A segunda regra é a menos intuitiva e a mais importante: impede que um **cavalo de Troia** executando com nível Secreto copie informação para um documento Confidencial, acessível a quem não deveria lê-la. As regras são **mandatórias** — aplicadas pelo sistema independentemente da vontade do usuário, ao contrário do controle discricionário típico do Unix.

Anderson registra as críticas clássicas (§9.3.3): o modelo não trata bem a mudança de rótulos, os sujeitos confiáveis que precisam "desclassificar" informações, nem a criação e destruição de objetos.

### Biba: integridade

O modelo **Biba** é o **dual** de Bell-LaPadula para integridade (§9.3.5, pp. 325–326):

- **No read down:** um processo de alta integridade não lê dados de integridade baixa (não se contamina).
- **No write up:** um processo de baixa integridade não escreve em objetos de integridade alta (não os corrompe).

O exemplo de Anderson é a calibração de um equipamento de eletrocardiograma: a configuração calibrada (alta integridade) não pode ser alterada por dados vindos de fontes não confiáveis. No Windows, os **níveis de integridade** de processos seguem a lógica Biba e aplicam *no write up* por padrão (§9.5.1).

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m01-l07-blp-biba.mmd"
```

<figcaption>Figura 1 — Fluxos permitidos e proibidos em Bell-LaPadula (confidencialidade) e Biba (integridade).</figcaption>
</figure>

### Clark-Wilson: integridade comercial

Bell-LaPadula e Biba vêm do mundo militar. Em 1987, Clark e Wilson propuseram um modelo voltado a **sistemas comerciais**, especialmente contabilidade (*Security Engineering*, Cap. 12, §12.2.3, p. 410). Seus elementos:

| Elemento | Significado | Exemplo bancário |
|:---|:---|:---|
| **CDI** (*Constrained Data Item*) | Dado cuja integridade o sistema garante | Saldos das contas |
| **UDI** (*Unconstrained Data Item*) | Entrada ainda não controlada | Um pedido de transferência recebido |
| **TP** (*Transformation Procedure*) | Única forma permitida de alterar CDIs, preservando invariantes | Transação de transferência que mantém o balanço |
| **IVP** (*Integrity Verification Procedure*) | Verificação de que os CDIs estão íntegros | Conferir que os livros fecham |

O acesso é controlado por **triplas (sujeito, TP, CDI)**: um usuário só altera um dado por meio de procedimentos permitidos a ele. O modelo exige **separação de funções** e uma **trilha de auditoria** de onde cada transação possa ser reconstruída (§12.2.3). Anderson observa as limitações: o modelo exige "uma política adequada de separação de funções", mas não diz qual — e não garante que a transação esteja *certa*, apenas que foi feita pelo caminho controlado.

Clark-Wilson é o modelo formal por trás de ideias que todo arquiteto usa: **dados críticos só mudam por APIs que aplicam regras de negócio**, nunca por acesso direto ao banco; **duas pessoas** para operações sensíveis; **auditoria** de cada transação.

### Brewer-Nash: a Chinese Wall

O modelo **Brewer-Nash**, conhecido como **Chinese Wall**, trata conflito de interesses: um analista que acessou informações de um banco não pode acessar informações de um banco concorrente. O acesso depende do **histórico** do sujeito — é uma regra com estado. Anderson trata o modelo no capítulo sobre fronteiras (§10.4.8, p. 369), destacando que ele usa regras com estado e separação de funções, e que tem fraquezas, como canais encobertos e períodos curtos de "resfriamento".

### O que as limitações ensinam

Os problemas apontados por Anderson para sistemas multinível (§9.6) valem para qualquer arquitetura:

- **Canais encobertos** (§9.6.3): informação pode vazar por meios não previstos pelo modelo — tempo de resposta, uso de recursos.
- **Composição** (§9.6.1): dois sistemas seguros, compostos, podem formar um sistema inseguro.
- **Problemas práticos** (§9.6.6): excesso de classificação, explosão de rótulos e custo de adaptar aplicações reduzem a adoção.

## Exemplo empresarial

!!! example "Aurora Pagamentos — modelos na prática"

    | Necessidade | Modelo | Controle adotado |
    |:---|:---|:---|
    | Saldos e liquidações só mudam por regras de negócio | Clark-Wilson | Nenhum acesso de escrita direto ao banco de liquidação; alterações apenas pela API de liquidação, que valida invariantes; conciliação diária como IVP |
    | Estornos altos exigem duas pessoas | Clark-Wilson (separação de funções) | Solicitante e aprovador distintos, registrados |
    | Equipe de consultoria atende dois varejistas concorrentes | Brewer-Nash | Analistas alocados a um cliente não acessam dados do concorrente; a alocação é registrada e verificada pelo sistema |
    | Arquivos recebidos de parceiros não podem contaminar a configuração de produção | Biba | Processamento em ambiente de menor integridade; promoção de dados apenas por procedimento validado |

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Alteração de dados críticos | Acesso direto ao banco por administradores e integrações | Apenas por procedimentos controlados (APIs), com auditoria |
| Classificação | Rótulos sem efeito técnico | Rótulos que orientam controles de acesso e de fluxo |
| Conflito de interesses | Tratado só por política escrita | Regras verificadas pelo sistema, com base no histórico de acesso |
| Dados não confiáveis | Processados no mesmo ambiente da configuração crítica | Separados por nível de integridade |

## Aplicabilidade: on-premises, cloud e híbrido

Os modelos são independentes de ambiente. Seus mecanismos aparecem em SELinux e AppArmor (controle mandatório), nos níveis de integridade do Windows, em rótulos de classificação de dados em plataformas de colaboração e em políticas de acesso baseadas em atributos (ABAC, M06-L02), que permitem expressar regras como as de Brewer-Nash.

## Como especificar e implementar

- "Dados classificados como críticos para integridade só são alterados por procedimentos aprovados; acesso direto de escrita é proibido e monitorado."
- "Operações que alteram dados críticos acima de limites definidos exigem duas identidades distintas."
- "Dados recebidos de fontes externas são processados em ambiente separado antes de serem promovidos."

## Trade-offs, limitações e antipadrões

- **Rigidez:** aplicar Bell-LaPadula estrito em ambientes corporativos gera excesso de classificação e bloqueia a colaboração.
- **Antipadrão — "DBA pode tudo":** administradores com escrita direta em dados críticos anulam qualquer modelo de integridade.
- **Limitação:** modelos formais garantem propriedades dentro de suas premissas; canais encobertos e composição ficam fora delas.

## Como validar

- Verificar quem tem escrita direta em bancos de dados críticos.
- Conferir se os procedimentos de verificação de integridade (conciliações, verificações de balanço) existem e são executados.
- Testar se regras de conflito de interesses são aplicadas pelo sistema.

## Como apresentar e justificar

- **Para engenharia:** "Pelo modelo Clark-Wilson, a liquidação só pode ser alterada pela API; o acesso direto de escrita será removido."
- **Para gestores:** "Nenhuma pessoa poderá alterar saldos fora do processo controlado, e cada alteração terá autor e registro."

## Checklist de revisão arquitetural

- [ ] Dados críticos para integridade têm procedimentos controlados de alteração.
- [ ] Não há escrita direta em dados críticos fora desses procedimentos.
- [ ] Verificações de integridade são executadas periodicamente.
- [ ] Separação de funções é aplicada pelo sistema em operações sensíveis.
- [ ] Dados não confiáveis são processados separadamente da configuração crítica.

## Questões de compreensão

**1.** Por que a regra *no write down* de Bell-LaPadula é necessária, se a regra *no read up* já existe?

??? success "Resposta comentada"

    Porque um programa malicioso executando com o nível do usuário (por exemplo, Secreto) pode ler informações desse nível e copiá-las para um objeto de nível inferior, acessível a outros. *No write down* impede esse vazamento.

**2.** Em Clark-Wilson, o que é um TP e por que ele é importante?

??? success "Resposta comentada"

    Um *Transformation Procedure* é a única forma permitida de alterar dados controlados (CDIs), preservando suas invariantes. Garante que dados críticos só mudem pelo caminho que aplica as regras de negócio.

**3.** O que diferencia Brewer-Nash dos outros modelos?

??? success "Resposta comentada"

    A decisão de acesso depende do histórico do sujeito: depois de acessar dados de uma empresa, ele fica impedido de acessar dados de concorrentes. As regras têm estado.

## Exercício de tomada de decisão

!!! question "Cenário: correções de dados no ERP da Meridiana"

    Para corrigir erros, a equipe de sistemas executa comandos SQL diretamente no banco do ERP, inclusive em tabelas financeiras. A auditoria apontou o problema. Compare (A) manter o SQL direto, com gravação das sessões e revisão mensal; (B) uma solução inspirada em Clark-Wilson, com procedimentos controlados para as correções recorrentes, acesso excepcional com dupla aprovação e verificação diária de integridade; (C) proibir qualquer correção fora das telas do ERP e encaminhar as demais ao fornecedor, pelos critérios integridade e separação de funções, capacidade de suporte e auditabilidade. Detalhe a alternativa escolhida.

??? success "Resolução de referência"

    | Critério | Peso | A — SQL direto com gravação | B — Inspirada em Clark-Wilson | C — Só pelas telas ou pelo fornecedor |
    |:---|:---|:---|:---|:---|
    | Integridade e separação de funções | 3 | 1 | 3 | 3 |
    | Capacidade de suporte | 2 | 3 | 2 | 1 |
    | Auditabilidade | 2 | 2 | 3 | 2 |
    | **Total ponderado** | | **13** | **19** | **15** |

    **Recomendação: B.** A alternativa A só descobre o problema depois; a C protege a integridade, mas paralisa correções urgentes e tende a gerar desvios informais.

    - **TPs para correções frequentes:** criar procedimentos no ERP (ou scripts aprovados e versionados) para os tipos de correção recorrentes, que validam regras e registram o motivo.
    - **Correções excepcionais:** acesso de escrita just-in-time, com chamado aprovado por uma segunda pessoa do financeiro, sessão gravada e revisão posterior.
    - **IVP:** conciliação automática diária entre o ERP e os registros bancários, com alerta em divergências.
    - **Remover** o acesso permanente de escrita da equipe de sistemas nas tabelas financeiras.

    O resultado preserva a capacidade de suporte, mas faz com que **toda alteração passe por um caminho controlado, com separação de funções e auditoria** — a essência do modelo.

## Pontos-chave

- Bell-LaPadula protege confidencialidade: *no read up* e *no write down*.
- Biba é o dual para integridade: *no read down* e *no write up*.
- Clark-Wilson formaliza a integridade comercial: dados críticos mudam apenas por procedimentos controlados, com separação de funções e auditoria.
- Brewer-Nash aplica regras com estado para conflitos de interesse.
- As limitações dos modelos — canais encobertos, composição, custo prático — são lições para qualquer arquitetura.

## Referências

### Fundamentação principal

- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020. <https://www.cl.cam.ac.uk/archive/rja14/book.html>
    - Cap. 9 *Multilevel Security* (pp. 315–339): §9.2 modelos de política (p. 316); §9.3.2 Bell-LaPadula (p. 320); §9.3.3 críticas (p. 321); §9.3.5 Biba (p. 325); §9.5.1 Windows (p. 329); §9.6 limitações (pp. 331–337).
    - Cap. 12 *Banking and Bookkeeping*: §12.2.3 Clark-Wilson (p. 410); §12.2.4 controles internos (p. 411).
    - Cap. 10 *Boundaries*: §10.4.8 *The Chinese Wall* (p. 369).

### Leitura complementar

- NIST. *SP 800-160 Vol. 1 Rev. 1*. Apêndice E — princípios *Hierarchical Protection* (E.13) e *Domain Separation* (E.12), relacionados aos modelos multinível *(localizados pelo sumário)*.
- J. Saltzer e M. Schroeder. *The Protection of Information in Computer Systems*. 1975.

### Aplicação prática

- Identifique na sua organização um dado crítico para integridade e verifique: por quais caminhos ele pode ser alterado? Todos são procedimentos controlados?

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
