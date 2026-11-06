# Registro de verificação de fontes

Como cada fonte de [`bibliography.yml`](bibliography.yml) foi verificada, o que ficou indisponível e o que depende de ação manual. O estado atual de cada referência fica no próprio registro; este arquivo guarda o **histórico** e as **pendências**.

## Método

1. Abrir a página **oficial** da fonte (instituição, editora ou autor), nunca um espelho.
2. Registrar título, autores, versão ou edição, data, identificadores (DOI, ISBN) e condições de acesso **como exibidos na página**.
3. Registrar capítulos e seções somente depois de vê-los no sumário oficial (`consulted: false`) ou de ler o texto (`consulted: true`).
4. Registrar separadamente *availability* e *redistribution*; sem termo explícito, `redistribution: Not Verified`.
5. Quando a página não pode ser aberta, marcar `Unavailable` ou `Pending` e não citar dados dela nas aulas.

Ambiente de verificação: o shell não tem acesso à internet; as páginas foram abertas pelas ferramentas de busca e leitura web, que trabalham com uma lista de domínios permitidos. Por isso **nenhum arquivo foi baixado** — PDFs foram lidos diretamente pela ferramenta quando permitido.

## 2026-10-23 — Integração da Research Library

**Verificadas nesta data (página oficial aberta):**

| Referência | O que foi conferido |
|:---|:---|
| `BOOK-ANDERSON-SE3` | Página do livro (edição, períodos de publicação, acordo com a Wiley, PDFs por capítulo e integral, licença CC só para slides); PDFs dos capítulos 1, 6, 8, 10, 27 e 28 — seções e páginas impressas |
| `BOOK-GOOGLE-BSRS` | Catálogo sre.google/books (leitura online); página da O'Reilly (março de 2020, 555 p., ISBN 9781492083115, sumário completo) |
| `NIST-SP800-160-V1R1` | Página CSRC (final de 16/11/2022, autores, DOI) e sumário do PDF |
| `NIST-SP800-207` | Página CSRC (final de 11/08/2020, autores, DOI) e PDF: sumário e §2.1 |
| `NIST-SP800-53` | Página CSRC: Release 5.2.0 de 27/08/2025, OSCAL, partes 53A e 53B |
| `NIST-CSF-INFORMATIVE-REFS` | Página oficial (atualizada em 15/10/2026): formatos, traduções, mapeamentos |
| `SABSA-CATALOG` e W100–W117, T100, G152 | Catálogo oficial: códigos, títulos, datas, download direto com SHA256, sem formulário |
| `AWS-SECURITY-PILLAR` | Whitepaper (06/11/2024) e as sete áreas de boas práticas |
| `AZURE-WAF-SECURITY`, `AZURE-WAF-SECURITY-CHECKLIST` | Cinco princípios; recomendações SE:01–SE:12 |
| `GCP-ARCH-CENTER`, `GCP-ENTERPRISE-FOUNDATIONS` | Categorias do Architecture Center; conteúdo do blueprint (versão Markdown oficial) e repositório Terraform |
| `CSA-GUIDANCE-V5` | Título, datas (15/07/2024; atualizado 26/08/2025), doze domínios, login para download |
| `CIS-CONTROLS-V8-1` | Página da v8.1 e conteúdo do download |
| `OWASP-ASVS-5` | Versão 5.0.0 estável; licença CC BY-SA 4.0 |
| `MITRE-ATTACK` | Versão v20 (13/10/2026) |

**Parcialmente verificadas:**

| Referência | Limitação |
|:---|:---|
| `CISA-ZTMM-2` | Página da CISA aberta sem versão e data; pilares, capacidades e data (abril de 2023) confirmados por fonte secundária da Microsoft |
| `CSA-GUIDANCE-V5` | Não ficou claro se o download exige cadastro gratuito |
| `MITRE-ATTACK` | Termos de uso (Legal & Branding) não abertos |

**Indisponíveis no ambiente de verificação:**

| Referência | Situação |
|:---|:---|
| `NIST-CSF-HOME` | `www.nist.gov/cyberframework` fora da lista de domínios permitidos; substituída por `NIST-CSF-2` e `NIST-CSF-INFORMATIVE-REFS` |
| `AZURE-ARCH-SECURITY` | `learn.microsoft.com/en-us/azure/architecture/security/` fora da lista permitida |
| `ISC2-ISSAP-OUTLINE`, `NIST-SP800-37-R2`, `MS-SC100-PATH`, `AZURE-SECURITY-ARCH-PTBR`, `GCP-ARCH-FUNDAMENTALS` | Pendentes desde a Fase 0; não usados como base de afirmações |

**Correções no registro:**

- `sabsa-requests` (antes "não verificada", com suposição de cadastro) → `SABSA-CATALOG`, verificada: download direto, sem formulário visível.
- `cis-controls-81` passou a apontar para a página da v8.1 em vez da página de Implementation Groups.
- `owasp-asvs` e `mitre-attack`: versões confirmadas (5.0.0 e v20), substituindo as anotações "a conferir".
- IDs migrados para o padrão estável em maiúsculas (por exemplo, `nist-sp-800-207` → `NIST-SP800-207`); aulas e template atualizados.

## 2026-10-23 — Segunda rodada (conteúdo acadêmico completo)

