# Laboratório 00 — Plano de endereçamento e segmentação

Ferramenta e modelos do [Laboratório 00](../../docs/labs/lab-00-network-plan.md) da Security Architecture Academy.

| Arquivo | Conteúdo |
|:---|:---|
| `netplan.py` | Lê um plano de rede em JSON e aplica regras de revisão (somente biblioteca padrão) |
| `models/meridiana-as-is.json` | Plano As-Is da Meridiana (ponto de partida) |
| `solutions/meridiana-to-be.json` | Plano To-Be de referência — consulte só depois de fazer o seu |
| `tests/` | Testes automatizados, executados no CI |

```bash
python3 netplan.py models/meridiana-as-is.json --markdown as-is.md
```

Ferramenta educacional, com dados fictícios. As regras ilustram o raciocínio de revisão e não substituem a análise de um plano real.
