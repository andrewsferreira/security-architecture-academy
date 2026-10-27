---
title: Desenvolvimento local
description: Como executar, construir e validar o portal da Security Architecture Academy localmente em macOS e Linux.
---

# Desenvolvimento local

O portal é um site estático gerado pelo [Zensical](https://zensical.org/docs/). Não há banco de dados, backend ou Docker: basta Python.

## Pré-requisitos

| Ferramenta | Versão | Uso |
|:---|:---|:---|
| Python | 3.11 ou superior | Portal e scripts de validação (obrigatório) |
| Git | qualquer versão recente | Controle de versão (obrigatório) |
| GNU Make | qualquer versão | Atalhos de comandos (opcional — os comandos equivalentes estão abaixo) |
| Node.js | 20 ou superior | Markdown lint e validação de diagramas (opcional localmente; executados no CI) |

!!! tip "Windows"

    Use o [WSL 2](https://learn.microsoft.com/windows/wsl/) com uma distribuição Linux. Os comandos abaixo funcionam sem alteração.

## Instalação

=== "Com Make"

    ```bash
    git clone https://github.com/andrewsferreira/security-architecture-academy.git
    cd security-architecture-academy
    make install
    ```

=== "Sem Make"

    ```bash
    git clone https://github.com/andrewsferreira/security-architecture-academy.git
    cd security-architecture-academy
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements-dev.txt
    ```

As versões das dependências estão fixadas em `requirements.txt` para que o build local seja idêntico ao do CI.

## Comandos do dia a dia

| Objetivo | Com Make | Sem Make |
|:---|:---|:---|
| Pré-visualizar com recarga automática | `make serve` | `python -m zensical serve` |
| Build de produção (gera `site/`) | `make build` | `python -m zensical build --clean` |
| Validação completa | `make validate` | ver [Validações](#validacoes) |
| Testes dos scripts | `make test` | `python -m pytest -q tests` |
| Atualizar o Curriculum Roadmap | `make curriculum` | `python scripts/render_curriculum.py` |
| Listar todos os comandos | `make help` | — |

O servidor local fica disponível em <http://localhost:8000/security-architecture-academy/> — o caminho acompanha o `site_url` configurado.

## Validações

`make validate` executa, em ordem:

1. `scripts/check_structure.py` — arquivos obrigatórios, front matter, navegação, templates e README.
2. `scripts/validate_manifest.py` — coerência do `curriculum/manifest.yml` com as páginas e a navegação.
3. `scripts/render_curriculum.py --check` — a tabela do Curriculum Roadmap está sincronizada com o manifesto.
4. `scripts/check_assets.py` — integridade dos SVGs, dimensões dos PNGs e sincronização dos assets de marca.
5. `zensical build --clean` — build estático.
6. `scripts/check_links.py` — todos os links, imagens e âncoras internas do site gerado.

Com Node.js instalado, também estão disponíveis `make lint` (markdownlint) e `make diagrams` (sintaxe Mermaid).

## Atualizar conteúdo

- Páginas ficam em `docs/` e seguem o [Guia editorial](../internal/style-guide.md).
- Toda página nova precisa de front matter com `description` e de uma entrada em `nav` no `zensical.toml`.
- Novos módulos seguem o procedimento do [Modelo de conteúdo](../internal/content-model.md#adicionar-um-novo-modulo).

## Incluir imagens

1. Prefira SVG. Coloque o arquivo em `docs/assets/images/` com nome em kebab-case.
2. Para ilustrações com variante clara e escura, crie dois arquivos e use os sufixos `#only-light` e `#only-dark`.
3. Escreva texto alternativo descritivo — ver [Design System](../internal/design-system.md#imagens).

## Incluir diagramas

1. Crie a fonte em `assets/diagrams/<nome>.mmd`, com `accTitle` e `accDescr`.
2. Inclua na página:

    ````markdown
    ```mermaid
    ;--8<-- "assets/diagrams/<nome>.mmd"
    ```
    ````

3. Detalhes em [Padrões de diagramas](../internal/diagrams.md).

## Troubleshooting

??? question "`zensical: command not found`"

    O ambiente virtual não está ativo. Use `source .venv/bin/activate` ou os alvos do `make`, que localizam o Python do `.venv` automaticamente.

??? question "A página nova não aparece no menu"

    Toda página precisa estar em `nav` no `zensical.toml`. Páginas fora da navegação só são aceitas com `status: draft` ou `in-review` e são bloqueadas na publicação.

??? question "`check_links.py` aponta âncora inexistente"

    Âncoras são geradas a partir dos títulos, sem acentos (por exemplo, `## Critérios de publicação` vira `#criterios-de-publicacao`). Confira o link no site local passando o mouse sobre o símbolo de permalink ao lado do título.

??? question "Diagrama Mermaid não renderiza"

    Teste a sintaxe com `make diagrams` ou no [Mermaid Live Editor](https://mermaid.live/). Rótulos com parênteses, dois-pontos ou aspas precisam estar entre aspas duplas: `A["Rótulo (exemplo)"]`.

??? question "`render_curriculum.py --check` falhou no CI"

    O manifesto mudou, mas a página não foi regenerada. Execute `make curriculum` e faça commit do resultado.
