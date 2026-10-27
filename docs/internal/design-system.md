---
title: Design System
description: Identidade visual, tokens de cor, tipografia, espaçamento, componentes e regras de acessibilidade da Security Architecture Academy.
---

# Design System

Este documento é a **referência obrigatória** para qualquer página, diagrama ou asset do projeto. Ele garante que conteúdos produzidos em momentos diferentes, por pessoas diferentes, mantenham a mesma identidade.

!!! abstract "Fontes da verdade"

    | O quê | Arquivo |
    |:---|:---|
    | Tokens de cor, espaçamento e componentes | `docs/assets/stylesheets/extra.css` |
    | Geração dos assets de marca | `scripts/build_brand.py` |
    | Fontes de diagramas | `assets/diagrams/*.mmd` |
    | Configuração do tema | `zensical.toml` |

    Se este documento e o código divergirem, o código vale — e este documento deve ser corrigido no mesmo Pull Request.

## Brand Guidelines

### Conceito

A identidade comunica **engenharia, precisão e confiança**, com a sobriedade de documentação corporativa. O símbolo representa três ideias centrais da arquitetura de segurança:

<div class="grid" markdown>

<div class="card" markdown>

![Símbolo da Security Architecture Academy para fundos claros](../assets/branding/symbol-light.svg){ width="64" height="64" }

**Camadas concêntricas** — defesa em profundidade: controles independentes e sobrepostos.

</div>

<div class="card" markdown>

![Símbolo da Security Architecture Academy para fundos escuros](../assets/branding/icon.svg){ width="64" height="64" }

**Fronteira interrompida** — o trust boundary externo tem pontos de travessia explícitos (os nós), nunca abertos por omissão.

</div>

<div class="card" markdown>

