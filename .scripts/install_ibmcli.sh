#!/bin/bash -e

# install IBM Cloud CLI
curl -fsSL https://clis.cloud.ibm.com/install/linux | sh
ibmcloud plugin install container-registry
