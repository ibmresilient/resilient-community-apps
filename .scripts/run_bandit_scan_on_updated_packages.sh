#!/bin/bash

# Title:         run_bandit_scan_on_updated_packages.sh
# Author:        ryan.gordon1@ibm.com
# Description:   A CI/CD script which uses the code analysis tool bandit to scan 1 or more recently changed projects.
#                   when a project is changed committed and pushed this script will run a scan on each package.
#                   Bandit has tiers of errors and for now we only so High and Medium severity
#                   When these are found for any newly updated packages the script fails.
# Version:       1.0.0
# Release notes
# 1.0.0 Initial Release

# Declare an array that will hold the fn_ or rc_ packages 
packages_that_have_been_changed=()

# For every file in the diff 
for file in $(git diff --name-only HEAD~0 HEAD~1); 
do 
    # If the file contains either fn_ or rc_ in the path 
    if [[ $file =~ (fn_|rc-)+ ]]; 
    then 
    # Strip everything except the first directory in the path (integration name) and append to an array
    packages_that_have_been_changed+=($(echo "$file" | awk -F "/" '{print $1}')); 
    fi
done

# Make a new array which acts as a Set to gather only unique package names 
INTEGRATIONS=($(for v in "${packages_that_have_been_changed[@]}"; do echo "$v";done| sort| uniq| xargs));


if [ -z "$INTEGRATIONS" ]
then
      echo "Did not find any integrations that were modified"
      exit 0
else
      echo "Most recently modified integrations from last commit show as : ${INTEGRATIONS}"
fi
      
for integration in ${INTEGRATIONS[@]};
do 
    echo "Running a bandit security scan for $integration"
    # Perform a bandit security scan on the given integration/app and suppress any Low level warnings. 
    bandit -r $integration -ll 
    # Get the exit code of the bandit scan 
    last_status=$?;

    if [ $last_status -ne 0 ]; then
            printf 'Security Scan failure for %s which gave an exit code of [%d]\n' $integration $last_status;
            status=$last_status;
    fi

done
printf 'Bandit security scan of packages complete.  Final Status [%d]\n' $status;
exit $status

