.PHONY: install

# upgrades and installs dependencies for application
install:


	python --version; which python

	@if ! python -c "import sys; sys.exit(0 if sys.version_info >= (3, 12) else 1)" 2>/dev/null; then \
		echo "Error: Python 3.12+ required but not found"; \
		exit 1; \
	fi

	rm -rf venv
	python -m venv venv


	@echo "Upgrading and installing requirements..."
	./scripts/upgrade_dependencies.sh

	venv/bin/pre-commit install




