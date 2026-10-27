---
id: LAB-02
title: "Laboratório 02 — Modelagem arquitetural como código"
description: Laboratório local e gratuito em que o estudante descreve uma arquitetura em YAML, gera o diagrama com fronteiras de confiança, analisa achados de revisão e constrói o To-Be com um ADR.
domain: enterprise-architecture
tier: professional
status: published
prerequisites: [M02-L03, M02-L04, M02-L08]
objectives:
  - Representar uma arquitetura como modelo versionável, com zonas, componentes e fluxos.
  - Interpretar achados de revisão arquitetural e classificá-los por nível de abstração.
  - Construir um modelo To-Be que elimine os achados de severidade alta.
  - Registrar uma decisão do To-Be em um ADR.
estimated_time: "2 a 3 h"
cost: "Sem custo — execução local"
tested: true
last_updated: 2026-10-23
reviewed_by: [Andrews Ferreira]
---

# Laboratório 02 — Modelagem arquitetural como código

<div class="saa-lesson-meta" markdown>
<span class="saa-level">Laboratório · LAB-02</span>
<span class="saa-tier saa-tier--professional">Professional</span>
<span class="saa-meta">2 a 3 h · sem custo</span>
</div>

## Resumo

!!! danger "Ambiente isolado e dados sintéticos"

    Este laboratório roda inteiramente no seu computador, sem acesso a nenhum sistema real. Todos os dados descrevem a organização fictícia do Caso A.

