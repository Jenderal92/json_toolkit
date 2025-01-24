#!/bin/bash
# lint_code.sh

# Run Flake8 for linting
flake8 json_toolkit tests scripts

# Run Pylint for linting
pylint json_toolkit tests scripts
