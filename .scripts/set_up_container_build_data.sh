#!/bin/bash
# This script pulls out the name of the integration out of the tag pushed
# It then pulls out current version of the integration from its setup.py

export INTEGRATION_NAME=$(echo $TRAVIS_TAG | cut -d "/" -f 2)

setup_file="$(dirname $BASH_SOURCE)/../$INTEGRATION_NAME/setup.py"

if [ ! -e "$setup_file" ]
then
    echo "Chosen integration $INTEGRATION_NAME doesn't have setup.py"
    exit 1
fi

export INTEGRATION_VERSION=$(cat "$setup_file" | grep -o "version=['\"][0-9.]*['\"]" | grep -oE "[0-9.]+")

echo "Integration's version is: $INTEGRATION_VERSION"

exit 0