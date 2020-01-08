#!/bin/sh
#
# An example script to do linting on the repo.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
echo "\nStarting a  script to run pylint on python files."
readonly MIN_PASSING_SCORE=7.25
readonly ERROR_MSG="Aborting commit. Your commit has a pylint score lower than ${MIN_PASSING_SCORE}"

# Declare an array that will hold the fn_ or rc_ packages
packages_that_have_been_changed=()

# For every file in the diff
for file in $(git diff --name-only HEAD~0 HEAD~1); do
    # If the file contains either fn_ or rc_ in the path
    if [[ $file =~ (fn_|rc-)+ ]]; then
        # Strip everything except the first directory in the path (integration name) and append to an array
        packages_that_have_been_changed+=($(echo "$file" | awk -F "/" '{print $1}'))
    fi
done

# Make a new array which acts as a Set to gather only unique package names
INTEGRATIONS=($(for v in "${packages_that_have_been_changed[@]}"; do echo "$v"; done | sort | uniq | xargs))
INTEGRATIONS=('fn_sep')
if [ -z "$INTEGRATIONS" ]; then
    echo "Did not find any integrations that were modified"
    exit 0
else
    echo "Most recently modified integrations from last commit show as : ${INTEGRATIONS}"
fi

for integration in ${INTEGRATIONS[@]}; do
    # Lint all the python files
    pylint ${integration}/**/**/*.py \; |
        # Only get the number values
        grep -oE "\-?[0-9]+\.[0-9]+" |
        # Extract the score
        awk 'NR==1 || NR % 4 == 0' |
        # # Round the score down
        # sed 's/...$//' |
        # For score lines
        while read line; do
            # If the line contains a score lower than MIN_PASSING_SCORE throw a problem.
            if (($(echo "$line < ${MIN_PASSING_SCORE}" | bc -l))); then
                # else print the error message
                echo "$ERROR_MSG" >&2
                exit 1
            else
                echo "Success: Pylint score $line greater than min required score: ${MIN_PASSING_SCORE}"
            fi
        done
done
printf 'Pylint Run Complete.  Final Status [%d]\n' $status
exit $status
