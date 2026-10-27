# NIST — conjunto de publicações para arquitetura de segurança

**Referências:** `NIST-SP800-160-V1R1`, `NIST-CSF-2`, `NIST-CSF-INFORMATIVE-REFS`, `NIST-SP800-53`, `NIST-SP800-207`, `NIST-RMF` · Nota de leitura original · Revisão de 2026-10-23

## Identificação

| Referência | Publicação | Versão conferida |
|:---|:---|:---|
| `NIST-SP800-160-V1R1` | SP 800-160 Vol. 1 Rev. 1 — *Engineering Trustworthy Secure Systems* | Final de 16/11/2022 (Ross, Winstead, McEvilley); DOI 10.6028/NIST.SP.800-160v1r1 |
| `NIST-CSF-2` | CSWP 29 — *The NIST Cybersecurity Framework (CSF) 2.0* | 26/02/2024; DOI 10.6028/NIST.CSWP.29 |
| `NIST-CSF-INFORMATIVE-REFS` | CSF 2.0 Informative References | Página atualizada em 15/10/2026 |
| `NIST-SP800-53` | SP 800-53 Rev. 5 — *Security and Privacy Controls for Information Systems and Organizations* | Release 5.2.0 de 27/08/2025; DOI 10.6028/NIST.SP.800-53r5 |
| `NIST-SP800-207` | SP 800-207 — *Zero Trust Architecture* | Final de 11/08/2020 (Rose, Borchert, Mitchell, Connelly); DOI 10.6028/NIST.SP.800-207 |
| `NIST-RMF` | Risk Management Framework (projeto) | Sete etapas: Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor |

Nesta revisão foram conferidas as **páginas oficiais** (título, data, autores, DOI, versão, materiais suplementares) e os **sumários dos PDFs** das SP 800-160 Vol. 1 Rev. 1 e SP 800-207, com as páginas impressas. Da SP 800-207 foi lida a §2.1 (*Tenets of Zero Trust*); as demais seções citadas abaixo foram localizadas pelo sumário, sem leitura do conteúdo.

## Relevância

As seis publicações formam uma pilha coerente, e confundi-las é um erro comum:

| Pergunta | Publicação |
|:---|:---|
| Como engenhar um sistema digno de confiança, do requisito à evidência? | SP 800-160 Vol. 1 |
| Como comunicar a postura e as prioridades da organização? | CSF 2.0 |
| Como ligar resultados do CSF a controles de catálogos específicos? | Informative References |
| Que controles existem e como são descritos? | SP 800-53 (catálogo) |
| Como gerenciar o risco de um sistema ao longo do seu ciclo de vida? | RMF |
| Como projetar decisões de acesso sem confiança implícita na rede? | SP 800-207 |

## Conceitos fundamentais

**Engenharia antes de controles.** A SP 800-160 Vol. 1 parte da engenharia de sistemas: segurança é uma propriedade emergente, obtida por processos de ciclo de vida — análise de missão, necessidades de stakeholders, requisitos, definição de arquitetura, verificação e validação. Para a Academy, é a base normativa da ideia de que o arquiteto trabalha com **rastreabilidade** do objetivo de negócio à evidência (M02-L07).

**Linguagem de resultados.** O CSF 2.0 descreve *o que* alcançar, em seis Functions (Govern, Identify, Protect, Detect, Respond, Recover), com perfis atual e alvo e Tiers que qualificam o rigor da gestão de risco. Não prescreve controles — por isso existe o mecanismo de Informative References.

**Mapeamentos oficiais.** As Informative References ligam o CSF a SP 800-53 Rev. 5.2.0, ISO/IEC 27001:2022, CIS Controls 8.1, CCM v4.0, PCI DSS 4.0.1 e outros, com download integral em planilha e tradução para português. O NIST testa a conformidade de formato, não a correção de mapeamentos de terceiros — um detalhe importante ao usá-los como evidência.

**Catálogo não é obrigação.** O SP 800-53 é um catálogo; baselines estão na SP 800-53B; obrigações vêm de lei, contrato ou política interna. Tratar todo o catálogo como exigência é o antipadrão de complexidade desnecessária discutido em M02-L04.

**Zero Trust como arquitetura.** O SP 800-207 descreve uma arquitetura lógica abstrata (§3, p. 9) — decisões de acesso por recurso, tomadas por um ponto de decisão e aplicadas por um ponto de aplicação, a partir de identidade, estado do dispositivo e contexto. Não é um produto nem um projeto com fim.

