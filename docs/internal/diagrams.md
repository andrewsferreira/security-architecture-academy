---
title: Padrões de diagramas
description: Como produzir, nomear, estilizar e manter diagramas Mermaid na Security Architecture Academy, com um catálogo de diagramas conceituais demonstrativos.
---

# Padrões de diagramas

Diagramas são parte central da formação. Este padrão garante que sejam **legíveis, consistentes, editáveis e acessíveis** — e que cada um comunique algo relevante.

## Ferramenta e fontes

- **Mermaid** é o padrão: texto versionado, revisável em Pull Requests e renderizado tanto no GitHub quanto no portal.
- A fonte de cada diagrama fica em `assets/diagrams/<nome>.mmd` e é **incluída** nas páginas — nunca copiada:

    ````markdown
    ```mermaid
    ;--8<-- "assets/diagrams/zero-trust-flow.mmd"
    ```
    ````

- O CI valida a sintaxe de todas as fontes com `mermaid-cli` (`make diagrams`).
- Exportações SVG/PNG só são geradas quando o diagrama precisar ser usado fora do portal (slides, artigos). Elas ficam ao lado da fonte, com o mesmo nome.

## Requisitos obrigatórios

| Requisito | Como atender | Verificação |
|:---|:---|:---|
| Descrição acessível | `accTitle:` e `accDescr:` logo após a declaração do diagrama | `check_assets.py` |
| Propósito declarado | Frase no texto antes do diagrama: *"O diagrama mostra…"* | Revisão |
| Legibilidade | Até ~12 nós; acima disso, dividir em visões | Revisão |
| Funcionamento em light/dark | Sem `fill` fixo; classes semânticas usam apenas contorno | Revisão visual |
| Rótulos em português | Termos técnicos em inglês quando consolidados | Revisão |

## Convenções

### Nomenclatura

- Arquivo: kebab-case, em inglês, descrevendo o conteúdo — `hybrid-infrastructure.mmd`.
- IDs de nós: curtos e em maiúsculas (`IDP`, `PEP`, `DB`). Rótulos legíveis entre aspas: `IDP["Identity Provider"]`.
- Subtítulos de nó em `<small>` para detalhes secundários.

### Direção e fluxo

| Tipo de diagrama | Direção |
|:---|:---|
| Fluxos entre ambientes ou zonas | `flowchart LR` |
| Camadas, hierarquias, processos | `flowchart TB` / `TD` |
| Interações temporais (protocolos) | `sequenceDiagram` com `autonumber` |

**Largura.** A coluna de conteúdo do portal tem cerca de 690 px em telas de desktop, e o diagrama é reduzido para caber nela. Um `flowchart LR` com muitas etapas chega a 1.500–2.400 px de largura natural e fica com texto ilegível (escala abaixo de 0,5). Regra prática: se a largura natural passar de cerca de 1.200 px, use `flowchart TB` ou simplifique o diagrama. Para medir, gere o SVG com `npx mmdc -i arquivo.mmd -o saida.svg` e leia a largura do `viewBox`. A figura `saa-diagram` ocupa toda a largura da coluna; diagramas estreitos mantêm o tamanho natural e não são ampliados.

### Conexões

| Estilo | Significado |
|:---|:---|
| `-->` seta contínua | Fluxo de dados ou de requisição |
| `-.->` seta tracejada | Fluxo de controle, telemetria ou retroalimentação |
| `==>` seta espessa | Conectividade de rede entre ambientes |
| `---` / `-.-` sem seta | Associação ou abrangência |

Rotule as conexões quando o significado não for óbvio, de preferência com verbo ou protocolo: `-- "HTTPS" -->`.

### Boundaries

- **Trust boundaries e zonas** são `subgraph` com título explícito: `subgraph DATAZ["Zona de dados"]`.
- Um subgraph = um nível de confiança. Não use subgraph apenas para agrupar visualmente.

### Classes semânticas

Copie apenas as classes que o diagrama usa:

```text
classDef identity  stroke:#2f74e8,stroke-width:2px
classDef control   stroke:#0e9fb8,stroke-width:2px
classDef actor     stroke:#64748b,stroke-width:1.5px
classDef untrusted stroke:#dc2626,stroke-width:2px,stroke-dasharray:5 4
```

### Legendas

Diagramas de conteúdo usam `<figure>` com legenda numerada por página:

````html
<figure class="saa-diagram" markdown>

```mermaid
;--8<-- "assets/diagrams/network-segmentation.mmd"
```

<figcaption>Figura 1 — Segmentação por zonas de confiança.</figcaption>
</figure>
````

## Catálogo demonstrativo

!!! example "Exemplos demonstrativos"

    Os diagramas abaixo são **referências de estilo** criadas na fase de fundação. São conceituais e genéricos; os diagramas das aulas serão desenvolvidos com os respectivos módulos.

### Architecture Overview

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/architecture-overview.mmd"
```

<figcaption>Figura 1 — Relação entre governança, controles e ambientes híbridos, com o ciclo de retroalimentação do monitoramento. Fonte: <code>assets/diagrams/architecture-overview.mmd</code>.</figcaption>
</figure>

### Layered Security Architecture

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/layered-security.mmd"
```

<figcaption>Figura 2 — Defesa em profundidade: camadas independentes, com monitoramento transversal. Fonte: <code>assets/diagrams/layered-security.mmd</code>.</figcaption>
</figure>

### Zero Trust — fluxo conceitual

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/zero-trust-flow.mmd"
```

<figcaption>Figura 3 — Componentes lógicos PEP/PDP e sinais de decisão, com terminologia do NIST SP 800-207. Fonte: <code>assets/diagrams/zero-trust-flow.mmd</code>.</figcaption>
</figure>

### Identity and Access Flow

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/identity-access-flow.mmd"
```

<figcaption>Figura 4 — OpenID Connect com Authorization Code + PKCE, da autenticação à validação do token pela API. Fonte: <code>assets/diagrams/identity-access-flow.mmd</code>.</figcaption>
</figure>

### Hybrid Infrastructure

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/hybrid-infrastructure.mmd"
```

<figcaption>Figura 5 — On-premises e dois provedores de cloud com identidade e monitoramento centralizados. Fonte: <code>assets/diagrams/hybrid-infrastructure.mmd</code>.</figcaption>
</figure>

### Network Segmentation

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/network-segmentation.mmd"
```

<figcaption>Figura 6 — Zonas de borda, aplicação, dados e gestão, com travessias controladas. Fonte: <code>assets/diagrams/network-segmentation.mmd</code>.</figcaption>
</figure>

### Security Control Lifecycle

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/control-lifecycle.mmd"
```

<figcaption>Figura 7 — Do requisito à desativação documentada, com revisão periódica. Fonte: <code>assets/diagrams/control-lifecycle.mmd</code>.</figcaption>
</figure>

### Risk Management Process

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/risk-management-process.mmd"
```

<figcaption>Figura 8 — Processo iterativo inspirado na ISO 31000. Fonte: <code>assets/diagrams/risk-management-process.mmd</code>.</figcaption>
</figure>

### Architecture Decision Flow

<figure class="saa-diagram" markdown>

```mermaid
--8<-- "assets/diagrams/architecture-decision-flow.mmd"
```

<figcaption>Figura 9 — Do requisito ao ADR e ao design review. Fonte: <code>assets/diagrams/architecture-decision-flow.mmd</code>.</figcaption>
</figure>
