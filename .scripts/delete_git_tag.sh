#!/bin/bash
# This script will delete the latest git tag.
# This script will always run in jenkins after the script generate_git_tag.sh.
echo Deleting tag...
latestTag=$(git describe --tags)
git tag -d $latestTag