Os sete princípios da §2.1 (p. 6), resumidos com palavras próprias: (1) todo serviço e fonte de dados é tratado como recurso; (2) toda comunicação é protegida, e estar na rede interna não confere confiança; (3) o acesso é concedido por sessão, com privilégio mínimo; (4) a decisão usa política dinâmica — identidade, estado do dispositivo e atributos de comportamento e ambiente; (5) a postura de todos os ativos é monitorada continuamente, sem confiança por padrão; (6) autenticação e autorização são dinâmicas e reavaliadas durante o uso; (7) a organização coleta dados de ativos, tráfego e pedidos de acesso para melhorar a postura.

Para ambientes híbridos, duas seções são diretamente relevantes: §4.2 *Multi-cloud/Cloud-to-Cloud Enterprise* (p. 24) e §7.2 *Hybrid ZTA and Perimeter-Based Architecture* (p. 36) — a coexistência de Zero Trust com o perímetro é a situação real da maioria das organizações, como a Meridiana do Caso A.

**Princípios de design (SP 800-160, Apêndice E, p. 82).** Trinta princípios para *trustworthy secure design*, entre eles *Defense In Depth* (E.9), *Least Privilege* (E.16), *Mediated Access* (E.19) e *Minimal Trusted Elements* (E.20). É a referência primária para os princípios ensinados em M01-L02 e aplicados em M02-L04; os nomes e a numeração foram conferidos no sumário, a definição de cada um ainda será conferida no texto.

**Requisito, política e mecanismo (SP 800-160, Apêndice C.3, p. 68).** Seção dedicada a distinguir requisitos, política e mecanismos — a mesma distinção que M02-L07 ensina ao separar requisito funcional, de qualidade e restrição. Conferir o texto antes de citar a definição.

**Processos técnicos (SP 800-160, Apêndice H, p. 115).** A sequência *Business or Mission Analysis* (H.1) → *Stakeholder Needs and Requirements Definition* (H.2) → *System Requirements Definition* (H.3) → *System Architecture Definition* (H.4) → … → *Verification* (H.9) e *Validation* (H.11) é a espinha da rastreabilidade do objetivo de negócio à evidência.

## Aplicação prática

- Em uma proposta para a diretoria, usar o CSF para *o quê*, o SP 800-53 (via Informative References) para *com quais controles* e a SP 800-160 para *como garantir que o sistema entregue o prometido*.
- Na Release 5.2.0 do SP 800-53, aproveitar o formato **OSCAL** (JSON, XML, YAML) para automatizar seleção e verificação de controles.

## Ambientes híbridos

Todas as publicações são neutras de tecnologia. O desafio híbrido é de **mapeamento**: o mesmo resultado do CSF ou controle do SP 800-53 é realizado por mecanismos diferentes no datacenter e em cada provedor — exatamente o exercício da visão física em M02-L03.

## Trade-offs

- Volume: o SP 800-53 é extenso; deve ser consultado, não lido.
- Origem: as publicações foram escritas para o contexto federal dos EUA; o vocabulário (por exemplo, *authorization* no RMF) precisa ser adaptado a empresas privadas brasileiras.

## Aplicação educacional

- **M02-L06:** quadro comparativo da tabela de relevância acima.
- **M03:** exercício de rastrear um resultado do CSF até controles com as Informative References.
- **M07:** PDP/PEP do SP 800-207 (§3) em laboratório; modelos de implantação da §3.2 como exercício de comparação.
- **M01/M02:** confrontar a lista de princípios da Academy com o Apêndice E da SP 800-160.

## Referências

- NIST. SP 800-160 Vol. 1 Rev. 1. <https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final> — página e sumário do PDF (<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf>) conferidos em 2026-10-23. Apêndices C (p. 64), D (p. 70), E (p. 82), F (p. 102), H (p. 115), I (p. 149).
- NIST. CSWP 29, CSF 2.0. <https://doi.org/10.6028/NIST.CSWP.29> — conferido em 2026-10-23.
- NIST. CSF 2.0 Informative References. <https://www.nist.gov/cyberframework/csf-20-informative-references> — conferido em 2026-10-23.
- NIST. SP 800-53 Rev. 5. <https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final> — página conferida em 2026-10-23.
- NIST. SP 800-207. <https://csrc.nist.gov/pubs/sp/800/207/final> — página e PDF (<https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf>) conferidos em 2026-10-23. §2.1 (p. 6) lida; §3 (p. 9), §3.2 (p. 13), §3.3 (p. 17), §4.2 (p. 24), §7.2 (p. 36) localizadas pelo sumário.
