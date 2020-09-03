# Resilient Function for QRadar Advisor Integration
## Release Notes
<!--
  Specify all changes in this release. Do not remove the release 
  notes of a previous release
-->
### v2.0.2
- Support added for App Host.
- Support added for proxies.
- Updated deprecated API endpoints.
- Bug fixes.

### v2.0.1
- Bug fixes for Python 3.

### v2.0
- Supports the V2.0 release.

### v1.0.1
- For Watson Search fixed version compatibility with search that returns no data.
- Fix typo in post-process script.

### v1.0
- Initial release.

---

## Description

This function package provides the following features to be used in a workflow:

1. Perform a QRadar Advisor quick search
2. Perform a QRadar Advisor full search
3. Retrieve QRadar Advisor insights and analysis for a QRadar offense
4. Map a given QRadar rule to MITRE ATT&CK tactics.

## System Requirements
- Resilient Server version 31 or later
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
#http_proxy=http://proxy:80
#https_proxy=https://proxy:80
```

## Customize
Run with: `resilient-circuits customize` to install function definitions and sample workflows to the Resilient server.

## Test
[Optional]: Run selftest to test the Integration you configured:
```
resilient-circuits selftest -l fn-qradar-advisor
```
## Start
Start this function app with: `resilient-circuits run`

## Samples
Please refer to the installation doc for more details about sample searches and workflows included in this package.

## Uninstall
Run with `pip uninstall fn_qradar_advisor`

---

## Troubleshooting
There are several ways to verify the successful operation of a function.

### Resilient Action Status
* When viewing an incident, use the Actions menu to view Action Status.
By default, pending and errors are displayed.
* Modify the filter for actions to also show Completed actions.
Clicking on an action displays additional information on the progress made or what error occurred.

### Resilient Scripting Log
* A separate log file is available to review scripting errors. This is useful when issues occur in the pre-processing or post-processing scripts.
* The default location for this log file is: `/var/log/resilient-scripting/resilient-scripting.log`.

### Resilient Logs
* By default, Resilient logs are retained at `/usr/share/co3/logs`.
* The `client.log` may contain additional information regarding the execution of functions.

### Resilient-Circuits
* The log is controlled in the `.resilient/app.config` file under the section [resilient] and the property `logdir`.
* The default file name is `app.log`.
* Each function creates progress information.
* Failures show up as errors and may contain python trace statements.

---

## Support
| Name | Version | Author | Support URL |
| ---- | ------- | ------ | ----------- |
| fn_qradar_advisor | 2.0.2 | IBM Resilient |  |
