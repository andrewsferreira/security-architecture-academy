# Contribuindo com a Security Architecture Academy

Obrigado pelo interesse em contribuir. Este guia resume como as contribuições chegam ao portal.

## Como o projeto é publicado

O conteúdo é produzido e revisado em um repositório de desenvolvimento. Este repositório recebe **somente** as versões publicadas, exportadas e verificadas (cada arquivo tem o SHA-256 registrado em `RELEASE-MANIFEST.yml`). Por isso, nenhuma alteração entra diretamente na `main` daqui: as propostas são incorporadas pelo mantenedor no desenvolvimento, revisadas e publicadas na versão seguinte — por exemplo, uma versão de correção `v0.1.x`.

## Formas de contribuir

| Contribuição | Como começar |
|:---|:---|
| Corrigir um erro técnico ou de digitação | Issue *Report a documentation error* — ou um Pull Request como proposta, que será incorporada pelo mantenedor |
| Sugerir conteúdo | Issue *Suggest new learning content* |
| Reportar link ou recurso quebrado | Issue *Report a broken resource* |
| Melhorar diagramas, padrões ou arquiteturas | Issue *Propose architecture improvements* |
| Reportar problema no site, build ou CI | Issue *Report technical problems* |
| Revisão técnica de módulos | Comente na issue ou no Pull Request do tema |

## Antes de escrever

- **Idioma:** português do Brasil; termos técnicos consolidados ficam em inglês, com explicação em português na primeira ocorrência da página.
- **Exemplos:** empresas, pessoas, endereços e números fictícios; domínios `example.com` e faixas de documentação (RFC 5737).
- **Fontes:** afirmações normativas com a fonte primária, a versão e a data de verificação.
- **Aulas:** cite outras aulas pelo nome público ("Módulo 1 — Aula 02"); os IDs técnicos (`M01-L02`) ficam nos metadados.
- **Diagramas:** Mermaid com `accTitle` e `accDescr`, legíveis nos modos claro e escuro.

O guia editorial completo, o modelo de conteúdo, o Design System e os padrões de diagramas são mantidos no repositório de desenvolvimento e aplicados na revisão.

## Validação local

```bash
make install
make validate   # estrutura, manifesto, assets, contraste, build e links
make test       # testes dos scripts e dos laboratórios
```

## Fluxo de uma mudança

```text
Issue → Proposta → Incorporação no desenvolvimento → Validação automática → Revisão → Release → Publicação manual
```

1. **Commits** no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/): `fix(m01): corrigir exemplo de TLS`.
2. **Um tema por proposta**, com o template de Pull Request preenchido.
3. **Revisão:** comentários indicam se são bloqueantes ou sugestões.
4. **Publicação:** manual, por release aprovada pelo mantenedor; o deploy do GitHub Pages nunca é disparado por um merge.

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
