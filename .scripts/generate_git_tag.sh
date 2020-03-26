# This script will create a git tag adding the jenkins build number.
# we're only looking at the tags in the form of v<version>
libVersion=$(git tag --list | grep "v[0-9]" | tail -n 1 | cut -d "." -f 1,2)

echo Creating tag...
git tag -a $libVersion.$BUILD_NUMBER -m "$libVersion Build $BUILD_NUMBER"


