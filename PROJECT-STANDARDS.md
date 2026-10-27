# Padrões do projeto

Regras editoriais, técnicas e de publicação da Security Architecture Academy. **Leia este documento antes de contribuir.** A plataforma já existe: os próximos trabalhos produzem conteúdo sobre ela, sem recriá-la. O fluxo de contribuição está em [`docs/internal/workflow.md`](docs/internal/workflow.md) e o modelo de conteúdo em [`docs/internal/content-model.md`](docs/internal/content-model.md).

## Objetivo do projeto

**Security Architecture Academy** — formação aberta, gratuita e progressiva em Arquitetura de Segurança da Informação (Enterprise, Cloud e Hybrid), em português brasileiro com terminologia técnica em inglês. Repositório: `github.com/andrewsferreira/security-architecture-academy`. Portal: `https://andrewsferreira.github.io/security-architecture-academy/`.

**Estado e planejamento:** o estado por entrega e o plano de releases ficam no repositório de desenvolvimento; o roadmap público está em [`ROADMAP.md`](ROADMAP.md).

**Fluxo obrigatório:** todo conteúdo é revisado pelo mantenedor **antes** de qualquer publicação. Nenhum push ao repositório público, alteração de configuração do GitHub ou deploy acontece sem aprovação expressa do mantenedor.

## Modelo de publicação e isolamento

