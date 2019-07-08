#!/bin/bash

# Run tests for the most recently modified package
most_recent_package=$(ls -td ./*/ | head -1)
toxfiles=(`find $most_recent_package -type f -name 'tox.ini'`);

status=0;
for toxfile in ${toxfiles[@]};
do
    # Run the tests if current TOXENV is applicable for this tox.ini file
    valid_envs=`env -u TOXENV tox -c $toxfile --listenvs;`
    #echo "Supported Environments: $valid_envs" 
    if [[ "$valid_envs" =~ "$TOXENV" ]]
    then
        # Run tox with dummy details which will serve as the user when running tests 
        tox -c $toxfile -- --resilient_email 'integrations@example.org' --resilient_password 'supersecret' --resilient_host '192.168.57.101' --resilient_org 'TestOrg' tests;
        last_status=$?;
        if [ $last_status -ne 0 ]; then
            printf 'FAILURE %s: [%d]\n' $toxfile $last_status;
            status=$last_status;
        fi
    else
        printf 'Skipping %s because TOXENV %s incompatible\n' "$toxfile" "$TOXENV"
    fi
done;

printf 'Test Run Complete.  Final Status [%d]\n' $status;
exit $status

