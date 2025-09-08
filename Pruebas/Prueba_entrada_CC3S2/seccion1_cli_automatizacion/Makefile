SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c

.PHONY: help tools report all
help: ## Mostrar ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | sed 's/:.*##/: /'

tools: ## Verifica binarios requeridos
	@echo "Verificando herramientas requeridas..."
	@for b in git bash make python3 pytest curl dig ss jq; do \
	  if ! command -v $$b >/dev/null; then \
	    echo "  Falta: $$b"; \
	  fi; \
	done
	@echo "OK herramientas restantes"

report: ## Genera reportes HTTP/DNS/TLS/puertos
	@echo "Generando reportes..."
	@bash scripts/syscheck.sh

all: tools report ## Ejecuta todo
