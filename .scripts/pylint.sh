#!/bin/bash -x
#
# An example script to do linting on the repo.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#

# param $1: (required) which package_name to run the scan for

###############
## Variables ##
###############
PACKAGE_NAME=$1
readonly MIN_PASSING_SCORE=6.25
readonly ERROR_MSG="Aborting commit. Your commit has a pylint score lower than ${MIN_PASSING_SCORE}"
RCFILE=".scripts/.pylintrc"

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
    print_msg "Latest commit is modifying the build. Not running pylint"
    exit 0
fi

print_msg "Starting a script to run pylint on python files for $PACKAGE_NAME"


# Lint all the python files;
# **/**/*.py catches every dir such as cmds, util, tests
pylint --rcfile=${RCFILE} ./${PACKAGE_NAME}/**/**/*.py \; |
    # Only get the number values
    grep -oE "\-?[0-9]+\.[0-9]+" |
    # Extract the score
    awk 'NR==1 || NR % 4 == 0' |
    # For score lines
    while read line; do
        print_msg "Pylint score for $PACKAGE_NAME is $line"
        # If the line contains a score lower than MIN_PASSING_SCORE throw a problem.
        if (($(echo "$line < ${MIN_PASSING_SCORE}" | bc -l))); then
            # and print the error message
            echo ">$ERROR_MSG" >&2
            # and save the last_status as failure
            last_status=1
        else
            print_msg "Pylint score $line greater than min required score: ${MIN_PASSING_SCORE}; Success!"
            last_status=0
        fi
        # Update the status if any pylint scan for a package fails
        if [ $last_status -ne 0 ]; then
            echo "FAILURE $toxfile: [$last_status]"
            status=$last_status;
        fi
    done

echo "Pylint Run Complete.  Final Status $status"
exit $status