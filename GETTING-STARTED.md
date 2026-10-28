# Getting Started

Como estudar com a Security Architecture Academy. A versão navegável está no portal: [Como usar a Academy](https://andrewsferreira.github.io/security-architecture-academy/getting-started/).

> [!NOTE]
> A formação é publicada em releases cumulativas, uma por nível. A **Release 1** reúne o Módulo Inicial e os Módulos 1 e 2, os Laboratórios 00, 01 e 02, o Caso A, as avaliações e os modelos; a **Release 2** completa o Nível 1 com os Módulos 3 e 4 e a avaliação integradora do Nível 1; os Níveis 2 a 5 vêm depois. A disponibilidade de cada release está na página inicial do portal e no [ROADMAP.md](ROADMAP.md).

## 1. Escolha o ponto de partida

| Seu perfil | Percurso sugerido |
|:---|:---|
| Iniciando na área ou vindo de desenvolvimento ou suporte | [Avaliação diagnóstica](docs/assessments/diagnostic-fundamentals.md) → [Módulo Inicial](docs/modules/00-foundations/index.md) → [Módulo 1](docs/modules/01-security-fundamentals/index.md) → Módulo 2 |
| Vindo de infraestrutura | Diagnóstico → [Módulo 1](docs/modules/01-security-fundamentals/index.md), consultando o Módulo Inicial nos temas indicados → Módulo 2 |
| Analista de segurança migrando para arquitetura | Diagnóstico → revisar no Módulo 1 os temas indicados → [Módulo 2](docs/modules/02-security-architecture/index.md) → [Caso A](docs/case-studies/case-a-meridiana/index.md) → [Laboratório 02](docs/labs/lab-02-architecture-modeling.md) → [avaliação do módulo](docs/assessments/m02-security-architecture.md) → [avaliação integradora do Módulo Inicial ao Módulo 2](docs/assessments/fundamentals-final.md) → [Módulo 3](docs/modules/03-governance-risk/index.md) → [Módulo 4](docs/modules/04-threat-modeling/index.md) → [avaliação integradora do Nível 1](docs/assessments/level-1-integrative.md) |
| Já atua como arquiteto | [Mapa de competências](docs/curriculum/competencies.md) → avaliação do módulo → aulas para as lacunas |
| Preparando-se para certificações | [Mapeamento de certificações](docs/certification-mapping/index.md), como guia complementar ao material oficial |

Um cronograma de 16 semanas está no [plano de estudos](docs/learning-paths/study-plan.md). O currículo completo — 18 módulos, 135 aulas e um complemento — está em [CURRICULUM.md](CURRICULUM.md).

## 2. Estude cada aula na ordem

Cada aula tem a mesma estrutura: conceito, fundamentos técnicos, exemplo empresarial, arquitetura tradicional *versus* recomendada, aplicabilidade em on-premises, cloud e híbrido, especificação e validação, trade-offs, checklist, questões e um exercício de decisão com matriz ponderada. **Responda antes de abrir as respostas.**

## 3. Pratique

- **Estudo de caso:** escreva a sua solução antes de ler a de referência.
- **Laboratórios:** rodam localmente, sem custo, com Python 3.11+. Os Laboratórios [00](docs/labs/lab-00-network-plan.md) e [01](docs/labs/lab-01-security-mechanisms.md) usam só a biblioteca padrão; o [02](docs/labs/lab-02-architecture-modeling.md) requer PyYAML:

  ```bash
  git clone https://github.com/andrewsferreira/security-architecture-academy.git
  cd security-architecture-academy/examples/lab-02-architecture-modeling
  python3 -m venv .venv && source .venv/bin/activate
  pip install pyyaml
  python archcheck.py --help
  ```

- **Modelos:** use os [modelos de ADR, requisitos e revisão](docs/artifacts/index.md) nas suas entregas.

## 4. Avalie-se

As avaliações são baseadas em competência. Os gabaritos ficam em arquivos separados (`docs/assessments/answers/`) — consulte só depois de responder.

## 5. Rodar o portal localmente

```bash
make install     # .venv com dependências fixadas
make serve       # http://localhost:8000/security-architecture-academy/
```

Sem `make`: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements-dev.txt` e depois `python -m zensical serve`.

## Princípios

- Dados sempre fictícios; domínios `example.com` e endereços de documentação.
- Afirmações normativas com fonte, versão e data. As fontes ficam na [Research Library](research/README.md), com edição conferida, condições de acesso e redistribuição e a localização de cada conceito; fontes não confirmadas ficam como **Pendente**.
- Conceitos antes de produtos.
- Nenhum laboratório exige gasto; riscos de cobrança são avisados explicitamente.
