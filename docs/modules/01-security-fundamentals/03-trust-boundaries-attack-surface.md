---
id: M01-L03
title: "Trust boundaries, attack surface e responsabilidade compartilhada"
description: Onde a confiança muda dentro de um sistema, como mapear os pontos de entrada que formam a superfície de ataque e como a responsabilidade compartilhada com provedores e parceiros cria fronteiras organizacionais.
domain: security-foundations
tier: fundamental
status: published
prerequisites: [M01-L02, M00-L07]
objectives:
  - Definir trust boundary e identificar fronteiras técnicas e organizacionais em um diagrama.
  - Mapear a superfície de ataque de um sistema a partir de seus pontos de entrada.
  - Priorizar pontos de entrada por privilégio, exposição e dados alcançáveis.
  - Explicar como a responsabilidade compartilhada com provedores e parceiros altera as fronteiras.
minutes: 60
sources: [BOOK-ANDERSON-SE3, NIST-SP800-160-V1R1, NIST-SP800-145]
further_reading: [NIST-SP800-207, AWS-SECURITY-PILLAR]
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
module: M01
---

# Trust boundaries, attack surface e responsabilidade compartilhada

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Nível 0 · M01-L03</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Ataques acontecem nas **costuras** de um sistema: onde dados vindos de fora entram, onde um componente passa a confiar em outro, onde a responsabilidade passa de uma equipe — ou de uma empresa — para outra. Esta aula ensina a encontrar essas costuras: as **trust boundaries**, a **superfície de ataque** formada pelos pontos de entrada e as fronteiras organizacionais criadas pela responsabilidade compartilhada com provedores e parceiros.

