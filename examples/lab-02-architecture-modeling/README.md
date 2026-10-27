# Laboratório 02 — Modelagem arquitetural como código

Ferramenta e modelos do [Laboratório 02](../../docs/labs/lab-02-architecture-modeling.md) da Security Architecture Academy.

| Arquivo | Conteúdo |
|:---|:---|
| `archcheck.py` | Valida o modelo YAML, gera o diagrama Mermaid e aplica regras de revisão arquitetural |
| `models/meridiana-as-is.yaml` | Modelo As-Is do Caso A (ponto de partida do laboratório) |
| `solutions/meridiana-to-be.yaml` | Modelo To-Be de referência — consulte só depois de fazer o seu |
| `tests/` | Testes automatizados, executados no CI |

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pyyaml
python archcheck.py models/meridiana-as-is.yaml --mermaid as-is.mmd --report as-is.md
```

Ferramenta educacional, com dados fictícios. As regras ilustram o raciocínio de revisão e não substituem uma revisão arquitetural completa.
