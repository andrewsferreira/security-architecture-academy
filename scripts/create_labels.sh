#!/usr/bin/env bash
# Cria (ou atualiza) as labels recomendadas no repositório via GitHub CLI.
# Uso: gh auth login && scripts/create_labels.sh [owner/repo]
set -euo pipefail
REPO="${1:-andrewsferreira/security-architecture-academy}"

label() { gh label create "$1" --repo "$REPO" --color "$2" --description "$3" --force; }

label "type: content"        "1E5EC8" "Conteúdo educacional"
label "type: bug"            "B91C1C" "Erro técnico ou de conteúdo"
label "type: design"         "2CC4DA" "Identidade visual e Design System"
label "type: infrastructure" "475569" "Build, CI e scripts"
label "type: proposal"       "8DB4F5" "Proposta a discutir"
label "level: fundamentals"  "C3D2E8" "Nível Fundamentals"
label "level: professional"  "8DB4F5" "Nível Professional"
label "level: architect"     "5B93F0" "Nível Architect"
label "status: needs-triage" "FBBF24" "Aguardando análise"
label "status: accepted"     "15803D" "Aprovado para execução"
label "status: blocked"      "B45309" "Depende de outra entrega"
label "good first issue"     "0B7F93" "Boa para novos colaboradores"
label "dependencies"         "0C1D36" "Atualizações de dependências"
