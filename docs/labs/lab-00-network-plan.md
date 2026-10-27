---
id: LAB-00
title: "Laboratório 00 — Plano de endereçamento e segmentação"
description: Laboratório local e gratuito em que o estudante revisa o plano de rede de uma empresa fictícia — sobreposição de endereços entre datacenter e nuvem, rede plana, fluxos amplos e administração exposta — e constrói um plano To-Be segmentado, com fluxos documentados.
domain: infrastructure-foundations
tier: fundamental
status: published
prerequisites: [M00-L02, M00-L03, M00-L07]
objectives:
  - Ler um plano de endereçamento e identificar sobreposições entre ambientes.
  - Reconhecer redes planas e zonas que misturam funções.
  - Documentar fluxos mínimos entre zonas, com portas e finalidade.
  - Construir um plano To-Be que elimine os problemas graves e justificar cada mudança.
estimated_time: "1 h 30 min a 2 h"
cost: "Sem custo — execução local"
tested: true
last_updated: 2026-10-27
reviewed_by: [Andrews Ferreira]
---

# Laboratório 00 — Plano de endereçamento e segmentação

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Laboratório · LAB-00</span>
<span class="saa-tier saa-tier--fundamental">Fundamental</span>
<span class="saa-meta">1 h 30 min a 2 h · sem custo</span>
</div>

## Resumo

!!! danger "Ambiente isolado e dados sintéticos"

    Este laboratório roda inteiramente no seu computador e não faz nenhuma conexão de rede. Todos os endereços e nomes descrevem a organização fictícia Meridiana Distribuidora.

