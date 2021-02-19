#!/bin/bash 

# Title:         run_safety_scan_for_cve.sh
# Author:        ryan.gordon1@ibm.com
# Description:   A CI/CD script which uses the security tool safety to scan 1 or more recently changed projects.
#                   when a project is changed, committed and pushed this script will run attempt to install each package and then run a scan.
#                   
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
    echo "Running a cve security scan for $package"
    # Install the package and all its deps. 
    python $package/setup.py install 

    # Perform a safety check printing all info to job logs
    safety check --full-report
    # Get the exit code of the safety scan 
    last_status=$?;

    if [ $last_status -ne 0 ]; then
            echo "Security Scan failure for $package which gave an exit code of $last_status"
            status=$last_status;
    fi

done
echo "CVE Safety security scan of packages complete.  Final Status $status"
exit $status

