# Licenciamento

O projeto combina tipos de obra diferentes, e cada tipo usa a licença mais adequada a ele. Decisão do mantenedor registrada em 2026-10-23.

| Componente | Onde fica | Licença | Arquivo |
|:---|:---|:---|:---|
| **Conteúdo educacional** — aulas, exercícios, estudos de caso, avaliações, gabaritos, modelos para o estudante, diagramas e notas de pesquisa originais | `docs/` (exceto o indicado abaixo), `authoring/`, `assets/diagrams/`, `curriculum/`, `research/`, arquivos `.md` da raiz | [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt-br) | [`LICENSE`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/LICENSE) |
| **Código** — scripts, testes, código dos laboratórios, workflows, configuração e CSS | `scripts/`, `tests/`, `examples/`, `overrides/`, `.github/`, `Makefile`, `zensical.toml`, `docs/assets/stylesheets/` | [MIT](https://opensource.org/license/mit) | [`LICENSE-CODE`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/LICENSE-CODE) |
| **Identidade visual** — logotipos, símbolo, banners, social preview e favicons | `assets/branding/`, `docs/assets/branding/`, `docs/assets/images/hero-*` | Todos os direitos reservados | — |
| **Fontes Inter e JetBrains Mono** | `docs/assets/fonts/` | [SIL Open Font License 1.1](https://openfontlicense.org/) | junto aos arquivos |

## Por que essa combinação

- **CC BY 4.0 para o conteúdo.** É uma licença feita para obras textuais e visuais. Permite que o material seja usado em cursos, treinamentos internos de empresas, traduções e adaptações — inclusive comerciais —, exigindo apenas atribuição e a indicação de alterações. Atende ao objetivo da Academy: formar profissionais com o maior alcance possível.
- **MIT para o código.** Licenças de conteúdo como as Creative Commons não são recomendadas para software; a MIT é permissiva, curta e amplamente compreendida.
- **Marca reservada.** Impede que derivados usem a identidade visual de forma que sugira endosso da Academy. Quem adaptar o conteúdo deve usar outra identidade.

### Alternativas avaliadas

- **CC BY-SA 4.0:** garantiria que derivados permanecessem abertos, mas dificultaria o uso em materiais corporativos internos.
- **CC BY-NC 4.0:** impediria uso comercial — e, com isso, treinamentos dentro de empresas. Contrária ao objetivo do projeto.
- **MIT para tudo:** simples, mas licenças de software não tratam bem textos e diagramas.

## Como atribuir

Ao reutilizar o conteúdo, indique o título, o autor, a fonte, a licença e se houve alterações. Exemplo:

> "Arquitetura conceitual, lógica e física", de Andrews Ferreira — [Security Architecture Academy](https://github.com/andrewsferreira/security-architecture-academy), licenciado sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Adaptado: tradução para o inglês.

## O que a licença **não** cobre

A CC BY 4.0 só se aplica ao que é obra original deste projeto. Ela **não** cobre:

- **Obras de terceiros citadas ou referenciadas** — normas, frameworks, livros, white papers e documentação de provedores. Seguem os termos dos seus titulares, registrados em [`research/bibliography.yml`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/bibliography.yml). Acesso gratuito a um documento não significa permissão para redistribuí-lo.
- **Citações curtas** de terceiros, feitas com indicação de fonte para fins de estudo e crítica.
- **Marcas de terceiros** (ver abaixo).

Nenhum livro, norma ou documento integral de terceiros é distribuído neste repositório; cópias de pesquisa ficam em `private-research/`, que não é versionado.

## Recursos de terceiros incorporados

| Recurso | Uso | Licença | Arquivo de licença |
|:---|:---|:---|:---|
| [Inter](https://github.com/rsms/inter) (via Fontsource 5.3.0) | Tipografia do portal e texto convertido em curvas nos assets de marca | SIL OFL 1.1 | `docs/assets/fonts/LICENSE-Inter-OFL.txt` |
| [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono) (via Fontsource 5.3.0) | Tipografia de código no portal | SIL OFL 1.1 | `docs/assets/fonts/LICENSE-JetBrainsMono-OFL.txt` |
| [Lucide](https://lucide.dev/) | Ícones da interface, fornecidos pelo tema Zensical | ISC | distribuído com o Zensical |
| [Zensical](https://github.com/zensical/zensical) | Gerador do portal (dependência de build, não redistribuída) | MIT | — |
| Textos das licenças | `LICENSE`, `LICENSE-CODE` | Textos oficiais obtidos de [spdx/license-list-data](https://github.com/spdx/license-list-data) | — |

Todos os demais assets visuais (logotipos, banners, ilustrações e diagramas) são originais deste projeto.

## Marcas de terceiros

Nomes de organizações, normas e produtos (por exemplo NIST, ISO, ISC2, OWASP, CSA, SABSA, The Open Group, AWS, Microsoft, Google) são marcas de seus respectivos titulares e aparecem **apenas como referência**. O projeto não utiliza logotipos de terceiros e não declara afiliação, certificação, patrocínio ou endosso.
