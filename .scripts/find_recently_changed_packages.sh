#!/bin/bash -x

# Title:         find_recently_changed_packages.sh
# Author:        ryan.gordon1@ibm.com
# Description:   A CI/CD script which contains a helper function for algorithmically determining 
#                which packages in the repository we should be doing CI/CD actions on based on the work that was 
#                done in the PR
# Version:       1.0.0
# Release notes
# 1.0.0 Initial Release

# Helper function find_recently_changed_packages
# Used by our CI/CD scripts to scour the PR/Pushed branch and find
# - Any packages which were changed that match our naming convention
# - From these packages gather the filepaths
# - Using the filepaths, return a list of project names
# - Filter the list into a Set to ensure we don't test something twice
function find_recently_changed_packages(){

    # Declare an array that will hold the fn_ or rc_ packages 
    packages_that_have_been_changed=()
    
    # Gather a range of commits to find candidate projects to return which were recently modified
    # If the TRAVIS_COMMIT_RANGE is missing, we are not in Travis. Instead get latest commit (Possibly running locally)
    # If the TRAVIS_COMMIT_RANGE is defined, use that as a convenience to get all commits that were pushed.
    if [ -z $TRAVIS_COMMIT_RANGE ]; then
        echo "No TRAVIS_COMMIT_RANGE found using most recent commit"
        commit_range=$(git diff --name-only HEAD~0 HEAD~1) 
    else 
        echo "TRAVIS_COMMIT_RANGE was defined, using this to find commit range"
        commit_range=$(git diff --name-only ${TRAVIS_COMMIT_RANGE/.../..})
    fi
    # For every file in the PR/commit diff
    # Replacing ... w/ ..: https://github.com/travis-ci/travis-ci/issues/4596
    for file in ${commit_range}; 
    do 
        # If the file contains either fn_ or rc_ in the path 
        if [[ $file =~ (fn_|rc-)+ ]]; then 
            # Strip everything except the first directory in the path (integration name) and append to an array
            packages_that_have_been_changed+=($(echo "$file" | awk -F "/" '{print $1}')); 
        fi
    done

    # Make a new array which acts as a Set to gather only unique package names 
    PACKAGES=($(for v in "${packages_that_have_been_changed[@]}"; do echo "$v";done| sort| uniq| xargs));


    if [ -z "$PACKAGES" ]; then
        echo "Did not find any packages that were modified"
        # We're using return and not exit, because we are sourcing this script and don't want to kill the job
        return 0
    else
        echo "Most recently modified packages from last commit show as : ${PACKAGES}"
        # echo the $PACKAGES so any script, which calls this can get them, we can only use numbers with the return keyword in bash
        echo "$PACKAGES" 
    fi
}