- O repositório público recebe **somente** árvores geradas por `scripts/export_release.py` (allowlist `curriculum/public-allowlist.yml` + escopo da release, com `RELEASE-MANIFEST.yml` verificado por `scripts/verify_release_manifest.py`) (`make release-candidate` / `make release-export RELEASE=Rn`) com o escopo cumulativo das releases aprovadas. Nunca enviar ao repositório público — em nenhuma branch — conteúdo em desenvolvimento ou em revisão; ocultar da `nav` não é isolamento.
- Desenvolvimento e histórico completo ficam no repositório de desenvolvimento **privado** (`andrewsferreira/security-architecture-academy-dev`). O repositório público tem histórico próprio e nunca recebe objetos Git do desenvolvimento.
- `approved_by`/`approved_on` da release e `reviewed_by` das páginas só são preenchidos com aprovação expressa do mantenedor. A exportação final falha sem eles.
- `published_on` e `url` da release só depois de o deploy ter sido executado e a URL conferida.
- Rollback sem operações destrutivas: `git revert` + novo deploy, ou *patch*; nunca force push.
- Procedimento completo: [`docs/internal/workflow.md`](docs/internal/workflow.md#8-releases-e-publicacao).

## Autoria e créditos

- O projeto é mantido sob a conta do proprietário. Nenhum arquivo, página compilada, mensagem de commit, tag, nota de release ou metadado sob controle do projeto apresenta assistentes ou ferramentas de IA como autores, coautores, colaboradores, revisores ou geradores do conteúdo — inclusive trailers `Co-authored-by`, "Generated with…" ou equivalentes.
- Arquivos de configuração ou de instrução de ferramentas de automação e de assistentes de código ficam fora do versionamento; a verificação automática bloqueia a inclusão deles. Regras duradouras e neutras vivem neste documento.
- Commits usam somente a identidade Git real e autorizada de quem os assina; nunca se falsifica autor, e-mail ou histórico.
- A ausência desses créditos não autoriza afirmar que nenhuma ferramenta foi usada nem que houve revisão humana independente que não ocorreu.
- Atribuições, licenças e referências exigidas por materiais de terceiros são sempre preservadas. O ensino de segurança de IA e a citação técnica de produtos são legítimos.
- Verificação: `scripts/check_attribution.py` (arquivos versionados, `--commits` para mensagens e autores, `--path` para a árvore exportada e o site compilado). Roda em `make check`, no CI e na exportação de releases; ocorrências legítimas que casem com as expressões de crédito vão para `scripts/attribution_allowlist.yml`, com justificativa.

## Arquitetura de diretórios

| Caminho | Conteúdo | Regras |
|:---|:---|:---|
| `docs/` | Páginas do portal | Toda página tem `description` e entrada em `nav`. `draft` nunca em `nav`; `in-review` em `nav` só em branch (deploy bloqueia). |
| `docs/modules/NN-<slug>/` | Módulo e aulas | Padrão de aula de 14 elementos (`authoring/technical-lesson.md`). |
| `docs/case-studies/`, `docs/labs/`, `docs/assessments/` | Atividades | Gabaritos sempre em `docs/assessments/answers/`; soluções de caso em `solution.md`. |
| `docs/artifacts/` | Modelos **para o estudante** (ADR, requisitos, revisão) | Não confundir com `authoring/`. Nunca usar `docs/templates/`: o Zensical ignora essa pasta (verificado por `check_structure.py`). |
| `docs/internal/` | Handbook (Design System, guia editorial, modelo de conteúdo, diagramas, componentes, workflow) | Referência normativa — atualize junto com o código. |
| `docs/assets/` | CSS, fontes, imagens, cópia dos assets de marca | `branding/` é cópia de `assets/branding/` — nunca edite direto. |
| `curriculum/manifest.yml` | Fonte única do currículo (schema v2) e dos status | Validado por `scripts/validate_manifest.py` (`--release` no deploy). |
| `research/` | Research Library: `bibliography.yml` (IDs estáveis, acesso, redistribuição, verificação, capítulos), `knowledge-map.yml`, `notes/`, plano de leitura e registro de verificação | Validada por `scripts/validate_references.py`. Nunca inventar capítulo, página, versão, ISBN ou permissão — use `Pending`. `consulted: true` só para trecho efetivamente lido. Aulas citam IDs em `sources` (base, só fontes verificadas) e `further_reading` (complementares). |
| `private-research/` | Cópias locais de obras de terceiros | Ignorada pelo git; nunca versionar PDFs/EPUBs (verificado). |
| `examples/` | Código dos laboratórios, com testes | Rodam no CI (`pytest tests examples`). |
| `CURRICULUM.md` | Currículo completo | **Gerado** por `render_curriculum.py` — não editar. |
| `authoring/` | 13 templates de autoria | Fora de `docs/` para não serem publicados. |
| `assets/branding/` | Marca (fonte) | Gerada por `scripts/build_brand.py`; não editar SVGs à mão. |
| `assets/diagrams/` | Fontes Mermaid `.mmd` | Incluídas nas páginas via snippets; nunca copiar o diagrama para a página. |
| `includes/abbreviations.md` | Siglas com tooltip em todo o portal | Anexado automaticamente; manter em ordem alfabética. |
| `overrides/main.html` | Extensão mínima do tema (Open Graph, título da home) | Não sobrescrever blocos visuais do tema. |
| `scripts/` | Validações e geradores | Python 3.11+, apenas stdlib + PyYAML. |
| `tests/` | Testes dos scripts | `make test`. |

Diretórios de conteúdo futuros (`docs/complements/`, `docs/architecture-patterns/`, `docs/reference-architectures/`, `docs/glossary/`) **são criados apenas com o primeiro conteúdo real**. Estrutura detalhada em `docs/internal/content-model.md`.

## Stack

- **Zensical 0.0.71** (`zensical.toml`, tema `modern`, idioma `pt-BR`), fixado em `requirements.txt`.
- Python-Markdown + PyMdown Extensions (admonitions, tabs, superfences/Mermaid, snippets, tasklist, emoji/ícones Lucide).
- Mermaid é carregado pelo tema sob demanda (CDN unpkg, `mermaid@11`).
- Fontes Inter e JetBrains Mono auto-hospedadas (`theme.font = false`).
- GitHub Actions: `ci.yml` (PR e push: validações, build, testes), `pages.yml` (deploy **somente manual**, `workflow_dispatch` com confirmação "publicar", restrito à `main` — nunca reativar gatilho em push sem autorização do mantenedor), `links.yml` (links externos e registro bibliográfico, semanal). Actions fixadas por SHA.

## Comandos

```bash
make install      # .venv + requirements-dev.txt
make serve        # http://localhost:8000/security-architecture-academy/
make build        # site/
make check        # estrutura, manifesto, páginas geradas, assets, contraste, matrizes de decisão, Research Library, atribuição
make validate     # check + build + links internos
make test         # pytest tests examples
make lint         # markdownlint (Node.js)
make diagrams     # sintaxe Mermaid (Node.js + Chrome)
make curriculum   # regenera CURRICULUM.md e as páginas geradas do currículo e da Research Library
make references   # relatório de cobertura bibliográfica
make brand        # regenera a marca (requirements-brand.txt + fontes Inter OTF)
make release-candidate RELEASE=R1  # árvore pública candidata em build/, validada
make release-export RELEASE=R1     # árvore final (exige aprovação e commit aprovado registrados no manifesto)
```

**Antes de concluir qualquer tarefa:** `make validate && make test && make lint` sem erros.

## Padrões visuais

- Tokens em `docs/assets/stylesheets/extra.css`; documentação em `docs/internal/design-system.md`.
- Use apenas tokens semânticos (`--saa-primary`, `--saa-text-muted`…), nunca hex em componentes. Classes próprias com prefixo `.saa-`.
- Prefira recursos nativos do tema (grid cards, admonitions, tabs) a CSS novo.
- Ícones: somente Lucide (`:lucide-nome:`), conforme a tabela de ícones por domínio. Sem emojis em conteúdo.
- Status editorial: `<span class="saa-status saa-status--published">Published</span>`; nível: `<span class="saa-level">Professional</span>`.
- Contraste mínimo AA verificado por `scripts/check_contrast.py`.

## Convenções de Markdown

- Front matter obrigatório: `title`, `description`; conteúdo educacional segue os campos dos templates (`id`, `domain`, `tier`, `status`, `prerequisites`, `objectives`, `last_updated`, `reviewed_by`).
- Metadados no topo de aulas, labs e avaliações: `<div class="saa-lesson-meta" markdown>` com `.saa-level`, `.saa-tier saa-tier--fundamental|professional|architect` e `.saa-meta`.
- Matrizes de decisão: coluna `Peso` e última linha `**Total ponderado**`; os totais são recalculados por `check_decision_matrices.py`.
- Respostas de questões em `??? success`; gabaritos de avaliação em arquivo separado, com alternativas corretas distribuídas entre as letras.
- Um H1 por página, hierarquia sem saltos, links relativos para `.md`.
- Listas aninhadas com 4 espaços; grid cards com hífen seguido de 3 espaços.
- Para mostrar a sintaxe de snippet dentro de blocos de código, escape com `;--8<--`.
- Idioma e terminologia: `docs/internal/style-guide.md` (obrigatório).

## Padrões de Mermaid

- Fonte em `assets/diagrams/<nome-kebab>.mmd`, com `accTitle:` e `accDescr:` (verificado).
- Inclusão: bloco ` ```mermaid ` contendo `--8<-- "assets/diagrams/<nome>.mmd"`.
- Subgraphs = trust boundaries/zonas; aplique `classDef zone fill:transparent,…` (sem fill, para funcionar no modo escuro).
- Classes semânticas apenas com contorno: `identity` `#2f74e8`, `control` `#0e9fb8`, `actor` `#64748b`, `untrusted` `#dc2626` tracejado.
- Diagramas de conteúdo dentro de `<figure class="saa-diagram" markdown>` com `<figcaption>Figura N — …</figcaption>`.
- O diagrama do README é cópia de `assets/diagrams/learning-journey.mmd` marcada com `<!-- source: … -->`; `check_structure.py` exige que sejam idênticos.

## Como adicionar um módulo

Procedimento completo em `docs/internal/content-model.md#adicionar-um-novo-modulo`. Resumo:

1. Página em `docs/modules/NN-<slug>/index.md` a partir de `authoring/module-overview.md`; aulas a partir de `authoring/technical-lesson.md`.
2. Manifesto: `status: draft` + `path` no módulo; `file` + `status` em cada aula. Rascunhos ficam **fora** de `nav`.
3. Revisão: `in-review` na página e no manifesto; páginas entram na `nav` da branch. Entregar ao mantenedor para revisão.
4. Publicação (só após aprovação): `published`, `published_on`, `reviewed_by`, sem marcadores `{{ … }}`/`TODO`/`TBD`.
5. `make curriculum && make check && make validate && make test`.

O workflow de deploy roda `check_structure.py --release` e `validate_manifest.py --release`, que falham com qualquer conteúdo não publicado.

## Como incluir assets

- Imagens de conteúdo: SVG em `docs/assets/images/`, kebab-case, texto alternativo descritivo; variantes `#only-light`/`#only-dark` quando necessário.
- Marca: alterar `scripts/build_brand.py` e rodar `make brand` (gera fonte e cópia sincronizada). `check_assets.py` falha se a cópia divergir.
- Assets de terceiros: só com licença compatível, registrada em `LICENSING.md`. Nunca logotipos de organizações (NIST, ISC2, AWS, Microsoft…).

## Validação de links e navegação

- `scripts/check_links.py` verifica href/src/âncoras internos no `site/` (inclui o caminho base do Pages).
- `scripts/check_structure.py` verifica que toda entrada de `nav` existe e que nenhuma página publicada está fora de `nav`.
- Links externos: workflow `links.yml` (não bloqueia PR).

## Regras de publicação e integridade

1. **Nunca** marcar conteúdo como `published` sem os critérios de `content-model.md#criterios-de-publicacao`.
2. **Nunca** criar páginas vazias, placeholders publicados, avaliações ou laboratórios fictícios apresentados como concluídos.
3. **Nunca** usar dados reais, credenciais (mesmo revogadas), dados pessoais ou informações de empregadores. Use `example.com`, RFC 5737/3849.
4. **Nunca** sugerir afiliação, certificação ou endosso de terceiros.
5. Afirmações normativas sempre com fonte, versão e data; diferenciar requisito, boa prática e opinião.
6. Licenças (decididas em 2026-10-23): conteúdo **CC BY 4.0** (`LICENSE`), código **MIT** (`LICENSE-CODE`), marca com todos os direitos reservados. Não alterar sem decisão do mantenedor. Nunca versionar obras de terceiros integrais — cópias de pesquisa só em `private-research/` (ignorado pelo git).
7. Não usar `force push`, não reescrever histórico da `main`, não alterar remotes existentes.
8. Atualizar `CHANGELOG.md` (seção *Unreleased*) a cada mudança relevante.

## Decisões arquiteturais

| Decisão | Motivo |
|:---|:---|
| Zensical em vez de MkDocs + Material | Sucessor oficial, compatível com a sintaxe Material, build rápido. |
| Templates de autoria em `authoring/` | Evitar que sejam publicados; `docs/artifacts/` fica para modelos do estudante. |
| `in-review` permitido na `nav` de branch | Revisão navegável no portal local; o deploy continua bloqueado. |
| Gabaritos em arquivos separados | O estudante tenta antes de ver a resposta. |
| Laboratórios com código e testes em `examples/` | `tested: true` só é afirmado com execução real. |
| Manifesto YAML + página gerada | Status com fonte única, verificável no CI. |
| Fontes auto-hospedadas | Privacidade (sem requisições a terceiros) e desempenho. |
| Texto da marca convertido em curvas | Renderização idêntica no GitHub e em qualquer visualizador. |
| Mermaid via snippets de `assets/diagrams/` | Fonte única, validável com mermaid-cli. |
| Rascunhos bloqueados no deploy | Garante que só conteúdo revisado chega ao site. |
