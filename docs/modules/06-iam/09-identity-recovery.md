---
id: M06-L09
title: "Aula 09 — Recuperação de identidade em incidentes"
public_title: "Módulo 6 — Aula 09 — Recuperação de identidade em incidentes"
description: Como recuperar o plano de controle quando a identidade é comprometida — preparação, contas de emergência, contenção na nuvem, decisão entre limpar e recuperar a floresta do Active Directory, recuperação isolada, rotação de credenciais e reentrada controlada.
domain: iam
tier: architect
status: published
prerequisites: [M06-L03, M06-L05, M06-L06, M03-L05]
objectives:
  - Explicar por que a recuperação de identidade precede a recuperação de qualquer outro sistema.
  - Projetar a preparação — backups, contas de emergência, canais fora de banda e ambiente isolado.
  - Conduzir a decisão entre limpar o diretório e recuperar a floresta.
  - Sequenciar a contenção, a recuperação, a rotação de credenciais e a reentrada.
minutes: 75
sources: [MS-AD-FOREST-RECOVERY, MS-ENTRA-HYBRID-AUTHN, MS-ENTERPRISE-ACCESS-MODEL, NIST-SP800-34-R1, NIST-SP800-53, CIS-CONTROLS-V8-1]
further_reading: [MITRE-ATTACK, BOOK-GOOGLE-BSRS, AWS-DR-WHITEPAPER]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M06
---

# Aula 09 — Recuperação de identidade em incidentes { #recuperacao-de-identidade-em-incidentes }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 6 · Nível 2</span>
<span class="saa-tier saa-tier--architect">Architect</span>
<span class="saa-meta">75 min · ID técnico: M06-L09</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Em um ataque que comprometeu o diretório, nenhum sistema pode ser restaurado com confiança antes da identidade: servidores restaurados voltam a confiar no mesmo domínio, credenciais roubadas continuam válidas e o atacante retorna. A **recuperação de identidade** é, por isso, a primeira dependência de qualquer plano de recuperação de ransomware (Módulo 3 — Aula 05). Esta aula trata da preparação que torna a recuperação possível e da sequência que impede a reentrada do atacante.

