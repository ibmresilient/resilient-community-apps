# fn-symantec-dlp Integration for IBM Resilient

- [Release Notes](#release-notes)
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Uninstall](#uninstall)
- [Troubleshooting](#troubleshooting)
- [Support](#support)

---

## Release Notes
### v0.0.1
* Pre-Release -- DLP Polling Component to import Incidents into Resilient.

---

## Overview
**Resilient Circuits Components used to establish DLP as a source of Incidents for Resilient**

 ![screenshot: main](./doc/screenshots/main.png)

Included in this package are two main components; a Incident Poller used to gather Incidents from DLP and a Resilient Circuits Function for updating a Symantec DLP Incident from Resilient

---

## Requirements
<!--
  List any Requirements 
-->
* Resilient platform >= `v31.0.4235`
* An Integration Server running `resilient_circuits>=30.0.0`
  * To set up an Integration Server see: [ibm.biz/res-int-server-guide](https://ibm.biz/res-int-server-guide)

---

## Installation
* Download the `fn_symantec_dlp.zip`.
* Copy the `.zip` to your Integration Server and SSH into it.
* **Unzip** the package:
  ```
  $ unzip fn_symantec_dlp-x.x.x.zip
  ```
* **Change Directory** into the unzipped directory:
  ```
  $ cd fn_symantec_dlp-x.x.x
  ```
* **Install** the package:
  ```
  $ pip install fn_symantec_dlp-x.x.x.tar.gz
  ```
* Import the **configurations** into your app.config file:
  ```
  $ resilient-circuits config -u
  ```
* Import the fn_symantec_dlp **customizations** into the Resilient platform:
  ```
  $ resilient-circuits customize -y -l fn-symantec-dlp
  ```
* Open the config file, scroll to the bottom and edit your fn_symantec_dlp configurations:
  ```
  $ nano ~/.resilient/app.config
  ```
  | Config | Required | Example | Description |
  | ------ | :------: | ------- | ----------- |
  | **sdlp_should_poller_run** | Yes | `True` | *Whether or not to start the listener* |
  | **sdlp_host** | Yes | `https://<serverip>:<port>` | *The URL of the DLP Installation* |
  | **sdlp_wsdl** | Yes | `https://<serverip>:<port>/ProtectManager/services/v2011/incidents?wsdl` | *The location of your WSDL file used to construct requests when dealing with the Incident and Reporting API* |
  | **sdlp_incident_endpoint** | Yes | `https://<serverip>:<port>/ProtectManager/services/v2011/incidents` | *The URL of the Incident and Reporting API for your DLP Installation* |
  | **sdlp_username** | Yes | `<SDLP Username>` | *Username for DLP* |
  | **sdlp_password** | Yes | `<SDLP Password>` | *Password for DLP* |
  | **sdlp_cafile** | No | `<SDLP Password>` | *Location of the CA file for DLP, leave Blank or ‘comment out’ for unverified requests* |
  | **sdlp_listener_timer** | Yes | `600` | *Used to set how often the Listener should poll, default is 10 mins (600)sdlp_listener_timer=600* |
  | **sdlp_savedreportid** | Yes | `0` | *The Saved Report ID used to query for Incidents, must be set otherwise the integration will fail* |
  | **sdlp_should_search_res** | Yes | `False` | *An optional app.config that, if set to True will perform an additional filter on DLP Incident results 
  to ensure no Resilient incident exists with the same DLP Incident ID. 
  Uses search_ex to query for incidents with an sdlp_incident_id custom field* |

* **Save** and **Close** the app.config file.
* [Optional]: Run selftest to test the Integration you configured:
  ```
  $ resilient-circuits selftest -l fn-symantec-dlp
  ```
* **Run** resilient-circuits or restart the Service on Windows/Linux:
  ```
  $ resilient-circuits run
  ```

### Custom Layouts
# TODO: Finish this section when all custom fields defined.
* Import the Data Tables and Custom Fields like the screenshot below:

  ![screenshot: custom_layouts](./doc/screenshots/custom_layouts.png)

---

## Uninstall
* SSH into your Integration Server.
* **Uninstall** the package:
  ```
  $ pip uninstall fn-symantec-dlp
  ```
* Open the config file, scroll to the [fn_symantec_dlp] section and remove the section or prefix `#` to comment out the section.
* **Save** and **Close** the app.config file.

---

## Troubleshooting
There are several ways to verify the successful operation of a function.

### Resilient Action Status
* When viewing an incident, use the Actions menu to view **Action Status**.
* By default, pending and errors are displayed.
* Modify the filter for actions to also show Completed actions.
* Clicking on an action displays additional information on the progress made or what error occurred.

### Resilient Scripting Log
* A separate log file is available to review scripting errors.
* This is useful when issues occur in the pre-processing or post-processing scripts.
* The default location for this log file is: `/var/log/resilient-scripting/resilient-scripting.log`.

### Resilient Logs
* By default, Resilient logs are retained at `/usr/share/co3/logs`.
* The `client.log` may contain additional information regarding the execution of functions.

### Resilient-Circuits
* The log is controlled in the `.resilient/app.config` file under the section [resilient] and the property `logdir`.
* The default file name is `app.log`.
* Each function will create progress information.
* Failures will show up as errors and may contain python trace statements.

---


## Configure Symantec DLP 
This Integration with Symantec DLP works by querying a Saved Report for Incidents. When hitting this saved report, any Incidents within it which does not have a value for the `resilient_incident_id` custom attribute will be marked for import into Resilient and after this happens, the `resilient_incident_id` custom attribute will be filled with the new Incident ID. With this in mind, Saved Reports can be used to specify which Incidents should be imported to Resilient and if desired, another Saved Report can be setup to show which Incidents have already been imported to Resilient.

To setup a basic Saved Report for the integration follow these high level steps: 
* Login to Symantec DLP and navagate to the Incidents View 
* View any existing report such as `Endpoint Incidents - All`
* Apply filtering rules as needed by your Org
* Include an additional filter to be done on the `resilient_incident_id` where the value `Is Unassigned`
* Click `Save As` and name your new report 
* With the saved report active, note the `reportID` value in the URL. This will be the saved Report ID needed. 

---


## Support
| Name | Version | Author | Support URL |
| ---- | ------- | ------ | ----------- |
| fn_symantec_dlp | 1.0.0 | IBM Resilient | https://github.com/ibmresilient/resilient-community-apps |