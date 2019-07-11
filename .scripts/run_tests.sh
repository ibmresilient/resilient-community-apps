#!/bin/bash
echo "`realpath .scripts/integration_list.txt`"

echo "`pwd .scripts/integration_list.txt`"
# Map the listed integrations into a list 
mapfile -t INTEGRATIONS < .scripts/integration_list.txt

for INTEGRATION in ${INTEGRATIONS[@]};
do  
    echo ">>> Searching for ${INTEGRATION} tox.ini";
    # For each listed integration until EOM gather the setup.py paths
    toxfiles=(`find ./$INTEGRATION -type f -name 'tox.ini'`);
done


status=0;
for toxfile in ${toxfiles[@]};
do
    # Run the tests if current TOXENV is applicable for this tox.ini file
    valid_envs=`env -u TOXENV tox -c $toxfile --listenvs;`
    #echo "Supported Environments: $valid_envs" 
    if [[ "$valid_envs" =~ "$TOXENV" ]]
    then
        tox -c $toxfile -- --resilient_email 'integrations@example.org' --resilient_password 'supersecret' --resilient_host 'example.com' --resilient_org 'TestOrg' -m "not livetest" tests;
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