**Pré-requisitos:** [AD, LDAP e Kerberos](03-directories-kerberos.md), [Identidade híbrida](05-hybrid-identity.md), [Contas privilegiadas](06-privileged-machine-identities.md) e [BIA, RTO e RPO](../03-governance-risk/05-bia-rto-rpo.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Explicar por que a recuperação de identidade precede a recuperação de qualquer outro sistema.
- Projetar a preparação — backups, contas de emergência, canais fora de banda e ambiente isolado.
- Conduzir a decisão entre limpar o diretório e recuperar a floresta.
- Sequenciar a contenção, a recuperação, a rotação de credenciais e a reentrada.

## Conceito

### Por que identidade primeiro

| Se a identidade não for recuperada antes | Consequência |
|:---|:---|
| Restaurar servidores de aplicação | Voltam a confiar no domínio comprometido |
| Restaurar backups de dados | O atacante, com credenciais válidas, cifra de novo |
| Reabrir o acesso remoto | Contas comprometidas voltam a entrar |
| Reconectar a sincronização com a nuvem | Alterações maliciosas propagam para a nuvem |

Na análise de dependências (Módulo 4 — Aula 05), identidade, DNS e chaves aparecem como dependências de quase todos os processos críticos. Na recuperação, essa dependência define a **ordem**.

### Recuperação de floresta como última opção { #recuperacao-de-floresta-como-ultimo-recurso }

O *Active Directory Forest Recovery Guide* da Microsoft trata da recuperação quando uma falha de toda a floresta deixa todos os controladores de domínio incapazes de funcionar normalmente. Ao identificar o problema, o guia pede avaliar as alternativas com as partes interessadas e registra que, em muitos casos, a recuperação total da floresta deve ser a **última opção**. O processo tem cinco etapas:

1. **Identificar o problema** — escopo e causas, avaliando as alternativas com as partes interessadas.
2. **Determinar como recuperar** — e executar os passos preliminares.
3. **Recuperação inicial, em isolamento** — recuperar um DC por domínio, limpá-lo e reconectar os domínios; **redefinir contas privilegiadas** e corrigir problemas causados por violações de segurança.
4. **Reimplantar os demais DCs**.
5. **Limpeza** — resolução de nomes e retorno das aplicações de negócio.

O guia declara que os passos foram desenhados para minimizar a chance de reintroduzir dados perigosos na floresta recuperada. Entre os procedimentos, estão a redefinição da senha da conta **krbtgt**, das senhas de relações de confiança e da senha da conta de computador dos DCs. A krbtgt guarda as duas senhas mais recentes, por isso o guia manda redefini-la **duas vezes**, com intervalo de pelo menos 10 horas — o tempo de vida máximo padrão dos tíquetes, ou mais, se a política tiver sido alterada — para que nenhum DC continue usando a senha antiga.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m06-l09-recovery.mmd"
```

<figcaption>Figura 1 — Sequência de recuperação: canais e contas de emergência, contenção na nuvem, decisão entre limpar e recuperar, recuperação isolada, validação, restabelecimento da sincronização e monitoração na reentrada.</figcaption>
</figure>

## Fundamentos técnicos

### Preparação

| Preparação | Por quê |
|:---|:---|
| **Backups do diretório** fora do alcance das credenciais do domínio, com retenção que cubra o tempo de permanência típico de um atacante | Recuperar de um ponto anterior ao comprometimento (Módulo 3 — Aula 05, Módulo 4 — Aula 05) |
| **Ambiente de recuperação isolado** (rede, hipervisor, estações) | O guia prevê a recuperação inicial em isolamento |
| **Contas de emergência** no IdP em nuvem, fora do AD | Administrar a nuvem quando o domínio não é confiável (Aula 05, Aula 06) |
| **Canal de comunicação fora de banda** | O e-mail e o chat corporativos podem estar comprometidos ou indisponíveis |
| **PHS habilitado** | Manter o acesso a SaaS e nuvem com o datacenter fora do ar, como recomenda a documentação da Microsoft (Aula 05) |
| **Inventário de credenciais** a rotacionar — contas privilegiadas, contas de serviço, segredos de aplicações, chaves de federação | Saber o que trocar e em que ordem |
| **Runbook ensaiado** com tempos medidos | Transformar o RTO declarado em RTO demonstrado |

O NIST SP 800-34 Rev. 1 lembra que planos sem testes, treinamento e manutenção — as etapas 6 e 7 do planejamento de contingência — não sustentam os objetivos declarados.

### Limpar ou recuperar?

| Situação | Tendência |
|:---|:---|
| Comprometimento limitado, com escopo conhecido e confiável | Limpeza: remover persistência, redefinir contas, rotacionar credenciais |
| Persistência de escopo que a investigação não consegue delimitar, alterações em objetos críticos do diretório que não possam ser verificadas, perda de confiança nos DCs | Recuperação de floresta a partir de backup anterior ao comprometimento |
| DCs cifrados ou destruídos | Recuperação de floresta |

A decisão é de negócio e técnica ao mesmo tempo, e deve ser tomada com evidências da investigação — não com pressa.

### Contenção na nuvem

Enquanto o diretório local é tratado, a nuvem precisa ser protegida da propagação:

- **Revogar sessões e tokens** de contas afetadas e privilegiadas.
- **Suspender a sincronização** até que o diretório recuperado seja validado.
- Verificar **alterações recentes** em papéis, aplicações registradas, credenciais de aplicações e configurações de federação.
- Usar **contas de emergência somente em nuvem** para administrar o IdP durante o incidente.

### Rotação de credenciais e reentrada

| Ordem | O que rotacionar | Observação |
|:---|:---|:---|
| 1 | Contas privilegiadas do diretório e do IdP | Inclui a conta krbtgt (duas redefinições, com intervalo de ao menos 10 horas), as senhas de relações de confiança e as contas de computador dos DCs, conforme os procedimentos do guia de recuperação |
| 2 | Contas de serviço e segredos usados por sistemas críticos | Coordenar com donos para evitar indisponibilidade |
| 3 | Credenciais de aplicações registradas e de federação | Inclui chaves de assinatura de tokens |
| 4 | Senhas de usuários | Com MFA resistente a phishing na reentrada, quando possível |

A reentrada é monitorada de perto: novos logins privilegiados, alterações em grupos e uso de credenciais antigas devem gerar alertas.

## Exemplo empresarial

!!! example "Meridiana — exercício de recuperação de identidade"

    A Meridiana conduziu um exercício de mesa com o cenário "domínio comprometido e DCs cifrados". O exercício revelou que:

    - O único backup do AD estava em um servidor do próprio domínio.
    - O plano de comunicação dependia do e-mail corporativo.
    - Ninguém sabia quais contas de serviço precisariam ser rotacionadas.
    - A autenticação de passagem tornaria o e-mail em nuvem inacessível.

    As correções viraram requisitos: backup do diretório no cofre isolado (Módulo 4 — Aula 05), grupo de mensagens fora de banda para o comitê de crise, inventário de contas de serviço com dono (Aula 06) e PHS habilitado (Aula 05). No exercício seguinte, em ambiente isolado, a recuperação de um DC por domínio levou 5 horas — compatível com o RTO de 8 horas da expedição, considerando as demais dependências.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Ordem de recuperação | Aplicações primeiro | Identidade primeiro |
| Backup do diretório | No próprio domínio | Isolado, fora do alcance das credenciais do domínio |
| Comunicação | Canais corporativos | Canal fora de banda definido |
| Nuvem durante o incidente | Sincronização ativa | Sincronização suspensa; contas de emergência em nuvem |
| Credenciais | Trocar "as principais" | Inventário e ordem de rotação definidos |
| Ensaio | Nunca | Exercícios periódicos com tempos medidos |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias para a preparação e a recuperação:

| Controle ou padrão | Objetivo na recuperação de identidade | Referência |
|:---|:---|:---|
| Plano de contingência | Plano com funções essenciais, objetivos de recuperação e prioridades — identidade primeiro | SP 800-53: CP-2 (Contingency Plan) |
| Teste do plano | Testar o plano para medir eficácia e prontidão, com ações corretivas | SP 800-53: CP-4 (Contingency Plan Testing) |
| Backup do diretório | Backup testado quanto à confiabilidade e à integridade, guardado fora do local do sistema em produção | SP 800-53: CP-9 (System Backup), CP-9(1) e CP-9(3) |
| Recuperação a estado conhecido | Recuperar e reconstituir o sistema a um estado conhecido após interrupção, comprometimento ou falha | SP 800-53: CP-10 (System Recovery and Reconstitution) |
| Tratamento de incidentes | Preparação, detecção e análise, contenção, erradicação e recuperação, coordenadas com o plano de contingência | SP 800-53: IR-4 (Incident Handling) |
| Rotação de credenciais | Trocar autenticadores comprometidos ou suspeitos | SP 800-53: IA-5 (Authenticator Management) |
| Recuperação de dados e resposta a incidentes | Processo de recuperação de dados e gestão de resposta a incidentes | CIS v8.1: Controles 11 (Data Recovery) e 17 (Incident Response Management) |

## Aplicabilidade: on-premises, cloud e híbrido

Em ambientes só em nuvem, a recuperação foca no IdP: contas de emergência, revisão de papéis, aplicações registradas e credenciais. Em on-premises, a recuperação de floresta domina. Em ambientes híbridos — o caso mais comum —, as duas frentes correm em paralelo, e a sincronização entre elas é o ponto que precisa ser controlado para evitar recontaminação.

## Como especificar e implementar

- "O plano de recuperação de desastres recupera a identidade antes de qualquer outro sistema."
- "Backups do diretório são mantidos fora do alcance das credenciais do domínio, com retenção definida."
- "Há ambiente de recuperação isolado e canal de comunicação fora de banda."
- "O inventário de credenciais a rotacionar está atualizado, com ordem e donos."
- "A recuperação de identidade é ensaiada ao menos uma vez por ano, com tempos medidos."

## Trade-offs, limitações e antipadrões

- **Trade-off:** retenção longa de backups do diretório aumenta a chance de ter um ponto limpo, mas também o custo e a complexidade de validar de qual ponto recuperar.
- **Antipadrão — restaurar tudo de uma vez:** reintroduz a persistência do atacante.
- **Antipadrão — plano que depende do sistema comprometido:** runbook guardado no compartilhamento de arquivos cifrado.
- **Limitação:** esta aula descreve a arquitetura e a sequência; os procedimentos detalhados de recuperação de floresta estão no guia da Microsoft e devem ser seguidos e adaptados.

## Como validar

- Restaurar um DC a partir do backup em ambiente isolado e medir o tempo.
- Verificar se contas de emergência da nuvem funcionam sem o AD.
- Conferir se o canal fora de banda alcança todos os membros do comitê de crise.
- Simular a suspensão da sincronização e o impacto nos SaaS.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Um DC por domínio restaurado em ambiente isolado dentro do tempo-alvo | Registro do exercício com tempos medidos |
| Backup do diretório inacessível às credenciais do domínio | Teste de acesso ao repositório de backup com conta administrativa do domínio, negado |
| Contas de emergência da nuvem funcionam sem o AD | Registro do teste com o AD desconectado |
| Canal fora de banda alcança todo o comitê de crise | Registro da última convocação de teste |
| Inventário de credenciais a rotacionar com ordem e donos | Inventário revisado no último ciclo |

## Como apresentar e justificar

- **Para a diretoria:** "Em um ransomware, nada volta antes da identidade. O exercício mostrou que hoje não conseguiríamos recuperá-la. Com estas quatro medidas, recuperamos em cinco horas."
- **Para a equipe técnica:** "A recuperação inicial é feita em rede isolada, com um DC por domínio, e as contas privilegiadas são redefinidas antes de qualquer reconexão."

## Checklist de revisão arquitetural

- [ ] Identidade é a primeira etapa do plano de recuperação.
- [ ] Backups do diretório isolados e testados.
- [ ] Ambiente de recuperação isolado disponível.
- [ ] Contas de emergência em nuvem e canal fora de banda definidos.
- [ ] Inventário e ordem de rotação de credenciais.
- [ ] Exercício anual com tempos medidos.

## Questões de compreensão

**1.** Por que restaurar servidores de aplicação antes da identidade é arriscado?

??? success "Resposta comentada"

    Porque os servidores voltam a confiar no domínio comprometido e as credenciais roubadas continuam válidas; o atacante pode retornar e repetir o ataque.

**2.** Quais são as cinco etapas de recuperação de floresta descritas pelo guia da Microsoft?

??? success "Resposta comentada"

    Identificar o problema; determinar como recuperar; recuperação inicial em isolamento (um DC por domínio, limpeza, redefinição de contas privilegiadas); reimplantar os demais DCs; e limpeza final.

**3.** Por que suspender a sincronização com a nuvem durante o incidente?

??? success "Resposta comentada"

    Para impedir que alterações maliciosas no diretório local — contas criadas, grupos alterados — propaguem para a nuvem, e para que a sincronização só seja retomada a partir de um diretório validado.

## Exercício de tomada de decisão

!!! question "Cenário: limpar ou recuperar na Aurora"

    A investigação de um incidente na Aurora encontrou: uma conta administrativa do domínio criada há 40 dias pelo atacante, alterações em políticas de grupo e indícios de uso da chave de assinatura do servidor de federação. Os DCs estão funcionando. As opções em discussão são:

    - **A** — o que a equipe de infraestrutura propõe: remover a conta e trocar senhas;
    - **B** — recuperação de floresta a partir de backup anterior aos 40 dias, em ambiente isolado, com contenção na nuvem;
    - **C** — erradicação ampla no lugar, guiada pela investigação: redefinição das contas privilegiadas, da krbtgt (duas vezes), das relações de confiança e das contas de serviço; revisão de todas as políticas de grupo e delegações alteradas; contenção na nuvem; e preparação de B em paralelo.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e recomende uma.

**Objetivos avaliados:** Conduzir a decisão entre limpar o diretório e recuperar a floresta; sequenciar a contenção, a recuperação, a rotação de credenciais e a reentrada.

**Entrega esperada:** Matriz ponderada, recomendação com gatilhos que levariam à recuperação da floresta e a sequência de contenção na nuvem.

**Critérios de avaliação:**

- A resposta avalia a perda de confiança no plano de controle híbrido, incluindo a chave de federação.
- Os gatilhos para mudar de estratégia são explícitos e verificáveis.
- A sequência inclui rotação do certificado de assinatura de tokens e administração por contas de emergência em nuvem.

??? success "Resolução de referência"

    | Critério | Peso | A — Remover a conta e trocar senhas | B — Recuperação de floresta | C — Erradicação ampla com B preparado |
    |:---|:---|:---|:---|:---|
    | Confiança na eliminação da persistência | 3 | 1 | 3 | 2 |
    | Indisponibilidade adicional | 2 | 3 | 1 | 2 |
    | Contenção do plano de controle híbrido (nuvem e federação) | 2 | 1 | 3 | 3 |
    | Preservação das mudanças legítimas dos últimos 40 dias | 1 | 3 | 1 | 3 |
    | **Total ponderado** | | **14** | **18** | **19** |

    - **Avaliação:** persistência de 40 dias, alteração de políticas de grupo e possível comprometimento da chave de federação indicam **perda de confiança no plano de controle híbrido**. Remover uma conta não garante a eliminação de outras formas de persistência — A está descartada. As políticas de grupo alteradas são verificáveis: podem ser comparadas, uma a uma, com o backup anterior aos 40 dias e com o histórico de versões — por isso, sozinhas, não exigem a recuperação da floresta.
    - **Pesos:** eliminar a persistência é o objetivo (peso 3). Indisponibilidade e contenção da nuvem pesam 2: a Aurora precisa voltar a operar, e a chave de federação ameaça a nuvem independentemente do que se faça no AD. Preservar as mudanças dos últimos 40 dias pesa 1, porque podem ser refeitas.
    - **Recomendação: C**, com B preparada em paralelo. Os DCs funcionam, e o guia da Microsoft trata a recuperação total da floresta como última opção em muitos casos; a erradicação ampla, com a investigação delimitando o que foi alterado, resolve o problema com menos indisponibilidade. Na nuvem, de imediato: revogar sessões; suspender a sincronização; **rotacionar o certificado de assinatura de tokens** e atualizar a relação de confiança no IdP, para que tokens forjados com a chave antiga sejam rejeitados; monitorar a emissão de tokens; administrar pelas contas de emergência somente em nuvem; revisar aplicações registradas e papéis. A migração para PHS (Aula 05) fica para depois da validação do diretório: a Aurora não tinha PHS habilitado, e com a sincronização suspensa não haveria hashes válidos para usar. B fica pronta — backup anterior aos 40 dias validado e ambiente isolado preparado — para ser acionada se um gatilho ocorrer.
    - **Trade-off aceito e risco residual:** a confiança de C depende da completude da investigação; persistência não encontrada (outra conta, delegação ou alteração em objeto protegido) sobreviveria. O residual é tratado com monitoração intensiva na reentrada e com os gatilhos abaixo.
    - **O que mudaria a decisão:** a investigação não conseguir delimitar o comprometimento, encontrar alterações em objetos críticos que não possam ser verificadas (esquema, permissões de objetos protegidos, relações de confiança) ou nova atividade do atacante depois da erradicação — qualquer um desses gatilhos leva a B, como prevê a tabela "Limpar ou recuperar?"; se os DCs forem cifrados ou destruídos, B é a única opção.
    - **Decisão do negócio:** apresentar ao comitê de crise o trade-off entre a indisponibilidade adicional da recuperação e o risco de recontaminação, com a recomendação e os gatilhos registrados.
    - **Depois:** rotação de credenciais na ordem definida, reentrada monitorada e lições aprendidas incorporadas ao plano.

    **Erros comuns:**

    - Remover a conta do atacante e considerar o incidente encerrado.
    - Esquecer a krbtgt (duas redefinições) e as contas de serviço.
    - Tratar a nuvem como fora do escopo enquanto a chave de federação pode ter sido usada.

## Pontos-chave

- Identidade é a primeira dependência da recuperação; nada é restaurado com confiança antes dela.
- A recuperação de floresta é, em muitos casos, a última opção; quando necessária, é feita em isolamento, com redefinição de contas privilegiadas e duas redefinições da krbtgt.
- Preparação decide o resultado: backups isolados, ambiente isolado, contas de emergência, canal fora de banda.
- Contenha a nuvem durante o incidente: sessões, sincronização, federação.
- Rotacione credenciais em ordem definida e monitore a reentrada.

<!-- next-steps:start -->

!!! tip "Próximos passos"

    Você concluiu a última aula do **Módulo 6** — [voltar ao módulo](index.md).

    Em seguida: [Módulo 7 — Zero Trust Architecture](../../modules/07-zero-trust/index.md).

<!-- next-steps:end -->

## Referências

### Fundamentação principal

- Microsoft. *Active Directory Forest Recovery Guide*, *Steps for restoring the forest* e *Procedures*. Microsoft Learn. <https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-guide>. *(Página de entrada, etapas e lista de procedimentos lidas; procedimentos detalhados não lidos.)*
- Microsoft. *Authentication for Microsoft Entra hybrid identity solutions* — PHS como contingência. *(Lido.)*
- Microsoft. *The enterprise access model* — contas de emergência. *(Lido.)*
- NIST. *SP 800-34 Rev. 1* — Cap. 3, testes e manutenção do plano. *(Lido.)*
- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — controles CP-2, CP-4, CP-9, CP-9(1), CP-9(3), CP-10, IA-5 e IR-4, conferidos no catálogo OSCAL oficial — gratuito.
- CIS. *CIS Critical Security Controls v8.1* — Controles 11 e 17 — gratuito.

### Leitura complementar

- MITRE. *ATT&CK v20* — T1558 e T1078, persistência por credenciais.
- H. Adkins et al. *Building Secure and Reliable Systems* — Cap. 9, *Design for Recovery*, e Cap. 18, *Recovery and Aftermath*.
- AWS. *Disaster Recovery of Workloads on AWS* — cópias pontuais e corrupção de dados.

### Aplicação prática

- Escreva o primeiro rascunho do runbook de recuperação de identidade da sua organização: onde estão os backups do diretório, quem decide entre limpar e recuperar, qual o canal fora de banda e quais credenciais serão rotacionadas, em que ordem.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
