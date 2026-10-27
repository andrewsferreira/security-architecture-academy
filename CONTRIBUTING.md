# Contribuindo com a Security Architecture Academy

Obrigado pelo interesse em contribuir. Este guia resume o essencial; os detalhes estão no [Fluxo de contribuição](docs/internal/workflow.md) do Handbook.

## Formas de contribuir

| Contribuição | Como começar |
|:---|:---|
| Corrigir um erro técnico ou de digitação | Pull Request direto, ou issue *Report a documentation error* |
| Sugerir conteúdo | Issue *Suggest new learning content* |
| Reportar link ou recurso quebrado | Issue *Report a broken resource* |
| Melhorar diagramas, padrões ou arquiteturas | Issue *Propose architecture improvements* |
| Reportar problema no site, build ou CI | Issue *Report technical problems* |
| Revisão técnica de módulos | Comente nos Pull Requests marcados com `type: content` |

## Antes de escrever

Leia, nesta ordem:

1. [Guia editorial](docs/internal/style-guide.md) — idioma, terminologia, exemplos e referências.
2. [Modelo de conteúdo](docs/internal/content-model.md) — templates, front matter, status e critérios de publicação.
3. [Design System](docs/internal/design-system.md) e [Padrões de diagramas](docs/internal/diagrams.md).

## Fluxo

```text
Issue → Branch → Pull Request → Validação automática → Review → Merge → Publicação
```

1. **Branch** no formato `<tipo>/<descrição>`: `content/`, `fix/`, `design/`, `ci/`, `docs/`.
2. **Commits** no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/): `feat(m05): adicionar aula sobre federação`.
3. **Valide localmente:**

    ```bash
    make install
    make validate   # estrutura, manifesto, assets, contraste, build e links
    make test       # testes dos scripts
    ```

4. **Pull Request** com o template preenchido. Um tema por PR.
5. **Review:** comentários indicam se são bloqueantes ou sugestões.
6. **Merge** por squash; a publicação no GitHub Pages é automática.

## Regras inegociáveis

- **Nenhum dado real:** sem credenciais (mesmo revogadas), dados pessoais, informações de empregadores ou sistemas de terceiros. Use `example.com` e as faixas de IP de documentação (RFC 5737).
- **Nada anunciado antes de pronto:** status editoriais refletem o estado real.
- **Fontes rastreáveis:** afirmações normativas com referência, versão e data.
- **Sem logotipos de terceiros** e sem sugestão de afiliação ou endosso.
- **Conteúdo original:** não copie trechos extensos de normas, livros ou cursos.

## Licença das contribuições

Ao abrir um Pull Request, você concorda que sua contribuição seja distribuída sob a licença do tipo de arquivo correspondente: [CC BY 4.0](LICENSE) para conteúdo educacional e [MIT](LICENSE-CODE) para código (detalhes em [LICENSING.md](LICENSING.md)). Não inclua material de terceiros que você não tenha direito de licenciar.

## Código de Conduta

Este projeto segue o [Código de Conduta](CODE_OF_CONDUCT.md). Ao participar, você concorda em respeitá-lo.
