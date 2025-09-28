# Actividad 5: Construyendo un pipeline DevOps con Make y Bash

## Parte 1: Construir - Makefile y Bash desde cero

Se creo el siguiente script de Python basico para hacer uso en el makefile:

``` python
def saludo(name):
    return f"Hola, {name}!"

if __name__ == "__main__":
    print(saludo("Jharvy"))
```

Ademas el siguiente Makefile basico con algunos targets implementados:

``` Makefile
SHELL := bash
.SHELLFLAGS := -eu -o pipefile -c
MAKEFLAGS 	+= --warn-undefined-variables --no-builtin-rules
.DELETE_ON_ERRORW:
.DEFAULT_GOAL 	:= help
export LC_ALL	:= C
export LANG 	:= C
export TZ		:= UTC

.PHONY: all build test package clean help init tools check benchmark format dist-clean verify-repo

PYTHON		?= python3
SHELLCHECK	:= shellcheck
SHFMT		:= shfmt
SRC_DIR		:= src
TEST_DIR	:= test
OUT_DIR		:= out
DIST_DIR	:= dist

all: tools lint build test package ## Construir, testear y empaquetar todo

build: $(OUT_DIR)/hello.txt ## Generar out/hello.txt

$(OUT_DIR)/hello.txt: $(SRC_DIR)/hello.py
	mkdir -p $(@D)
	$(PYTHON) $< > $@

clean: ## Limpiar archivos generados
	rm -rf $(OUT_DIR) $(DIST_DIR)

help: ## Mostrar ayuda
	@grep -E '^[a-zA-Z0-9_-]+:.*?## ' $(MAKEFILE_LIST) | awk -F':|##' '{printf "  %-12s %s\n", $$1, $$3}'
```

