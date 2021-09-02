#!/bin/bash -x

# Title:         run_bandit_scan.sh
# Description:   A CI/CD script which uses the code analysis tool bandit to scan 1 or more recently changed projects.
#                when a project is changed committed and pushed this script will run a scan on each package.
#                Bandit has tiers of errors and for now we only so High and Medium severity
#                When these are found for any newly updated packages the script fails.
# Version:       1.0.1

# param $1: (required) which package_name to run the scan for

###############
## Variables ##
###############
PACKAGE_NAME=$1

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

if [ "$PACKAGE_NAME" == "MERGE" ] ; then
    print_msg "Latest commit is a Merge. Not running bandit scan"
    exit 0
fi

print_msg "Running a bandit security scan for $PACKAGE_NAME"

# Perform a bandit security scan on the given integration/app and suppress any Low level warnings. 
bandit -r $PACKAGE_NAME -ll
# Get the exit code of the bandit scan 
last_status=$?;

if [ $last_status -ne 0 ]; then
    print_msg "Security Scan failure for $PACKAGE_NAME which gave an exit code of $last_status"
    status=$last_status;
fi

print_msg "Bandit security scan of $PACKAGE_NAME complete.  Final Status $status"
exit $status
