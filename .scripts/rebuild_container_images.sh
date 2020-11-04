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
QUAY_URL="quay.io"
QUAY_API_URL="$QUAY_URL/api/v1"
PATH_IGNORE_IMAGE_NAMES="$TRAVIS_BUILD_DIR/.scripts/IGNORE_IMAGE_NAMES.txt"

###############
## Functions ##
###############
print_msg () {
    printf "\n--------------------\n$1\n--------------------\n"
}

# Logs in to repository at given URL with username and passowrd
# Args: URL, username, password
function repo_login (){
    echo "$3" | docker login --password-stdin --username "$2" https://${1}/
}

###########
## Start ##
###########
print_msg "\
RESILIENT_CIRCUITS_VERSION:\t$RESILIENT_CIRCUITS_VERSION \n\
QUAY_URL:\t\t\t$QUAY_URL \n\
QUAY_API_URL:\t\t\t$QUAY_API_URL \n\
QUAY_USERNAME:\t\t\t$QUAY_USERNAME \n\
PATH_IGNORE_IMAGE_NAMES:\t$PATH_IGNORE_IMAGE_NAMES \
"

# Make array of image names public on quay.io to rebuild
IMAGE_NAMES=( $(curl "https://$QUAY_API_URL/repository?namespace=$QUAY_USERNAME&public=true" | jq -r ".repositories[].name") )
print_msg "IMAGE_NAMES:\n${IMAGE_NAMES[*]}"

IGNORE_IMAGE_NAMES=( $(<$PATH_IGNORE_IMAGE_NAMES) )
print_msg "IGNORE_IMAGE_NAMES:\n${IGNORE_IMAGE_NAMES[*]}"

quay_io_tags=()

# Loop all image names at https://quay.io/user/$QUAY_USERNAME
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
        print_msg "Packaging $image_name with resilient-sdk"
        resilient-sdk package -p $int_path

        docker_tag="$image_name:$int_version"

        # run docker build
        print_msg "Building $image_name with docker"
        docker build \
        --quiet \
        --build-arg RESILIENT_CIRCUITS_VERSION=$RESILIENT_CIRCUITS_VERSION \
        -t $docker_tag \
        $int_path

        # tag the image for quay.io
        quay_io_tag="$QUAY_URL/$QUAY_USERNAME/$image_name:$int_version"
        print_msg "Tagging $image_name for quay.io with: $quay_io_tag"
        docker tag $docker_tag $quay_io_tag
        quay_io_tags+=($quay_io_tag)

        # TODO: tag the image for artifactory

        print_msg "Done building: $image_name"

    fi

done

print_msg "List of all docker images:\n$(docker images)"

# Login and push to quay.io
print_msg "Logging into $QUAY_URL as $QUAY_USERNAME"
repo_login $QUAY_URL $QUAY_USERNAME $QUAY_PASSWORD

# for t in "${quay_io_tags[@]}"; do
#     print_msg "Pushing $t"
#     docker push $t
# done

# TODO: Login and push to artifactory