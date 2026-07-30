PYTHON_IMAGE ?= python:3.12-slim
TEST_FILE ?= tests
INPUT_FILE ?= testdata/sample_clubes.jsonl

ifneq (,$(wildcard .env))
include .env
export
endif

.PHONY: install test test-shell test-file run

install:
	@if [ ! -f .env ] && [ -f .env.example ]; then cp .env.example .env; echo "Arquivo .env criado a partir de .env.example"; fi
	@docker pull $(PYTHON_IMAGE)

test:
	@docker run --rm -v $(PWD):/app -w /app $(PYTHON_IMAGE) sh -lc "pip install --no-cache-dir -r requirements.txt && PYTHONPATH=/app pytest -q"

test-file:
	@docker run --rm -v $(PWD):/app -w /app $(PYTHON_IMAGE) sh -lc "pip install --no-cache-dir -r requirements.txt && PYTHONPATH=/app pytest -q $(TEST_FILE)"

run:
	@test -f $(INPUT_FILE) || (echo "Arquivo de entrada não encontrado: $(INPUT_FILE)" && exit 1)
	@docker run --rm -v $(PWD):/app -w /app $(PYTHON_IMAGE) sh -lc "pip install --no-cache-dir -r requirements.txt && PYTHONPATH=/app python -m batch_clubs $(INPUT_FILE)"


