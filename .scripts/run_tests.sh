#!/bin/bash

# Map the listed integrations into a list 
mapfile -t INTEGRATIONS < .scripts/integration_list.txt

# For each integration in the list
for INTEGRATION in ${INTEGRATIONS[@]};
do  
    echo ">>> Searching for ${INTEGRATION} tox.ini";
    # Find the toxfile for this intgration, only go 1 depth down
    toxfiles=(`find ./$INTEGRATION -maxdepth 1 -type f -name 'tox.ini'`);
done


status=0;
# For each toxfile
for toxfile in ${toxfiles[@]};
do
    # Run the tests if current TOXENV is applicable for this tox.ini file
    valid_envs=`env -u TOXENV tox -c $toxfile --listenvs;`
    #echo "Supported Environments: $valid_envs" 
    if [[ "$valid_envs" =~ "$TOXENV" ]]
    then
        tox -c $toxfile -- --resilient_email 'integrations@example.org' --resilient_password 'supersecret' --resilient_host 'example.com' -m "not livetest" tests;
        last_status=$?;
        if [ $last_status -ne 0 ]; then
            printf 'FAILURE %s: [%d]\n' $toxfile $last_status;
            status=$last_status;
        fi
    else
        # Skip tests if TOXENV variable is not in the tox.ini envlist.
        printf 'Skipping %s because TOXENV %s incompatible\n' "$toxfile" "$TOXENV"
    fi
done;

printf 'Test Run Complete.  Final Status [%d]\n' $status;
exit $status