![Logotipo horizontal da Security Architecture Academy](../assets/branding/logo-light.svg#only-light){ height="48" }
![Logotipo horizontal da Security Architecture Academy](../assets/branding/logo-dark.svg#only-dark){ height="48" }

**Núcleo destacado** — o ativo protegido, em cyan, é a única cor de destaque do símbolo.

</div>

</div>

### Assets

| Asset | Arquivo | Uso |
|:---|:---|:---|
| Logotipo (padrão) | `assets/branding/logo.svg` | Fundos claros; equivale a `logo-light.svg` |
| Logotipo para fundos claros | `assets/branding/logo-light.svg` | Documentos, slides, GitHub em modo claro |
| Logotipo para fundos escuros | `assets/branding/logo-dark.svg` | Fundos navy ou escuros |
| Isotipo (ícone) | `assets/branding/icon.svg` | Avatares, favicons, espaços quadrados |
| Símbolo sem fundo | `assets/branding/symbol-{light,dark}.svg` | Header do portal, composições |
| Banner | `assets/branding/banner{,-light,-dark}.svg` | README (1280×400) |
| Social Preview | `assets/branding/social-preview.png` | GitHub e Open Graph (1280×640) |
| Favicon | `assets/branding/favicon.png`, `apple-touch-icon.png` | Navegadores e dispositivos |

### Regras de uso

- **Faça:** mantenha uma área de respiro ao redor do logotipo de no mínimo metade da altura do símbolo.
- **Faça:** use a versão `-dark` sobre fundos escuros e a `-light` sobre fundos claros.
- **Não faça:** alterar cores, proporções, rotacionar, aplicar sombras ou contornos.
- **Não faça:** combinar o logotipo com marcas de terceiros de forma que sugira parceria ou endosso.
- **Não faça:** editar os SVGs manualmente — altere `scripts/build_brand.py` e regenere com `make brand`.

!!! info "Texto em curvas"

    Todo texto dos assets de marca é convertido em curvas pelo script de geração. Assim os SVGs renderizam igual no GitHub, no portal e em qualquer visualizador, sem depender de fontes instaladas.

## Color Palette

### Paleta de marca

| Token | Hex | Papel |
|:---|:---|:---|
| `--saa-navy-950` | `#081426` | Fundo mais profundo, rodapé escuro |
| `--saa-navy-900` | `#0C1D36` | **Cor institucional**: botões primários, banners, social preview |
| `--saa-navy-800` | `#132B4F` | Secondary (modo claro) |
| `--saa-navy-700` | `#1B3A68` | Variação de header e superfícies escuras |
| `--saa-blue-600` | `#1E5EC8` | **Primary** no modo claro: links, botões |
| `--saa-blue-500` | `#2F74E8` | Azul técnico: camadas e destaques gráficos |
| `--saa-blue-400` | `#5B93F0` | Fronteiras no símbolo sobre fundo escuro |
| `--saa-blue-300` | `#8DB4F5` | **Primary** no modo escuro |
| `--saa-cyan-700` | `#0A7083` | **Accent** no modo claro (AA também sobre o fundo do item ativo da navegação) |
| `--saa-cyan-600` | `#0B7F93` | Variação de apoio |
| `--saa-cyan-400` | `#2CC4DA` | **Accent** no modo escuro e núcleo do símbolo |
| `--saa-slate-*` | `#0F172A` a `#F1F5F9` | Texto, bordas e superfícies neutras |
| `--saa-off-white` | `#F7F9FC` | Surface no modo claro |

### Tokens semânticos

Componentes usam **apenas tokens semânticos**, que mudam automaticamente entre os modos:

| Token | Light | Dark | Uso |
|:---|:---|:---|:---|
| `--saa-bg` | `#FFFFFF` | `#0A1424` | Fundo da página |
| `--saa-surface` | `#F7F9FC` | `#0F1D33` | Cabeçalhos de tabela, blocos neutros |
| `--saa-surface-raised` | `#FFFFFF` | `#132440` | Cards |
| `--saa-text` | `#0F172A` | `#E6EBF3` | Texto principal |
| `--saa-text-muted` | `#475569` | `#A3B1C6` | Texto secundário, legendas |
| `--saa-primary` | `#1E5EC8` | `#8DB4F5` | Links, ações, foco de seleção |
| `--saa-secondary` | `#132B4F` | `#CBD5E1` | Rótulos de nível |
| `--saa-accent` | `#0B7F93` | `#2CC4DA` | Destaques, foco visível |
| `--saa-border` | `#E2E8F0` | `#22385A` | Bordas e divisores |
| `--saa-success` | `#15803D` | `#4ADE80` | Status positivo |
| `--saa-warning` | `#B45309` | `#FBBF24` | Atenção |
| `--saa-error` | `#B91C1C` | `#F87171` | Erro, descontinuado |
| `--saa-info` | `#1E5EC8` | `#8DB4F5` | Informação |

### Contraste (WCAG 2.x)

Valores calculados por `scripts/check_contrast.py`, que lê os tokens do CSS e **falha o CI** se algum par ficar abaixo de AA (4.5:1):

| Modo | Par | Cores | Contraste | Nível |
|:---|:---|:---|:---|:---|
| Light | Texto | `#0f172a` / `#ffffff` | 17.9:1 | AAA |
| Light | Texto secundário | `#475569` / `#ffffff` | 7.6:1 | AAA |
| Light | Link / Primary | `#1e5ec8` / `#ffffff` | 6.0:1 | AA |
| Light | Accent | `#0a7083` / `#ffffff` | 5.7:1 | AA |
| Light | Success | `#15803d` / `#ffffff` | 5.0:1 | AA |
| Light | Warning | `#b45309` / `#ffffff` | 5.0:1 | AA |
| Light | Error | `#b91c1c` / `#ffffff` | 6.5:1 | AA |
| Light | Texto secundário sobre surface | `#475569` / `#f7f9fc` | 7.2:1 | AAA |
| Light | Texto sobre Navy 900 (botão primário) | `#ffffff` / `#0c1d36` | 16.9:1 | AAA |
| Light | Accent sobre item ativo da navegação | `#0a7083` / `#e6f1f3` | 5.0:1 | AA |
| Dark | Texto | `#e6ebf3` / `#0a1424` | 15.4:1 | AAA |
| Dark | Texto secundário | `#a3b1c6` / `#0a1424` | 8.5:1 | AAA |
| Dark | Link / Primary | `#8db4f5` / `#0a1424` | 8.8:1 | AAA |
| Dark | Accent | `#2cc4da` / `#0a1424` | 8.8:1 | AAA |
| Dark | Success | `#4ade80` / `#0a1424` | 10.6:1 | AAA |
| Dark | Warning | `#fbbf24` / `#0a1424` | 11.0:1 | AAA |
| Dark | Error | `#f87171` / `#0a1424` | 6.7:1 | AA |
| Dark | Texto secundário sobre surface | `#a3b1c6` / `#132440` | 7.1:1 | AAA |

## Typography

| Família | Uso | Licença | Entrega |
|:---|:---|:---|:---|
| **Inter** (400, 500, 600, 700, 400 itálico) | Interface e texto | SIL OFL 1.1 | Auto-hospedada em `docs/assets/fonts/` |
| **JetBrains Mono** (400, 500) | Código, identificadores, caminhos | SIL OFL 1.1 | Auto-hospedada em `docs/assets/fonts/` |
| **Inter Display** | Títulos dos assets de marca (convertidos em curvas) | SIL OFL 1.1 | Apenas na geração dos assets |

As fontes são servidas pelo próprio site (`theme.font = false`): **nenhuma requisição a serviços de terceiros**, o que melhora privacidade e desempenho. Somente o subconjunto *latin* é incluído (cobre o português).

| Papel | Tamanho | Peso | Observações |
|:---|:---|:---|:---|
| Hero Heading | `clamp(1.9rem, 4.2vw, 2.7rem)` | 700 | Apenas na homepage; tracking −0.03em |
| Page Title (H1) | padrão do tema | 700 | Um por página; tracking −0.02em |
| Section Title (H2) | padrão do tema | 650 | Espaço superior ampliado (2.2em) |
| Subsection (H3/H4) | padrão do tema | 600 | Sem caixa-alta |
| Body Text | 0.82rem | 400 | Altura de linha 1.7 |
| Lead | 0.98rem | 400 | Parágrafo de abertura, cor secundária |
| Captions | 0.72rem | 400 | `figcaption`, cor secundária |
| Tables | 0.74rem | 400 / 600 no cabeçalho | |
| Eyebrow / rótulos | 0.62–0.68rem | 600 | Caixa-alta com tracking 0.12–0.14em |
| Code | padrão do tema | 400 | Ligaduras desativadas |

## Spacing Scale

Escala de base 4 px, exposta como tokens `--saa-space-*`:

| Token | Valor | Uso típico |
|:---|:---|:---|
| `--saa-space-1` | 0.25rem | Ajustes finos |
| `--saa-space-2` | 0.5rem | Espaço entre rótulo e conteúdo |
| `--saa-space-3` | 0.75rem | Gap entre botões |
| `--saa-space-4` | 1rem | Padding de cards |
| `--saa-space-6` | 1.5rem | Separação entre blocos |
| `--saa-space-8` | 2rem | Seções da homepage |
| `--saa-space-12` | 3rem | Respiro amplo |
| `--saa-space-16` | 4rem | Reservado |

Raios: `--saa-radius-sm` 6 px (botões, tabelas), `--saa-radius-md` 10 px (cards), `--saa-radius-lg` 16 px (ilustrações).

## Grid

- Conteúdo: largura máxima do tema; a homepage amplia para 70rem.
- Cards usam o grid nativo (`.grid.cards`), responsivo e sem CSS adicional de layout.
- A trilha de níveis (`.saa-journey`) usa 3 colunas e passa a 1 coluna abaixo de 720 px.
- O hero usa 2 colunas e empilha (ilustração acima) abaixo de 960 px.

## Icons

- Conjunto único: **Lucide**, fornecido pelo tema, sintaxe `:lucide-nome:`.
- Ícones têm função de reconhecimento rápido, nunca são a única forma de transmitir informação.
- Use o mesmo ícone para o mesmo conceito em todo o portal:

| Conceito | Ícone | Conceito | Ícone |
|:---|:---|:---|:---|
| Security Foundations | :lucide-layers: `lucide-layers` | Cloud Security | :lucide-cloud: `lucide-cloud` |
| GRC | :lucide-scale: `lucide-scale` | Hybrid & Multicloud | :lucide-git-fork: `lucide-git-fork` |
| IAM | :lucide-fingerprint: `lucide-fingerprint` | Application Security | :lucide-code-xml: `lucide-code-xml` |
| Zero Trust | :lucide-shield-check: `lucide-shield-check` | Data Security | :lucide-database: `lucide-database` |
| Network Security | :lucide-network: `lucide-network` | Vulnerability Management | :lucide-radar: `lucide-radar` |
| Enterprise Architecture | :lucide-building-2: `lucide-building-2` | Laboratório | :lucide-flask-conical: `lucide-flask-conical` |

- Emojis decorativos não são usados em páginas de conteúdo.

## Cards

Use os grid cards nativos. Estrutura padrão:

```markdown
<div class="grid cards" markdown>

-   :lucide-cloud:{ .lg .saa-card-icon } **Título do card**

    ---

    Uma ou duas frases. Sem listas longas dentro de cards.

</div>
```

Regras: um card = uma ideia; título com no máximo 5 palavras; textos de tamanho semelhante dentro de um mesmo grid.

## Documentation Components

O catálogo completo, com exemplos renderizados, está na [Referência de componentes](components.md). Resumo do uso de admonitions:

| Tipo | Quando usar |
|:---|:---|
| `note` | Informação complementar |
| `info` | Contexto sobre status ou escopo |
| `tip` | Recomendação prática |
| `warning` | Risco de erro conceitual ou operacional |
| `danger` | Ação que pode causar dano real (nunca execute em produção etc.) |
| `example` | Cenário ilustrativo |
| `abstract` | Resumo de seção ou de aula |
| `question` | Exercício ou pergunta de reflexão |
| `quote` | Citação de norma (curta, com referência) |

### Status e nível

Status editorial e nível sempre têm **texto visível** (não dependem só de cor):

<span class="saa-status saa-status--planned">Planned</span>
<span class="saa-status saa-status--draft">Draft</span>
<span class="saa-status saa-status--published">Published</span>
<span class="saa-status saa-status--published">Published</span>
<span class="saa-status saa-status--deprecated">Deprecated</span>
<span class="saa-level">Fundamentals</span>

```html
<span class="saa-status saa-status--published">Published</span>
<span class="saa-level">Professional</span>
```

## Diagrams

Padrões completos em [Padrões de diagramas](diagrams.md). Paleta semântica dos diagramas (cores de contorno, que funcionam nos dois modos):

| Classe | Cor | Significado |
|:---|:---|:---|
| `identity` | `#2F74E8` | Identidades, IdP, decisões de acesso |
| `control` | `#0E9FB8` | Controles de segurança, pontos de inspeção |
| `actor` | `#64748B` | Pessoas e sistemas externos |
| `untrusted` | `#DC2626` tracejado | Zonas ou origens não confiáveis |

## Code Presentation

- Sempre declarar a linguagem do bloco (` ```yaml `, ` ```bash `, ` ```text ` quando não houver).
- Usar `title="arquivo.ext"` quando o arquivo de origem importa.
- Anotações de código (`# (1)!`) para explicar linhas específicas, em vez de comentários longos.
- Valores sensíveis sempre fictícios e explícitos: `example.com`, `203.0.113.0/24`, `AKIAEXAMPLE…`.

## Tables

- Cabeçalho obrigatório; alinhar à esquerda (`:---`).
- Até 5 colunas; acima disso, dividir a tabela ou usar tabs.
- Primeira coluna identifica a linha (é lida primeiro por leitores de tela).
- Não usar tabela para layout.

## Responsive Behavior

| Largura | Comportamento |
|:---|:---|
| ≥ 1220 px | Navegação em abas, sidebar e índice da página visíveis |
| 960–1219 px | Índice da página recolhido |
| 720–959 px | Hero em coluna única |
| < 720 px | Menu em gaveta, trilha de níveis em coluna única, tabelas com rolagem horizontal |

## Accessibility

- Contraste mínimo AA verificado automaticamente (ver [tabela](#contraste-wcag-2x)).
- Foco visível em todos os elementos interativos (`:focus-visible` com contorno accent).
- Hierarquia de títulos sem saltos (H1 → H2 → H3).
- Todo diagrama tem `accTitle` e `accDescr`; toda imagem tem texto alternativo.
- Animações respeitam `prefers-reduced-motion`.
- Siglas ganham tooltip automático via `includes/abbreviations.md`.
- Estado nunca é comunicado só por cor: status sempre tem texto.
- `docs/assets/javascripts/a11y.js` corrige a marcação gerada pelo tema: rótulo acessível nas caixas de checklist (o texto do item), nos marcadores de anotação de código e foco por teclado em tabelas com rolagem horizontal. Âncoras por linha de código ficam desativadas (`anchor_linenums = false`) porque geram links sem texto.

**Auditoria (2026-10-23):** axe-core 4.10.3, regras WCAG 2.0/2.1 A e AA, 18 páginas representativas nos modos claro e escuro (36 renderizações) — **nenhuma violação**. A auditoria inicial encontrou quatro problemas, todos corrigidos: contraste do item ativo da navegação (4,1:1 → 5,0:1, com o token `--saa-cyan-700`), links de linha de código sem texto, checkboxes sem rótulo e regiões roláveis sem acesso por teclado. Testes automatizados não substituem a revisão com leitor de tela, que continua pendente.

## Light/Dark Mode

- O portal segue a preferência do sistema e permite alternar manualmente (três estados: sistema, claro, escuro).
- Componentes usam tokens semânticos — nunca hex direto no CSS de componentes.
- Ilustrações com variante própria usam `#only-light` / `#only-dark`.
- Diagramas Mermaid herdam as cores do tema; classes semânticas definem apenas contorno.

## Imagens

- **Formato:** SVG para ilustrações e diagramas exportados; PNG apenas quando exigido (social preview, favicon); fotografias não são usadas.
- **Nome:** kebab-case descritivo — `zero-trust-pep-pdp.svg`, nunca `image1.svg`.
- **Local:** `docs/assets/images/` (conteúdo) ou `assets/branding/` (marca).
- **Texto alternativo:** descreve o que a imagem comunica, não sua aparência ("Fluxo de autenticação com IdP central…", não "diagrama azul").
- **Legenda:** obrigatória em diagramas de conteúdo, via `<figure>` + `<figcaption>`.
- **Proibido:** imagens genéricas de cadeados, hackers encapuzados, logotipos de terceiros, imagens sem licença compatível.
