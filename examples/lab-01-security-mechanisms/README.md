# Laboratório 01 — Mecanismos de segurança na prática

Ferramenta e dados do [Laboratório 01](../../docs/labs/lab-01-security-mechanisms.md) da Security Architecture Academy.

| Arquivo | Conteúdo |
|:---|:---|
| `seclab.py` | Quatro experimentos: integridade, HMAC, armazenamento de senhas e autorização (somente biblioteca padrão) |
| `data/` | Documentos, usuários e lista de palavras **sintéticos** |
| `tests/` | Testes automatizados, executados no CI |

```bash
python3 seclab.py integrity build data/docs manifest.json
python3 seclab.py hmac demo
python3 seclab.py passwords demo
python3 seclab.py authz demo
```

Ferramenta educacional, com dados fictícios. Não use os exemplos como implementação de produção.
