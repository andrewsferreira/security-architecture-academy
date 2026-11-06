---
id: M08-L01
title: "Aula 01 — Segurança de datacenters"
public_title: "Módulo 8 — Aula 01 — Segurança de datacenters"
description: Como proteger um datacenter próprio ou em colocation — camadas de segurança física, controles ambientais e de energia, gerenciamento fora de banda, ciclo de vida de mídias e equipamentos — e como avaliar a responsabilidade quando o datacenter é de terceiros.
domain: infrastructure-foundations
tier: fundamental
status: published
prerequisites: [M00-L04, M03-L05]
objectives:
  - Organizar a segurança física de um datacenter em camadas com controles preventivos e detectivos.
  - Relacionar energia, refrigeração e proteção contra incêndio a disponibilidade e aos objetivos de recuperação.
  - Especificar gerenciamento fora de banda e ciclo de vida seguro de mídias.
  - Avaliar a divisão de responsabilidades em colocation e hospedagem gerenciada.
minutes: 60
sources: [NIST-SP800-53, NSA-NETWORK-INFRA-2022, ISO-27002-2022, NIST-SP800-34-R1, CIS-CONTROLS-V8-1]
further_reading: [BOOK-ANDERSON-SE3, AWS-WA-RELIABILITY]
last_updated: 2026-10-29
reviewed_by: [Andrews Ferreira]
module: M08
---

# Aula 01 — Segurança de datacenters { #seguranca-de-datacenters }

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Módulo 8 · Nível 2</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">60 min · ID técnico: M08-L01</span>
</div>

## Resumo

!!! abstract "Nesta aula"

    Muitas organizações brasileiras ainda operam datacenters próprios ou salas de servidores — e quase todas dependem de algum datacenter de terceiros. A segurança física costuma ficar fora do radar do arquiteto de segurança, até que um técnico sai com um disco, um ar-condicionado falha num fim de semana ou um switch de gerência fica acessível na rede de usuários. Esta aula organiza a segurança de datacenters em camadas e mostra onde ela encontra as decisões de arquitetura.

**Pré-requisitos:** [Datacenter e alta disponibilidade](../00-foundations/04-datacenter-high-availability.md) e [BIA, RTO e RPO](../03-governance-risk/05-bia-rto-rpo.md).

**Objetivos de aprendizagem** — ao final, você será capaz de:

- Organizar a segurança física de um datacenter em camadas com controles preventivos e detectivos.
- Relacionar energia, refrigeração e proteção contra incêndio a disponibilidade e aos objetivos de recuperação.
- Especificar gerenciamento fora de banda e ciclo de vida seguro de mídias.
- Avaliar a divisão de responsabilidades em colocation e hospedagem gerenciada.

## Conceito

### Defesa em profundidade física

