# Security Engineering (3ª edição) — Ross Anderson

**Referência:** `BOOK-ANDERSON-SE3` · Nota de leitura original da Security Architecture Academy · Revisão de 2026-10-23

## Identificação

| Campo | Valor |
|:---|:---|
| Título | *Security Engineering: A Guide to Building Dependable Distributed Systems* |
| Autor | Ross Anderson |
| Edição | Third Edition — capítulos publicados de abril de 2019 a setembro de 2020 |
| Editora | Wiley |
| Acesso | PDF gratuito por capítulo e integral na [página do autor](https://www.cl.cam.ac.uk/archive/rja14/book.html), por acordo com a editora |
| Redistribuição | **Proibida** — a obra continua protegida por direitos autorais; a licença Creative Commons citada pelo autor se aplica aos slides, não ao livro |

Capítulos efetivamente consultados nesta revisão: **1, 6, 8, 10, 27 e 28**. Os demais foram identificados apenas pelo sumário oficial. Páginas são as impressas (cabeçalhos do PDF por capítulo) e podem variar em uma unidade.

## Relevância

Anderson trata segurança como **engenharia de sistemas sujeitos a adversários**, não como lista de produtos. Para um arquiteto, o livro oferece duas coisas raras: um vocabulário preciso (o que é confiável, o que é apenas confiado) e um acervo de casos em que sistemas bem-intencionados falharam por razões de incentivo, usabilidade ou mudança de contexto. É a melhor base para o raciocínio adversarial que as aulas da Academy exigem.

## Conceitos fundamentais

**Quatro perspectivas de qualquer controle (Cap. 1, §1.2, p. 4).** Toda proteção pode ser analisada por *policy* (o que se quer alcançar), *mechanism* (com o que), *assurance* (quanto se pode confiar no mecanismo) e *incentive* (o que motiva quem defende e quem ataca). Na prática de arquitetura, a quarta perspectiva é a que mais falta: um controle tecnicamente correto falha quando quem o opera não tem motivo para mantê-lo.

**Trusted não é trustworthy (Cap. 1, §1.7, p. 11).** Um componente *confiado* é aquele cuja falha quebra a política; um componente *confiável* é aquele que não falha. Uma arquitetura madura reduz o conjunto de componentes confiados e exige evidência de que cada um deles merece essa posição. Essa distinção sustenta, por exemplo, a ideia de minimizar o *trusted computing base* e a de não confiar implicitamente na rede interna.

**Controle de acesso existe em camadas (Cap. 6, §6.1–6.3, pp. 207–231).** Aplicação, middleware, sistema operacional e hardware aplicam controles de natureza diferente. Camadas superiores são mais expressivas e, em geral, menos confiáveis. A mesma regra de negócio costuma ser reimplementada em várias camadas — e a inconsistência entre elas é fonte frequente de falhas.

**Como o ambiente corrói controles (Cap. 6, §6.4.5, p. 238).** Mecanismos projetados para um contexto continuam em uso quando o contexto muda. É o argumento técnico para revisões periódicas de padrões e para exceções com prazo.

**Incentivos e economia (Cap. 8, §8.3 e §8.6, pp. 281–308).** Externalidades, informação assimétrica e incentivos desalinhados explicam falhas que nenhuma análise puramente técnica explica: quem guarda o sistema nem sempre é quem paga pela falha; compradores não conseguem distinguir produtos seguros de inseguros; fornecedores priorizam participação de mercado.

**Fronteiras entre pares (Cap. 10, pp. 341–370).** Além da proteção hierárquica, há a necessidade de impedir fluxos *laterais* entre grupos de mesmo nível — clientes concorrentes, unidades de negócio, áreas de um hospital. O capítulo mostra que essas fronteiras dependem de governança, consentimento e incentivos tanto quanto de tecnologia.

**Desenvolvimento seguro e risco (Cap. 27, pp. 965–995).** Gestão de risco com dados, suposições e política misturados; técnicas da engenharia de segurança funcional (análise de perigos, árvores de falha, FMEA) aplicadas a ameaças; e a evolução de métodos top-down para iterativos e DevSecOps.

**Assurance como processo (Cap. 28, pp. 1015–1044).** Avaliações e certificações oferecem evidência parcial e sujeita a incentivos próprios. A tendência é passar da certificação pontual para manutenção e correção ao longo de todo o ciclo de vida.

## Capítulos prioritários para a Academy

| Capítulo | Seções-chave | Módulos |
|:---|:---|:---|
| 1 What Is Security Engineering? | §1.2 A framework; §1.7 Definitions | M01, M02 |
| 6 Access Control | §6.2 Operating system access controls; §6.4 What goes wrong | M01, M06, M08 |
| 8 Economics | §8.3 Information economics; §8.6 The economics of security and dependability | M02, M03, M14, M16 |
| 10 Boundaries | §10.2 Compartmentation and the lattice model; §10.4.8 The Chinese Wall | M01, M05, M13 |
| 27 Secure Systems Development | §27.2 Risk management; §27.3 Lessons from safety-critical systems; §27.5 Methodology | M02, M03, M04, M12 |
| 28 Assurance and Sustainability | §28.2 Evaluation; §28.3 Metrics and dynamics of dependability | M03, M14, M16 |

Candidatos para leitura em revisões futuras, pelo sumário: Cap. 2 (oponentes), 4 (protocolos), 7 (sistemas distribuídos), 9 (segurança multinível) e 21 (ataque e defesa de redes).

## Aplicação prática

- **Revisão de arquitetura:** acrescentar às revisões a pergunta "quem tem incentivo para manter este controle funcionando?" ao lado de "o controle funciona?".
- **Classificação de componentes:** listar explicitamente os componentes confiados de uma solução (IdP, broker de privilégios, backup) e a evidência de que são confiáveis.
- **Exceções:** usar o argumento de *environmental creep* para justificar prazo e reavaliação obrigatória de toda exceção.

## Ambientes híbridos

A distinção entre camadas de controle de acesso ajuda a comparar realizações físicas diferentes de um mesmo requisito lógico — por exemplo, autorização por objeto na aplicação (igual em todos os ambientes) e isolamento por hipervisor no datacenter *versus* controles do provedor em cloud. O livro não trata de serviços de cloud específicos; essa adaptação é do arquiteto.

## Arquitetura empresarial

O capítulo de economia é a ponte para governança: decisões de dono do risco, terceirização e contratação de fornecedores mudam incentivos, e portanto mudam a eficácia dos controles. É um bom contraponto a frameworks que tratam controles como itens de checklist.

## Trade-offs

- O livro é extenso e cheio de estudos de caso históricos; ler integralmente não é necessário para avançar na formação.
- Exemplos de plataformas refletem o período de escrita (2019–2020).
- Não é um guia de implementação: não traz configurações, processos corporativos nem modelos de documentação.

## Aplicação educacional

- **M01/M02:** exercício "quatro perspectivas" sobre um controle do Caso A.
- **M03:** debate sobre incentivos do dono do risco e do fornecedor de serviços gerenciados.
- **M04:** comparação entre árvore de ataque e FMEA para o mesmo sistema.
- **M13:** desenho de fronteiras entre unidades de negócio com dados sensíveis.

## Referências

- R. Anderson. *Security Engineering*, 3ª ed. Wiley, 2020. Cap. 1, §1.2 (p. 4) e §1.7 (p. 11); Cap. 6, §6.1–6.4 (pp. 207–238); Cap. 8, §8.3 e §8.6 (pp. 281–308); Cap. 10 (pp. 341–370); Cap. 27, §27.2–27.5 (pp. 966–995); Cap. 28, §28.1–28.3 (pp. 1015–1044). Página do livro: <https://www.cl.cam.ac.uk/archive/rja14/book.html>. Consultado em 2026-10-23.
