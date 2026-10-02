# Symantec Endpoint Protection

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
  - [Custom Layouts](#custom-layouts)
- [Function - SEP - Add Fingerprint List](#function---sep---add-fingerprint-list)
- [Function - SEP - Assign Fingerprint List to Group](#function---sep---assign-fingerprint-list-to-group)
- [Function - SEP - Cancel a Command](#function---sep---cancel-a-command)
- [Function - SEP - Delete Fingerprint List](#function---sep---delete-fingerprint-list)
- [Function - SEP - Get Command Status](#function---sep---get-command-status)
- [Function - SEP - Get Computers](#function---sep---get-computers)
- [Function - SEP - Get Critical Events Info](#function---sep---get-critical-events-info)
- [Function - SEP - Get Domains](#function---sep---get-domains)
- [Function - SEP - Get Exceptions Policy](#function---sep---get-exceptions-policy)
- [Function - SEP - Get File Content as Base64](#function---sep---get-file-content-as-base64)
- [Function - SEP - Get Fingerprint List](#function---sep---get-fingerprint-list)
- [Function - SEP - Get Firewall Policy](#function---sep---get-firewall-policy)
- [Function - SEP - Get Groups](#function---sep---get-groups)
- [Function - SEP - Get Policy Summary](#function---sep---get-policy-summary)
- [Function - SEP - Move endpoint](#function---sep---move-endpoint)
- [Function - SEP - Quarantine Endpoints](#function---sep---quarantine-endpoints)
- [Function - SEP - Scan Endpoints](#function---sep---scan-endpoints)
- [Function - SEP - Update Fingerprint List](#function---sep---update-fingerprint-list)
- [Function - SEP - Upload File to SEPM](#function---sep---upload-file-to-sepm)
- [Script - scr_sep_add_artifact_from_scan_results](#script---scr_sep_add_artifact_from_scan_results)
- [Script - scr_sep_parse_email_notification](#script---scr_sep_parse_email_notification)
- [Data Table - Symantec SEP - Critical Events](#data-table---symantec-sep---critical-events)
- [Data Table - Symantec SEP - Endpoint details](#data-table---symantec-sep---endpoint-details)
- [Data Table - Symantec SEP - Endpoint status summary](#data-table---symantec-sep---endpoint-status-summary)
- [Data Table - Symantec SEP - EOC scan results](#data-table---symantec-sep---eoc-scan-results)
- [Data Table - Symantec SEP - Fingerprint lists](#data-table---symantec-sep---fingerprint-lists)
- [Data Table - Symantec SEP - Groups](#data-table---symantec-sep---groups)
- [Data Table - Symantec SEP - Non-compliant Endpoints status details](#data-table---symantec-sep---non-compliant-endpoints-status-details)
- [Playbooks](#playbooks)
- [Troubleshooting & Support](#troubleshooting--support)

---

## Release Notes
| Version | Date | Notes |
| ------- | ---- | ----- |
| 06/2024 | 1.2.0 | Add support for SHA256 hashes. Convert rules/workflows to playbooks. |
| 11/2023 | 1.1.1 | Convert Workflow/Script to Python3 |
| 01/2023 | 1.1.0 | Five more functions added (Cancel a command, Get critical event information, Get all policy summary, Get firewall policy, Get exceptions policy) and relevant test functions implemented. Payload, ReadMe added and bug fix for patch import.|
| 12/2022 | 1.0.2 | Bug fix for osname and selftest |
| 11/2020 | 1.0.1 | Support added for App Host |
| 08/2019 | 1.0.0 | Initial Release |

---

## 1.2.0 Changes
In v1.2, the existing rules and workflows have been replaced with playbooks. This change is made to support the ongoing, newer capabilities of playbooks. Each playbook has the same functionality as the previous, corresponding rule/workflow.

If upgrading from a previous release, you'll noticed that the previous release's rules/workflows remain in place. Both sets of rules and playbooks are active. For manual actions, playbooks will have the same name as it's corresponding rule, but with "(PB)" added at the end. For automatic actions, the playbooks will be disabled by default.

You can continue to use the rules/workflows. But migrating to playbooks will provide greater functionality along with future app enhancements and bug fixes.

## Overview

**Symantec Endpoint Protection Integration for IBM SOAR**

 ![screenshot: main](./doc/screenshots/main.png)

Integration with Symantec Endpoint Protection to facilitate manual enrichment and targeted remediation actions. Teams can investigate an attack by hunting for IOCs or suspect Endpoints across an enterprise, and quickly respond to attacks by executing endpoint remediation actions, such as deleting or blacklisting suspicious files from within the IBM SOAR platform.

### Key Features
•	Execute an Evidence of Compromise (EOC) scan for artifacts of type file (name or path) and hash (MD5, SHA1 or SHA256).
•	Upload a file from an endpoint to the Symantec Endpoint Protect Manager (SEPM).
•	Download a file from the SEPM as base64.
•	Remediate (quarantine) files (by hash match) discovered in an EOC scan.
•	Get endpoint details or status.
•	Get groups.
•	Get fingerprint lists.
•	Add or delete an MD5 hash value from a fingerprint list, which can be used to blacklist files.
•	Assign a fingerprint list to a group for system lock down.
•	Delete a fingerprint list.
•	Move an endpoint to a new group.
•	Quarantine an endpoint.
•	Cancel a command
•	Get critical event information
• Get all policy summary
•	Get firewall policy
•	Get exceptions policy

---

## Requirements

This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, Edge Gateway (also known as App Host) and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `51.0.0.0.9340`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `51.0.0.0.9340`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient_circuits>=51.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions:
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read |
  | Function | Read |

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
The app **does** support a https proxy server.

### Python Environment
Python 3.9, 3.11, and 3.12 are officially supported. When deployed as an app, the app runs on Python 3.11.
Additional package dependencies may exist for each of these packages:
* defusedxml==0.7.1
* resilient_circuits>=51.0.0
* resilient_lib>=51.0.0

### Endpoint Developed With

This app has been implemented using:
| Product Name | Product Version | API URL | API Version |
| ------------ | --------------- | ------- | ----------- |
| Symantec Endpoint Protection | 14 | https://apidocs.securitycloud.symantec.com | v1 |

---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **sep_host** | Yes | `<SEPM server dns name or ip address>` | *DNS name of ip address of the SEP server.* |
| **sep_port** | Yes | `8446` | *The port on which the app is accessible* |
| **sep_auth_path** | Yes | `/sepm/api/v1/identity/authenticate` | *Authentication Path for SEP api.* |
| **sep_base_path** | Yes | `/sepm/api/v1` | *Base path for SEP api.* |
| **sep_username** | Yes | `<username>` | *User name for SEP api access.* |
| **sep_password** | Yes | `<password>` | *User password for SEP api access.* |
| **sep_domain** | Yes | `<SEP domain name>` | *User password for McAfee ESM api access.* |
| **sep_results_limit** | Yes | `200` | *Limit result sent to IBM SOAR, add full result as an attachment.* |
| **sep_scan_timeout** | Yes | `1800` | *Period of time (seconds) to wait for all endpoints to return a scan result.* |
| **https_proxy** | No | `<HTTPS_PROXY>` | *Optional settings for accessing Symantec Endpoint Protection via a https proxy* |
| **client_auth_cert** | No | `<CLIENT_AUTH_CERT>` | *Specify path to <cert.pem> file if client certs are needed to authenticate* |
| **client_auth_key** | No | `<CLIENT_AUTH_KEY>` | *Specify path to <cert_private_key.pem> file if client certs are needed to authenticate* |

### Custom Layouts
* To use the functions, create new Incident tabs e.g. Symantec SEP - Threats, Symantec SEP - Blacklists and Symantec SEP - Status. Drag the SEP data tables on to the layouts and click Save as shown in the screenshots below:
  ![screenshot: custom_layouts_1](./doc/screenshots/custom_layouts_1.png)
  ![screenshot: custom_layouts_2](./doc/screenshots/custom_layouts_2.png)
  ![screenshot: custom_layouts_3](./doc/screenshots/custom_layouts_3.png)

---

## Function - SEP - Add Fingerprint List
Add an MD5 hash to a new fingerprint list.
Note: Currently only supports MD5 hash type.

 ![screenshot: fn-sep---add-fingerprint-list ](./doc/screenshots/fn-sep---add-fingerprint-list.png)
<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_description` | `text` | No | `-` | The SEP object (e.g. scan) description. |
| `sep_domainid` | `text` | No | `-` | The SEPM domain id. |
| `sep_fingerprintlist_name` | `text` | No | `-` | Name of a SEP fingerprint list. |
| `sep_hash_value` | `text` | No | `-` | The hash value. Can be MD5 or SHA256 hash value. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "id": "44BB68279D984220AD60A069DCF6079F"
  },
  "inputs": {
    "sep_description": "Fingerprint list \u0027Blacklist2\u0027",
    "sep_domainid": "6E70F043092E5BB93F74FD57C083F99E",
    "sep_fingerprintlist_name": "Blacklist2",
    "sep_hash_value": "e4ac4548eeebdba19817b5c47322f0c95a17a9ef6af4099088d6e552f34038d9"
  },
  "metrics": {
    "execution_time_ms": 226915,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-15 08:34:13",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
content = playbook.functions.results.get_domains_results.get("content", [])

for i in range(len(content)):
  if content[i].get("name") == playbook.inputs.sep_domain_name:
    inputs.sep_domainid = content[i].get("id")
    break

inputs.sep_hash_value = artifact.value
inputs.sep_fingerprintlist_name = playbook.inputs.sep_fingerprintlist_name
inputs.sep_description = "Fingerprint list '{}'".format(inputs.get("sep_fingerprintlist_name"))
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_add_fingerprint_list script ##
FN_NAME = "Add Hash to Fingerprint List"
WF_NAME = "fn_sep_add_fingerprint_list"
results = playbook.functions.results.add_fingerprintlist_results
INPUTS = results.get("inputs")
note_text = None
hash_type = "MD5"
if artifact.type == "Malware SHA-256 Hash":
  hash_type = "SHA256"

if results.get("success"):
  # If we got here we assume we are successful.
  note_text = f"Symantec SEP Integration:\nPlaybook <b>{WF_NAME}</b>:\nSuccessfully added {hash_type} hash <b>{artifact.value}</b> to new fingerprint "\
              f"list <b>{INPUTS.get('sep_fingerprintlist_name')}</b> for SOAR function <b>{FN_NAME}</b>"
else:
  note_text = f"Symantec SEP Integration:\nPlaybook <b>{WF_NAME}</b>:\nFailed with reason: {results.get('reason')}"

incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Assign Fingerprint List to Group
Assign a fingerprint list to a group for lock-down.

 ![screenshot: fn-sep---assign-fingerprint-list-to-group ](./doc/screenshots/fn-sep---assign-fingerprint-list-to-group.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_fingerprintlist_id` | `text` | No | `-` | Id of SEP fingerprint list |
| `sep_groupid` | `text` | No | `-` | Group id on which to run the SEP command. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {},
  "inputs": {
    "sep_fingerprintlist_id": "fingerprintlist_id",
    "sep_groupid": "groupid"
  },
  "metrics": {
    "execution_time_ms": 2038,
    "host": "host",
    "package": "fn-sep",
    "package_version": "1.0.1",
    "timestamp": "2023-01-06 11:32:28",
    "version": "1.0"
  },
  "raw": "{}",
  "reason": null,
  "success": true,
  "version": "1.0"
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
content = playbook.functions.results.get_fingerprintlist_results.get("content", {})
inputs.sep_fingerprintlist_id = content.get("id")
inputs.sep_groupid = row.group_id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_assign_fingerprint_list_to_group ##
# Globals
FN_NAME = "fn_sep_assign_fingerprint_list_to_group"
WF_NAME = "Assign Fingerprint List to lockdown group"
results = playbook.functions.results.assign_fingerprintlist_to_group_results
content = results.get("content", {})
INPUTS = results.get("inputs", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

# Processing
note_text = ''
if content:
  if isinstance(content, dict) and content.get("errorCode") and int(content.get("errorCode")) == 400:
    # The finger print list doesn't exist.
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThe fingerprint list <b>{1}</b> does not exist or is invalid " \
                "for domain id <b>{2}</b> for SOAR function <b>{3}</b>"\
        .format(WF_NAME, INPUTS.get("sep_fingerprintlist_name"), row.domain_id, FN_NAME)
  else:
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nSuccessfully assigned fingerprint list with id " \
                "<b>{1}</b> to group with id <b>{2}</b> for SOAR function <b>{3}</b>"\
        .format(WF_NAME, INPUTS.get("sep_fingerprintlist_id"), INPUTS.get("sep_groupid"), FN_NAME)

else:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> results returned " \
               "with fingerprint id <b>{1}</b> and group id <b>{2}</b> for SOAR function <b>{3}</b>"\
      .format(WF_NAME, INPUTS.get("sep_fingerprintlist_id"), INPUTS.get("sep_groupid"), FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Cancel a Command
Cancels an existing command by creating a new cancel command for clients for which the command is still pending.

 ![screenshot: fn-sep---cancel-a-command ](./doc/screenshots/fn-sep---cancel-a-command.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_command_id` | `text` | Yes | `-` | The command ID for which details are needed. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "commandID": "4C697374D15C433880A56800BAC25E56"
  },
  "inputs": {
    "sep_command_id": "367F5DE4A7F346E4A40B3475DFD93B06"
  },
  "metrics": {
    "execution_time_ms": 1322,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-17 10:59:14",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.sep_command_id = playbook.inputs.sep_command_id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.cancel_command_results
if results.get("success"):
  incident.addNote(f"SEP Command {playbook.inputs.sep_command_id} was canceled.")
else:
  incident.addNote(f"SEP Command {playbook.inputs.sep_command_id} was not canceled. Reason: {results.get('reason')}")
```

</p>
</details>

---
## Function - SEP - Delete Fingerprint List
Delete  a  fingerprint list.

 ![screenshot: fn-sep---delete-fingerprint-list ](./doc/screenshots/fn-sep---delete-fingerprint-list.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_fingerprintlist_id` | `text` | No | `-` | Id of SEP fingerprint list |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {},
  "inputs": {
    "sep_fingerprintlist_id": "fingerprintlist_id"
  },
  "metrics": {
    "execution_time_ms": 2041,
    "host": "host",
    "package": "fn-sep",
    "package_version": "1.0.1",
    "timestamp": "2023-01-06 11:12:40",
    "version": "1.0"
  },
  "raw": "{}",
  "reason": null,
  "success": true,
  "version": "1.0"
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.sep_fingerprintlist_id = row.list_id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_delete_fingerprint_list ##
# Globals
FN_NAME = "fn_sep_delete_fingerprint_list"
WF_NAME = "Delete Fingerprint List"
results = playbook.functions.results.delete_fingerprintlist_results
content = results.get("content", {})
INPUTS = results.get("inputs", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

# Processing
note_text = ''
if content:
  if "errorCode" in content and int(content.get("errorCode")) == 410:
    # The finger print list doesn't exist.
    note_text = "Symantec SEP Integration:\nPlaybooks <b>{0}</b>:\nThe fingerprint list <b>{1}</b> does not exist or is invalid " \
                "for SOAR function <b>{2}</b>"\
        .format( WF_NAME, INPUTS.get("sep_fingerprintlist_name"), FN_NAME)
  else:
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nSuccessfully deleted fingerprint list with id " \
                "<b>{1}</b> for SOAR function <b>{2}</b>"\
        .format(WF_NAME, INPUTS.get("sep_fingerprintlist_id"), FN_NAME)
    row.list_description = "Fingerprint list deleted"
    row.hash_values = "Fingerprint list deleted"
    row.list_id = "Fingerprint list deleted"

else:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> results returned " \
               "with fingerprint id <b>{1}</b> for SOAR function <b>{2}</b>"\
      .format(WF_NAME, INPUTS.get("sep_fingerprintlist_id"),  FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Get Command Status
Gets the details of a command status from a command id.

 ![screenshot: fn-sep---get-command-status ](./doc/screenshots/fn-sep---get-command-status.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_commandid` | `text` | No | `-` | Command id of SEP job. |
| `sep_incident_id` | `number` | No | `-` | The IBM SOAR incident ID. |
| `sep_matching_endpoint_ids` | `boolean` | No | `-` | Get list of matching endpoints. |
| `sep_order` | `text` | No | `-` | Specifies whether the results are in ascending order (ASC) or descending order (DESC). |
| `sep_pageindex` | `number` | No | `-` | The index page that is used for the returned results. The default page index is 1. |
| `sep_pagesize` | `number` | No | `-` | The number of results to include on each page. The default is 20. |
| `sep_scan_date` | `text` | No | `-` | Time when scan was initiated |
| `sep_sort` | `text` | No | `-` | The column by which the results are sorted. Possible values are COMPUTER_NAME (Default value), COMPUTER_ID, COMPUTER_DOMAIN_NAME, or DOMAIN_ID. |
| `sep_status_type` | `text` | No | `-` | The type of command status requested. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "content": [
      {
        "beginTime": null,
        "binaryFileId": null,
        "computerId": "01ECF4E8092E5BB91E4D52E45C3ABE4D",
        "computerIp": "9.37.29.102",
        "computerName": "WIN-N5KGH4CP3N3",
        "currentLoginUserName": "Administrator",
        "domainName": "Default",
        "hardwareKey": "8DACE2559C1C951E09CC0BF71D973BB7",
        "lastUpdateTime": null,
        "resultInXML": null,
        "stateId": 0,
        "subStateDesc": null,
        "subStateId": 0
      }
    ],
    "firstPage": true,
    "lastPage": true,
    "number": 0,
    "numberOfElements": 1,
    "overall_command_state": "In progress",
    "remediate_artifact_value": "",
    "scan_artifact_value": "",
    "size": 20,
    "sort": [
      {
        "ascending": true,
        "direction": "ASC",
        "property": "Begintime"
      }
    ],
    "totalElements": 1,
    "totalPages": 1,
    "total_ep_count": 1,
    "total_fail_remediation_count": 0,
    "total_match_count": 0,
    "total_match_ep_count": 0,
    "total_not_completed": 1,
    "total_remediation_count": 0,
    "total_remediation_ep_count": 0
  },
  "inputs": {
    "sep_commandid": "1CA9D4F37DD94CA88A9D93D09402E3D3",
    "sep_incident_id": 2133,
    "sep_status_type": "quarantine"
  },
  "metrics": {
    "execution_time_ms": 765,
    "host": "my.app.host",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-08-21 08:40:33",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.sep_incident_id = incident.id
inputs.sep_commandid = row.remediation_commandid
inputs.sep_status_type = "remediation"
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_get_command_status script ##
# Globals
# List of fields in datatable fn_sep_get_command_status script
DATA_TBL_FIELDS = ["query_execution_date", "remediation_status"]
FN_NAME = "fn_sep_get_command_status"
WF_NAME = "Get Remediation status"
STATUS_TYPE = "remediate"
results = playbook.functions.results.get_command_results
REMEDIATE_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")
C_OUTER = results.get("content", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

# Processing
remediation_command_state = C_OUTER.get("overall_command_state")
total_remediation_count = C_OUTER.get("total_remediation_count")
total_remediation_ep_count = C_OUTER.get("total_remediation_ep_count")
total_fail_remediation_count = C_OUTER.get("total_fail_remediation_count")
total_ep_count = C_OUTER.get("total_ep_count")
att_name = C_OUTER.get("att_name")

note_text = ''
att_note = ''
if C_OUTER:
  if total_remediation_count > 0:
    att_note = "<br>Added full result as an attachment. Attachment name: <b>{0}</b>.".format(att_name)
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nRemediate artifact returned <b>{1}</b> remediated " \
              "artifacts on <b>{2}</b> out of a total of <b>{3}</b> endpoints for artifact with type <b>{4}</b> " \
              "and value <b>{5}</b> for SOAR function <b>{7}</b>.{6}" \
      .format(WF_NAME, total_remediation_count, total_remediation_ep_count, total_ep_count, row.artifact_type,
              row.artifact_value, att_note, FN_NAME)

  if remediation_command_state == "Completed":
    if total_fail_remediation_count == 0 and total_remediation_count > 0:
      row.remediation_status = "{0} at {1}. For remediation results see note/attachment.".format(remediation_command_state, REMEDIATE_EXECUTION_DATE)
    elif total_fail_remediation_count == 0 and total_remediation_count == 0:
      row.remediation_status = "No match found"
    elif total_fail_remediation_count > 0:
      row.remediation_status = "Failed"
  else:
    row.remediation_status = remediation_command_state
else:
  row.remediation_status = remediation_command_state
  note_text += "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nRemediate artifact returned <b>no</b> results for " \
               "for artifact with type <b>{1}</b> and value <b>{2}</b> for SOAR function <b>{3}</b>"\
      .format(WF_NAME, row.artifact_type, row.artifact_value, FN_NAME)
incident.addNote(helper.createRichText(note_text))

```

</p>
</details>

---
## Function - SEP - Get Computers
Gets the information about the computers in a specified domain.

 ![screenshot: fn-sep---get-computers ](./doc/screenshots/fn-sep---get-computers.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_computername` | `text` | No | `-` | The host name of computer. Wild card is supported as '*'. |
| `sep_domain` | `text` | No | `-` | The SEPM domain. |
| `sep_lastupdate` | `text` | No | `-` | Indicates when a computer last updated its status. The default value of 0 gets all the results. |
| `sep_matching_endpoint_ids` | `boolean` | No | `-` | Get list of matching endpoints. |
| `sep_order` | `text` | No | `-` | Specifies whether the results are in ascending order (ASC) or descending order (DESC). |
| `sep_os` | `text` | No | `-` | The list of OS to filter. Possible values are CentOs, Debian, Fedora, MacOSX, Oracle, OSX, RedHat, SUSE, Ubuntu, Win10, Win2K, Win7, Win8, WinEmb7, WinEmb8, WinEmb81, WinFundamental, WinNT, Win2K3, Win2K8, Win2K8R2, WinVista, WinXP, WinXPEmb, WinXPProf64 |
| `sep_pageindex` | `number` | No | `-` | The index page that is used for the returned results. The default page index is 1. |
| `sep_pagesize` | `number` | No | `-` | The number of results to include on each page. The default is 20. |
| `sep_sort` | `text` | No | `-` | The column by which the results are sorted. Possible values are COMPUTER_NAME (Default value), COMPUTER_ID, COMPUTER_DOMAIN_NAME, or DOMAIN_ID. |
| `sep_status` | `boolean` | No | `-` | Get overall status for endpoints. |
| `sep_status_details` | `boolean` | No | `-` | Get endpoints status details. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "content": [
      {
        "agentId": "FC50D87A092E5BB91E4D52E4CB82C6CF",
        "agentTimeStamp": 1724243995817,
        "agentType": "105",
        "agentUsn": 1228250,
        "agentVersion": "14.3.9717.7000",
        "apOnOff": 3,
        "atpDeviceId": null,
        "atpServer": "",
        "attributeExtension": "",
        "avDefsetRevision": "21",
        "avDefsetSequence": "236155",
        "avDefsetVersion": "240820021",
        "avEngineOnOff": 1,
        "bashStatus": 1,
        "behavioralAnalysisDefsetVersion": "240820001",
        "biosVersion": "INTEL  - 6040000 PhoenixBIOS 4.0 Release 6.0",
        "bwf": 2,
        "cidsBrowserFfOnOff": 1,
        "cidsBrowserIeOnOff": 1,
        "cidsDefsetVersion": "240820081",
        "cidsDrvMulfCode": 0,
        "cidsDrvOnOff": 1,
        "cidsEngineVersion": "17.2.11.37",
        "cidsSilentMode": 0,
        "computerDescription": "",
        "computerName": "WIN-N5KGH4CP3N3",
        "computerTimeStamp": 1724243995822,
        "computerUsn": 1228250,
        "contentUpdate": 1,
        "creationTime": 1721051528927,
        "currentClientId": "76B1CFBD092E5BB91E4D52E426621842",
        "daOnOff": 3,
        "deleted": 0,
        "department": "",
        "deploymentMessage": "",
        "deploymentPreVersion": "",
        "deploymentRunningVersion": "14.3.9717.7000",
        "deploymentStatus": "302456832",
        "deploymentTargetVersion": "14.3.9717.7000",
        "description": "",
        "dhcpServer": "0.0.0.0",
        "diskDrive": "C:\\",
        "dnsServers": [
          "9.42.106.2",
          "9.42.106.3"
        ],
        "domainOrWorkgroup": "WORKGROUP",
        "edrStatus": 0,
        "elamOnOff": 1,
        "email": "",
        "employeeNumber": "",
        "employeeStatus": "",
        "encryptedDevicePassword": null,
        "fbwf": 2,
        "firewallOnOff": 1,
        "freeDisk": 57622753280,
        "freeMem": 1404067840,
        "fullName": "",
        "gateways": [
          "9.37.29.1",
          "0.0.0.0",
          "0.0.0.0",
          "0.0.0.0"
        ],
        "group": {
          "domain": {
            "id": "6E70F043092E5BB93F74FD57C083F99E",
            "name": "Default"
          },
          "externalReferenceId": null,
          "fullPathName": null,
          "id": "E5E684A6092E5BB90F46E84BB6F35BBC",
          "name": "My Company\\Group1",
          "source": null
        },
        "groupUpdateProvider": false,
        "hardwareKey": "8DACE2559C1C951E09CC0BF71D973BB7",
        "homePhone": "",
        "hypervisorVendorId": "1",
        "idsChecksum": null,
        "idsSerialNo": "",
        "idsVersion": "",
        "infected": 1,
        "installType": "0",
        "ipAddresses": [
          "9.37.29.102"
        ],
        "isGrace": 0,
        "isNpvdiClient": 0,
        "jobTitle": "",
        "kernel": null,
        "lastConnectedIpAddr": "9.37.29.102",
        "lastDeploymentTime": 1721052502000,
        "lastDownloadTime": 1721051552300,
        "lastHeuristicThreatTime": 0,
        "lastScanTime": 1724225880000,
        "lastServerId": "477D0222092E5BB91EC14117B8C56C14",
        "lastServerName": "c95648v1",
        "lastSiteId": "C18D5D63092E5BB937BFAB713E75E3E9",
        "lastSiteName": "My Site",
        "lastUpdateTime": 1724243995809,
        "lastVirusTime": 1723561216000,
        "licenseExpiry": 0,
        "licenseId": null,
        "licenseStatus": -1,
        "logicalCpus": 0,
        "loginDomain": "LocalComputer",
        "logonUserName": "Administrator",
        "macAddresses": [
          "00-50-56-B4-75-BA"
        ],
        "majorVersion": 14,
        "memory": 4294430720,
        "minorVersion": 3,
        "mobilePhone": "",
        "officePhone": "",
        "onlineStatus": 1,
        "operatingSystem": "Windows Server 2012 Standard Edition",
        "osBitness": "x64",
        "osElamStatus": 0,
        "osFlavorNumber": 7,
        "osFunction": "Server",
        "osLanguage": "en-US",
        "osMajor": 6,
        "osMinor": 2,
        "osName": "Windows Server 2012",
        "osServicePack": "9200",
        "osVersion": "6.2",
        "patternIdx": "B47B44938636895A503D54AEEB825207",
        "pepOnOff": 1,
        "physicalCpus": 1,
        "processorClock": 2400,
        "processorType": "Intel64 Family 6 Model 45 Stepping 7",
        "profileChecksum": null,
        "profileSerialNo": "E5E6-08/21/2024 12:38:31 900",
        "profileVersion": "14.3.25029",
        "pskVersion": 0,
        "ptpOnOff": 1,
        "publicKey": "BgIAAACkAABSU0ExAAgAAAEAAQDJQWPswlLrapkfkrrHE/GXPhvoJcmLbLXPs13mDC6PMI5zPm0p1FkQQMXuP3B7226OSac4j+WOqtQvTUy4poQwWn6ijUNuOmQE8AhjJGQeWbuN18jsUuu24T9S3xCcUUrGMPd5v8DIqAWZuXEZ5sjIXMhYI1hvTVmzKZNczXXw64kRvoc7/yDtC98uJfQxxWpIaa+oppPvtp8kYrdBTqwppDppJhocK+Jjs1l85Hkp7qdrNs+eZ33zMxUrlW/j8jvpOtcfIPLpqXD8FaClh7httfydwQqCeRZ2HBLVYIIZocOAuqKqGMvCpbdQAs/ypP5dH7zztwL4CunXJqMKeUy4",
        "quarantineCode": 105,
        "quarantineDesc": "Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.",
        "quarantineStatus": 3,
        "readableLastScanTime": "2024-08-21 03:38:00",
        "readableLastUpdateTime": "2024-08-21 08:39:55",
        "readableLastVirusTime": "2024-08-13 11:00:16",
        "rebootReason": "",
        "rebootRequired": 0,
        "securityVirtualAppliance": null,
        "serialNumber": "VMware-42 34 52 a5 74 32 c7 6d-a9 27 aa 84 04 d4 a1 29",
        "snacLicenseId": null,
        "subnetMasks": [
          "255.255.255.0"
        ],
        "svaId": null,
        "tamperOnOff": 1,
        "tdadGlobalDataDownloadTime": 0,
        "tdadGlobalDataProcessingDoneTime": 0,
        "tdadOnOff": 3,
        "tdadStatusId": 127,
        "telemetryHwid": "8E76E0DA-CE2B-2237-925B-67F7E347B878",
        "telemetryMid": "B3EE6501-5E29-4F03-B9D8-64762C8EF84D",
        "timeZone": 480,
        "timediffLastScanTime": 18156.769050836563,
        "timediffLastUpdateTime": 40.96005082130432,
        "timediffLastVirusTime": 682820.7690508366,
        "tmpDevice": null,
        "totalDiskSpace": 81567,
        "tpmDevice": "0",
        "uniqueId": "01ECF4E8092E5BB91E4D52E45C3ABE4D",
        "uuid": "A5523442-3274-6DC7-A927-AA8404D4A129",
        "uwf": 2,
        "virtualizationPlatform": "VMware",
        "vsicStatus": 3,
        "winServers": [
          "0.0.0.0",
          "0.0.0.0"
        ],
        "worstInfectionIdx": "0",
        "writeFiltersStatus": null,
        "wssStatus": 0
      }
    ],
    "firstPage": true,
    "lastPage": true,
    "number": 0,
    "numberOfElements": 1,
    "size": 20,
    "sort": [
      {
        "ascending": true,
        "direction": "ASC",
        "property": "COMPUTER_NAME"
      }
    ],
    "totalElements": 1,
    "totalPages": 1
  },
  "inputs": {
    "sep_computername": "WIN-N5KGH4CP3N3"
  },
  "metrics": {
    "execution_time_ms": 992,
    "host": "my.app.host",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-08-21 08:40:36",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.sep_status = True
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_get_computers script ##
# Globals
# List of fields in datatable for "Get Endpoints status" playbook.
DATA_TBL_FIELDS = ["query_execution_date", "non_compliant", "up_to_date", "out_of_date", "total", "disabled",
                   "offline","hi_failed", ]
FN_NAME = "fn_sep_get_computers"
WF_NAME = "Get Endpoints status"
results = playbook.functions.results.get_computers_results
CONTENT = results.get("content", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

# Processing
note_text = ''
new_row = incident.addRow("sep_endpoint_status_summary")

if CONTENT and CONTENT.get("total"):
  new_row.query_execution_date = QUERY_EXECUTION_DATE
  for f in DATA_TBL_FIELDS:
    if f == "query_execution_date":
      continue
    new_row[f] = CONTENT.get(f)

  if CONTENT.get("non_compliant") > 0:
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>{1}</b> non-compliant endpoints " \
                "detected out of a total of <b>{2}</b> for SOAR function <b>{3}</b>"\
        .format(WF_NAME, CONTENT.get("non_compliant"), CONTENT.get("total"), FN_NAME)
  else:
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> non-compliant endpoints " \
                 "detected out of a total of <b>{1}</b> for SOAR function <b>{2}</b>" \
        .format(WF_NAME, CONTENT.get("total"), FN_NAME)
else:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> results returned for SOAR " \
              "function <b>{1}</b>".format(WF_NAME, FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Get Critical Events Info
Gets information related to critical events. 'results_limit' is not currently used for this function.

 ![screenshot: fn-sep---get-critical-events-info ](./doc/screenshots/fn-sep---get-critical-events-info.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_results_limit` | `number` | No | `5` | The maximum number of records to be returned. Page size must be between 1 and 10000 |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "criticalEventsInfoList": [
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:02:38.0",
        "eventId": "C73763EF092E5BB9462D7353C645BC2C",
        "message": "To enhance security, Symantec recommends that you should require the users in this client group to use passwords in the following situations: opening, stopping, or uninstalling the client, or importing the Sylink file. You should assign a password to the following client groups.\u003cbr/\u003e\u003cbr/\u003eDefault: My Company\u003cbr/\u003e\u003cbr/\u003e\u003cbr/\u003eFor information on how to enable password protection on the client, see: \u003ca href=\"https://techdocs.broadcom.com/bin/gethidpage.html?ux-context-string=sesm_computersnusers_policies_password_setting\u0026appid=SEP\u0026language=en\u0026format=rendered\" class=\"bluelink\" target=\"_blank\" rel=\"noopener\"\u003ePassword-protecting the Symantec Endpoint Protection client\u003c/a\u003e",
        "subject": "Some Symantec Endpoint Protection groups have not been assigned a password."
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:02:50.0",
        "eventId": "388DC550092E5BB9462D7353CF5066D4",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jun 26, 2024 7:02:34 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:03:03.0",
        "eventId": "A091BB08092E5BB9462D735340E9132C",
        "message": "Date: Jun 26, 2024 6:46:43 AM PDT\tServer: c95648v1\nDownload: Successfully downloaded the Symantec Agent for Linux 14.3 RU8 package from LiveUpdate. This package is now available for deployment.",
        "subject": "New software package available"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:03:03.0",
        "eventId": "8EC7022F092E5BB9462D73539D642D01",
        "message": "Date: Jun 26, 2024 6:50:27 AM PDT\tServer: c95648v1\nDownload: Successfully downloaded the Symantec Agent for Linux 14.3 RU5 package from LiveUpdate. This package is now available for deployment.",
        "subject": "New software package available"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:03:03.0",
        "eventId": "CCF70323092E5BB9462D7353600B23F8",
        "message": "Date: Jun 26, 2024 6:51:35 AM PDT\tServer: c95648v1\nDownload: Successfully downloaded the Symantec Endpoint Protection Mac 14.3 RU3 package from LiveUpdate. This package is now available for deployment.",
        "subject": "New software package available"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:03:03.0",
        "eventId": "8F3BBDAE092E5BB9462D7353B2402856",
        "message": "Date: Jun 26, 2024 6:52:23 AM PDT\tServer: c95648v1\nDownload: Successfully downloaded the Symantec Endpoint Protection Mac 14.3 RU6 package from LiveUpdate. This package is now available for deployment.",
        "subject": "New software package available"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:03:03.0",
        "eventId": "B935736A092E5BB9462D73537BBD9220",
        "message": "Date: Jun 26, 2024 6:54:04 AM PDT\tServer: c95648v1\nDownload: Successfully downloaded the Symantec Endpoint Protection Mac 14.3 RU5 package from LiveUpdate. This package is now available for deployment.",
        "subject": "New software package available"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:03:03.0",
        "eventId": "2CAEEDB5092E5BB9462D7353ADD2908C",
        "message": "Date: Jun 26, 2024 6:54:10 AM PDT\tServer: c95648v1\nDownload: Successfully downloaded the Symantec Agent for Linux 14.3 RU4 package from LiveUpdate. This package is now available for deployment.",
        "subject": "New software package available"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:03:03.0",
        "eventId": "D34404C5092E5BB9462D73534707F282",
        "message": "Date: Jun 26, 2024 6:54:28 AM PDT\tServer: c95648v1\nDownload: Successfully downloaded the Symantec Endpoint Protection Mac 14.3 RU8 package from LiveUpdate. This package is now available for deployment.",
        "subject": "New software package available"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:03:03.0",
        "eventId": "D130C96D092E5BB9462D73538F0E81DE",
        "message": "Date: Jun 26, 2024 6:54:46 AM PDT\tServer: c95648v1\nDownload: Successfully downloaded the Symantec Agent for Linux 14.3 RU6 package from LiveUpdate. This package is now available for deployment.",
        "subject": "New software package available"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-26 14:29:46.0",
        "eventId": "00AEA0F3092E5BB9462D7353169FDC4E",
        "message": "Number of clients changed: 1.  Changes could be that a client was added, renamed, or deleted, Unmanaged Detector status changed, client mode changed, or the hardware changed.",
        "subject": "Informational: Symantec Endpoint Protection Computer List Changed"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-27 07:03:15.0",
        "eventId": "6443D9CA092E5BB936229E5074834588",
        "message": "Your Symantec Endpoint Protection Trial license expires in 60 days. To continue to receive virus definitions and product updates, contact your \u0026lt;a class=\u0026quot;bluelink\u0026quot; onclick=\u0026quot;createWindowFromURL(\u0026#039;../util/universal-redirect.php?WhereWeWant=https://ced.broadcom.com/sep/14/partnerlocator\u0026#039;, \u0026#039;_blank\u0026#039;, \u0026#039;scrollbars=yes,width=800, height=650, resizable=yes, screenX=100, screenY=100\u0026#039;);\u0026quot; href=\u0026quot;#\u0026quot; \u0026gt;preferred reseller\u0026lt;/a\u0026gt;.\u0026lt;br\u0026gt;",
        "subject": "Information: Symantec Trial license Expires In 60 Days"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-28 12:29:23.0",
        "eventId": "5ED2B2DE092E5BB936229E5022E27035",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jun 28, 2024 5:29:04 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-28 22:29:23.0",
        "eventId": "D23F6954092E5BB936229E50AA2CB93F",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jun 28, 2024 3:29:06 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-29 08:30:38.0",
        "eventId": "10E1F0A9092E5BB97E3F195BF1A05A94",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jun 29, 2024 1:30:17 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-08 17:58:05.0",
        "eventId": "EC7CF59F092E5BB954B29F87D815C7AC",
        "message": "Date: Jul 8, 2024 10:54:58 AM PDT\tServer: c95648v1\nDownload: Successfully downloaded the null package from LiveUpdate. This package is now available for deployment.",
        "subject": "New software package available"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-28 02:28:23.0",
        "eventId": "1C4CB36B092E5BB936229E50775A9E56",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jun 27, 2024 7:28:02 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-29 18:30:40.0",
        "eventId": "C07CE910092E5BB97E3F195B25EC92BF",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jun 29, 2024 11:30:18 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-30 04:30:45.0",
        "eventId": "6E7A6527092E5BB97E3F195B1BCE841D",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jun 29, 2024 9:30:30 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-06-30 14:30:49.0",
        "eventId": "43E80046092E5BB97E3F195BC2F4AD74",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jun 30, 2024 7:30:32 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-01 00:30:54.0",
        "eventId": "1C8161DE092E5BB97E3F195BAFB5DBB1",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jun 30, 2024 5:30:36 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-01 10:31:04.0",
        "eventId": "573028FB092E5BB97E3F195B639B9F4D",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 1, 2024 3:30:50 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-01 20:31:09.0",
        "eventId": "A4D7D5C9092E5BB97E3F195BAEEF6330",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 1, 2024 1:30:55 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-03 22:31:36.0",
        "eventId": "0C680D8A092E5BB97E3F195B276EBAE8",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 3, 2024 3:31:18 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-04 18:31:45.0",
        "eventId": "9C5ED05E092E5BB97E3F195B9B610D17",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 4, 2024 11:31:30 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-06 10:32:12.0",
        "eventId": "62646CAA092E5BB97E3F195BA0C158E8",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 6, 2024 3:31:51 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-07 06:32:24.0",
        "eventId": "A51FCF09092E5BB97E3F195B11557294",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 6, 2024 11:32:02 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-08 13:18:11.0",
        "eventId": "58E62790092E5BB954B29F87B6A521C4",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 8, 2024 6:17:51 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-08 23:18:04.0",
        "eventId": "3A23B513092E5BB954B29F8789D7CF43",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 8, 2024 4:17:42 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-02 06:31:13.0",
        "eventId": "6F4FCE57092E5BB97E3F195B0E91B958",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 1, 2024 11:30:59 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-02 16:31:18.0",
        "eventId": "816E4D4F092E5BB97E3F195B3A42774E",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 2, 2024 9:31:00 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-03 02:31:28.0",
        "eventId": "520DD58E092E5BB97E3F195B7C029BFE",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 2, 2024 7:31:10 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-04 08:31:40.0",
        "eventId": "CDFCA802092E5BB97E3F195B7F1A8637",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 4, 2024 1:31:18 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-05 04:31:52.0",
        "eventId": "E9FEB9C7092E5BB97E3F195BF7613F08",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 4, 2024 9:31:32 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-05 14:32:02.0",
        "eventId": "AC5F04BE092E5BB97E3F195B3897DEFB",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 5, 2024 7:31:44 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-06 00:32:07.0",
        "eventId": "DB847B29092E5BB97E3F195B18644C0E",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 5, 2024 5:31:44 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-07 16:32:33.0",
        "eventId": "8DA48D11092E5BB97E3F195BD8691A78",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 7, 2024 9:32:14 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-08 02:32:38.0",
        "eventId": "76530F37092E5BB97E3F195B364CA62E",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 7, 2024 7:32:16 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-08 13:21:05.0",
        "eventId": "3F45D825092E5BB954B29F875AE1D576",
        "message": "Number of system events detected: 1 \r\nSystem events included: Server and Errors.\r\n\r\n",
        "subject": "System Event Notification"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-09 19:19:05.0",
        "eventId": "8C428752092E5BB954B29F87BC51C1D2",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 9, 2024 12:18:46 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-03 12:31:32.0",
        "eventId": "48C3782D092E5BB97E3F195BD2035D87",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 3, 2024 5:31:08 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-06 20:32:17.0",
        "eventId": "06269CC1092E5BB97E3F195BB9232A9B",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 6, 2024 1:32:01 PM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-09 09:19:05.0",
        "eventId": "7A42801F092E5BB954B29F87CA0AE4E7",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 9, 2024 2:18:44 AM.",
        "subject": "Server Health Alert"
      },
      {
        "acknowledged": 0,
        "eventDateTime": "2024-07-10 05:19:14.0",
        "eventId": "C6C9F775092E5BB954B29F871CA45A10",
        "message": "Server c95648v1 health status: poor. \nReason: The Symantec Endpoint Protection Manager server does not have Symantec Endpoint Protection installed. \nStatus reported on Jul 9, 2024 10:18:56 PM.",
        "subject": "Server Health Alert"
      }
    ],
    "lastUpdated": 1720622406545,
    "totalUnacknowledgedMessages": 44
  },
  "inputs": {},
  "metrics": {
    "execution_time_ms": 1078,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-10 10:40:06",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
None
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from time import time

now = int(time()*1000)
results = playbook.functions.results.get_critical_events_info_results

if not results.get("success"):
  incident.addNote(f"Symantec SEP - Get Critical Events failed: {results.reason}")
else:
  for event in results.get("content", {}).get("criticalEventsInfoList", []):
    row = incident.addRow("sep_critical_events")
    row['date_added'] = now
    row['event_id'] = event.get('eventId')
    row['event_date'] = event.get('eventDateTime')
    row['subject'] = event.get('subject')
    row['message'] = event.get('message')
    row['acknowledged'] = bool(event.get('acknowledged'))
```

</p>
</details>

---
## Function - SEP - Get Domains
Gets a list of all accessible domains.

 ![screenshot: fn-sep---get-domains ](./doc/screenshots/fn-sep---get-domains.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "administratorCount": 1,
      "companyName": "IBM",
      "contactInfo": null,
      "createdTime": 1719408628134,
      "description": null,
      "enable": true,
      "id": "6E70F043092E5BB93F74FD57C083F99E",
      "name": "Default"
    }
  ],
  "inputs": {},
  "metrics": {
    "execution_time_ms": 4283,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-15 08:30:19",
    "version": "1.0"
  },
  "raw": "[{\"id\": \"6E70F043092E5BB93F74FD57C083F99E\", \"name\": \"Default\", \"description\": null, \"createdTime\": 1719408628134, \"enable\": true, \"companyName\": \"IBM\", \"contactInfo\": null, \"administratorCount\": 1}]",
  "reason": null,
  "success": true,
  "version": "1.0"
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
None
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
fn_name = "fn_sep_get_domains"
wf_name = "Example: SEP - Get Groups information"
results = playbook.functions.results.get_domains_results
content = results.get("content", [])
domainid = None
for i in range(len(content)):
  if content[i].get("name") == playbook.inputs.sep_domain_name:
    domainid = content[i].get("id")
    break
if domainid:
  playbook.addProperty("domid_exists", {"exists": True})
else:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThe domain name <b>{1}</b> was not found " \
              "for SOAR function <b>{2}</b>.".format(wf_name, str(playbook.inputs.sep_domain_name), fn_name)
  incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Get Exceptions Policy
Get the exceptions policy for specified policy id.

 ![screenshot: fn-sep---get-exceptions-policy ](./doc/screenshots/fn-sep---get-exceptions-policy.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_exceptions_id` | `text` | Yes | `-` | The ID of the exceptions policy to get |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "configuration": {
      "applications": [],
      "applications_to_monitor": [
        {
          "name": "net.exe",
          "rulestate": {
            "enabled": true
          }
        }
      ],
      "blacklistrules": [],
      "certificates": [],
      "directories": [],
      "dns_and_host_applications": [],
      "dns_and_host_blacklistrules": [],
      "extension_list": null,
      "files": [],
      "knownrisks": [],
      "linux": {
        "directories": [],
        "extension_list": null
      },
      "mac": {
        "files": []
      },
      "non_pe_rules": [],
      "tamper_files": [],
      "webdomains": []
    },
    "desc": "Created automatically during product installation.",
    "enabled": true,
    "lastmodifiedtime": 1720451135816,
    "lockedoptions": {
      "application": true,
      "certificate": true,
      "dnshostfile": true,
      "domain": true,
      "extension": true,
      "file": true,
      "knownrisk": true,
      "securityrisk": false,
      "sonar": true
    },
    "name": "Exceptions policy",
    "sources": []
  },
  "inputs": {
    "sep_exceptions_id": "523B0176092E5BB97F83814D1657F3A4"
  },
  "metrics": {
    "execution_time_ms": 1294,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-10 10:45:19",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.sep_exceptions_id = playbook.inputs.sep_exceptions_id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from json import dumps

results = playbook.functions.results.get_exceptions_policy_results
if not results.get("success"):
  incident.addNote(f"SEP Exceptions Policy {playbook.inputs.sep_exceptions_id} error. Reason: {results.get('reason')}")
else:
  incident.addNote(f"SEP Exceptions Policy: {playbook.inputs.sep_exceptions_id}\n\n{dumps(results.get('content'), indent=4)}")
```

</p>
</details>

---
## Function - SEP - Get File Content as Base64
Get contents of a file uploaded to SEPM server as a Base64 string for a given file ID.

 ![screenshot: fn-sep---get-file-content-as-base64 ](./doc/screenshots/fn-sep---get-file-content-as-base64.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_file_id` | `text` | No | `-` | The file ID from which to get detailed information. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": "WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCo=",
  "inputs": {
    "sep_file_id": "A5E2EE53092E5BB91EBE5413EE47C386"
  },
  "metrics": {
    "execution_time_ms": 1098,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-29 10:04:04",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.sep_file_id = row.file_id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_get_file_content_as_base64 ##
# Globals
DATA_TBL_FIELDS = []
FN_NAME = "fn_sep_get_file_content_as_base64"
WF_NAME = "Get File Content as Base64 string"
# List of fields in datatable fn_amp_get_computers script
DATA_TBL_FIELDS = []
results = playbook.functions.results.get_file_content_as_base65_results
CONTENT = results.get("content")
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

# Processing
note_text = ''
if CONTENT:
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nReturned Base64 string of size <b>{1}</b> returned " \
                "for SOAR function <b>{2}</b>".format(WF_NAME, len(CONTENT), FN_NAME)
else:
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere was <b>no</b> result returned for " \
                "SOAR function <b>{1}</b>".format(WF_NAME, FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Get Fingerprint List
Get the fingerprint list information for a specified name or id.

 ![screenshot: fn-sep---get-fingerprint-list ](./doc/screenshots/fn-sep---get-fingerprint-list.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_domainid` | `text` | No | `-` | The SEPM domain id. |
| `sep_fingerprintlist_id` | `text` | No | `-` | Id of SEP fingerprint list |
| `sep_fingerprintlist_name` | `text` | No | `-` | Name of a SEP fingerprint list. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "appErrorCode": "",
    "errorCode": "410",
    "errorMessage": "Fingerprint list with ID Blacklist2 do not exist"
  },
  "inputs": {
    "sep_domainid": "6E70F043092E5BB93F74FD57C083F99E",
    "sep_fingerprintlist_name": "Blacklist2"
  },
  "metrics": {
    "execution_time_ms": 995,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-15 08:30:24",
    "version": "1.0"
  },
  "raw": "{\"errorCode\": \"410\", \"appErrorCode\": \"\", \"errorMessage\": \"Fingerprint list with ID Blacklist2 do not exist\"}",
  "reason": null,
  "success": true,
  "version": "1.0"
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
domain_content = playbook.functions.results.get_domains_results.get("content", [])

for i in range(len(domain_content)):
  if domain_content[i].get("name") == playbook.inputs.sep_domain_name:
    inputs.sep_domainid = domain_content[i].get("id")
    break

inputs.sep_fingerprintlist_name = playbook.inputs.sep_fingerprintlist_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_get_fingerprint_list script ##
# Globals
# List of fields in datatable fn_sep_get_fingerprint_list script
DATA_TBL_FIELDS = ["domain_name", "list_name", "list_id", "list_description", "hash_values", "hash_type", "group_ids"]
WF_NAME = "Add Hash to Fingerprint List"
results = playbook.functions.results.get_fingerprintlist_results
CONTENT = results.get("content")
INPUTS = results.get("inputs")
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

# Processing
fpl_exists = hash_in_list = False
note_text = ''
if CONTENT:
  if CONTENT.get("errorCode") and int(CONTENT.get("errorCode")) == 410:
    # The finger print list doesn't already exist.
    pass
  elif CONTENT.get("data"):
    # The finger print list exists set flag for gateway.
    fpl_exists = True
    playbook.addProperty("fpl_exists", {"exists": True})
  if CONTENT.get("data"):
    # Check if data is in new format. A list of dictionaries
    if isinstance(CONTENT.get("data", [])[0], dict):
      if artifact.value.upper() in [h.upper() for d in CONTENT.get("data") for h in d]:
        # Finger print list exists and hash in list set flag for hash in list.
        hash_in_list = True
    else:
      if artifact.value.upper() in [d.upper() for d in CONTENT.get("data")]:
        # Finger print list exists and hash in list set flag for hash in list.
        hash_in_list = True
    if hash_in_list:
      playbook.addProperty("hash_in_list", {"hash_in_list": True})

if fpl_exists and hash_in_list:
  note_text = f"""Symantec SEP Integration:
                  playbook <b>{WF_NAME}</b>:
                  The hash <b>{artifact.value}</b> has already been added to fingerprint list <b>{INPUTS.get('sep_fingerprintlist_name')}</b> for domain id <b>{INPUTS.get('sep_domainid')}</b>."""
  incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Get Firewall Policy
Get the firewall policy for specified policy id.

 ![screenshot: fn-sep---get-firewall-policy ](./doc/screenshots/fn-sep---get-firewall-policy.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_firewall_id` | `text` | Yes | `-` | The ID of the firewall policy to get. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "configuration": {
      "antiIP_spoofing": false,
      "antimac_spoofing": false,
      "autoblock": true,
      "autoblock_duration": 600,
      "baseline_rules": [
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 139
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 445
                }
              ],
              "protocol_ids": [
                6
              ]
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 137
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 138
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 139
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 445
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": [
            {
              "ip_range": {
                "ip_end": "10.255.255.255",
                "ip_start": "10.0.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "172.31.255.255",
                "ip_start": "172.16.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "192.168.255.255",
                "ip_start": "192.168.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "169.254.255.255",
                "ip_start": "169.254.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fc00::"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fe80::"
              },
              "location": "REMOTE"
            }
          ],
          "log_action": 0,
          "name": "Allow Local File Sharing to private IP addresses",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "69FF496F092E5BB94E898D1E4D224D28"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 139
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 445
                }
              ],
              "protocol_ids": [
                6
              ]
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 137
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 138
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 139
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 445
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 1,
          "name": "Block Local File Sharing",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "0F37D0BB092E5BB90B7A03EDE1B3DB2C"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 68
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 67
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow Bootp",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "98E6DD8D092E5BB94F3948010B0EEAC9"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "DST",
                  "start": 1900
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": [
            {
              "ip_range": {
                "ip_end": "10.255.255.255",
                "ip_start": "10.0.0.0"
              },
              "location": "SRC"
            },
            {
              "ip_range": {
                "ip_end": "172.31.255.255",
                "ip_start": "172.16.0.0"
              },
              "location": "SRC"
            },
            {
              "ip_range": {
                "ip_end": "192.168.255.255",
                "ip_start": "192.168.0.0"
              },
              "location": "SRC"
            },
            {
              "ip_range": {
                "ip_end": "169.254.255.255",
                "ip_start": "169.254.0.0"
              },
              "location": "SRC"
            },
            {
              "ip_range": {
                "ip_end": "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fc00::"
              },
              "location": "SRC"
            },
            {
              "ip_range": {
                "ip_end": "febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fe80::"
              },
              "location": "SRC"
            }
          ],
          "log_action": 0,
          "name": "Allow UPnP Discovery from private IP addresses",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "0E2B7C47092E5BB97B9071E9F20B71B5"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 1900
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 1,
          "name": "Block UPnP Discovery",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "0BC3E9F0092E5BB9669E0FD237C8578E"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5357
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5358
                }
              ],
              "protocol_ids": [
                6
              ]
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5357
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5358
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": [
            {
              "ip_range": {
                "ip_end": "10.255.255.255",
                "ip_start": "10.0.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "172.31.255.255",
                "ip_start": "172.16.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "192.168.255.255",
                "ip_start": "192.168.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "169.254.255.255",
                "ip_start": "169.254.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fc00::"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fe80::"
              },
              "location": "REMOTE"
            }
          ],
          "log_action": 0,
          "name": "Allow Web Service requests from private IP addresses",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "A6037EFE092E5BB936343F3A4F976490"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5357
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5358
                }
              ],
              "protocol_ids": [
                6
              ]
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5357
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5358
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 1,
          "name": "Block Web Service requests",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "D0B6ED57092E5BB92AD7E416CEC5B38E"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5355
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": [
            {
              "ip_range": {
                "ip_end": "10.255.255.255",
                "ip_start": "10.0.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "172.31.255.255",
                "ip_start": "172.16.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "192.168.255.255",
                "ip_start": "192.168.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "169.254.255.255",
                "ip_start": "169.254.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fc00::"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fe80::"
              },
              "location": "REMOTE"
            }
          ],
          "log_action": 0,
          "name": "Allow LLMNR from private IP addresses",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "E232F5CA092E5BB9101039267C0E0589"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5355
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": [
            {
              "ip_range": {
                "ip_end": "255.255.255.255",
                "ip_start": "0.0.0.1"
              },
              "location": "REMOTE"
            }
          ],
          "log_action": 1,
          "name": "Block LLMNR",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "F39698A8092E5BB9465A33C08E4E132B"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5355
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow LLMNR from ipv6 traffic",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "989BB854092E5BB93FABBA6EDC80EC8E"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 3702
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": [
            {
              "ip_range": {
                "ip_end": "10.255.255.255",
                "ip_start": "10.0.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "172.31.255.255",
                "ip_start": "172.16.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "192.168.255.255",
                "ip_start": "192.168.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "169.254.255.255",
                "ip_start": "169.254.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fc00::"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fe80::"
              },
              "location": "REMOTE"
            }
          ],
          "log_action": 0,
          "name": "Allow Web Services Discovery from private IP addresses",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "EAD641B3092E5BB932821F06F1DF3BC0"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 3702
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 1,
          "name": "Block Web Services Discovery",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "D2A71E10092E5BB9148778DE794E7D5B"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 2869
                }
              ],
              "protocol_ids": [
                6
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": [
            {
              "ip_range": {
                "ip_end": "10.255.255.255",
                "ip_start": "10.0.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "172.31.255.255",
                "ip_start": "172.16.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "192.168.255.255",
                "ip_start": "192.168.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "169.254.255.255",
                "ip_start": "169.254.0.0"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fc00::"
              },
              "location": "REMOTE"
            },
            {
              "ip_range": {
                "ip_end": "febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "ip_start": "fe80::"
              },
              "location": "REMOTE"
            }
          ],
          "log_action": 0,
          "name": "Allow SSDP from private IP addresses",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "7D3F9127092E5BB9266A3276D4C51F7F"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 2869
                }
              ],
              "protocol_ids": [
                6
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 1,
          "name": "Block SSDP",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "39230892092E5BB957AF518273836C33"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 1,
              "enabled": true,
              "icmp_types": [
                0
              ],
              "protocol_ids": [
                1
              ]
            },
            {
              "direction_id": 0,
              "enabled": true,
              "icmp_types": [
                8
              ],
              "protocol_ids": [
                1
              ]
            },
            {
              "direction_id": 1,
              "enabled": true,
              "icmp_types": [
                11
              ],
              "protocol_ids": [
                1
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow ping, pong and tracert",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "73E8BCB4092E5BB938013D7530FA8804"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": [
            {
              "name": "*"
            }
          ],
          "connections": null,
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow all applications",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "E30F6208092E5BB96C448A07BA9C4A95"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 2,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 1723
                }
              ],
              "protocol_ids": [
                6
              ],
              "svc_name": "VPN --- PPTP",
              "svc_uid": "C8013082092E5BB93CFA886C25C48A04"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 500
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 1701
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 4500
                }
              ],
              "protocol_ids": [
                17
              ],
              "svc_name": "VPN --- PPTP",
              "svc_uid": "C8013082092E5BB93CFA886C25C48A04"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": false,
              "protocol_ids": [
                47,
                50
              ],
              "svc_name": "VPN --- PPTP",
              "svc_uid": "C8013082092E5BB93CFA886C25C48A04"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 1032
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 1033
                }
              ],
              "protocol_ids": [
                6
              ],
              "svc_name": "VPN --- Check Point",
              "svc_uid": "FF34EE4A092E5BB92609F4E71C39D814"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 256
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 264
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 18231
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 18234
                }
              ],
              "protocol_ids": [
                6
              ],
              "svc_name": "VPN --- Check Point",
              "svc_uid": "FF34EE4A092E5BB92609F4E71C39D814"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 1266
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 1368
                }
              ],
              "protocol_ids": [
                17
              ],
              "svc_name": "VPN --- Check Point",
              "svc_uid": "FF34EE4A092E5BB92609F4E71C39D814"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 18231
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 18234
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 500
                }
              ],
              "protocol_ids": [
                17
              ],
              "svc_name": "VPN --- Check Point",
              "svc_uid": "FF34EE4A092E5BB92609F4E71C39D814"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": false,
              "protocol_ids": [
                50
              ],
              "svc_name": "VPN --- Check Point",
              "svc_uid": "FF34EE4A092E5BB92609F4E71C39D814"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": true,
              "protocol_ids": [
                17
              ],
              "svc_name": "VPN --- Check Point",
              "svc_uid": "FF34EE4A092E5BB92609F4E71C39D814"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 62516
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 500
                }
              ],
              "protocol_ids": [
                17
              ],
              "svc_name": "VPN --- NetScreen",
              "svc_uid": "5D7E9B38092E5BB968DCBE0FDFE2A339"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": false,
              "protocol_ids": [
                50
              ],
              "svc_name": "VPN --- NetScreen",
              "svc_uid": "5D7E9B38092E5BB968DCBE0FDFE2A339"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 1029
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 500
                }
              ],
              "protocol_ids": [
                17
              ],
              "svc_name": "VPN --- Cisco 5000",
              "svc_uid": "50F33FE0092E5BB95DA9DB7BFD3A2E41"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": false,
              "protocol_ids": [
                50
              ],
              "svc_name": "VPN --- Cisco 5000",
              "svc_uid": "50F33FE0092E5BB95DA9DB7BFD3A2E41"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 500
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 10000
                },
                {
                  "end": 62524,
                  "location": "REMOTE",
                  "start": 62514
                }
              ],
              "protocol_ids": [
                17
              ],
              "svc_name": "VPN --- Cisco 3000",
              "svc_uid": "EF3159B9092E5BB94CDFCE3DB8806921"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": false,
              "protocol_ids": [
                50
              ],
              "svc_name": "VPN --- Cisco 3000",
              "svc_uid": "EF3159B9092E5BB94CDFCE3DB8806921"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 8282
                }
              ],
              "protocol_ids": [
                6
              ],
              "svc_name": "VPN --- Nortel",
              "svc_uid": "B8C0FD37092E5BB96C6760F6E662A23D"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 17
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 586
                }
              ],
              "protocol_ids": [
                6
              ],
              "svc_name": "VPN --- Nortel",
              "svc_uid": "B8C0FD37092E5BB96C6760F6E662A23D"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 500
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 8121
                }
              ],
              "protocol_ids": [
                17
              ],
              "svc_name": "VPN --- Nortel",
              "svc_uid": "B8C0FD37092E5BB96C6760F6E662A23D"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": false,
              "protocol_ids": [
                50
              ],
              "svc_name": "VPN --- Nortel",
              "svc_uid": "B8C0FD37092E5BB96C6760F6E662A23D"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 443
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 1080
                }
              ],
              "protocol_ids": [
                6
              ],
              "svc_name": "VPN --- Aventail",
              "svc_uid": "5A6BBF37092E5BB924BD0656C5EDC154"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": false,
              "protocol_ids": [
                50
              ],
              "svc_name": "VPN --- Aventail",
              "svc_uid": "5A6BBF37092E5BB924BD0656C5EDC154"
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow VPN",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 4,
          "time_slots": null,
          "uid": "ADB2292C092E5BB93065667F4A40BFF9"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ether_type_id": 51966
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow Veritas Protocol",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 4,
          "time_slots": null,
          "uid": "E7E47214092E5BB92AB2B3A0E2776740"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": false,
              "protocol_ids": [
                2
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow IGMP traffic",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 4,
          "time_slots": null,
          "uid": "E764F25C092E5BB90FF2A93E70D04A8C"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 5353
                }
              ],
              "protocol_ids": [
                17
              ]
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 5353
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow Bonjour traffic",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "65AFBD1C092E5BB9643C123950557886"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": null,
          "desc": null,
          "email_alert": false,
          "hosts": [
            {
              "location": "LOCAL",
              "mac": "FF-FF-FF-FF-FF-FF"
            },
            {
              "ip_range": {
                "ip_end": "239.255.255.255",
                "ip_start": "224.0.0.0"
              },
              "location": "LOCAL"
            }
          ],
          "log_action": 0,
          "name": "Block broadcast and multicast traffic and don\u0027t log",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 1,
          "time_slots": null,
          "uid": "6A35F99F092E5BB95DDD5B2960C09319"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": false
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 1,
          "name": "Block all other IP traffic and log",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 1,
          "time_slots": null,
          "uid": "0B2AE82F092E5BB978629101355BF16B"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": null,
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Block all other traffic and don\u0027t log",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 1,
          "time_slots": null,
          "uid": "604C4BAA092E5BB9343DAC446707079F"
        }
      ],
      "dos": false,
      "endpoint_notification": {
        "ask_enabled": false,
        "enabled": false,
        "endpoint_notification_ask_message": null,
        "endpoint_notification_message": null
      },
      "enforced_rules": [
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ether_type_id": 34525
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Block IPv6",
          "packet_capture": false,
          "rulestate": {
            "enabled": false
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "AF6C0B7F092E5BB90F1F6AAAA6A9091C"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 3544
                }
              ],
              "protocol_ids": [
                17
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Block IPv6 over IPv4 (Teredo)",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "93B197B4092E5BB97B99073C27A4A7FB"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": false,
              "protocol_ids": [
                41
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Block IPv6 over IPv4 (ISATAP)",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "C15FF9A5092E5BB903C0D2ECA39FB09D"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "icmp_code_ranges": [
                {
                  "end": 4,
                  "start": 1
                },
                {
                  "end": 132,
                  "start": 128
                },
                {
                  "end": 143,
                  "start": 141
                },
                {
                  "end": 153,
                  "start": 151
                }
              ],
              "icmp_codes": [
                135,
                136,
                148,
                149
              ],
              "icmp_type_ranges": [
                {
                  "end": 4,
                  "start": 1
                },
                {
                  "end": 132,
                  "start": 128
                },
                {
                  "end": 143,
                  "start": 141
                },
                {
                  "end": 153,
                  "start": 151
                }
              ],
              "icmp_types": [
                135,
                136,
                148,
                149
              ],
              "protocol_ids": [
                58
              ]
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow ICMPv6",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "3FA24409092E5BB9047C4962ECE67CBF"
        },
        {
          "action": "BLOCK",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 161
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 162
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 10161
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 10162
                }
              ],
              "protocol_ids": [
                6
              ],
              "svc_name": "SNMP Management",
              "svc_uid": "CE856BE3092E5BB95C42D34F3BD620DD"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 161
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 162
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 10161
                },
                {
                  "end": null,
                  "location": "REMOTE",
                  "start": 10162
                }
              ],
              "protocol_ids": [
                17
              ],
              "svc_name": "SNMP Management",
              "svc_uid": "CE856BE3092E5BB95C42D34F3BD620DD"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 161
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 162
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 10161
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 10162
                }
              ],
              "protocol_ids": [
                6
              ],
              "svc_name": "SNMP Client",
              "svc_uid": "EF333F34092E5BB96FBAC8682039FA34"
            },
            {
              "direction_id": 0,
              "enabled": true,
              "ports": [
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 161
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 162
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 10161
                },
                {
                  "end": null,
                  "location": "LOCAL",
                  "start": 10162
                }
              ],
              "protocol_ids": [
                17
              ],
              "svc_name": "SNMP Client",
              "svc_uid": "EF333F34092E5BB96FBAC8682039FA34"
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Block SNMP",
          "packet_capture": false,
          "rulestate": {
            "enabled": false
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "06DBD8D4092E5BB95C50F9F0BD7C1EBD"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ip_fragmented_only": true
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow fragmented packets",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "033A04EE092E5BB9145E670ACDEA46E7"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ether_type_id": 34958
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow wireless EAPOL",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "D6C2BB7E092E5BB9439171F2482999EF"
        },
        {
          "action": "ALLOW",
          "adapters": [
            {
              "enabled": true,
              "name": "All Adapters",
              "type": "ANY",
              "uid": "88FCC040092E5BB930FDDC8EEE3946B6"
            }
          ],
          "applications": null,
          "connections": [
            {
              "direction_id": 0,
              "enabled": true,
              "ether_type_id": 35118
            }
          ],
          "desc": null,
          "email_alert": false,
          "hosts": null,
          "log_action": 0,
          "name": "Allow USB over IEEE802",
          "packet_capture": false,
          "rulestate": {
            "enabled": true
          },
          "screen_saver": "ANY",
          "severity": 3,
          "time_slots": null,
          "uid": "0EBEEDC5092E5BB94D53BF4F111AC78C"
        }
      ],
      "hide_os": false,
      "ignore_parent_rules": null,
      "mac": {
        "antimac_spoofing": false,
        "autoblock": true,
        "autoblock_duration": 600,
        "baseline_rules": [
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 137
                  },
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 138
                  }
                ],
                "protocol_ids": [
                  17
                ]
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 20
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 21
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 22
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 139
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 445
                  }
                ],
                "protocol_ids": [
                  6
                ]
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 137
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 138
                  }
                ],
                "protocol_ids": [
                  17
                ]
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 445
                  },
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 548
                  }
                ],
                "protocol_ids": [
                  6
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": [
              {
                "ip_range": {
                  "ip_end": "10.255.255.255",
                  "ip_start": "10.0.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "172.31.255.255",
                  "ip_start": "172.16.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "192.168.255.255",
                  "ip_start": "192.168.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "169.254.255.255",
                  "ip_start": "169.254.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                  "ip_start": "fc00::"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                  "ip_start": "fe80::"
                },
                "location": "REMOTE"
              }
            ],
            "log_action": 0,
            "name": "Allow Local File Sharing to private IP addresses",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "53DACF1E092E5BB90D7BE4F2910F0F6A"
          },
          {
            "action": "BLOCK",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 445
                  }
                ],
                "protocol_ids": [
                  6
                ]
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 20
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 21
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 22
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 139
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 445
                  }
                ],
                "protocol_ids": [
                  6
                ]
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 137
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 138
                  }
                ],
                "protocol_ids": [
                  17
                ]
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 137
                  }
                ],
                "protocol_ids": [
                  17
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 1,
            "name": "Block Local File Sharing to external computers",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "77A01134092E5BB97F7828DF8D14642D"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 68
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 67
                  }
                ],
                "protocol_ids": [
                  17
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow Bootp",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "9507DAE4092E5BB9147007D3306BB8DC"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "DST",
                    "start": 1900
                  }
                ],
                "protocol_ids": [
                  17
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": [
              {
                "ip_range": {
                  "ip_end": "10.255.255.255",
                  "ip_start": "10.0.0.0"
                },
                "location": "SRC"
              },
              {
                "ip_range": {
                  "ip_end": "172.31.255.255",
                  "ip_start": "172.16.0.0"
                },
                "location": "SRC"
              },
              {
                "ip_range": {
                  "ip_end": "192.168.255.255",
                  "ip_start": "192.168.0.0"
                },
                "location": "SRC"
              },
              {
                "ip_range": {
                  "ip_end": "169.254.255.255",
                  "ip_start": "169.254.0.0"
                },
                "location": "SRC"
              },
              {
                "ip_range": {
                  "ip_end": "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                  "ip_start": "fc00::0"
                },
                "location": "SRC"
              },
              {
                "ip_range": {
                  "ip_end": "febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                  "ip_start": "fe80::0"
                },
                "location": "SRC"
              }
            ],
            "log_action": 0,
            "name": "Allow UPnP Discovery from private IP addresses",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "294E17C9092E5BB92AAFDCFC6AF01270"
          },
          {
            "action": "BLOCK",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 1900
                  }
                ],
                "protocol_ids": [
                  17
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 1,
            "name": "Block UPnP Discovery",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "05942D1E092E5BB96DD96AA5199D35BC"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 2869
                  }
                ],
                "protocol_ids": [
                  6
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": [
              {
                "ip_range": {
                  "ip_end": "10.255.255.255",
                  "ip_start": "10.0.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "172.31.255.255",
                  "ip_start": "172.16.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "192.168.255.255",
                  "ip_start": "192.168.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "169.254.255.255",
                  "ip_start": "169.254.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                  "ip_start": "fc00::0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                  "ip_start": "fe80::0"
                },
                "location": "REMOTE"
              }
            ],
            "log_action": 0,
            "name": "Allow SSDP from private IP addresses",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "F829FB4A092E5BB92B1F80E5388C0870"
          },
          {
            "action": "BLOCK",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 2869
                  }
                ],
                "protocol_ids": [
                  6
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 1,
            "name": "Block SSDP",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "DF25F540092E5BB962A1555998460F41"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 1,
                "enabled": true,
                "icmp_types": [
                  0
                ],
                "protocol_ids": [
                  1
                ]
              },
              {
                "direction_id": 0,
                "enabled": true,
                "icmp_types": [
                  8
                ],
                "protocol_ids": [
                  1
                ]
              },
              {
                "direction_id": 1,
                "enabled": true,
                "icmp_types": [
                  11
                ],
                "protocol_ids": [
                  1
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow ping, pong and tracert",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "19B6E398092E5BB96A30E07E951FE96B"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 62516
                  },
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 500
                  }
                ],
                "protocol_ids": [
                  17
                ],
                "svc_name": "VPN --- NetScreen",
                "svc_uid": "5D7E9B38092E5BB968DCBE0FDFE2A339"
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ip_fragmented_only": false,
                "protocol_ids": [
                  50
                ],
                "svc_name": "VPN --- NetScreen",
                "svc_uid": "5D7E9B38092E5BB968DCBE0FDFE2A339"
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 1029
                  },
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 500
                  }
                ],
                "protocol_ids": [
                  17
                ],
                "svc_name": "VPN --- Cisco 5000",
                "svc_uid": "50F33FE0092E5BB95DA9DB7BFD3A2E41"
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ip_fragmented_only": false,
                "protocol_ids": [
                  50
                ],
                "svc_name": "VPN --- Cisco 5000",
                "svc_uid": "50F33FE0092E5BB95DA9DB7BFD3A2E41"
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 500
                  },
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 10000
                  },
                  {
                    "end": 62524,
                    "location": "REMOTE",
                    "start": 62514
                  }
                ],
                "protocol_ids": [
                  17
                ],
                "svc_name": "VPN --- Cisco 3000",
                "svc_uid": "EF3159B9092E5BB94CDFCE3DB8806921"
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ip_fragmented_only": false,
                "protocol_ids": [
                  50
                ],
                "svc_name": "VPN --- Cisco 3000",
                "svc_uid": "EF3159B9092E5BB94CDFCE3DB8806921"
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 1723
                  }
                ],
                "protocol_ids": [
                  6
                ],
                "svc_name": "VPN --- OS X",
                "svc_uid": "7889F07C092E5BB96A66B39A1E88630C"
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 1723
                  }
                ],
                "protocol_ids": [
                  6
                ],
                "svc_name": "VPN --- OS X",
                "svc_uid": "7889F07C092E5BB96A66B39A1E88630C"
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 500
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 1701
                  },
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 4500
                  }
                ],
                "protocol_ids": [
                  17
                ],
                "svc_name": "VPN --- OS X",
                "svc_uid": "7889F07C092E5BB96A66B39A1E88630C"
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 500
                  },
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 1701
                  },
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 4500
                  }
                ],
                "protocol_ids": [
                  17
                ],
                "svc_name": "VPN --- OS X",
                "svc_uid": "7889F07C092E5BB96A66B39A1E88630C"
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow VPN",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 4,
            "time_slots": null,
            "uid": "16357E1D092E5BB95B84BECA70D06182"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ip_fragmented_only": false,
                "protocol_ids": [
                  2
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow IGMP traffic",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 4,
            "time_slots": null,
            "uid": "C0AFE420092E5BB91A59800472B588D8"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 2,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 80
                  },
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 443
                  }
                ],
                "protocol_ids": [
                  6
                ]
              },
              {
                "direction_id": 2,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 80
                  },
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 443
                  }
                ],
                "protocol_ids": [
                  17
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow outgoing web traffic",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 4,
            "time_slots": null,
            "uid": "8A7C6BF0092E5BB97C19F9DF273312A7"
          },
          {
            "action": "BLOCK",
            "adapters": null,
            "applications": null,
            "connections": null,
            "desc": null,
            "email_alert": false,
            "hosts": [
              {
                "ip": "255.255.255.255",
                "location": "LOCAL"
              },
              {
                "ip_range": {
                  "ip_end": "239.255.255.255",
                  "ip_start": "224.0.0.0"
                },
                "location": "LOCAL"
              }
            ],
            "log_action": 0,
            "name": "Block broadcast and multicast traffic and don\u0027t log",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 1,
            "time_slots": null,
            "uid": "884D30DA092E5BB930DC6EBC4A3E9B5B"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 192
                  }
                ],
                "protocol_ids": [
                  17
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow Airport",
            "packet_capture": false,
            "rulestate": {
              "enabled": false
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "5D857B08092E5BB9744D3BD774298986"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 88
                  }
                ],
                "protocol_ids": [
                  17
                ]
              },
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 88
                  }
                ],
                "protocol_ids": [
                  6
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow Kerberos",
            "packet_capture": false,
            "rulestate": {
              "enabled": false
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "711DC180092E5BB959A6ACFC5861CEAB"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 2,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 10443
                  }
                ],
                "protocol_ids": [
                  6
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow outgoing DLP",
            "packet_capture": false,
            "rulestate": {
              "enabled": false
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "63475044092E5BB970FE9EACAB21EFB1"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 2,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 3283
                  }
                ],
                "protocol_ids": [
                  6
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow outgoing RDP",
            "packet_capture": false,
            "rulestate": {
              "enabled": false
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "109E0CD9092E5BB9566624F7E9BF266F"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 2,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 8443
                  }
                ],
                "protocol_ids": [
                  6
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": [
              {
                "ip_range": {
                  "ip_end": "10.255.255.255",
                  "ip_start": "10.0.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "172.31.255.255",
                  "ip_start": "172.16.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "192.168.255.255",
                  "ip_start": "192.168.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "169.254.255.255",
                  "ip_start": "169.254.0.0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                  "ip_start": "fc00::0"
                },
                "location": "REMOTE"
              },
              {
                "ip_range": {
                  "ip_end": "febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                  "ip_start": "fe80::0"
                },
                "location": "REMOTE"
              }
            ],
            "log_action": 0,
            "name": "Allow outgoing JAMF",
            "packet_capture": false,
            "rulestate": {
              "enabled": false
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "2F96536A092E5BB900FBB64BA54B9C2B"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 389
                  }
                ],
                "protocol_ids": [
                  6
                ]
              },
              {
                "direction_id": 2,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 3268
                  }
                ],
                "protocol_ids": [
                  6
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow LDAP",
            "packet_capture": false,
            "rulestate": {
              "enabled": false
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "E3F78964092E5BB92FE6B57EC76E8C07"
          },
          {
            "action": "BLOCK",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ip_fragmented_only": false
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 1,
            "name": "Block all other IP traffic and log",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 1,
            "time_slots": null,
            "uid": "45488FD5092E5BB9045BBC3330D499EA"
          }
        ],
        "dos": false,
        "endpoint_notification": {
          "ask_enabled": null,
          "enabled": false,
          "endpoint_notification_ask_message": null,
          "endpoint_notification_message": null
        },
        "enforced_rules": [
          {
            "action": "BLOCK",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 3544
                  }
                ],
                "protocol_ids": [
                  17
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Block IPv6 over IPv4 (Teredo)",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "A7132944092E5BB91799542349877DC4"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "icmp_code_ranges": [
                  {
                    "end": 4,
                    "start": 1
                  },
                  {
                    "end": 132,
                    "start": 128
                  },
                  {
                    "end": 143,
                    "start": 141
                  },
                  {
                    "end": 153,
                    "start": 151
                  }
                ],
                "icmp_codes": [
                  135,
                  136,
                  148,
                  149
                ],
                "icmp_type_ranges": [
                  {
                    "end": 4,
                    "start": 1
                  },
                  {
                    "end": 132,
                    "start": 128
                  },
                  {
                    "end": 143,
                    "start": 141
                  },
                  {
                    "end": 153,
                    "start": 151
                  }
                ],
                "icmp_types": [
                  135,
                  136,
                  148,
                  149
                ],
                "protocol_ids": [
                  58
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow ICMPv6",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "438C14D8092E5BB93B8797FC3D2836C4"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 5353
                  }
                ],
                "protocol_ids": [
                  17
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": [
              {
                "ip_range": {
                  "ip_end": "239.255.255.255",
                  "ip_start": "224.0.0.0"
                },
                "location": "DST"
              },
              {
                "ipv6_subnet": "FF00::/12",
                "location": "DST"
              }
            ],
            "log_action": 0,
            "name": "Allow Mac Discovery from local computers",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "AB6FDFDC092E5BB9493E327E03CFE785"
          },
          {
            "action": "BLOCK",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 0,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "LOCAL",
                    "start": 5353
                  }
                ],
                "protocol_ids": [
                  17
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 1,
            "name": "Block Mac Discovery from external computers",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "6EBCC33E092E5BB968E1C4FF9C750796"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 2,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 1900
                  }
                ],
                "protocol_ids": [
                  17
                ]
              },
              {
                "direction_id": 2,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 5223
                  }
                ],
                "protocol_ids": [
                  6
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow outgoing ichat requests",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "7212F8B4092E5BB9415DE41EB43D4459"
          },
          {
            "action": "ALLOW",
            "adapters": null,
            "applications": null,
            "connections": [
              {
                "direction_id": 2,
                "enabled": true,
                "ports": [
                  {
                    "end": null,
                    "location": "REMOTE",
                    "start": 123
                  }
                ],
                "protocol_ids": [
                  17
                ]
              }
            ],
            "desc": null,
            "email_alert": false,
            "hosts": null,
            "log_action": 0,
            "name": "Allow outgoing NTP requests",
            "packet_capture": false,
            "rulestate": {
              "enabled": true
            },
            "screen_saver": "ANY",
            "severity": 3,
            "time_slots": null,
            "uid": "94238995092E5BB9278B654265950A7E"
          }
        ],
        "ignore_parent_rules": null,
        "port_scan": true,
        "smart_dhcp": true,
        "smart_dns": true
      },
      "netbios_protection": false,
      "p2p_auth": {
        "enabled": false,
        "excludeHosts": null,
        "hosts": null,
        "max_auth_attempts": null,
        "session_timeout": null,
        "time_before_re_auth": null,
        "time_between_auth_attempts": null,
        "time_for_remote_blocked": null
      },
      "port_scan": true,
      "reverse_dns": false,
      "smart_dhcp": true,
      "smart_dns": true,
      "smart_wins": true,
      "stealth_web": false,
      "token_ring_traffic": false,
      "windows_firewall": "DISABLE_ONCE",
      "windows_firewall_notification": false
    },
    "desc": "Created automatically during product installation.",
    "enabled": true,
    "lastmodifiedtime": 1719408684497,
    "name": "Firewall policy",
    "sources": null
  },
  "inputs": {
    "sep_firewall_id": "7231E523092E5BB93F329A371754A877"
  },
  "metrics": {
    "execution_time_ms": 1791,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-10 10:46:04",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.sep_firewall_id = playbook.inputs.sep_firewall_id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from json import dumps
results = playbook.functions.results.get_firewall_policy_results

if not results.get("success"):
  incident.addNote(f"SEP Firewall Policy {playbook.inputs.sep_firewall_id} error. Reason: {results.get('reason')}")
else:
  incident.addNote(f"SEP Firewall Policy: {playbook.inputs.sep_firewall_id}\n\n{dumps(results.get('content'), indent=4)}")
```

</p>
</details>

---
## Function - SEP - Get Groups
Get properties of all groups in a domain.

 ![screenshot: fn-sep---get-groups ](./doc/screenshots/fn-sep---get-groups.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_domain` | `text` | No | `-` | The SEPM domain. |
| `sep_fullpathname` | `text` | No | `-` | The full path name of the group. |
| `sep_mode` | `text` | No | `-` | The presentation mode for the results, as a list (default) or as a tree. |
| `sep_order` | `text` | No | `-` | Specifies whether the results are in ascending order (ASC) or descending order (DESC). |
| `sep_pageindex` | `number` | No | `-` | The index page that is used for the returned results. The default page index is 1. |
| `sep_pagesize` | `number` | No | `-` | The number of results to include on each page. The default is 20. |
| `sep_sort` | `text` | No | `-` | The column by which the results are sorted. Possible values are COMPUTER_NAME (Default value), COMPUTER_ID, COMPUTER_DOMAIN_NAME, or DOMAIN_ID. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "content": [
      {
        "created": 1719408628197,
        "createdBy": "AF3C39A10A320801000000DBF200C60A                                                                                                ",
        "customIpsNumber": "",
        "description": "",
        "domain": {
          "id": "6E70F043092E5BB93F74FD57C083F99E",
          "name": null
        },
        "fullPathName": "My Company\\Default Group",
        "id": "23899461092E5BB937223FCF3A0605E3",
        "lastModified": 1719408628197,
        "name": "Default Group",
        "numberOfPhysicalComputers": 1,
        "numberOfRegisteredUsers": 1,
        "policyDate": 1720506552652,
        "policyInheritanceEnabled": true,
        "policySerialNumber": "2389-07/09/2024 06:29:12 652"
      }
    ],
    "firstPage": true,
    "lastPage": true,
    "number": 0,
    "numberOfElements": 1,
    "size": 25,
    "sort": [
      {
        "ascending": true,
        "direction": "ASC",
        "property": "NAME"
      }
    ],
    "totalElements": 1,
    "totalPages": 1
  },
  "inputs": {
    "sep_domain": "6E70F043092E5BB93F74FD57C083F99E",
    "sep_fullpathname": "My Company\\Default Group"
  },
  "metrics": {
    "execution_time_ms": 1180,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-18 10:48:52",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
domain_content = playbook.functions.results.get_domains_results.get("content", [])

for i in range(len(domain_content)):
  if domain_content[i]["name"] ==  playbook.inputs.sep_domain_name:
    inputs.sep_domain = domain_content[i]["id"]
    break
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_get_groups script ##
# Globals
FN_NAME = "fn_symc_sep_get_groups"
WF_NAME = "Get Groups information"
results = playbook.functions.results.get_groups_results
C_OUTER = results.get("content", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")
DOMAIN_NAME = playbook.inputs.sep_domain_name

# Processing
note_text = ''
if C_OUTER is not None:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>{1}</b> results returned for domain " \
              "<b>{2}</b> for SOAR function <b>{3}</b>"\
      .format(WF_NAME, results.get("content", {}).get("numberOfElements"), DOMAIN_NAME, FN_NAME)
  groups = C_OUTER.get("content")
  for i in range(len(groups)):
    newrow = incident.addRow("sep_groups")
    newrow["query_execution_date"] = QUERY_EXECUTION_DATE
    newrow["group_name"] = groups[i].get("name")
    newrow["group_id"] = groups[i].get("id")
    newrow["group_description"] = groups[i].get("description")
    newrow["fullPathName"] = groups[i].get("fullPathName")
    newrow["numberOfPhysicalComputers"] = groups[i].get("numberOfPhysicalComputers")
    newrow["policyInheritanceEnabled"] = groups[i].get("policyInheritanceEnabled")

    domain = groups[i].get("domain")
    if domain:
      newrow["domain_name"] = domain.get("name")
      newrow["domain_id"] = domain.get("id")

else:
  note_text += "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> results returned for domain " \
               "<b>{1}</b>for SOAR function <b>{2}</b>".format(WF_NAME, DOMAIN_NAME, FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Get Policy Summary
Get the summary information for policies within a specific Domain. Also gets the list of groups to which the policies are assigned.

 ![screenshot: fn-sep---get-policy-summary ](./doc/screenshots/fn-sep---get-policy-summary.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_domainid` | `text` | No | `-` | The SEPM domain id. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "content": [
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": [
          {
            "defaultLocationId": "8E451D96092E5BB94D06F6F216972F1C",
            "groupId": "52BBA2A9092E5BB94DC766C08B9D6354",
            "locationIds": [
              "8E451D96092E5BB94D06F6F216972F1C"
            ]
          }
        ],
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": false,
        "id": "3418C720092E5BB96B7E42AD3BE5D55F",
        "lastmodifiedtime": 1719408684510,
        "name": "Intensive Protection policy",
        "policytype": "hid",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": [
          {
            "defaultLocationId": "8E451D96092E5BB94D06F6F216972F1C",
            "groupId": "52BBA2A9092E5BB94DC766C08B9D6354",
            "locationIds": [
              "8E451D96092E5BB94D06F6F216972F1C"
            ]
          }
        ],
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "523B0176092E5BB97F83814D1657F3A4",
        "lastmodifiedtime": 1720451135816,
        "name": "Exceptions policy",
        "policytype": "exceptions",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": [
          {
            "defaultLocationId": "8E451D96092E5BB94D06F6F216972F1C",
            "groupId": "52BBA2A9092E5BB94DC766C08B9D6354",
            "locationIds": [
              "8E451D96092E5BB94D06F6F216972F1C"
            ]
          }
        ],
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "F12FDA6C092E5BB951DF7579239EF18B",
        "lastmodifiedtime": 1719408684432,
        "name": "Memory Exploit Mitigation policy",
        "policytype": "mem",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": [
          {
            "defaultLocationId": "8E451D96092E5BB94D06F6F216972F1C",
            "groupId": "52BBA2A9092E5BB94DC766C08B9D6354",
            "locationIds": [
              "8E451D96092E5BB94D06F6F216972F1C"
            ]
          }
        ],
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "4E48B231092E5BB94B04E043AC98C412",
        "lastmodifiedtime": 1719408684432,
        "name": "Web and Cloud Access Protection policy",
        "policytype": "ntr",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": [
          {
            "defaultLocationId": "8E451D96092E5BB94D06F6F216972F1C",
            "groupId": "52BBA2A9092E5BB94DC766C08B9D6354",
            "locationIds": [
              "8E451D96092E5BB94D06F6F216972F1C"
            ]
          }
        ],
        "desc": "Recommended policy for most environments, providing a good balance between security and performance. Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "39A014CA092E5BB96712B9382E078D95",
        "lastmodifiedtime": 1719408684535,
        "name": "Virus and Spyware Protection policy - Balanced",
        "policytype": "av",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": null,
        "desc": "High security policy that may affect the performance of other applications. Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "0C512A3A092E5BB947C433BCF26DEA2E",
        "lastmodifiedtime": 1719408684567,
        "name": "Virus and Spyware Protection policy - High Security",
        "policytype": "av",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": null,
        "desc": "Higher performance policy, but with reduced security. Relies on Auto-Protect scanning of files with selected extensions for most detections. One monthly scheduled scan and no email scanning. Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "1FF0FECA092E5BB95E6EFB78588BD500",
        "lastmodifiedtime": 1719408684587,
        "name": "Virus and Spyware Protection policy - High Performance",
        "policytype": "av",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": [
          {
            "defaultLocationId": "8E451D96092E5BB94D06F6F216972F1C",
            "groupId": "52BBA2A9092E5BB94DC766C08B9D6354",
            "locationIds": [
              "8E451D96092E5BB94D06F6F216972F1C"
            ]
          }
        ],
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "7231E523092E5BB93F329A371754A877",
        "lastmodifiedtime": 1719408684497,
        "name": "Firewall policy",
        "policytype": "fw",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": null,
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "F23A143E092E5BB9729D4A06F126B084",
        "lastmodifiedtime": 1719408684497,
        "name": "Quarantine Firewall policy",
        "policytype": "fw",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": [
          {
            "defaultLocationId": "8E451D96092E5BB94D06F6F216972F1C",
            "groupId": "52BBA2A9092E5BB94DC766C08B9D6354",
            "locationIds": [
              "8E451D96092E5BB94D06F6F216972F1C"
            ]
          }
        ],
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "79B840A5092E5BB915D114AB2C0EA950",
        "lastmodifiedtime": 1719408684432,
        "name": "Intrusion Prevention policy",
        "policytype": "ips",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": null,
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "52AD1F3F092E5BB927116FA915BBBDBF",
        "lastmodifiedtime": 1719408684638,
        "name": "LiveUpdate Content policy",
        "policytype": "lucontent",
        "sources": null,
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": [
          {
            "defaultLocationId": "8E451D96092E5BB94D06F6F216972F1C",
            "groupId": "52BBA2A9092E5BB94DC766C08B9D6354",
            "locationIds": [
              "8E451D96092E5BB94D06F6F216972F1C"
            ]
          }
        ],
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "ECD7CDCD092E5BB93DE49DE84E475BFA",
        "lastmodifiedtime": 1719408684636,
        "name": "LiveUpdate Settings policy",
        "policytype": "lu",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": null,
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "523E53EC092E5BB90A16A700DAEEBE85",
        "lastmodifiedtime": 1719408684510,
        "name": "Host Integrity policy",
        "policytype": "hi",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": [
          {
            "defaultLocationId": "8E451D96092E5BB94D06F6F216972F1C",
            "groupId": "52BBA2A9092E5BB94DC766C08B9D6354",
            "locationIds": [
              "8E451D96092E5BB94D06F6F216972F1C"
            ]
          }
        ],
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": true,
        "id": "4793B972092E5BB92E3450AD7023CD88",
        "lastmodifiedtime": 1719408684510,
        "name": "Application and Device Control policy",
        "policytype": "adc",
        "sources": [],
        "subtype": null
      },
      {
        "assignedtocloudgroups": null,
        "assignedtolocations": [
          {
            "defaultLocationId": "8E451D96092E5BB94D06F6F216972F1C",
            "groupId": "52BBA2A9092E5BB94DC766C08B9D6354",
            "locationIds": [
              "8E451D96092E5BB94D06F6F216972F1C"
            ]
          }
        ],
        "desc": "Created automatically during product installation.",
        "domainid": "6E70F043092E5BB93F74FD57C083F99E",
        "enabled": false,
        "id": "7C1FC997092E5BB90C24C0EA3BA7798A",
        "lastmodifiedtime": 1719408684497,
        "name": "Client Upgrade policy",
        "policytype": "upgrade",
        "sources": [],
        "subtype": null
      }
    ],
    "firstPage": true,
    "lastPage": true,
    "number": 0,
    "numberOfElements": 15,
    "size": 15,
    "sort": null,
    "totalElements": 15,
    "totalPages": 1
  },
  "inputs": {
    "sep_domainid": "6E70F043092E5BB93F74FD57C083F99E"
  },
  "metrics": {
    "execution_time_ms": 1100,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-10 10:42:05",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.sep_domainid = playbook.inputs.sep_domain_id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from json import dumps
results = playbook.functions.results.get_policy_summary_results

if not results.get("success"):
  incident.addNote(f"SEP Policy Summary for Domain: {playbook.inputs.sep_domain_id} error. Reason: {results.get('reason')}")
else:
  incident.addNote(f"Policy Summary for Domain: {playbook.inputs.sep_domain_id}\n\n{dumps(results.get('content'), indent=4)}")
```

</p>
</details>

---
## Function - SEP - Move endpoint
Check for and move an endpoint to a different group.

 ![screenshot: fn-sep---move-endpoint ](./doc/screenshots/fn-sep---move-endpoint.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_groupid` | `text` | No | `-` | Group id on which to run the SEP command. |
| `sep_hardwarekey` | `text` | No | `-` | Hardware key of SEP computer. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "responseCode": "200",
      "responseMessage": "OK"
    }
  ],
  "inputs": {
    "sep_groupid": "23899461092E5BB937223FCF3A0605E3",
    "sep_hardwarekey": "8DACE2559C1C951E09CC0BF71D973BB7"
  },
  "metrics": {
    "execution_time_ms": 883,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-18 10:48:55",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
content = playbook.functions.results.get_groups_results.get("content", {})
full_path_name = content.get("content", [])[0].get("fullPathName")
inputs.sep_hardwarekey = row.hardwareKey
inputs.sep_groupid = content.get("content", [])[0].get("id")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_move_client script ##
# List of fields in datatable fn_amp_get_computers script
FN_NAME = "fn_set_move_client"
WF_NAME = "Move Endpoint"
results = playbook.functions.results.move_endpoint_results
CONTENT = results.get("content", [])
HW_KEY = results.get("inputs", {}).get("sep_hardwarekey")
GROUP_ID = results.get("inputs", {}).get("sep_groupid")
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

note_text = ''
if CONTENT:
  response_msg = CONTENT[0].get("responseMessage")
  if response_msg == "OK":
    oldfullpath = playbook.properties.sep_oldpathname.get("oldPathName")
    fullpathname = playbook.properties.sep_fullpathname.get("fullPathName")
    note_text = "Symantec SEP Integration:\nPlaybook: <b>{0}</b>:\nSuccessfully moved computer <b>{1}</b> " \
               "from group <b>{2}</b> to group <b>{3}</b> for SOAR function <b>{4}</b>."\
        .format(WF_NAME, row.computerName, oldfullpath, fullpathname, FN_NAME)
    row.group_id = GROUP_ID
    if fullpathname:
      row.group_name = fullpathname
  else:
    note_text = "Symantec SEP Integration:\nPlaybook: <b>{0}</b>:\nUnsuccessful move of computer <b>{1}</b> " \
               "to group with id <b>{2}</b>. Received response <b>{3}</b> for SOAR function <b>{4}</b>."\
        .format(WF_NAME, row.computerName, GROUP_ID, response_msg, FN_NAME)
else:
  noteText = "Symantec SEP Integration:\nPlaybook: <b>{0}</b>:\nMove unsuccessful for computer with hardware id <b>{1}</b> " \
             "to group with id <b>{2}</b> for SOAR function <b>{3}</b>."\
      .format(WF_NAME, HW_KEY, GROUP_ID, FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Quarantine Endpoints
Quarantine/un-quarantine Symantec Endpoint Protection endpoints. The function will add or remove endpoints to or from network quarantine.

 ![screenshot: fn-sep---quarantine-endpoints ](./doc/screenshots/fn-sep---quarantine-endpoints.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_computer_ids` | `text` | No | `-` | The list of computer ids on which to run the SEP command. |
| `sep_group_ids` | `text` | No | `-` | The list of groups on which to run the SEP command. |
| `sep_hardwarekey` | `text` | No | `-` | Hardware key of SEP computer. |
| `sep_undo` | `boolean` | No | `-` | Boolean value, if set to true, will undo operation. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "commandID_computer": "1CA9D4F37DD94CA88A9D93D09402E3D3",
    "commandID_group": "89637CF1D7204D028522C81C4389301B"
  },
  "inputs": {
    "sep_computer_ids": "01ECF4E8092E5BB91E4D52E45C3ABE4D",
    "sep_group_ids": "E5E684A6092E5BB90F46E84BB6F35BBC",
    "sep_hardwarekey": "8DACE2559C1C951E09CC0BF71D973BB7",
    "sep_undo": false
  },
  "metrics": {
    "execution_time_ms": 1016,
    "host": "my.app.host",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-08-21 08:40:30",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.sep_computer_ids = row.uniqueId
inputs.sep_group_ids = row.group_id
inputs.sep_hardwarekey = row.hardwareKey

# un-quarantine the endpoint
inputs.sep_undo = True
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_quarantine_endpoints script ##
# Globals
# List of fields in datatable fn_sep_quarantine_endpoints script
DATA_TBL_FIELDS = ["quarantine_commandid"]
fn_name = "fn_sep_quarantine_endpoints"
wf_name = "Quarantine Endpoint"
# Processing
results = playbook.functions.results.quarantine_ep_results
content = results.get("content", {})
inputs = results.get("inputs", {})
query_execution_date = results.get("metrics", {}).get("timestamp")

if content:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nExecuted with command id <b>{1}</b> for endpoint " \
              "<b>{2}</b> for SOAR function <b>{3}</b>"\
      .format(wf_name, content.get("commandID_computer"), row.computerName, fn_name)
  row.query_execution_date = query_execution_date
  row.quarantine_commandid = content.get("commandID_computer")
else:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere was <b>no</b> results returned for SOAR function <b>{1}</b>" \
               .format(wf_name, fn_name)

incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Scan Endpoints
Initiates an Evidence of Compromise (EOC) scan  of an artifact value  against  a list of endpoints or groups. The function can also be used to complete a remediation (quarantine) scan action  for hash value (MD5, SHA1 or SHA256).

 ![screenshot: fn-sep---scan-endpoints ](./doc/screenshots/fn-sep---scan-endpoints.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_computer_ids` | `text` | No | `-` | The list of computer ids on which to run the SEP command. |
| `sep_description` | `text` | No | `-` | The SEP object (e.g. scan) description. |
| `sep_file_path` | `text` | No | `-` | The file path of the suspect file. |
| `sep_group_ids` | `text` | No | `-` | The list of groups on which to run the SEP command. |
| `sep_md5` | `text` | No | `-` | The MD5 hash value of the suspicious file. |
| `sep_scan_action` | `select` | No | `-` | Action to be performed during a scan. |
| `sep_scan_type` | `select` | No | `-` | The SEP eoc scan type. Possible values are:  FULL_SCAN and QUICK_SCAN. |
| `sep_sha1` | `text` | No | `-` | The SHA1 hash value of the suspicious file. |
| `sep_sha256` | `text` | No | `-` | The SHA256 hash value of the suspicious file. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "commandID_computer": "A0B9FC7873584EEAA44E1C3F78882D28"
  },
  "inputs": {
    "sep_computer_ids": "01ECF4E8092E5BB91E4D52E45C3ABE4D",
    "sep_description": "Scan eoc for suspicious hash of type Malware SHA-256 Hash and value 1ac32478198ae72153801c58d2e437f27827f434fd810ae8d6ec6bc8f54350fb in the SEP environment.",
    "sep_file_path": null,
    "sep_md5": null,
    "sep_scan_action": null,
    "sep_scan_type": "QUICK_SCAN",
    "sep_sha1": null,
    "sep_sha256": "1ac32478198ae72153801c58d2e437f27827f434fd810ae8d6ec6bc8f54350fb"
  },
  "metrics": {
    "execution_time_ms": 1002,
    "host": "my.app.host",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-08-16 08:46:57",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python

GET_COMPUTERS_CONTENT = playbook.functions.results.get_computers_results.get("content", {})
ARTIFACT_TYPE = artifact.type
ARTIFACT_VALUE = artifact.value
ARTIFACT_DESCRIPTION = artifact.description
ARTIFACT_TYPE_TO_ROW = {
  "File Name": "file_name",
  "File Path": "file_path",
  "Malware MD5 Hash": "md5",
  "Malware SHA-1 Hash": "sha1",
  "Malware SHA-256 Hash": "sha256"
}
ARTIFACT_TYPES = ['file_name', 'file_path', 'md5', 'sha1', 'sha256']
COMPUTER_IDS = []

def set_inputs(fn, fp, md5, sha1, sha256):
  global COMPUTER_IDS
  inputs.sep_file_path = fn if fp is None else fp
  inputs.sep_md5 = md5
  inputs.sep_sha1 = sha1
  inputs.sep_sha256 = sha256
  inputs.sep_computer_ids = ','.join(COMPUTER_IDS)
  inputs.sep_scan_type = playbook.inputs.sep_scan_type
  inputs.sep_scan_action = None
  if ARTIFACT_DESCRIPTION:
    inputs.sep_description = "Scan eoc for {0}".format(ARTIFACT_DESCRIPTION.get("content"))
  else:
    inputs.sep_description = "Scan eoc for suspicious hash of type {0} and value {1} in the SEP environment.".format(ARTIFACT_TYPE, ARTIFACT_VALUE)

# Get computers to run scan against from previous step.
if GET_COMPUTERS_CONTENT and GET_COMPUTERS_CONTENT.get("endpoints_matching_ids"):
  COMPUTER_IDS = GET_COMPUTERS_CONTENT.get("endpoints_matching_ids")
# Assign values to correct row based on artifact type
types = [None if t not in ARTIFACT_TYPE_TO_ROW.get(ARTIFACT_TYPE) else ARTIFACT_VALUE for t in ARTIFACT_TYPES]
set_inputs(*types)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_upload_file_to_sepm script ##
# List of fields in datatable fn_sep_get_command_status script
DATA_TBL_FIELDS = ["scan_commandID"]
FN_NAME = "fn_sep_scan_endpoints"
WF_NAME = "Initiate EOC Scan for Artifact"

results = playbook.functions.results.scan_eoc_results
CONTENT = results.get("content", {})
INPUTS = results.get("inputs", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")
note_text = ''

if CONTENT:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nReturned command id <b>{1}</b> for a <b>{2}</b> " \
              "scan on artifact <b>{3}</b> for SOAR function <b>{4}</b>"\
      .format(WF_NAME, CONTENT.get("commandID_computer"), INPUTS.get("sep_scan_type"), artifact.value, FN_NAME)
else:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere was <b>no</b> command id returned for a " \
              "<b>{1}</b> scan on artifact <b>{2}</b> for SOAR function <b>{3}</b>"\
      .format(WF_NAME, INPUTS.get("sep_scan_type"), INPUTS.get("sep_file_path"), artifact.value, FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Update Fingerprint List
Updates an existing fingerprint list with a set of hash values. 
Note: Currently supports MD5 and SHA256 hash type.

 ![screenshot: fn-sep---update-fingerprint-list ](./doc/screenshots/fn-sep---update-fingerprint-list.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_description` | `text` | No | `-` | The SEP object (e.g. scan) description. |
| `sep_domainid` | `text` | No | `-` | The SEPM domain id. |
| `sep_fingerprintlist_id` | `text` | No | `-` | Id of SEP fingerprint list |
| `sep_fingerprintlist_name` | `text` | No | `-` | Name of a SEP fingerprint list. |
| `sep_hash_value` | `text` | No | `-` | The hash value. Can be MD5 or SHA256 hash value. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": "",
  "inputs": {
    "sep_description": "Fingerprint list \u0027Blacklist\u0027",
    "sep_domainid": "6E70F043092E5BB93F74FD57C083F99E",
    "sep_fingerprintlist_content": "[{\u0027SHA256\u0027: \u00279a4e26d0c4ab855d5346bae28272bbeeb1ab713b29a4aab030770655f05acc25\u0027}, {\u0027MD5\u0027: \u0027FF8C053969C0A52FF267D25138C71553\u0027, \u0027SHA256\u0027: \u002702E188239C4A7761C2F4C63964B6A754E15A388980F4050AC8C327D1FA30255F\u0027}, {\u0027MD5\u0027: \u0027FF8D7335A370D17A1379A949AF595F78\u0027, \u0027SHA256\u0027: \u00276E46434DACCDED82FA235FA14A019C20CF3AAFDAAB3F8EB81EBD0195C8F1D909\u0027}, {\u0027MD5\u0027: \u0027FF8D847F4173DBFCAF0A25C6C17C7B99\u0027, \u0027SHA256\u0027: \u0027BC56124B126D2A2F468125C38789FF19C9655FDD3A84990A1B90E2F91BCA1FD9\u0027}, {\u0027MD5\u0027: \u0027FF8F37FECFB4F7A56531E413883E03F5\u0027, \u0027SHA256\u0027: \u0027AD49D17F25670CF54B14DC7FE3EC086D9FCB92DEB4375B598AB95ECCD676CDBC\u0027}, {\u0027MD5\u0027: \u0027FF8FFEA7310D9A4A642CC8018227B91B\u0027, \u0027SHA256\u0027: \u0027924D3456B5D72F6792CAE92895CFA9C0FEBA74616D92C8CD63639F77646B6B05\u0027}, {\u0027MD5\u0027: \u0027FF9171426D5A9490D548B08A5CA9C805\u0027, \u0027SHA256\u0027: \u00271F83EF7D0548828F101A6C760F1D208E2B220186ED71E38942D6CF6EF95FF756\u0027}, {\u0027MD5\u0027: \u0027FF91FA115BA27CD56716623DC6933946\u0027, \u0027SHA256\u0027: \u002705C2FB7565D2953D46E458D96000CD589AC14C4E4C33E718E38BE4739A9F7504\u0027}, {\u0027MD5\u0027: \u0027FF92B0EA7579E691C1FF669FAB5AC186\u0027, \u0027SHA256\u0027: \u0027048E17562A6C601D3EAFF05FF62318944C9E7083825F587AD0F5C1C2C26CBD71\u0027}, {\u0027MD5\u0027: \u0027FF93C7959F24921381B8338686B0509C\u0027, \u0027SHA256\u0027: \u00272C6DCF143C41A5780DD24B48CA08EFC96595D86F4DB1FCD10D59E28EC1DBB0E2\u0027}, {\u0027MD5\u0027: \u0027FF95B2B128EB6B0BDDDF39CD05C78A0F\u0027, \u0027SHA256\u0027: \u0027DF1AE05C349A5C4E9D3187D0D85BD6172FB131BD5B826A1FFC947DB9A09F3DCF\u0027}, {\u0027MD5\u0027: \u0027FF9932C30F72B19E57D9B07F230487E7\u0027, \u0027SHA256\u0027: \u0027FBD7F130718C6A73E0AFD15D1F8D843426604A866EC63624357F8A952B484AD1\u0027}, {\u0027MD5\u0027: \u0027FF995A3411623293F7E3FD72143D04AB\u0027, \u0027SHA256\u0027: \u0027ACEA65301D759F922BDB1AB8DD52B57828FF4D64106A93C3EEAF89553466EA58\u0027}, {\u0027MD5\u0027: \u0027FF9CD8F4947AD1474D29187220BC3972\u0027, \u0027SHA256\u0027: \u0027AE17F31CBEEC0471392A42E85CB8B258351351212AB028C0B6B5C101C76083D9\u0027}, {\u0027MD5\u0027: \u0027FF9CF495023DD6D5BCE4187214B1469B\u0027, \u0027SHA256\u0027: \u00278D9FE0851D4D35D312F35E83618F63DFCBB4A045B5348468E04AE3CA61782F74\u0027}, {\u0027MD5\u0027: \u0027FF9D51FB459CF535F33003FABB0E7FD9\u0027, \u0027SHA256\u0027: \u00276D36FEB1167103BFE37251D1B049C449466A21590710F1E7F20C9B0C69511F7B\u0027}, {\u0027MD5\u0027: \u0027FF9E058DAC27FCC739884D3DBE43D81F\u0027, \u0027SHA256\u0027: \u00278C6A42FC8D9262A7E84C39566AB25931FBD77A7F9B5F1806DB69B297ADC87F3C\u0027}, {\u0027MD5\u0027: \u0027FF9E1E7E499D8C6336FA697C7142FA0C\u0027, \u0027SHA256\u0027: \u0027FD8862560FFA44B8177F1B1E053C1E820F2E19636F28E75A9AC427DBA0E15534\u0027}, {\u0027MD5\u0027: \u0027FF9E62ECB2BFD5B9CA608A40A96DEB04\u0027, \u0027SHA256\u0027: \u002795A9CB94CCB3F30029E1C977B63A845FE129C02E6CAF26AD234AB66AA9AF1C6C\u0027}, {\u0027MD5\u0027: \u0027FFA44FD7FEDA32632E8CE84AD0F9101B\u0027, \u0027SHA256\u0027: \u00272A0746A7876C1A430F9C9A5BE4BE28CAA2FF4F73477651AE5CC74462278F333B\u0027}, {\u0027MD5\u0027: \u0027FFA6335553397F28CA47ADC34343CA62\u0027, \u0027SHA256\u0027: \u00270D43D4D40C9854EB158DDE164699D02F47B21D68CEACAFEB2F469587B861C356\u0027}]",
    "sep_fingerprintlist_id": "C5C4CAC9092E5BB9315A5137B5B8DC8B",
    "sep_fingerprintlist_name": "Blacklist",
    "sep_hash_value": "0b9e4cb2af3dd1686accf0c469ce7b60"
  },
  "metrics": {
    "execution_time_ms": 1685,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-11 10:29:26",
    "version": "1.0"
  },
  "raw": "\"\"",
  "reason": null,
  "success": true,
  "version": "1.0"
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
domain_content = playbook.functions.results.get_domains_results.get("content", [])
fpl_content = playbook.functions.results.get_fingerprintlist_results.get("content", {})
fpl_data = fpl_content.get("data", []).copy()

for i in range(len(domain_content)):
  if domain_content[i].get("name") == playbook.inputs.sep_domain_name:
    inputs.sep_domainid = domain_content[i].get("id")
    break

if fpl_content.get("name") == playbook.inputs.sep_fingerprintlist_name:
  inputs.sep_fingerprintlist_id = fpl_content.get("id")
  inputs.sep_fingerprintlist_name = playbook.inputs.sep_fingerprintlist_name

  if fpl_data:
    # If the fingerprintlist a list of dictionaries, then it is using the new format.
    if isinstance(fpl_data[0], dict):
      # Get hash type
      hash_type = "MD5"
      if artifact.type == "Malware SHA-256 Hash":
        hash_type = "SHA256"

      fpl_data.append({hash_type: artifact.value})
      inputs.sep_hash_value = str(fpl_data)
    else:
      inputs.sep_hash_value = artifact.value + ',' + ','.join(fpl_data)

inputs.sep_description = f"Fingerprint list '{playbook.inputs.sep_fingerprintlist_name}'"
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_update_fingerprint_list script ##
FN_NAME = "fn_sep_update_fingerprint_list"
WF_NAME = "Add Hash to Fingerprint List"
results = playbook.functions.results.update_fingerprintlist_results
INPUTS = results.get("inputs")
note_text = None
hash_type = "MD5"
if artifact.type == "Malware SHA-256 Hash":
  hash_type = "SHA256"

if results.get("success"):
  # If we got here we assume we are successful, no status message is returned by api.
  note_text = f"Symantec SEP Integration:\nPlaybook: <b>{WF_NAME}</b>\nSuccessfully added {hash_type} hash <b>{artifact.value}</b> to fingerprint " \
              f"list <b>{INPUTS.get('sep_fingerprintlist_name')}</b> for SOAR function <b>{FN_NAME}</b>"

else:
  note_text = f"Symantec SEP Integration:\nPlaybook: <b>{WF_NAME}</b>\nFailed with reason: {results.get('reason')}"

incident.addNote(helper.createRichText(note_text))
```

</p>
</details>

---
## Function - SEP - Upload File to SEPM
Upload a file from an endpoint back to the SEPM server.  
Note: Only supports executable file types such as binary executable (.exe), batch (.bat), Windows installer package (.msi) etc. File source can be FILESYTEM, QUARANTINE or BOTH

 ![screenshot: fn-sep---upload-file-to-sepm ](./doc/screenshots/fn-sep---upload-file-to-sepm.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `sep_computer_ids` | `text` | No | `-` | The list of computer ids on which to run the SEP command. |
| `sep_file_path` | `text` | No | `-` | The file path of the suspect file. |
| `sep_md5` | `text` | No | `-` | The MD5 hash value of the suspicious file. |
| `sep_sha1` | `text` | No | `-` | The SHA1 hash value of the suspicious file. |
| `sep_sha256` | `text` | No | `-` | The SHA256 hash value of the suspicious file. |
| `sep_source` | `text` | No | `-` | The file source from where to search for the suspicious file. Possible values are: FILESYSTEM (default), QUARANTINE, or BOTH.  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "commandID": "C9456A597A0E42A89F243B8A537A056D"
  },
  "inputs": {
    "sep_computer_ids": "01ECF4E8092E5BB91E4D52E45C3ABE4D",
    "sep_file_path": "C:\\Users\\Administrator\\Desktop\\tesy.txt",
    "sep_md5": "44d88612fea8a8f36de82e1278abb02f",
    "sep_sha1": null,
    "sep_sha256": null,
    "sep_source": "QUARANTINE"
  },
  "metrics": {
    "execution_time_ms": 7428,
    "host": "local",
    "package": "fn-sep",
    "package_version": "1.2.0",
    "timestamp": "2024-07-29 09:49:39",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.sep_computer_ids = row.computer_id
inputs.sep_file_path = row.file_path
inputs.sep_source = playbook.inputs.sep_source
hash_lengths  = [64, 40, 32]
hvs = [None if h != len(row.hash_value) else row.hash_value for h in hash_lengths]
inputs.sep_sha256 = hvs[0]
inputs.sep_sha1 = hvs[1]
inputs.sep_md5 = hvs[2]
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
## Symantec Endpoint Protection - fn_sep_upload_file_to_sepm script ##
# Globals
# List of fields in datatable fn_sep_get_command_status script
DATA_TBL_FIELDS = ["commandID"]
fn_name = "fn_sep_upload_file_to_sepm"
wf_name = "Upload file to SEPM server"
results = playbook.functions.results.upload_file_results
content = results.get("content", {})
inputs = results.get("inputs", {})

# Processing
if content:
  noteText = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nCommand executed with id <b>{1}</b> for artifact with " \
             "type <b>{2}</b> and value <b>{3}</b> from source <b>{4}</b> for SOAR function <b>{5}</b>"\
      .format(wf_name, content.get("commandID"), row.artifact_type, row.artifact_value, inputs.get("sep_source"), fn_name)
  row.upload_commandid = content.get("commandID")

else:
  noteText += "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere was <b>no</b> results returned for SOAR " \
              "function <b>{1}</b>".format(wf_name, fn_name)

incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---

## Script - scr_sep_add_artifact_from_scan_results
Script for Symantec SEP to add a SOAR artifact from a property of the 'Symantec SEP - EOC scan results' data-table.
The supported artifact types supported are: "File Path", "Malware SHA-256 Hash" and "System Name".

**Object:** sep_eoc_scan_results

<details><summary>Script Text:</summary>
<p>

```python
# Create a SOAR artifact based on a dropdown which selects the corresponding data-table field.
ARTIFACT_TYPE = rule.properties.sep_artifact_type_scan_results
FUNCTION_NAME = "fn_sep_scan_endpoints"

PARAMS = {
    "Malware SHA-256 Hash": row.hash_value,
    "System Name": row.computer_name,
    "File Path": row.file_path
}


def addArtifact(artifact_type, artifact_value, description):
    """This method adds new artifacts to the incident derived from matches of the the regular expression

    :param artifact_type: The type of the artifact.
    :param artifact_value: - The value of the artifact.
    :param description: - the description of the artifact.
    """
    incident.addArtifact(artifact_type, artifact_value, description)


def validate_fields(fields, params):
    """
    Ensure required fields are present. Throw ValueError if not
    :param fields: Required fields.
    :param params: Data-table fields as parameters.
    :return: no return
    """
    for f in fields:
        if f not in params or not params.get(f) or params.get(f) == '':
            raise ValueError(str('Required data-table field is missing or empty for artifact type: ' + f))


def main():
    desc = ''

    validate_fields(["System Name", ARTIFACT_TYPE], PARAMS)

    desc = "Detected by Symantec SEP Eoc Scan for artifact of type '{0}' and value '{1}' by function " \
    "'{2}' for Symantec SEP.".format(row.artifact_type, row.artifact_value, FUNCTION_NAME)
    addArtifact(ARTIFACT_TYPE, PARAMS[ARTIFACT_TYPE], desc)


# Script execution starts here
if __name__ == "__main__":
    main()
```

</p>
</details>

---
## Script - scr_sep_parse_email_notification
Script for Symantec SEP to parse email notifications to generate incidents and artifacts.

**Object:** __emailmessage

<details><summary>Script Text:</summary>
<p>

```python
# Symantec SEP email notification parsing script.
# This is a a follow-on from the generic parsing script which is used specifically to parse for Symantec SEP notifications.

import re

# Dict to capture suspicious file details to add to data-table.
FILE_PATH_LIST = []
COMPUTER_NAME = ''

def add_artifact(artifact_type, artifact_value, description):
    """ Add new artifacts to the incident.
    :param artifact_type: The type of the artifact.
    :param artifact_value: - The value of the artifact.
    :param description: - the description of the artifact.
    """
    incident.addArtifact(artifact_type, artifact_value, description)

def add_artifact_from_email(regex, artifact_type, description):
    """This method adds new artifacts to the incident derived from matches of the the regular expression
    parameter within the email body contents.
    :param regex: - A regular expression to match against the email body contents.
    :param artifact_type: - The type of the artifact(s).
    :param description: - The description of the artifact(s).
    """
    global FILE_PATH_LIST, COMPUTER_NAME
    data_list = []
    if artifact_type == "System Name":
        # Only extract 1st match found for "Computer:"
        data = re.search(regex, emailmessage.body.content)
        if data is not None:
            add_artifact(artifact_type, data.group(1), description)
            COMPUTER_NAME = data.group(1).strip()
    else:
        data_set = set(re.findall(regex, emailmessage.body.content))  # Using a set to enforce uniqueness
        if data_set is not None and len(data_set) > 0:
            # Convert regex set to list
            for d in data_set:
                data_list.append(d.strip())
            [add_artifact(artifact_type, artifact_value, description) for artifact_value in data_list]
            if artifact_type == "File Path":
                [FILE_PATH_LIST.append(fp) for fp in data_list]


###
# Mainline starts here
###
def main():
    # Add "Phishing" as an incident type for the associated incident
    incident.incident_type_ids.append("Phishing")

    # Add the email sender information to the incident as the recipient of the Symantec SEP notification.
    reportingUserInfo = emailmessage.from.address
    if emailmessage.from.name is not None:
        reportingUserInfo = u"{0} <{1}>".format(emailmessage.from.name,emailmessage.from.address)
        incident.addArtifact("Email Recipient", reportingUserInfo, "Symantec SEP notification email reipient.")
        # Extract email sender information on the assumption that a fishing email is being forwarded
    if emailmessage.body.content is not None:
        add_artifact_from_email(r"From: (.*)\n", "Email Sender", "Symantec SEP notification  email sender.")
        add_artifact_from_email(r"Reply-To: (.*)\n", "Email Sender", "Symantec SEP notification email sender (Reply-To).")
        add_artifact_from_email(r"File path: (.*)\n", "File Path", "File path of suspicious file in SEP environment.")
        add_artifact_from_email(r"Computer: (.*)\n", "System Name", "Endpoint  with suspicious file in SEP environment.")
        add_artifact_from_email(r"User: (.*)\n", "User Account", "User account which had a suspicious file in SEP environment.")
        add_artifact_from_email(r"IP Address: (.*)\n", "IP Address",
                        "IP address of Endpoint which had the suspicious file in SEP environment.")
        add_artifact_from_email(r"Security alert: suspicious activity from (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) .*", "IP Address",
                                "IP address with suspicious activity detected in SEP environment.")
    if FILE_PATH_LIST:
        for fp in FILE_PATH_LIST:
          file_name = fp.split("\\")[-1] if '\\' in fp else fp.split("/")[-1]
          add_artifact("File Name", file_name, "File name of file path for suspicious file {} in SEP environment.".format(fp))

# Script execution starts here
main()
```

</p>
</details>

---

## Playbooks
| Playbook Name | Description | Activation Type | Object | Status | Condition | 
| ------------- | ----------- | --------------- | ------ | ------ | --------- | 
| SEP: Add Artifact from Scan Result - Example (PB) | add a SOAR artifact from a property of the 'Symantec SEP - EOC scan results' data-table. The supported artifact types supported are: "File Path", "Malware SHA-256 Hash" and "System Name". | Manual | sep_eoc_scan_results | `enabled` | `sep_eoc_scan_results.file_path has_a_value AND sep_eoc_scan_results.computer_name has_a_value AND sep_eoc_scan_results.scan_command_state contains Completed AND sep_eoc_scan_results.hash_value has_a_value AND (sep_eoc_scan_results.scan_result contains Hash match OR sep_eoc_scan_results.scan_result contains Full match)` | 
| SEP: Add Hash to Blacklist - Example (PB) | Create a new blacklist fingerprint list and add an MD5 hash if the fingerprint list doesn't already exist. Add an MD5 hash to an existing blacklist fingerprint list if it already exists. | Manual | artifact | `enabled` | `artifact.type in ['Malware MD5 Hash', 'Malware SHA-256 Hash']` | 
| SEP: Assign Blacklist to lockdown group - Example (PB) | Assign a blacklist fingerprint list to a group for system lockdown. | Manual | sep_groups | `enabled` | `sep_groups.group_id has_a_value AND sep_groups.policyInheritanceEnabled equals` | 
| SEP: Cancel a Command - Example (PB) | Cancel an existing pending command | Manual | incident | `enabled` | `-` | 
| SEP: Delete Blacklist - Example (PB) | Delete an existing blacklist fingerprint list. Note: Also removes it from any group to which it has been assigned. | Manual | sep_fingerprint_lists | `enabled` | `sep_fingerprint_lists.list_id has_a_value` | 
| SEP: Delete Hash from Blacklist - Example (PB) | Update a blacklist fingerprint list to remove an MD5 hash. Note: The fingerprint list will be deleted if only a single MD5 hash is remaining in the list. | Manual | artifact | `enabled` | `artifact.type in ['Malware MD5 Hash', 'Malware SHA-256 Hash']` | 
| SEP: Get Blacklist information - Example (PB) | Get a blacklist fingerprint list information for a specified name. | Manual | incident | `enabled` | `-` | 
| SEP: Get Critical Events - Example (PB) | Gets information related to critical events. | Manual | incident | `enabled` | `-` | 
| SEP: Get Endpoint Details - Example (PB) | Get endpoint details for Evidence of Compromise (EOC) data table row "computer_name" value. | Manual | sep_eoc_scan_results | `enabled` | `sep_eoc_scan_results.computer_name has_a_value` | 
| SEP: Get Endpoint Details for artifact - Example (PB) | Get endpoint details for artifact value. Artifact value will be "DNS name" or "System name" | Manual | artifact | `enabled` | `artifact.type equals DNS Name OR artifact.type equals System Name` | 
| SEP: Get Endpoints status summary - Example (PB) | Get overall Endpoint status summary. | Manual | incident | `enabled` | `-` | 
| SEP: Get Endpoints status summary (refresh) - Example (PB) | Get overall Endpoint status summary. | Manual | sep_endpoint_status_summary | `enabled` | `-` | 
| SEP: Get Exceptions Policy - Example (PB) | Get the exception's policy for the specified policy ID. | Manual | incident | `enabled` | `-` | 
| SEP: Get File Content as Base64 string - Example (PB) | Get contents of a file uploaded to SEPM server as a Base64 string. | Manual | sep_eoc_scan_results | `enabled` | `sep_eoc_scan_results.file_id has_a_value AND sep_eoc_scan_results.file_upload_status contains Completed AND sep_eoc_scan_results.scan_command_state contains Completed AND sep_eoc_scan_results.scan_commandid has_a_value` | 
| SEP: Get Firewall Policy - Example (PB) | Get the firewall policy for the specified policy ID. | Manual | incident | `enabled` | `-` | 
| SEP: Get Groups information - Example (PB) | Get groups information. | Manual | incident | `enabled` | `-` | 
| SEP: Get Non-Compliant Endpoints status details - Example (PB) | Get further details for Endpoints with non-compliant status. | Manual | sep_endpoint_status_summary | `enabled` | `sep_endpoint_status_summary.non_compliant gt` | 
| SEP: Get Policy Summary - Example (PB) | Get the summary information for policies within a specific Domain. Also gets the list of groups to which the policies are assigned. | Manual | incident | `enabled` | `-` | 
| SEP: Get Quarantine status - Example (PB) | Get the status of a Quarantine Endpoint command. | Manual | sep_endpoint_details | `enabled` | `sep_endpoint_details.computerName has_a_value AND sep_endpoint_details.quarantine_commandid has_a_value AND sep_endpoint_details.uniqueId has_a_value` | 
| SEP: Get Remediation status - Example (PB) | Get the status of a remediation scan command. | Manual | sep_eoc_scan_results | `enabled` | `sep_eoc_scan_results.remediation_status has_a_value AND (sep_eoc_scan_results.remediation_status contains In progress OR sep_eoc_scan_results.remediation_status contains Waiting/Not received OR sep_eoc_scan_results.remediation_status contains Received)` | 
| SEP: Get Scan results - Example (PB) | Get the results of a scan EOC command. | Manual | sep_eoc_scan_results | `enabled` | `sep_eoc_scan_results.scan_command_state not_contains Completed AND sep_eoc_scan_results.scan_command_state not_contains Timedout AND sep_eoc_scan_results.scan_commandid has_a_value AND (sep_eoc_scan_results.scan_command_state contains In progress OR sep_eoc_scan_results.scan_command_state contains Received OR sep_eoc_scan_results.scan_command_state contains Waiting/Not received)` | 
| SEP: Get Upload status - Example (PB) | Get the status of an Upload command. | Manual | sep_eoc_scan_results | `enabled` | `sep_eoc_scan_results.file_upload_status contains In progress AND sep_eoc_scan_results.upload_commandid has_a_value` | 
| SEP: Initiate EOC Scan for Artifact - Example (PB) | Initiate an Evidence of Compromise (EOC) scan on artifacts of type file (name or path) or hash (MD5, SHA1 or SHA256) against all endpoints. Use the returned command ID to get the initial command status and information on any matches for each endpoint. | Manual | artifact | `enabled` | `artifact.type equals File Name OR artifact.type equals File Path OR artifact.type equals Malware MD5 Hash OR artifact.type equals Malware SHA-1 Hash OR artifact.type equals Malware SHA-256 Hash` | 
| SEP: Move Endpoint - Example (PB) | Move an endpoint to a different group. | Manual | sep_endpoint_details | `enabled` | `sep_endpoint_details.hardwareKey has_a_value AND sep_endpoint_details.uniqueId has_a_value` | 
| SEP: Quarantine Endpoint - Example (PB) | Quarantine or un-quarantine an endpoint. Add or remove endpoints to or from network quarantine. | Manual | sep_endpoint_details | `enabled` | `sep_endpoint_details.computerName has_a_value AND sep_endpoint_details.endpoint_quarantine_status not_equals Quarantined AND sep_endpoint_details.group_id has_a_value AND sep_endpoint_details.hardwareKey has_a_value AND sep_endpoint_details.quarantine_command_state not_contains In progress AND sep_endpoint_details.uniqueId has_a_value` | 
| SEP: Remediate Artifact on Endpoint - Example (PB) | Initiate a file quarantine scan on Symantec Endpoint Protection endpoints and get initial command status. A remediation action quarantines all copies of the selected file on the target endpoint(s) by hash value (SHA256, SHA1 or MD5). | Manual | sep_eoc_scan_results | `enabled` | `sep_eoc_scan_results.scan_commandid has_a_value AND sep_eoc_scan_results.scan_command_state contains Completed AND (sep_eoc_scan_results.scan_result contains FULL_MATCH OR sep_eoc_scan_results.scan_result contains HASH_MATCH OR sep_eoc_scan_results.scan_result contains PARTIAL_MATCH) AND sep_eoc_scan_results.remediation_status not_contains Completed AND sep_eoc_scan_results.remediation_status not_contains In progress AND sep_eoc_scan_results.remediation_status not_contains Unexpected status AND sep_eoc_scan_results.remediation_status not_contains No match found AND sep_eoc_scan_results.remediation_status not_contains Failed` | 
| SEP: Un-Quarantine Endpoint - Example (PB) | Quarantine or un-quarantine an endpoint. Add or remove endpoints to or from network quarantine. | Manual | sep_endpoint_details | `enabled` | `sep_endpoint_details.computerName has_a_value AND sep_endpoint_details.endpoint_quarantine_status equals Quarantined AND sep_endpoint_details.group_id has_a_value AND sep_endpoint_details.hardwareKey has_a_value AND sep_endpoint_details.quarantine_command_state not_contains In progress AND sep_endpoint_details.uniqueId has_a_value` | 
| SEP: Upload file to SEPM server - Example (PB) | Request a file discovered by an EOC scan be uploaded to the SEPM server. Note: Only supports file executable types such as binary executable (.exe), batch (.bat), Windows installer package (.msi) etc. | Manual | sep_eoc_scan_results | `enabled` | `sep_eoc_scan_results.scan_commandid has_a_value AND sep_eoc_scan_results.scan_command_state contains Completed AND (sep_eoc_scan_results.scan_result contains Full match OR sep_eoc_scan_results.scan_result contains Hash match OR sep_eoc_scan_results.scan_result contains Partial match) AND sep_eoc_scan_results.file_upload_status not_contains In progress AND sep_eoc_scan_results.file_upload_status not_contains Completed` | 

---

## Data Table - Symantec SEP - Critical Events

 ![screenshot: dt-symantec-sep---critical-events](./doc/screenshots/dt-symantec-sep---critical-events.png)

#### API Name:
sep_critical_events

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Acknowledged | `acknowledged` | `boolean` | - |
| Date Added | `date_added` | `datetimepicker` | - |
| Event Date | `event_date` | `text` | - |
| Event Id | `event_id` | `text` | - |
| Message | `message` | `text` | - |
| Subject | `subject` | `text` | - |

---
## Data Table - Symantec SEP - Endpoint details

 ![screenshot: dt-symantec-sep---endpoint-details](./doc/screenshots/dt-symantec-sep---endpoint-details.png)

#### API Name:
sep_endpoint_details

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Computer name | `computerName` | `text` | - |
| Description | `sep_description` | `text` | Description of an endpoint in the SEP environment. |
| Endpoint Quarantine Status | `endpoint_quarantine_status` | `textarea` | Quarantine status of an endpoint. Possible statuses are 'Un-Quarantined' and 'Quarantined'. Note: Only applicable for MS Windows endpoints. |
| Hardware key | `hardwareKey` | `text` | Hardware Key is the way to identify a client in SEP. |
| Infected | `infected` | `text` | - |
| IP addresses | `ipAddresses` | `text` | - |
| Operating system | `operatingSystem` | `text` | - |
| Quarantine command state | `quarantine_command_state` | `textarea` | State of the quarantine command for a SEP command id. |
| Query execution date | `query_execution_date` | `text` | - |
| SEP Computer id | `uniqueId` | `text` | - |
| SEP domain id | `domain_id` | `text` | - |
| SEP domain name | `domain_name` | `text` | - |
| SEP group id | `group_id` | `text` | - |
| SEP group name | `group_name` | `text` | - |
| SEP quarantine  command id | `quarantine_commandid` | `text` | - |

---
## Data Table - Symantec SEP - Endpoint status summary

 ![screenshot: dt-symantec-sep---endpoint-status-summary](./doc/screenshots/dt-symantec-sep---endpoint-status-summary.png)

#### API Name:
sep_endpoint_status_summary

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Disabled | `disabled` | `number` | Count of endpoints on which at least one of the main Symantec SEP engines are disabled. |
| Host integrity failed | `hi_failed` | `number` | Count of endpoints where Host Integrity check has failed. |
| Non compliant | `non_compliant` | `number` | Total count of non-compliant endpoints in the Symantec SEP environment.  |
| Offline | `offline` | `number` | Count of offline endpoints. |
| Out of date | `out_of_date` | `number` | Count of endpoints which have not sent an update within the heartbeart (15 minute) windows. |
| Query execution date | `query_execution_date` | `text` | - |
| Total | `total` | `number` | Total count of endpoints in the Symantec SEP environment. Note: Endpoints can be counted in more than status column. |
| Up to date | `up_to_date` | `number` | Count of endpoints which have sent an update within the heartbeart (15 minute) windows. |

---
## Data Table - Symantec SEP - EOC scan results

 ![screenshot: dt-symantec-sep---eoc-scan-results](./doc/screenshots/dt-symantec-sep---eoc-scan-results.png)

#### API Name:
sep_eoc_scan_results

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Artifact id | `artifact_id` | `text` | The ID of the artifact |
| Artifact type | `artifact_type` | `text` | The SOAR artifact type. Either Malware SHA-256 Hash, Malware SHA-1 Hash, Malware MD5 Hash, File Name, or File Path |
| Artifact value | `artifact_value` | `text` | The value of the SOAR artifact |
| Computer name | `computer_name` | `text` | Name of the SEP computer |
| File path | `file_path` | `text` | - |
| File upload  status | `file_upload_status` | `textarea` | The status of the file upload from SEP |
| Hash value | `hash_value` | `text` | Scan match can return sha-256, sha1 or md5 hash values. |
| Query execution date | `query_execution_date` | `text` | Time the Query was executed |
| Remediation status | `remediation_status` | `textarea` | The remediation status from SEP |
| Scan command state | `scan_command_state` | `textarea` | This value contains the overall state of the scan command across all target endpoints. Possible values are 'In progress', 'Completed' and 'Timedout''. |
| Scan Query/Result | `scan_result` | `textarea` | This column is used to signify whether the row is being used to display a query or a query result.  Possible values: 'Query' for a query and 'Full match', 'Partial Match' or 'Hash match' for a match. |
| SEP computer id | `computer_id` | `text` | The SEP computer ID |
| SEP file id | `file_id` | `text` | The file ID from SEP |
| SEP remediation command id | `remediation_commandid` | `text` | The remediation command ID from SEP |
| SEP scan command id | `scan_commandid` | `text` | The scan command ID from SEP |
| SEP Scan type | `scan_type` | `text` | The SEP eoc scan type.  |
| SEP upload command id | `upload_commandid` | `text` | The upload command ID from SEP |

---
## Data Table - Symantec SEP - Fingerprint lists

 ![screenshot: dt-symantec-sep---fingerprint-lists](./doc/screenshots/dt-symantec-sep---fingerprint-lists.png)

#### API Name:
sep_fingerprint_lists

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Assigned SEP group ids | `group_ids` | `text` | - |
| Description | `list_description` | `text` | SEP list description. |
| Hash values | `hash_values` | `text` | Hash values in list. |
| List name | `list_name` | `text` | SEP list name. |
| Query Execution date | `query_execution_date` | `text` | - |
| SEP domain name | `domain_name` | `text` | - |
| SEP list id | `list_id` | `text` | - |

---
## Data Table - Symantec SEP - Groups

 ![screenshot: dt-symantec-sep---groups](./doc/screenshots/dt-symantec-sep---groups.png)

#### API Name:
sep_groups

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Description | `group_description` | `text` | Description of the SEP group.  |
| Full path name | `fullPathName` | `text` | Full path name of the SEP group. |
| Number of physical computers | `numberOfPhysicalComputers` | `text` | Numer of physical endpoints assigned to the SEP group. |
| Policy inheritance enabled | `policyInheritanceEnabled` | `boolean` | - |
| Query execution date | `query_execution_date` | `text` | - |
| SEP domain id | `domain_id` | `text` | - |
| SEP domain name | `domain_name` | `text` | - |
| SEP Group id | `group_id` | `text` | - |
| SEP Group name | `group_name` | `text` | - |

---
## Data Table - Symantec SEP - Non-compliant Endpoints status details

 ![screenshot: dt-symantec-sep---non-compliant-endpoints-status-details](./doc/screenshots/dt-symantec-sep---non-compliant-endpoints-status-details.png)

#### API Name:
sep_endpoints_non_compliant_details

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Anti-Virus engine | `avEngineOnOff` | `text` | Anti-Virus engine - status on an endpoint. |
| Auto-protect engine | `apOnOff` | `text` | Auto-protect engine - status on an endpoint. |
| Browser Intrustion Prevention - FireFox engine | `cidsBrowserFfOnOff` | `text` | Browser Intrustion Prevention - FireFox engine - status on an endpoint. |
| Browser Intrustion Prevention - IE engine | `cidsBrowserIeOnOff` | `text` | Browser Intrustion Prevention - IE engine - status on an endpoint. |
| Client Intrusion Detection System engine | `cidsDrvOnOff` | `text` | Client Intrusion Detection System engine - status on an endpoint. |
| Computer name | `computer_name` | `text` | - |
| Download Insight engine | `daOnOff` | `text` | Client Intrusion Detection System engine - status on an endpoint. |
| Early Launch Antimalware engine | `elamOnOff` | `text` | Client Intrusion Detection System engine - status on an endpoint. |
| Firewall engine | `firewallOnOff` | `text` | Client Intrusion Detection System engine - status on an endpoint. |
| Host integrity check status | `host_integrity_check` | `text` | Status of Host Integrity check.  Possible values are 'Passed' and  'Failed'. |
| Last Scan Time | `readableLastScanTime` | `text` | Last time the ednpoint performed a scan. |
| Last update time | `readableLastUpdateTime` | `text` | Last time Endpoint sent an update to the SEPM server. |
| Online status | `onlineStatus` | `text` | - |
| Proactive Exploit Protection engine | `pepOnOff` | `text` | Client Intrusion Detection System engine - status on an endpoint. |
| Proactive Threat Protection engine | `ptpOnOff` | `text` | Client Intrusion Detection System engine - status on an endpoint. |
| Query execution date | `query_execution_date` | `text` | - |
| Tamper protection engine | `tamperOnOff` | `text` | Client Intrusion Detection System engine - status on an endpoint. |

---

## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.

### For Support
This is an IBM supported app. Please search https://ibm.com/mysupport for assistance.
