#!/bin/bash

# Build python packages with setup.py
# This section builds all the feature packages implemented in
# python. It searches for all folders that contains setup.py
#
most_recent_package=$(ls -td ./*/ | head -1)
echo "Most Recent package shows as : $most_recent_package";

setup_files=(`find $most_recent_package -type f -name 'setup.py'`); # TODO: Remove to use most_recent_package 
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

# Zip all .tar.gz builds
cd "$dist_dir"
builds=(`find . -type f -name '*.tar.gz'`);
echo "zip all these builds:";
printf '  %s\n' "${builds[@]}";
for build in ${builds[@]};
do
    zip_name=$(echo "${build}.zip"| sed s/.tar.gz//)
    (zip -r "${zip_name}" $build)
done;