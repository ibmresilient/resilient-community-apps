#!/bin/bash -e

# param $1: (required) internal branch name to push to. Normally 'public_main'
# param $2: (required) external branch name to sync to. Normally 'main'
# param $3: (required) path to the paths_to_exclude.txt file with each path on seperate line
# param $4: (required) path to the $PATH_SCRIPTS_DIR dir
# param $5: (required) path to the $PATH_COMMON_SCRIPTS_DIR dir
# param $6: (required) path to the $PATH_DOWNLOAD_SCRIPT file

# Dependencies on:
#   the environmental variable $GH_PUBLIC_SYNC_PATH which will include the $GH_PUBLIC_TOKEN_COMMUNITY_APPS
#   that must have write permissions of our EXTERNAL repo

###############
## Variables ##
###############
INTERNAL_BRANCH=$1
EXTERNAL_BRANCH=$2
PATH_EXCLUDE_FILES=$3
PATH_SCRIPTS_DIR=$4
PATH_COMMON_SCRIPTS_DIR=$5
PATH_DOWNLOAD_SCRIPT=$6
NOW=`date '+%Y_%m_%d'`
TEMP_BRANCH="repo_sync_$NOW"

##################
## Check params ##
##################
if [ -z "$1" ] ; then
    echo "ERROR: Must provide INTERNAL_BRANCH name as first parameter."
    exit 1
fi

if [ -z "$2" ] ; then
    echo "ERROR: Must provide EXTERNAL_BRANCH name as second parameter."
    exit 1
fi

if [ -z "$3" ] ; then
    echo "ERROR: Must provide PATH_EXCLUDE_FILES name as third parameter."
    exit 1
fi

if [ -z "$4" ] ; then
    echo "ERROR: Must provide PATH_SCRIPTS_DIR name as fourth parameter."
    exit 1
fi

if [ -z "$5" ] ; then
    echo "ERROR: Must provide PATH_COMMON_SCRIPTS_DIR name as fifth parameter."
    exit 1
fi

if [ -z "$6" ] ; then
    echo "ERROR: Must provide PATH_DOWNLOAD_SCRIPT name as sixth parameter."
    exit 1
fi

cd $TRAVIS_BUILD_DIR

###############
## Functions ##
###############
print_msg () {
    printf "\n--------------------\n$1\n--------------------\n"
}

rename_path () {
    src_path=$1
    target_path=$2

    print_msg "Renaming '$src_path' to '$target_path'"
    mv $src_path $target_path
}

###########
## Start ##
###########
print_msg "\
INTERNAL_BRANCH:\t$INTERNAL_BRANCH\n\
EXTERNAL_BRANCH:\t$EXTERNAL_BRANCH\n\
PATH_EXCLUDE_FILES:\t$PATH_EXCLUDE_FILES\n\
PATH_SCRIPTS_DIR:\t$PATH_SCRIPTS_DIR\n\
PATH_COMMON_SCRIPTS_DIR:\t$PATH_COMMON_SCRIPTS_DIR\n\
TEMP_BRANCH:\t\t$TEMP_BRANCH\
"

# Checkout new branch with no history
print_msg "Checking out new orphan branch: '$TEMP_BRANCH'"
git checkout --orphan $TEMP_BRANCH

# Get all PATHS to exclude
EXCLUDE_PATHS=( $(<$PATH_EXCLUDE_FILES) )

print_msg "Attempting to remove files: ${EXCLUDE_PATHS[*]}"

for path in "${EXCLUDE_PATHS[@]}"; do
    print_msg "rm -rf $TRAVIS_BUILD_DIR/$path"
    rm -rf $TRAVIS_BUILD_DIR/$path
done

rename_path "$PATH_SCRIPTS_DIR" "$PATH_SCRIPTS_DIR.bak"
rename_path "$PATH_COMMON_SCRIPTS_DIR" "$PATH_COMMON_SCRIPTS_DIR.bak"
rename_path "$PATH_DOWNLOAD_SCRIPT" "$PATH_DOWNLOAD_SCRIPT.bak"

print_msg "Locally commit all changes to '$TEMP_BRANCH'"
git add -A && git commit -q -m "Syncing external repository on $NOW"

print_msg "Checkout INTERNAL '$INTERNAL_BRANCH' branch"
git checkout $INTERNAL_BRANCH

print_msg "Merge changes in from '$TEMP_BRANCH' temp branch"
# --no-edit: avoid prompting for custom merge message
# -X theirs: automatically accept all incoming merge conflicts
# --allow-unrelated-histories: allow merging into a branch that has different history
git merge $TEMP_BRANCH --allow-unrelated-histories --no-edit -X theirs

print_msg "Push changes to INTERNAL '$INTERNAL_BRANCH' branch"
git push -u origin $INTERNAL_BRANCH

print_msg "Sync INTERNAL '$INTERNAL_BRANCH' with EXTERNAL '$EXTERNAL_BRANCH' branch"
git push $GH_PUBLIC_SYNC_PATH $INTERNAL_BRANCH:$EXTERNAL_BRANCH

rename_path "$PATH_SCRIPTS_DIR.bak" "$PATH_SCRIPTS_DIR"
rename_path "$PATH_COMMON_SCRIPTS_DIR.bak" "$PATH_COMMON_SCRIPTS_DIR"
rename_path "$PATH_DOWNLOAD_SCRIPT.bak" "$PATH_DOWNLOAD_SCRIPT"
