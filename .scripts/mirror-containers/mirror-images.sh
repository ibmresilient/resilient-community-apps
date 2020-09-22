#!/bin/bash

# Title:         mirror-images.sh
# Description:   Facilitates the transfer of a number of named images from a source registry to a destination one

# Version:       1.0.0
set -x

# v1: At a high level; with this script we want to:
# 0. Determine whether to use docker or podman
# 1. Take in a named list of image we want to move WITH versions
# 2. Pull each image from the source registry only grabbing the tags specified
# 3. Tag each image with its new destination tag before push
# 4. Push each image with its new tag to the destination registry
# 5. Delete all the images we pulled except for those named in the preserved_images.conf file, note only images not in use will be deleted.

# Functions
# Function used to check the existance of a command
function cmd_exists() {
  command -v $1 > /dev/null 2>&1
}
## Variables
# The file from which we will pull configuration files
readonly IMAGES_TO_TRANSFER="${IMAGES_TO_TRANSFER:-repo_quay.conf}"

readonly IMAGES_TO_PRESERVE_LOCALLY="${IMAGES_TO_TRANSFER:-preserved_images.conf}"

readonly IMAGE_REGISTRY="${SOURCE_REGISTRY_DOMAIN:-quay.io}"
readonly REGISTRY_ORG="${SOURCE_REGISTRY_ORG:-ibmresilient}"
# The registry we will pull images from 
readonly SOURCE_REGISTRY="$IMAGE_REGISTRY/$REGISTRY_ORG"
# The registry we will push images too
destination_registry=""

# ========================================
#
# Checks for arguments and the needed unix commands
#
# ========================================
# Check if string is empty using -z. For more 'help test'    
if [[ -z "$1" ]]; then
   printf '%s\n' "No destination registry provided. Registry must be provided in the form: fqdn.registry.io/ exiting"
   exit 1
fi

# Before trying to pull or push anything, check for the existance of either docker or podman
container_engine=""
# Users may provide a preferred container engine using arg 2, otherwise the script checks whether it can use docker or podman.    
if [[ ! -z "$2" ]]; then
    # Ensure the user provided command is available to use 
    if cmd_exists $2; then
        container_engine=$2
    else # the user provided container engine command does not exist, exit with a message.
        echo >&2 "Script was provided with ${2} command to be used, but this command was not found."; exit 1;
    fi
elif cmd_exists docker; then
    # If docker exists, use that as our container engine
    container_engine=docker

elif cmd_exists podman; then
    # Or if podman is there and docker isin't use that
    container_engine=podman
else # neither of the engines were found, exit with a message
    echo >&2 "Image mirroring requires either Docker or Podman but neither were found. Aborting."; exit 1;
fi

# # ========================================
# #
# # Operational Logic to get images tags and transfer them
# #
# # ========================================

destination_registry=$1
# Read file to gather each image name, $image represents one imagename with a version
while IFS='' read -r image || [[ -n "$image" ]]; do 
    echo "Now starting to pull image: $image"

    # Pull the given image from the SOURCE_REGISTRY
    $container_engine pull "$SOURCE_REGISTRY/$image"

    echo "Image pulled; Retagging image before pushing"

    # Tag the image with our destination registry
    $container_engine tag "$SOURCE_REGISTRY/$image" "$destination_registry/$REGISTRY_ORG/$image"

    # Uncomment this if you are on AWS and want to have repositories created for your newly tagged images
    # aws ecr describe-repositories  --region us-east-2 --repository-names $image 2>&1 > /dev/null
    # status=$?
    # if [[ ! "${status}" -eq 0 ]]; then
    #     aws ecr create-repository --repository-name $image --region us-east-2
    # fi

    echo "Image tagged; Pushing now to destination registry: $destination_registry"

    # Push our newly tagged image to the destination
    $container_engine push "$destination_registry/$REGISTRY_ORG/$image"

    # After upload, check the second conf file to determine if this image should be removed
    if grep -Fxq $image $IMAGES_TO_PRESERVE_LOCALLY
    then
        echo "Transfer completed for image $image. The image $image was found in the list of images to be preserved and will not be removed locally"
    else
        echo "Transfer completed for image $image. Now cleaning up and removing these local images: $destination_registry/$REGISTRY_ORG/$image, $SOURCE_REGISTRY/$image"
    
        $container_engine rmi -f "$destination_registry/$REGISTRY_ORG/$image"
        
        $container_engine rmi -f "$SOURCE_REGISTRY/$image"
    fi

done < "$IMAGES_TO_TRANSFER"
