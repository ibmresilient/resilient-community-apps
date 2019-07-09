#!/bin/bash

# Build python packages with setup.py
# This section builds all the feature packages implemented in
# python. It searches for all folders that contains setup.py
#
most_recent_package=$(ls -td ../fn_* | head -1)
echo "Most Recent package shows as : ${most_recent_package}/setup.py";

dist_dir=$( cd $(dirname $0) ; pwd -P )

echo "Building this package:";
printf '  %s\n' "${most_recent_package}/setup.py";
echo "Storing packages to: $dist_dir";

# Run the Build
pkg_dir=$(dirname "${most_recent_package}/setup.py")
echo "Running build from $pkg_dir";
(cd $pkg_dir && python setup.py -q sdist --formats=zip --dist-dir $dist_dir);
