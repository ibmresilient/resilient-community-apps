#!/bin/bash -e

# param $1: (required) absolute path to save common scripts e.g. "$TRAVIS_BUILD_DIR/common_scripts"
# param $2: (required) raw.github.ibm.com to file to download e.g. "https://raw.github.ibm.com/Resilient/hydra-common-scripts/main/download_files_from_other_repo.py"

# Usage:
#   ./download_common_scripts.sh "$PATH_COMMON_SCRIPTS_DIR" "$GH_PATH_COMMON_SCRIPTS_REPO"

# Dependencies on:
#   the environmental variable GITHUB_AUTH_TOKEN is set and has read permissions of the repo to download from


###############
## Variables ##
###############
PATH_COMMON_SCIPTS_SAVE_LOC=$1
PATH_COMMON_SCRIPTS_REPO=$2
PATH_DOWNLOAD_SCRIPT_SAVE_LOC="$TRAVIS_BUILD_DIR/download_script.py"

##################
## Check params ##
##################
if [ -z "$1" ] ; then
    echo "ERROR: Must provide absolute path to save common scripts to as first parameter"
    exit 1
fi

if [ -z "$2" ] ; then
    echo "ERROR: Must provide raw.github.ibm.com to file to download e.g. https://raw.github.ibm.com/Resilient/hydra-common-scripts/main/download_files_from_other_repo.py"
    exit 1
fi

wget --header 'Authorization: token '$GITHUB_AUTH_TOKEN \
    -O $PATH_DOWNLOAD_SCRIPT_SAVE_LOC \
    $PATH_COMMON_SCRIPTS_REPO

python $PATH_DOWNLOAD_SCRIPT_SAVE_LOC "Resilient/hydra-common-scripts" "common" $PATH_COMMON_SCIPTS_SAVE_LOC
