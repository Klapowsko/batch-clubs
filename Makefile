PYTHON_IMAGE ?= python:3.12-slim
TEST_FILE ?= tests

.PHONY: install test test-shell test-file

install:
	@docker pull $(PYTHON_IMAGE)

test:
	@docker run --rm -v $(PWD):/app -w /app $(PYTHON_IMAGE) sh -lc "pip install --no-cache-dir -r requirements.txt && PYTHONPATH=/app pytest -q"

test-file:
	@docker run --rm -v $(PWD):/app -w /app $(PYTHON_IMAGE) sh -lc "pip install --no-cache-dir -r requirements.txt && PYTHONPATH=/app pytest -q $(TEST_FILE)"


