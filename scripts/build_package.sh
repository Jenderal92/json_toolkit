#!/bin/bash
# build_package.sh

# Build the package using setuptools
python setup.py sdist bdist_wheel
