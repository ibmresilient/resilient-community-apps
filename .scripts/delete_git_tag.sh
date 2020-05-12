#!/bin/bash
# This script will delete the latest git tag.
# This script will always run in jenkins after the script generate_git_tag.sh.
echo Deleting tag...
latestTag=$(git tag --list | grep "v[0-9]" | tail -n 1)
git tag -d $latestTag
