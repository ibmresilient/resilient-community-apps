#!/bin/bash -e

# param $1: (required) CSV string of source files to include in the Sonar scan.
#           It is the value of `sonar.sources` in the sonar-project.properties file

##################
## Check params ##
##################
if [ -z "$1" ] ; then
    echo "ERROR: CSV string of source files to include in the Sonar scan as first parameter"
    exit 1
fi

# Download common scripts
$PATH_SCRIPTS_DIR/download_common_scripts.sh "$PATH_COMMON_SCRIPTS_DIR" "$GH_PATH_COMMON_SCRIPTS_REPO"

# Download coverage files
# python $PATH_COMMON_SCRIPTS_DIR/manage_artifactory.py "DOWNLOAD" "$ARTIFACTORY_COV_LOCATION" --save-location "$TRAVIS_BUILD_DIR/$PATH_COV_SAVE_LOC"

# Update the sonar-project.properties file
sed -e "s|{{SONAR_QUBE_BRANCH}}|$TRAVIS_BRANCH|" \
-e "s|{{SONAR_QUBE_PROJ_KEY}}|$SONAR_QUBE_PROJ_KEY|" \
-e "s|{{PATH_COV_SAVE_LOC}}|$PATH_COV_SAVE_LOC|" \
-e "s|{{SONAR_QUBE_FILES_FOR_SCAN}}|$1|" \
$PATH_SONAR_PROPERTIES > $PATH_SONAR_PROPERTIES.tmp && mv $PATH_SONAR_PROPERTIES.tmp $PATH_SONAR_PROPERTIES

# Run the sonar-scanner
/tmp/sonar-scanner-$SONAR_SCANNER_VERSION-linux/bin/sonar-scanner -Dsonar.host.url=$SONAR_QUBE_URL -Dsonar.login=$SONAR_QUBE_TOKEN

# Sleep here to ensure there is sufficient time for analysis report
# to be generated. This is a Travis env var and can be adjusted
sleep $SONAR_QUBE_SEC_TO_WAIT_FOR_ANALYSIS

# Get analysis status
python $PATH_COMMON_SCRIPTS_DIR/get_sonar_qube_project_status.py "$SONAR_QUBE_URL" "$SONAR_QUBE_TOKEN" "$SONAR_QUBE_PROJ_KEY" "$TRAVIS_BRANCH"
