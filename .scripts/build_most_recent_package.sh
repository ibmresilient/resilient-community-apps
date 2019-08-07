#!/bin/bash

# Build python packages with setup.py
# This section builds all the feature packages implemented in
# python. It searches for all folders that contains setup.py
#

# Declare an array that will hold the fn_ or rc_ packages 
packages_that_have_been_changed=()

# For every file in the diff 
for file in $(git diff --name-only HEAD~0 HEAD~1); 
do 
    # If the file contains either fn_ or rc_ in the path 
    if [[ $file =~ (fn_|rc-)+ ]]; 
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
      exit 0
else
      echo "Most recently modified integrations from last commit show as : ${INTEGRATIONS}"
fi
      
for integration in ${INTEGRATIONS[@]};
do 
    echo "For package: $integration"
    dist_dir=$( cd $(dirname $integration) ; pwd -P )
    echo "Storing package to: $dist_dir";
    # Build the python package storing the output as a zip
    (cd $integration && python setup.py -q sdist --dist-dir $dist_dir);
done
printf 'Building complete.  Final Status [%d]\n' $status;
exit $status


