#!/bin/bash -e

# param $1: (required) version of resilient_circuits library to use in format x.x.x
# param $2: (optional) repo name to push to. Accepted values are: ARTIFACTORY, QUAY or BOTH. Defaults to BOTH if blank

# Dependencies on:
# sudo apt-get install jq
# pip install resilient-sdk

# Map ARTIFACTORY_URL until we change in Travis
ARTIFACTORY_URL=$ARTIFACTORY_URL_2

###############
## Variables ##
###############
RESILIENT_CIRCUITS_VERSION=$1
REPO_TO_PUSH=$2
QUAY_API_URL="$QUAY_URL/api/v1"
ARTIFACTORY_REPO_URL="$ARTIFACTORY_REPO_NAME.$ARTIFACTORY_URL"
PATH_IGNORE_IMAGE_NAMES="$TRAVIS_BUILD_DIR/.scripts/IGNORE_IMAGE_NAMES.txt"
quay_io_tags=()
artifactory_tags=()
skipped_packages=()

##################
## Check params ##
##################
if [ -z "$1" ] ; then
    echo "Must provide resilient_circuits version as first parameter"
    exit 1
fi

if [ -z "$2" ] ; then
    REPO_TO_PUSH="BOTH"
fi

###############
## Functions ##
###############
print_msg () {
    printf "\n--------------------\n$1\n--------------------\n"
}

# Logs in to repository at given URL with username and passowrd
# Args: URL, username, password
repo_login () {
    echo "$3" | docker login --password-stdin --username "$2" https://${1}/
}

###########
## Start ##
###########
print_msg "\
RESILIENT_CIRCUITS_VERSION:\t$RESILIENT_CIRCUITS_VERSION \n\
REPO_TO_PUSH:\t\t\t$REPO_TO_PUSH \n\
QUAY_URL:\t\t\t$QUAY_URL \n\
QUAY_API_URL:\t\t\t$QUAY_API_URL \n\
QUAY_USERNAME:\t\t\t$QUAY_USERNAME \n\
ARTIFACTORY_URL:\t\t$ARTIFACTORY_URL \n\
ARTIFACTORY_REPO_NAME:\t\t$ARTIFACTORY_REPO_NAME \n\
ARTIFACTORY_REPO_URL:\t\t$ARTIFACTORY_REPO_URL \n\
ARTIFACTORY_USERNAME:\t\t$ARTIFACTORY_USERNAME \n\
PATH_IGNORE_IMAGE_NAMES:\t$PATH_IGNORE_IMAGE_NAMES \
"

# Make array of image names public on quay.io to rebuild
IMAGE_NAMES=( $(curl "https://$QUAY_API_URL/repository?namespace=$QUAY_USERNAME&public=true" | jq -r ".repositories[].name") )
print_msg "IMAGE_NAMES:\n${IMAGE_NAMES[*]}"

IGNORE_IMAGE_NAMES=( $(<$PATH_IGNORE_IMAGE_NAMES) )
print_msg "IGNORE_IMAGE_NAMES:\n${IGNORE_IMAGE_NAMES[*]}"

# Login to quay.io
if [ "$REPO_TO_PUSH" == "BOTH" ] || [ "$REPO_TO_PUSH" == "QUAY" ] ; then
    print_msg "Logging into $QUAY_URL as $QUAY_USERNAME"
    repo_login $QUAY_URL $QUAY_USERNAME $QUAY_PASSWORD
fi

# Login to artifactory
if [ "$REPO_TO_PUSH" == "BOTH" ] || [ "$REPO_TO_PUSH" == "ARTIFACTORY" ] ; then
    print_msg "Logging into artifactory as $ARTIFACTORY_USERNAME"
    repo_login $ARTIFACTORY_REPO_URL $ARTIFACTORY_USERNAME $ARTIFACTORY_PASSWORD
fi

# Loop all image names at https://quay.io/user/$QUAY_USERNAME
for image_name in "${IMAGE_NAMES[@]}"; do

    # If not in our blocked list
    if [[ ! " ${IGNORE_IMAGE_NAMES[@]} " =~ " ${image_name} " ]]; then
        docker_build_pass=0
        resilient_sdk_package_pass=0

        print_msg "Building: $image_name"

        int_path="$TRAVIS_BUILD_DIR/$image_name"
        print_msg "int_path: $int_path"

        # run resilient-sdk package
        print_msg "Packaging $image_name with resilient-sdk"
        resilient-sdk package -p $int_path || resilient_sdk_package_pass=$?

        # If passes resilient-sdk package build it with docker
        if [ $resilient_sdk_package_pass = 0 ] ; then

            # Get version to create latest tag
            int_version=$(python "$int_path/setup.py" --version)
            print_msg "int_version: $int_version"

            docker_tag="$image_name:$int_version"

            # run docker build
            print_msg "Building $image_name with docker"
            docker build \
            --quiet \
            --build-arg RESILIENT_CIRCUITS_VERSION=$RESILIENT_CIRCUITS_VERSION \
            -t $docker_tag \
            $int_path || docker_build_pass=$?

            # if passes docker build tag it
            if [ $docker_build_pass = 0 ] ; then
                # tag the image for quay.io
                quay_io_tag="$QUAY_URL/$QUAY_USERNAME/$image_name:$int_version"
                print_msg "Tagging $image_name for $QUAY_URL/$QUAY_USERNAME with: $quay_io_tag"
                docker tag $docker_tag $quay_io_tag
                quay_io_tags+=($quay_io_tag)

                # tag the image for artifactory
                artifactory_tag="$ARTIFACTORY_REPO_URL/$QUAY_USERNAME/$image_name:$int_version"
                print_msg "Tagging $image_name for artifactory with: $artifactory_tag"
                docker tag $docker_tag $artifactory_tag
                artifactory_tags+=($artifactory_tag)

                print_msg "Done building: $image_name"
            fi
        fi

        if [ $resilient_sdk_package_pass != 0 ] || [ $docker_build_pass != 0 ] ; then
            print_msg "Packaging or building failed. Adding $image_name to list of skipped_packages"
            skipped_packages+=($image_name)
        fi
    
    else
        print_msg "$image_name is in $PATH_IGNORE_IMAGE_NAMES\nAdding it to list of skipped_packages"
        skipped_packages+=($image_name)
    fi

done

print_msg "List of all docker images:\n$(docker images)"

# Push images to quay.io
if [ "$REPO_TO_PUSH" == "BOTH" ] || [ "$REPO_TO_PUSH" == "QUAY" ] ; then
    for t in "${quay_io_tags[@]}"; do
        print_msg "Pushing $t to quay.io"
        docker push $t
    done
fi

# Push images to artifactory
if [ "$REPO_TO_PUSH" == "BOTH" ] || [ "$REPO_TO_PUSH" == "ARTIFACTORY" ] ; then
    for t in "${artifactory_tags[@]}"; do
        print_msg "Pushing $t to artifactory"
        docker push $t
    done
fi

print_msg "Skipped Packages:\n${skipped_packages[*]}"