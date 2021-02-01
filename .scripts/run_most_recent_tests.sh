#!/bin/bash

# Source the script which finds recent changes 
. .scripts/find_recently_changed_packages.sh
# Call the function which will search for packages, the result will be available via the $PACKAGES variable defined in that script
find_recently_changed_packages
      
for integration in ${INTEGRATIONS[@]};
do 
    echo "Checking if additional OS dependencies are required for $integration"
    if [ -f ${integration}"/.travis_package_setup.sh" ]
      then
        echo "OS package install script found. About to run"
        sh ${integration}"/.travis_package_setup.sh"
      else
        echo "Nothing additional to install"
    fi
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
            echo "FAILURE $toxfile: [$last_status]"
            status=$last_status;
        fi
    else
        echo "Skipping $toxfile because TOXENV $TOXENV incompatible"
    fi
done
echo "Test Run Complete.  Final Status [$status]"
exit $status

