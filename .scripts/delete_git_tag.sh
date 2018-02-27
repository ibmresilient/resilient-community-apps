# This script will delete the latest git tag.
# This script will always run in jenkins after the script generate_git_tag.sh.
echo Deleting tag...
latestTag=$(git tag --list | tail -n 1)
git tag -d $latestTag
