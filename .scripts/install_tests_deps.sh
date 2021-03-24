#!/bin/bash -e
readonly CUR_DIR=$( cd $(dirname $0) ; pwd -P )
pip install tox
pip install pylint
pip install pytest
pip install --upgrade attrs
pip install setuptools-scm==5.0.2

${CUR_DIR}/install_resilient_api.sh