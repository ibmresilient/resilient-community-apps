#!/bin/bash -x 

# Title:         run_bandit_scan_on_updated_packages.sh
# Author:        ryan.gordon1@ibm.com
# Description:   A CI/CD script which uses the code analysis tool bandit to scan 1 or more recently changed projects.
#                   when a project is changed committed and pushed this script will run a scan on each package.
#                   Bandit has tiers of errors and for now we only so High and Medium severity
#                   When these are found for any newly updated packages the script fails.
# Version:       1.0.0
# Release notes
# 1.0.0 Initial Release
set -x 
# Source the script which finds recent changes 
. .scripts/find_recently_changed_packages.sh
# Call the function which will search for packages, the result will be available via the $PACKAGES variable defined in that script
find_recently_changed_packages

# Loop over all recently changed package
for package in ${PACKAGES[@]};
do 
    echo "Running a bandit security scan for $package"
    # Perform a bandit security scan on the given integration/app and suppress any Low level warnings. 
    bandit -r $package -ll 
    # Get the exit code of the bandit scan 
    last_status=$?;

    if [ $last_status -ne 0 ]; then
            printf 'Security Scan failure for %s which gave an exit code of [%d]\n' $package $last_status;
            status=$last_status;
    fi

done
printf 'Bandit security scan of packages complete.  Final Status [%d]\n' $status;
exit $status

