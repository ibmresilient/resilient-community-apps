#!/bin/bash -e

# param $1: (required) version of Python Libraries to use in format x.x.x
# param $2: (required) name of package that is in ALLOW_IMAGE_NAMES.txt to rebuild or ALL for all images in ALLOW_IMAGE_NAMES.txt
# param $3: (required) repo name to push to. Accepted values are: ARTIFACTORY, QUAY or BOTH.

# Dependencies on:
# sudo apt-get install jq
# pip install resilient-sdk

###############
## Variables ##
###############
PYTHON_LIBRARIES_VERSION=$1
IMAGE_TO_REBUILD=$2
REPO_TO_PUSH=$3
QUAY_API_URL="$QUAY_URL/api/v1"
PACKAGES_TO_CHANGE="[{\"name\":\"resilient\",\"version\":\"$PYTHON_LIBRARIES_VERSION\"},{\"name\":\"resilient-circuits\",\"version\":\"$PYTHON_LIBRARIES_VERSION\"},{\"name\":\"resilient-lib\",\"version\":\"$PYTHON_LIBRARIES_VERSION\"}]"
DOCKERFILE_KEYWORD="registry.access.redhat.com"
DOCKERFILE_WORDS_TO_INSERT="[\"\\n\", \"RUN pip install --upgrade pip\\n\", \"COPY ./new_requirements.txt /tmp/new_requirements.txt\\n\", \"RUN pip install -r /tmp/new_requirements.txt\\n\"]"
quay_io_tags=()
artifactory_tags=()
skipped_packages=()

##################
## Check params ##
##################
if [ -z "$1" ] ; then
    echo "Must provide Python Libraries version as first parameter"
    exit 1
fi

if [ -z "$2" ] ; then
    echo "Must provide ALL or <package_name> as second parameter"
    exit 1
fi

if [ -z "$3" ] ; then
    echo "Must provide repo name as third parameter: ARTIFACTORY, QUAY or BOTH"
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

###########
## Start ##
###########
print_msg "\
PYTHON_LIBRARIES_VERSION:\t$PYTHON_LIBRARIES_VERSION \n\
IMAGE_TO_REBUILD:\t$IMAGE_TO_REBUILD \n\
REPO_TO_PUSH:\t\t\t$REPO_TO_PUSH \n\
QUAY_URL:\t\t\t$QUAY_URL \n\
QUAY_API_URL:\t\t\t$QUAY_API_URL \n\
QUAY_USERNAME:\t\t\t$QUAY_USERNAME \n\
ARTIFACTORY_URL:\t\t$ARTIFACTORY_URL \n\
ARTIFACTORY_DOCKER_REPO:\t\t$ARTIFACTORY_DOCKER_REPO \n\
ARTIFACTORY_USERNAME:\t\t$ARTIFACTORY_USERNAME \n\
PATH_ALLOW_IMAGE_NAMES:\t\t$PATH_ALLOW_IMAGE_NAMES \n\
PACKAGES_TO_CHANGE:\t\t$PACKAGES_TO_CHANGE \n\
DOCKERFILE_KEYWORD:\t\t$DOCKERFILE_KEYWORD \n\
DOCKERFILE_WORDS_TO_INSERT:\t$DOCKERFILE_WORDS_TO_INSERT \n\
"

if [ "$IMAGE_TO_REBUILD" == "ALL" ] ; then
    # Make array of image names public on quay.io to rebuild
    print_msg "Getting list of IMAGE_NAMES at 'https://$QUAY_API_URL/repository?namespace=$QUAY_USERNAME&public=true'"
    IMAGE_NAMES=( $(curl "https://$QUAY_API_URL/repository?namespace=$QUAY_USERNAME&public=true" | jq -r ".repositories[].name") )

else
    IMAGE_NAMES=$IMAGE_TO_REBUILD
fi

print_msg "IMAGE_NAMES:\n${IMAGE_NAMES[*]}"

ALLOW_IMAGE_NAMES=( $(<$PATH_ALLOW_IMAGE_NAMES) )
print_msg "ALLOW_IMAGE_NAMES:\n${ALLOW_IMAGE_NAMES[*]}"

# Login to quay.io
if [ "$REPO_TO_PUSH" == "BOTH" ] || [ "$REPO_TO_PUSH" == "QUAY" ] ; then
    print_msg "Logging into $QUAY_URL as $QUAY_USERNAME"
    repo_login $QUAY_URL $QUAY_USERNAME $QUAY_PASSWORD
fi

# Login to artifactory
if [ "$REPO_TO_PUSH" == "BOTH" ] || [ "$REPO_TO_PUSH" == "ARTIFACTORY" ] ; then
    print_msg "Logging into artifactory as $ARTIFACTORY_USERNAME"
    repo_login $ARTIFACTORY_DOCKER_REPO $ARTIFACTORY_USERNAME $ARTIFACTORY_PASSWORD
