#!/bin/bash -x

# Title:         run_safety_scan_for_cve.sh
# Description:   A CI/CD script which uses the security tool safety to scan 1 or more recently changed projects.
#                when a project is changed, committed and pushed this script will run attempt to install each package and then run a scan.

# param $1: (required) which package_name to run the scan for

###############
## Variables ##
###############
PACKAGE_NAME=$1
status=0

##################
## Check params ##
##################
if [ -z "$1" ] ; then
    echo "ERROR: Must provide PACKAGE_NAME as first parameter"
    exit 1
fi

###############
## Functions ##
###############
print_msg () {
    printf "\n--------------------\n$1\n--------------------\n"
}

###########
## Start ##
###########

if [ "$PACKAGE_NAME" == "build" ] ; then
    print_msg "Latest commit is a modifying thee build. Not running and package's tests"
    exit 0
fi

print_msg "Installing $PACKAGE_NAME"
# Install the package and all its deps.
python $PACKAGE_NAME/setup.py -q install

echo "Running CVE security scan for $PACKAGE_NAME"
# Perform a safety check printing all info to job logs
# NOTE: as of Dec 14 2021 Travis pulls in a version of pipenv
# that is not compliant with safety check. since we don't use that
# in our apps, we ignore that cve here (ID = 38334)
safety check --full-report --ignore 38334
# Get the exit code of the safety scan
last_status=$?;

if [ $last_status -ne 0 ]; then
    echo "Security Scan failure for $PACKAGE_NAME which gave an exit code of $last_status"
    status=$last_status;
fi

print_msg "CVE Safety security scan of $PACKAGE_NAME complete. Final Status $status"
exit $status
