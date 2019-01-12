SHELL=/bin/bash

# Should be exported for sub-makes to see it as an env var.
# The sub-make must be called with make -e (do disable re-definition of env vars)
export timestamp := $(shell date -u +"%Y-%m-%d-%H-%M")
# usr := $(shell id -u):$(shell id -g)
dcrun := docker-compose -f docker-compose.yml -f docker-compose.dev.yml run --rm -e ENV=DEV
dc := docker-compose -f docker-compose.yml -f docker-compose.dev.yml

clean:
	$(dcrun) postgres clean

imagebuild:
	$(dc) build

createcerts:
	$(dcrun) postgres bash -c 'createcerts -n $$HOST_NAME'

createsecret:
	$(dcrun) postgres createsecret_ui

readsecret:
	$(dcrun) postgres readsecret_ui

migrate:
	$(dcrun) django with_django django-admin migrate

createsuperuser:
	$(dcrun) django with_django django-admin createsuperuser

collectstatic:
	$(dcrun) django collectstatic

shell:
	docker-compose run --rm django with_django bash

.PHONY: backup
backup:
	docker-compose run --rm backup backup

restore:
	docker-compose down
	docker-compose run --rm backup restore

build:
	@echo "Building $(timestamp)"
	$(dc) down
	make imagebuild
	$(dcrun) build_js npm install
	$(dcrun) build_js npm run build
	make collectstatic
	make -e docs
	make test
	make imagebuild
	$(dc) down

shell_plus:
	$(dcrun) django with_django django-admin shell_plus

test:
	$(dcrun) django test

# test_keepdb:
# 	docker-compose run --rm django test keepdb
#
# coverage:
# 	docker-compose run --rm django coverage

.PHONY: docs
docs:
	$(dcrun) -e 'VERSION=$(timestamp)' django docs

makemigrations:
	make clean
	$(dcrun) django makemigrations
	make clean

# makemessages:
# 	docker-compose run --rm django makemessages
