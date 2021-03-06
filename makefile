SHELL=/bin/bash

timestamp := $(shell date +"%Y-%m-%d-%H-%M")
usr := $(shell id -u):$(shell id -g)
devcompose := COMPOSE_FILE=docker-compose.yml:docker-compose.dev.yml

createsecret:
	@docker-compose run --rm -u $(usr) postgres createsecret

readsecret:
	@docker-compose run --rm -u $(usr) postgres readsecret

collectstatic:
	$(devcompose) docker-compose run --rm django collectstatic

build:
	$(devcompose) docker-compose down
	docker run --rm -v "$(CURDIR):/src/" ubuntu:bionic-20200219 bash -c "rm -rf /src/static/"
	$(devcompose) docker-compose build
	$(devcompose) docker-compose run --rm build_js npm install
	$(devcompose) docker-compose run --rm build_js build
	$(devcompose) docker-compose run --rm django with_django django-admin createcachetable
	$(devcompose) docker-compose run --rm django collectstatic
	$(devcompose) docker-compose run --rm -e 'VERSION=$(timestamp)' django docs
	$(devcompose) docker-compose build
	$(devcompose) docker-compose down

build_js_only:
	$(devcompose) docker-compose run --rm build_js npm install
	$(devcompose) docker-compose run --rm build_js build

create_dev_certificates:
	docker-compose run --rm -u $(usr) -w /src/.files postgres ./create_dev_certificates.sh

shell_plus:
	docker-compose run --rm django with_django django-admin shell_plus

create_superuser:
	docker-compose run --rm django with_django django-admin createsuperuser

node_bash:
	docker-compose run --rm -u "$(usr)" build_js bash

bash:
	docker-compose run --rm django with_django bash

super_bash:
	docker-compose run --rm django with_django_superuser bash

test:
	docker-compose run --rm django test

test_keepdb:
	docker-compose run --rm django test keepdb

coverage:
	docker-compose run --rm django coverage

.PHONY: docs
docs:
	docker-compose run --rm django docs

migrate:
	docker-compose run --rm django with_django django-admin migrate

makemigrations:
	docker-compose run --rm django makemigrations

makemessages:
	docker-compose run --rm django makemessages

.PHONY: backup
backup:
	docker-compose run --rm backup backup

restore:
	docker-compose down
	docker-compose run --rm backup restore
