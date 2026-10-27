# Getting Started

Como estudar com a Security Architecture Academy. A versão navegável está no portal: [Como usar a Academy](https://andrewsferreira.github.io/security-architecture-academy/getting-started/).

> [!NOTE]
> A formação é publicada em releases cumulativas por nível. A **Release 1 — Fundamentals** reúne os Módulos 00, 01 e 02, os Laboratórios 00, 01 e 02, o Caso A, as avaliações e os modelos para o estudante; as releases Professional e Architect vêm depois. A disponibilidade de cada uma está na página inicial do portal e no [ROADMAP.md](ROADMAP.md).

## 1. Escolha o ponto de partida

| Seu perfil | Percurso sugerido |
|:---|:---|
| Iniciando na área ou vindo de desenvolvimento ou suporte | [Avaliação diagnóstica](docs/assessments/diagnostic-fundamentals.md) → [Módulo 00](docs/modules/00-foundations/index.md) → [Módulo 01](docs/modules/01-security-fundamentals/index.md) → Módulo 02 |
| Vindo de infraestrutura | Diagnóstico → [Módulo 01](docs/modules/01-security-fundamentals/index.md), consultando o Módulo 00 nos temas indicados → Módulo 02 |
| Analista de segurança migrando para arquitetura | Diagnóstico → revisar no Módulo 01 os temas indicados → [Módulo 02](docs/modules/02-security-architecture/index.md) → [Caso A](docs/case-studies/case-a-meridiana/index.md) → [Laboratório 02](docs/labs/lab-02-architecture-modeling.md) → [avaliação do módulo](docs/assessments/m02-security-architecture.md) → [avaliação final de Fundamentals](docs/assessments/fundamentals-final.md) |
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

Detalhes e comandos sem `make` em [Desenvolvimento local](docs/getting-started/local-development.md).

## Princípios

- Dados sempre fictícios; domínios `example.com` e endereços de documentação.
- Afirmações normativas com fonte, versão e data. As fontes ficam na [Research Library](research/README.md), com edição conferida, condições de acesso e redistribuição e a localização de cada conceito; fontes não confirmadas ficam como **Pendente**.
- Conceitos antes de produtos.
- Nenhum laboratório exige gasto; riscos de cobrança são avisados explicitamente.
