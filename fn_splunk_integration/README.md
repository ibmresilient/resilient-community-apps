# Splunk Integration for SOAR

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
  - [Custom Layouts](#custom-layouts)
- [Function - Splunk Add Intel Item](#function---splunk-add-intel-item)
- [Function - Splunk Delete Threat Intel Item](#function---splunk-delete-threat-intel-item)
- [Function - Splunk Search](#function---splunk-search)
- [Function - Splunk Update Notable Event](#function---splunk-update-notable-event)
- [Data Table - Splunk Intel Results](#data-table---splunk-intel-results)
- [Rules](#rules)
- [How to configure to use a single Splunk Server](#how-to-configure-to-use-a-single-splunk-server)
- [Creating playbooks when server/servers in app.config are labeled](#creating-workflows-when-server/servers-in-app.config-are-labeled)
- [Troubleshooting & Support](#troubleshooting--support)
---

## Release Notes
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.0.0 | 06/2018 | Initial Release |
| 1.0.1 | 10/2019 | added SSL validation to the integrations server |
| 1.0.2 | 05/2020 | Support added for App Host |
| 1.0.3 | 09/2020 | Updated Example Rules and Workflows |
| 1.1.0 | 03/2022 | Allow for configuration of multiple Splunk instances |
| 1.1.1 | 04/2022 | Fix for splunk_max_count |
| 1.2.0 | 05/2022 | Add more documentation and bug fix |
| 1.3.0 | 06/222 | Add authentication using tokens |
| 1.3.1 | 11/2022 | Bug Fix |
| 1.4.0 | 10/2023 | Add Proxy support & Convert workflows/rules to playbooks |

* For customers upgrading from a previous release to 1.1.0 or greater, the app.config file must be manually edited to add new settings required to each server configuration. See [1.1.0 Changes](#1.1.0-changes)

### 1.4.0

In v1.4.0, the existing rules and workflows have been replaced with playbooks. This change is made to support the ongoing, newer capabilities of playbooks. Each playbook has the same functionality as the previous, corresponding rule/workflow.

If upgrading from a previous release, you'll notice that the previous release's rules/workflows remain in place. Both sets of rules and playbooks are active. For manual actions, playbooks have the same name as it's corresponding rule, but with "(PB)" added at the end.

You can continue to use the rules/workflows. But migrating to playbooks provides greater functionality along with future app enhancements and bug fixes.

---

## Overview

**Add, Search and Delete artifacts to Splunk ES**

 ![screenshot: main](./doc/screenshots/main.png)

Several functions to operate with Splunk ES intel collections, including updates to SplunkES notable events and add, search and delete operations to intel collections based on artifact type values.

### Key Features
* Add a new threat intelligence item to the collections of Splunk ES
* Delete a threat intelligence item
* Execute a given Splunk or Splunk ES search/query
* Update a Splunk ES notable event

---

## Requirements
- SOAR Server version 45 or later
- Splunk version 7.0 or later, or Splunk Cloud
- Splunk ES 4.7.2 or later, or Splunk ES Cloud
- Ability to connect to SOAR server with HTTPS on port 443 and 65001
- Ability to connect to Splunk server with HTTPS on port 8089
- In the app.config either username & password OR token are required
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, App Host and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `45.0.0`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `45.0.0`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient_circuits>=45.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions:
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read, Edit |
  | Function | Read |
  | Action Invocations | Read |

The following SOAR platform guides provide additional information:
* _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _Integration Server Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _System Administrator Guide_: provides the procedure to install, configure and deploy apps.

The above guides are available on the IBM Documentation website at [ibm.biz/soar-docs](https://ibm.biz/soar-docs). On this web page, select your SOAR platform version. On the follow-on page, you can find the _App Host Deployment Guide_ or _Integration Server Guide_ by expanding **Apps** in the Table of Contents pane. The System Administrator Guide is available by expanding **System Administrator**.

### Cloud Pak for Security
If you are deploying to IBM Cloud Pak for Security, the requirements are:
* IBM Cloud Pak for Security >= 1.4.
* Cloud Pak is configured with an App Host.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

The following Cloud Pak guides provide additional information:
* _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. From the Table of Contents, select Case Management and Orchestration & Automation > **Orchestration and Automation Apps**.
* _System Administrator Guide_: provides information to install, configure, and deploy apps. From the IBM Cloud Pak for Security IBM Documentation table of contents, select Case Management and Orchestration & Automation > **System administrator**.

These guides are available on the IBM Documentation website at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs). From this web page, select your IBM Cloud Pak for Security version. From the version-specific IBM Documentation page, select Case Management and Orchestration & Automation.

### Proxy Server
The app does support a proxy server.

### Python Environment
Python 3.6 and above are supported.
Additional package dependencies may exist for each of these packages:
* resilient_circuits>=45.0.0
* resilient_lib

---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure. 

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **host** | Yes | `localhost` | Splunk host |
| **port** | Yes | `8089` | Splunk port for restapi |
| **splunkpassword** | No | `changeme` | Splunk password |
| **username** | No | `admin` | Splunk login username |
| **token** | No | `` | Splunk authentication token |
| **verify_cert** | Yes | `false|/path/to/cert` | Verify https certificate or not |

#### 1.1.0 Changes
Starting in version 1.1.0, more than one Splunk instance can be configured for SOAR case data synchronization. For enterprises with only one Splunk instance, your app.config file will continue to define the Splunk instance under the `[fn_splunk_integration]` section header.

For enterprises with more than one Splunk instance, each instance will have it's own section header, such as `[fn_splunk_integration:splunk_instance_label]` where `splunk_instance_label` represents any label helpful to define your Splunk environment.

Be aware that modifications to the workflows will be needed to correctly pass this label through the `splunk_label` function input field if the Splunk server/servers in the app.config have labels.

If you have existing custom workflows, see [Creating workflows when server/servers in app.config are labeled](#creating-workflows-when-serverservers-in-appconfig-are-labeled) for more information about changing them to reference the `splunk_label` function input field.

### Custom Layouts

* Import the Data Tables and Custom Fields like the screenshot below:

  ![screenshot: custom_layouts](./doc/screenshots/custom_layout.png)


---

## Function - Splunk Add Intel Item
Add a new Splunk ES threat intelligence item to a given collection. splunk_threat_intel_type is one of the 9 collections, including ip_intel, file_intel.... splunk_query_param1 to splunk_query_param10 are used to build a dict {splunk_query_param1:splunk_query_parame2, splunk_query_param3:splunk_query_param4....} This dict is used to create the new threat intel item.

 ![screenshot: fn-splunk-add-intel-item ](./doc/screenshots/fn-splunk-add-intel-item.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `splunk_label` | `text` | No | `-` | Label given to each splunk server in the app.config |
| `splunk_query_param1` | `text` | No | `-` | - |
| `splunk_query_param10` | `text` | No | `-` | - |
| `splunk_query_param2` | `text` | No | `-` | - |
| `splunk_query_param3` | `text` | No | `-` | - |
| `splunk_query_param4` | `text` | No | `-` | - |
| `splunk_query_param5` | `text` | No | `-` | - |
| `splunk_query_param6` | `text` | No | `-` | - |
| `splunk_query_param7` | `text` | No | `-` | - |
| `splunk_query_param8` | `text` | No | `-` | - |
| `splunk_query_param9` | `text` | No | `-` | - |
| `splunk_threat_intel_type` | `text` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "version": 2.0,
  "success": true,
  "reason": null,
  "content": {
    "message": "Create operation successful.",
    "status": true
  },
  "raw": null,
  "inputs": {
    "splunk_query_param1": "ip",
    "splunk_threat_intel_type": "ip_intel",
    "splunk_label": null,
    "splunk_query_param2": "1.1.1.1"
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-splunk-integration",
    "package_version": "1.4.0",
    "host": "local",
    "execution_time_ms": 1115,
    "timestamp": "2023-08-29 09:40:23"
  }
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
lookup_map = {
  "DNS Name": ("ip_intel", "domain"),
  "Email Attachment": None,
  "Email Attachment Name": ("file_intel", "file_name"),
  "Email Body": None,
  "Email Recipient": None,
  "Email Sender": ("email_intel", "src_user"),
  "Email Sender Name": ("email_intel", "src_user"),
  "Email Subject": ("email_intel", "subject"),
  "File Name": ("file_intel", "file_name"),
  "File Path": None,
  "HTTP Request Header": None,
  "HTTP Response Header": None,
  "IP Address": ("ip_intel", "ip"),
  "Log File": None,
  "MAC Address": None,
  "Malware Family/Variant": None,
  "Malware MD5 Hash": ("file_intel", "file_hash"),
  "Malware Sample": None,
  "Malware Sample Fuzzy Hash": ("file_intel", "file_hash"),
  "Malware SHA-1 Hash": ("file_intel", "file_hash"),
  "Malware SHA-256 Hash": ("file_intel", "file_hash"),
  "Mutex": None,
  "Network CIDR Range": None,
  "Other File": None,
  "Password": None,
  "Port": None,
  "Process Name": ("process_intel", "process"),
  "Registry Key": ("registry_intel", "registry_value_name"),
  "RFC 822 Email Message File": None,
  "Service": ("service_intel", "service"),
  "String": None,
  "System Name": ("service_intel", "service"),
  "URI Path": None,
  "URL": ("http_intel", "url"),
  "URL Referer": ("http_intel", "http_referrer"),
  "User Account": None,
  "User Agent": ("http_intel", "http_user_agent")
}

if artifact.type in lookup_map and lookup_map[artifact.type]:
  threat_type, threat_field_name = lookup_map[artifact.type]
  inputs.splunk_threat_intel_type = threat_type
  inputs.splunk_query_param1 = threat_field_name
  inputs.splunk_query_param2 = artifact.value
  inputs.splunk_label = getattr(playbook.inputs, "splunk_server")
else:
  helper.fail(f"Artifact type not supported: {artifact.type}")
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.add_intel_item
now = int(datetime.now().timestamp()*1000)
results_content = results.get("content", {})

result_note = u"""<b>Artifact</b>: {}<br><br>
<b>Splunk Add Status</b>: {}<br>
<b>Message</b>: {}""".format(artifact.value,
                             "Successful" if results_content.get("status", False) else "Unsuccessful",
                             results_content.get("message", "None"))

if results_content.get("status", False):
  incident.addNote(helper.createRichText(result_note))
  result_row = incident.addRow("splunk_intel_results")
  result_row.create_date = now
  result_row.status = "Added"
  result_row.intel_collection = results.inputs['splunk_threat_intel_type']
  result_row.intel_field = results.inputs['splunk_query_param1']
  result_row.intel_value = results.inputs['splunk_query_param2']
  result_row.splunk_server = getattr(playbook.inputs, "splunk_server")
```

</p>
</details>

---
## Function - Splunk Delete Threat Intel Item
Delete a threat intelligence item from a given collection. splunk_threat_intel_type is one of 9 collections, including ip_intel, file_intel... splunk_threat_intel_key is the _key of the item to be deleted.

 ![screenshot: fn-splunk-delete-threat-intel-item ](./doc/screenshots/fn-splunk-delete-threat-intel-item.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `splunk_label` | `text` | No | `-` | Label given to each splunk server in the app.config |
| `splunk_threat_intel_key` | `text` | No | `-` | The _key from Splunk ES for this threat_intel item |
| `splunk_threat_intel_type` | `text` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "version": 2.0,
  "success": true,
  "reason": null,
  "content": {
    "message": "Delete operation successful.",
    "status": true
  },
  "raw": null,
  "inputs": {
    "splunk_threat_intel_key": "dc3c8a0ce1f2464897d8c1995d66e1e4",
    "splunk_threat_intel_type": "ip_intel",
    "splunk_label": null
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-splunk-integration",
    "package_version": "1.4.0",
    "host": "local",
    "execution_time_ms": 875,
    "timestamp": "2023-08-29 09:50:50"
  }
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
inputs.splunk_threat_intel_type = row.intel_collection
inputs.splunk_threat_intel_key = row.intel_key
inputs.splunk_label = row.splunk_server
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
results = playbook.functions.results.delete_intel_item
results_content = results.get("content", {})

result_note = u"""<b>Artifact</b>: {}<br><br>
<b>Splunk Delete Status</b>: {}<br>
<b>Message</b>: {}""".format(row.intel_value,
                             "Successful" if results_content.get("status", False) else "Unsuccessful",
                             results_content.get("message", "None"))

incident.addNote(helper.createRichText(result_note))
if results_content.get("status"):
  row.status = "Deleted"
```

</p>
</details>

---
## Function - Splunk Search
Define a Splunk query string with parameters. Map parameters from inputs, and perform the query. For example, %param1% in the query string will be replaced by the value of splunk_query_param1. The return is a list.

 ![screenshot: fn-splunk-search ](./doc/screenshots/fn-splunk-search.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `splunk_label` | `text` | No | `-` | Label given to each splunk server in the app.config |
| `splunk_max_return` | `number` | No | `-` | Max number of events to return (if empty, up to 100 are returned) |
| `splunk_query` | `textarea` | No | `-` | - |
| `splunk_query_param1` | `text` | No | `-` | - |
| `splunk_query_param2` | `text` | No | `-` | - |
| `splunk_query_param3` | `text` | No | `-` | - |
| `splunk_query_param4` | `text` | No | `-` | - |
| `splunk_query_param5` | `text` | No | `-` | - |
| `splunk_search_time_to_wait` | `number` | No | `2` | Time in seconds to wait before checking if the search has completed |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "version": 2.0,
  "success": true,
  "reason": null,
  "content": [
    {
      "_key": "dc3c8a0ce1f2464897d8c1995d66e1e4",
      "disabled": "1",
      "ip": "1.1.1.1",
      "item_key": "dc3c8a0ce1f2464897d8c1995d66e1e4",
      "threat_collection": "ip_intel",
      "threat_key": "restapi",
      "time": "1693316401",
      "updated": "0"
    },
    {
      "_key": "ecbe47f05d3b47788529c89050c1bf56",
      "disabled": "0",
      "ip": "1.1.1.1",
      "item_key": "ecbe47f05d3b47788529c89050c1bf56",
      "threat_collection": "ip_intel",
      "threat_key": "restapi",
      "time": "1693316423",
      "updated": "0"
    }
  ],
  "raw": null,
  "inputs": {
    "splunk_query_param1": "ip_intel",
    "splunk_max_return": 10,
    "splunk_query": "| `%param1%` | eval item_key=_key | search %param2%=%param3%",
    "splunk_label": null,
    "splunk_query_param3": "1.1.1.1",
    "splunk_query_param2": "ip"
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-splunk-integration",
    "package_version": "1.4.0",
    "host": "local",
    "execution_time_ms": 9392,
    "timestamp": "2023-08-29 09:50:33"
  }
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
lookup_map = {
  "DNS Name": ("ip_intel", "domain"),
  "Email Attachment": None,
  "Email Attachment Name": ("file_intel", "file_name"),
  "Email Body": None,
  "Email Recipient": None,
  "Email Sender": ("email_intel", "src_user"),
  "Email Sender Name": ("email_intel", "src_user"),
  "Email Subject": ("email_intel", "subject"),
  "File Name": ("file_intel", "file_name"),
  "File Path": None,
  "HTTP Request Header": None,
  "HTTP Response Header": None,
  "IP Address": ("ip_intel", "ip"),
  "Log File": None,
  "MAC Address": None,
  "Malware Family/Variant": None,
  "Malware MD5 Hash": ("file_intel", "file_hash"),
  "Malware Sample": None,
  "Malware Sample Fuzzy Hash": ("file_intel", "file_hash"),
  "Malware SHA-1 Hash": ("file_intel", "file_hash"),
  "Malware SHA-256 Hash": ("file_intel", "file_hash"),
  "Mutex": None,
  "Network CIDR Range": None,
  "Other File": None,
  "Password": None,
  "Port": None,
  "Process Name": ("process_intel", "process"),
  "Registry Key": ("registry_intel", "registry_value_name"),
  "RFC 822 Email Message File": None,
  "Service": ("service_intel", "service"),
  "String": None,
  "System Name": ("service_intel", "service"),
  "URI Path": None,
  "URL": ("http_intel", "url"),
  "URL Referer": ("http_intel", "http_referrer"),
  "User Account": None,
  "User Agent": ("http_intel", "http_user_agent")
}

if artifact.type in lookup_map and lookup_map.get(artifact.type):
  threat_type, threat_field_name = lookup_map.get(artifact.type)
  inputs.splunk_query_param1 = threat_type
  inputs.splunk_query_param2 = threat_field_name
  inputs.splunk_query_param3 = artifact.value
  inputs.splunk_label = getattr(playbook.inputs, "splunk_server")
else:
  helper.fail("Artifact type not supported: {}".format(artifact.type))

inputs.splunk_query = "| `%param1%` | eval item_key=_key | search %param2%=%param3%"
inputs.splunk_max_return = 10
inputs.splunk_search_time_to_wait = 2
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
results = playbook.functions.results.search

if results.get("content", {}):
  for event in results.get("content", {}):
    result_row = incident.addRow("splunk_intel_results")
    result_row.create_date = int(float(event.pop("time"))*1000)
    result_row.source = event.get("threat_key")
    result_row.intel_collection = results.get("inputs", {}).get('splunk_query_param1')
    result_row.intel_key = event.get("_key")
    result_row.splunk_server = getattr(playbook.inputs, "splunk_server")
    result_row.status = "Active" if int(event.get("disabled")) == 0 else "Disabled"
    event.pop("item_key") # not presented
    result_row.intel_field = results.get("inputs", {}).get("splunk_query_param2")
    result_row.intel_value = results.get("inputs", {}).get("splunk_query_param3")
else:
  result_row = incident.addRow("splunk_intel_results")
  result_row.intel_value = artifact.value
  result_row.status = "Not Found"
  result_row.splunk_server = getattr(playbook.inputs, "splunk_server")
```

</p>
</details>

---
## Function - Splunk Update Notable Event
Update notable events according to the status of the corresponding incident. Parameters:
1. event_id: The event_id of the notable event;
2. notable_event_status: Change new status for the notable event;
3. comment: comment to be added to the notable event.

 ![screenshot: fn-splunk-update-notable-event ](./doc/screenshots/fn-splunk-update-notable-event.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `comment` | `text` | No | `-` | Update the notable comment using this |
| `event_id` | `text` | No | `-` | Notable event id from splunk ES |
| `notable_event_status` | `number` | No | `-` | - |
| `splunk_label` | `text` | No | `-` | Label given to each splunk server in the app.config |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "version": 2.0,
  "success": true,
  "reason": null,
  "content": {
    "details": {},
    "success_count": 1,
    "failure_count": 0,
    "warnings": [],
    "success": true,
    "message": "1 event updated successfully"
  },
  "raw": null,
  "inputs": {
    "event_id": "0DE6791A-6F7D-42DC-BAF0-26D58032AE40@@notable@@b98308abb5851cacd0589ec3177389d6",
    "notable_event_status": 2,
    "comment": "SOAR incident is active",
    "splunk_label": null
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-splunk-integration",
    "package_version": "1.4.0",
    "host": "local",
    "execution_time_ms": 3790,
    "timestamp": "2023-08-29 09:55:24"
  }
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
inputs.comment = "Updating information from SOAR"
if incident.properties.splunk_notable_event_id:
  inputs.event_id = incident.properties.splunk_notable_event_id
  if incident.plan_status == "C":
      inputs.notable_event_status = 5
      inputs.comment = "SOAR incident is closed"
  else:
      inputs.notable_event_status = 2
      inputs.comment = "SOAR incident is active"
  inputs.splunk_label = getattr(playbook.inputs, "splunk_server")
else:
  helper.fail("Ensure that the incident custom field is set: splunk_notable_event_id")
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
results = playbook.functions.results.update_event
results_content = results.get("content", {})

result_note = u"<b>Splunk Update notable event</b>:<br><br>"
if isinstance(results.get("content"), dict):
  result_note = result_note + u"""<b>Splunk Update Status</b>: {}<br>
<b>Message</b>: {}""".format("Successful" if results_content.get("success", False) else "Unsuccessful",
                             results_content.get("message", "None"))
else:
  result_note = result_note + results_content

incident.addNote(helper.createRichText(result_note))
```

</p>
</details>

---


## Data Table - Splunk Intel Results

 ![screenshot: dt-splunk-intel-results](./doc/screenshots/dt-splunk-intel-results.png)

#### API Name:
splunk_intel_results

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Create Date | `create_date` | `datetimepicker` | - |
| Intel Collection | `intel_collection` | `text` | - |
| Intel Field | `intel_field` | `text` | - |
| Intel Key | `intel_key` | `text` | - |
| Intel Value | `intel_value` | `text` | - |
| Source | `source` | `text` | - |
| Splunk Server | `splunk_server` | `text` | - |
| Status | `status` | `text` | - |

---


## Playbook
| Playbook Name | Object | API Name |
| --------- | ------ | ------------------ |
| Splunk: Add Artifact - Example (PB) | artifact | `splunk_add_artifact` |
| Splunk: Delete an intel entry - Example (PB) | datatable | `splunk_delete_an_intel_entry` |
| Splunk: Search for an artifact - Example (PB) | artifact | `splunk_search_for_an_artifact` |
| Splunk: Update notable event - Example (PB) | incident | `splunk_update_notable_event` |

---

## How to configure to use a single Splunk Server
To use only a single server there are two ways this can be configured
1. Use the configuration used in Splunk Integration versions prior to V1.1.0
```
[fn_splunk_integration]
host=localhost
port=8089
username=admin
splunkpassword=changeme
verify_cert=false|/path/to/cert
```
2. Specify a splunk system label meaningful to our environment. The label has no other significance.
```
[fn_splunk_integration:splunk_label1]
host=localhost
port=8089
username=admin
splunkpassword=changeme
verify_cert=false|/path/to/cert
```

## Creating playbooks when server/servers in app.config are labeled
The function input field `splunk_label` is required when Splunk server/servers in the app.config are labeled. In the example playbooks function script the
input field `splunk_label` is defined the following way,
```python
inputs.splunk_label = playbook.inputs.splunk_server
```
The playbook field `splunk_server` is a select field that is filled with the labels of the splunk servers from the app.config when the integration is initialized.

## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.

### For Support
This is a IBM Community provided App. Please search the Community [ibm.biz/soarcommunity](https://ibm.biz/soarcommunity) for assistance.
