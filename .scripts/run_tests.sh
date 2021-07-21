#!/bin/bash -e

# param $1: (required) which package_name to run the tests for or ALL.
#           If ALL, run tox for all packages in ALLOW_IMAGE_NAMES.txt
# param $2: (required) the PYPI_INDEX to use when running tox
#            "https://pypi.org/simple" or $ARTIFACTORY_PYPI_INDEX

###############
## Variables ##
###############
PACKAGE_NAME=$1
PYPI_INDEX_TO_USE=$2

##################
## Check params ##
##################
if [ -z "$1" ] ; then
    echo "ERROR: Must provide PACKAGE_NAME or 'ALL' as first parameter"
    exit 1
fi

if [ -z "$2" ] ; then
    echo "ERROR: Must provide PYPI_INDEX_TO_USE as second parameter"
    exit 1
fi

###############
## Functions ##
###############
print_msg () {
    printf "\n--------------------\n$1\n--------------------\n"
}

###########
## Start ##
###########
print_msg "\
PACKAGE_NAME:\t$PACKAGE_NAME \n\
"

if [ "$PACKAGE_NAME" == "MERGE" ] ; then
    print_msg "Latest commit is a Merge. Not running tests"
    exit 0
fi

ALLOW_IMAGE_NAMES=( $(<$PATH_ALLOW_IMAGE_NAMES) )
print_msg "ALLOW_IMAGE_NAMES:\n${ALLOW_IMAGE_NAMES[*]}"

if [ "$PACKAGE_NAME" == "ALL" ] ; then
    print_msg "Running ALL tests"

    for p in "${ALLOW_IMAGE_NAMES[@]}"; do
        # If line starts with a '#', skip it
        if [[ $p == \#* ]] ; then
            print_msg "Skipping comment: $p..."
        else
            print_msg "Running tests for $p"
            package_path=$TRAVIS_BUILD_DIR/$p
            tox -c $package_path -i $PYPI_INDEX_TO_USE -- \
            --resilient_email 'integrations@example.org' \
            --resilient_password 'supersecret' \
            --resilient_host 'example.com' \
            --resilient_org 'Test Organization' \
            -m "not livetest"
            print_msg "Test complete for $p"
        fi
    done
else
    # If NOT in our allowed list, exit
    if [[ ! " ${ALLOW_IMAGE_NAMES[@]} " =~ " ${PACKAGE_NAME} " ]]; then
        print_msg "'$PACKAGE_NAME' is not a valid name or is not in $PATH_ALLOW_IMAGE_NAMES"
        exit 1
    fi

    print_msg "Running tests for $PACKAGE_NAME"
    package_path=$TRAVIS_BUILD_DIR/$PACKAGE_NAME
    tox -c $package_path -i $PYPI_INDEX_TO_USE -- \
    --resilient_email 'integrations@example.org' \
    --resilient_password 'supersecret' \
    --resilient_host 'example.com' \
    --resilient_org 'Test Organization' \
    -m "not livetest"
    print_msg "Test complete for $PACKAGE_NAME"
fi
