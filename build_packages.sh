#!/bin/bash

# Build all packages

setup_files=(`find ./packages -type f -name 'setup.py'`);
dist_dir=$( cd $(dirname $0) ; pwd -P )

echo "Building these packages:";
printf '  %s\n' "${setup_files[@]}";
echo "Storing packages to: $dist_dir";
for setup in ${setup_files[@]};
do
    # Run the Build
    pkg_dir=$(dirname "${setup}")
    echo "Running build from $pkg_dir";
    (cd $pkg_dir && python setup.py -q sdist --dist-dir $dist_dir);
done;
