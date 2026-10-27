# SABSA — catálogo de white papers

**Referências:** `SABSA-CATALOG`, `SABSA-W100`, `SABSA-W101`, `SABSA-W102`, `SABSA-W103`, `SABSA-W105`, `SABSA-W117`, `SABSA-T100`, `SABSA-G152` · Nota de orientação de leitura · Revisão de 2026-10-23

> **Escopo desta nota.** Foram conferidos o **catálogo oficial** e as páginas do W101 e do W105. O texto do **W100** (*SABSA White Paper*, 2009) foi lido em 2026-10-23 numa cópia hospedada fora do site do instituto, e confirmou as camadas, a matriz e o Business Attributes Profile usados no M02. W101 e W105 não foram lidos.

## Identificação

O SABSA Institute mantém um [catálogo de white papers](https://sabsa.org/white-paper-requests/). Em 2026-10-23, cada item tinha link de download direto e hash SHA256, sem formulário visível na página.

| Código | Título | Publicação | Prioridade |
|:---|:---|:---|:---|
| W100 | SABSA White Paper | 2009 | 2 — visão geral do método |
| W101 | Architecting a Secure Digital World | Agosto de 2018 | **1** — introdução atual |
| W102 | SABSA Risk Management Part One – The Meaning of Risk | Outubro de 2018 | 2 — base para M03 |
| W103 | SABSA Responsibility Assignment Modelling | Junho de 2023 | 3 — governança de responsabilidades |
| W105 | SABSA Enterprise Security Architecture Principles | Janeiro de 2026 — **inicialmente apenas para membros** | **1** — princípios e framework PAB (M02-L04, M16) |
| W117 | SABSA–TOGAF Integration White Paper | Outubro de 2011 | 2 — integração com TOGAF |
| T100 | Modelling SABSA with ArchiMate | Outubro de 2019; v2.5 de fevereiro de 2026 | 3 — modelagem |
| G152 | Integrating Risk and Security within a TOGAF Enterprise Architecture | Janeiro de 2016 | 2 — guia Open Group |

## O que o W100 confirma

| Elemento | Conteúdo (W100, 2009) |
|:---|:---|
| Camadas e visões (Table 1, p. 9) | Contextual — visão do negócio; Conceptual — do arquiteto; Logical — do projetista; Physical — do construtor; Component — do especialista (*tradesman*); Security Service Management — do gestor de serviços, atravessando as demais |
| Matriz (Table 3, p. 16) | Seis perguntas por camada: Assets (*what*), Motivation (*why*, em termos de risco), Process (*how*), People (*who*), Location (*where*), Time (*when*) |
| Business Attributes Profile (pp. 19–20) | Técnica de engenharia de requisitos que normaliza necessidades de negócio; atributos selecionados de uma taxonomia em sete grupos, cada um com definição e métrica |
| Origem (p. 8) | Segue de perto o framework de Zachman, adaptado à segurança |

## Relevância

O SABSA é a principal ponte da Academy entre **necessidades de negócio e decisões de arquitetura**. Os conceitos que as aulas usam — atributos de negócio mensuráveis, camadas de abstração e rastreabilidade bidirecional — precisam ser conferidos nas publicações do instituto antes da publicação do M16.

## Plano de leitura

1. **W101** e **W105** — confirmar, na fonte primária, a descrição das camadas, do Business Attributes Profile e dos princípios usados em M02-L04, L06 e L07.
2. **W102** — base de risco para M03.
3. **W117** e **G152** — integração com TOGAF para M02-L02 e M16; confirmar se o W117 é o mesmo documento anunciado pela The Open Group em 07/11/2011 (`TOG-SABSA-2011`) e como o G152 se relaciona com o guia atual da série TOGAF (`TOG-RISK-SECURITY`).
4. **T100** — opcional, para quem modela arquitetura em ArchiMate.

## Direitos

Download gratuito não significa licença aberta. Os termos de redistribuição não foram verificados: as cópias ficam apenas em `private-research/` e as aulas citam, resumem com palavras próprias e apontam para o catálogo.

## Ação manual necessária

O ambiente de verificação não consegue baixar arquivos. O mantenedor deve baixar W100 e W101 do catálogo, conferir o hash SHA256 publicado e salvar em `private-research/sabsa/`. O W105 exige cadastro como membro do instituto.

## Referências

- SABSA Institute. *White Paper Requests*. <https://sabsa.org/white-paper-requests/> — catálogo conferido em 2026-10-23.