- **Novas fontes verificadas** para M00 e M01: NIST SP 800-145, 800-190 (e boletim ITL de 10/2017), 800-125, 800-41 Rev. 1, 800-215, 800-34 Rev. 1, 800-204 (e partes A–D), 800-57 Pt. 1 Rev. 5, 800-30 Rev. 1, 1800-16, FIPS 203/204/205, IR 8547 (rascunho); RFC 1918; **RFC 9846** (TLS 1.3, julho de 2026, que tornou obsoleto o RFC 8446); documentação Kubernetes; AWS Reliability Pillar; CA/Browser Forum Ballot SC081v3; Saltzer e Schroeder (1975, dados em fonte secundária).
- **Lidos:** Anderson, caps. 9 e 12; SP 800-160 Vol. 1 Rev. 1 — §3.2, §3.8 e *Trust and Trustworthiness*; SP 800-145, §2; SABSA W100 (cópia não oficial).
- **Limitações:** os apêndices da SP 800-160 não são extraídos pela ferramenta de leitura; o RFC 5280 e a página da ISO 42010 exigiram permissão não concedida.
- **Correção:** o W105 do SABSA está inicialmente disponível só para membros — `availability: Restricted`.

## 2026-11-05 — Auditoria de conteúdo M00–M08

Verificação independente feita durante a auditoria de conteúdo dos Módulos 0 a 8 (R3).

| Fonte | O que foi conferido | Resultado |
|:---|:---|:---|
| NIST SP 800-53 Rev. 5, Release 5.2.0 (OSCAL, `usnistgov/oscal-content`) | Os 196 pares "ID (título)" citados em M00–M08, avaliações, artefatos e no Caso A; enunciados de SA-22 e AC-5 | Todos conferem; único desvio: título abreviado de IA-2 em M02-L03 (corrigido). Nenhum controle retirado |
| Microsoft Learn — *Deprecated features for Windows client* | Linha NTLM (junho de 2024) e atualização de novembro de 2024 | Novo registro `MS-WINDOWS-DEPRECATED-FEATURES` (Verified); passa a ser a fonte primária de M08-L06 |
| Windows IT Pro Blog — *Advancing Windows security: disabling NTLM by default* | Localizado; texto não renderizado pela ferramenta | O plano em fases continua sustentado por `PETRI-NTLM-2026` (secundária) |
| Saltzer e Schroeder (1975) — versão HTML na página do autor (MIT) | Seção I.A.3: oito princípios e dois de aplicação imperfeita | Princípios conferidos no original; periódico e páginas ainda vêm de fonte secundária (Partially Verified) |
| BeyondCorp (Ward e Beyer, ;login: 2014) | Página da USENIX: dados bibliográficos e resumo | Novo registro `BEYONDCORP-2014` (Partially Verified) |
| Mplify 169 — Security Service Edge Framework (2026) | Página oficial: escopo, funções, termos de reprodução | Novo registro `MPLIFY-169-SSE` (Partially Verified); MEF 117 consta como substituído pelo Mplify 117.1 |
| NIST SP 800-63B-4 (HTML) | AAL2: verificadores devem oferecer ao menos uma opção resistente a phishing; AAL3: chave não exportável e resistência a phishing | Confere com M05-L04 e M06-L01 |
| NIST SP 800-41 Rev. 1, 800-34 Rev. 1, 800-160 Vol. 1 Rev. 1, 800-207A (CSRC) | Situação e datas | Finais e vigentes; nenhuma revisão anunciada para 800-41 e 800-34 |
| OWASP ASVS 5.0.0, ISO/IEC/IEEE 42010:2022, PCI DSS v4.0.1 (blog oficial) | Versão, data, licença e formato de identificadores; edição 2 (nov. 2022); 11/06/2024, sem requisitos novos ou removidos, v4.0 retirada em 31/12/2024 | Conferem com os registros |
| CISA ZTMM 2.0 (PDF e notícia oficial) | Duas URLs oficiais falharam; página da CISA sem versão; Microsoft Learn reconferido | Continua Partially Verified — conferência do PDF pelo mantenedor pendente |
| SABSA W101 | Página oficial aberta; PDF não acessível pela ferramenta | Leitura continua pendente (ação manual abaixo) |

## Ações manuais pendentes (mantenedor)

| Ação | Por quê |
|:---|:---|
| Baixar `SABSA-W101` e `SABSA-W105`, conferir o SHA256 publicado no catálogo e salvar em `private-research/sabsa/` | Leitura de verificação das afirmações sobre o SABSA em M02-L03, L06 e L07 |
| Ler os capítulos 4, 5, 8 e 9 do BSRS na versão online | Converter a nota de orientação em nota de leitura e fundamentar exemplos do M02 e do Caso A |
| Ler os Apêndices C.3 e E da SP 800-160 | Alinhar princípios e a distinção requisito/política/mecanismo |
| Confirmar se o download da CSA Security Guidance v5 exige cadastro | Preencher `availability` com segurança |
| Liberar, se desejado, os domínios `www.nist.gov` e `learn.microsoft.com/en-us/azure/architecture` para a verificação automatizada | Fechar `NIST-CSF-HOME` e `AZURE-ARCH-SECURITY` |
| Confirmar termos de redistribuição dos white papers SABSA e da CSA | Hoje registrados como `Not Verified` e `Restricted` |

## Próxima revisão

Revisar todas as fontes `Verified` com `verified_on` anterior a seis meses e, obrigatoriamente, antes de publicar cada módulo que as cite.
