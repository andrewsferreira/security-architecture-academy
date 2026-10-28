# Changelog

Todas as mudanças relevantes deste projeto são registradas aqui.

O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e o projeto adota [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

Release 2 — Fundamentals: conclusão do Nível 1 (v0.2.0, em revisão; não publicada).

### Added

- **Módulo 3 — Governança, Riscos e Controles** (8 aulas) e **Módulo 4 — Métodos de Design e Threat Modeling** (7 aulas): com a Release 1, o portal passa a reunir os Níveis 0 e 1 completos — 37 aulas.
- **Avaliação integradora do Nível 1** (`AS-N1`), com cenário fictício, rubrica, resultados de aprendizagem do Nível 1 e gabarito comentado separado. A avaliação final de Fundamentals (`AS-FUND`) não muda.
- Matriz de decisão ponderada nos exercícios das 15 aulas dos Módulos 3 e 4, com testes que conferem a aritmética.

### Changed

- Publicação progressiva por nível: a R1 continua com o Módulo Inicial e os Módulos 1 e 2 (v0.1.0 e v0.1.1); a R2 completa o Nível 1; as Releases 3 a 6 trazem os Níveis 2 a 5. A página inicial, o ROADMAP e as trilhas mostram o estado de cada release a partir do manifesto.
- Mapas dos módulos já publicados (Módulo Inicial, Módulos 1 e 2) com os nomes públicos dos módulos no título e nos rótulos; páginas e endereços não mudam.
- Avaliação final de Fundamentals (`AS-FUND`, publicada na R1) renomeada para **Avaliação integradora do Módulo Inicial ao Módulo 2**, porque Fundamentals passa a abranger os Níveis 0 e 1; a abertura e o encerramento indicam que ela conclui a etapa do Módulo Inicial ao Módulo 2 e que a avaliação integradora do Nível 1 conclui Fundamentals. ID, endereço e âncoras não mudam.
- Introdução do Curriculum Roadmap atualizada para as releases por nível.
- Como usar a Academy, plano de estudos e trilhas: disponibilidade gerada do manifesto e percursos até a avaliação integradora do Nível 1.
- Research Library: registros de verificação de MITRE ATT&CK v20, Resolução CD/ANPD nº 15/2024, LGPD, PCI DSS v4.0.1, NIST SP 800-53 Release 5.2.0, CIS Controls v8.1 e OWASP ASVS 5.0.0 atualizados.

### Fixed

- Rubrica da avaliação integradora do Módulo Inicial ao Módulo 2 (`AS-FUND`): *Adequado* nas tarefas de 15 pontos passa de 10 para 11 (70% arredondado para cima, como na rubrica padrão); quem é *Adequado* em todas as tarefas soma 71 e é aprovado. Teste de regressão das rubricas.

## [0.1.1] — 2026-10-27

Estabilização da Release 1 — Fundamentals, publicada no GitHub Pages.

### Changed

- Nomenclatura pública de módulos e aulas: o Módulo 00 passa a ser exibido como **Módulo Inicial** e os demais como **Módulo 1** a **Módulo 17**; as aulas, como **Aula 01**, **Aula 02**… pela ordem do manifesto, reiniciando a cada módulo. Títulos de página, menu, índices, currículo, trilhas, avaliações, laboratórios e referências cruzadas usam os nomes públicos; os IDs técnicos (`M00-L01`…), arquivos, URLs e âncoras não mudam. Regras em `scripts/naming.py`, aplicadas por `make curriculum`.
- Última aula de cada módulo com "Próximos passos": laboratório e avaliação do módulo, atividades integradoras e o módulo seguinte, quando publicado.
- ROADMAP, Como usar a Academy, plano de estudo e matriz de cobertura atualizados para a Release 1 publicada.
- Navegação pública reorganizada em sete grupos: Início, Começar, Fundamentals, Prática, Research Library, Currículo e Roadmap, Sobre. Fundamentals agrupa os módulos por nível (Nível 0 — Módulo Inicial e Módulo 1; Nível 1 — Módulo 2), a Research Library deixa de ficar dentro da Prática e não há mais aba Módulos. Os endereços das páginas não mudam.
- Portal atualizado para o Zensical 0.0.72.
- Versões de correção de uma release registradas em `patches` no manifesto, com aprovação e publicação próprias; o manifesto da árvore pública passa a trazer o histórico de versões.

### Removed

- Documentação operacional do repositório de desenvolvimento deixa a árvore pública: Handbook (`internal/`), guia de ambiente local, templates de autoria e padrões internos. As demais páginas mantêm o endereço e as âncoras da v0.1.0.

### Fixed

- A exportação final da v0.1.0 trocou o selo "In Review" por "Published" na legenda de status do currículo, no Modelo de conteúdo e no Design System; legendas e Handbook deixam de ser alterados, com teste de regressão.
- Gabarito da avaliação diagnóstica ainda dizia que os módulos de fundamentos não estavam publicados.
- Nos índices do Módulo Inicial e do Módulo 1, o selo de nível causava rolagem horizontal a 360 px de largura.

## [0.1.0] — 2026-10-27

Release 1 — Fundamentals publicada no GitHub Pages: Módulos 00, 01 e 02 (22 aulas), laboratórios 00 a 02, Caso A, avaliação diagnóstica, avaliações de módulo, avaliação final integradora e modelos. A lista abaixo reúne todo o desenvolvimento até esta primeira publicação.

### Added

- Página institucional para o GitHub Pages antes da Release 1 (`landing/`): objetivo do projeto e fundamentos que serão tratados, sem conteúdo de aulas; gerada por `scripts/export_landing.py` com manifesto verificável e workflows próprios.
- Fundação da plataforma (fase 1):
    - Identidade visual original: logotipos claro e escuro, isotipo, banners, social preview e favicons, gerados por `scripts/build_brand.py`.
    - Portal de documentação com Zensical, modo claro/escuro, busca, navegação em abas, homepage própria e fontes auto-hospedadas.
    - Handbook: Design System, guia editorial, modelo de conteúdo, padrões de diagramas, referência de componentes e fluxo de contribuição.
    - `curriculum/manifest.yml` com 18 módulos planejados e Curriculum Roadmap gerado automaticamente.
    - 13 templates educacionais.
    - 10 fontes de diagramas Mermaid demonstrativos com descrição acessível.
    - Validações: estrutura, manifesto, assets, contraste WCAG, links internos e testes.
    - Workflows de CI, publicação no GitHub Pages e verificação semanal de links externos; Dependabot.
    - Documentação de comunidade: CONTRIBUTING, Código de Conduta, política de segurança, issue forms e PR template.
    - Proposta de licenciamento (licença ainda não aplicada).
- Planejamento acadêmico (fase 0):
    - Manifesto v2: seis níveis, três trilhas (Fundamentals, Professional, Advanced), quatro fases, 14 domínios, 18 módulos (M00–M17) com 135 aulas e o complemento C01; coleções de estudos de caso, laboratórios, avaliações e artefatos.
    - `CURRICULUM.md` e páginas do portal geradas do manifesto; grafo de dependências em Mermaid.
    - Mapa de competências, matriz de cobertura, mapeamento de certificações, learning paths e plano de estudos.
    - `curriculum/sources.yml`: registro de fontes com data de verificação e marcação "não verificada".
    - Padrão de aula com 14 elementos e de laboratório com 10 elementos (`authoring/`).
    - `GETTING-STARTED.md` e registro de progresso das entregas.
- MVP educacional (fase 1):
    - Módulo 02 — Introdução à Arquitetura de Segurança, com 8 aulas e 14 diagramas.
    - Caso A — Meridiana Distribuidora: enunciado, solução de referência, As-Is/To-Be e ADR-001 a ADR-003.
    - Laboratório 02 — modelagem arquitetural como código (`examples/lab-02-architecture-modeling/`), com testes.
    - Avaliação diagnóstica e avaliação do Módulo 02, com gabaritos separados e rubricas.
    - Modelos para o estudante: ADR, especificação de requisitos de segurança e checklist de revisão.
- `scripts/check_decision_matrices.py`: recalcula os totais ponderados das matrizes de decisão.
- Research Library:
    - `research/bibliography.yml` (schema 2): 51 referências com IDs estáveis, estados independentes de acesso, redistribuição e verificação, e 106 capítulos ou seções localizados (26 lidos), com páginas impressas.
    - Livros *Security Engineering*, 3ª ed. (Anderson) e *Building Secure and Reliable Systems* (Google); SP 800-160 Vol. 1 Rev. 1 e SP 800-207 com sumários conferidos; catálogo de white papers SABSA; AWS, Azure, Google Cloud e CSA.
    - `research/knowledge-map.yml` com 32 conceitos × fonte × localização × módulo; cinco notas de leitura originais; plano de leitura; registro de verificação com ações manuais pendentes.
    - Revisão bibliográfica retroativa do Módulo 02: `further_reading` e *Leituras de aprofundamento* nas oito aulas, identificadas como posteriores à escrita; pendências registradas.
    - Portal: seção *Research Library* com registro, livros, frameworks, cloud, plano de leitura, matriz de referências, cobertura bibliográfica, metodologia e notas.
    - `scripts/validate_references.py` (CI e deploy): esquema, IDs, citações das aulas, consistência do mapa de conhecimento, referências não usadas, módulos sem fontes e arquivos privados versionados; `--report` e `--links`.
    - `private-research/` ignorada pelo git; PDFs e EPUBs ignorados em todo o repositório.
- Release 1 — Fundamentals (publicada nesta versão):
    - Módulo 00 — Fundamentos de Infraestrutura e Computação (7 aulas) e Módulo 01 — Fundamentos de Segurança (7 aulas).
    - Laboratório 00 — plano de endereçamento e segmentação (`examples/lab-00-network-plan/`, 6 testes) e Laboratório 01 — mecanismos de segurança: integridade, HMAC, armazenamento de senhas e autorização (`examples/lab-01-security-mechanisms/`, 5 testes), executados em diretório limpo.
    - Avaliações dos Módulos 00 e 01 e avaliação final integradora de Fundamentals (Livraria Ipê), com gabaritos comentados e critérios objetivos.
    - Diagramas do fluxo identificação → autenticação → autorização → registro (M01-L01), das funções dos controles ao longo de um incidente (M01-L06), do ciclo de vida de ADRs (M02-L08) e das camadas da arquitetura com serviços de segurança transversais (M02-L02).
- Release 2 — Professional (em desenvolvimento, fora do portal público): Módulos 03 a 10 escritos (59 aulas, em revisão) e Módulo 11 em escrita (9 de 11 aulas em rascunho).
- Modelo de releases progressivas:
    - Seção `releases` no manifesto (R1, R2, R3), validada por `validate_manifest.py`: escopo cumulativo e disjunto, aprovação obrigatória para `approved`/`published`, URL e data só após publicação.
    - `scripts/export_release.py` e alvos `make release-candidate` / `make release-export`: geram a árvore pública só com o escopo aprovado, transformam manifesto e navegação e rodam todas as validações na árvore gerada.
    - Bloco de disponibilidade da homepage gerado do manifesto ("Disponível" só para release publicada).
    - Plano de releases com escopo, isolamento entre desenvolvimento e publicação, procedimento e rollback sem operações destrutivas; checklist de publicação por release.
- Research Library: 189 referências; rastreabilidade conceito → fonte → aula → diagrama na matriz de referências; conceitos dos Módulos 00 a 10.
- Licenças: conteúdo sob CC BY 4.0 (`LICENSE`) e código sob MIT (`LICENSE-CODE`); identidade visual com direitos reservados.

### Changed

- M02-L06 renomeada para "Frameworks, padrões e certificações: NIST, SABSA, TOGAF, CISSP e ISSAP", com a distinção entre framework, método, padrão, arquitetura de referência e certificação profissional e o limite de interpretação da NIST SP 800-160; título atualizado no manifesto, nos índices e nas páginas geradas.
- Alternativas das avaliações de M00, M01 e M02 reescritas para que a correta não seja sistematicamente a mais longa nem a única com justificativa; respostas da avaliação diagnóstica redistribuídas entre as letras. `tests/test_assessments.py` confere gabaritos, resumos e distribuição.
- Referências à ISO/IEC/IEEE 42010 qualificadas de forma uniforme como norma paga não consultada na íntegra.
- Exportação de releases por allowlist explícita (`curriculum/public-allowlist.yml`), com `RELEASE-MANIFEST.yml` na árvore pública (escopo, aprovação, commit de origem e SHA-256 de cada arquivo), verificado por `scripts/verify_release_manifest.py`; o modo final exige o commit aprovado pelo mantenedor e recusa mudanças posteriores.
- Deploy no GitHub Pages exige a tag da release aprovada apontando para o commit atual da `main`, manifesto de release íntegro e aprovado, verificação de atribuição de autoria e testes.
- Padrões do projeto em `PROJECT-STANDARDS.md`, com a política de autoria e créditos; `scripts/check_attribution.py` no `make check`, no CI, na exportação e no deploy.
- Relatórios de processo (progresso, plano de releases, pacotes de revisão, auditorias) ficam só no repositório de desenvolvimento.
- `curriculum/sources.yml` substituído por `research/bibliography.yml`; IDs de fontes migrados para o padrão estável em maiúsculas.
- Publicação no GitHub Pages congelada: o deploy só roda manualmente (`workflow_dispatch` com confirmação), sem gatilho em push.
- Verificação semanal de links passa a incluir o registro bibliográfico.
- Templates de autoria movidos de `templates/` para `authoring/`; campo `level` substituído por `tier`.
- Páginas `in-review` podem entrar na navegação em branches de revisão; o deploy (`--release`) exige `published`.
- Jornada de aprendizagem do README e da homepage atualizada para seis níveis.
- README, roadmap, learning paths e fluxo de contribuição reorganizados em torno das três releases; a versão `1.0.0` passa a corresponder à formação completa revisada.
- Testes do manifesto independentes do estado atual do conteúdo, para rodarem também na árvore pública exportada.

### Fixed

- M01-L05 apresentava forward secrecy como propriedade de todo handshake TLS 1.3: o texto agora distingue o handshake autenticado por certificado (DH efêmero e `CertificateVerify`) dos modos com chave pré-compartilhada (PSK isolado sem forward secrecy; 0-RTT sem forward secrecy e sujeito a replay) e descreve o mTLS, conforme o RFC 9846 (§2, §2.2 e §2.3).
- LAB-00 informava 6 achados altos e 4 médios no As-Is; a ferramenta produz 8 altos, 2 médios e 1 baixo. Enunciado corrigido, com teste que fixa as contagens.
- M00-L06: afirmação estatística sobre a origem de incidentes em cloud, sem fonte, reformulada.
- Diagramas ilegíveis no portal: a figura era ajustada à largura da legenda (agora ocupa a coluna de conteúdo) e 19 diagramas largos da Release 1 passaram de `flowchart LR` para `flowchart TB`; regra de largura documentada no guia de diagramas.
- A alternativa "(c)" de questões e gabaritos era exibida como "©" pela extensão de símbolos tipográficos; a conversão foi desativada, com teste de regressão.
- Exercícios de decisão de M00, M01 e M02-L08 sem a matriz ponderada exigida pelo modelo de conteúdo: alternativas, critérios e matrizes acrescentados, mantendo as recomendações.
- Redação do Business Attributes Profile do SABSA alinhada ao W100 (M02-L06 e M02-L07): definição e métrica; a justificativa por atributo é identificada como prática recomendada pelo curso.
- Fluxo de contribuição deixava a entender que o merge na `main` disparava o deploy; o deploy é manual.
- Referências ao white paper SABSA W101 corrigidas: download direto confirmado no catálogo oficial (antes "forma de acesso não confirmada").
- Detecção de marcadores de rascunho passa a diferenciar maiúsculas (a palavra "todo", em português, não é mais confundida com `TODO`).
