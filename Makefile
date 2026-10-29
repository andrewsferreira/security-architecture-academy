# Security Architecture Academy — comandos de desenvolvimento
# Uso: make help

VENV    ?= .venv
PYTHON  ?= $(if $(wildcard $(VENV)/bin/python),$(VENV)/bin/python,python3)
ZENSICAL = $(PYTHON) -m zensical
MMDC    ?= npx --yes @mermaid-js/mermaid-cli@12.0.0

.DEFAULT_GOAL := help
.PHONY: help install serve build curriculum check validate test lint diagrams brand brand-sync clean references release-candidate release-export

help: ## Lista os comandos disponíveis
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Cria o ambiente virtual e instala as dependências
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements-dev.txt

serve: ## Inicia o portal com recarga automática (http://localhost:8000)
	$(ZENSICAL) serve

build: ## Gera o site estático em site/
	$(ZENSICAL) build --clean

curriculum: ## Regenera CURRICULUM.md e as páginas geradas do currículo e da Research Library
	$(PYTHON) scripts/render_curriculum.py

check: ## Validações rápidas (sem build)
	$(PYTHON) scripts/check_structure.py
	$(PYTHON) scripts/validate_manifest.py
	$(PYTHON) scripts/render_curriculum.py --check
	$(PYTHON) scripts/check_assets.py
	$(PYTHON) scripts/check_contrast.py
	$(PYTHON) scripts/check_decision_matrices.py
	$(PYTHON) scripts/validate_references.py
	$(PYTHON) scripts/check_attribution.py
	$(PYTHON) scripts/verify_release_manifest.py
	$(PYTHON) scripts/check_changelog.py

validate: check build ## Validação completa: estrutura, manifesto, assets, build e links
	$(PYTHON) scripts/check_links.py

test: ## Testes unitários dos scripts de validação
	$(PYTHON) -m pytest -q tests examples

references: ## Relatório de cobertura bibliográfica da Research Library
	$(PYTHON) scripts/validate_references.py --report

lint: ## Markdown lint (requer Node.js)
	npx --yes markdownlint-cli2@0.24.0

diagrams: ## Valida a sintaxe das fontes Mermaid (requer Node.js e Chrome)
	@mkdir -p .cache/diagrams
	@for f in assets/diagrams/*.mmd; do \
	  echo "  $$f"; $(MMDC) -q -i $$f -o .cache/diagrams/$$(basename $$f .mmd).svg || exit 1; \
	done

brand: ## Regenera a identidade visual (requer requirements-brand.txt e fontes Inter)
	$(PYTHON) scripts/build_brand.py

brand-sync: ## Copia assets/branding para docs/assets/branding
	cp assets/branding/*.svg assets/branding/*.png docs/assets/branding/

release-candidate: ## Gera e valida a árvore pública candidata de uma release (RELEASE=R1)
	$(PYTHON) scripts/export_release.py --release $(RELEASE) --mode candidate --out build/candidate-$(RELEASE)

release-export: ## Gera a árvore pública final (exige aprovação registrada no manifesto) (RELEASE=R1)
	$(PYTHON) scripts/export_release.py --release $(RELEASE) --mode final --out build/public-$(RELEASE)

clean: ## Remove artefatos de build
	rm -rf site .cache build
