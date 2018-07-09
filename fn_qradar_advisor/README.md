# Resilient Function for QRadar Advisor Integration

## Description

This function package provides the following features to be used in a workflow:

1. Perform a QRadar Advisor quick search
2. Perform a QRadar Advisor full search
3. Retrieve QRadar Advisor insights and analysis for a QRadar offense


## System Requirements
- Resilient Server version 30 or later
- QRadar 7.3.0 or later
- QRadar Advisor 1.12.1 or later
- Ability to connect to Resilient server with HTTPS on port 443 and 65001
- Ability to connect to QRadar server with HTTPS on port 443

## Package Dependences
- python requests
- resilient_circuits version 30 or later

## Installation
Install this package with 'pip', or run `python setup.py install`

## Setup
Create app.config by running `resilient-circuits config -c`.

The app.config needs the following configuration values, in addition to the appropriate [resilient] section for connecting to your Resilient platform:  

```
[fn_qradar_advisor]  
qradar_host=qradar_host
qradar_advisor_token=qradar_advisor_token_keyring_protection_recommended
qradar_advisor_app_id=app_id_from_qradar_server
verify_cert=[true, false] for verify https certificate or not
full_search_timeout=optional_full_search_timeout_in_seconds_default_1200
full_search_period=optional_full_search_period_in_seconds_default_5
offense_analysis_timeout=optional_offense_analysis_timeout_in_seconds_default_1200
offense_analysis_period=optional_offense_analysis_period_in_seconds_default_5
```


## Customize
Run with: `resilient-circuits customize` to install function definitions and sample workflows to the Resilient server.

## Start
Start this function app with: `resilient-circuits run`

## Samples
Please refer to the installation doc for more details about sample searches and workflows included in this package.

## Uninstall
Run with `pip uninstall fn_qradar_advisor`


