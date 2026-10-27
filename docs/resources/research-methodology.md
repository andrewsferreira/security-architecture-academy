---
title: Metodologia de pesquisa
description: Como a Research Library verifica fontes, registra capítulos e páginas, separa acesso de redistribuição, protege direitos autorais e é mantida e validada automaticamente.
---

# Metodologia de pesquisa

A biblioteca existe para que cada aula aponte **exatamente** quais fontes sustentam seus conceitos — sem depender de conhecimento gerado de memória. Esta página descreve como uma fonte entra no registro, o que significa cada estado e como a integridade é verificada.

## Do registro à aula

```mermaid
--8<-- "assets/diagrams/research-traceability.mmd"
```

1. **Registro.** A fonte entra em [`research/bibliography.yml`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/bibliography.yml) com um ID estável — por exemplo `BOOK-ANDERSON-SE3`, `NIST-SP800-207`, `SABSA-W101`.
2. **Verificação.** A página **oficial** é aberta e o registro recebe título, autores, edição ou versão, data, DOI ou ISBN e condições de acesso, como exibidos na fonte.
3. **Localização.** Capítulos e seções são registrados quando aparecem no sumário oficial (*localizado*) e marcados como *lido* somente depois que o texto foi consultado. Páginas indicam se seguem a numeração **impressa** ou o **índice do PDF**.
4. **Mapeamento.** Conceitos são ligados à localização e aos módulos em [`research/knowledge-map.yml`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/knowledge-map.yml), com aplicação arquitetural e limitações.
5. **Citação.** Cada aula lista no front matter as fontes que a sustentam (`sources`) e as leituras complementares (`further_reading`), e as cita com localização na seção *Referências*.

## Estados independentes

| Dimensão | Valores | O que responde |
|:---|:---|:---|
| **Acesso** (*availability*) | Download gratuito · Leitura online gratuita · Gratuito com cadastro · Pago · Restrito · Não confirmado | Como o estudante chega à fonte |
| **Redistribuição** (*redistribution*) | Permitida pela licença · Restrita · Proibida · Não verificada | Se a fonte pode ser copiada ou republicada |
| **Verificação** (*verification*) | Verificada · Parcialmente verificada · Indisponível · Pendente | Se a página oficial foi conferida e quando |

**Acesso gratuito não é licença aberta.** O livro de Anderson pode ser baixado gratuitamente, mas sua redistribuição é proibida; a OWASP ASVS, por outro lado, é distribuída sob CC BY-SA 4.0. Sem um termo explícito, a redistribuição fica *Não verificada*.

## Integridade e direitos autorais

- Nenhum capítulo, página, versão, ISBN, DOI, permissão ou citação é inventado. Sem confirmação, o estado é *Pendente*.
- Referências acrescentadas depois da escrita de uma aula aparecem como **leituras de aprofundamento**, identificadas como posteriores — nunca como base original do texto.
- Notas de leitura são **análises originais**: sem trechos extensos, sem figuras de terceiros, sem resumos que substituam a obra.
- Obras de terceiros nunca entram no repositório. Cópias de estudo ficam em `private-research/`, ignorada pelo git; PDFs e EPUBs são ignorados em todo o projeto.

## Validação automática

[`scripts/validate_references.py`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/scripts/validate_references.py) roda no CI e verifica:

- esquema do registro, valores permitidos, datas e IDs únicos;
- fontes sem metadados mínimos;
- citações das aulas que apontam para IDs inexistentes — e aulas que usam como base uma fonte *Pendente* ou *Indisponível*;
- conceitos do mapa marcados como lidos em capítulos não consultados;
- referências não utilizadas e módulos sem fontes;
- arquivos privados, PDFs ou EPUBs versionados por engano.

Os links externos são verificados semanalmente (`--links`), com uma requisição por segundo, sem varredura agressiva.

## Revisão retroativa do Módulo 02

O Módulo 02 foi escrito antes da biblioteca. A [revisão bibliográfica retroativa](m02-bibliographic-review.md) registra, afirmação por afirmação, o que está fundamentado, o que foi apenas localizado e o que ainda depende de fonte primária.

## Histórico de verificação

O registro detalhado — o que foi conferido em cada data, fontes indisponíveis e ações manuais pendentes — está em [`research/source-verification.md`](https://github.com/andrewsferreira/security-architecture-academy/blob/main/research/source-verification.md).
