# Política de Segurança

## Escopo

Esta política cobre vulnerabilidades **no próprio projeto**:

- Repositório, scripts e workflows do GitHub Actions (por exemplo, exposição de tokens, injeção em workflows, permissões excessivas).
- Portal publicado no GitHub Pages (por exemplo, XSS em páginas ou templates).
- Dependências utilizadas no build.

**Fora do escopo:** erros conceituais ou desatualização de conteúdo educacional — use a issue *Report a documentation error*.

## Como reportar uma vulnerabilidade

**Não abra uma issue pública.** Use um destes canais privados:

1. **Preferencial:** [GitHub Private Vulnerability Reporting](https://github.com/andrewsferreira/security-architecture-academy/security/advisories/new) (aba *Security → Report a vulnerability*).
2. **Alternativo:** e-mail para **<andrewslf1@gmail.com>** com o assunto `[SECURITY] security-architecture-academy`.

Inclua: descrição, impacto, passos para reproduzir e, se possível, uma sugestão de correção.

## O que esperar

| Etapa | Prazo-alvo |
|:---|:---|
| Confirmação de recebimento | até 5 dias úteis |
| Avaliação inicial | até 10 dias úteis |
| Correção de problemas confirmados | conforme a severidade, com comunicação de andamento |

O projeto é mantido por uma pessoa, de forma voluntária; os prazos são metas, não garantias contratuais. Reportes válidos serão creditados no advisory, se a pessoa desejar.

## Conteúdo educacional e segurança

Os materiais da Academy usam exclusivamente cenários e dados fictícios. Se encontrar algum dado real, credencial ou informação sensível no repositório, reporte pelos canais privados acima.