| Item | Valor |
|:---|:---|
| Tempo estimado | 1 h 30 min a 2 h |
| Custo | Nenhum — Python, somente biblioteca padrão |
| Status de teste | **Executado e testado** em 2026-10-23 e novamente em 2026-10-27: passos executados em diretório limpo; ferramenta e planos verificados por testes automatizados no CI |
| Arquivos | [`examples/lab-00-network-plan/`](https://github.com/andrewsferreira/security-architecture-academy/tree/main/examples/lab-00-network-plan) |

Você vai revisar o **plano de rede** da Meridiana — os blocos de endereços de cada ambiente, as zonas e os fluxos permitidos entre elas — com uma pequena ferramenta que aplica regras de revisão. Depois, vai reescrever o plano até eliminar os problemas graves. O objetivo é praticar o que o Módulo 00 ensinou: **endereçamento é decisão de arquitetura**, segmentação separa funções e cada fluxo entre zonas precisa ter porta e finalidade.

## Objetivo

- Ler um plano de endereçamento e identificar sobreposições entre ambientes.
- Reconhecer redes planas e zonas que misturam funções.
- Documentar fluxos mínimos entre zonas, com portas e finalidade.
- Construir um plano To-Be que elimine os problemas graves e justificar cada mudança.

## Cenário empresarial

A Meridiana Distribuidora tem um datacenter, um centro de distribuição em Contagem e acaba de colocar o portal B2B em uma conta de nuvem. O time que montou a nuvem escolheu o bloco `10.0.0.0/16` "porque é o padrão" — o mesmo do datacenter. Agora a diretoria quer integrar o portal ao ERP, e o fornecedor do ERP continua acessando o servidor por RDP pela internet. Você foi chamado para revisar o plano antes da integração.

## Requisitos

| Item | Versão | Observação |
|:---|:---|:---|
| Python | 3.11 ou superior | Gratuito; nenhuma biblioteca externa |
| Editor de texto | Qualquer | Para editar JSON |

## Arquitetura inicial

O arquivo `models/meridiana-as-is.json` tem três partes:

```json title="Estrutura do plano (extrato)"
{
  "allocations": {"datacenter": "10.0.0.0/16", "aws-portal": "10.0.0.0/16"},
  "zones": [
    {"name": "rede-corporativa", "trust": "internal", "environment": "datacenter",
     "cidr": "10.0.0.0/16", "hosts": 220, "roles": ["users", "servers", "management"]}
  ],
  "flows": [
    {"from": "internet", "to": "rede-corporativa", "ports": [3389],
     "purpose": "acesso remoto do fornecedor do ERP"}
  ]
}
```

- **allocations** — o bloco de endereços reservado para cada ambiente (datacenter, nuvem, filial).
- **zones** — cada zona com nível de confiança (`untrusted`, `dmz`, `internal`, `restricted`, `management`), ambiente, sub-rede, quantidade aproximada de hosts e funções (`users`, `servers`, `management`, `devices`).
- **flows** — fluxos permitidos entre zonas, com portas e finalidade.

As regras da ferramenta, em resumo:

| Regra | O que verifica | Aula relacionada |
|:---|:---|:---|
| AD-01 | Blocos de ambientes diferentes não podem se sobrepor | [M00-L02](../modules/00-foundations/02-tcp-ip-networking.md) |
| AD-02, AD-03 | Zonas dentro do bloco do ambiente e sem sobreposição entre si | M00-L02 |
| AD-04 | Faixas internas privadas (RFC 1918) | M00-L02 |
| SG-01, SG-02 | Zonas grandes demais e mistura de usuários, servidores e gestão | [M00-L03](../modules/00-foundations/03-segmentation-connectivity.md) |
| FL-01 a FL-04 | Fluxos com qualquer porta, origem não confiável em zona interna, fluxo sem finalidade e administração fora da zona de gestão | M00-L03 e [M00-L07](../modules/00-foundations/07-reading-architecture-diagrams.md) |

## Passo a passo

### 1. Preparar o ambiente

```bash
git clone https://github.com/andrewsferreira/security-architecture-academy.git
cd security-architecture-academy/examples/lab-00-network-plan
python3 netplan.py --help
```

**Resultado esperado:** a ferramenta exibe a ajuda. Não é preciso instalar nada.

### 2. Revisar o As-Is

```bash
python3 netplan.py models/meridiana-as-is.json --markdown as-is.md
```

**Resultado esperado:** **11 achados — 8 altos, 2 médios e 1 baixo** —, código de saída `1` e o relatório `as-is.md`. Os dois fluxos com "qualquer porta" (FL-01) são altos porque chegam à rede corporativa, que abriga funções de gestão.

### 3. Interpretar os achados

Antes de corrigir, responda para cada achado alto: **qual o risco concreto?** Use a tabela:

| Regra | Achado | Risco concreto | Correção pretendida |
|:---|:---|:---|:---|
| AD-01 | Datacenter e nuvem no mesmo bloco | … | … |
| … | … | … | … |

### 4. Construir o To-Be

```bash
cp models/meridiana-as-is.json models/meridiana-to-be.json
```

Edite o novo arquivo. Algumas decisões que você precisará tomar:

- Um bloco por ambiente, sem sobreposição (por exemplo, um `/16` para o datacenter, outro para a nuvem, um bloco menor para o CD).
- Zonas separadas para usuários, servidores e gestão; uma zona intermediária para o acesso remoto.
- Fluxos com as portas realmente necessárias e a finalidade de cada um; administração apenas a partir da zona de gestão.

Execute até não restar nenhum achado alto:

```bash
python3 netplan.py models/meridiana-to-be.json --markdown to-be.md
echo $?    # 0 quando não houver achados altos
```

**Altere o plano, não as regras.**

### 5. Comparar com a referência

Somente agora, compare com o plano de referência:

```bash
python3 netplan.py solutions/meridiana-to-be.json
```

**Resultado esperado:** zero achados. Compare as decisões — blocos, zonas, fluxos — com as suas. Diferenças são normais; o que importa é conseguir justificá-las.

## Critérios de validação

- [ ] O As-Is foi revisado e cada achado alto tem risco concreto descrito.
- [ ] O To-Be não tem erros de estrutura e retorna código `0`.
- [ ] Nenhum bloco de ambiente se sobrepõe a outro.
- [ ] Usuários, servidores e gestão estão em zonas distintas.
- [ ] Todo fluxo tem portas específicas e finalidade.
- [ ] Administração parte apenas da zona de gestão.

## Evidências esperadas

| Evidência | Arquivo |
|:---|:---|
| Relatório do As-Is | `as-is.md` |
| Tabela de interpretação dos achados | Documento próprio |
| Plano To-Be | `models/meridiana-to-be.json` |
| Relatório do To-Be | `to-be.md` |

## Perguntas arquiteturais

1. Por que a sobreposição entre o bloco do datacenter e o da nuvem é um problema de **arquitetura**, e não só de configuração? O que acontece se ela só for descoberta depois de dez integrações?
2. O fluxo `vpc-portal → rede-corporativa` com qualquer porta foi criado "para funcionar". Que informação você precisa obter de quem o pediu para substituí-lo por um fluxo mínimo?
3. A ferramenta aceita um fluxo `internet → zona dmz` na porta 443. Isso significa que o serviço exposto é seguro? O que ela **não** avalia?
4. O fornecedor do ERP diz que precisa de RDP. Como atender à necessidade sem expor a porta 3389 à internet?
5. Que regra você acrescentaria para a realidade de uma rede com filiais e coletores de dados?

## Explicação do resultado

??? success "O que este laboratório demonstra"

    **Endereçamento é decisão de arquitetura.** A sobreposição `10.0.0.0/16` entre datacenter e nuvem parece inofensiva até a primeira integração: a partir daí, ou se renumera um dos lados, ou se usa NAT entre ambientes — e cada endereço passa a significar coisas diferentes conforme a origem, dificultando regras e investigações.

    **Rede plana é ausência de fronteira.** Uma zona com usuários, servidores e gestão permite que qualquer estação comprometida alcance tudo. Separar por função cria as fronteiras onde os controles do M00-L03 podem atuar.

    **Fluxo "any" é uma decisão adiada.** Quase sempre alguém sabe quais portas são necessárias; o trabalho do arquiteto é obter essa informação e registrar a finalidade, para que o fluxo possa ser revisado depois.

    **Administração tem caminho próprio.** RDP exposto à internet é um dos vetores iniciais mais explorados por ransomware; o To-Be leva o acesso remoto a uma zona intermediária com autenticação forte e a administração a uma zona de gestão.

    **A ferramenta é deliberadamente limitada.** Ela não sabe se o serviço na porta 443 está atualizado, se a autenticação é forte ou se a regra no firewall corresponde ao plano. Revisão automatizada é filtro, não parecer.

## Desmontagem

Nenhum recurso externo é criado. Para remover os arquivos gerados:

```bash
rm -f as-is.md to-be.md
```

## Referências

- IETF. *RFC 1918 — Address Allocation for Private Internets*. 1996. <https://www.rfc-editor.org/rfc/rfc1918> — gratuito.
- NIST. *SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy*. 2009. <https://csrc.nist.gov/pubs/sp/800/41/r1/final> — gratuito.
- Python Software Foundation. *ipaddress — IPv4/IPv6 manipulation library*. <https://docs.python.org/3/library/ipaddress.html> — gratuito.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última execução de teste | 2026-10-27 — `pytest examples/lab-00-network-plan` (7 testes, incluindo as contagens por severidade do passo 2) e execução dos passos 1, 2 e 5 em diretório limpo (Linux, Python 3.13). No passo 4, o To-Be foi validado com o plano de referência; a edição pelo estudante não é automatizável. |
