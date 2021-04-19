#!/bin/bash -e

# param $1: (required) which package_name to build. It MUST be in ALLOW_IMAGE_NAMES.txt
# param $2: (required) the BUILD_TYPE. Accepted values are: DEV or MAIN
# param $3: (required) the PYPI_INDEX_TO_USE when building the images with Docker: e.g. "https://pypi.org/simple" or $ARTIFACTORY_PYPI_INDEX

# Dependencies on:
# pip install resilient-sdk

###############
## Variables ##
###############
PACKAGE_NAME=$1
BUILD_TYPE=$2
PYPI_INDEX_TO_USE=$3


##################
## Check params ##
##################
if [ -z "$1" ] ; then
    echo "ERROR: Must provide PACKAGE_NAME as first parameter"
    exit 1
fi

if [ -z "$2" ] ; then
    echo "ERROR: Must provide BUILD_TYPE as second parameter. Accepted values are DEV or MAIN"
    exit 1
fi

if [ -z "$3" ] ; then
    echo "ERROR: Must provide PYPI_INDEX_TO_USE as third parameter"
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
PACKAGE_NAME:\t\t$PACKAGE_NAME \n\
BUILD_TYPE:\t\t$BUILD_TYPE \n\
PYPI_INDEX_TO_USE:\t$PYPI_INDEX_TO_USE \n\
"

ALLOW_IMAGE_NAMES=( $(<$PATH_ALLOW_IMAGE_NAMES) )
print_msg "ALLOW_IMAGE_NAMES:\n${ALLOW_IMAGE_NAMES[*]}"

# If NOT in our allowed list, exit
if [[ ! " ${ALLOW_IMAGE_NAMES[@]} " =~ " ${PACKAGE_NAME} " ]]; then
    print_msg "'$PACKAGE_NAME' is not a valid name or is not in $PATH_ALLOW_IMAGE_NAMES"
    exit 1
fi

# Login to quay.io
if [ "$BUILD_TYPE" == "MAIN" ] ; then
    print_msg "Logging into $QUAY_URL as $QUAY_USERNAME"
    repo_login $QUAY_URL $QUAY_USERNAME $QUAY_PASSWORD
fi

# Login to artifactory
if [ "$BUILD_TYPE" == "DEV" ] ; then
    print_msg "Logging into artifactory as $ARTIFACTORY_USERNAME"
    repo_login $ARTIFACTORY_DOCKER_REPO $ARTIFACTORY_USERNAME $ARTIFACTORY_PASSWORD
fi

package_path="$TRAVIS_BUILD_DIR/$PACKAGE_NAME"

# Update setup.py with new version
path_setup_py_file="$package_path/setup.py"
current_version=$(python $path_setup_py_file --version)
lib_version=$(echo $current_version | cut -d "." -f 1,2)
version_to_use=current_version

if [ "$BUILD_TYPE" == "DEV" ] ; then
    version_to_use=$lib_version.$TRAVIS_BUILD_NUMBER
    print_msg "Updating $path_setup_py_file to version '$version_to_use'"
    python $SCRIPTS_DIR/modify_attribute_in_setup_py_file.py "$package_path/setup.py" "version" "version=\"$version_to_use\","
fi

docker_tag="$PACKAGE_NAME:$version_to_use"

print_msg "Packaging $PACKAGE_NAME with resilient-sdk"
resilient-sdk package -p $package_path
app_zip_path=$(ls $package_path/dist/*.zip)

print_msg "Building $PACKAGE_NAME with docker"
image_sha_digest=`docker build \
-q \
-t $docker_tag \
$package_path`
image_sha_digest=$(echo $image_sha_digest | cut -d ":" -f 2)

print_msg "image_sha_digest=$image_sha_digest"

# tag the image for quay.io
quay_io_tag="$QUAY_URL/$QUAY_USERNAME/$PACKAGE_NAME:$version_to_use"
print_msg "Tagging $PACKAGE_NAME for $QUAY_URL/$QUAY_USERNAME with: $quay_io_tag"
docker tag $docker_tag $quay_io_tag

# tag the image for artifactory
artifactory_tag="$ARTIFACTORY_DOCKER_REPO/$QUAY_USERNAME/$PACKAGE_NAME:$version_to_use"
print_msg "Tagging $PACKAGE_NAME for artifactory with: $artifactory_tag"
docker tag $docker_tag $artifactory_tag

print_msg "Done building: $PACKAGE_NAME"

if [ "$BUILD_TYPE" == "MAIN" ] ; then
    print_msg "Push to quay.io for $BUILD_TYPE"

    print_msg "Pushing $quay_io_tag to quay.io"
    # docker push $quay_io_tag

    full_file_name=$(basename -- $app_zip_path)
    file_name="${full_file_name%.*}-$TRAVIS_BUILD_NUMBER.zip"
    artifactory_path="$ARTIFACTORY_GENERIC_STORAGE/$PACKAGE_NAME/main/$lib_version/$file_name"
    print_msg "copying App.zip $file_name to Artifactory at: $artifactory_path"
    # curl -H [header including the Artifactory API Key] -T [path to the file to upload to Artifactory] "https://na.artifactory.swg-devops.com/artifactory/<repo-name>/<path-in-repo>"
    curl -H "X-JFrog-Art-Api:${ARTIFACTORY_API_KEY}" -T $app_zip_path $artifactory_path

    echo "$artifactory_path"
    echo "$artifactory_path" >> $TRAVIS_BUILD_DIR/PATH_APP_ZIP.txt
fi

if [ "$BUILD_TYPE" == "DEV" ] ; then
    print_msg "Re-packing + push to Artifactory for $BUILD_TYPE"

    print_msg "Re-packaging $PACKAGE_NAME with resilient-sdk --image-hash '$image_sha_digest'"
    resilient-sdk package -p $package_path --image-hash "$image_sha_digest"
    app_zip_path=$(ls $package_path/dist/*.zip)

    print_msg "Pushing $artifactory_tag to artifactory"
    docker push $artifactory_tag

    file_name=$(basename $app_zip_path)
    artifactory_path="$ARTIFACTORY_GENERIC_STORAGE/$PACKAGE_NAME/development/$lib_version/$file_name"
    print_msg "copying App.zip $file_name to Artifactory at: $artifactory_path"
    # curl -H [header including the Artifactory API Key] -T [path to the file to upload to Artifactory] "https://na.artifactory.swg-devops.com/artifactory/<repo-name>/<path-in-repo>"
    curl -H "X-JFrog-Art-Api:${ARTIFACTORY_API_KEY}" -T $app_zip_path $artifactory_path

    echo "$artifactory_path"
    echo "$artifactory_path" >> $TRAVIS_BUILD_DIR/PATH_APP_ZIP.txt
fi
