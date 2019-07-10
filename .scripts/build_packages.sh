#!/bin/bash

# Build python packages with setup.py
# This section builds all the feature packages implemented in
# python. It searches for all folders that contains setup.py
#
setup_files=(`find ./* -maxdepth 1 -type f -name 'setup.py'`);
dist_dir=$( cd $(dirname $0) ; pwd -P )

echo "Building these packages:";
printf '  %s\n' "${setup_files[@]}";
echo "Storing packages to: $dist_dir";
for setup in ${setup_files[@]};
do
    # Run the Build
    pkg_dir=$(dirname "${setup}")
    echo "Running build from $pkg_dir";
    (cd $pkg_dir && python setup.py -q sdist --formats=zip --dist-dir $dist_dir);
done;

# Build content packages with resilient-res-package.sh
# This section builds all the content/resource only package. No setup.py
# It searches for a script called resilient-res-package.sh, and calls it.
# Most likely you only need to zip some files folders. Follow the example
# in the ../res_qraw_mitre folder.

build_scripts=(`find ./ -type f -name 'resilient-res-package.sh'`);

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
