#!/bin/bash
# This script is used to bring files from the top level of resilient-community-apps into the integration directory
# to be used during the docker build process. We need to copy the files into the inegration directory because docker
# is unable to access files outside of the build process (anything in the filestructure above the working directory).

# Create a drivers directory and copy the content from ../.odbc_drivers
echo "copying odbc drivers into the integration directory"
mkdir drivers
cp ./.odbc_drivers ./fn_odbc_query/drivers
