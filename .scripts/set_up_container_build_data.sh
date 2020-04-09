#!/bin/bash -v
# This script either
# - pulls out the name of the integration out of the tag pushed
# - or gets a list of all changed integrations based on the TRAVIS_COMMIT_RANGE
# It then pulls out current version of each integration from its setup.py
# builds its Dockerfile and pushes it up to the artifactory.

# Logs in to repository at given URL with username and passowrd
# Args: URL, username, password
function repo_login (){
	echo "$3" | docker login --password-stdin --username "$2" https://${1}/
}

# Build a container
# Args: Name and the tags to attach
function container_build (){
	argc=$#
	argv=("$@")

	docker build -t resilient/${1} ./${1}
	if [ $? -ne 0 ]; then
		return 1
	fi

	# for tags we will iterate only starting with 2nd argument
	# and tag built image with the following tag
	# in Travis it works a little different for some reason than locally
	for (( j=1; j<argc; j++ )); do
		docker tag resilient/${1} "${argv[j]}"
	done
}

# Pushes container with a given label
# Args: label to push
function container_push (){
	docker push $1
}

packages_that_have_been_changed=()
skipped_packages=()

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


if [ -z "$INTEGRATIONS" ]; then
      echo "Did not find any integrations that were modified"
      # We're using return and not exit, because we are sourcing this script and don't want to kill the job
      return 0
else
      echo "Most recently modified integrations from last commit show as : ${INTEGRATIONS}"
fi

echo "Logging in to Artifactory"
repo_login $ARTIFACTORY_URL $ARTIFACTORY_USERNAME $ARTIFACTORY_PASSWORD
if [ $? -ne 0 ]; then
	echo "Failed log in to artifactory"
	set -e
	return 1
fi   	

echo "Logging in to Quay"
repo_login $QUAY_URL $QUAY_USERNAME $QUAY_PASSWORD
if [ $? -ne 0 ]; then
	echo "Failed log in to Quay"
	set -e
	return 1
fi   	

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

    echo "Building $integration"

    dist_dir="$(dirname $BASH_SOURCE)/../$integration/dist"
    mkdir dist_dir
    (cd $(dirname $setup_file) && python setup.py -q sdist --dist-dir ./dist);

    echo "Building container for $integration"

	# To get version of the integration we first extract line verion=<version> from setup.py, from where we extract
	# the actual version substring. Doing it in 2 steps to avoid using Perl style regex with lookahead capabilities
	integration_version=$(cat "$setup_file" | grep -o "version=['\"][0-9.]*['\"]" | grep -oE "[0-9.]+")
	if [ -z "$integration_version" ]; then
		echo "Couldn't detect version for package $integration. Make sure it's listed as version=<version>."
		skipped_packages+=($integration)
		continue
	fi
	echo "$(echo $integration)'s version is: $integration_version"

	ARTIFACTORY_LABEL=${ARTIFACTORY_URL}/resilient/${integration}:${integration_version}
	QUAY_LABEL=${QUAY_URL}/${QUAY_ORG}/${integration}:${integration_version}

	container_build "$integration" "$ARTIFACTORY_LABEL" "$QUAY_LABEL"

	if [ $? -ne 0 ]; then
		skipped_packages+=($integration)
		continue
	fi

	container_push $ARTIFACTORY_LABEL
	if [ $? -ne 0 ]; then
		skipped_packages+=($integration)
		continue
	fi

	container_push $QUAY_LABEL
	if [ $? -ne 0 ]; then
		echo "Pushed the version tag, but did not label as the latest."
		skipped_packages+=($integration)
		continue
	fi
done

if [[ -n "${skipped_packages[*]}" ]]; then
	echo "Wasn't able to build and push the following integrations: $skipped_packages"
	echo "Fix the errors and create tags to deploy each individually."
	export FAILED_CONTAINERS=$skipped_packages
fi
