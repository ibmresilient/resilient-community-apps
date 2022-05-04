#!/bin/bash -e

# param $1: (required) repo name to pull FROM. Acccepted values are QUAY or ICR.
# param $2: (required) repo name to push TO. Acccepted values are QUAY or ICR.

# Dependencies on:
# sudo apt-get install jq
# curl -fsSL https://clis.cloud.ibm.com/install/linux | sh 
# ibmcloud plugin install container-registry -r 'IBM Cloud'

###############
## Variables ##
###############
SOURCE=$1
DEST=$2
DEST_TAGS=()
IMAGE_NAMES=()
SOURCE_URL=""
DEST_URL=""

##################
## Check params ##
##################
if [ -z "$1" ] ; then
    printf "Must provide source registry as first parameter. Options are QUAY or ICR"
    exit 1
fi

if [ -z "$2" ] ; then
    printf "Must provide destination registry as second parameter. Options are QUAY or ICR"
    exit 1
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

# logs in to ICR repo using $IBMCLOUD_API_KEY env variable
# Args: none
icr_login () {
    ibmcloud login --no-region -a https://$IBMCLOUD_URL
    ibmcloud cr region-set global
    ibmcloud cr login
}

source_is_quay() {
    if [ "$1" == "QUAY" ] && [ "$2" == "ICR" ]; then
        return 0
    else
        return 1
    fi
}

source_is_icr() {
    if [ "$1" == "ICR" ] && [ "$2" == "QUAY" ]; then
        return 0
    else
        return 1
    fi
}

###########
## Start ##
###########
print_msg "\
Sync Stage\n\
SOURCE:\t\t\t\t$SOURCE \n\
DEST:\t\t\t\t$DEST \n\
QUAY_URL:\t\t\t$QUAY_URL \n\
QUAY_API_URL:\t\t\t$QUAY_API_URL \n\
QUAY_USERNAME:\t\t\t$QUAY_USERNAME \n\
ICR_URL:\t\t\t$ICR_URL \n\
REGISTRY_NAMESPACE:\t\t$REGISTRY_NAMESPACE \n\
"

# Login to quay.io
print_msg "Logging into $QUAY_URL as $QUAY_USERNAME"
repo_login $QUAY_URL $QUAY_USERNAME $QUAY_PASSWORD

# Login to icr.io
print_msg "Logging into $ICR_URL using API key"
icr_login

if source_is_quay $SOURCE $DEST; then
    # Make array of image names public on quay.io to rebuild
    print_msg "Getting list of IMAGE_NAMES at 'https://$QUAY_IMAGES_API_URL'"
    IMAGE_NAMES=( $(curl "https://$QUAY_IMAGES_API_URL" | jq -r ".repositories[].name") )
    SOURCE_URL="$QUAY_URL"
    DEST_URL="$ICR_URL"
elif source_is_icr $SOURCE $DEST; then
    # Make array of image names on icr.io to rebuild
    print_msg "Getting list of IMAGE_NAMES from IBM Container Registry in namespace '$REGISTRY_NAMESPACE'"
    IMAGE_NAMES=( $(ibmcloud cr images --restrict $REGISTRY_NAMESPACE -q) )
    SOURCE_URL="$ICR_URL"
    DEST_URL="$QUAY_URL"
else
    print_msg "Must provide QUAY or ICR as source and destination parameters"
    exit 1
fi

print_msg "IMAGE_NAMES:\n${IMAGE_NAMES[*]}"

# Loop all image names
for image_name in "${IMAGE_NAMES[@]}"; do

    version_tags=()
    if source_is_quay $SOURCE $DEST; then
        # grab image versions from quay api
        # these tags are put in an array to be looped over and all pulled then tagged for dest
        version_tags=( $(curl "https://$QUAY_API_URL/repository/$QUAY_USERNAME/$image_name/tag/?onlyActiveTags=true" | jq -r ".tags[].name") )
    elif source_is_icr $SOURCE $DEST; then
        # grab image version and image name from ICR by chopping up $image_name 
        # which will be in format: "icr.io/ibmresilient/<image_name>:<image_tag>"
        # note: to keep logic relatively similar between quay and icr as source, 
        #       the one tag from icr image is added to an array but will only ever have one element
        version_tags=( $(echo $image_name | cut -d ":" -f 2) )
        image_name=$(echo $image_name | cut -d "/" -f 3 | cut -d ":" -f 1)
    fi

    print_msg "::$image_name:: \nversion_tags:\t\t\t${version_tags[*]} \nSOURCE_URL:\t\t\t$SOURCE_URL \nDEST_URL:\t\t\t$DEST_URL"

    for int_version in "${version_tags[@]}"; do
        
        source_tag="$SOURCE_URL/$REGISTRY_NAMESPACE/$image_name:$int_version"

        print_msg "$image_name:: Pull image with tag $source_tag from $SOURCE_URL"
        docker pull $source_tag

        # tag the image for icr.io
        dest_tag="$DEST_URL/$REGISTRY_NAMESPACE/$image_name:$int_version"
        print_msg "$image_name:: Tagging $image_name for $DEST_URL/$REGISTRY_NAMESPACE with: $dest_tag"
        docker tag $source_tag $dest_tag
        DEST_TAGS+=($dest_tag)
    done

done

print_msg "List of images to be pushed to $DEST:\n${DEST_TAGS[*]}"1

for t in "${DEST_TAGS[@]}"; do
    print_msg "Pushing $t to $DEST"
    docker push $t
done
