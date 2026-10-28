---
id: M04-L07
title: "Aula 07 — Revisão arquitetural, As-Is/To-Be e validação de controles"
public_title: "Módulo 4 — Aula 07 — Revisão arquitetural, As-Is/To-Be e validação de controles"
description: Como conduzir uma revisão de arquitetura de segurança que termina em decisão — estado atual e estado-alvo, lacunas, transição, critérios de aceite — e como validar controles com os métodos de examinar, entrevistar e testar.
domain: enterprise-architecture
tier: architect
status: published
prerequisites: [M04-L06, M02-L08]
objectives:
  - Estruturar uma revisão de arquitetura de segurança com escopo, critérios, achados e decisão.
  - Representar estado atual e estado-alvo e derivar lacunas e etapas de transição.
  - Validar controles com os métodos examinar, entrevistar e testar e escolher o método adequado a cada controle.
  - Registrar o resultado da revisão em ADRs e no risk register.
minutes: 75
sources: [NIST-SP800-53A-R5, TM-MANIFESTO, NIST-SP800-37-R2]
further_reading: [NYGARD-ADR-2011, NIST-SP800-160-V1R1, OWASP-ASVS-5]
last_updated: 2026-10-28
reviewed_by: [Andrews Ferreira]
module: M04
---

# Aula 07 — Revisão arquitetural, As-Is/To-Be e validação de controles { #revisao-arquitetural-as-isto-be-e-validacao-de-controles }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 4 · Nível 1</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">75 min · ID técnico: M04-L07</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Uma revisão de arquitetura de segurança não é uma lista de opiniões nem uma auditoria disfarçada. É um processo com escopo, critérios e evidências que termina em **decisão**: aprovar, aprovar com condições ou reprovar — e com o risco residual explícito. Esta aula mostra como estruturar a revisão, como usar **estado atual (As-Is)** e **estado-alvo (To-Be)** para derivar lacunas e uma transição viável, e como **validar** que os controles prometidos existem e funcionam, usando os métodos de avaliação descritos pela NIST SP 800-53A.

