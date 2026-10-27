# private-research/

Pasta **local e privada** para cópias de pesquisa de obras de terceiros — PDFs de livros, normas e white papers baixados legalmente para estudo.

- Tudo nesta pasta, exceto este arquivo, é ignorado pelo git (`.gitignore`). PDFs e EPUBs são ignorados em todo o repositório.
- `scripts/validate_references.py` falha se qualquer arquivo daqui, ou qualquer PDF/EPUB, estiver versionado.
- O portal é construído a partir de `docs/`; nada desta pasta entra no site nem nos artefatos do GitHub Actions.
- Acesso gratuito **não** é licença de redistribuição. Nunca mova estes arquivos para `docs/`, `assets/` ou `research/`.

Organização sugerida, com o ID de `research/bibliography.yml`:

```text
private-research/
├── BOOK-ANDERSON-SE3/      # PDFs por capítulo da página do autor
├── NIST-SP800-160-V1R1/
├── NIST-SP800-207/
└── sabsa/                  # W101, W105... — conferir o SHA256 publicado no catálogo
```

Downloads pendentes de ação manual estão listados em `research/source-verification.md`.
