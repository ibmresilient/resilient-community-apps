#!/bin/bash -v
dist_dir=$( cd $(dirname $0) ; pwd -P )

# build using either global PyPi or Artifactory
PYPI_INDEX="https://pypi.com"
if [[ $MASTER_BUILD -ne 0 && -n $DEV_DEPS && $DEV_DEPS -eq 0 ]]; then
	PYPI_INDEX="$ARTIFACTORY_PYPI_INDEX"
fi

packages_that_have_been_changed=()
skipped_packages=()
shipped_packages=()

if [ -z $TRAVIS_TAG ]; then
	echo "Build is triggered with a commit to master - collecting changed packages."
	# For every file in the PR/commit diff
	# Replacing ... w/ ..: https://github.com/travis-ci/travis-ci/issues/4596
	for file in $(git diff --name-only ${TRAVIS_COMMIT_RANGE/.../..}); 
	do 
	    # If the file contains either fn_ or rc_ in the path 
	    if [[ $file =~ (fn_|rc-)+ ]]; then 
	    	# Strip everything except the first directory in the path (integration name) and append to an array
	    	packages_that_have_been_changed+=($(echo "$file" | awk -F "/" '{print $1}')); 
	    fi
	done
else
	echo "Build is triggered with a tag push. Collecting the integration"
	# required tag format is container/<name>/# - name gets taken out
	packages_that_have_been_changed+=($(echo $TRAVIS_TAG | cut -d "/" -f 2)); 
fi

INTEGRATIONS=($(for v in "${packages_that_have_been_changed[@]}"; do echo "$v";done| sort| uniq| xargs));


for integration in ${INTEGRATIONS[@]};
do
	echo "Building and deploying: $integration" 
    # get the setup.py file for current integration

    setup_file="$(dirname $BASH_SOURCE)/../$integration/setup.py"
    if [ ! -e "$setup_file" ]; then
        echo "Chosen integration $integration doesn't have setup.py"
        skipped_packages+=($integration)
        continue
    fi

    dist_dir="$(dirname $BASH_SOURCE)/../$integration/dist"
    mkdir dist_dir
    #actually build
    (cd $(dirname $setup_file) && python setup.py -q sdist --dist-dir ./dist && resilient-sdk package -p .);

	# To get version of the integration we first extract line verion=<version> from setup.py, from where we extract
	# the actual version substring. Doing it in 2 steps to avoid using Perl style regex with lookahead capabilities
	integration_version=$(cat "$setup_file" | grep -o "version=['\"][0-9.]*['\"]" | grep -oE "[0-9.]+")
	if [ -z "$integration_version" ]; then
		echo "Couldn't detect version for package $integration. Make sure it's listed as version=<version>."
		skipped_packages+=($integration)
		continue
	fi
	echo "$(echo $integration)'s version is: $integration_version"

	# To get name of the integrations we will extract line name='<name>' from setup.py
	integration_name=$(grep -o "name[[:space:]]*=[[:space:]]*['\"][a-z0-9\-\_]*['\"]" $setup_file| cut -d '=' -f 2 | tr -d "\"'[:space:]")
	if [ -z "$integration_name" ]; then
		echo "Couldn't extract package name from $integration. Make sure it's listed in setup.py."
		skipped_packages+=($integration)
		continue
	fi

	if [ -f ${dist_dir}/app-${integration_name}-${integration_version}.zip ]; then
        # curl -H [header including the Artifactory API Key] -T [path to the file to upload to Artifactory] "https://na.artifactory.swg-devops.com/artifactory/<repo-name>/<path-in-repo>"
		curl -H "X-JFrog-Art-Api:${ARTIFACTORY_API_KEY}" -T ${dist_dir}/app-${integration_name}-${integration_version}.zip "$ARTIFACTORY_REPO_LINK/$integration_name/$integration_version/app-${integration_name}-${integration_version}-${TRAVIS_BUILD_NUMBER}.zip"
		shipped_packages+=("$ARTIFACTORY_REPO_LINK/$integration_name/$integration_version/app-${integration_name}-${integration_version}-${TRAVIS_BUILD_NUMBER}.zip")
    else
        curl -H "X-JFrog-Art-Api:${ARTIFACTORY_API_KEY}" -T ${integration_name}-${integration_version}.zip "$ARTIFACTORY_REPO_LINK/$integration_name/$integration_version/${integration_name}-${integration_version}-${TRAVIS_BUILD_NUMBER}.zip"
        shipped_packages+=("$ARTIFACTORY_REPO_LINK/$integration_name/$integration_version/${integration_name}-${integration_version}-${TRAVIS_BUILD_NUMBER}.zip")
    fi
done

export PUBLISHED_PACKAGES=$shipped_packages

if [[ -n "${skipped_packages[*]}" ]]; then
	echo "Wasn't able to build and push the following integrations: $skipped_packages"
	echo "Fix the errors and create tags to deploy each individually."
	export FAILED_PACKAGES=$skipped_packages
fi