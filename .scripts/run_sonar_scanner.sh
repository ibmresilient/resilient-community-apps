#!/bin/bash -e

# param $1: (required)  CSV string of source files to include in the Sonar scan.
#                       It is the value of `sonar.sources` in the sonar-project.properties file
# param $2: (required)  Path to the location of the downloaded common scripts
# param $3: (optional)  0 if we want coverage downloaded from artifactory and included in the sonar scan
#                       1 if we do not want any test coverage included
#
# Usage:
#   $ run_sonar_scanner.sh "$PACKAGE_NAME/$PACKAGE_NAME" "$PATH_COMMON_SCRIPTS_DIR" 1
#
#   In Travis:
#       - ALL_ALLOWED_IMAGES=`python $PATH_SCRIPTS_DIR/get_all_allowed_image_names.py "$PATH_ALLOW_IMAGE_NAMES" --ignore-lines "rc-" "rc_data_feed_plugin_odbcfeed"`
#       - $PATH_SCRIPTS_DIR/run_sonar_scanner.sh "$ALL_ALLOWED_IMAGES" "$PATH_COMMON_SCRIPTS_DIR" 1

###############
## Variables ##
###############
SOURCE_FILES=$1
PATH_COMMON_SCRIPTS_DIR=$2
DOWNLOAD_COV_FILES=$3

##################
## Check params ##
##################
if [ -z "$1" ] ; then
    echo "ERROR: CSV string of source files to include in the Sonar scan as first parameter"
    exit 1
fi

if [ -z "$2" ] ; then
    echo "ERROR: Path to the location of the downloaded common scripts must be set as second parameter"
    exit 1
fi

if [ -z "$3" ] ; then
    echo "WARNING: not specified if we need coverage - so we are setting it to 1 by default"
    DOWNLOAD_COV_FILES=1
fi

###############
## Functions ##
###############
print_msg () {
    printf "\n--------------------\n$1\n--------------------\n"
}

if [ $DOWNLOAD_COV_FILES -eq 0 ]
then
    # Download coverage files
    python $PATH_COMMON_SCRIPTS_DIR/manage_artifactory.py "DOWNLOAD" "$ARTIFACTORY_COV_LOCATION" --save-location "$TRAVIS_BUILD_DIR/$PATH_COV_SAVE_LOC"
fi

print_msg "Updating '$PATH_SONAR_PROPERTIES' file"

# Update the sonar-project.properties file
sed -e "s|{{SONAR_QUBE_BRANCH}}|$TRAVIS_BRANCH|" \
-e "s|{{SONAR_QUBE_PROJ_KEY}}|$SONAR_QUBE_PROJ_KEY|" \
-e "s|{{PATH_COV_SAVE_LOC}}|$PATH_COV_SAVE_LOC|" \
-e "s|{{SONAR_QUBE_FILES_FOR_SCAN}}|$SOURCE_FILES|" \
$PATH_SONAR_PROPERTIES > $PATH_SONAR_PROPERTIES.tmp && mv $PATH_SONAR_PROPERTIES.tmp $PATH_SONAR_PROPERTIES

print_msg "Running sonar-scanner on: '$SOURCE_FILES'"

# Run the sonar-scanner
/tmp/sonar-scanner-$SONAR_SCANNER_VERSION-linux/bin/sonar-scanner -Dsonar.host.url=$SONAR_QUBE_URL -Dsonar.login=$SONAR_QUBE_TOKEN

print_msg "Waiting for '$SONAR_QUBE_SEC_TO_WAIT_FOR_ANALYSIS' seconds for SonarQube Analysis report to be generated"

# Sleep here to ensure there is sufficient time for analysis report
# to be generated. This is a Travis env var and can be adjusted
sleep $SONAR_QUBE_SEC_TO_WAIT_FOR_ANALYSIS

# Get analysis status
python $PATH_COMMON_SCRIPTS_DIR/get_sonar_qube_project_status.py "$SONAR_QUBE_URL" "$SONAR_QUBE_TOKEN" "$SONAR_QUBE_PROJ_KEY" "$TRAVIS_BRANCH"
