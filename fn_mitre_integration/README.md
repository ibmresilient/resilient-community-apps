# Resilient Function for MITRE ATT&CK Integration

## Description

This function package provides the following features to be used in a workflow:
1. For a given MITRE ATT&CK tactic, fetch the followings from the MITRE STIX TAXII server
* All the techniques associated with this tactic, together with
- Reference links
- Description
- Detection
* Tactic ID and reference link
2. For a given MITRE ATT&CK, fetch the mitigation from the MITRE STIX TAXII server

## System Requirements
- Resilient Server version 30 or later
- Ability to connect to Resilient server with HTTPS on port 443 and 65001
- Ability to connect to QRadar server with HTTPS on port 443
- Ability to connect to MITRE STIX TAXII server (https://cti-taxii.mitre.org/taxii/)

## Package Dependences
- python requests
- python stix2
- python taxii2client
- resilient_circuits version 30 or later

## Installation
Install this package with 'pip', or run `python setup.py install`

## Setup
Create app.config by running `resilient-circuits config -c`.
Fill in proper information in the appropriate [resilient] section for connecting to your Resilient platform

## Customize
Run with: `resilient-circuits customize` to install function definitions and sample workflows to the Resilient server.

## Start
Start this function app with: `resilient-circuits run`

## Samples
Please refer to the installation doc for more details about sample searches and workflows included in this package.

## Uninstall
Run with `pip uninstall fn_mitre_integration`