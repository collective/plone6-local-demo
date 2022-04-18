### Defensive settings for make:
#     https://tech.davis-hansson.com/p/make/
SHELL:=bash
.ONESHELL:
.SHELLFLAGS:=-xeu -o pipefail -O inherit_errexit -c
.SILENT:
.DELETE_ON_ERROR:
MAKEFLAGS+=--warn-undefined-variables
MAKEFLAGS+=--no-builtin-rules

# We like colors
# From: https://coderwall.com/p/izxssa/colored-makefile-for-golang-projects
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
YELLOW=`tput setaf 3`

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## remove virtualenv
	rm -Rf bin include lib lib64 pyvenv.cfg

bin/pip:
	@echo "$(GREEN)==> Setup Virtual Env$(RESET)"
	python -m venv .
	bin/pip install -U pip setuptools
	bin/pip install -r requirements.txt

.PHONY: start
start: ## Start containers
	@echo "$(GREEN)==> Start containers$(RESET)"
	@docker-compose up -d --build

.PHONY: stop
stop: ## Stop containers
	@echo "$(RED)==> Stop containers$(RESET)"
	@docker-compose down

.PHONY: run
run: bin/pip ## Start containers, and populate demo content
	@echo "$(GREEN)==> Start containers$(RESET)"
	@docker-compose up -d --build
	@echo "$(GREEN)==> Populate content$(RESET)"
	bin/python populate_plone.py
	@echo "$(GREEN)==> Done$(RESET)"