fi

# Loop all image names at https://quay.io/user/$QUAY_USERNAME
for image_name in "${IMAGE_NAMES[@]}"; do

    # If in our allowed list
    if [[ " ${ALLOW_IMAGE_NAMES[@]} " =~ " ${image_name} " ]]; then

        print_msg="$image_name:: Starting: $image_name"

        resilient_sdk_package_pass=0
        docker_build_pass=0

        package_path="$TRAVIS_BUILD_DIR/$image_name"
        # Make available externally
        export PACKAGE_PATH=$package_path
        path_current_requirements="$package_path/current_requirements.txt"
        path_new_requirements="$package_path/new_requirements.txt"
        path_dockerfile="$package_path/Dockerfile"
        int_version=$(python "$package_path/setup.py" --version)
        print_msg "package_path:\t\t\t$package_path\npath_current_requirements:\t$path_current_requirements\npath_new_requirements:\t\t$path_new_requirements\npath_dockerfile:\t\t$path_dockerfile\nint_version:\t\t\t$int_version"

        # Check if package has extra travis script
        if [ -f "$package_path/$FILE_NAME_EXTRA_SETUP" ] ; then
            print_msg "Executing extra .sh travis setup file found at $package_path/$FILE_NAME_EXTRA_SETUP"
            sh $package_path/$FILE_NAME_EXTRA_SETUP
        fi

        docker_tag="$image_name:$int_version"
        quay_io_tag="$QUAY_URL/$QUAY_USERNAME/$docker_tag"

        print_msg "$image_name:: docker_tag:\t\t\t$docker_tag\nquay_io_tag:\t\t\t$quay_io_tag"

        print_msg "$image_name:: Pull image from $quay_io_tag"
        docker pull $quay_io_tag

        print_msg "$image_name:: Starting container for $quay_io_tag"
        # Can point -v to mock file but has to exist
        docker_container=`docker run -d -v $path_dockerfile:/etc/rescircuits/app.config $quay_io_tag`

        print_msg "$image_name:: Running pip freeze on $docker_container"
        docker exec -it $docker_container sh -c "pip freeze" > $path_current_requirements
        print_msg "$image_name:: Current requirements:\n$(cat $path_current_requirements)"

        print_msg "$image_name:: Stopping and removing $docker_container"
        docker stop $docker_container
        docker container rm $docker_container

        print_msg "$image_name:: Writing new requirements file"
        python $SCRIPTS_DIR/modify_requirements_file.py $path_current_requirements $path_new_requirements $PACKAGES_TO_CHANGE
        print_msg "$image_name:: New requirements:\n$(cat $path_new_requirements)"

        print_msg "$image_name:: Overwriting Dockerfile"
        python $SCRIPTS_DIR/insert_into_Dockerfile.py $path_dockerfile "$DOCKERFILE_KEYWORD" "$DOCKERFILE_WORDS_TO_INSERT"

        print_msg "$image_name:: Packaging $image_name with resilient-sdk"
        resilient-sdk package -p $package_path || resilient_sdk_package_pass=$?

        print_msg "$image_name:: Rebuilding: $image_name"

        # If passes resilient-sdk package build it with docker
        if [ $resilient_sdk_package_pass = 0 ] ; then

            print_msg "$image_name:: Rebuilding $image_name with docker"
            docker build \
            --quiet \
            -t $docker_tag \
            $package_path || docker_build_pass=$?

            # if passes docker build tag it
            if [ $docker_build_pass = 0 ] ; then
                # tag the image for quay.io
                quay_io_tag="$QUAY_URL/$QUAY_USERNAME/$image_name:$int_version"
                print_msg "$image_name:: Tagging $image_name for $QUAY_URL/$QUAY_USERNAME with: $quay_io_tag"
                docker tag $docker_tag $quay_io_tag
                quay_io_tags+=($quay_io_tag)

                # tag the image for artifactory
                artifactory_tag="$ARTIFACTORY_DOCKER_REPO/$QUAY_USERNAME/$image_name:$int_version"
                print_msg "$image_name:: Tagging $image_name for artifactory with: $artifactory_tag"
                docker tag $docker_tag $artifactory_tag
                artifactory_tags+=($artifactory_tag)

                print_msg "$image_name:: Done building: $image_name"
            fi
        fi

        if [ $resilient_sdk_package_pass != 0 ] || [ $docker_build_pass != 0 ] ; then
            print_msg "$image_name:: Packaging or building failed. Adding $image_name to list of skipped_packages"
            skipped_packages+=($image_name)
        fi

    else
        print_msg "$image_name:: $image_name is NOT in $PATH_ALLOW_IMAGE_NAMES\nAdding it to list of skipped_packages"
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