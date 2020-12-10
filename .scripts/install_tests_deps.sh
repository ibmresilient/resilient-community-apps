#!/bin/bash -e

pip install tox
pip install pylint
pip install pytest

./install_resilient_api.sh