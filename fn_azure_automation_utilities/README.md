# Azure Automation Utilities

## Table of Contents
- [Azure Automation Utilities](#azure-automation-utilities)
  - [Table of Contents](#table-of-contents)
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
  - [Function - Azure Create Account](#function---azure-create-account)
  - [Function - Azure Create Credential](#function---azure-create-credential)
  - [Function - Azure Create Schedule](#function---azure-create-schedule)
  - [Function - Azure Delete Account](#function---azure-delete-account)
  - [Function - Azure Delete Credential](#function---azure-delete-credential)
  - [Function - Azure Delete Runbook](#function---azure-delete-runbook)
  - [Function - Azure Delete Schedule](#function---azure-delete-schedule)
  - [Function - Azure Execute Runbook](#function---azure-execute-runbook)
  - [Function - Azure Get Account](#function---azure-get-account)
  - [Function - Azure Get Agent Registration Information](#function---azure-get-agent-registration-information)
  - [Function - Azure Get Credential](#function---azure-get-credential)
  - [Function - Azure Get Job](#function---azure-get-job)
  - [Function - Azure Get Module Activity](#function---azure-get-module-activity)
  - [Function - Azure Get Node Report](#function---azure-get-node-report)
  - [Function - Azure Get Runbook](#function---azure-get-runbook)
  - [Function - Azure Get Schedule](#function---azure-get-schedule)
  - [Function - Azure List Statistics by Automation Account](#function---azure-list-statistics-by-automation-account)
  - [Function - Azure Regenerate Agent Registration Key](#function---azure-regenerate-agent-registration-key)
  - [Playbooks](#playbooks)
  - [Data Table - Azure Automation Accounts](#data-table---azure-automation-accounts)
      - [API Name:](#api-name)
      - [Columns:](#columns)
  - [Data Table - Azure Automation Credentials](#data-table---azure-automation-credentials)
      - [API Name:](#api-name-1)
      - [Columns:](#columns-1)
  - [Data Table - Azure Automation Runbooks](#data-table---azure-automation-runbooks)
      - [API Name:](#api-name-2)
      - [Columns:](#columns-2)
  - [Data Table - Azure Automation Schedules](#data-table---azure-automation-schedules)
      - [API Name:](#api-name-3)
      - [Columns:](#columns-3)
  - [Data Table - Azure Automation Statistics](#data-table---azure-automation-statistics)
      - [API Name:](#api-name-4)
      - [Columns:](#columns-4)
  - [Custom Fields](#custom-fields)
  - [Troubleshooting \& Support](#troubleshooting--support)
    - [For Support](#for-support)

---

## Release Notes
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.0.0 | 11/2023 | Initial Release |

---

## Overview
<!--
  Provide a high-level description of the function itself and its remote software or application.
  The text below is parsed from the "description" and "long_description" attributes in the setup.py file
-->
**IBM SOAR App for Azure Automation**

 ![screenshot: main](./doc/screenshots/main.png) 

This app allows interaction with the following Azure Automation resources:
  - Automation Accounts
  - Activities
  - Jobs
  - Runbooks
  - Nodes
  - Credentials
  - Schedules
  - Modules
  - Agent Registration
  - Statistics

### Key Features
* Automation Accounts
* Activities
* Jobs
* Runbooks
* Nodes
* Credentials
* Schedules
* Modules
* Agent Registration
* Statistics


---

## Requirements
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, Edge Gateway (also known as App Host) and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `48.0.0`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `48.0.0`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient-circuits>=48.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions: 
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read |
  | Function | Read |
  | Layout | Edit, Read |

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
The app does support a proxy server.

### Python Environment
Python 3.6 and Python 3.9 are supported.
Additional package dependencies may exist for each of these packages:
* resilient-circuits>=48.0.0

---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **auth_url** | Yes | `https://login.microsoftonline.com/(tenant_id)/oauth2/v2.0/authorize` | *The auth_url setting is used to get a new refresh token.* |
| **client_id** | Yes | `aaaaaaaa-bbbb-cccc-dddd-609dc6e4d76f` | *Azure AD Application client ID* |
| **client_secret** | Yes | `11111~D_gt~dB222226gq11111-v3333333LAaLt` | *Azure AD Application client secret* |
| **refresh_token** | Yes | `` | *The refresh token used to obtain a new access token (for refresh token grant)* |
| **scope** | Yes | `https://management.azure.com/user_impersonation openid profile offline_access` | *Scopes are a way to limit the amount of access that is granted to an access token.* |
| **subscription_id** | Yes | `11111111-aaaa-2222-cccc-89e99b336784` | *Azure subscription ID* |
| **tenant_id** | Yes | `11111111-aaaa-2222-cccc-89e99b336784` | *Azure AD Application tenant ID* |
| **token_url** | Yes | `https://login.microsoftonline.com/(tenant_id)/oauth2/v2.0/token` | *The token_url setting is used to get a new access token.* |
| **https_proxy** | No | `https://proxy:443` | *Proxy url and port* |

### Custom Layouts
* Import the Data Tables and Custom Fields like the screenshot below:

  ![screenshot: custom_layouts](./doc/screenshots/custom_layouts.png)

 ---

## Function - Azure Create Account
Create or update an automation account on Azure

 ![screenshot: fn-azure-create-account ](./doc/screenshots/fn-azure-create-account.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `account_update` | `boolean` | No | `-` | True if you are updating an account |
| `input_parameters` | `text` | No | `-` | string with dictionary format |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "etag": null,
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/autotester24",
    "location": "Canada East",
    "name": "autotester24",
    "properties": {
      "RegistrationUrl": "https://55555555-3333-4444-bb0f-030397ea7fc1.agentsvc.yq.azure-automation.net/accounts/55555555-3333-4444-bb0f-030397ea7fc1",
      "RuntimeConfiguration": {
        "powershell": {
          "builtinModules": {
            "Az": "8.0.0"
          }
        },
        "powershell7": {
          "builtinModules": {
            "Az": "8.0.0"
          }
        }
      },
      "automationHybridServiceUrl": "https://55555555-3333-4444-bb0f-030397ea7fc1.jrds.yq.azure-automation.net/automationAccounts/55555555-3333-4444-bb0f-030397ea7fc1",
      "creationTime": "2023-08-22T12:44:27.9+00:00",
      "disableLocalAuth": false,
      "encryption": {
        "identity": {
          "userAssignedIdentity": null
        },
        "keySource": "Microsoft.Automation"
      },
      "lastModifiedBy": null,
      "lastModifiedTime": "2023-08-22T12:44:27.9+00:00",
      "publicNetworkAccess": true,
      "sku": {
        "capacity": null,
        "family": null,
        "name": "Basic"
      },
      "state": "Ok"
    },
    "systemData": {
      "createdAt": "2023-08-22T12:44:27.9+00:00",
      "lastModifiedAt": "2023-08-22T12:44:27.9+00:00"
    },
    "tags": {},
    "type": "Microsoft.Automation/AutomationAccounts"
  },
  "inputs": {
    "account_name": "autotester24",
    "input_parameters": "{\u0027name\u0027: \u0027autotester24\u0027, \u0027location\u0027: \u0027Canada East\u0027, \u0027tags\u0027: None, \u0027properties\u0027: {\u0027publicNetworkAccess\u0027: True, \u0027disableLocalAuth\u0027: False, \u0027sku\u0027: {\u0027name\u0027: \u0027Basic\u0027}}}",
    "resource_group_name": "demoassets"
  },
  "metrics": {
    "execution_time_ms": 4988,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-22 08:44:29",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group

public_network_access = getattr(playbook.inputs, "azure_automation_account_public_network_access", True)
disable_local_auth = getattr(playbook.inputs, "azure_automation_account_disable_local_auth", False)

payload = {
  "name": playbook.inputs.azure_automation_account_name,
  "location": playbook.inputs.azure_automation_account_location,
  "properties": {
    "publicNetworkAccess": True if public_network_access == None else public_network_access,
    "disableLocalAuth": False if disable_local_auth == None else disable_local_auth,
    "sku":{
      "name": "Basic"
    }
  }
}
if getattr(playbook.inputs, "azure_automation_account_tags", None):
  payload["tags"] = getattr(playbook.inputs, "azure_automation_account_tags", {})
inputs.input_parameters = str(payload)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.account_results
public_network_access = getattr(playbook.inputs, "azure_automation_account_public_network_access", True)
disable_local_auth = getattr(playbook.inputs, "azure_automation_account_disable_local_auth", False)

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  content = results.get("content", {})
  account_id = content.get("id", "")
  resourceGroup_start = account_id.find("resourceGroups/")+15
  resource_group = account_id[resourceGroup_start:account_id.find("/providers", resourceGroup_start)]
  
  row = incident.addRow("azure_automation_accounts")
  row["account_name_accounts"] = content.get("name", "")
  row["resource_group_accounts"] = resource_group
  row["location_accounts"] = content.get("location", "")
  row["tags_accounts"] = str(content.get("tags"))
  row["publicnetworkaccess_accounts"] = content.get("properties", {}).get("publicNetworkAccess", None)
  row["disablelocalauth_accounts"] = content.get("properties", {}).get("disableLocalAuth", None)
  row["account_deleted_accounts"] = False
  row["account_query_date"] = int(datetime.now().timestamp()*1000)
```

</p>
</details>

---
## Function - Azure Create Credential
Create or update a credential.

 ![screenshot: fn-azure-create-credential ](./doc/screenshots/fn-azure-create-credential.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `credential_name` | `text` | No | `-` | Name of the Azure automation credential |
| `credential_update` | `boolean` | No | `-` | If True will update the given credential. If False will create the given credential |
| `input_parameters` | `text` | No | `-` | string with dictionary format |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/credentials/tes43",
    "name": "tes43",
    "properties": {
      "creationTime": "2023-08-21T18:14:38.87+00:00",
      "description": null,
      "lastModifiedTime": "2023-08-21T18:14:38.87+00:00",
      "userName": "tes43"
    },
    "type": "Microsoft.Automation/AutomationAccounts/Credentials"
  },
  "inputs": {
    "account_name": "automation1",
    "credential_name": "tes43",
    "input_parameters": "{\u0027name\u0027: \u0027tes43\u0027, \u0027properties\u0027: {\u0027userName\u0027: \u0027tes43\u0027, \u0027password\u0027: \u0027password\u0027}}",
    "resource_group_name": "demoassets"
  },
  "metrics": {
    "execution_time_ms": 1506,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-21 14:14:38",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group
inputs.credential_name = playbook.inputs.azure_automation_credential_name

payload = {
  "name": playbook.inputs.azure_automation_credential_name,
  "properties": {
    "userName": playbook.inputs.azure_automation_credential_username,
    "password": playbook.inputs.azure_automation_credential_password
  }
}
if getattr(playbook.inputs, "azure_automation_credential_description", None):
  payload["properties"]["description"] = getattr(playbook.inputs, "azure_automation_credential_description", None)
inputs.input_parameters = str(payload)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.create_results
if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  # Add information to the data table
  row = incident.addRow("azure_automation_credentials")
  row["credential_name"] = playbook.inputs.azure_automation_credential_name
  row["credential_username"] = playbook.inputs.azure_automation_credential_username
  row["credential_description"] = getattr(playbook.inputs, 'azure_automation_credential_description', None)
  row["account_name_credentials"] = playbook.inputs.azure_automation_account_name
  row["resource_group_credentials"] = playbook.inputs.azure_automation_resource_group
  row["credential_deleted"] = False
  row["credential_query_date"] = int(datetime.now().timestamp()*1000)
```

</p>
</details>

---
## Function - Azure Create Schedule
Create or update a schedule.

 ![screenshot: fn-azure-create-schedule ](./doc/screenshots/fn-azure-create-schedule.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `input_parameters` | `text` | No | `-` | string with dictionary format |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |
| `schedule_name` | `text` | No | `The name of the azure automation schedule` | - |
| `schedule_update` | `boolean` | No | `-` | If True schedule will update. If False schedule will be created |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/schedules/tester1324",
    "name": "tester1324",
    "properties": {
      "advancedSchedule": null,
      "creationTime": "2023-08-24T15:31:44.2666667+00:00",
      "description": "something",
      "expiryTime": "2023-08-25T08:40:00+00:00",
      "expiryTimeOffsetMinutes": 0.0,
      "frequency": "OneTime",
      "interval": null,
      "isEnabled": true,
      "lastModifiedTime": "2023-08-24T15:31:44.2666667+00:00",
      "nextRun": "2023-08-25T08:40:00+00:00",
      "nextRunOffsetMinutes": 0.0,
      "startTime": "2023-08-25T08:40:00+00:00",
      "startTimeOffsetMinutes": 0.0,
      "timeZone": "Etc/UTC"
    },
    "type": "Microsoft.Automation/AutomationAccounts/Schedules"
  },
  "inputs": {
    "account_name": "automation1",
    "input_parameters": "{\u0027name\u0027: \u0027tester1324\u0027, \u0027properties\u0027: {\u0027startTime\u0027: 1692967200000, \u0027frequency\u0027: \u0027OneTime\u0027, \u0027description\u0027: \u0027something\u0027}}",
    "resource_group_name": "demoassets",
    "schedule_name": "tester1324"
  },
  "metrics": {
    "execution_time_ms": 30624,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-24 11:31:44",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group
inputs.schedule_name = playbook.inputs.azure_automation_schedule_name

payload = {
  "name": playbook.inputs.azure_automation_schedule_name,
  "properties": {
    "startTime": playbook.inputs.azure_automation_schedule_start_time,
    "frequency": "OneTime",
    "advancedSchedule": {}
  }
}

if getattr(playbook.inputs, "azure_automation_schedule_description", None): # Set the description
  payload["properties"]["description"] = getattr(playbook.inputs, "azure_automation_schedule_description", None)
if getattr(playbook.inputs, "schedule_time_zone", None): # Set the time zone
  payload["properties"]["timeZone"] = getattr(playbook.inputs, "schedule_time_zone", None)

frequency = getattr(playbook.inputs, "recur_frequency", None)
# If the frequency Recurring is selected
if playbook.inputs.schedule_recurrence == "Recurring":
  if frequency:
    payload["properties"]["frequency"] = frequency # Set user selected frequency
  else: # Fail if not given by user
    helper.fail("If Schedule Recurrence equals Recurring than Recur Frequency must be given.")
  payload["properties"]["interval"] = int(getattr(playbook.inputs, "recur_interval", 1)) # Add user given interval to payload
  # If an expiration date time is given then add it to the payload
  if getattr(playbook.inputs, "schedule_expiration", None):
    payload["properties"]["expiryTime"] = getattr(playbook.inputs, "schedule_expiration", None)
  # If the frequency selected equals Week, then add the user selected days to the payload
  if frequency == "Week":
    if getattr(playbook.inputs, "recur_week_days", []):
      # List of selected days
      payload["properties"]["advancedSchedule"]["weekDays"] = getattr(playbook.inputs, "recur_week_days", [])
    else:
      helper.fail("If Recur Frequency Week is selected than Recur Week Days must be given.")

inputs.input_parameters = str(payload)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.schedule
if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  # Add information to the data table
  schedule = results.get("content", {})
  row = incident.addRow("azure_automation_schedules")
  row["schedule_name"] = schedule.get("name", "")
  row["schedule_description"] = schedule.get("properties", {}).get("description", None)
  row["schedule_enabled"] = schedule.get("properties", {}).get("isEnabled", False)
  row["schedule_start_time"] = schedule.get("properties", {}).get("startTime", None)
  row["schedule_expiry_time"] = schedule.get("properties", {}).get("expiryTime", None)
  row["schedule_frequency"] = schedule.get("properties", {}).get("frequency", None)
  row["schedule_interval"] = str(schedule.get("properties", {}).get("interval", 1))
  row["schedule_time_zone"] = schedule.get("properties", {}).get("timeZone", None)
  row["advanced_schedule"] = str(schedule.get("properties", {}).get("advancedSchedule", {}))
  row["account_name_schedules"] = playbook.inputs.azure_automation_account_name
  row["resource_group_schedules"] = playbook.inputs.azure_automation_resource_group
  row["schedule_deleted"] = False
  row["schedule_query_row"] = int(datetime.now().timestamp()*1000)
```

</p>
</details>

---
## Function - Azure Delete Account
Delete an Azure automation account.

 ![screenshot: fn-azure-delete-account ](./doc/screenshots/fn-azure-delete-account.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "status": 200
  },
  "inputs": {
    "account_name": "test-account",
    "resource_group_name": "DemoAssets"
  },
  "metrics": {
    "execution_time_ms": 5098,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-07-25 08:24:31",
    "version": "1.0"
  },
  "raw": null,
  "reason": "",
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.account_name = row.account_name_accounts
inputs.resource_group_name = row.resource_group_accounts
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.account_delete

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  status = results.get("content", {}).get("status")
  if status == 200:
    row.account_deleted_accounts = True
    row.account_query_date = int(datetime.now().timestamp()*1000)
  elif status == 204:
    incident.addNote(f"""Azure Automation: Account Delete - Example (PB)
Inputs -
  Account Name: {playbook.inputs.azure_automation_account_name}
  Resource Group: {playbook.inputs.azure_automation_account_resource_group}

Results -
  Azure automation account '{playbook.inputs.azure_automation_account_name}' not found.""")
```

</p>
</details>

---
## Function - Azure Delete Credential
Delete the credential.

 ![screenshot: fn-azure-delete-credential ](./doc/screenshots/fn-azure-delete-credential.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `credential_name` | `text` | No | `-` | Name of the Azure automation credential |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "status": 200
  },
  "inputs": {
    "account_name": "automation1",
    "credential_name": "tes43",
    "resource_group_name": "demoassets"
  },
  "metrics": {
    "execution_time_ms": 1570,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-21 14:16:11",
    "version": "1.0"
  },
  "raw": null,
  "reason": "",
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.account_name = row.account_name_credentials
inputs.resource_group_name = row.resource_group_credentials
inputs.credential_name = row.credential_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.delete_cred

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  status = results.get("content", {}).get("status")
  if status == 200:
    row["credential_deleted"] = True
    row["credential_query_date"] = int(datetime.now().timestamp()*1000)
  elif status == 204:
    incident.addNote(f"""Azure Automation: Credential Delete - Example (PB)
Inputs -
  Account Name: {row.account_name}
  Resource Group: {row.resource_group}
  Credential Name: {row.credential_name}

Results -
  Azure automation credential '{row.credential_name}' not found.""")
```

</p>
</details>

---
## Function - Azure Delete Runbook
Delete the runbook by name.

 ![screenshot: fn-azure-delete-runbook ](./doc/screenshots/fn-azure-delete-runbook.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |
| `runbook_name` | `text` | No | `-` | Runbook name in Azure Automation |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "status": 200
  },
  "inputs": {
    "account_name": "automation1",
    "resource_group_name": "demoassets",
    "runbook_name": "test_fail"
  },
  "metrics": {
    "execution_time_ms": 3220,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-16 14:09:43",
    "version": "1.0"
  },
  "raw": null,
  "reason": "",
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.account_name = row.account_name_runbooks
inputs.resource_group_name = row.resource_group_runbooks
inputs.runbook_name = row.runbook_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.delete_runbook
if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  row.runbook_deleted = True
  row.runbook_query_date = int(datetime.now().timestamp()*1000)
```

</p>
</details>

---
## Function - Azure Delete Schedule
Delete the schedule identified by schedule name.

 ![screenshot: fn-azure-delete-schedule ](./doc/screenshots/fn-azure-delete-schedule.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |
| `schedule_name` | `text` | No | `The name of the azure automation schedule` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "status": 200
  },
  "inputs": {
    "account_name": "automation1",
    "resource_group_name": "demoassets",
    "schedule_name": "tester1324"
  },
  "metrics": {
    "execution_time_ms": 1244,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-24 11:38:33",
    "version": "1.0"
  },
  "raw": null,
  "reason": "",
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.account_name = row.account_name_schedules
inputs.resource_group_name = row.resource_group_schedules
inputs.schedule_name = row.schedule_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.delete_schedule

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  status = results.get("content", {}).get("status")
  if status == 200:
    row["schedule_deleted"] = True
    row["schedule_query_date"] = int(datetime.now().timestamp()*1000)
  elif status == 204:
    incident.addNote(f"""Azure Automation: Schedule Delete - Example (PB)
Inputs -
  Account Name: {row.account_name}
  Resource Group: {row.resource_group}
  Schedule Name: {row.schedule_name}

Results -
  Schedule '{row.schedule_name}' not found.""")
```

</p>
</details>

---
## Function - Azure Execute Runbook
Execute a given Azure runbook and retrieve the results

 ![screenshot: fn-azure-execute-runbook ](./doc/screenshots/fn-azure-execute-runbook.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `input_parameters` | `text` | No | `-` | string with dictionary format |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |
| `runbook_name` | `text` | No | `-` | Runbook name in Azure Automation |
| `time_to_wait` | `number` | No | `-` | Amount of seconds to wait in between Azure automation job status checks. This should be hold long it takes the given runbook to complete. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": "\r\nLocation              : eastus\r\nTags                  : {}\r\nJobCount              : 0\r\nRunbookType           : PowerShell\r\nParameters            : {}\r\nLogVerbose            : False\r\nLogProgress           : False\r\nLastModifiedBy        : \r\nState                 : Published\r\nResourceGroupName     : DemoAssets\r\nAutomationAccountName : automation1\r\nName                  : get_all_runbooks\r\nCreationTime          : 7/19/2023 3:39:27 PM +00:00\r\nLastModifiedTime      : 7/19/2023 4:03:24 PM +00:00\r\nDescription           : Return all runbooks\r\n\r\n\r\nEnvironments                                                                                                            \r\n------------                                                                                                            \r\n{[AzureChinaCloud, AzureChinaCloud], [AzureCloud, AzureCloud], [AzureGermanCloud, AzureGermanCloud], [AzureUSGovernme...\r\n\r\n",
  "inputs": {
    "account_name": "automation1",
    "input_parameters": "{\u0027runbook_name\u0027: \u0027get_all_runbooks\u0027}",
    "resource_group_name": "DemoAssets",
    "runbook_name": "Get_given_runbook",
    "time_to_wait": 20
  },
  "metrics": {
    "execution_time_ms": 41660,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-07-25 08:29:24",
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
inputs.account_name = row.account_name_runbooks
if getattr(playbook.inputs, "azure_automation_runbook_input_parameters", None):
  inputs.input_parameters = playbook.inputs.azure_automation_runbook_input_parameters
inputs.resource_group_name = row.resource_group_runbooks
inputs.runbook_name = row.runbook_name

time_to_wait = getattr(playbook.inputs, "time_to_wait", 30)
# If no time_to_wait is given then default to 30 seconds
inputs.time_to_wait = time_to_wait if time_to_wait else 30
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.runbook_results
if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  incident.addNote(f"""Azure Automation: Runbook Execute - Example (PB)
Inputs -
  Account Name: {row.account_name_runbooks}
  Resource Group: {row.resource_group_runbooks}
  Runbook Name: {row.runbook_name}
  Time to Wait: {getattr(playbook.inputs, 'time_to_wait', 30)}
  Input Parameters: {playbook.inputs.azure_automation_runbook_input_parameters}

Results -  
  {str(results.get('content', {}))}""")
```

</p>
</details>

---
## Function - Azure Get Account
Get a specified Azure automation account information or list accounts.

 ![screenshot: fn-azure-get-account ](./doc/screenshots/fn-azure-get-account.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "etag": null,
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/testing352",
    "identity": {
      "principalId": "ee616124-e026-4ca0-8c64-d34bae779faf",
      "tenantId": "50ad7d3e-b889-434d-802d-13b87c68047b",
      "type": "SystemAssigned"
    },
    "location": "eastus",
    "name": "testing352",
    "properties": {
      "RegistrationUrl": "https://99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5.agentsvc.eus.azure-automation.net/accounts/99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5",
      "RuntimeConfiguration": {
        "powershell": {
          "builtinModules": {
            "Az": "8.0.0"
          }
        },
        "powershell7": {
          "builtinModules": {
            "Az": "8.0.0"
          }
        }
      },
      "automationHybridServiceUrl": "https://99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5.jrds.eus.azure-automation.net/automationAccounts/99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5",
      "creationTime": "2023-07-25T12:05:22.16+00:00",
      "disableLocalAuth": false,
      "encryption": {
        "identity": {
          "userAssignedIdentity": null
        },
        "keySource": "Microsoft.Automation"
      },
      "lastModifiedBy": null,
      "lastModifiedTime": "2023-07-25T12:05:22.16+00:00",
      "privateEndpointConnections": [],
      "publicNetworkAccess": true,
      "sku": {
        "capacity": null,
        "family": null,
        "name": "Basic"
      },
      "state": "Ok"
    },
    "systemData": {
      "createdAt": "2023-07-25T12:05:22.16+00:00",
      "lastModifiedAt": "2023-07-25T12:05:22.16+00:00"
    },
    "tags": {},
    "type": "Microsoft.Automation/AutomationAccounts"
  },
  "inputs": {
    "account_name": "testing352",
    "resource_group_name": "DemoAssets"
  },
  "metrics": {
    "execution_time_ms": 1433,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-07-27 14:14:45",
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
if getattr(playbook.inputs, "azure_automation_account_name", None):
  inputs.account_name = playbook.inputs.azure_automation_account_name
if getattr(playbook.inputs, "azure_automation_resource_group_name", None):
  inputs.resource_group_name = playbook.inputs.azure_automation_resource_group_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.account_info

def add_to_row(account):
  account_id = account.get("id", "")
  resourceGroup_start = account_id.find("resourceGroups/")+15
  resource_group = account_id[resourceGroup_start:account_id.find("/providers", resourceGroup_start)]

  row = incident.addRow("azure_automation_accounts")
  row["account_name_accounts"] = account.get("name", "")
  row["resource_group_accounts"] = resource_group
  row["location_accounts"] = account.get("location", "")
  row["tags_accounts"] = str(account.get("tags"))
  row["publicnetworkaccess_accounts"] = account.get("properties", {}).get("publicNetworkAccess", None)
  row["disablelocalauth_accounts"] = account.get("properties", {}).get("disableLocalAuth", None)
  row["account_deleted_accounts"] = False
  row["account_query_date"] = int(datetime.now().timestamp()*1000)

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  content = results.get("content", {})
  if content.get("value", None):
    for account in content.get("value", []):
      add_to_row(account)
  else:
    add_to_row(content)
```

</p>
</details>

---
## Function - Azure Get Agent Registration Information
Retrieve the automation agent registration information.

 ![screenshot: fn-azure-get-agent-registration-information ](./doc/screenshots/fn-azure-get-agent-registration-information.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "dscMetaConfiguration": "\r\n\tinstance of MSFT_WebDownloadManager as $MSFT_WebDownloadManager1ref\r\n\t{\r\n\tResourceID = \"[ConfigurationRepositoryWeb]AzureAutomationDSC\";\r\n\t SourceInfo = \"C:\\\\OaaS-RegistrationMetaConfig2.ps1::20::9::ConfigurationRepositoryWeb\";\r\n\t RegistrationKey = \"1234RYKSRuyfmINzCvic0Oz7DpGskIbty5W12345QbKWlsYT0BGp6qzfwz12345678vuh28cqRMoxDD39Iut7w==\"; \r\n\t ServerURL = \"https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6\";\r\n\t};\r\n\r\n\tinstance of MSFT_WebResourceManager as $MSFT_WebResourceManager1ref\r\n\t{\r\n\t SourceInfo = \"C:\\\\OaaS-RegistrationMetaConfig2.ps1::27::9::ResourceRepositoryWeb\";\r\n\t ServerURL = \"https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6\";\r\n\t ResourceID = \"[ResourceRepositoryWeb]AzureAutomationDSC\";\r\n\t RegistrationKey = \"1234RYKSRuyfmINzC*******pGskIbty5W12345QbKWlsYT0BGp6qzfwz12345678vuh28cqRMoxDD39Iut7w==\"; \r\n\t};\r\n\r\n\tinstance of MSFT_WebReportManager as $MSFT_WebReportManager1ref\r\n\t{\r\n\t SourceInfo = \"C:\\\\OaaS-RegistrationMetaConfig2.ps1::34::9::ReportServerWeb\";\r\n\t ServerURL = \"https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6\";\r\n\t ResourceID = \"[ReportServerWeb]AzureAutomationDSC\";\r\n\t RegistrationKey = \"1234RYKSRuyfmINzCvic0Oz7DpGskIbty5W12345QbKWlsYT0BGp6qzfwz12345678vuh28cqRMoxDD39Iut7w==\"; \r\n\t};\r\n\r\n\tinstance of MSFT_DSCMetaConfiguration as $MSFT_DSCMetaConfiguration1ref\r\n\t{\r\n\t RefreshMode = \"Pull\";\r\n\t AllowModuleOverwrite = False;\r\n\t ActionAfterReboot = \"ContinueConfiguration\";\r\n\t RefreshFrequencyMins = 30;\r\n\t RebootNodeIfNeeded = False;\r\n\t ConfigurationModeFrequencyMins = 15;\r\n\t ConfigurationMode = \"ApplyAndMonitor\";\r\n\r\n\t  ResourceModuleManagers = {\r\n\t  $MSFT_WebResourceManager1ref  \r\n\t};\r\n\t  ReportManagers = {\r\n\t  $MSFT_WebReportManager1ref  \r\n\t };\r\n\t  ConfigurationDownloadManagers = {\r\n\t  $MSFT_WebDownloadManager1ref  \r\n\t };\r\n\t};\r\n\r\n\tinstance of OMI_ConfigurationDocument\r\n\t{\r\n\t Version=\"2.0.0\";\r\n\t MinimumCompatibleVersion = \"2.0.0\";\r\n\t CompatibleVersionAdditionalProperties= { \"MSFT_DSCMetaConfiguration:StatusRetentionTimeInDays\" };\r\n\t Author=\"azureautomation\";\r\n\t GenerationDate=\"04/17/2015 11:41:09\";\r\n\t GenerationHost=\"azureautomation-01\";\r\n\t Name=\"RegistrationMetaConfig\";\r\n\t};\r\n\t",
    "endpoint": "https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6",
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/agentRegistrationInformation/https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6",
    "keys": {
      "primary": "1234RYKSRuyfmI*******7DpGskIbty5W12345QbKWlsYT0BGp6qzfwz12345678vuh28cqRMoxDD39Iut7w==",
      "secondary": "bC6hr123456789qP*******rDRqfJMnJmUOhP123450/x53Vezc3rqDhherrLzb123456MWhub+86IKwxssg=="
    }
  },
  "inputs": {
    "account_name": "automation1",
    "resource_group_name": "demoassets"
  },
  "metrics": {
    "execution_time_ms": 1725,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-21 09:45:31",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from json import dumps
results = playbook.functions.results.registration_info

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  incident.addNote(f"""Azure Automation: Agent Registration Get Information - Example (PB)
Inputs -
  Account Name: {playbook.inputs.azure_automation_account_name}
  Resource Group Name: {playbook.inputs.azure_automation_resource_group_name}

Results -
  {dumps(results.get('content', {}), indent=4)}""")
```

</p>
</details>

---
## Function - Azure Get Credential
Get credential from given credential name or list all credentials on given resource group.

 ![screenshot: fn-azure-get-credential ](./doc/screenshots/fn-azure-get-credential.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `credential_name` | `text` | No | `-` | Name of the Azure automation credential |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/credentials/tes43",
    "name": "tes43",
    "properties": {
      "creationTime": "2023-08-21T18:14:38.87+00:00",
      "description": null,
      "lastModifiedTime": "2023-08-21T18:14:38.87+00:00",
      "userName": "tes43"
    },
    "type": "Microsoft.Automation/AutomationAccounts/Credentials"
  },
  "inputs": {
    "account_name": "automation1",
    "credential_name": "tes43",
    "resource_group_name": "demoassets"
  },
  "metrics": {
    "execution_time_ms": 1393,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-21 14:15:23",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group
if getattr(playbook.inputs, "azure_automation_credential_name", None):
  inputs.credential_name = getattr(playbook.inputs, "azure_automation_credential_name", None)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.cred

# Add credential information to data table
def add_to_row(credential):
  row = incident.addRow("azure_automation_credentials")
  row["credential_name"] = credential.get("name")
  row["credential_username"] = credential.get("properties", {}).get("userName")
  row["credential_description"] = credential.get("properties", {}).get("description")
  row["account_name_credentials"] = playbook.inputs.azure_automation_account_name
  row["resource_group_credentials"] = playbook.inputs.azure_automation_resource_group
  row["credential_deleted"] = False
  row["credential_query_date"] = int(datetime.now().timestamp()*1000)

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  content = results.get('content', {})
  if content.get("value", []):
    # If list of credentials returned
    for credential in content.get("value", []):
      add_to_row(credential)
  elif content.get("name", None): # If single credential returned
    add_to_row(content)
```

</p>
</details>

---
## Function - Azure Get Job
Retrieve the job info or job output identified by job name or list jobs.

 ![screenshot: fn-azure-get-job ](./doc/screenshots/fn-azure-get-job.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `job_name` | `text` | No | `-` | Azure Automation job name |
| `job_output` | `boolean` | No | `-` | If True will return Job output. If False will return job details |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/jobs/1692024049238",
    "name": "1692024049238",
    "properties": {
      "creationTime": "2023-08-14T14:42:29.5306946+00:00",
      "endTime": "2023-08-14T14:42:55.9297673+00:00",
      "exception": null,
      "jobId": "efe4db52-a124-4bea-9582-7b0c7f7133e4",
      "lastModifiedTime": "2023-08-14T14:42:55.9297673+00:00",
      "lastStatusModifiedTime": "2023-08-14T14:42:55.9297673+00:00",
      "parameters": {
        "runbook_name": "get_all_runbooks"
      },
      "provisioningState": "Succeeded",
      "runOn": "",
      "runbook": {
        "name": "Get_given_runbook"
      },
      "startTime": "2023-08-14T14:42:41.9604553+00:00",
      "startedBy": "{scrubbed}",
      "status": "Completed",
      "statusDetails": "None"
    },
    "type": "Microsoft.Automation/AutomationAccounts/Jobs"
  },
  "inputs": {
    "account_name": "automation1",
    "job_name": "1692024049238",
    "resource_group_name": "demoassets"
  },
  "metrics": {
    "execution_time_ms": 533,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-16 14:52:41",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group_name
if getattr(playbook.inputs, "azure_automation_job_name", None):
  inputs.job_name = playbook.inputs.azure_automation_job_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from json import dumps
results = playbook.functions.results.job_results
if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  incident.addNote(f"""Azure Automation: Job Get - Example (PB)
Inputs -
  Account Name: {playbook.inputs.azure_automation_account_name}
  Resource Group: {playbook.inputs.azure_automation_resource_group_name}
  Job Name: {getattr(playbook.inputs, 'azure_automation_job_name', None)}

Results -
  {dumps(results.get('content', {}), indent=4)}""")
```

</p>
</details>

---
## Function - Azure Get Module Activity
Retrieve the activity in the module identified by module name and activity name or 
Retrieve a list of activities in the module identified by module name.

 ![screenshot: fn-azure-get-module-activity ](./doc/screenshots/fn-azure-get-module-activity.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `activity_name` | `text` | No | `-` | The Azure automation module activity name |
| `module_name` | `text` | No | `-` | The name of the Azure automation module. |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/modules/Az.Advisor/activities/Set-AzAdvisorConfiguration",
    "name": "Set-AzAdvisorConfiguration",
    "properties": {
      "creationTime": "2022-07-06T10:01:53.9133333+00:00",
      "definition": "",
      "description": "Updates or creates the Azure Advisor Configuration. ^https://docs.microsoft.com/powershell/module/az.advisor/set-azadvisorConfiguration^",
      "lastModifiedTime": "2022-07-06T10:01:53.9133333+00:00",
      "outputTypes": [
        {
          "name": "Microsoft.Azure.Commands.Advisor.Cmdlets.Models.PsAzureAdvisorConfigurationData",
          "type": "Microsoft.Azure.Commands.Advisor.Cmdlets.Models.PsAzureAdvisorConfigurationData"
        }
      ],
      "parameterSets": [
        {
          "name": "InputObjectLowCpuExcludeParameterSet",
          "parameters": [
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "DefaultProfile",
              "position": -2147483648,
              "type": "Microsoft.Azure.Commands.Common.Authentication.Abstractions.Core.IAzureContextContainer",
              "validationSet": [],
              "valueFromPipeline": false,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            },
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "Exclude",
              "position": 2,
              "type": "System.Management.Automation.SwitchParameter",
              "validationSet": [],
              "valueFromPipeline": false,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            },
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": true,
              "name": "LowCpuThreshold",
              "position": 0,
              "type": "System.Int32",
              "validationSet": [],
              "valueFromPipeline": false,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            },
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "WhatIf",
              "position": -2147483648,
              "type": "System.Management.Automation.SwitchParameter",
              "validationSet": [],
              "valueFromPipeline": false,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            },
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "InputObject",
              "position": 1,
              "type": "Microsoft.Azure.Commands.Advisor.Cmdlets.Models.PsAzureAdvisorConfigurationData",
              "validationSet": [],
              "valueFromPipeline": true,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            },
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "Confirm",
              "position": -2147483648,
              "type": "System.Management.Automation.SwitchParameter",
              "validationSet": [],
              "valueFromPipeline": false,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            }
          ]
        },
        {
          "name": "InputObjectRgExcludeParameterSet",
          "parameters": [
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "InputObject",
              "position": 1,
              "type": "Microsoft.Azure.Commands.Advisor.Cmdlets.Models.PsAzureAdvisorConfigurationData",
              "validationSet": [],
              "valueFromPipeline": true,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            },
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "Exclude",
              "position": 2,
              "type": "System.Management.Automation.SwitchParameter",
              "validationSet": [],
              "valueFromPipeline": false,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            },
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "Confirm",
              "position": -2147483648,
              "type": "System.Management.Automation.SwitchParameter",
              "validationSet": [],
              "valueFromPipeline": false,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            },
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "ResourceGroupName",
              "position": 0,
              "type": "System.String",
              "validationSet": [],
              "valueFromPipeline": false,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            },
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "WhatIf",
              "position": -2147483648,
              "type": "System.Management.Automation.SwitchParameter",
              "validationSet": [],
              "valueFromPipeline": false,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            },
            {
              "description": null,
              "isDynamic": false,
              "isMandatory": false,
              "name": "DefaultProfile",
              "position": -2147483648,
              "type": "Microsoft.Azure.Commands.Common.Authentication.Abstractions.Core.IAzureContextContainer",
              "validationSet": [],
              "valueFromPipeline": false,
              "valueFromPipelineByPropertyName": false,
              "valueFromRemainingArguments": false
            }
          ]
        }
      ],
      "type": null
    },
    "type": null
  },
  "inputs": {
    "account_name": "automation1",
    "activity_name": "Set-AzAdvisorConfiguration",
    "module_name": "Az.Advisor",
    "resource_group_name": "demoassets"
  },
  "metrics": {
    "execution_time_ms": 2203,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-14 10:52:19",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.module_name = playbook.inputs.azure_automation_module_name
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group_name

if getattr(playbook.inputs, "azure_automation_activity_name", None):
  inputs.activity_name = playbook.inputs.azure_automation_activity_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from json import dumps
results = playbook.functions.results.module_activity

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  incident.addNote(f"""Azure Automation: Module Get Activity - Example (PB)
Inputs -
  Account Name: {playbook.inputs.azure_automation_account_name}
  Resource Group: {playbook.inputs.azure_automation_resource_group_name}
  Module Name: {playbook.inputs.azure_automation_module_name}
  Activity Name: {getattr(playbook.inputs, 'azure_automation_activity_name', None)}

Results -
  {dumps(results.get('content', {}), indent=4)}""")
```

</p>
</details>

---
## Function - Azure Get Node Report
Retrieve the Dsc node report data by node id and report id or
List Dsc node reports by node id.

 ![screenshot: fn-azure-get-node-report ](./doc/screenshots/fn-azure-get-node-report.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `node_id` | `text` | Yes | `-` | Azure Automation Dsc node ID |
| `report_id` | `text` | No | `-` | Azure Automation Dsc node report ID |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "configurationVersion": "2.0.0",
    "endTime": "2023-09-06T13:30:02.1606975+00:00",
    "errors": [],
    "hostName": null,
    "iPV4Addresses": [],
    "iPV6Addresses": [],
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/nodes/24939717-e819-4059-aa08-82862c65f3c8/reports/3c47f0b6-aeb7-429a-a656-70f2a19ab22a",
    "lastModifiedTime": "2023-09-06T13:30:02.2533333+00:00",
    "metaConfiguration": null,
    "numberOfResources": 0,
    "rawErrors": null,
    "rebootRequested": null,
    "refreshMode": null,
    "reportFormatVersion": "2.0",
    "reportId": "3c47f0b6-aeb7-429a-a656-70f2a19ab22a",
    "resources": [],
    "startTime": "2023-09-06T13:30:01.9451859+00:00",
    "status": "Compliant",
    "type": "Consistency"
  },
  "inputs": {
    "account_name": "automation1",
    "node_id": "24939717-e819-4059-aa08-82862c65f3c8",
    "report_id": "3c47f0b6-aeb7-429a-a656-70f2a19ab22a",
    "resource_group_name": "DemoAssets"
  },
  "metrics": {
    "execution_time_ms": 1084,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-09-06 09:55:00",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.node_id = playbook.inputs.azure_automation_node_id
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group_name
if getattr(playbook.inputs, "azure_automation_report_id", None):
  inputs.report_id = playbook.inputs.azure_automation_report_id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from json import dumps
results = playbook.functions.results.node_report

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  incident.addNote(f"""Azure Automation: Node Get Report - Example (PB)
Inputs -
  Account Name: {playbook.inputs.azure_automation_account_name}
  Resource Group: {playbook.inputs.azure_automation_resource_group_name}
  Node ID: {playbook.inputs.azure_automation_node_id}
  Report ID: {getattr(playbook.inputs, 'azure_automation_report_id', None)}

Results -
  {dumps(results.get('content', {}), indent=4)}""")
```

</p>
</details>

---
## Function - Azure Get Runbook
Retrieve the runbook identified by runbook name or list runbooks on given account.

 ![screenshot: fn-azure-get-runbook ](./doc/screenshots/fn-azure-get-runbook.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |
| `runbook_name` | `text` | No | `-` | Runbook name in Azure Automation |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "etag": "\"638246066435733333\"",
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/runbooks/Hello_world",
    "location": "eastus",
    "name": "Hello_world",
    "properties": {
      "creationTime": "2023-07-10T17:22:53.7066667+00:00",
      "description": "My first python 3 runbook",
      "draft": null,
      "jobCount": 0,
      "lastModifiedBy": null,
      "lastModifiedTime": "2023-07-10T17:24:03.5733333+00:00",
      "logActivityTrace": 0,
      "logProgress": false,
      "logVerbose": false,
      "outputTypes": [],
      "parameters": {},
      "provisioningState": "Succeeded",
      "runbookType": "Python3",
      "serviceManagementTags": null,
      "state": "Published"
    },
    "tags": {},
    "type": "Microsoft.Automation/AutomationAccounts/Runbooks"
  },
  "inputs": {
    "account_name": "automation1",
    "resource_group_name": "demoassets",
    "runbook_name": "Hello_world"
  },
  "metrics": {
    "execution_time_ms": 7989,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-16 10:20:00",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.resource_group_name = playbook.inputs.azure_resource_group
if getattr(playbook.inputs, 'azure_automation_runbook_name', None):
  inputs.runbook_name = playbook.inputs.azure_automation_runbook_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.runbook_results

# Add runbooks info to the data table
def add_to_row(runbook):
  row = incident.addRow("azure_automation_runbooks")
  row["runbook_name"] = runbook.get("name")
  row["runbook_type"] = runbook.get("properties", {}).get("runbookType")
  row["runbook_state"] = runbook.get("properties", {}).get("state")
  row["runbook_tags"] = str(runbook.get("tags"))
  row["account_name_runbooks"] = playbook.inputs.azure_automation_account_name
  row["resource_group_runbooks"] = playbook.inputs.azure_resource_group
  row["runbook_deleted"] = False
  row["runbook_query_date"] = int(datetime.now().timestamp()*1000)

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  content = results.get("content", {})
  if content.get("value", None):
    # If list of runbooks returned
    for runbook in content.get("value", []):
      add_to_row(runbook)
  else: # If single runbook returned
    add_to_row(content)
```

</p>
</details>

---
## Function - Azure Get Schedule
Retrieve the schedule identified by schedule name or list schedules.

 ![screenshot: fn-azure-get-schedule ](./doc/screenshots/fn-azure-get-schedule.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |
| `schedule_name` | `text` | No | `The name of the azure automation schedule` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/demoassets/providers/Microsoft.Automation/automationAccounts/automation1/schedules/tester1324",
    "name": "tester1324",
    "properties": {
      "advancedSchedule": null,
      "creationTime": "2023-08-24T15:31:44.2666667+00:00",
      "description": "something",
      "expiryTime": "2023-08-25T08:40:00+00:00",
      "expiryTimeOffsetMinutes": 0.0,
      "frequency": "OneTime",
      "interval": null,
      "isEnabled": true,
      "lastModifiedTime": "2023-08-24T15:31:44.2666667+00:00",
      "nextRun": "2023-08-25T08:40:00+00:00",
      "nextRunOffsetMinutes": 0.0,
      "startTime": "2023-08-25T08:40:00+00:00",
      "startTimeOffsetMinutes": 0.0,
      "timeZone": "Etc/UTC"
    },
    "type": "Microsoft.Automation/AutomationAccounts/Schedules"
  },
  "inputs": {
    "account_name": "automation1",
    "resource_group_name": "demoassets",
    "schedule_name": "tester1324"
  },
  "metrics": {
    "execution_time_ms": 1586,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-24 11:33:14",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group
if getattr(playbook.inputs, "azure_automation_schedule_name", None):
  inputs.schedule_name = playbook.inputs.azure_automation_schedule_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.get_schedule

# Add schedule information to data table
def row_to_add(schedule):
  row = incident.addRow("azure_automation_schedules")
  row["schedule_name"] = schedule.get("name", "")
  row["schedule_description"] = schedule.get("properties", {}).get("description", None)
  row["schedule_enabled"] = schedule.get("properties", {}).get("isEnabled", False)
  row["schedule_start_time"] = schedule.get("properties", {}).get("startTime", None)
  row["schedule_expiry_time"] = schedule.get("properties", {}).get("expiryTime", None)
  row["schedule_frequency"] = schedule.get("properties", {}).get("frequency", None)
  row["schedule_interval"] = schedule.get("properties", {}).get("interval", 1)
  row["schedule_time_zone"] = schedule.get("properties", {}).get("timeZone", None)
  row["advanced_schedule"] = str(schedule.get("properties", {}).get("advancedSchedule", {}))
  row["account_name_schedules"] = playbook.inputs.azure_automation_account_name
  row["resource_group_schedules"] = playbook.inputs.azure_automation_resource_group
  row["schedule_deleted"] = False
  row["schedule_query_date"] = int(datetime.now().timestamp()*1000)

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  content = results.get("content", {})
  if content.get("value", None):
    # If list of schedules returned
    for schedule in content.get("value", []):
      row_to_add(schedule)
  else: # If single schedule returned
    row_to_add(content)
```

</p>
</details>

---
## Function - Azure List Statistics by Automation Account
Retrieve the statistics for the account.

 ![screenshot: fn-azure-list-statistics-by-automation-account ](./doc/screenshots/fn-azure-list-statistics-by-automation-account.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "value": [
      {
        "counterProperty": "New",
        "counterValue": 0,
        "endTime": "2023-09-06T13:58:01.5985342+00:00",
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/statistics/New",
        "startTime": "2023-08-30T13:58:01.5985342+00:00"
      },
      {
        "counterProperty": "Activating",
        "counterValue": 0,
        "endTime": "2023-09-06T13:58:01.5985342+00:00",
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/statistics/Activating",
        "startTime": "2023-08-30T13:58:01.5985342+00:00"
      },
      {
        "counterProperty": "Running",
        "counterValue": 0,
        "endTime": "2023-09-06T13:58:01.5985342+00:00",
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/statistics/Running",
        "startTime": "2023-08-30T13:58:01.5985342+00:00"
      },
      {
        "counterProperty": "Completed",
        "counterValue": 0,
        "endTime": "2023-09-06T13:58:01.5985342+00:00",
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/statistics/Completed",
        "startTime": "2023-08-30T13:58:01.5985342+00:00"
      },
      {
        "counterProperty": "Failed",
        "counterValue": 0,
        "endTime": "2023-09-06T13:58:01.5985342+00:00",
        "id": "/subscriptions/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/automation1/statistics/Failed",
        "startTime": "2023-08-30T13:58:01.5985342+00:00"
      }
    ]
  },
  "inputs": {
    "account_name": "automation1",
    "resource_group_name": "DemoAssets"
  },
  "metrics": {
    "execution_time_ms": 773,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-09-06 09:58:01",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from datetime import datetime
results = playbook.functions.results.statistics

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  for stat in results.get("content", {}).get("value", []):
    row = incident.addRow("azure_automation_statistics")
    row["statistic_counter_property"] = stat.get("counterProperty", None)
    row["statistic_counter_value"] = stat.get("counterValue", 0)
    row["account_name_statistics"] = playbook.inputs.azure_automation_account_name
    row["resource_group_statistics"] = playbook.inputs.azure_automation_resource_group_name
    row["statistic_query_date"] = int(datetime.now().timestamp()*1000)
```

</p>
</details>

---
## Function - Azure Regenerate Agent Registration Key
Regenerate a primary or secondary agent registration key

 ![screenshot: fn-azure-regenerate-agent-registration-key ](./doc/screenshots/fn-azure-regenerate-agent-registration-key.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `account_name` | `text` | No | `-` | Azure Automation Account Name |
| `input_parameters` | `text` | No | `-` | string with dictionary format |
| `resource_group_name` | `text` | No | `-` | Existing Azure automation resource group name  |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "dscMetaConfiguration": null,
    "endpoint": "https://abcdefgh-1234-abcd-1234-a1b2c3d4e5f6.agentsvc.eus.azure-automation.net/accounts/abcdefgh-1234-abcd-1234-a1b2c3d4e5f6",
    "id": null,
    "keys": {
      "primary": "g+Z4E/12345678c/YbuFnwTe4yI12EYPRTdmFHVj+SI12345b0R8ghU8YNWe7BM3hjYDCzkqWhZGd0r5V4YHag==",
      "secondary": "bC6hr123456789qPD2eeowEt9rDRqfJMnJmUOhP123450/x53Vezc3rqDhherrLzb123456MWhub+86IKwxssg=="
    }
  },
  "inputs": {
    "account_name": "automation1",
    "input_parameters": "{\u0027keyName\u0027: \u0027primary\u0027}",
    "resource_group_name": "demoassets"
  },
  "metrics": {
    "execution_time_ms": 1104,
    "host": "local",
    "package": "fn-azure-automation-utilities",
    "package_version": "1.0.0",
    "timestamp": "2023-08-21 09:53:13",
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
inputs.account_name = playbook.inputs.azure_automation_account_name
inputs.resource_group_name = playbook.inputs.azure_automation_resource_group
inputs.input_parameters = str({"keyName": playbook.inputs.azure_automation_agent_key_to_regenerate})
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
from json import dumps
results = playbook.functions.results.registration_key

if results.get("success"):
  incident.properties.azure_automation_create_ui_tab = True
  incident.addNote(f"""Azure Automation: Agent Registration Regenerate Key - Example (PB)
Inputs -
  Account Name: {playbook.inputs.azure_automation_account_name}
  Resource Group: {playbook.inputs.azure_automation_resource_group}
  Key to Regenerate: {playbook.inputs.azure_automation_agent_key_to_regenerate}

Results -
  {dumps(results.get('content', {}), indent=4)}""")
```

</p>
</details>

---


## Playbooks
| Playbook Name | Description | Activation Type | Object | Status | Condition | 
| ------------- | ----------- | --------------- | ------ | ------ | --------- | 
| Azure Automation: Account Delete - Example (PB) | Delete an Azure automation account | Manual | azure_automation_accounts | `enabled` | `azure_automation_accounts.account_deleted_accounts not_equals True AND azure_automation_accounts.account_name_accounts has_a_value AND azure_automation_accounts.resource_group_accounts has_a_value` | 
| Azure Automation: Account Update - Example (PB) | Update an automation account. | Manual | azure_automation_accounts | `enabled` | `azure_automation_accounts.account_deleted_accounts not_equals True AND azure_automation_accounts.account_name_accounts has_a_value AND azure_automation_accounts.resource_group_accounts has_a_value` | 
| Azure Automation: Credential Delete - Example (PB) | Delete a credential | Manual | azure_automation_credentials | `enabled` | `azure_automation_credentials.account_name_credentials has_a_value AND azure_automation_credentials.credential_deleted not_equals True AND azure_automation_credentials.credential_name has_a_value AND azure_automation_credentials.resource_group_credentials has_a_value` | 
| Azure Automation: Credential Update - Example (PB) | Update a credential. | Manual | azure_automation_credentials | `enabled` | `azure_automation_credentials.account_name_credentials has_a_value AND azure_automation_credentials.credential_deleted not_equals True AND azure_automation_credentials.credential_name has_a_value AND azure_automation_credentials.resource_group_credentials has_a_value` | 
| Azure Automation: Runbook Delete - Example (PB) | Delete an Azure runbook | Manual | azure_automation_runbooks | `enabled` | `azure_automation_runbooks.account_name_runbooks has_a_value AND azure_automation_runbooks.resource_group_runbooks has_a_value AND azure_automation_runbooks.runbook_deleted not_equals True AND azure_automation_runbooks.runbook_name has_a_value` | 
| Azure Automation: Runbook Execute - Example (PB) | Execute a runbook on Azure | Manual | azure_automation_runbooks | `enabled` | `azure_automation_runbooks.account_name_runbooks has_a_value AND azure_automation_runbooks.resource_group_runbooks has_a_value AND azure_automation_runbooks.runbook_name has_a_value` | 
| Azure Automation: Schedule Delete - Example (PB) | Delete the schedule identified by schedule name. | Manual | azure_automation_schedules | `enabled` | `azure_automation_schedules.account_name_schedules has_a_value AND azure_automation_schedules.resource_group_schedules has_a_value AND azure_automation_schedules.schedule_deleted not_equals True AND azure_automation_schedules.schedule_name has_a_value` | 
| Azure Automation: Schedule Update - Example (PB) | Update the schedule identified by schedule name. | Manual | azure_automation_schedules | `enabled` | `azure_automation_schedules.account_name_schedules has_a_value AND azure_automation_schedules.resource_group_schedules has_a_value AND azure_automation_schedules.schedule_deleted not_equals True AND azure_automation_schedules.schedule_name has_a_value` | 
| Azure Automation: Account Create - Example (PB) | Create an Azure automation account | Manual | incident | `enabled` | `-` | 
| Azure Automation: Credential Create - Example (PB) | Create a credential | Manual | incident | `enabled` | `-` | 
| Azure Automation: Schedule Create - Example (PB) | Create a schedule. | Manual | incident | `enabled` | `-` | 
| Azure Automation: Account Get - Example (PB) | Get the details of the given Azure automation account. | Manual | incident | `enabled` | `-` | 
| Azure Automation: Agent Registration Get Information - Example (PB) | Retrieve the automation agent registration information. | Manual | incident | `enabled` | `-` | 
| Azure Automation: Credential Get - Example (PB) | Get credential from given credential name or list all credentials on given resource group. | Manual | incident | `enabled` | `-` | 
| Azure Automation: Job Get - Example (PB) | Retrieve the job identified by job name. | Manual | incident | `enabled` | `-` | 
| Azure Automation: Job Get Output - Example (PB) | Retrieve the job output identified by job name. | Manual | incident | `enabled` | `-` | 
| Azure Automation: Module Get Activity - Example (PB) | Retrieve the activity in the module identified by module name and activity name. | Manual | incident | `enabled` | `-` | 
| Azure Automation: DSC Node Get Report - Example (PB) | Retrieve the Dsc node report data by node id and report id or List Dsc node reports by node id. | Manual | incident | `enabled` | `-` | 
| Azure Automation: Runbook Get - Example (PB) | Retrieve the runbook identified by runbook name. | Manual | incident | `enabled` | `-` | 
| Azure Automation: Schedule Get - Example (PB) | Retrieve the schedule identified by schedule name. | Manual | incident | `enabled` | `-` | 
| Azure Automation: Statistics List by Automation Account - Example (PB) | Retrieve the statistics for the account. | Manual | incident | `enabled` | `-` | 
| Azure Automation: Agent Registration Regenerate Key - Example (PB) | Regenerate a primary or secondary agent registration key | Manual | incident | `enabled` | `-` | 

---

## Data Table - Azure Automation Accounts

 ![screenshot: dt-azure-automation-accounts](./doc/screenshots/dt-azure-automation-accounts.png)

#### API Name:
azure_automation_accounts

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Deleted | `account_deleted_accounts` | `boolean` | If the account has been deleted or not |
| disableLocalAuth | `disablelocalauth_accounts` | `boolean` | Either disable or enable local Auth. A value of True would mean local auth is disabled. |
| Location | `location_accounts` | `text` | The region the account is in |
| Name | `account_name_accounts` | `text` | Azure Automation Account Name |
| publicNetworkAccess | `publicnetworkaccess_accounts` | `boolean` | Either allow or deny access to public network from account |
| Query Date | `account_query_date` | `datetimepicker` | Time the query to get this information was run |
| Resource Group | `resource_group_accounts` | `text` | Azure Automation resource group name |
| Tags | `tags_accounts` | `text` | dictionary of Azure automation account tags |

---
## Data Table - Azure Automation Credentials

 ![screenshot: dt-azure-automation-credentials](./doc/screenshots/dt-azure-automation-credentials.png)

#### API Name:
azure_automation_credentials

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Account Name | `account_name_credentials` | `text` | Name fo the account the credential is on |
| Deleted | `credential_deleted` | `boolean` | If the credential is deleted |
| Description | `credential_description` | `text` | Description for the credential |
| Name | `credential_name` | `text` | Name of the credential |
| Query Date | `credential_query_date` | `datetimepicker` | Time the query was run to get this information |
| Resource Group | `resource_group_credentials` | `text` | Resource group the credential is on |
| Username | `credential_username` | `text` | Username for the credential |

---
## Data Table - Azure Automation Runbooks

 ![screenshot: dt-azure-automation-runbooks](./doc/screenshots/dt-azure-automation-runbooks.png)

#### API Name:
azure_automation_runbooks

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Account Name | `account_name_runbooks` | `text` | Name of the account the runbook is on |
| Deleted | `runbook_deleted` | `boolean` | If the runbook as been deleted or not |
| Name | `runbook_name` | `text` | Name of the runbook |
| Query Date | `runbook_query_date` | `datetimepicker` | Time the query to get this information was run |
| Resource Group | `resource_group_runbooks` | `text` | The resource group the account is on |
| State | `runbook_state` | `text` | State of the runbook |
| Tags | `runbook_tags` | `text` | Tags given to the runbook |
| Type | `runbook_type` | `text` | Type of runbook |

---
## Data Table - Azure Automation Schedules

 ![screenshot: dt-azure-automation-schedules](./doc/screenshots/dt-azure-automation-schedules.png)

#### API Name:
azure_automation_schedules

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Account Name | `account_name_schedules` | `text` | Azure automation account name |
| Advanced Schedule | `advanced_schedule` | `text` | The advanced schedule properties |
| Deleted | `schedule_deleted` | `boolean` | If the schedule is deleted or not |
| Description | `schedule_description` | `text` | Description of the schedule |
| Enabled | `schedule_enabled` | `boolean` | Is the schedule enabled |
| Expiry Time | `schedule_expiry_time` | `text` | The time the schedule expires |
| Frequency | `schedule_frequency` | `text` | The frequency of the schedule |
| Interval | `schedule_interval` | `text` | The execute intervals of the schedule |
| Name | `schedule_name` | `text` | Name of the schedule |
| Query Date | `schedule_query_date` | `datetimepicker` | Time the query to get this information was run |
| Resource Group | `resource_group_schedules` | `text` | Azure Automation resource group |
| Start Time | `schedule_start_time` | `text` | The time the schedule starts |
| Time Zone | `schedule_time_zone` | `text` | The time zone the schedule is in |

---
## Data Table - Azure Automation Statistics

 ![screenshot: dt-azure-automation-statistics](./doc/screenshots/dt-azure-automation-statistics.png)

#### API Name:
azure_automation_statistics

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Account Name | `account_name_statistics` | `text` | Azure Automation Account Name |
| Counter Property | `statistic_counter_property` | `text` | Property of the counter statistic |
| Counter Value | `statistic_counter_value` | `number` | The value of the counter statistic |
| Query Date | `statistic_query_date` | `datetimepicker` | Time the query to get this information was run |
| Resource Group | `resource_group_statistics` | `text` | Azure Automation resource group |

---

## Custom Fields
| Label | API Access Name | Type | Prefix | Placeholder | Tooltip |
| ----- | --------------- | ---- | ------ | ----------- | ------- |
| Create UI Tab | `azure_automation_create_ui_tab` | `boolean` | `properties` | - | If true the Azure Automation UI Tab will be created |

---




## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.
 
### For Support
This is an IBM supported app. Please search [ibm.com/mysupport](https://ibm.com/mysupport) for assistance.
