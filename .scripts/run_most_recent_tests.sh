#!/bin/bash

# Run tests for the most recently modified package
most_recent_package=$(ls -I="*."{zip,gz} -td ./* | head -1)
echo "Most Recent package shows as : ${most_recent_package}";
toxfile="${most_recent_package}/tox.ini"

# Run the tests if current TOXENV is applicable for this tox.ini file
valid_envs=`env -u TOXENV tox -c $toxfile --listenvs;`

echo "Environments supported by toxfile: $toxfile $valid_envs" 
if [[ "$valid_envs" =~ "$TOXENV" ]]
then
    # Run tox with dummy details which will serve as the user when running tests 
    tox -c $toxfile -- --resilient_email 'integrations@example.org' --resilient_password 'supersecret' --resilient_host 'example.com' --resilient_org 'TestOrg' -m "not livetest" tests;
    last_status=$?;
    if [ $last_status -ne 0 ]; then
        printf 'FAILURE %s: [%d]\n' $toxfile $last_status;
        status=$last_status;
    fi
else
    printf 'Skipping %s because TOXENV %s incompatible\n' "$toxfile" "$TOXENV"
fi
printf 'Test Run Complete.  Final Status [%d]\n' $status;
exit $status