**Pré-requisitos:** [Princípios de design seguro](02-secure-design-principles.md) e [Lendo diagramas arquiteturais](../00-foundations/07-reading-architecture-diagrams.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Definir trust boundary e identificar fronteiras técnicas e organizacionais em um diagrama.
- Mapear a superfície de ataque de um sistema a partir de seus pontos de entrada.
- Priorizar pontos de entrada por privilégio, exposição e dados alcançáveis.
- Explicar como a responsabilidade compartilhada com provedores e parceiros altera as fronteiras.

## Conceito

### Trust boundary

Uma **trust boundary** (fronteira de confiança) é um ponto em que o nível de confiança muda: de um lado, dados ou entidades em que o sistema confia mais; do outro, menos. Exemplos:

- entre a internet e a DMZ;
- entre o navegador do usuário e o servidor;
- entre um serviço e o banco de dados;
- entre o kernel e um processo de usuário;
- entre a sua organização e um fornecedor SaaS.

**Todo dado que atravessa uma fronteira no sentido de maior confiança precisa ser verificado**: autenticado, autorizado e validado. Esse é o sentido prático do conceito — ele diz *onde* aplicar controles.

Anderson lembra que fronteiras não são só técnicas: muitas dependem de governança, incentivos e regulação (*Security Engineering*, Cap. 10). Uma fronteira entre duas empresas, por exemplo, só existe de fato se o contrato e a operação a sustentarem.

### Attack surface

A **superfície de ataque** é o conjunto de pontos pelos quais um atacante pode interagir com o sistema: interfaces de usuário, APIs, portas de rede, integrações, canais administrativos, filas, arquivos importados, dependências de software. Reduzir a superfície de ataque — remover o que não é necessário — é frequentemente o controle mais barato e mais eficaz.

Superfície de ataque não é só "o que está na internet". Um painel administrativo interno, alcançável por qualquer estação, é parte da superfície para um atacante que já comprometeu uma estação por phishing.

### Confiança versus confiabilidade

O Capítulo 2 da SP 800-160 Vol. 1 Rev. 1 distingue **confiança** — a crença de que uma entidade atenderá a certas expectativas, que pode ser depositada até em quem não a merece — de **confiabilidade** (*trustworthiness*) — a capacidade, demonstrada por evidência, de merecer essa confiança. Toda trust boundary embute uma decisão de confiança; a arquitetura deve garantir que ela seja depositada em componentes cuja confiabilidade foi demonstrada.

## Fundamentos técnicos

### Mapeando a superfície de ataque

Um método simples, a partir do diagrama:

1. **Liste os pontos de entrada** — todo lugar em que dados ou comandos entram no sistema.
2. **Para cada um, registre:** quem pode alcançá-lo (exposição), que identidade é exigida, que privilégio o ponto de entrada tem e que dados ele alcança.
3. **Identifique as fronteiras atravessadas.**
4. **Priorize** pelos três fatores: exposição, privilégio e dados alcançáveis.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m01-l03-attack-surface.mmd"
```

<figcaption>Figura 1 — Superfície de ataque e fronteiras de confiança de uma aplicação de agendamento.</figcaption>
</figure>

Aplicando o método à figura:

| Entrada | Exposição | Identidade | Privilégio | Dados alcançáveis | Prioridade |
|:---|:---|:---|:---|:---|:---|
| 1 Site | Internet | Paciente | Baixo | Agenda própria | Média |
| 2 API móvel | Internet | Paciente (token) | Baixo | Agenda própria | Média |
| 3 Painel administrativo | Rede interna | Funcionário + MFA | Alto | Todos os pacientes | **Alta** |
| 4 Integração com laboratório | Parceiro | Certificado mTLS | Médio | Resultados de exames | **Alta** |
| 5 Acesso administrativo | Zona de gestão | Administrador | Total | Tudo | **Alta** |

O resultado contraria a intuição de que "o que está na internet é o mais crítico": os pontos de entrada de **maior privilégio** merecem mais atenção, mesmo que sejam internos.

### Responsabilidade compartilhada como fronteira organizacional

Quando parte do sistema é operada por terceiros — um provedor de cloud, um SaaS, um parceiro de integração —, surge uma fronteira **organizacional**. Ela tem três características:

- **Visibilidade limitada:** você não vê os controles do outro lado; depende de contratos, relatórios e certificações.
- **Responsabilidades divididas:** no modelo de cloud, o provedor responde pela infraestrutura e o cliente pelo que configura (M00-L06, com base no NIST SP 800-145).
- **Lacunas na divisa:** os incidentes costumam ocorrer onde "cada lado achava que era do outro" — logs que ninguém coleta, contas de integração que ninguém revisa.

## Exemplo empresarial

!!! example "Lumen Saúde — a integração esquecida"

    Ao mapear a superfície de ataque do agendamento, a equipe da Lumen listou o site e a API móvel e concentrou os testes neles. A integração com o laboratório parceiro ficou fora, "porque é de um parceiro confiável".

    Na revisão, o arquiteto mostrou que a integração era o ponto de entrada de maior risco depois do painel administrativo: alcançava resultados de exames de todos os pacientes e usava uma chave de API estática, compartilhada por todos os funcionários técnicos do laboratório.

    Foram definidos: autenticação por mTLS com certificado do laboratório; autorização restrita aos exames solicitados por aquele laboratório; e cláusula contratual exigindo notificação de incidentes em 24 horas. A fronteira técnica (mTLS e autorização) e a organizacional (contrato) foram tratadas juntas.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Fronteiras | Só a borda da internet é considerada | Toda mudança de confiança é uma fronteira, inclusive internas e organizacionais |
| Superfície de ataque | Foco no que é público | Inventário de todos os pontos de entrada, priorizados por privilégio e dados |
| Parceiros | "Confiáveis" por padrão | Autenticados, autorizados e com obrigações contratuais |
| Redução | Proteger tudo o que existe | Remover pontos de entrada desnecessários primeiro |

## Aplicabilidade: on-premises, cloud e híbrido

| Ambiente | Fronteiras típicas |
|:---|:---|
| **On-premises** | Zonas de rede, DMZ, rede de gestão. |
| **Cloud** | Contas, projetos e assinaturas; o plano de controle do provedor (o console e as APIs de gestão) é um ponto de entrada de privilégio máximo. |
| **Híbrido** | A conexão entre ambientes e as identidades sincronizadas são fronteiras críticas: um comprometimento no datacenter pode alcançar a cloud pela federação de identidade, e vice-versa. |

## Como especificar e implementar

- "Toda solução documenta seus pontos de entrada, com exposição, identidade exigida, privilégio e dados alcançáveis."
- "Todo dado que atravessa uma fronteira no sentido de maior confiança é autenticado, autorizado e validado."
- "Integrações com terceiros usam credenciais exclusivas por parceiro, com escopo mínimo e obrigações contratuais de segurança."

## Trade-offs, limitações e antipadrões

- **Antipadrão — confiança por localização:** confiar em um componente porque está na rede interna.
- **Antipadrão — parceiro confiável sem controle técnico.**
- **Limitação:** a superfície de ataque muda a cada implantação; o mapeamento precisa ser atualizado ou, melhor, gerado a partir do inventário.

## Como validar

- Comparar a lista de pontos de entrada documentada com o que realmente responde na rede e nas APIs.
- Para cada fronteira, verificar se há autenticação, autorização e validação.
- Revisar credenciais de integração: são exclusivas, com escopo mínimo e com rotação?

## Como apresentar e justificar

- **Para engenharia:** "A integração com o laboratório é o segundo ponto de entrada mais privilegiado; vamos trocar a chave estática por mTLS e restringir o escopo."
- **Para gestores:** "Um parceiro com uma senha compartilhada tem acesso aos exames de todos os nossos pacientes. Vamos limitar esse acesso ao necessário e formalizar as obrigações do parceiro."

## Checklist de revisão arquitetural

- [ ] As trust boundaries, inclusive organizacionais, estão marcadas no diagrama.
- [ ] Todos os pontos de entrada estão listados, com exposição, identidade, privilégio e dados.
- [ ] Pontos de entrada desnecessários foram removidos.
- [ ] Fluxos que atravessam fronteiras são autenticados, autorizados e validados.
- [ ] Integrações com terceiros têm credenciais exclusivas e obrigações contratuais.

## Questões de compreensão

**1.** Por que o painel administrativo interno pode ser mais prioritário que o site público?

??? success "Resposta comentada"

    Porque a prioridade depende também do privilégio e dos dados alcançáveis. O painel dá acesso a todos os pacientes; um atacante que já comprometeu uma estação interna (por phishing, por exemplo) pode alcançá-lo.

**2.** Qual a diferença entre confiança e confiabilidade?

??? success "Resposta comentada"

    Confiança é a crença de que uma entidade atenderá às expectativas e pode ser depositada até em quem não a merece. Confiabilidade é a capacidade dessa entidade de merecer a confiança, demonstrada por evidência.

**3.** Dê um exemplo de lacuna típica na fronteira de responsabilidade compartilhada.

??? success "Resposta comentada"

    Logs de um serviço SaaS que ninguém coleta, porque o cliente achava que o fornecedor monitorava e o fornecedor considera o monitoramento responsabilidade do cliente. Outro exemplo: contas de integração que nenhum dos lados revisa.

## Exercício de tomada de decisão

!!! question "Cenário: reduzir a superfície de ataque da Meridiana"

    A Meridiana tem, alcançáveis da internet: o portal B2B, a VPN, um servidor FTP usado por dois clientes antigos para enviar pedidos, a interface web de gestão do firewall e o webmail. O orçamento permite tratar dois itens neste trimestre. Quais você escolheria e como? Use como critérios o privilégio obtido por quem explorar o item, a facilidade de remoção ou de substituição e a fragilidade do protocolo ou do serviço.

??? success "Resolução de referência"

    | Critério | Peso | Portal B2B | VPN | FTP | Gestão do firewall | Webmail |
    |:---|:---|:---|:---|:---|:---|:---|
    | Privilégio obtido se explorado | 3 | 2 | 3 | 2 | 3 | 2 |
    | Facilidade de remoção ou substituição | 2 | 1 | 1 | 2 | 3 | 1 |
    | Fragilidade do protocolo ou do serviço | 2 | 2 | 2 | 3 | 2 | 2 |
    | **Total ponderado** | | **12** | **15** | **16** | **19** | **12** |

    1. **Interface de gestão do firewall:** remover da internet — é o ponto de entrada de privilégio máximo e não há motivo para estar exposto. Custo quase zero.
    2. **Servidor FTP:** substituir por envio via portal B2B ou SFTP com credenciais por cliente, ou desligar após migrar os dois clientes. O FTP transmite credenciais em claro e é um serviço legado com pouca manutenção.

    A VPN (já discutida no Caso A) e o portal B2B precisam de tratamento, mas exigem projeto maior. O critério usado foi **privilégio e facilidade de remoção**: os melhores primeiros passos são remover pontos de entrada que não deveriam existir.

## Pontos-chave

- Trust boundaries são onde o nível de confiança muda; é ali que se aplicam autenticação, autorização e validação.
- A superfície de ataque inclui todos os pontos de entrada, não só os públicos.
- Priorize pontos de entrada por exposição, privilégio e dados alcançáveis.
- Responsabilidade compartilhada cria fronteiras organizacionais, cujas lacunas são causa frequente de incidentes.
- Remover pontos de entrada desnecessários costuma ser o controle mais barato e eficaz.

## Referências

### Fundamentação principal

- R. Anderson. *Security Engineering*, 3ª ed. Cap. 10 *Boundaries* (pp. 341–370), especialmente §10.1 — fronteiras dependem de governança e incentivos, além de tecnologia.
- NIST. *SP 800-160 Vol. 1 Rev. 1*. 2022. Cap. 2, *Trust and Trustworthiness* (p. 10) — distinção entre confiança e confiabilidade demonstrada por evidência. <https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final>
- NIST. *SP 800-145*. 2011. §2 — modelos de serviço e a base da divisão de responsabilidades. <https://csrc.nist.gov/pubs/sp/800/145/final>

### Leitura complementar

- NIST. *SP 800-207*. §2.1 (p. 6) — por que a localização na rede não deve conferir confiança.
- AWS. *Security Pillar* — seção *Definition*, sobre o modelo de responsabilidade compartilhada.

### Aplicação prática

- A tabela de pontos de entrada desta aula é o ponto de partida dos Data Flow Diagrams e do STRIDE no [M04](../../curriculum/index.md).

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última atualização | 2026-10-23 |