A segurança física aplica o mesmo princípio de defesa em profundidade (Módulo 1 — Aula 02) a espaços: cada camada reduz quem chega à seguinte e registra quem passou.

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/m08-l01-datacenter-layers.mmd"
```

<figcaption>Figura 1 — Camadas físicas do site ao equipamento, com infraestrutura de suporte e gerenciamento fora de banda.</figcaption>
</figure>

| Camada | Controles preventivos | Controles detectivos |
|:---|:---|:---|
| **Site** | Barreiras, controle de veículos | Vigilância por vídeo, rondas |
| **Edifício** | Recepção, identificação, crachás de visitante | Registro de visitantes |
| **Sala** | Acesso por credencial e segundo fator, lista de autorizados revisada | Registro de entradas, vídeo, alarme de porta aberta |
| **Rack** | Fechaduras, acesso por equipe | Sensores de abertura |
| **Equipamento** | Portas e consoles desabilitados ou protegidos, discos cifrados | Inventário e conferência periódica |

O catálogo SP 800-53 Rev. 5 dedica uma família inteira à proteção física e ambiental (PE), e a ISO/IEC 27002:2022 organiza seus 93 controles em quatro temas, um deles de controles físicos (estrutura conferida em fonte secundária; a norma é paga) — referências úteis para montar o checklist, que deve ser proporcional ao risco.

## Fundamentos técnicos

### Infraestrutura de suporte e disponibilidade

| Elemento | Falha típica | Efeito na arquitetura |
|:---|:---|:---|
| **Energia** | Queda da concessionária, falha do nobreak | Redundância de alimentação; teste do gerador; desligamento ordenado |
| **Refrigeração** | Falha de um equipamento em fim de semana | Redundância, alarmes de temperatura com plantão |
| **Incêndio** | Detecção tardia, combate que danifica equipamentos | Detecção precoce, sistema de combate adequado à sala |
| **Água e umidade** | Vazamento | Sensores, posicionamento da sala |

Essas falhas entram na BIA (Módulo 3 — Aula 05) como causas de indisponibilidade, e a SP 800-34 Rev. 1 inclui a identificação de **controles preventivos** como etapa do planejamento de contingência, antes das estratégias de recuperação.

### Gerenciamento fora de banda

Interfaces de gerenciamento de servidores (controladoras de placa-mãe), de switches e de storage são **plano de gestão** com privilégio total sobre o hardware. A NSA recomenda, para equipamentos que não suportam protocolos de gerenciamento cifrados, conectar um sistema de gerência diretamente à porta de console ou de gerenciamento, ou estabelecer uma **rede de gerenciamento fora de banda dedicada**, e colocar equipamentos sem suporte a listas de controle em um segmento de gerenciamento separado (Sec. 7.1 e 7.4). Na arquitetura:

- Rede de gerenciamento separada da produção e dos usuários.
- Acesso apenas a partir da zona de gestão, via bastion (Módulo 5 — Aula 04).
- Credenciais padrão trocadas e contas nominais.
- Firmware das controladoras incluído no ciclo de correções.

### Ciclo de vida de mídias e equipamentos

| Etapa | Prática |
|:---|:---|
| Entrada | Inventário com número de série e dono |
| Operação | Discos cifrados; troca de discos registrada |
| Manutenção | Técnico acompanhado; discos com defeito não saem sem sanitização ou destruição |
| Descarte | Sanitização ou destruição com evidência (certificado) |

### Colocation e hospedagem

Em colocation, o provedor responde pelas camadas externas (site, edifício, energia, refrigeração), e o cliente pelo rack, pelos equipamentos e pela lógica. A divisão precisa estar no **contrato** e ser verificável: relatórios de auditoria do provedor, lista de quem tem acesso à gaiola ou ao rack, procedimento de acompanhamento de técnicos e notificação de incidentes físicos. É a mesma lógica da responsabilidade compartilhada em nuvem (Módulo Inicial — Aula 06).

## Exemplo empresarial

!!! example "Meridiana — a sala de servidores e o gerador"

    Uma avaliação da sala de servidores da Meridiana encontrou: lista de acesso com 34 pessoas (17 já desligadas), controladoras de servidores na mesma rede dos usuários com senha padrão, gerador nunca testado sob carga e discos substituídos guardados em uma caixa no almoxarifado.

    Ações: lista de acesso reduzida a 6 pessoas com revisão trimestral; rede de gerenciamento separada, acessível só pela zona de gestão; teste semestral do gerador incluído no plano de contingência; procedimento de sanitização e destruição de discos com registro. O custo foi baixo — e a controladora com senha padrão, sozinha, permitiria reinstalar ou desligar qualquer servidor.

## Arquitetura tradicional versus recomendada

| Aspecto | Prática tradicional | Prática recomendada |
|:---|:---|:---|
| Acesso à sala | Lista que só cresce | Lista mínima, revisada, com segundo fator |
| Gerenciamento de hardware | Na rede de usuários, senha padrão | Rede fora de banda, acesso pela zona de gestão |
| Infraestrutura de suporte | Testada na instalação | Testes periódicos, alarmes com plantão |
| Mídias | Descarte informal | Sanitização ou destruição com evidência |
| Colocation | Confiança no provedor | Responsabilidades contratuais e evidências |

## Controles e padrões relevantes

Controles do catálogo da NIST SP 800-53 Rev. 5 (Release 5.2.0) e dos CIS Controls v8.1, referências voluntárias para as camadas físicas, a infraestrutura de suporte e o gerenciamento de hardware:

| Controle ou padrão | Objetivo no datacenter | Referência |
|:---|:---|:---|
| Autorização e controle de acesso físico | Lista de autorizados mantida e revisada; acesso controlado nos pontos de entrada | SP 800-53: PE-2 (Physical Access Authorizations) e PE-3 (Physical Access Control) |
| Monitoração do acesso físico | Monitorar e revisar registros de acesso físico | SP 800-53: PE-6 (Monitoring Physical Access) |
| Infraestrutura de suporte | Energia de emergência, proteção contra incêndio, controles ambientais e contra água | SP 800-53: PE-11, PE-13, PE-14 e PE-15 |
| Mídias e descarte | Sanitizar mídias antes de descarte ou reuso | SP 800-53: MP-6 (Media Sanitization) |
| Dados em repouso | Proteção criptográfica de discos | SP 800-53: SC-28(1) (Cryptographic Protection) |
| Manutenção | Manutenção remota controlada e pessoal de manutenção autorizado e acompanhado | SP 800-53: MA-4 (Nonlocal Maintenance) e MA-5 (Maintenance Personnel) |
| Gerenciamento fora de banda | Rede de gerenciamento dedicada para interfaces de equipamentos | NSA, *Network Infrastructure Security Guidance*, Sec. 7.1 e 7.4; CIS v8.1: Controle 12 (Network Infrastructure Management) |

## Aplicabilidade: on-premises, cloud e híbrido

Em cloud, a segurança física é do provedor, e a organização obtém evidência por relatórios de auditoria e certificações — dentro do escopo declarado (Módulo 3 — Aula 04). Em on-premises e colocation, a responsabilidade é total ou compartilhada. Em ambientes híbridos, a sala de servidores remanescente (com controladores de domínio, backup ou legados) frequentemente recebe menos atenção do que deveria, justamente por ser "o que sobrou".

## Como especificar e implementar

- "O acesso a salas de servidores exige credencial e segundo fator; a lista de autorizados é revisada trimestralmente."
- "Interfaces de gerenciamento de hardware ficam em rede fora de banda, acessível apenas pela zona de gestão."
- "Energia, refrigeração e detecção de incêndio têm redundância proporcional ao MTD e alarmes com plantão."
- "Mídias são cifradas em operação e sanitizadas ou destruídas com evidência no descarte."
- "Contratos de colocation definem responsabilidades, evidências e notificação de incidentes físicos."

## Trade-offs, limitações e antipadrões

- **Trade-off:** controles físicos fortes encarecem a operação diária; proporcione-os ao valor do que está na sala.
- **Antipadrão — "porta trancada" como único controle.**
- **Antipadrão — controladoras de servidor expostas:** controle total do hardware na rede de usuários.
- **Limitação:** segurança física não substitui a lógica; quem tem acesso legítimo à sala ainda pode abusar dele.

## Como validar

- Comparar a lista de acesso com o RH.
- Varrer a rede de usuários em busca de interfaces de gerenciamento de hardware.
- Revisar o último teste do gerador e dos alarmes.
- Pedir evidência do descarte dos últimos discos substituídos.

Critérios de aceite:

| Critério | Evidência |
|:---|:---|
| Nenhuma pessoa desligada na lista de acesso físico | Cruzamento da lista com o RH na última revisão |
| Nenhuma interface de gerenciamento de hardware alcançável da rede de usuários | Varredura da rede de usuários sem achado |
| Gerador e alarmes testados no período definido | Registro do último teste sob carga e dos alarmes com plantão |
| Todo disco substituído com evidência de sanitização ou destruição | Certificados ou registros correspondentes ao inventário de trocas |

## Como apresentar e justificar

- **Para a diretoria:** "Dezessete ex-funcionários ainda abriam a sala de servidores, e qualquer pessoa na rede podia desligar os servidores pela interface de gerenciamento. As duas correções custam pouco."
- **Para a operação:** "A interface de gerenciamento é o acesso mais poderoso que existe ao servidor; ela vai para a rede de gestão."

## Checklist de revisão arquitetural

- [ ] Camadas físicas com controles preventivos e detectivos.
- [ ] Lista de acesso mínima e revisada.
- [ ] Infraestrutura de suporte testada, com alarmes.
- [ ] Gerenciamento fora de banda isolado.
- [ ] Ciclo de vida de mídias com evidência.
- [ ] Responsabilidades de colocation em contrato.

## Questões de compreensão

**1.** Por que interfaces de gerenciamento de hardware merecem tratamento de plano de gestão?

??? success "Resposta comentada"

    Porque dão controle total sobre o equipamento — ligar, desligar, reinstalar, acessar o console — independentemente do sistema operacional. Expostas, contornam todos os controles lógicos do servidor.

**2.** Como a infraestrutura de suporte se liga à BIA?

??? success "Resposta comentada"

    Falhas de energia, refrigeração ou incêndio são causas de indisponibilidade; a redundância e os testes dessas infraestruturas precisam ser proporcionais ao MTD dos processos que dependem do datacenter.

**3.** O que verificar em um contrato de colocation?

??? success "Resposta comentada"

    A divisão de responsabilidades por camada, as evidências fornecidas pelo provedor (relatórios de auditoria), quem tem acesso ao espaço do cliente, o acompanhamento de técnicos e a notificação de incidentes físicos.

## Exercício de tomada de decisão

!!! question "Cenário: sala de servidores das clínicas da Lumen"

    Cada uma das 20 clínicas da Lumen tem um pequeno rack com switch, servidor de imagens e nobreak, em uma sala que também guarda material de limpeza. As opções são:

    - **A** — sala dedicada com controle de acesso por credencial em cada clínica;
    - **B** — requisitos proporcionais: rack fechado, disco cifrado, gerenciamento centralizado e sensores;
    - **C** — retirar o servidor de imagens das clínicas e centralizar as imagens no datacenter ou na nuvem.

    Compare as opções com uma matriz ponderada (notas de 1 a 3; 3 = melhor desempenho no critério) e proponha requisitos físicos proporcionais.

**Objetivos avaliados:** Organizar a segurança física de um datacenter em camadas com controles preventivos e detectivos; especificar gerenciamento fora de banda e ciclo de vida seguro de mídias.

**Entrega esperada:** Matriz ponderada e a lista de requisitos físicos proporcionais para as clínicas.

**Critérios de avaliação:**

- Os requisitos tratam o risco principal (furto e exposição de dados) com cifragem e gestão centralizada.
- Energia, temperatura e materiais inflamáveis são tratados como requisitos de disponibilidade.
- O risco residual de interrupção tem resposta (equipamento de reserva e restauração central).

??? success "Resolução de referência"

    | Critério | Peso | A — Sala dedicada com credencial | B — Requisitos proporcionais | C — Centralizar as imagens |
    |:---|:---|:---|:---|:---|
    | Proteção dos dados de saúde contra furto e acesso físico | 3 | 2 | 3 | 3 |
    | Custo para 20 clínicas | 2 | 1 | 3 | 2 |
    | Continuidade do atendimento se o link cair | 2 | 3 | 3 | 1 |
    | Esforço de operação | 1 | 1 | 2 | 3 |
    | **Total ponderado** | | **15** | **23** | **18** |

    - **Pesos:** o risco principal é a exposição de dados de saúde por furto do equipamento (peso 3). Custo e continuidade pesam 2: são 20 clínicas, e o atendimento depende das imagens. O esforço pesa 1.
    - **Recomendação: B**, com os requisitos a seguir. A gasta em obra o que a cifragem resolve melhor; C elimina o dado local, mas torna o atendimento dependente do link de cada clínica.

    - **Rack fechado com chave** sob responsabilidade da gerência da clínica, com registro de abertura; câmera simples cobrindo o rack.
    - **Disco do servidor de imagens cifrado**, para que o furto do equipamento não exponha dados de saúde (LGPD, Módulo 3 — Aula 04).
    - **Interface de gerenciamento** do servidor e do switch acessível apenas pela rede de gestão via conexão com o datacenter central.
    - **Nobreak com alarme** de bateria e desligamento ordenado; sensor de temperatura com alerta central.
    - **Separação** de materiais inflamáveis do rack.
    - **Proporcionalidade:** sem controle biométrico nem sala dedicada — o principal risco (furto e exposição de dados) é tratado pela cifragem e pela gestão centralizada.
    - **Trade-off aceito e risco residual:** o furto ou a danificação do rack ainda interrompe o atendimento da clínica até a reposição; o residual é tratado com equipamento de reserva regional e restauração das imagens a partir do backup central.
    - **O que mudaria a decisão:** links redundantes e de boa capacidade em todas as clínicas tornariam C viável e eliminariam o dado local; uma exigência contratual de convênio ou de auditoria por controle de acesso físico nominal elevaria A nas clínicas de maior volume.

    **Erros comuns:**

    - Copiar requisitos de datacenter (sala dedicada, biometria) para 20 salas pequenas sem avaliar custo e efeito.
    - Esquecer que o furto do equipamento expõe dados se o disco não estiver cifrado.
    - Deixar a interface de gerenciamento acessível pela rede da clínica.

## Pontos-chave

- Segurança física é defesa em profundidade aplicada a espaços.
- Energia, refrigeração e incêndio são causas de indisponibilidade a tratar na BIA.
- Gerenciamento de hardware é plano de gestão: rede fora de banda e acesso pela zona de gestão.
- Mídias cifradas e descarte com evidência protegem dados no fim do ciclo.
- Em colocation, responsabilidades e evidências precisam estar no contrato.

## Referências

### Fundamentação principal

- NIST. *SP 800-53 Rev. 5*, Release 5.2.0 — família PE; controles PE-2, PE-3, PE-6, PE-11, PE-13, PE-14, PE-15, MP-6, SC-28(1), MA-4 e MA-5, conferidos no catálogo OSCAL oficial — gratuito.
- NSA. *Network Infrastructure Security Guidance*. 2022 — Sec. 7.1 e 7.4, gerenciamento fora de banda. *(Lido.)*
- ISO/IEC. *ISO/IEC 27002:2022* — tema de controles físicos (estrutura conferida em fonte secundária).
- NIST. *SP 800-34 Rev. 1* — Cap. 3, controles preventivos no planejamento de contingência. *(Lido.)*
- CIS. *CIS Critical Security Controls v8.1* — Controle 12 — gratuito.

### Leitura complementar

- R. Anderson. *Security Engineering*, 3ª ed. — capítulo sobre proteção física.
- AWS. *Well-Architected — Reliability Pillar*.

### Aplicação prática

- Visite (ou peça fotos e listas de) uma sala de servidores da sua organização e preencha a tabela de camadas desta aula, indicando lacunas e o controle proporcional para cada uma.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Revisado por Andrews Ferreira — 2026-11-05 |
| Última atualização | 2026-10-29 |
