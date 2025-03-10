# Utilities (Deprecated)

- [Utility Functions for IBM SOAR](#utility-functions-for-ibm-soar)
  - [Release Notes](#release-notes)
    - [Release History](#release-history)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Uninstall](#uninstall)
  - [Troubleshooting](#troubleshooting)
    - [SOAR Action Status](#soar-action-status)
    - [SOAR Scripting Log](#soar-scripting-log)
    - [SOAR Logs](#soar-logs)
    - [Resilient-Circuits](#resilient-circuits)
  - [Support](#support)

---

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release
  notes of a previous release
-->
### Release History

| Version | Date   | Notes |
| ------- | ------ |:----- |
| 2.1.3 | 03/2023 | Remove log for rest_headers in fn_call_rest_api |
| 2.1.2 | 01/2023 | Bug fix for version of cryptography |
| 2.1.1 | 04/2022 | Bug fix for selftest |
| 2.1.0 | 03/2022 | <ul><li>Support for PATCH method</li><li>Add rule to get owner contact info for Tasks</li><li>Bug fix for utilities_pdfid</li><li>Add new utilities_artifact_hash function</li><li>Add a timeout parameter to call_rest_api function</li></ul> |
| 2.0.6 | 07/2021 | pin dependency 'chardet' at v4.0.0 |
| 2.0.2 | 02/2021 | bug fixes for Shell Command |
| 2.0.1 | 09/2020 | bug fixes |
| 2.0.0 | 07/2020 | Numerous fixes, improved Rules and workflows and only Python 3 supported |
| 1.0.15 | 05/2020 | Bug fixes, App Host Support |
| 1.0.14 | 05/2020 | Shell Command support for Remote Linux Execution |


---

## Overview
<!--
  Provide a high-level description of the function itself and its remote software or application.
  The text below is parsed from the "description" and "long_description" attributes in the setup.py file
-->
**Useful workflow functions for common automation and integration activities in the SOAR platform**

 ![screenshot: main](./doc/screenshots/main.png)

SOAR functions simplify development of integrations by wrapping each external activity into an individual workflow component. These components can be easily installed, then used and combined in SOAR workflows. The SOAR platform sends data to the function component that performs an activity then returns the results to the workflow. The results can be acted upon by scripts, rules, and workflow decision points to dynamically orchestrate the security incident response activities

---

## Requirements
<!--
  List any Requirements
-->
* SOAR platform >= `v42.0`
* An Integration Server running `resilient_circuits>=47.1.0`
  * To set up an Integration Server see: [ibm.biz/res-int-server-guide](https://ibm.biz/res-int-server-guide)

---

## Installation
* Download the `fn_utilities.zip`.
* Copy the `.zip` to your Integration Server and SSH into it.
* **Unzip** the package:
  ```
  $ unzip fn_utilities-x.x.x.zip
  ```
* **Change Directory** into the unzipped directory:
  ```
  $ cd fn_utilities-x.x.x
  ```
* **Install** the package:
  ```
  $ pip install fn_utilities-x.x.x.tar.gz
  ```
* Import the **configurations** into your app.config file:
  ```
  $ resilient-circuits config -u
  ```
* Import the fn_utilities **customizations** into the SOAR platform:
  ```
  $ resilient-circuits customize -y -l fn-utilities
  ```
* Open the config file, scroll to the bottom and edit your fn_utilities configurations:
  ```
  $ nano ~/.resilient/app.config
  ```
  | Config | Required | Example | Description |
  | ------ | :------: | ------- | ----------- |
  | **shell_escaping** | No | `sh` | For safety, shell_command parameter values are escaped. Set this to `sh` (Bash) or `ps` (PowerShell). |
  | **remote_powershell_extensions** | No | `ps1, psm1` | A CSV list of extensions a remote PowerShell is trusted to run. |
  | **remote_auth_transport** | No | `ntlm` | Transport authentication method for a remote PowerShell. Can be NTLM or basic. |
  | **max_timer** | No | `30d` | Max Timer sleep time. The input string is of format “time value” concatenated with a “time unit” character, where character is: ‘s’ for seconds, ‘m’ for minutes, ‘h’ for hours ‘d’ for days.  For example: '30s' = 30 seconds; '40m' = 40 minutes; |

* **Save** and **Close** the app.config file.
* [Optional]: Run selftest to test the Integration you configured:
  ```
  $ resilient-circuits selftest -l fn-utilities
  ```
* **Run** resilient-circuits or restart the Service on Windows/Linux:
  ```
  $ resilient-circuits run
  ```

---

## Uninstall
* SSH into your Integration Server.
* **Uninstall** the package:
  ```
  $ pip uninstall fn-utilities
  ```
* Open the config file, scroll to the [fn_utilities] section and remove the section or prefix `#` to comment out the section.
* **Save** and **Close** the app.config file.

---

## Troubleshooting
There are several ways to verify the successful operation of a function.

### SOAR Action Status
* When viewing an incident, use the Actions menu to view **Action Status**.
* By default, pending and errors are displayed.
* Modify the filter for actions to also show Completed actions.
* Clicking on an action displays additional information on the progress made or what error occurred.

### SOAR Scripting Log
* A separate log file is available to review scripting errors.
* This is useful when issues occur in the pre-processing or post-processing scripts.
* The default location for this log file is: `/var/log/resilient-scripting/resilient-scripting.log`.

### SOAR Logs
* By default, SOAR logs are retained at `/usr/share/co3/logs`.
* The `client.log` may contain additional information regarding the execution of functions.

### Resilient-Circuits
* The log is controlled in the `.resilient/app.config` file under the section [resilient] and the property `logdir`.
* The default file name is `app.log`.
* Each function will create progress information.
* Failures will show up as errors and may contain python trace statements.

---

<!--
  If necessary, use this section to describe how to configure your security application to work with the integration.
  Delete this section if the user does not need to perform any configuration procedures on your product.

## Configure <Product_Name>

* Step One
* Step Two
* Step Three

---
-->

## Support
| Name | Version | Author | Support URL |
| ---- | ------- | ------ | ----------- |
| fn_utilities | 1.0.10 | IBM SOAR | http://ibm.biz/soarcommunity |