**Pré-requisitos:** [De ameaças a requisitos](06-threats-to-requirements.md) e [Architecture Decision Records](../02-security-architecture/08-architecture-decision-records.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Estruturar uma revisão de arquitetura de segurança com escopo, critérios, achados e decisão.
- Representar estado atual e estado-alvo e derivar lacunas e etapas de transição.
- Validar controles com os métodos examinar, entrevistar e testar e escolher o método adequado a cada controle.
- Registrar o resultado da revisão em ADRs e no risk register.

## Conceito

### O que uma revisão produz

| Saída | Conteúdo |
|:---|:---|
| **Escopo** | O que foi revisado e o que ficou de fora |
| **Critérios** | Padrões, arquiteturas de referência, requisitos e nível do ASVS aplicáveis |
| **Achados** | Lacunas com evidência, severidade e cenário de risco relacionado |
| **Decisão** | Aprovado, aprovado com condições (prazo e dono) ou reprovado |
| **Residual** | Riscos que permanecem, com dono |
| **Registros** | ADRs das decisões relevantes; itens no risk register |

O valor do *Threat Modeling Manifesto* — cultura de encontrar e corrigir problemas de design acima de conformidade de checklist — vale também para a revisão: o objetivo é melhorar o desenho, não acumular evidência de que alguém foi avisado.

### As-Is e To-Be

Representar lado a lado o **estado atual** e o **estado-alvo** torna as lacunas visíveis e permite planejar a **transição**, que quase sempre precisa de etapas intermediárias seguras.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m04-l07-as-is.mmd"
```

<figcaption>Figura 1 — As-Is: integração de parceiros da Aurora por SFTP com conta compartilhada, na rede interna plana.</figcaption>
</figure>

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m04-l07-to-be.mmd"
```

<figcaption>Figura 2 — To-Be: identidade por parceiro com mTLS, quarentena e validação, zonas separadas e administração por acesso privilegiado.</figcaption>
</figure>

## Fundamentos técnicos

### Etapas da revisão

1. **Preparar:** receber o DFD, o threat model, os requisitos e o ADR proposto; confirmar escopo e critérios.
2. **Entender:** sessão com a equipe para percorrer o desenho e os fluxos críticos.
3. **Analisar:** comparar com critérios; aplicar os cenários críticos (ATT&CK, abuse cases) e verificar onde o desenho os interrompe.
4. **Validar:** coletar evidências dos controles que já existem ou são herdados.
5. **Decidir:** classificar achados, propor condições e registrar a decisão.
6. **Acompanhar:** verificar as condições no prazo.

### Lacunas e transição

Do confronto As-Is × To-Be saem as lacunas. Na integração da Aurora:

| Lacuna | Risco no As-Is | To-Be | Etapa |
|:---|:---|:---|:---|
| Conta compartilhada | Sem prova de origem; parceiro A envia como B | Identidade por parceiro, mTLS | 1 |
| SFTP exposto com senha | Credencial adivinhável ou vazada dá acesso | Gateway com mTLS e limites | 1 |
| Processamento sem validação | Arquivo adulterado processado | Quarentena e validação de assinatura | 2 |
| Rede plana | Comprometimento do SFTP alcança o banco | Zonas de borda, aplicação e dados | 2 |
| Administração pelo SFTP | Caminho administrativo exposto | Acesso privilegiado com MFA | 1 |
| Sem registro por parceiro | Investigação impossível | Eventos no SIEM | 1 |

A **transição** precisa manter a operação: por exemplo, o gateway pode aceitar SFTP e mTLS em paralelo por 90 dias, com cada parceiro migrado individualmente, e a conta compartilhada desativada ao fim — uma decisão que merece ADR.

### Validar controles: examinar, entrevistar, testar

A SP 800-53A Rev. 5 descreve procedimentos de avaliação de controles executáveis em várias fases do ciclo de vida, e o glossário do NIST define três métodos de avaliação com origem nela:

| Método | Definição (glossário NIST, SP 800-53A Rev. 5) | Exemplo na revisão |
|:---|:---|:---|
| **Examinar** | Verificar, inspecionar, revisar, observar ou estudar objetos de avaliação | Ler a política do gateway; inspecionar a configuração de mTLS |
| **Entrevistar** | Conduzir discussões com pessoas | Perguntar ao operador como um novo parceiro é cadastrado |
| **Testar** | Exercitar objetos de avaliação em condições especificadas | Enviar arquivo com certificado de outro parceiro e verificar a rejeição |

O método define a **força da evidência**. Para controles críticos, **testar** é preferível; examinar configuração mostra que o controle foi configurado, não que funciona; entrevistar mostra o que as pessoas acreditam que acontece.

| Controle | Método mínimo | Por quê |
|:---|:---|:---|
| Rejeição de certificado de outro parceiro | Testar | Falha silenciosa permitiria falsificação |
| Registro de eventos no SIEM | Examinar + testar | Configuração pode existir sem eventos chegando |
| Processo de cadastro de parceiro | Entrevistar + examinar | Controle de processo, com evidência documental |
| Restauração do banco | Testar | Única forma de provar RTO e RPO (Módulo 3 — Aula 05) |

### Classificar achados e decidir

| Severidade | Critério | Efeito na decisão |
|:---|:---|:---|
| **Bloqueante** | Cenário crítico sem interrupção; violação de obrigação legal ou contratual | Reprovado até correção |
| **Condição** | Lacuna relevante com compensação temporária | Aprovado com condição, prazo e dono |
| **Recomendação** | Melhoria sem risco relevante imediato | Registrada, sem bloquear |

## Exemplo empresarial

!!! example "Aurora Pagamentos — revisão da nova integração"

    A revisão da integração To-Be encontrou: um bloqueante (o gateway aceitava certificados de qualquer CA pública, não só os emitidos pela Aurora — descoberto **testando**, não examinando o documento de desenho), duas condições (eventos de rejeição ainda não chegavam ao SIEM; procedimento de revogação de certificado de parceiro não documentado) e três recomendações.

    Depois da correção do bloqueante, a decisão foi **aprovado com condições**, com prazo de 30 dias e dono definido. Dois ADRs foram registrados: a escolha de mTLS com CA própria e o período de convivência de 90 dias com SFTP. O cenário RSK-027 do register teve o residual reduzido de alto para baixo.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Momento | Pouco antes da produção | No desenho, com validação antes da produção |
| Critérios | Experiência do revisor | Padrões, referências e requisitos explícitos |
| Evidência | Documento de desenho | Examinar, entrevistar e, para o crítico, testar |
| Resultado | Lista de comentários | Decisão, condições com prazo e residual com dono |
| Transição | Big bang | Etapas intermediárias seguras, registradas em ADRs |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, muitas validações podem ser automatizadas: testes de política, varreduras de configuração e testes de integração na pipeline produzem evidência contínua. Em on-premises, testes manuais e janelas de manutenção pesam mais no plano de validação. Em ambientes híbridos, a revisão precisa validar o canal entre ambientes nos dois lados — um teste que só verifica o lado cloud não prova que o lado on-premises rejeita o tráfego indevido.

## Como especificar e implementar

- "Revisões de arquitetura de segurança têm escopo, critérios, achados classificados, decisão e residual registrados."
- "Mudanças relevantes apresentam As-Is, To-Be e plano de transição com etapas seguras."
- "Controles críticos são validados por teste; examinar e entrevistar complementam."
- "Decisões relevantes da revisão viram ADRs; riscos residuais entram no register com dono."
- "Condições têm prazo e dono e são verificadas no vencimento."

## Trade-offs, limitações e antipadrões

- **Trade-off:** profundidade versus prazo. Revisões proporcionais ao impacto evitam que a arquitetura vire gargalo.
- **Antipadrão — revisão-carimbo:** aprova tudo com "recomendações" que ninguém acompanha.
- **Antipadrão — revisão-tribunal:** reprova sem oferecer caminho; as equipes passam a evitar a revisão.
- **Limitação:** a revisão avalia o desenho e uma amostra de evidências; não substitui testes de intrusão nem monitoração contínua.

## Como validar

- Acompanhar a taxa de condições cumpridas no prazo.
- Verificar se achados bloqueantes de revisões anteriores reapareceram.
- Comparar incidentes com revisões: o problema teria sido encontrado com os critérios atuais?

## Como apresentar e justificar

- **Para a equipe:** "Encontramos um bloqueante testando, não lendo o documento. Corrigido, vocês seguem com duas condições de 30 dias."
- **Para gestores:** "A nova integração reduz o risco de fraude por parceiro de alto para baixo; a migração dos 12 parceiros leva 90 dias, sem parar a operação."

## Checklist de revisão arquitetural

- [ ] Escopo e critérios estão explícitos.
- [ ] As-Is e To-Be foram representados; as lacunas estão listadas.
- [ ] A transição tem etapas seguras e prazos.
- [ ] Controles críticos foram testados.
- [ ] Achados têm severidade, evidência e cenário de risco.
- [ ] A decisão, as condições e o residual estão registrados em ADR e no register.

## Questões de compreensão

**1.** Por que examinar a configuração não basta para controles críticos?

??? success "Resposta comentada"

    Porque mostra que o controle foi configurado, não que funciona no contexto real. Erros de escopo, exceções esquecidas e dependências só aparecem quando o controle é exercitado — por isso, para controles críticos, o método preferível é testar.

**2.** Para que serve representar As-Is e To-Be lado a lado?

??? success "Resposta comentada"

    Para tornar as lacunas explícitas, ligá-las a riscos e planejar uma transição com etapas intermediárias seguras, em vez de uma mudança única e arriscada.

**3.** O que diferencia "aprovado com condições" de "aprovado com recomendações"?

??? success "Resposta comentada"

    Condições são obrigatórias, têm prazo e dono e são verificadas; se não forem cumpridas, a decisão é revista. Recomendações são melhorias desejáveis que não bloqueiam a decisão.

## Exercício de tomada de decisão

!!! question "Cenário: estratégia de transição da integração da Aurora"

    Para migrar os 12 parceiros do SFTP com conta compartilhada para o gateway com mTLS, a Aurora considera: (A) corte único em uma data, com todos os parceiros migrando juntos; (B) convivência por 90 dias, migrando parceiro a parceiro, com a conta compartilhada desativada ao fim; (C) manter o SFTP indefinidamente para parceiros que não conseguirem migrar, com controles compensatórios. Compare as opções com uma matriz ponderada — redução do risco ao fim da transição (peso 3), risco operacional durante a transição (3), esforço de operação (2) e prazo até o estado-alvo (1); notas de 1 a 3, 3 = melhor desempenho no critério, e no risco operacional e no esforço 3 significa o menor risco e o menor esforço — e recomende.

??? success "Resolução de referência"

    | Critério | Peso | A — Corte único | B — Convivência de 90 dias | C — SFTP indefinido |
    |:---|:---|:---|:---|:---|
    | Redução do risco ao fim da transição | 3 | 3 | 3 | 1 |
    | Risco operacional durante a transição (3 = menor) | 3 | 1 | 3 | 3 |
    | Esforço de operação (3 = menor) | 2 | 3 | 2 | 1 |
    | Prazo até o estado-alvo | 1 | 3 | 2 | 1 |
    | **Total ponderado** | | **21** | **24** | **15** |

    **Pesos:** o risco ao fim da transição e o risco operacional durante ela recebem 3 — a Aurora não pode trocar o risco de fraude pelo de parar a liquidação; o esforço recebe 2 porque a equipe de integração é pequena; o prazo recebe 1 porque a diferença entre A e B é de semanas.

    **Recomendação: B.** Atinge o mesmo estado-alvo de A sem o risco de parar a liquidação caso parceiros falhem na data única. C nunca elimina a conta compartilhada e perpetua o risco.

    **Condições:** durante a convivência, o SFTP fica restrito por origem aos parceiros ainda não migrados, com alertas de uso; a data de desativação é registrada em ADR; parceiros que não migrarem dependem de decisão formal do dono do risco.

    **Risco residual:** durante os 90 dias, a conta compartilhada continua existindo para os parceiros não migrados. **O que mudaria a decisão:** um incidente ativo envolvendo a conta compartilhada justificaria o corte único (A), aceitando a parada de parceiros atrasados; um parceiro estratégico sem capacidade técnica para mTLS exigiria uma exceção formal, e não a opção C para todos.

## Pontos-chave

- A revisão termina em decisão, condições com prazo e residual com dono.
- As-Is e To-Be tornam lacunas explícitas e permitem uma transição em etapas seguras.
- Examinar, entrevistar e testar têm forças de evidência diferentes; teste o que é crítico.
- Achados bloqueantes, condições e recomendações têm efeitos distintos na decisão.
- Registre as decisões em ADRs e os residuais no risk register.

<!-- next-steps:start -->

!!! tip "Próximos passos"

    Você concluiu a última aula do **Módulo 4** — [voltar ao módulo](index.md).

    Atividades integradoras:

    - [Avaliação integradora do Nível 1](../../assessments/level-1-integrative.md)

<!-- next-steps:end -->

## Referências

### Fundamentação principal

- NIST. *SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations*. 2022. <https://csrc.nist.gov/pubs/sp/800/53/a/r5/final> — página oficial e definições de *examine*, *interview* e *test* no glossário do CSRC. *(Conferidos.)*
- *Threat Modeling Manifesto* — valores e a pergunta "fizemos um bom trabalho?".
- NIST. *SP 800-37 Rev. 2* — etapas Assess e Authorize (Módulo 3 — Aula 02).

### Leitura complementar

- M. Nygard. *Documenting Architecture Decisions*. 2011 — formato de ADR (Módulo 2 — Aula 08).
- NIST. *SP 800-160 Vol. 1 Rev. 1* — determinação de segurança adequada baseada em evidências.
- OWASP. *ASVS 5.0* — critérios verificáveis para revisões de aplicações.

### Aplicação prática

- Use o [checklist de revisão de arquitetura](../../artifacts/architecture-review-checklist.md) do portal em uma solução real, representando As-Is e To-Be e indicando o método de validação de cada controle crítico.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-28 |
| Última atualização | 2026-10-28 |
