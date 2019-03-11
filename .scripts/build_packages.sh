#!/bin/bash

# Build python packages with setup.py

setup_files=(`find .. -type f -name 'setup.py'`);
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

# Build content packages with resilient-res-package.sh

build_scripts=(`find .. -type f -name 'resilient-res-package.sh'`);

echo "Building these packages:";
printf '  %s\n' "${build_scripts[@]}";
echo "Storing packages to: $dist_dir";
for res_folder in ${build_scripts[@]};
do
    # Run the Build
    pkg_dir=$(dirname "${res_folder}")
    pushd $pkg_dir
    ./resilient-res-package.sh $dist_dir;
    popd
done;
