#!/bin/bash

###########################################
# Upgrade python dependencies
# 1. Upgrade pip
# 2. Upgrade pip-tools
# 3. Upgrade setuptools
# 4. Upgrade requirements/requirements-prod.txt
# 5. Upgrade requirements/requirements-dev.txt
###########################################

# Virtual environment path
VENV_NAME="venv"

set -e


upgrade_core_tools() {
    echo "Upgrading core pip tools..."
    "$VENV_NAME/bin/pip" install --upgrade pip
    "$VENV_NAME/bin/pip" install --upgrade pip-tools
    "$VENV_NAME/bin/pip" install --upgrade setuptools
}

upgrade_requirements() {
    echo "Compiling and upgrading requirements..."
    "$VENV_NAME/bin/pip-compile" requirements/requirements-prod.in
    "$VENV_NAME/bin/pip-compile" requirements/requirements-dev.in
    "$VENV_NAME/bin/pip" install --upgrade -r requirements/requirements-dev.txt
}

main() {
    echo "Starting typocalypse dependency upgrade process..."

    upgrade_core_tools
    upgrade_requirements

    echo "Typocalypse dependency upgrade completed successfully!"
}

# Execute main function in subshell to prevent crashing parent shell
(
    main "$@"
)