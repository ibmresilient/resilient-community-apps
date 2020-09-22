#!/bin/bash
# This script will create a git tag adding the jenkins build number.
# we're only looking at the tags in the form of v<version>
libVersion=$(git describe --tags | grep -o "v[0-9]*.[0-9]*.[0-9]*" | cut -d "." -f 1,2)

echo Creating tag...
git tag -a $libVersion.$BUILD_NUMBER -m "$libVersion Build $BUILD_NUMBER"


