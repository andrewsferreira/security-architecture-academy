# Revisão bibliográfica retroativa — Módulo 02

Revisão feita em 2026-10-23, **depois** da escrita das aulas, para conferir se as afirmações do Módulo 02 têm fundamentação em fontes oficiais verificadas. As fontes acrescentadas aparecem em cada aula na seção *Leituras de aprofundamento* e no campo `further_reading` do front matter, sempre identificadas como posteriores à escrita — nunca como base original do texto.

**Legenda:** **Fundamentada** — confirmada em fonte verificada · **Localizada** — a seção correspondente foi identificada no sumário da fonte, mas o texto ainda não foi lido · **Pendente** — depende de fonte primária ainda não consultada · **Ajustada** — o texto da aula foi corrigido nesta revisão.

## Resultado por aula

| Aula | Afirmação ou conceito | Fonte | Situação |
|:---|:---|:---|:---|
| L01 | Segurança como propriedade emergente do sistema | `NIST-SP800-160-V1R1`, Apêndice D.2 (p. 73) | Localizada |
| L01 | Definição de arquitetura da ISO/IEC/IEEE 42010 (elementos, relacionamentos, princípios) | `ISO-42010-2022` — norma paga; `ARC42-ISO42010-SUMMARY` (resumo secundário lido em 2026-10-23) | **Fundamentada em fonte secundária** — texto ajustado para indicar a origem; norma não consultada |
| L01 | Raciocínio adversarial e o papel do arquiteto | `BOOK-ANDERSON-SE3`, Cap. 1 (§1.2, §1.7) | Fundamentada (leitura complementar) |
| L02 | Integração de segurança ao TOGAF por serviços de segurança | `TOG-RISK-SECURITY` (introdução conferida); `SABSA-G152`, `SABSA-W117` | Pendente — leitura dos white papers |
| L03 | SABSA em camadas *contextual*, *conceptual*, *logical*, *physical*, componentes e operação | `SABSA-W100`, Table 1 (p. 9) | **Fundamentada** — confirmada no W100 em 2026-10-23 (cópia não oficial) |
| L03 | Princípio AWS *Apply security at all layers* | `AWS-WA-SECURITY-DESIGN` | Fundamentada |
| L04 | Formato de princípio: nome, declaração, justificativa e implicações (TOGAF) | `TOG-TOGAF9-PRINCIPLES` (documentação online da série TOGAF 9, lida em 2026-10-23) | **Fundamentada** — formato e critérios confirmados; a 10ª edição não foi consultada |
| L04 | Lista de princípios de design seguro usados como origem de padrões | `NIST-SP800-160-V1R1`, Apêndice E (E.1–E.30) | Localizada |
| L04 | Exceções com prazo e revisão periódica | `BOOK-ANDERSON-SE3`, Cap. 6, §6.4.5 | Fundamentada (leitura complementar) |
| L05 | SP 800-207 descreve componentes lógicos e modelos de implantação, de forma neutra | `NIST-SP800-207`, §3 (p. 9) e §3.2 (p. 13) | Fundamentada — seções existem com esses títulos |
| L05 | AWS SRA (setembro de 2023) e MCRA (abril de 2025) | `AWS-SRA`, `MS-MCRA` | Fundamentada |
| L06 | Functions, Profiles e Tiers do CSF 2.0 | `NIST-CSF-2`, `NIST-CSF-FAQ` | Fundamentada |
| L06 | Release 5.2.0 do SP 800-53 (agosto de 2025) | `NIST-SP800-53` — página oficial: 27/08/2025 | Fundamentada |
| L06 | Camadas, matriz e Business Attributes Profile do SABSA | `SABSA-W100`, pp. 8–20 | **Ajustada** — confirmada no W100; exemplos de atributos e a menção a "justificativa" foram alinhados ao texto; nota da aula atualizada |
| L06 | Outlines CISSP (15/04/2024) e ISSAP (01/08/2025, quatro domínios) | `ISC2-CISSP-OUTLINE`, `ISC2-ISSAP-2025` | Fundamentada |
| L06 | Referência ao W101 com "forma de acesso não confirmada" | `SABSA-CATALOG` | **Ajustada** — download direto confirmado |
| L07 | Distinção entre requisito, política e mecanismo; rastreabilidade do negócio à evidência | `NIST-SP800-160-V1R1`, Apêndices C.3 e H.1–H.4 | Localizada |
| L07 | Business Attributes Profile e derivação de requisitos | `SABSA-W100`, pp. 19–20 | **Fundamentada** — atributos com definição e métrica, na camada conceitual |
| L07 | Referência ao W101 com "forma de acesso não confirmada" | `SABSA-CATALOG` | **Ajustada** |
| L08 | Formato do ADR (Nygard, 2011) | `NYGARD-ADR-2011` | Fundamentada |
| L08 | Decisão como processo de engenharia | `NIST-SP800-160-V1R1`, Apêndice I.3 (p. 153) | Localizada |

## Atualização de 2026-10-23 (segunda revisão)

O texto do *SABSA White Paper* (W100) foi lido e confirmou as camadas, as visões, a matriz 6 × 6 e o Business Attributes Profile. A L06 foi ajustada nos exemplos de atributos e deixou de mencionar uma "justificativa" por atributo, que não aparece no W100. A página do W105 informou que o documento está **inicialmente disponível apenas para membros** do instituto — o registro bibliográfico foi corrigido.

## Imprecisões identificadas

Nenhuma afirmação do Módulo 02 foi **contrariada** pelas fontes conferidas. Ajustes feitos:

1. L06 e L07 — a referência ao W101 dizia que a forma de acesso não estava confirmada; o catálogo oficial oferece download direto. Texto atualizado.
2. Registro de fontes — a ideia anterior de que os white papers do SABSA exigiam cadastro (`sabsa-requests`, "não verificada") foi corrigida: a página do catálogo não exibe formulário.

## Afirmações que precisam de mais fundamentação

| Prioridade | O quê | Ação |
|:---|:---|:---|
| Resolvida | Camadas do SABSA e Business Attributes Profile (L03, L06, L07) | Conferidos no W100 (2009) em 2026-10-23; L06 ajustada. Permanece recomendável confirmar no W101 (2018) se houve mudança de nomenclatura |
| Resolvida (nomes) | Princípios de design da L04 *versus* Apêndice E da SP 800-160 | Títulos e numeração E.1–E.30 reconferidos no sumário do PDF oficial em 2026-10-24; os nomes usados em M01-L02 e M02-L04 coincidem. As definições do apêndice continuam sem leitura integral — a citação permanece marcada como "localizada pelo sumário" |
| Resolvida (fonte secundária) | Definição de arquitetura da ISO/IEC/IEEE 42010 (L01) | Texto ajustado para indicar o resumo secundário (`ARC42-ISO42010-SUMMARY`); a norma, paga, não foi consultada |
| Resolvida (série 9) | Formato de princípios do TOGAF (L04) | Formato e critérios conferidos na documentação online da série TOGAF 9 (`TOG-TOGAF9-PRINCIPLES`); a 10ª edição não foi consultada |
| Baixa | Exemplo de acesso administrativo com privilégio mínimo (L03) | Ler o Cap. 5 do BSRS e citar a seção correspondente |

## Cobertura bibliográfica do Módulo 02

Todas as oito aulas têm ao menos uma fonte verificada em `sources` e ao menos uma leitura de aprofundamento localizada em `further_reading`. O relatório automático de cobertura de todo o currículo é gerado por `scripts/validate_references.py --report` e publicado em *Recursos → Cobertura bibliográfica*.
