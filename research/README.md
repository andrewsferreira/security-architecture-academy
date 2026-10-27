# Security Architecture Research Library

Base de pesquisa que sustenta o conteúdo da Academy: **quais fontes oficiais existem, em que versão, com que condições de acesso e redistribuição, e exatamente onde cada conceito está nelas.** A versão navegável fica no portal, em *Prática → Recursos*.

| Arquivo | Conteúdo |
|:---|:---|
| [`bibliography.yml`](bibliography.yml) | Registro bibliográfico — fonte única das referências, com IDs estáveis (`BOOK-ANDERSON-SE3`, `NIST-SP800-207`…), estados de acesso, redistribuição e verificação, e capítulos localizados. |
| [`knowledge-map.yml`](knowledge-map.yml) | Conceito × fonte × localização × módulo, com aplicação, limitações e exemplos. |
| [`notes/`](notes/) | Notas de leitura originais por fonte ou conjunto de fontes. |
| [`reading-priorities.md`](reading-priorities.md) | Plano de leitura: essencial, aprofundada, consulta, exercícios e projetos. |
| [`source-verification.md`](source-verification.md) | Registro de verificação, fontes indisponíveis e ações manuais pendentes. |
| [`retroactive-review-m02.md`](retroactive-review-m02.md) | Revisão bibliográfica retroativa do Módulo 02: cobertura, divergências e pendências. |

## Regras

1. **Nunca inventar** capítulo, página, versão, ISBN, DOI, permissão ou citação. Sem confirmação → `Pending`.
2. `consulted: true` só quando o trecho foi **aberto e lido** na data de `verified_on`. Capítulos identificados apenas pelo sumário ficam `consulted: false`.
3. Páginas: `page_basis: printed` (numeração impressa) ou `pdf` (índice físico do arquivo).
4. **Acesso gratuito ≠ redistribuição.** `availability` e `redistribution` são independentes.
5. Obras de terceiros nunca são versionadas — cópias ficam em `private-research/` (ignorada pelo git).
6. Notas são **análises originais**: sem trechos longos, sem figuras de terceiros, sem resumos que substituam a obra.
7. Referência citada em aula usa o ID no front matter (`sources:`) e aparece na seção *Referências* com localização.

## Manutenção

```bash
python scripts/validate_references.py            # esquema, IDs, uso, cobertura e arquivos privados
python scripts/validate_references.py --report   # imprime o relatório de cobertura
python scripts/render_curriculum.py              # regenera as páginas de docs/resources
```

O workflow semanal `links.yml` verifica os links externos, inclusive os desta biblioteca.

**Para adicionar uma fonte:** acrescente a entrada em `bibliography.yml` com `verification: Pending`; abra a página oficial; preencha versão, datas e condições; registre capítulos somente depois de vê-los; rode o validador e o gerador.

**Para revisar uma fonte:** atualize `verified_on`, confira se há versão nova e registre a mudança em `source-verification.md`.
