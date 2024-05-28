# PagerDuty

## Table of Contents
- [Release Notes](#release-notes)
- [Overview](#overview)
  - [Key Features](#key-features)
- [Requirements](#requirements)
  - [SOAR platform](#soar-platform)
  - [Cloud Pak for Security](#cloud-pak-for-security)
  - [Proxy Server](#proxy-server)
  - [Python Environment](#python-environment)
  - [Endpoint Developed With](#endpoint-developed-with)
- [Installation](#installation)
  - [Install](#install)
  - [App Configuration](#app-configuration)
- [Function - PagerDuty Create Incident](#function---pagerduty-create-incident)
- [Function - PagerDuty Create Note](#function---pagerduty-create-note)
- [Function - PagerDuty Transition Incident](#function---pagerduty-transition-incident)
- [Function - PagerDuty Create Service](#function---pagerduty-create-services)
- [Function - PagerDuty List Services](#function---pagerduty-list-incidents)
- [Function - PagerDuty List Incidents](#function---pagerduty-create-service)
- [Custom Fields](#custom-fields)
- [Poller Templates](#poller-templates)
- [Playbooks](#Playbooks)
- [Troubleshooting & Support](#troubleshooting--support)
---

## Release Notes
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.0.0 | 09/2018 | Initial Release |
| 1.0.1 | 05/2020 | Support added for App Host |
| 1.0.2 | 07/2022 | Updated documentation to new format |
| 1.1.0 | 10/2023 | Add Playbooks and implement Create Service, List Services, and List Incidents functions |
| 1.2.0 | 04/2024 | Add support for authentication with API key. Add poller for bi-directional sync between SOAR and PagerDuty incidents. |
---
### PagerDuty App  1.1.0 Changes
In v1.1.0, the existing rules and workflows have been replaced with playbooks. This change is made to support the ongoing, newer capabilities of playbooks. Each playbook has the same functionality as the previous, corresponding rule/workflow.

If upgrading from a previous release, you'll noticed that the previous release's rules/workflows remain in place. Both sets of rules and playbooks are active. For manual actions, playbooks will have the same name as it's corresponding rule, but with "(PB)" added at the end. For automatic actions, the playbooks will be disabled by default.

You can continue to use the rules/workflows. But migrating to playbooks will provide greater functionality along with future app enhancements and bug fixes.

Add Create Service, List Services and List Incidents functions.

## Overview

**SOAR Components for 'fn_pagerduty'**

SOAR Components for 'fn_pagerduty'. Used to create PagerDuty incidents, create notes and transition incidents (acknowledged and resolved)

### Key Features
This SOAR Functions package provides integration with PagerDuty for:
* Incident Creation
* Incident Transitions
* Note Creation
* Bi-directional sync

---

## Requirements

This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, App Host and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `50.0.0`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `50.0.0`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient_circuits>=50.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions:
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read |
  | Function | Read |
  | Incident | Create, Read, Edit |
  | Layout | Read, Edit |

The following SOAR platform guides provide additional information:
* _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _Integration Server Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _System Administrator Guide_: provides the procedure to install, configure and deploy apps.

The above guides are available on the IBM Documentation website at [ibm.biz/soar-docs](https://ibm.biz/soar-docs). On this web page, select your SOAR platform version. On the follow-on page, you can find the _App Host Deployment Guide_ or _Integration Server Guide_ by expanding **Apps** in the Table of Contents pane. The System Administrator Guide is available by expanding **System Administrator**.

### Cloud Pak for Security
If you are deploying to IBM Cloud Pak for Security, the requirements are:
* IBM Cloud Pak for Security >= 1.10.
* Cloud Pak is configured with an App Host.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

The following Cloud Pak guides provide additional information:
* _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. From the Table of Contents, select Case Management and Orchestration & Automation > **Orchestration and Automation Apps**.
* _System Administrator Guide_: provides information to install, configure, and deploy apps. From the IBM Cloud Pak for Security IBM Documentation table of contents, select Case Management and Orchestration & Automation > **System administrator**.

These guides are available on the IBM Documentation website at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs). From this web page, select your IBM Cloud Pak for Security version. From the version-specific IBM Documentation page, select Case Management and Orchestration & Automation.

### Proxy Server
The app does not support a proxy server.

### Python Environment
Both Python 3.6, 3.9 and 3.11 are supported

Additional package dependencies may exist for each of these packages:
* beautifulsoup4
* pdpyras
* resilient-lib
* resilient_circuits>=50.0.0


#### Prerequisites
resilient-circuits >=v50.0.0

#### Configuration
Follow the steps to add a PagerDuty section to your `app.config` file by running `resilient-circuits config [-u | -c]` and updating the fields:

```
[pagerduty]
api_token=<api_token>
# bypass https certificate validation (only set to False for testing purposes)
verifyFlag=False
resilient_client=IBM Resilient
```


## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **api_token** | Yes | `<api_token>` | API Token from PagerDuty |
| **from_email** | Yes | `some@email.com` | for some endpoints (namely creating and modifying incidents), PagerDuty requires the "email address of the user to record as having taken the action". In this app, this is passed to the package `pdpyras` as `default_from`. You can read about pdpyras [here](https://pagerduty.github.io/pdpyras/#using-a-basic-rest-api-key), and read about PagerDuty's REST API headers (of which is the from_email header) [here](https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTUw-rest-api-v2-overview)|
| **resilient_client** | Yes | `IBM SOAR` | this refers to the name identifier used for logging|
| **verifyflag** | Yes | `False` | True/False flag associated with https client certification (False means no https certification) |
| **pd_sync_notes** | No | `False` | True/False to sync notes from PagerDuty incident to SOAR incident. |
| **pd_poller_filter** | No | `"statuses": ["triggered", "acknowledged"]` | Filters to apply to the poller when getting incidents from PagerDuty. See the default app.config for more details. |
| **polling_interval** | Yes | `0` | Time in seconds to wait between polling PagerDuty. 0 will disable the poller. |
| **polling_lookback** | Yes | `60` | Time in minutes to lookback the first time the poller runs. |


---

## Function - PagerDuty Create Incident
Create a PagerDuty Incident based on a SOAR Incident

 ![screenshot: create_incident ](./doc/screenshots/create_incident.png)

  ![screenshot: create_incident_pb ](./doc/screenshots/create_incident_pb.png)


<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incidentID` | `number` | No | `-` | incident_id, typically from incident.id |
| `pd_description` | `text` | No | `-` | description from PagerDuty |
| `pd_escalation_policy` | `text` | Yes | `-` | escalation policy name from PagerDuty |
| `pd_incident_key` | `text` | No | `-` | used during acknowledge and resolve event actions |
| `pd_priority` | `text` | No | `-` | incident priority |
| `pd_service` | `text` | Yes | `-` | service name from PagerDuty |
| `pd_title` | `text` | Yes | `-` | title from PagerDuty |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "pd": {
    "incident": {
      "acknowledgements": [],
      "alert_counts": {
        "all": 0,
        "resolved": 0,
        "triggered": 0
      },
      "alert_grouping": null,
      "assigned_via": "escalation_policy",
      "assignments": [
        {
          "assignee": {
            "html_url": "https://soar-hydra.pagerduty.com/users/PMTNPRV",
            "id": "PMTNPRV",
            "self": "https://api.pagerduty.com/users/PMTNPRV",
            "summary": "Sami Amer",
            "type": "user_reference"
          },
          "at": "2022-07-15T19:47:21Z"
        }
      ],
      "basic_alert_grouping": null,
      "body": {
        "details": "https://murine1.fyre.ibm.com:443/#incidents/2100\n"
      },
      "created_at": "2022-07-15T19:47:21Z",
      "description": "Resilient: pd_test",
      "escalation_policy": {
        "html_url": "https://soar-hydra.pagerduty.com/escalation_policies/PYAMD55",
        "id": "PYAMD55",
        "self": "https://api.pagerduty.com/escalation_policies/PYAMD55",
        "summary": "Default",
        "type": "escalation_policy_reference"
      },
      "first_trigger_log_entry": {
        "html_url": "https://soar-hydra.pagerduty.com/incidents/Q1I8E2P0CJSIIB/log_entries/R5OQSQS81S9AS5KS9FLX770IG4",
        "id": "R5OQSQS81S9AS5KS9FLX770IG4",
        "self": "https://api.pagerduty.com/log_entries/R5OQSQS81S9AS5KS9FLX770IG4",
        "summary": "Triggered through the website.",
        "type": "trigger_log_entry_reference"
      },
      "html_url": "https://soar-hydra.pagerduty.com/incidents/Q1I8E2P0CJSIIB",
      "id": "Q1I8E2P0CJSIIB",
      "impacted_services": [
        {
          "html_url": "https://soar-hydra.pagerduty.com/service-directory/PFA4BVU",
          "id": "PFA4BVU",
          "self": "https://api.pagerduty.com/services/PFA4BVU",
          "summary": "API Service",
          "type": "service_reference"
        }
      ],
      "incident_key": "RES-2100",
      "incident_number": 8,
      "incidents_responders": [],
      "is_mergeable": true,
      "last_status_change_at": "2022-07-15T19:47:21Z",
      "last_status_change_by": {
        "html_url": "https://soar-hydra.pagerduty.com/service-directory/PFA4BVU",
        "id": "PFA4BVU",
        "self": "https://api.pagerduty.com/services/PFA4BVU",
        "summary": "API Service",
        "type": "service_reference"
      },
      "pending_actions": [],
      "responder_requests": [],
      "self": "https://api.pagerduty.com/incidents/Q1I8E2P0CJSIIB",
      "service": {
        "html_url": "https://soar-hydra.pagerduty.com/service-directory/PFA4BVU",
        "id": "PFA4BVU",
        "self": "https://api.pagerduty.com/services/PFA4BVU",
        "summary": "API Service",
        "type": "service_reference"
      },
      "status": "triggered",
      "subscriber_requests": [],
      "summary": "[#8] Resilient: pd_test",
      "teams": [],
      "title": "Resilient: pd_test",
      "type": "incident",
      "urgency": "high"
    }
  }
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
inputs.incidentID = incident.id
inputs.pd_title = "SOAR: {}".format(incident.name)
inputs.pd_incident_key = 'RES-'+str(incident.id)

priority = { 'Low': 'p3', 'Medium': 'p2', 'High': 'p1' }
if incident.severity_code in priority:
  inputs.pd_priority = priority.get(incident.severity_code)
else:
  inputs.pd_priority = 'p4' # lowest

if not incident.description is None:
  inputs.pd_description = incident.description.content

```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
incident.properties.pd_incident_id  = results.pd['incident']['id']
incident.properties.pd_incident_url = "<a href='{}' target='blank'>Link</a>".format(results.pd['incident']['html_url'])
```

</p>
</details>

---
## Function - PagerDuty Create Note
Create a PagerDuty Note based on a SOAR Incident's Note
 ![screenshot: create_pagerduty_note ](./doc/screenshots/create_pagerduty_note.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `pd_description` | `text` | No | `-` | description from PagerDuty |
| `pd_incident_id` | `text` | Yes | `-` | id of incident |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "note": {
    "channel": {
      "summary": "The PagerDuty website or APIs"
    },
    "content": "Test Note",
    "created_at": "2022-07-15T15:48:12-04:00",
    "id": "PNL36C8",
    "user": {
      "html_url": "https://soar-hydra.pagerduty.com/users/PMTNPRV",
      "id": "PMTNPRV",
      "self": "https://api.pagerduty.com/users/PMTNPRV",
      "summary": "Sami Amer",
      "type": "user_reference"
    }
  }
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
inputs.pd_incident_id = incident.properties.pd_incident_id
inputs.pd_description = note.text.content
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
None
```

</p>
</details>

---
## Function - PagerDuty Transition Incident
Transition a PagerDuty Incident based on changes to a SOAR Incident (such as Closing the Incident)

 ![screenshot: resolve_pagerduty_incident.png ](./doc/screenshots/resolve_pagerduty_incident.png)

  ![screenshot: update_pagerduty_incident_severity.png ](./doc/screenshots/update_pagerduty_incident_severity.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `pd_description` | `text` | No | `-` | description from PagerDuty |
| `pd_incident_id` | `text` | Yes | `-` | id of incident |
| `pd_priority` | `text` | No | `-` | incident priority |
| `pd_status` | `text` | No | `-` | status of PagerDuty incident |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "incident": {
    "acknowledgements": [],
    "alert_counts": {
      "all": 0,
      "resolved": 0,
      "triggered": 0
    },
    "alert_grouping": null,
    "assigned_via": "escalation_policy",
    "assignments": [],
    "basic_alert_grouping": null,
    "created_at": "2022-07-15T19:47:21Z",
    "description": "Resilient: pd_test",
    "escalation_policy": {
      "html_url": "https://soar-hydra.pagerduty.com/escalation_policies/PYAMD55",
      "id": "PYAMD55",
      "self": "https://api.pagerduty.com/escalation_policies/PYAMD55",
      "summary": "Default",
      "type": "escalation_policy_reference"
    },
    "first_trigger_log_entry": {
      "html_url": "https://soar-hydra.pagerduty.com/incidents/Q1I8E2P0CJSIIB/log_entries/R5OQSQS81S9AS5KS9FLX770IG4",
      "id": "R5OQSQS81S9AS5KS9FLX770IG4",
      "self": "https://api.pagerduty.com/log_entries/R5OQSQS81S9AS5KS9FLX770IG4",
      "summary": "Triggered through the website.",
      "type": "trigger_log_entry_reference"
    },
    "html_url": "https://soar-hydra.pagerduty.com/incidents/Q1I8E2P0CJSIIB",
    "id": "Q1I8E2P0CJSIIB",
    "impacted_services": [
      {
        "html_url": "https://soar-hydra.pagerduty.com/service-directory/PFA4BVU",
        "id": "PFA4BVU",
        "self": "https://api.pagerduty.com/services/PFA4BVU",
        "summary": "API Service",
        "type": "service_reference"
      }
    ],
    "incident_key": "RES-2100",
    "incident_number": 8,
    "incidents_responders": [],
    "is_mergeable": true,
    "last_status_change_at": "2022-07-15T19:55:22Z",
    "last_status_change_by": {
      "html_url": "https://soar-hydra.pagerduty.com/users/PMTNPRV",
      "id": "PMTNPRV",
      "self": "https://api.pagerduty.com/users/PMTNPRV",
      "summary": "Sami Amer",
      "type": "user_reference"
    },
    "pending_actions": [],
    "resolve_reason": null,
    "responder_requests": [],
    "self": "https://api.pagerduty.com/incidents/Q1I8E2P0CJSIIB",
    "service": {
      "html_url": "https://soar-hydra.pagerduty.com/service-directory/PFA4BVU",
      "id": "PFA4BVU",
      "self": "https://api.pagerduty.com/services/PFA4BVU",
      "summary": "API Service",
      "type": "service_reference"
    },
    "status": "resolved",
    "subscriber_requests": [],
    "summary": "[#8] Resilient: pd_test",
    "teams": [],
    "title": "Resilient: pd_test",
    "type": "incident",
    "urgency": "high"
  }
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
inputs.pd_incident_id = incident.properties.pd_incident_id
if incident.resolution_id:
  inputs.pd_status = 'resolved'
  inputs.pd_description = incident.resolution_summary.content
#else:
#  inputs.pd_status = 'acknowledged'

priority = { 'Low': 'p3', 'Medium': 'p2', 'High': 'p1' }
if incident.severity_code in priority:
  inputs.pd_priority = priority.get(incident.severity_code)
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
None
```

</p>
</details>

---
## Function - PagerDuty Create Service
Create a PagerDuty Service

 ![screenshot: resolve_pagerduty_incident.png ](./doc/screenshots/create_sevice.png)

<details><summary>Inputs:</summary>
<p>

```python
if not playbook.inputs.pd_escalation_policy:
  inputs.pd_escalation_policy = "default"

if playbook.inputs.pd_description:
  inputs.pd_description = playbook.inputs.pd_description

inputs.pd_title = playbook.inputs.pd_title
```
</details>

<details><summary>Outputs:</summary>
<p>
`create_service`
</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>
None
</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
results = playbook.functions.results.create_service

if results.pd['service']:
  incident.addNote("Service Created:<a href='{}' target='blank'>{}</a> " .format(results.pd['service']['html_url'], results.pd['service']['name']))
elif results.pd['error']:
  incident.addNote("Create Service Failed : {}" .format(results.pd['error']['errors']))
else:
  incident.addNote("Create Service Failed")
```

</p>
</details>

---
## Function - PagerDuty List Incidents
List all incidents on PagerDuty

 ![screenshot: list_incidents.png ](./doc/screenshots/list_incidents.png)


<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `pd_search_date` | `text` | No | `-` | description from PagerDuty |


</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
{
  "incidents": [
    {
      "incident_number": 1,
      "title": "TestService",
      "description": "TestService",
      "created_at": "2023-08-24T06:53:30Z",
      "updated_at": "2023-08-24T07:32:29Z",
      "status": "acknowledged",
      "incident_key": "e9120574be8c45e1a92d1a0d34199b56",
      "service": {
        "id": "P94IRVL",
        "type": "service_reference",
        "summary": "dummyTestService",
        "self": "https://api.pagerduty.com/services/P94IRVL",
        "html_url": "https://dev-resilient.pagerduty.com/service-directory/P94IRVL"
      },
      "assignments": [
        {
          "at": "2023-08-24T06:53:30Z",
          "assignee": {
            "id": "P7V7SAJ",
            "type": "user_reference",
            "summary": "dummy Lee",
            "self": "https://api.pagerduty.com/users/P7V7SAJ",
            "html_url": "https://dev-resilient.pagerduty.com/users/P7V7SAJ"
          }
        }
      ],
      "assigned_via": "escalation_policy",
      "last_status_change_at": "2023-08-24T07:32:28Z",
      "resolved_at": null,
      "first_trigger_log_entry": {
        "id": "R2RPSI1N0M3C53904CK0QKVA18",
        "type": "trigger_log_entry_reference",
        "summary": "Triggered through the website.",
        "self": "https://api.pagerduty.com/log_entries/R2RPSI1N0M3C53904CK0QKVA18",
        "html_url": "https://dev-resilient.pagerduty.com/incidents/Q0JC5FKZB7QKWA/log_entries/R2RPSI1N0M3C53904CK0QKVA18"
      },
      "alert_counts": {
        "all": 0,
        "triggered": 0,
        "resolved": 0
      },
      "is_mergeable": true,
      "escalation_policy": {
        "id": "PMV0LFG",
        "type": "escalation_policy_reference",
        "summary": "dummyTestService-ep",
        "self": "https://api.pagerduty.com/escalation_policies/PMV0LFG",
        "html_url": "https://dev-resilient.pagerduty.com/escalation_policies/PMV0LFG"
      },
      "teams": [],
      "pending_actions": [],
      "acknowledgements": [
        {
          "at": "2023-08-24T07:32:28Z",
          "acknowledger": {
            "id": "P7V7SAJ",
            "type": "user_reference",
            "summary": "dummy Lee",
            "self": "https://api.pagerduty.com/users/P7V7SAJ",
            "html_url": "https://dev-resilient.pagerduty.com/users/P7V7SAJ"
          }
        }
      ],
      "basic_alert_grouping": null,
      "alert_grouping": null,
      "last_status_change_by": {
        "id": "P7V7SAJ",
        "type": "user_reference",
        "summary": "dummy Lee",
        "self": "https://api.pagerduty.com/users/P7V7SAJ",
        "html_url": "https://dev-resilient.pagerduty.com/users/P7V7SAJ"
      },
      "priority": null,
      "incidents_responders": [],
      "responder_requests": [],
      "subscriber_requests": [],
      "urgency": "high",
      "id": "Q0JC5FKZB7QKWA",
      "type": "incident",
      "summary": "[#1] TestService",
      "self": "https://api.pagerduty.com/incidents/Q0JC5FKZB7QKWA",
      "html_url": "https://dev-resilient.pagerduty.com/incidents/Q0JC5FKZB7QKWA"
    }
  ],
  "limit": 25,
  "offset": 0,
  "total": null,
  "more": false
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
None
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
import json

results = playbook.functions.results.list_incidents

if results['incidents']:
  incident.addNote(json.dumps(results, indent=2))
else:
  incident.addNote("Get Incidents Failed (No Incidents returned)")
```

</p>
</details>

---
## Function - PagerDuty List Services
List all services on PagerDuty

 ![screenshot: list_services.png ](./doc/screenshots/list_services.png)

<details><summary>Inputs:</summary>
<p>

```python
None
```

</p>
</details>

<details><summary>Outputs:</summary>
<p>


```python
{
  "services": [
    {
      "id": "P94IRVL",
      "name": "dummyTestService",
      "description": null,
      "created_at": "2023-08-24T14:52:50+08:00",
      "updated_at": "2023-08-24T14:52:50+08:00",
      "status": "critical",
      "teams": [],
      "alert_creation": "create_alerts_and_incidents",
      "addons": [],
      "scheduled_actions": [],
      "support_hours": null,
      "last_incident_timestamp": "2023-09-11T11:31:14Z",
      "escalation_policy": {
        "id": "PMV0LFG",
        "type": "escalation_policy_reference",
        "summary": "dummyTestService-ep",
        "self": "https://api.pagerduty.com/escalation_policies/PMV0LFG",
        "html_url": "https://dev-resilient.pagerduty.com/escalation_policies/PMV0LFG"
      },
      "incident_urgency_rule": {
        "type": "constant",
        "urgency": "high"
      },
      "acknowledgement_timeout": null,
      "auto_resolve_timeout": null,
      "alert_grouping": "intelligent",
      "alert_grouping_timeout": null,
      "alert_grouping_parameters": {
        "type": "intelligent",
        "config": {
          "time_window": 300,
          "recommended_time_window": 300
        }
      },
      "integrations": [
        {
          "id": "P4WG9MK",
          "type": "generic_email_inbound_integration_reference",
          "summary": "Email",
          "self": "https://api.pagerduty.com/services/P94IRVL/integrations/P4WG9MK",
          "html_url": "https://dev-resilient.pagerduty.com/services/P94IRVL/integrations/P4WG9MK"
        },
        {
          "id": "P0KV9NX",
          "type": "events_api_v2_inbound_integration_reference",
          "summary": "Events API V2",
          "self": "https://api.pagerduty.com/services/P94IRVL/integrations/P0KV9NX",
          "html_url": "https://dev-resilient.pagerduty.com/services/P94IRVL/integrations/P0KV9NX"
        },
        {
          "id": "PJGE9XE",
          "type": "generic_events_api_inbound_integration_reference",
          "summary": "Prometheus",
          "self": "https://api.pagerduty.com/services/P94IRVL/integrations/PJGE9XE",
          "html_url": "https://dev-resilient.pagerduty.com/services/P94IRVL/integrations/PJGE9XE"
        },
        {
          "id": "PG7T8IR",
          "type": "event_transformer_api_inbound_integration_reference",
          "summary": "Amazon CloudWatch",
          "self": "https://api.pagerduty.com/services/P94IRVL/integrations/PG7T8IR",
          "html_url": "https://dev-resilient.pagerduty.com/services/P94IRVL/integrations/PG7T8IR"
        },
        {
          "id": "PCY5861",
          "type": "event_transformer_api_inbound_integration_reference",
          "summary": "Splunk",
          "self": "https://api.pagerduty.com/services/P94IRVL/integrations/PCY5861",
          "html_url": "https://dev-resilient.pagerduty.com/services/P94IRVL/integrations/PCY5861"
        },
        {
          "id": "PYLH7TB",
          "type": "nagios_inbound_integration_reference",
          "summary": "Nagios",
          "self": "https://api.pagerduty.com/services/P94IRVL/integrations/PYLH7TB",
          "html_url": "https://dev-resilient.pagerduty.com/services/P94IRVL/integrations/PYLH7TB"
        },
        {
          "id": "PVPW6EO",
          "type": "generic_events_api_inbound_integration_reference",
          "summary": "Zabbix",
          "self": "https://api.pagerduty.com/services/P94IRVL/integrations/PVPW6EO",
          "html_url": "https://dev-resilient.pagerduty.com/services/P94IRVL/integrations/PVPW6EO"
        },
        {
          "id": "PRD861L",
          "type": "generic_events_api_inbound_integration_reference",
          "summary": "Datadog",
          "self": "https://api.pagerduty.com/services/P94IRVL/integrations/PRD861L",
          "html_url": "https://dev-resilient.pagerduty.com/services/P94IRVL/integrations/PRD861L"
        },
        {
          "id": "PO3K5PY",
          "type": "events_api_v2_inbound_integration_reference",
          "summary": "SolarWinds Orion",
          "self": "https://api.pagerduty.com/services/P94IRVL/integrations/PO3K5PY",
          "html_url": "https://dev-resilient.pagerduty.com/services/P94IRVL/integrations/PO3K5PY"
        },
        {
          "id": "P7UZ4A8",
          "type": "generic_events_api_inbound_integration_reference",
          "summary": "New Relic",
          "self": "https://api.pagerduty.com/services/P94IRVL/integrations/P7UZ4A8",
          "html_url": "https://dev-resilient.pagerduty.com/services/P94IRVL/integrations/P7UZ4A8"
        }
      ],
      "response_play": null,
      "type": "service",
      "summary": "dummyTestService",
      "self": "https://api.pagerduty.com/services/P94IRVL",
      "html_url": "https://dev-resilient.pagerduty.com/service-directory/P94IRVL"
    },
    {
      "id": "P8WS4HA",
      "name": "dummyTestService2",
      "description": null,
      "created_at": "2023-09-08T22:47:55+08:00",
      "updated_at": "2023-09-08T22:47:55+08:00",
      "status": "active",
      "teams": [],
      "alert_creation": "create_incidents",
      "addons": [],
      "scheduled_actions": [],
      "support_hours": null,
      "last_incident_timestamp": null,
      "escalation_policy": {
        "id": "P8021BT",
        "type": "escalation_policy_reference",
        "summary": "Default",
        "self": "https://api.pagerduty.com/escalation_policies/P8021BT",
        "html_url": "https://dev-resilient.pagerduty.com/escalation_policies/P8021BT"
      },
      "incident_urgency_rule": {
        "type": "constant",
        "urgency": "high"
      },
      "acknowledgement_timeout": null,
      "auto_resolve_timeout": null,
      "alert_grouping": null,
      "alert_grouping_timeout": null,
      "alert_grouping_parameters": {
        "type": null,
        "config": null
      },
      "integrations": [],
      "response_play": null,
      "type": "service",
      "summary": "dummyTestService2",
      "self": "https://api.pagerduty.com/services/P8WS4HA",
      "html_url": "https://dev-resilient.pagerduty.com/service-directory/P8WS4HA"
    },
    {
      "id": "PK723D4",
      "name": "dummyTestService3",
      "description": "TestDes",
      "created_at": "2023-09-08T22:48:49+08:00",
      "updated_at": "2023-09-08T22:48:49+08:00",
      "status": "active",
      "teams": [],
      "alert_creation": "create_incidents",
      "addons": [],
      "scheduled_actions": [],
      "support_hours": null,
      "last_incident_timestamp": null,
      "escalation_policy": {
        "id": "P8021BT",
        "type": "escalation_policy_reference",
        "summary": "Default",
        "self": "https://api.pagerduty.com/escalation_policies/P8021BT",
        "html_url": "https://dev-resilient.pagerduty.com/escalation_policies/P8021BT"
      },
      "incident_urgency_rule": {
        "type": "constant",
        "urgency": "high"
      },
      "acknowledgement_timeout": null,
      "auto_resolve_timeout": null,
      "alert_grouping": null,
      "alert_grouping_timeout": null,
      "alert_grouping_parameters": {
        "type": null,
        "config": null
      },
      "integrations": [],
      "response_play": null,
      "type": "service",
      "summary": "dummyTestService3",
      "self": "https://api.pagerduty.com/services/PK723D4",
      "html_url": "https://dev-resilient.pagerduty.com/service-directory/PK723D4"
    },
    {
      "id": "PQNVIL9",
      "name": "My Web App",
      "description": "My cool web application that does things.",
      "created_at": "2023-09-05T15:44:12+08:00",
      "updated_at": "2023-09-05T15:44:12+08:00",
      "status": "active",
      "teams": [],
      "alert_creation": "create_alerts_and_incidents",
      "addons": [],
      "scheduled_actions": [
        {
          "type": "urgency_change",
          "at": {
            "type": "named_time",
            "name": "support_hours_start"
          },
          "to_urgency": "high"
        }
      ],
      "support_hours": {
        "type": "fixed_time_per_day",
        "time_zone": "America/Lima",
        "days_of_week": [
          1,
          2,
          3,
          4,
          5
        ],
        "start_time": "09:00:00",
        "end_time": "17:00:00"
      },
      "last_incident_timestamp": null,
      "escalation_policy": {
        "id": "P8021BT",
        "type": "escalation_policy_reference",
        "summary": "Default",
        "self": "https://api.pagerduty.com/escalation_policies/P8021BT",
        "html_url": "https://dev-resilient.pagerduty.com/escalation_policies/P8021BT"
      },
      "incident_urgency_rule": {
        "type": "use_support_hours",
        "during_support_hours": {
          "type": "constant",
          "urgency": "high"
        },
        "outside_support_hours": {
          "type": "constant",
          "urgency": "low"
        }
      },
      "acknowledgement_timeout": 600,
      "auto_resolve_timeout": 14400,
      "alert_grouping": "time",
      "alert_grouping_timeout": 2,
      "alert_grouping_parameters": {
        "type": "time",
        "config": {
          "timeout": 2
        }
      },
      "integrations": [],
      "response_play": null,
      "type": "service",
      "summary": "My Web App",
      "self": "https://api.pagerduty.com/services/PQNVIL9",
      "html_url": "https://dev-resilient.pagerduty.com/service-directory/PQNVIL9"
    }
  ],
  "limit": 25,
  "offset": 0,
  "total": null,
  "more": false
}

```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
None
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
import json

results = playbook.functions.results.list_incidents

if results['incidents']:
  incident.addNote(json.dumps(results, indent=2))
else:
  incident.addNote("Get Incidents Failed (No Incidents returned)")
```

</p>
</details>

---

## Poller Templates
It may be necessary to modify the templates used to create, update, or close SOAR cases based on your required custom fields in SOAR.

This is especially relevant if you have required custom _close_ fields that need to be filled when closing a case in SOAR. If that is the case, be sure to implement a custom `close_case` and reference those required close fields in the template.

When overriding the template in App Host, specify the file path for each file as `/var/rescircuits`.

Below are the default templates used which can be copied, modified, and used with app_config's
`soar_create_case`, `soar_update_case`, and `soar_close_case` settings to override the default templates.

<details><summary>soar_create_case.jinja</summary>

```jinja
{
  {# JINJA template for creating a new SOAR incident from a PagerDuty incident #}
  "name": "{{ title }}",
  "description": "{{ summary | replace('"', '\\"') }}",
  {# start_date cannot be after discovered_date #}
  "discovered_date": {{ created_at | soar_datetimeformat(date_format="%Y-%m-%dT%H:%M:%SZ") }},
  "start_date": {{ created_at | soar_datetimeformat(date_format="%Y-%m-%dT%H:%M:%SZ") }},
  {# if alert users are different than SOAR users, consider using a mapping table using soar_substitute: #}
  {# "owner_id": "{{ **assignedTo** |soar_substitute('{"Automation": "soar_user1@example.com", "default_user@example.com": "soar_user2@example.com", "DEFAULT": "default_user@example.com" }') }}", #}
  "plan_status": "A",
  "severity_code": "{{ urgency | soar_substitute('{"high": "High", "low": "Low"}') }}",
  {# specify your custom fields for your endpoint solution #}
  "properties": {
    "pd_incident_id": "{{ id }}",
    "pd_incident_url": "<a target='_blank' href='{{ html_url }}'>Link</a>",
    "pd_incident_service_name": "{{ service.summary }}",
    "pd_incident_service_id": "{{ service.id }}",
    "pd_incident_key": "{{ incident_key }}",
    "pd_incident_status": "{{ status }}",
    "pd_incident_escalation_policy_name": "{{ escalation_policy.summary }}",
    "pd_incident_escalation_policy_id": "{{ escalation_policy.id }}"
    {% if priority %}
      ,"pd_incident_priority": "{{ priority.summary }}"
    {% endif %}
  }
}
```

</details>

<details><summary>soar_close_case.jinja</summary>

```jinja
{
  {# JINJA template for closing a SOAR incident using endpoint data #}
  {# modify to specify your specific **data** fields #}
  "plan_status": "C",
  "resolution_id": "Resolved",
  "resolution_summary": {% if resolve_reason %} "Closed by PagerDuty, with resolution note {{ resolve_reason }}" {% else %} "Closed by PagerDuty" {% endif %},
  "properties": {
    "pd_incident_id": "{{ id }}",
    "pd_incident_url": "<a target='_blank' href='{{ html_url }}'>Link</a>",
    "pd_incident_service_name": "{{ service.summary }}",
    "pd_incident_service_id": "{{ service.id }}",
    "pd_incident_key": "{{ incident_key }}",
    "pd_incident_status": "{{ status }}",
    "pd_incident_escalation_policy_name": "{{ escalation_policy.summary }}",
    "pd_incident_escalation_policy_id": "{{ escalation_policy.id }}"
    {% if priority %}
      ,"pd_incident_priority": "{{ priority.summary }}"
    {% endif %}
  }
}
```

</details>

<details><summary>soar_update_case.jinja</summary>

```jinja
{
  {# JINJA template for updating a SOAR incident from a PagerDuty incident #}
  "severity_code": "{{ urgency | soar_substitute('{"high": "High", "low": "Low"}') }}",
  {# specify your custom fields for your endpoint solution #}
  "properties": {
    "pd_incident_service_name": "{{ service.summary }}",
    "pd_incident_service_id": "{{ service.id }}",
    "pd_incident_status": "{{ status }}",
    "pd_incident_escalation_policy_name": "{{ escalation_policy.summary }}",
    "pd_incident_escalation_policy_id": "{{ escalation_policy.id }}"
    {% if priority %}
      ,"pd_incident_priority": "{{ priority.summary }}"
    {% endif %}
  }
}
```

</details>

---

## Playbooks
| Playbook Name | Object | Activation type | Status |
| --------- | ------ | ------ | ------------------ |
| PagerDuty: Create Incident (PB) | incident |Manual| `enabled` |
| PagerDuty: Create PagerDuty Note (PB) | note |Automatic| `enabled` |
| PagerDuty: Resolve PagerDuty Incident (PB) | incident | Automatic |`enabled` |
| PagerDuty: Update PagerDuty Incident Severity (PB) | incident | Automatic | `enabled` |
| PagerDuty: List Incidents (PB) | incident | Manual | `enabled` |
| PagerDuty: List Services (PB) | incident | Manual | `enabled` |
| PagerDuty: Create Service (PB) | incident | Manual | `enabled` |

---


## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.

### For Support
This is a IBM Community provided App. Please search the Community [ibm.biz/soarcommunity](https://ibm.biz/soarcommunity) for assistance.
