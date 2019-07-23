#!/bin/bash

# Declare an array that will hold the fn_ or rc_ packages 
packages_that_have_been_changed=()

# For every file in the diff 
for file in $(git diff --name-only HEAD~0 HEAD~1); 
do 
    # If the file contains either fn_ or rc_ in the path 
    if [[ $file =~ (fn_|rc_)+ ]]; 
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
else
      echo "Most recently modified integrations from last commit show as : ${INTEGRATIONS}"
fi
      
for integration in ${INTEGRATIONS[@]};
do 
    echo "Running tox tests for this package: $integration" 
    toxfile=${integration}"/tox.ini"
    # Run the tests if current TOXENV is applicable for this tox.ini file
    valid_envs=`env -u TOXENV tox -c $toxfile --listenvs;`
    echo "Environments supported by toxfile: $toxfile $valid_envs" 
    if [[ "$valid_envs" =~ "$TOXENV" ]]
    then
        # Run tox with dummy details which will serve as the user when running tests 
        tox -c $toxfile -- --resilient_email 'integrations@example.org' --resilient_password 'supersecret' --resilient_host 'example.com' -m "not livetest" tests;
        last_status=$?;
        if [ $last_status -ne 0 ]; then
            printf 'FAILURE %s: [%d]\n' $toxfile $last_status;
            status=$last_status;
        fi
    else
        printf 'Skipping %s because TOXENV %s incompatible\n' "$toxfile" "$TOXENV"
    fi
done
printf 'Test Run Complete.  Final Status [%d]\n' $status;
exit $status

