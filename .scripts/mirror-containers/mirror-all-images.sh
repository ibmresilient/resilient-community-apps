#!/bin/bash

# Title:         mirror-images.sh
# Author:        ryan.gordon1@ibm.com
# Description:   Facilitates the transfer of a number of named images from a source registry to a destination one

# Version:       1.0.1
# Release notes
# 1.0.0 Initial Release
# 1.0.1 Enhancement for local registries with podman using --tls-verify flag
set -x

# v1: At a high level; with this script we want to:
# 0. Determine whether to use docker or podman
# 1. Query the QUAY REST API to gather all repos for the given namespace
# 2. For each repo:
# 2.1 Query each repo for tags and for each tag
# 2.1 Pull the tagged image from the source registry
# 2.2 Tag the image with its new destination tag before push
# 2.3 Push the image with its new tag to the destination registry
# 2.4 Delete both the local image we pushed as well as the destination retagged image(Local step)

# Syntax: mirror-all-images registry.com:5000 [podman|docker] [insecure_registry] [latest_tag]

## Functions
# Function used to check the existance of a command
function cmd_exists() {
  command -v $1 > /dev/null 2>&1
}
## Variables
readonly IMAGE_REGISTRY="${SOURCE_REGISTRY_DOMAIN:-quay.io}"
readonly REGISTRY_ORG="${SOURCE_REGISTRY_ORG:-ibmresilient}"
# The registry we will pull images from
readonly SOURCE_REGISTRY="$IMAGE_REGISTRY/$REGISTRY_ORG"
# This is an exposed cred; the cred has only the repo:read permission and is used to get a list of all images and tags from the REST API
readonly AUTH_TOKEN="j0ZG8Jm3hD3HRmXOaDMFsL0zWrRKjqsFJeswCHDF"
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
   printf 'Syntax: mirror-all-images registry.com:5000 [podman|docker] [insecure_registry] [latest_tag]'
   exit 1
fi
destination_registry=$1; shift

cmd_exists jq || { echo >&2 "Jq is required for parsing the API call responses from Quay and was not found in the environment."; exit 1; }

# Before trying to pull or push anything, check for the existance of either docker or podman
container_engine=""

# Users may provide a preferred container engine using arg 2, otherwise the script checks whether it can use docker or podman.
if [[ "$1" =~ "podman"|"docker" ]]; then
    # Ensure the user provided command is available to use
    if cmd_exists "${1}"; then
        container_engine=$1; shift
    fi
elif cmd_exists podman; then
    # If podman exists, use that as our default container engine
    container_engine=podman

elif cmd_exists docker; then
    # Or if docker is there and podman isn't, we use that
    container_engine=docker
else # neither of the engines were found, exit with a message
    echo >&2 "Image mirroring requires either Docker or Podman but neither were found. Aborting."; exit 1;
fi

if [[ $container_engine == "podman" && "$1" == "insecure_registry" ]]; then
    insecure_registry=1
else
    insecure_registry=0
fi

if [[ "$1" == "insecure_registry" ]]; then shift; fi

# collect only latest tag if cmd line argument is specified

#if [[ "$1" == "latest_tag" ]]; then
#    latest_tag=" | sort | tail -1"
#else
#    latest_tag=" | uniq"
#fi


# # ========================================
# #
# # Operational Logic to get images tags and transfer them
# #
# # ========================================

# First get a handle on all the repositories; use jq to parse the json and return only the names
repos=`curl -s "https://quay.io/api/v1/repository?namespace=${REGISTRY_ORG}" -H "authorization: Bearer ${AUTH_TOKEN}" | jq ".repositories[$count].name" | tr -d '"'`

while IFS= read -r repo;
do
    if [[ "$1" == "latest_tag" ]]; then
    echo "Starting to process all tags for repository: ${repo}"
    # Get all tags for the repo
    #tag_it=`curl -s "https://quay.io/api/v1/repository/${REGISTRY_ORG}/${repo}/tag/" -H "authorization: Bearer ${AUTH_TOKEN}" | jq ".tags[$count].name" | tr -d '"'`
    tags=`curl -s "https://quay.io/api/v1/repository/${REGISTRY_ORG}/${repo}/tag/" -H "authorization: Bearer ${AUTH_TOKEN}" | jq ".tags[$count].name" | sort | tail -1 | tr -d '"'`
    #tags="$tag_it$latest_tag"
    else
    echo "Starting to process all tags for repository: ${repo}"
    tags=`curl -s "https://quay.io/api/v1/repository/${REGISTRY_ORG}/${repo}/tag/" -H "authorization: Bearer ${AUTH_TOKEN}" | jq ".tags[$count].name" | uniq | tr -d '"'`
    fi
    echo "Made an API Call to Registry for repository $repo; Found these tags ${tags[@]}"
    while IFS= read -r tag;
    do
        # Pull the given image from the SOURCE_REGISTRY
        $container_engine pull "$SOURCE_REGISTRY/$repo:$tag"

        echo "Image pulled; Retagging image before pushing"

        # Tag the image with our destination registry
        $container_engine tag "$SOURCE_REGISTRY/$repo:$tag" "$destination_registry/$REGISTRY_ORG/$repo:$tag"

        # Uncomment this if you are on AWS and want to have repositories created for your newly tagged images
        # aws ecr describe-repositories  --region us-east-2 --repository-names $image 2>&1 > /dev/null
        # status=$?
        # if [[ ! "${status}" -eq 0 ]]; then
        #     aws ecr create-repository --repository-name $image --region us-east-2
        # fi

        echo "Image tagged; Pushing now to destination registry: $destination_registry"

        # Push our newly tagged image to the destination
        if [[ $container_engine == podman && $insecure_registry == 1 ]];
        then
           $container_engine push --tls-verify=false "$destination_registry/$REGISTRY_ORG/$repo:$tag"
        else
           $container_engine push "$destination_registry/$REGISTRY_ORG/$repo:$tag"
        fi
        echo "Transfer completed for image $image. Now cleaning up and removing these local images: $destination_registry/$REGISTRY_ORG/$repo:$tag, $SOURCE_REGISTRY/$repo:$tag"

        # Delete the images locally to avoid using up all storage during transfer
        $container_engine rmi -f "$destination_registry/$REGISTRY_ORG/$repo:$tag"

        $container_engine rmi -f "$SOURCE_REGISTRY/$repo:$tag"

    echo "Finished processing all tags for repository: ${repo}"
    # Finish processing the tags for a repository
    done <<< "$tags"
# Finish processing a repository
done <<< "$repos"
