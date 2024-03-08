CURRENT_DIRECTORY := $(shell pwd)
TESTSCOPE = apps
TESTFLAGS = --with-timer --timer-top-n 10 --keepdb


help:
	@echo "Docker Compose Help"
	@echo "-----------------------"
	@echo ""
	@echo "Run tests to ensure current state is good:"
	@echo "    make test"
	@echo ""
	@echo "If tests pass, add fixture data and start up the api:"
	@echo "    make begin"
	@echo ""
	@echo "Really, really start over:"
	@echo "    make clean"
	@echo ""
	@echo "See contents of Makefile for more targets."
.PHONY: help

install-dependencies:
	poetry install
.PHONY: install-dependencies

isort:
	 isort --atomic .
.PHONY: isort

apply-isort:
	isort .
.PHONY: apply-isort

autopep8:
	autopep8 -d .
.PHONY: autopep8

flake8:
	flake8 -v --count --show-source --statistics
.PHONY: flake8

test:
	pytest -n 8 --cov --cov-fail-under=80
.PHONY: test

migrate:
	alembic upgrade head
.PHONY: migrate

make-migration:
	alembic revision --autogenerate
.PHONY: make-migration

server:
	python manage.py runserver 0.0.0.0:8000
.PHONY: server

dev-setup: \
	make-migration \
	migrate
.PHONY: dev-setup

local-ci: \
	blank \
	isort \
	flake8 \
	autopep8
.PHONY: local-ci
