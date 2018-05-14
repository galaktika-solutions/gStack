SHELL=/bin/bash

readvar = $(shell cat .env | sed -nr 's/^$(1)=(.*)$$/\1/ p')

timestamp := $(shell date +"%Y-%m-%d-%H-%M")
usr := $(shell id -u):$(shell id -g)
REGISTRY_URL := $(call readvar,REGISTRY_URL)
COMPOSE_PROJECT_NAME := $(call readvar,COMPOSE_PROJECT_NAME)

# self documenting makefile
.DEFAULT_GOAL := help
## Print (this) short summary
help: bold = $(shell tput bold; tput setaf 3)
help: reset = $(shell tput sgr0)
help:
	@echo
	@sed -nr \
		-e '/^## /{s/^## /    /;h;:a;n;/^## /{s/^## /    /;H;ba};' \
		-e '/^[[:alnum:]_\-]+:/ {s/(.+):.*$$/$(bold)\1$(reset):/;G;p};' \
		-e 's/^[[:alnum:]_\-]+://;x}' ${MAKEFILE_LIST}
	@echo

###########
# TARGETS #
###########

run-as-me:
	docker-compose run --rm -u "$(usr)" -v "$(CURDIR):/gstack" -w "/gstack" django bash

## Build the Docker image, tag it and push it to the registry
push: img = $(REGISTRY_URL)/$(COMPOSE_PROJECT_NAME)
push:
	IMAGE_TAG=latest docker-compose build
	docker tag $(img)-postgres:latest $(img):$(timestamp)
	docker push "$(img):latest"
	docker push "$(img):$(timestamp)"
