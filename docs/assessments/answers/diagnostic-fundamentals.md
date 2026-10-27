---
title: "Gabarito — Avaliação diagnóstica de fundamentos"
description: Gabarito comentado da avaliação diagnóstica de fundamentos, com justificativa das alternativas incorretas e indicação de estudo por seção.
status: published
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
---

# Gabarito — Avaliação diagnóstica de fundamentos

!!! warning "Responda primeiro"

    Este é o gabarito da [avaliação diagnóstica](../diagnostic-fundamentals.md). Faça a avaliação antes de ler.

## Resumo das respostas

| Seção A | Seção B | Seção C |
|:---|:---|:---|
| A1 **b** · A2 **d** · A3 **c** · A4 **c** · A5 **a** · A6 **c** | B1 **c** · B2 **a** · B3 **b** · B4 **c** · B5 **d** · B6 **b** | C1 **b** · C2 **d** · C3 **a** · C4 **d** · C5 **a** · C6 **c** |

## Seção A — Infraestrutura e redes

**A1 — (b) NAT.** A tradução de endereços privados para públicos é Network Address Translation. (a) DHCP atribui endereços automaticamente; (c) DNS resolve nomes; (d) VLAN segmenta a rede na camada 2. *Estudo:* M00-L02.

**A2 — (d).** VLANs separam domínios de broadcast; a comunicação entre elas exige roteamento em camada 3 — e é nesse ponto que se aplica filtragem entre zonas. (a) é falsa: VLANs não se comunicam sem roteamento; (b) VPN interliga redes remotas e não é necessária no mesmo switch; (c) DNS não provê conectividade. *Estudo:* M00-L03.

**A3 — (c).** Em PaaS, o provedor cuida da infraestrutura e da plataforma; o cliente continua responsável pela aplicação que implanta, pelos dados e pela configuração de acesso. (a), (b) e (d) são responsabilidades do provedor nesse modelo. *Estudo:* M00-L06 e M01-L03.

**A4 — (c).** O banco em instância única é o ponto único de falha. (a) o balanceador pode ser ponto único se não for redundante, mas o enunciado não dá essa informação, e "sempre" é incorreto; (b) os servidores de aplicação estão duplicados; (d) há um ponto único evidente. *Estudo:* M00-L04.

**A5 — (a).** Containers compartilham o kernel do hospedeiro; máquinas virtuais têm kernel próprio sobre um hipervisor. Por isso uma falha no kernel afeta todos os containers do host. (b) é o oposto do usual; (c) e (d) são falsas. *Estudo:* M00-L01 e M00-L05.

**A6 — (c) Duas.** Internet → DMZ é uma fronteira; DMZ → zona interna é outra. O protocolo (d) não muda o número de fronteiras, apenas os controles necessários em cada uma. *Estudo:* M00-L07 e M01-L03.

## Seção B — Princípios e mecanismos de segurança

**B1 — (c) Não repúdio.** A assinatura vinculada ao aprovador impede que ele negue a ação. (d) Autorização decide se ele *podia* aprovar, não impede a negação posterior; (a) e (b) não se relacionam ao cenário. *Estudo:* M01-L01.

**B2 — (a) Fail secure.** Em falha, o sistema assume o estado mais seguro — negar. (b) é a sobreposição de controles; (c) e (d) são princípios não relacionados ao comportamento em falha. *Estudo:* M01-L02.

**B3 — (b) Separation of duties.** A mesma pessoa controla duas etapas que deveriam ser independentes, o que permite fraude sem conluio. (a) Least privilege trata do excesso de permissões em geral; aqui o problema específico é a combinação de funções. *Estudo:* M01-L02.

**B4 — (c) Assinatura digital.** Garante integridade e autenticidade da origem. (a) criptografia simétrica protege confidencialidade e não identifica o emissor entre quem tem a chave; (b) um hash publicado no mesmo servidor pode ser trocado junto com o arquivo por quem comprometer o servidor; (d) compactação com senha não prova a origem. *Estudo:* M01-L04.

**B5 — (d).** Inventário e renovação automatizada de certificados evitam expirações. (a) e (b) removem proteção; (c) certificados muito longos aumentam o impacto de comprometimentos e dificultam a troca de algoritmos. *Estudo:* M01-L05.

**B6 — (b) Confidencialidade.** Bell-LaPadula trata do fluxo de informação para impedir leitura acima do nível de habilitação e escrita para níveis inferiores. (a) Integridade é o foco do modelo Biba. *Estudo:* M01-L07.

## Seção C — Risco e controles

**C1 — (b).** Risco combina probabilidade (uma ameaça explorar uma vulnerabilidade) e impacto. (a) confunde conceitos; (c) ignora contexto e impacto; (d) descreve uma vulnerabilidade, não uma ameaça. *Estudo:* M01-L06.

**C2 — (d) Detectivo.** O alerta identifica um evento que já ocorreu. Ele pode disparar uma ação corretiva, mas sua função principal é detectar. *Estudo:* M01-L06.

**C3 — (a) Controle compensatório.** Substitui parcialmente o controle exigido (MFA no sistema) por outro que trata o mesmo risco (acesso controlado com MFA no bastion). Deve vir acompanhado de exceção com prazo. *Estudo:* M01-L06 e M02-L04.

**C4 — (d) Seguro.** Transfere parte do impacto financeiro para terceiros. (a) é evitar; (b) é mitigar; (c) é aceitar. *Estudo:* M01-L06; aprofundado em M03-L06.

**C5 — (a) Normalmente menor.** O risco depende de exposição, probabilidade e impacto, não apenas da severidade técnica. (b) ignora o contexto; (c) risco raramente é zero; (d) generaliza sem base. *Estudo:* M01-L06; aprofundado em M14-L05.

**C6 — (c) Risco residual.** É o risco que permanece após os controles. (a) Risco inerente é o risco antes dos controles; (b) risco transferido é a parcela repassada a terceiros; (d) risco operacional é uma categoria de risco, não uma etapa do tratamento. *Estudo:* M01-L06.

## Interpretação do resultado

| Resultado por seção | O que fazer |
|:---|:---|
| 6 ou 5 acertos | Siga para o Módulo 02. |
| 4 acertos | Revise as aulas indicadas nas questões erradas e refaça a seção. |
| 3 ou menos | Estude o módulo correspondente (Seção A: M00; Seções B e C: M01) antes do Módulo 02. |

Enquanto M00 e M01 não estiverem publicados, use as referências indicadas nas aulas do Módulo 02 e o [registro de fontes](../../resources/index.md) para revisar os temas.
