#!/bin/bash

# Build python packages with setup.py
# This section builds all the feature packages implemented in
# python. It searches for all folders that contains setup.py
#
#echo "Running this command : ls -td `find ./* -maxdepth 1 -type f -name 'setup.py'` | head -1";
most_recent_package=$(ls -td ./* | head -1)

echo "$(ls -tld `find ./* -maxdepth 1 -type f -name 'setup.py'`)"

echo "Most Recent package shows as : $most_recent_package";

setup_file="${most_recent_package}"
echo "${setup_file}"
dist_dir=$( cd $(dirname $most_recent_package) ; pwd -P )

echo "Building this package:";
printf '  %s\n' "$setup_file";
echo "Storing packages to: $dist_dir";

# Run the Build
pkg_dir=$(dirname "$setup_file")
echo "Running build from $pkg_dir";
(cd $pkg_dir && python setup.py -q sdist --formats=zip --dist-dir $dist_dir);
