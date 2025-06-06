# Run tests using Poetry's virtual environment
.PHONY: test
test:
	poetry run pytest tests/

# Install dependencies from pyproject.toml
.PHONY: install
install:
	poetry install --no-root