#!/bin/bash

# Run tests for any package with a tox.ini file

# Some package must be run first b/c others depend on them, list them here
must_run_first=( rc-query-runner rc-webserver);
match=$( IFS='|'; echo "${must_run_first[*]}" );


# Some package must be run second b/c others depend on them and they depend on ones run first, list them here
must_run_second=( rc-cts);
match_second=$( IFS='|'; echo "${must_run_second[*]}" );


echo "$match";
toxfiles=(`find . -type f -name 'tox.ini'`);
first_runs=();
second_runs=();
third_runs=();
for i in ${!toxfiles[@]};
do
    #echo "look for " ${toxfiles[$i]} " in " $match;
    if [[ ${toxfiles[$i]} =~ $match ]]
    then
      first_runs+=(${toxfiles[$i]});
    elif [[ ${toxfiles[$i]} =~ match_second ]]
    then
      second_runs+=(${toxfiles[$i]});
    else
      third_runs+=(${toxfiles[$i]});
    fi
done;
echo "Running these first:";
printf '  %s\n' "${first_runs[@]}";
echo "Running these second:";
printf '  %s\n' "${second_runs[@]}";
echo "Running these third:";
printf '  %s\n' "${third_runs[@]}";
toxfiles=("${first_runs[@]}" "${second_runs[@]}" "${third_runs[@]}");

status=0;
for toxfile in ${toxfiles[@]};
do
    # Run the tests if current TOXENV is applicable for this tox.ini file
    valid_envs=`env -u TOXENV tox -c $toxfile --listenvs;`
    #echo "Supported Environments: $valid_envs" 
    if [[ "$valid_envs" =~ "$TOXENV" ]]
    then
        tox -c $toxfile -- tests;
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
