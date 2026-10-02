#!/bin/bash

# This script is used to bring files from the top level of resilient-community-apps into the integration directory
# to be used during the docker build process. We need to copy the files into the inegration directory because docker
# is unable to access files outside of the build process (anything in the filestructure above the working directory).

# When ran in SPS this script will have access to all
# env vars specifically $PACKAGE_PATH and $PIPELINE_BUILD_DIR

echo "copying drivers into the fn_odbc_query/.drivers directory"
cp -R $PIPELINE_BUILD_DIR/.drivers $PACKAGE_PATH/.drivers

echo "Installing OS-level packages"
sudo yum install -y unixodbc-dev
sudo yum install -y gcc
