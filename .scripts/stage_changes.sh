#!/bin/bash

# Utility helper to move things around on the internal repo.
# Run from the `.scripts/` directory
branch_to_stage_from=INT-2163/dockerfile_final


# get the latest revision from the dockerfile final branch 
git checkout branch_to_stage_from && git pull

# get onto our staging branch and pull incase there has been changes
git checkout staging_containers_apphost && git pull
paths_to_stage=(
    "Dockerfile"
    "apikey_permissions.txt"
    "entrypoint.sh"
)

while read line
do
    # check out a specific directory from the master branch
    # Remove the existing package first 
    # rm -rf ../$line
    # Copy over everything and overwrite, all changes from the branch brough over
    # git checkout INT-2163/dockerfile_final ../$line
    # Only copy everything in the dist folder, and the named paths in paths_to_stage
    git checkout branch_to_stage_from ../$line/dist/
    for i in "${paths_to_stage[@]}"; do
        git checkout branch_to_stage_from ../$line/$i
    done
done <<EOM
fn_utilities
EOM

