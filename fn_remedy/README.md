<!--
  This README.md is generated by running:
  "resilient-sdk docgen -p fn_remedy"

  This file was generated with resilient-sdk v51.0.2.0.974

  It is best edited using a Text Editor with a Markdown Previewer. VS Code
  is a good example. Checkout https://guides.github.com/features/mastering-markdown/
  for tips on writing with Markdown

  All fields followed by "::CHANGE_ME::"" should be manually edited

  If you make manual edits and run docgen again, a .bak file will be created

  Store any screenshots in the "doc/screenshots" directory and reference them like:
  ![screenshot: screenshot_1](./screenshots/screenshot_1.png)

  NOTE: If your app is available in the container-format only, there is no need to mention the integration server in this readme.
-->

# Remedy


## Table of Contents
- [Release Notes](#release-notes)
- [Overview](#overview)
  - [Key Features](#key-features)
- [Requirements](#requirements)
  - [SOAR platform](#soar-platform)
  - [Cloud Pak for Security](#cloud-pak-for-security)
  - [Proxy Server](#proxy-server)
  - [Python Environment](#python-environment)
- [Installation](#installation)
  - [Install](#install)
  - [App Configuration](#app-configuration)
- [Function - Remedy: Close Incident](#function---remedy-close-incident)
- [Function - Remedy: Create Incident](#function---remedy-create-incident)
  - [Custom Layouts](#custom-layouts)
- [Data Table - Remedy Linked Incidents Reference Table](#data-table---remedy-linked-incidents-reference-table)
- [Rules](#rules)
- [Troubleshooting & Support](#troubleshooting--support)

---

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release
  notes of a previous release
-->
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.0.2 | 07/2024 | Converted to Python3 |
| 1.0.1 | 04/2022 | Bug fix for use of 'verify' app.config parameter |
| 1.0.0 | 04/2021 | Initial Release |

---

## Overview
<!--
  Provide a high-level description of the function itself and its remote software or application.
  The text below is parsed from the "description" and "long_description" attributes in the setup.py file
-->
**Remedy for IBM SOAR**

 ![screenshot: main](./doc/screenshots/main.png)

Remedy for IBM SOAR This integration provides the capability to create new incidents in Remedy from SOAR tasks via the HPD:IncidentInterface_Create form over the REST API. Once the task is complete, this integration also provides the capability to close existing Remedy Incidents.

### Key Features
<!--
  List the Key Features of the Integration
-->
* Send IBM SOAR Case tasks to Remedy as Incidents
* Close Remedy Incidents from IBM SOAR


---

## Requirements
<!--
  List any Requirements
-->
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, Edge Gateway (also known as App Host) and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `51.0.0.0.9340`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `51.0.0.0.9340`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient-circuits>=30.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions:
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read |
  | Function | Read |
  | Incidents |  Read |
  | Incident Notes | Write |
  | Private Tasks | Read |

* Resilient-circuits will also require the following permission to run the customize import process.
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Write |

The following SOAR platform guides provide additional information:
* _Edge Gateway Deployment Guide_ or _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _Integration Server Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _System Administrator Guide_: provides the procedure to install, configure and deploy apps.

The above guides are available on the IBM Documentation website at [ibm.biz/soar-docs](https://ibm.biz/soar-docs). On this web page, select your SOAR platform version. On the follow-on page, you can find the _Edge Gateway Deployment Guide_, _App Host Deployment Guide_, or _Integration Server Guide_ by expanding **Apps** in the Table of Contents pane. The System Administrator Guide is available by expanding **System Administrator**.

### Cloud Pak for Security
If you are deploying to IBM Cloud Pak for Security, the requirements are:
* IBM Cloud Pak for Security >= `1.10.15`.
* Cloud Pak is configured with an Edge Gateway.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

The following Cloud Pak guides provide additional information:
* _Edge Gateway Deployment Guide_ or _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. From the Table of Contents, select Case Management and Orchestration & Automation > **Orchestration and Automation Apps**.
* _System Administrator Guide_: provides information to install, configure, and deploy apps. From the IBM Cloud Pak for Security IBM Documentation table of contents, select Case Management and Orchestration & Automation > **System administrator**.

These guides are available on the IBM Documentation website at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs). From this web page, select your IBM Cloud Pak for Security version. From the version-specific IBM Documentation page, select Case Management and Orchestration & Automation.

### Proxy Server
The app **does** support a proxy server.

### Python Environment
Python 3.9, 3.11, and 3.12 are officially supported. When deployed as an app, the app runs on Python 3.11.
Additional package dependencies may exist for each of these packages:
* resilient-circuits>=30.0.0
* resilient-lib>=39.0.0


---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **remedy_host** | Yes | `<example.domain>` | *Hostname or IP for the Remedy instance.* |
| **remedy_user** | Yes | `<example_user>` | *Username to use to authenticate with Remedy.* |
| **remedy_password** | Yes | `xxx` | *Password to use to authenticate with Remedy.* |
| **max_datatable_rows** | No | `30` | *Max number of datatable rows to return from the SOAR API when closing an Incident.* |
| remedy_port | No | `8443` | *Port number over which the Remedy REST API is exposed.* |
| verify | No | `true|false|/path/to/certificate.crt` | *Set to `true` or `/path/to/cerficate.crt` to make verified requests to Remedy, else set to `false`* |
| https_proxy | No | `example.domain` | *https proxy for request traffic.* |



 ---

## Function - Remedy: Close Incident
Close an incident ticket in Remedy

 ![screenshot: fn-remedy-close-incident ](./doc/screenshots/fn-remedy-close-incident.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | Yes | `-` | - |
| `remedy_payload` | `text` | No | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
    # TODO: Generate an example of the Function Output within this code block.
    # To get the output of a Function:
    #   1. Run resilient-circuits in DEBUG mode: $ resilient-circuits run --loglevel=DEBUG
    #   2. Invoke the Function in SOAR
    #   3. Gather the results using: $ resilient-sdk codegen -p fn_remedy --gather-results
    #   4. Run docgen again: $ resilient-sdk docgen -p fn_remedy
    # Or simply paste example outputs manually here. Be sure to remove any personal information
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
# Python 2 compatibility for CP4S 1.6
def mk_str(value, quotes=u'"'):
    if value is None:
        return "null"
    else:
        esc_value = value.replace(u'"', u'\\"')
        if quotes:
            return u'{0}{1}{0}'.format(quotes, esc_value)
        else:
            return esc_value


inputs.task_id = task.id
inputs.incident_id = incident.id

# Use this section to add key, value pairs to send to Remedy
# These values will be added/updated on the target Remedy incident,
# so they must conform with the "HPD:IncidentInterface_Create" schema
payload = """{"Status_Reason": "foo"}"""

inputs.remedy_payload = payload if payload else ''

```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
noteText = "<h5>Remedy Close Incident:</h5>"

if results["success"]:
    if results["content"]["closed"]:
      noteText += "<p>The following incidents were matched in Remedy and successfully closed:</p>"
      for item in results["content"]["closed"]:
        noteText += "<p>    Incident Number {0}, Request ID: {1}</p>".format(item["values"]["Incident Number"], item["values"]["Request ID"])
    if results["content"]["skipped"]:
      noteText += "<p>The following incidents were not able to be closed. Common reasons include that the incident has been previously closed, " \
      "the incident has been deleted, or the payload sent to Remedy was incomplete according to the requirements of your specific system:</p>"
      for item in results["content"]["skipped"]:
        noteText += "<p>    Incident Number {0}, Request ID: {1}</p>".format(item["values"]["Incident Number"], item["values"]["Request ID"])
elif not results["content"]["closed"] and not results["content"]["skipped"]:
  # no sync to remedy, just exit
  noteText = None
else:
  noteText += "<p>Function failed to complete. Reason: {}</p>".format(results.reason)

if noteText:
  richText = helper.createRichText(noteText)
  incident.addNote(richText)

```

</p>
</details>

---
## Function - Remedy: Create Incident
Create a new incident in Remedy from a Resilient task.

 ![screenshot: fn-remedy-create-incident ](./doc/screenshots/fn-remedy-create-incident.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | Yes | `-` | - |
| `remedy_incident_name` | `text` | No | `-` | - |
| `remedy_payload` | `text` | No | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
    # TODO: Generate an example of the Function Output within this code block.
    # To get the output of a Function:
    #   1. Run resilient-circuits in DEBUG mode: $ resilient-circuits run --loglevel=DEBUG
    #   2. Invoke the Function in SOAR
    #   3. Gather the results using: $ resilient-sdk codegen -p fn_remedy --gather-results
    #   4. Run docgen again: $ resilient-sdk docgen -p fn_remedy
    # Or simply paste example outputs manually here. Be sure to remove any personal information
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
# Python 2 compatibility for CP4S 1.6
def mk_str(value, quotes=u'"'):
    if value is None:
        return "null"
    else:
        esc_value = value.replace(u'"', u'\\"')
        if quotes:
            return u'{0}{1}{0}'.format(quotes, esc_value)
        else:
            return esc_value


payload = u"""{{ "ApplyTemplate": {},
  "First_Name": {},
  "Last_Name": {},
  "Impact": {},
  "Urgency": {},
  "Service_Type": {},
  "Status": {},
  "Reported Source": {},
  "Description": {},
  "Assigned Support Organization": {},
  "additional_data": {}
}}""".format(mk_str(rule.properties.remedy_template),
  mk_str(rule.properties.remedy_first_name),
  mk_str(rule.properties.remedy_last_name),
  mk_str(rule.properties.remedy_impact),
  mk_str(rule.properties.remedy_urgency),
  mk_str(rule.properties.remedy_service_type),
  mk_str(rule.properties.remedy_status),
  mk_str(rule.properties.remedy_reported_source),
  mk_str(rule.properties.remedy_note),
  mk_str(rule.properties.remedy_support_group),
  rule.properties.remedy_additional_data.content if rule.properties.remedy_additional_data.content else "null"
)

# set inputs
inputs.task_id = task.id 
inputs.incident_id = incident.id
inputs.remedy_incident_name = task.name
inputs.remedy_payload = payload

```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
noteText = "<h5> Remedy Create Incident</h5>"

task_id = task.id
task_name = task.name

if results["success"]:
  noteText += "<p>Successfully sent task {0} \"{1}\" to Remedy as Incident Number {2} (UI name) and Request ID {3} (API name).</p>"\
  "".format(task_id, task_name, \
  results["content"]["values"]["Incident Number"], results["content"]["values"]["Request ID"])
else:
  noteText += "<p>Unable to send task {0} \"{1}\" to Remedy</p>".format(task_id, task_name)
  noteText += "<p>Ensure the activity fields and payload you provide meet the minimum requirements in your system for incident creation and routing."

richText = helper.createRichText(noteText)
incident.addNote(richText)
```

</p>
</details>

---



## Custom Layouts
<!--
  Use this section to provide guidance on where the user should add any custom fields and data tables.
  You may wish to recommend a new incident tab.
  You should save a screenshot "custom_layouts.png" in the doc/screenshots directory and reference it here
-->
* Import the Data Tables and Custom Fields like the screenshot below:

  ![screenshot: custom_layouts](./doc/screenshots/custom_layouts.png)


## Data Table - Remedy Linked Incidents Reference Table

 ![screenshot: dt-remedy-linked-incidents-reference-table](./doc/screenshots/dt-remedy-linked-incidents-reference-table.png)

#### API Name:
remedy_linked_incidents_reference_table

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Extra | `extra` | `textarea` | - |
| Remedy ID | `remedy_id` | `text` | Request ID of the Remedy form entry |
| Status | `status` | `textarea` | Last status applied to the Remedy Incident |
| Task ID | `taskincident_id` | `text` | ID of the Task and its description |
| Timestamp | `timestamp` | `datetimepicker` | - |

---



## Rules
| Rule Name | Object | Workflow Triggered | Condition |
| --------- | ------ | ------------------ | ---------- |
| Remedy Close Incident from Task | task | `close_a_remedy_incident_from_task` | `task.status changed_to Closed` |
| Remedy Create Incident from Task | task | `create_a_remedy_incident_from_task` | `task.status equals Open` |

---


## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.
 
### For Support
This is an IBM supported app. Please search [ibm.com/mysupport](https://ibm.com/mysupport) for assistance.
