#!/bin/bash -e

# param $1: (required) version of resilient_circuits library to use in format x.x.x

# Dependencies on:
# sudo apt-get install jq
# pip install resilient-sdk

##################
## Check params ##
##################
if [ -z "$1" ] ; then
    echo "Must provide resilient_circuits version as first parameter"
    exit 1
fi

###############
## Variables ##
###############
RESILIENT_CIRCUITS_VERSION=$1
QUAY_IO_API_URL="quay.io/api/v1"
QUAY_IO_USER_NAME="ibmresilient"
# QUAY_IO_USER_NAME="sjcurtinibm"
PATH_IGNORE_IMAGE_NAMES="$TRAVIS_BUILD_DIR/.scripts/IGNORE_IMAGE_NAMES.txt"

###############
## Functions ##
###############
print_msg () {
    printf "\n--------------------\n$1\n--------------------\n"
}

print_msg "\
RESILIENT_CIRCUITS_VERSION:\t$RESILIENT_CIRCUITS_VERSION \n\
QUAY_IO_API_URL:\t\t$QUAY_IO_API_URL \n\
QUAY_IO_USER_NAME:\t\t$QUAY_IO_USER_NAME \n\
PATH_IGNORE_IMAGE_NAMES:\t$PATH_IGNORE_IMAGE_NAMES \
"

# Make array of image names public on quay.io to rebuild
# IMAGE_NAMES=( $(curl 'https://quay.io/api/v1/repository?namespace=ibmresilient&public=true' | jq -r '.repositories[].name') )
IMAGE_NAMES=( $(curl "https://$QUAY_IO_API_URL/repository?namespace=$QUAY_IO_USER_NAME&public=true" | jq -r ".repositories[].name") )
IGNORE_IMAGE_NAMES=( $(<$PATH_IGNORE_IMAGE_NAMES) )

###############
## Main Loop ##
###############
# Loop all image names at https://quay.io/user/$QUAY_IO_USER_NAME
for image_name in "${IMAGE_NAMES[@]}"; do

    # If not in our blocked list
    if [[ ! " ${IGNORE_IMAGE_NAMES[@]} " =~ " ${image_name} " ]]; then
        print_msg "Building: $image_name"

        int_path="$TRAVIS_BUILD_DIR/$image_name"
        print_msg "int_path: $int_path"

        # Get version to create latest tag
        int_version=$(python "$int_path/setup.py" --version)
        print_msg "int_version: $int_version"

        # run resilient-sdk package
        resilient-sdk package -p $int_path

        # run docker build
        docker build \
        --build-arg RESILIENT_CIRCUITS_VERSION=$RESILIENT_CIRCUITS_VERSION \
        -t "$QUAY_IO_USER_NAME/$image_name:$int_version" \
        $int_path

        # TODO: Login and push to docker and artifactory
    fi

done