| Item | Valor |
|:---|:---|
| Tempo estimado | 2 a 3 horas |
| Custo | Nenhum — Python e uma biblioteca open source |
| Status de teste | **Executado e testado** em 2026-10-23: passos executados em ambiente limpo; ferramenta e modelos verificados por testes automatizados no CI |
| Arquivos | [`examples/lab-02-architecture-modeling/`](https://github.com/andrewsferreira/security-architecture-academy/tree/main/examples/lab-02-architecture-modeling) |

Você vai descrever a arquitetura da Meridiana Distribuidora como **código** — um arquivo YAML com zonas, componentes e fluxos —, gerar o diagrama automaticamente, analisar os achados de uma revisão automatizada e construir o To-Be até eliminar os achados graves. O objetivo não é aprender uma ferramenta, e sim praticar a **leitura de fronteiras de confiança, a classificação de lacunas e o registro de decisões**.

## Objetivo

- Representar uma arquitetura como modelo versionável, com zonas, componentes e fluxos.
- Interpretar achados de revisão arquitetural e classificá-los por nível de abstração.
- Construir um modelo To-Be que elimine os achados de severidade alta.
- Registrar uma decisão do To-Be em um ADR.

## Cenário empresarial

A diretoria da Meridiana Distribuidora — o mesmo cenário do [Caso A](../case-studies/case-a-meridiana/index.md) — pediu que a arquitetura de segurança deixasse de viver em apresentações. Você decidiu manter os modelos de arquitetura **no repositório**, junto dos ADRs, para que cada mudança seja revisada e o diagrama nunca fique desatualizado em relação ao modelo. Antes de propor isso à equipe, vai testar a abordagem com o As-Is e um To-Be.

## Requisitos

| Item | Versão | Observação |
|:---|:---|:---|
| Python | 3.11 ou superior | Gratuito |
| PyYAML | 6.x | Gratuito, instalado pelo `pip` |
| Editor de texto | Qualquer | Recomendado um com destaque de YAML |
| Visualizador Mermaid | Qualquer | [Mermaid Live Editor](https://mermaid.live/), o GitHub ou o portal local da Academy |

## Arquitetura inicial

O modelo `models/meridiana-as-is.yaml` descreve o As-Is do Caso A. Sua estrutura:

```yaml title="Estrutura do modelo (extrato)"
name: "Meridiana Distribuidora — As-Is"
zones:                                  # (1)!
  - {id: internet, name: Internet, trust: 0}
  - {id: internal, name: Rede interna plana, trust: 2}
components:                             # (2)!
  - {id: vpn, name: VPN SSL, type: remote-access, zone: dmz, critical: true, redundancy: 1, logging: local}
flows:                                  # (3)!
  - {from: remote-users, to: vpn, protocol: HTTPS, authn: password, encrypted: true, data: internal}
```

1.  Zonas de confiança, com nível de 0 (nenhuma confiança) a 4 (máxima). Zonas de gestão recebem `management: true`.
2.  Componentes com tipo, zona e atributos que importam para a revisão: criticidade, redundância, envio de logs, suporte do fabricante e, para backups, imutabilidade, cópia fora do site e identidade administrativa.
3.  Fluxos com origem, destino, protocolo, autenticação (`none`, `password`, `shared`, `mfa`, `mtls`, `token`, `certificate`), criptografia e classificação dos dados.

## Passo a passo

### 1. Preparar o ambiente

```bash
git clone https://github.com/andrewsferreira/security-architecture-academy.git
cd security-architecture-academy/examples/lab-02-architecture-modeling
python3 -m venv .venv
source .venv/bin/activate        # Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install pyyaml
```

**Resultado esperado:** o comando `python archcheck.py --help` exibe as opções da ferramenta.

### 2. Analisar o As-Is

```bash
python archcheck.py models/meridiana-as-is.yaml \
  --mermaid as-is.mmd --report as-is.md
```

**Resultado esperado:** um relatório com **10 achados de severidade alta** e 20 médios, e os arquivos `as-is.md` e `as-is.mmd`.

### 3. Visualizar o diagrama

Abra `as-is.mmd` no Mermaid Live Editor (copie e cole o conteúdo). Os componentes com achados aparecem com contorno vermelho.

Antes de seguir, responda para si: **quais fluxos cruzam fronteiras de confiança?** Compare a sua resposta com as regras disparadas.

### 4. Classificar os achados

Para cada achado de severidade alta, registre em uma tabela:

| Regra | Achado | Nível da lacuna (conceitual, lógica ou física) | Requisito do Caso A relacionado |
|:---|:---|:---|:---|
| … | … | … | … |

A classificação por nível é a habilidade central da [aula 03](../modules/02-security-architecture/03-conceptual-logical-physical.md#as-is-e-to-be-em-cada-nivel).

### 5. Construir o To-Be

```bash
cp models/meridiana-as-is.yaml models/meridiana-to-be.yaml
```

Edite `models/meridiana-to-be.yaml` aplicando as decisões da sua solução do Caso A: novas zonas, fluxos intermediados, autenticação forte, backup isolado, monitoramento. **Altere o modelo, não as regras.**

Execute repetidamente:

```bash
python archcheck.py models/meridiana-to-be.yaml --mermaid to-be.mmd --report to-be.md --fail-on high
echo $?    # 0 quando não houver achados de severidade alta
```

**Resultado esperado:** código de saída `0` e nenhum achado alto. Achados médios podem permanecer se forem **riscos residuais conscientes** — por exemplo, o servidor legado, coberto por uma exceção.

### 6. Registrar uma decisão

Escolha a mudança mais significativa do seu To-Be e escreva um ADR no [modelo da Academy](../artifacts/architecture-decision-record.md), salvo como `adr-001.md` ao lado do modelo.

### 7. Comparar com a referência

Somente agora, execute a ferramenta sobre o modelo de referência e compare:

```bash
python archcheck.py solutions/meridiana-to-be.yaml --report referencia.md
```

## Critérios de validação

- [ ] O As-Is foi analisado e os achados altos foram classificados por nível.
- [ ] O To-Be é um modelo válido (a ferramenta não retorna erros de modelo).
- [ ] `archcheck.py --fail-on high` retorna código `0` para o seu To-Be.
- [ ] Cada achado médio remanescente está justificado como risco residual.
- [ ] Há um ADR com alternativas, consequências negativas e risco residual.

## Evidências esperadas

| Evidência | Arquivo |
|:---|:---|
| Relatório e diagrama do As-Is | `as-is.md`, `as-is.mmd` |
| Modelo To-Be | `models/meridiana-to-be.yaml` |
| Relatório e diagrama do To-Be | `to-be.md`, `to-be.mmd` |
| Tabela de classificação dos achados | Documento próprio |
| ADR | `adr-001.md` |

## Perguntas arquiteturais

1. A ferramenta não acusa nenhum achado para a conexão do portal com a API de integração se ela usar mTLS. Isso significa que o fluxo é seguro? O que a ferramenta **não** consegue avaliar?
2. Por que faz sentido que o servidor de etiquetas continue gerando um achado médio no To-Be?
3. Você aumentou a redundância de vários componentes para eliminar achados de ponto único de falha. Que custo isso tem, e quais desses achados você aceitaria como risco?
4. Que vantagens e limitações tem manter o modelo de arquitetura no repositório, em vez de em uma ferramenta de diagramação?
5. Que regra você acrescentaria à ferramenta para a realidade da sua organização?

## Explicação do resultado

??? success "O que este laboratório demonstra"

    **Fronteiras de confiança tornam-se verificáveis.** Ao declarar zonas e níveis de confiança, regras simples conseguem apontar fluxos que entram em zonas mais confiáveis sem autenticação, dados confidenciais sem criptografia e repositórios críticos alcançados a partir da DMZ — exatamente os achados que uma revisão manual do Caso A deveria encontrar.

    **A maioria das lacunas do As-Is é lógica.** Rede plana, acesso remoto apenas com senha e acesso direto ao banco são decisões de *padrão*, não de produto. Por isso o To-Be muda principalmente zonas e fluxos.

    **Achados médios remanescentes são decisões, não falhas.** O servidor sem suporte continua no To-Be porque depende do fornecedor; a ferramenta mantém o achado visível, e a exceção e o ADR tornam o risco consciente.

    **A ferramenta é deliberadamente limitada.** Ela não avalia autorização dentro das aplicações, qualidade das regras do firewall, configuração real nem ameaças específicas do negócio. Revisão automatizada é um **filtro**, não um parecer — esse é o ponto da pergunta 1.

    **Modelo e diagrama não divergem.** Como o diagrama é gerado do modelo, a visão nunca fica desatualizada em relação a ele. A divergência que resta é entre o modelo e o ambiente real — tratada nos módulos seguintes com inventário e infraestrutura como código.

## Desmontagem

Nenhum recurso externo é criado. Para remover tudo:

```bash
deactivate
rm -rf .venv as-is.* to-be.* referencia.md
```

Mantenha o seu modelo To-Be e o ADR se quiser reutilizá-los no Caso A.

## Referências

- ISO/IEC/IEEE. *42010:2022 — Architecture description*. <https://committee.iso.org/standard/74393.html> — norma paga; resumo público.
- M. Nygard. *Documenting Architecture Decisions*. 2011. <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions> — gratuito.
- Mermaid. *Mermaid Live Editor*. <https://mermaid.live/> — gratuito.

## Revisão

| Campo | Valor |
|:---|:---|
| Autor | Security Architecture Academy |
| Revisão técnica | Andrews Ferreira — 2026-10-27 |
| Última execução de teste | 2026-10-23 — `pytest examples/` e execução dos passos 1, 2, 3, 5, 7 e da desmontagem em diretório limpo (Linux, Python 3.13, PyYAML 6). No passo 5, o To-Be foi validado com o modelo de referência; a edição pelo estudante não é automatizável. |
