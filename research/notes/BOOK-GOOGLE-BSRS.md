# Building Secure and Reliable Systems — Google

**Referência:** `BOOK-GOOGLE-BSRS` · Nota de orientação de leitura · Revisão de 2026-10-23

> **Escopo desta nota.** Nesta revisão foram conferidos **os metadados e o sumário** do livro. Nenhum capítulo foi lido. A nota orienta onde ler e por quê; as sínteses de conteúdo serão acrescentadas quando os capítulos forem efetivamente consultados.

## Identificação

| Campo | Valor |
|:---|:---|
| Título | *Building Secure and Reliable Systems: Best Practices for Designing, Implementing, and Maintaining Systems* |
| Autores | Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana Oprea, Adam Stubblefield |
| Editora e data | O'Reilly Media, março de 2020 — 555 páginas — ISBN 9781492083115 |
| Acesso | Leitura online gratuita, a partir do [catálogo de livros do Google SRE](https://sre.google/books/) |
| Redistribuição | **Não verificada** — nenhum PDF oficial gratuito confirmado; não copiar nem espelhar o conteúdo |

## Relevância

O livro trata segurança e confiabilidade como **propriedades do mesmo sistema**, que competem pelos mesmos recursos de projeto e se reforçam quando desenhadas juntas. É o complemento natural à visão de Anderson: menos sobre adversários e economia, mais sobre como projetar, implantar e operar sistemas de grande escala.

## Estrutura (sumário conferido)

| Parte | Capítulos | Onde se encaixa na Academy |
|:---|:---|:---|
| I Introductory Material | 1 The Intersection of Security and Reliability; 2 Understanding Adversaries | M01, M04, M15 |
| II Designing Systems | 3 Case Study: Safe Proxies; 4 Design Tradeoffs; 5 Design for Least Privilege; 6 Design for Understandability; 7 Design for a Changing Landscape; 8 Design for Resilience; 9 Design for Recovery; 10 Mitigating Denial-of-Service Attacks | M02, M05, M06, M07, M14, M15 |
| III Implementing Systems | 11 Case Study: Designing, Implementing, and Maintaining a Publicly Trusted CA; 12 Writing Code; 13 Testing Code; 14 Deploying Code; 15 Investigating Systems | M12, M13, M15 |
| IV Maintaining Systems | 16 Disaster Planning; 17 Crisis Management; 18 Recovery and Aftermath | M15 |
| V Organization and Culture | 19 Case Study: Chrome Security Team; 20 Understanding Roles and Responsibilities; 21 Building a Culture of Security and Reliability | M03, M16 |
| Apêndice | A A Disaster Risk Assessment Matrix | M03, M15 |

## Leitura recomendada por prioridade

1. **Parte II inteira** — é a parte de *design*, diretamente ligada ao trabalho do arquiteto. Começar por 4 (trade-offs), 5 (privilégio mínimo) e 8–9 (resiliência e recuperação).
2. **Capítulo 1** — enquadramento conceitual de segurança com confiabilidade.
3. **Capítulos 16–18** — para M15 (operações e resiliência).
4. **Capítulos 20–21** — para M16 (papéis, responsabilidades e cultura).

## Aplicação educacional prevista

- **M02-L03 e M06:** o capítulo 5 deve fundamentar o desenho de acesso administrativo com privilégio mínimo usado no exemplo da Aurora Pagamentos — confirmar na leitura.
- **M15:** capítulos 8, 9 e 16–18 como base do módulo de resiliência.
- **Caso A:** capítulo 9 como leitura sobre recuperação após comprometimento (backup isolado).

## Trade-offs da fonte

- Baseado na experiência de uma organização de escala excepcional; práticas precisam ser proporcionalizadas para empresas médias, como a Meridiana.
- A edição é de 2020; práticas de supply chain e IA evoluíram desde então.

## Referências

- H. Adkins *et al.* *Building Secure and Reliable Systems*. O'Reilly Media, 2020. ISBN 9781492083115. Sumário conferido em <https://www.oreilly.com/library/view/building-secure-and/9781492083115> e acesso online em <https://google.github.io/building-secure-and-reliable-systems/raw/toc.html> (link do catálogo <https://sre.google/books/>). Consultado em 2026-10-23.
