#!/bin/bash

# Run tests for any package with a tox.ini file

# Some package must be run first b/c others depend on them, list them here
must_run_first=( rc-query-runner rc-webserver);
match=$( IFS='|'; echo "${must_run_first[*]}" );


echo "$match";
toxfiles=(`find . -type f -name 'tox.ini'`);
first_runs=();
second_runs=();
for i in ${!toxfiles[@]};
do
    #echo "look for " ${toxfiles[$i]} " in " $match;
    if [[ ${toxfiles[$i]} =~ $match ]]
    then
      first_runs+=(${toxfiles[$i]});
    else
      second_runs+=(${toxfiles[$i]});
    fi
done;
echo "Running these first:";
printf '  %s\n' "${first_runs[@]}";
echo "Running these second:";
printf '  %s\n' "${second_runs[@]}";
toxfiles=("${first_runs[@]}" "${second_runs[@]}");

for toxfile in ${toxfiles[@]};
do
    # Run the tests
    tox -c $toxfile -- tests;
done;
