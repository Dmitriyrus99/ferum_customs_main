APP = ferum_customs
SITE ?= dev.localhost
BENCH ?= frappe-bench

.PHONY: setup start update fixtures test-site test install lint bench

setup:
	bench get-app $(APP) --source-path . || true
	bench --site $(SITE) install-app $(APP)
	bench --site $(SITE) migrate

start:
	bench start

update:
	bench --site $(SITE) migrate
	bench build
	bench restart

fixtures:
	bench --site $(SITE) export-fixtures

test-site:
	./scripts/setup_test_site.sh

test: test-site
	pytest -q

install:
	pip install -e .
	pip install -r dev-requirements.txt
	pre-commit install

lint:
	pre-commit run --all-files

bench:
	bench start
