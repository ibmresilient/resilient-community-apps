# McAfee ePO Integration for SOAR

## Table of Contents
- [Release Notes](#release-notes)
- [3.0.0 Changes](#3.0.0-changes)
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
- [Function - McAfee ePO Add Permission sets to user](#function---mcafee-epo-add-permission-sets-to-user)
- [Function - McAfee ePO Add System](#function---mcafee-epo-add-system)
- [Function - McAfee ePO Add User](#function---mcafee-epo-add-user)
- [Function - McAfee ePO Assign Policy to Group](#function---mcafee-epo-assign-policy-to-group)
- [Function - McAfee ePO Assign Policy to Systems](#function---mcafee-epo-assign-policy-to-systems)
- [Function - McAfee ePO Create Issue](#function---mcafee-epo-create-issue)
- [Function - McAfee ePO Delete Issue](#function---mcafee-epo-delete-issue)
- [Function - McAfee ePO Delete System](#function---mcafee-epo-delete-system)
- [Function - McAfee ePO Execute Query](#function---mcafee-epo-execute-query)
- [Function - McAfee ePO Find a System](#function---mcafee-epo-find-a-system)
- [Function - McAfee ePO Find Client Tasks](#function---mcafee-epo-find-client-tasks)
- [Function - McAfee ePO Find Groups](#function---mcafee-epo-find-groups)
- [Function - McAfee ePO Find Policies](#function---mcafee-epo-find-policies)
- [Function - McAfee ePO Find Systems in Group](#function---mcafee-epo-find-systems-in-group)
- [Function - McAfee ePO Get All Permission sets](#function---mcafee-epo-get-all-permission-sets)
- [Function - McAfee ePO Get All Users](#function---mcafee-epo-get-all-users)
- [Function - McAfee ePO List Issues](#function---mcafee-epo-list-issues)
- [Function - McAfee ePO List Tags](#function---mcafee-epo-list-tags)
- [Function - McAfee ePO Remove Permission sets from user](#function---mcafee-epo-remove-permission-sets-from-user)
- [Function - McAfee ePO Remove Tag](#function---mcafee-epo-remove-tag)
- [Function - McAfee ePO Remove User](#function---mcafee-epo-remove-user)
- [Function - McAfee ePO Run Client Task](#function---mcafee-epo-run-client-task)
- [Function - McAfee ePO Update Issue](#function---mcafee-epo-update-issue)
- [Function - McAfee ePO Update User](#function---mcafee-epo-update-user)
- [Function - McAfee ePO Wake up agent](#function---mcafee-epo-wake-up-agent)
- [Function - McAfee Tag an ePO Asset](#function---mcafee-tag-an-epo-asset)
- [Data Table - McAfee ePO Client Tasks](#data-table---mcafee-epo-client-tasks)
- [Data Table - McAfee ePO Groups](#data-table---mcafee-epo-groups)
- [Data Table - McAfee ePO Issues](#data-table---mcafee-epo-issues)
- [Data Table - McAfee ePO Permission sets](#data-table---mcafee-epo-permission-sets)
- [Data Table - McAfee ePO Policies](#data-table---mcafee-epo-policies)
- [Data Table - McAfee ePO Systems](#data-table---mcafee-epo-systems)
- [Data Table - McAfee ePO tags](#data-table---mcafee-epo-tags)
- [Data Table - McAfee ePO Users](#data-table---mcafee-epo-users)
- [Playbooks](#playbooks)
- [Troubleshooting & Support](#troubleshooting--support)

---

## Release Notes
| Version | Date | Notes |
| ------- | ---- | ----- |
| 2.1.0 | 02/2024 | Convert from rule/workflows to playbooks |
| 2.0.0 | 07/2022 | <ul><li>Add 20 new functions</li><li>Added 7 new data tables</li><li>Update funct_mcafee_epo_find_a_system function to allow a list of systems properties to be used and return a list of systems</li></ul> |
| 1.0.3 | 10/2020 | Added functions: find system, get system info, remove tags and Updated capability to rule for add tag function |
| 1.0.2 | 04/2020 | Support added for App Host |
| 1.0.1 | 10/2019 | Fix py2/3 incompatibility |
| 1.0.0 | 08/2018 | Initial Release |

---

## 2.1.0 Changes
In v2.1, the existing rules and workflows have been replaced with playbooks. This change is made to support the ongoing, newer capabilities of playbooks. Each playbook has the same functionality as the previous, corresponding rule/workflow.

If upgrading from a previous release, you'll noticed that the previous release's rules/workflows remain in place. Both sets of rules and playbooks are active. For manual actions, playbooks will have the same name as it's corresponding rule, but with "(PB)" added at the end. For automatic actions, the playbooks will be disabled by default.

You can continue to use the rules/workflows. But migrating to playbooks will provide greater functionality along with future app enhancements and bug fixes.

The data table mcafee_epo_systems has been replaced by mcafee_epo_systems_dt and its columns names have been updated. The original data table was not compatible with SOAR v45+. When upgrading from a pervious version both data tables will be present, so make sure to use the new data table mcafee_epo_systems_dt.

---

## Overview
The McAfee ePO functions allow for manipulation of tags, systems, users, issues, policies and permission sets on the McAfee ePO server.

**IBM Security SOAR app for McAfee ePO**

 ![screenshot: main](./doc/screenshots/main.png)

The McAfee ePO functions allow for manipulation of tags, systems, users, issues, policies and permission sets.

### Key Features
* Add permission set(s) to an ePO user
* Add a system to the ePO server
* Add a user to the ePO server
* Assigns policy to the specified group no ePO server
* Assigns the policy to a supplied list of systems on the ePO server
* Create an issue on the ePO server
* Delete an issue from the ePO server
* Delete a system from the ePO server
* Execute a query on the ePO server
* Find client tasks on the ePO server
* Find groups on the ePO server
* Finds all policies that match the given search text or find all policies if no search text is given
* Find systems in a specified group on ePO server
* Get all of the permission sets on an ePO server
* Get all the users on a ePO server
* List the issues on the ePO server
* Remove permission set(s) from an ePO user
* Delete a user from the ePO server
* Run a client task on specified system(s)
* Update an issue on the ePO server
* Update a user on the ePO server
* Wake up an ePO agent
* Find an ePO system based on a property such as system name, tag, IP address, MAC address, etc.
* Find all tags specified in ePO
* Remove a tag associated with an ePO system(s).
* Applies tag to the systems in ePO. Inputs include: - mcafee_epo_system: Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO. - mcafee_epo_tag: A tag managed on ePO.


---

## Requirements
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, Edge Gateway (formerly App Host) and integration server.

If deploying to a SOAR platform with an Edge Gateway, the requirements are:
* SOAR platform >= `49.0.0`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `49.0.0`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient_circuits>=49.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions:
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read |
  | Function | Read |
  | Incident | Edit |

The following SOAR platform guides provide additional information:
* _Edge Gateway Deployment Guide_ or _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _Integration Server Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _System Administrator Guide_: provides the procedure to install, configure and deploy apps.

The above guides are available on the IBM Documentation website at [ibm.biz/soar-docs](https://ibm.biz/soar-docs). On this web page, select your SOAR platform version. On the follow-on page, you can find the _Edge Gateway Deployment Guide_, _App Host Deployment Guide_, or _Integration Server Guide_ by expanding **Apps** in the Table of Contents pane. The System Administrator Guide is available by expanding **System Administrator**.

### Cloud Pak for Security
If you are deploying to IBM Cloud Pak for Security, the requirements are:
* IBM Cloud Pak for Security >= `1.10`.
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
* resilient_circuits>=49.0.0

---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **epo_url** | Yes | `https://<your_epo_server>:8443` | *URL to your McAfee ePO server* |
| **epo_username** | Yes | `<your_epo_username>` | *Your McAfee ePO server username* |
| **epo_password** | Yes | `<your_epo_password>` | *Your McAfee ePO server password* |
| **epo_trust_cert** | Yes | `false` | *Path to server certificate or false to bypass verification* |
| **timeout** | No | `60` | *Timeout is seconds for calls made to the ePO server* |

### Custom Layouts

* Import the Data Tables and Custom Fields like the screenshot below:

  ![screenshot: custom_layouts](./doc/screenshots/custom_layouts.png)


---

## Function - McAfee ePO Add Permission sets to user
Add permission set(s) to an ePO user.
McAfee user requires administrator rights for this function.

 ![screenshot: fn-mcafee-epo-add-permission-sets-to-user ](./doc/screenshots/fn-mcafee-epo-add-permission-sets-to-user.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_permsetname` | `text` | No | `-` | Name of the permission set to add to the ePO user |
| `mcafee_epo_username` | `text` | No | `-` | User name for ePO user |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": true,
  "inputs": {
    "mcafee_epo_permsetname": "Global Reviewer",
    "mcafee_epo_username": "new user"
  },
  "metrics": {
    "execution_time_ms": 625,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:17:32",
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
if getattr(playbook.inputs, "epo_username", None):
  inputs.mcafee_epo_username = getattr(playbook.inputs, "epo_username", None)
inputs.mcafee_epo_permsetname = row.permission_set_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.add_perm_set
username = playbook.inputs.epo_username
if results.get('success'):
  if username not in row.users:
    if row.users:
      row.users = "{}, {}".format(row.users, username)
    else:
      row.users = username
    incident.addNote(f"Permissions set: {row.permission_set_name} was added to user: {username}")
  else:
    incident.addNote(f"User: {username} already has permission set: {row.permission_set_name}")
```

</p>
</details>

---
## Function - McAfee ePO Add System
Add a system to the ePO server.
McAfee user requires permission to edit System Tree for this function.

 ![screenshot: fn-mcafee-epo-add-system ](./doc/screenshots/fn-mcafee-epo-add-system.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_allow_duplicates` | `boolean` | No | `-` | Whether to allow duplicates or not |
| `mcafee_epo_delete_if_removed` | `boolean` | No | `-` | Should system be deleted if removed |
| `mcafee_epo_flatten_tree_structure` | `boolean` | No | `-` | Should flatten tree structure |
| `mcafee_epo_group_id` | `number` | No | `-` | Id for the group on the ePO server |
| `mcafee_epo_push_agent` | `boolean` | No | `-` | Whether to push the agent to the system or not |
| `mcafee_epo_push_agent_domain_name` | `text` | No | `-` | Domain name for system to push agent |
| `mcafee_epo_push_agent_force_install` | `boolean` | No | `-` | force install if agent on new system |
| `mcafee_epo_push_agent_install_path` | `text` | No | `-` | path to where the agent should be installed on the system |
| `mcafee_epo_push_agent_package_path` | `text` | No | `-` | Path the package on the new system |
| `mcafee_epo_push_agent_password` | `text` | No | `-` | Password for system |
| `mcafee_epo_push_agent_skip_if_installed` | `boolean` | No | `-` | Skip pushing agent if it is installed |
| `mcafee_epo_push_agent_suppress_ui` | `boolean` | No | `-` | Push agent and suppress ui |
| `mcafee_epo_push_agent_username` | `text` | No | `-` | username for system |
| `mcafee_epo_system_name_or_id` | `text` | No | `-` | Comma separated list of systems name or system ids |
| `mcafee_epo_uninstall` | `boolean` | No | `-` | True or false to uninstall system |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": true,
  "inputs": {
    "mcafee_epo_allow_duplicates": false,
    "mcafee_epo_delete_if_removed": false,
    "mcafee_epo_flatten_tree_structure": false,
    "mcafee_epo_group_id": 2,
    "mcafee_epo_push_agent": false,
    "mcafee_epo_push_agent_domain_name": null,
    "mcafee_epo_push_agent_force_install": false,
    "mcafee_epo_push_agent_install_path": null,
    "mcafee_epo_push_agent_package_path": null,
    "mcafee_epo_push_agent_password": null,
    "mcafee_epo_push_agent_skip_if_installed": false,
    "mcafee_epo_push_agent_suppress_ui": false,
    "mcafee_epo_push_agent_username": null,
    "mcafee_epo_system_name_or_id": "richard test1",
    "mcafee_epo_uninstall": false
  },
  "metrics": {
    "execution_time_ms": 787,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 10:26:00",
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
# Required
inputs.mcafee_epo_group_id = playbook.inputs.epo_group_id
inputs.mcafee_epo_system_name_or_id = playbook.inputs.epo_system_names_or_ids

# Optional
if getattr(playbook.inputs, "epo_allow_duplicates", None):
  inputs.mcafee_epo_allow_duplicates = getattr(playbook.inputs, "epo_allow_duplicates")
if getattr(playbook.inputs, "epo_delete_if_removed", None):
  inputs.mcafee_epo_delete_if_removed = getattr(playbook.inputs, "epo_delete_if_removed")
if getattr(playbook.inputs, "epo_flatten_tree_structure", None):
  inputs.mcafee_epo_flatten_tree_structure = getattr(playbook.inputs, "epo_flatten_tree_structure")
if getattr(playbook.inputs, "epo_push_agent", None):
  inputs.mcafee_epo_push_agent = getattr(playbook.inputs, "epo_push_agent")
if getattr(playbook.inputs, "epo_push_agent_domain_name", None):
  inputs.mcafee_epo_push_agent_domain_name = getattr(playbook.inputs, "epo_push_agent_domain_name")
if getattr(playbook.inputs, "epo_push_agent_force_install", None):
  inputs.mcafee_epo_push_agent_force_install = getattr(playbook.inputs, "epo_push_agent_force_install")
if getattr(playbook.inputs, "epo_push_agent_package_path", None):
  inputs.mcafee_epo_push_agent_package_path = getattr(playbook.inputs, "epo_push_agent_package_path")
if getattr(playbook.inputs, "epo_push_agent_password", None):
  inputs.mcafee_epo_push_agent_password = getattr(playbook.inputs, "epo_push_agent_password")
if getattr(playbook.inputs, "epo_push_agent_skip_if_installed", None):
  inputs.mcafee_epo_push_agent_skip_if_installed = getattr(playbook.inputs, "epo_push_agent_skip_if_installed")
if getattr(playbook.inputs, "epo_push_agent_suppress_ui", None):
  inputs.mcafee_epo_push_agent_suppress_ui = getattr(playbook.inputs, "epo_push_agent_suppress_ui")
if getattr(playbook.inputs, "epo_push_agent_user_name", None):
  inputs.mcafee_epo_push_agent_username = getattr(playbook.inputs, "epo_push_agent_user_name")
if getattr(playbook.inputs, "epo_uninstall_removed", None):
  inputs.mcafee_epo_uninstall = getattr(playbook.inputs, "epo_uninstall_removed")
if getattr(playbook.inputs, "epo_push_agent_install_path", None):
  inputs.mcafee_epo_push_agent_install_path = getattr(playbook.inputs, "epo_push_agent_install_path")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.add_sys
if results.get("success"):
  row = incident.addRow("mcafee_epo_systems_dt")
  row["epo_system_name"] = playbook.inputs.epo_system_names_or_ids
  row["epo_deleted"] = False
```

</p>
</details>

---
## Function - McAfee ePO Add User
Add a user to the ePO server.
McAfee user requires administrator rights for this function.

 ![screenshot: fn-mcafee-epo-add-user ](./doc/screenshots/fn-mcafee-epo-add-user.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_admin` | `boolean` | No | `-` | Should this user have admin privileges  |
| `mcafee_epo_allowed_ips` | `text` | No | `-` | A list of ips that can access the new user |
| `mcafee_epo_email` | `text` | No | `-` | Email for the new user |
| `mcafee_epo_fullname` | `text` | No | `-` | Full name for the new user |
| `mcafee_epo_notes` | `text` | No | `-` | Notes to add to the new user |
| `mcafee_epo_pass` | `text` | No | `-` | Password for ePO user |
| `mcafee_epo_phone_number` | `text` | No | `-` | Phone number for the new user |
| `mcafee_epo_user_disabled` | `boolean` | No | `-` | Should the new user be disabled when created? |
| `mcafee_epo_username` | `text` | No | `-` | User name for ePO user |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": true,
  "inputs": {
    "mcafee_epo_admin": false,
    "mcafee_epo_allowed_ips": null,
    "mcafee_epo_email": "richard@test.com",
    "mcafee_epo_fullname": "Richard Test",
    "mcafee_epo_notes": "Hello",
    "mcafee_epo_pass": "R3silient1",
    "mcafee_epo_phone_number": "7394034758",
    "mcafee_epo_user_disabled": null,
    "mcafee_epo_username": "richard-test"
  },
  "metrics": {
    "execution_time_ms": 825,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 10:37:10",
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
if getattr(playbook.inputs, "epo_username", None):
  inputs.mcafee_epo_username = getattr(playbook.inputs, "epo_username")
if getattr(playbook.inputs, "epo_user_password", None):
  inputs.mcafee_epo_pass = getattr(playbook.inputs, "epo_user_password")
if getattr(playbook.inputs, "epo_admin", None):
  inputs.mcafee_epo_admin = getattr(playbook.inputs, "epo_admin")
if getattr(playbook.inputs, "epo_allowed_ips", None):
  inputs.mcafee_epo_allowed_ips = getattr(playbook.inputs, "epo_allowed_ips")
if getattr(playbook.inputs, "epo_email", None):
  inputs.mcafee_epo_email = getattr(playbook.inputs, "epo_email")
if getattr(playbook.inputs, "epo_full_name", None):
  inputs.mcafee_epo_fullname = getattr(playbook.inputs, "epo_full_name")
if getattr(playbook.inputs, "epo_notes", None):
  inputs.mcafee_epo_notes = getattr(playbook.inputs, "epo_notes")
if getattr(playbook.inputs, "epo_phone_number", None):
  inputs.mcafee_epo_phone_number = getattr(playbook.inputs, "epo_phone_number")
if getattr(playbook.inputs, "epo_user_disabled", None):
  inputs.mcafee_epo_user_disabled = getattr(playbook.inputs, "epo_user_disabled")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.add_user
if results.get("success"):
  incident.addNote("User: {} successfully created.".format(playbook.inputs.epo_username))
```

</p>
</details>

---
## Function - McAfee ePO Assign Policy to Group
Assigns policy to the specified group no ePO server.
McAfee user requires permission to at least one group in the System Tree and edit permission for at least one product for this function.

 ![screenshot: fn-mcafee-epo-assign-policy-to-group ](./doc/screenshots/fn-mcafee-epo-assign-policy-to-group.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_group_id` | `number` | No | `-` | Id for the group on the ePO server |
| `mcafee_epo_object_id` | `number` | No | `-` | ID if object |
| `mcafee_epo_product_id` | `text` | No | `-` | The product ID for the task |
| `mcafee_epo_reset_inheritance` | `boolean` | No | `-` | Boolean to reset inheritance |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": true,
  "inputs": {
    "mcafee_epo_group_id": 3,
    "mcafee_epo_object_id": 4,
    "mcafee_epo_product_id": "EPOAGENTMETA"
  },
  "metrics": {
    "execution_time_ms": 702,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:20:24",
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
inputs.mcafee_epo_group_id = row.group_id
if getattr(playbook.inputs, "epo_policy_id", None):
  inputs.mcafee_epo_object_id = getattr(playbook.inputs, "epo_policy_id")
if getattr(playbook.inputs, "epo_product_id", None):
  inputs.mcafee_epo_product_id = getattr(playbook.inputs, "epo_product_id")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.assign_policy
if results.get("success"):
  incident.addNote("Policy: '{}' Assigned to Group: '{}'".format(getattr(playbook.inputs, "epo_policy_id"), row.group_id))
```

</p>
</details>

---
## Function - McAfee ePO Assign Policy to Systems
Assigns the policy to a supplied list of systems on the ePO server.
McAfee user requires permission to at least one group in the System Tree and edit permission for at least one product for this function.

 ![screenshot: fn-mcafee-epo-assign-policy-to-systems ](./doc/screenshots/fn-mcafee-epo-assign-policy-to-systems.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_object_id` | `number` | No | `-` | ID if object |
| `mcafee_epo_product_id` | `text` | No | `-` | The product ID for the task |
| `mcafee_epo_reset_inheritance` | `boolean` | No | `-` | Boolean to reset inheritance |
| `mcafee_epo_system_name_or_id` | `text` | No | `-` | Comma separated list of systems name or system ids |
| `mcafee_epo_type_id` | `number` | No | `-` | Type ID |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "id": "1011",
      "message": "Assign policy succeeded",
      "name": "richard test1",
      "status": 0
    }
  ],
  "inputs": {
    "mcafee_epo_object_id": 4,
    "mcafee_epo_product_id": "EPOAGENTMETA",
    "mcafee_epo_system_name_or_id": "richard test1",
    "mcafee_epo_type_id": 3
  },
  "metrics": {
    "execution_time_ms": 631,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:21:13",
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
inputs.mcafee_epo_system_name_or_id = row.epo_system_name
if getattr(playbook.inputs, "epo_product_id", None):
  inputs.mcafee_epo_product_id = getattr(playbook.inputs, "epo_product_id")
if getattr(playbook.inputs, "epo_policy_type_id", None):
  inputs.mcafee_epo_type_id = getattr(playbook.inputs, "epo_policy_type_id")
if getattr(playbook.inputs, "epo_policy_id", None):
  inputs.mcafee_epo_object_id = getattr(playbook.inputs, "epo_policy_id")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.assign_policy
if results.get("success"):
  incident.addNote("Policy: '{}' Assigned to system: '{}'".format(getattr(playbook.inputs, "epo_policy_id"), row.epo_system_name))
```

</p>
</details>

---
## Function - McAfee ePO Create Issue
Create an issue on the ePO server.
McAfee user requires permission to edit issues for this function.

 ![screenshot: fn-mcafee-epo-create-issue ](./doc/screenshots/fn-mcafee-epo-create-issue.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_issue_assignee` | `text` | No | `-` | Username of person assigned to the issue |
| `mcafee_epo_issue_description` | `text` | No | `-` | description of the issue  |
| `mcafee_epo_issue_due` | `datetimepicker` | No | `-` | Due date of the issue |
| `mcafee_epo_issue_name` | `text` | No | `-` | Name of the issue on the ePO server |
| `mcafee_epo_issue_priority` | `select` | No | `-` | The priority of the issue |
| `mcafee_epo_issue_properties` | `text` | No | `-` | Properties for the issue |
| `mcafee_epo_issue_resolution` | `select` | No | `-` | Resolution status of the issue |
| `mcafee_epo_issue_severity` | `select` | No | `-` | Severity of the issue |
| `mcafee_epo_issue_state` | `select` | No | `-` | State of the issue |
| `mcafee_epo_issue_type` | `select` | No | `-` | Issue type |
| `mcafee_epo_ticket_id` | `number` | No | `-` | ID of the ticket |
| `mcafee_epo_ticket_server_name` | `text` | No | `-` | Name of the server the issue should be on |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": 1,
  "inputs": {
    "mcafee_epo_issue_assignee": null,
    "mcafee_epo_issue_description": "Testing issue creation",
    "mcafee_epo_issue_due": 1698294000000,
    "mcafee_epo_issue_name": "richard test issue",
    "mcafee_epo_issue_priority": "Low",
    "mcafee_epo_issue_properties": null,
    "mcafee_epo_issue_resolution": "None",
    "mcafee_epo_issue_severity": "Low",
    "mcafee_epo_issue_state": "New",
    "mcafee_epo_issue_type": "Basic",
    "mcafee_epo_ticket_id": null,
    "mcafee_epo_ticket_server_name": null
  },
  "metrics": {
    "execution_time_ms": 606,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 10:39:15",
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
if getattr(playbook.inputs, "epo_issue_assignee", None):
  inputs.mcafee_epo_issue_assignee = getattr(playbook.inputs, "epo_issue_assignee")
if getattr(playbook.inputs, "epo_issue_description", None):
  inputs.mcafee_epo_issue_description = getattr(playbook.inputs, "epo_issue_description")
if getattr(playbook.inputs, "epo_issue_due", None):
  inputs.mcafee_epo_issue_due = getattr(playbook.inputs, "epo_issue_due")
if getattr(playbook.inputs, "epo_issue_name", None):
  inputs.mcafee_epo_issue_name = getattr(playbook.inputs, "epo_issue_name")
if getattr(playbook.inputs, "epo_issue_priority", None):
  inputs.mcafee_epo_issue_priority = getattr(playbook.inputs, "epo_issue_priority")
if getattr(playbook.inputs, "epo_issue_properties", None):
  inputs.mcafee_epo_issue_properties = getattr(playbook.inputs, "epo_issue_properties")
if getattr(playbook.inputs, "epo_issue_resolution", None):
  inputs.mcafee_epo_issue_resolution = getattr(playbook.inputs, "epo_issue_resolution")
if getattr(playbook.inputs, "epo_issue_severity", None):
  inputs.mcafee_epo_issue_severity = getattr(playbook.inputs, "epo_issue_severity")
if getattr(playbook.inputs, "epo_issue_state", None):
  inputs.mcafee_epo_issue_state = getattr(playbook.inputs, "epo_issue_state")
if getattr(playbook.inputs, "epo_ticket_id", None):
  inputs.mcafee_epo_ticket_id = getattr(playbook.inputs, "epo_ticket_id")
if getattr(playbook.inputs, "epo_ticket_server_name", None):
  inputs.mcafee_epo_ticket_server_name = getattr(playbook.inputs, "epo_ticket_server_name")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.create_issue
if results.get("success"):
  row = incident.addRow("mcafee_epo_issues")
  row["issue_name"] = getattr(playbook.inputs, "epo_issue_name")
  row["issue_id"] = results.get("content", {})
  row["severity"] = getattr(playbook.inputs, "epo_issue_severity")
  row["issue_due_date"] = getattr(playbook.inputs, "epo_issue_due")
  row["issue_description"] = getattr(playbook.inputs, "epo_issue_description")
  row["ticket_server_name"] = getattr(playbook.inputs, "epo_ticket_server_name")
  row["priority"] = getattr(playbook.inputs, "epo_issue_priority")
  row["type"] = getattr(playbook.inputs, "epo_issue_type")
  row["resolution"] = getattr(playbook.inputs, "epo_issue_resolution")
  row["assignee_name"] =getattr(playbook.inputs, "epo_issue_assignee")
  row["issue_state"] = getattr(playbook.inputs, "epo_issue_state")
  row["ticket_id"] = getattr(playbook.inputs, "epo_ticket_id")
  row["issue_deleted"] = False
```

</p>
</details>

---
## Function - McAfee ePO Delete Issue
Delete an issue from the ePO server.
McAfee user requires permission to edit issues for this function.

 ![screenshot: fn-mcafee-epo-delete-issue ](./doc/screenshots/fn-mcafee-epo-delete-issue.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_issue_id` | `number` | No | `-` | ID of the issue |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": 1,
  "inputs": {
    "mcafee_epo_issue_id": 1
  },
  "metrics": {
    "execution_time_ms": 519,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:15:09",
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
inputs.mcafee_epo_issue_id = row.issue_id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.delete_issue
if results.get("success"):
  row.issue_deleted = True
  incident.addNote("Issue: '{}' deleted successfully.".format(row.issue_id))
```

</p>
</details>

---
## Function - McAfee ePO Delete System
Delete a system from the ePO server.
McAfee user requires permission to edit System Tree groups and systems for this function.

 ![screenshot: fn-mcafee-epo-delete-system ](./doc/screenshots/fn-mcafee-epo-delete-system.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_system_name_or_id` | `text` | No | `-` | Comma separated list of systems name or system ids |
| `mcafee_epo_uninstall` | `boolean` | No | `-` | True or false to uninstall system |
| `mcafee_epo_uninstall_software` | `boolean` | No | `-` | True or false to uninstall software on system |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "id": "1010",
      "message": "Computer deleted successfully",
      "name": "SomethingNew",
      "status": 0
    }
  ],
  "inputs": {
    "mcafee_epo_system_name_or_id": "SomethingNew"
  },
  "metrics": {
    "execution_time_ms": 799,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:11:41",
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
inputs.mcafee_epo_system_name_or_id = row.epo_system_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.delete_system
if results.get("success"):
  row.epo_deleted = True
  incident.addNote("System: {} deleted".format(row.epo_system_name))
```

</p>
</details>

---
## Function - McAfee ePO Execute Query
Execute a query on the ePO server.
McAfee user requires permission to use queries for this function.

 ![screenshot: fn-mcafee-epo-execute-query ](./doc/screenshots/fn-mcafee-epo-execute-query.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `datatable_name` | `text` | No | `Name of the datatable being cleared` | - |
| `incident_id` | `number` | No | `SOAR incident id` | - |
| `mcafee_epo_query_group` | `text` | No | `-` | List, separated by a space, of properties to group together in the output |
| `mcafee_epo_query_order` | `text` | No | `-` | Starts with asc for ascending or des for descending order a space and then the property to sort by |
| `mcafee_epo_query_select` | `text` | No | `EPOAssignedPolicy.NodeName EPOAssignedPolicy.UserName` | List of fields to return separated by a space |
| `mcafee_epo_queryid` | `number` | No | `-` | The ID of the query you want to run |
| `mcafee_epo_target` | `text` | No | `-` | ePO data types target name |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "EPOLeafNode.AgentGUID": "E1ABB618-09C4-11ED-2BBA-005056B43418",
      "EPOLeafNode.AgentVersion": "5.6.5.236",
      "EPOLeafNode.ExcludedTags": "",
      "EPOLeafNode.LastCommSecure": "1",
      "EPOLeafNode.LastUpdate": "2023-10-09T07:49:56-07:00",
      "EPOLeafNode.ManagedState": 1,
      "EPOLeafNode.NodeName": "int-mcafee-tie",
      "EPOLeafNode.ResortEnabled": false,
      "EPOLeafNode.SequenceErrorCount": 0,
      "EPOLeafNode.SequenceErrorCountLastUpdate": null,
      "EPOLeafNode.Tags": "Server",
      "EPOLeafNode.TransferSiteListsID": false,
      "EPOLeafNode.os": "Linux|Server|4.9|227-1.mlos2.x86_64"
    },
    {
      "EPOLeafNode.AgentGUID": "D770FEB6-3C1E-40A9-ACB2-B74E5FF66D5E",
      "EPOLeafNode.AgentVersion": "5.5.1.388",
      "EPOLeafNode.ExcludedTags": "",
      "EPOLeafNode.LastCommSecure": "1",
      "EPOLeafNode.LastUpdate": "2022-07-22T07:42:36-07:00",
      "EPOLeafNode.ManagedState": 1,
      "EPOLeafNode.NodeName": "MCAFEE-EPO-CLIE",
      "EPOLeafNode.ResortEnabled": false,
      "EPOLeafNode.SequenceErrorCount": 0,
      "EPOLeafNode.SequenceErrorCountLastUpdate": null,
      "EPOLeafNode.Tags": "Server",
      "EPOLeafNode.TransferSiteListsID": false,
      "EPOLeafNode.os": "Windows Server 2016|Server|10.0|"
    },
    {
      "EPOLeafNode.AgentGUID": "B7E3C7E0-CDE7-11EB-3210-005056B41000",
      "EPOLeafNode.AgentVersion": "5.6.6.232",
      "EPOLeafNode.ExcludedTags": "",
      "EPOLeafNode.LastCommSecure": "1",
      "EPOLeafNode.LastUpdate": "2023-10-09T07:05:49-07:00",
      "EPOLeafNode.ManagedState": 1,
      "EPOLeafNode.NodeName": "WIN-MTHJTQ4ELBP",
      "EPOLeafNode.ResortEnabled": false,
      "EPOLeafNode.SequenceErrorCount": 0,
      "EPOLeafNode.SequenceErrorCountLastUpdate": null,
      "EPOLeafNode.Tags": "Server",
      "EPOLeafNode.TransferSiteListsID": false,
      "EPOLeafNode.os": "Windows Server 2016|Server|10.0|"
    },
    {
      "EPOLeafNode.AgentGUID": null,
      "EPOLeafNode.AgentVersion": null,
      "EPOLeafNode.ExcludedTags": "",
      "EPOLeafNode.LastCommSecure": "0",
      "EPOLeafNode.LastUpdate": null,
      "EPOLeafNode.ManagedState": 0,
      "EPOLeafNode.NodeName": "test",
      "EPOLeafNode.ResortEnabled": false,
      "EPOLeafNode.SequenceErrorCount": 0,
      "EPOLeafNode.SequenceErrorCountLastUpdate": null,
      "EPOLeafNode.Tags": "",
      "EPOLeafNode.TransferSiteListsID": false,
      "EPOLeafNode.os": "|||"
    },
    {
      "EPOLeafNode.AgentGUID": null,
      "EPOLeafNode.AgentVersion": null,
      "EPOLeafNode.ExcludedTags": "",
      "EPOLeafNode.LastCommSecure": "0",
      "EPOLeafNode.LastUpdate": null,
      "EPOLeafNode.ManagedState": 0,
      "EPOLeafNode.NodeName": "System1",
      "EPOLeafNode.ResortEnabled": false,
      "EPOLeafNode.SequenceErrorCount": 0,
      "EPOLeafNode.SequenceErrorCountLastUpdate": null,
      "EPOLeafNode.Tags": "",
      "EPOLeafNode.TransferSiteListsID": false,
      "EPOLeafNode.os": "|||"
    },
    {
      "EPOLeafNode.AgentGUID": null,
      "EPOLeafNode.AgentVersion": null,
      "EPOLeafNode.ExcludedTags": "",
      "EPOLeafNode.LastCommSecure": "0",
      "EPOLeafNode.LastUpdate": null,
      "EPOLeafNode.ManagedState": 0,
      "EPOLeafNode.NodeName": "test1254",
      "EPOLeafNode.ResortEnabled": false,
      "EPOLeafNode.SequenceErrorCount": 0,
      "EPOLeafNode.SequenceErrorCountLastUpdate": null,
      "EPOLeafNode.Tags": "",
      "EPOLeafNode.TransferSiteListsID": false,
      "EPOLeafNode.os": "|||"
    },
    {
      "EPOLeafNode.AgentGUID": null,
      "EPOLeafNode.AgentVersion": null,
      "EPOLeafNode.ExcludedTags": "",
      "EPOLeafNode.LastCommSecure": "0",
      "EPOLeafNode.LastUpdate": null,
      "EPOLeafNode.ManagedState": 0,
      "EPOLeafNode.NodeName": "SomethingNew",
      "EPOLeafNode.ResortEnabled": false,
      "EPOLeafNode.SequenceErrorCount": 0,
      "EPOLeafNode.SequenceErrorCountLastUpdate": null,
      "EPOLeafNode.Tags": "",
      "EPOLeafNode.TransferSiteListsID": false,
      "EPOLeafNode.os": "|||"
    },
    {
      "EPOLeafNode.AgentGUID": null,
      "EPOLeafNode.AgentVersion": null,
      "EPOLeafNode.ExcludedTags": "",
      "EPOLeafNode.LastCommSecure": "0",
      "EPOLeafNode.LastUpdate": null,
      "EPOLeafNode.ManagedState": 0,
      "EPOLeafNode.NodeName": "richard test1",
      "EPOLeafNode.ResortEnabled": false,
      "EPOLeafNode.SequenceErrorCount": 0,
      "EPOLeafNode.SequenceErrorCountLastUpdate": null,
      "EPOLeafNode.Tags": "",
      "EPOLeafNode.TransferSiteListsID": false,
      "EPOLeafNode.os": "|||"
    }
  ],
  "inputs": {
    "datatable_name": "mcafee_epo_systems_dt",
    "incident_id": 4057,
    "mcafee_epo_target": "EPOLeafNode"
  },
  "metrics": {
    "execution_time_ms": 2391,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 10:55:10",
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
inputs.datatable_name = "mcafee_epo_permission_sets"
inputs.incident_id = incident.id
inputs.mcafee_epo_target = "EntitlementView"
inputs.mcafee_epo_query_select = "EntitlementView.PrincipalName EntitlementView.GroupName"
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.query
perm_sets = playbook.functions.results.perm_sets
if results.get("success"):
  for permset in perm_sets.get("content"):
    permsetName = permset.get("name")
    table_row = incident.addRow("mcafee_epo_permission_sets")
    table_row["permission_set_name"] = permsetName
    users = ""
    for perm in results.get("content"):
      user = perm.get("EntitlementView.PrincipalName")
      permGroup = perm.get("EntitlementView.GroupName")
      if user and permGroup and permsetName.lower() == permGroup.lower() and user not in users:
        users = "{}, {}".format(users, user)
    table_row["users"] = users[2:]
```

</p>
</details>

---
## Function - McAfee ePO Find a System
Find an ePO system based on a property such as system name, tag, IP address, MAC address, etc.
McAfee user requires permission to at least one group in the System Tree for this function.

 ![screenshot: fn-mcafee-epo-find-a-system ](./doc/screenshots/fn-mcafee-epo-find-a-system.png)
<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_systems` | `text` | No | `-` | Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "EPOBranchNode.AutoID": 2,
      "EPOComputerProperties.CPUSerialNumber": "",
      "EPOComputerProperties.CPUSpeed": 0,
      "EPOComputerProperties.CPUType": "",
      "EPOComputerProperties.ComputerDescription": null,
      "EPOComputerProperties.ComputerName": "richard test1",
      "EPOComputerProperties.DefaultLangID": "",
      "EPOComputerProperties.Description": null,
      "EPOComputerProperties.DomainName": "",
      "EPOComputerProperties.FreeDiskSpace": 0,
      "EPOComputerProperties.FreeMemory": 0,
      "EPOComputerProperties.Free_Space_of_Drive_C": 0,
      "EPOComputerProperties.IPAddress": "",
      "EPOComputerProperties.IPHostName": "",
      "EPOComputerProperties.IPSubnet": null,
      "EPOComputerProperties.IPSubnetMask": null,
      "EPOComputerProperties.IPV4x": null,
      "EPOComputerProperties.IPV6": null,
      "EPOComputerProperties.IPXAddress": "",
      "EPOComputerProperties.IsPortable": -1,
      "EPOComputerProperties.LastAgentHandler": null,
      "EPOComputerProperties.NetAddress": "",
      "EPOComputerProperties.NumOfCPU": 0,
      "EPOComputerProperties.OSBitMode": -1,
      "EPOComputerProperties.OSBuildNum": 0,
      "EPOComputerProperties.OSCsdVersion": "",
      "EPOComputerProperties.OSOEMID": "",
      "EPOComputerProperties.OSPlatform": "",
      "EPOComputerProperties.OSType": "",
      "EPOComputerProperties.OSVersion": "",
      "EPOComputerProperties.ParentID": 1011,
      "EPOComputerProperties.SubnetAddress": "",
      "EPOComputerProperties.SubnetMask": "",
      "EPOComputerProperties.TimeZone": "",
      "EPOComputerProperties.TotalDiskSpace": 0,
      "EPOComputerProperties.TotalPhysicalMemory": 0,
      "EPOComputerProperties.Total_Space_of_Drive_C": 0,
      "EPOComputerProperties.UserName": "",
      "EPOComputerProperties.UserProperty1": null,
      "EPOComputerProperties.UserProperty2": null,
      "EPOComputerProperties.UserProperty3": null,
      "EPOComputerProperties.UserProperty4": null,
      "EPOComputerProperties.UserProperty5": null,
      "EPOComputerProperties.UserProperty6": null,
      "EPOComputerProperties.UserProperty7": null,
      "EPOComputerProperties.UserProperty8": null,
      "EPOComputerProperties.Vdi": -1,
      "EPOLeafNode.AgentGUID": null,
      "EPOLeafNode.AgentVersion": null,
      "EPOLeafNode.ExcludedTags": "",
      "EPOLeafNode.LastUpdate": null,
      "EPOLeafNode.ManagedState": 0,
      "EPOLeafNode.Tags": "Workstation"
    }
  ],
  "inputs": {
    "mcafee_epo_systems": "richard test1"
  },
  "metrics": {
    "execution_time_ms": 547,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:07:06",
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
if getattr(playbook.inputs, "epo_system", None):
  inputs.mcafee_epo_systems = getattr(playbook.inputs, "epo_system")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.system
note = ''
if results.get("success"):
  resContent = results.get('content', [])
  for x in range(len(resContent)):
    content = dict((k, v) for k, v in resContent[x].items() if v and "N/A" not in str(v))
    note += "{}\n{}".format(resContent[x].get('EPOComputerProperties.ComputerName'), str(content))

  incident.addNote(note.replace("{","").replace("u'","'").replace("}","\n\n"))
```

</p>
</details>

---
## Function - McAfee ePO Find Client Tasks
Find client tasks on the ePO server.
McAfee user requires view permission for at least one product for this function.

 ![screenshot: fn-mcafee-epo-find-client-tasks ](./doc/screenshots/fn-mcafee-epo-find-client-tasks.png)
<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `datatable_name` | `text` | No | `Name of the datatable being cleared` | - |
| `incident_id` | `number` | No | `SOAR incident id` | - |
| `mcafee_epo_search_text` | `text` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "objectId": 7,
      "objectName": "Collect All",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 4,
      "typeName": "McAfee Agent: McAfee Agent Statistics"
    }
  ],
  "inputs": {
    "datatable_name": "mcafee_epo_client_tasks",
    "incident_id": 4057
  },
  "metrics": {
    "execution_time_ms": 1653,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 10:39:57",
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
inputs.datatable_name = "mcafee_epo_client_tasks"
inputs.incident_id = incident.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.client_task
if results.get("success"):
  for x in results.get("content", {}):
    table = incident.addRow("mcafee_epo_client_tasks")
    table["object_name"] = x.get("objectName")
    table["type_name"] = x.get("typeName")
    table["product_name"] = x.get("productName")
    table["product_id"] = x.get("productId")
    table["task_id"] = x.get("objectId")
```

</p>
</details>

---
## Function - McAfee ePO Find Groups
Find groups on the ePO server.
McAfee user requires access to at least one group in the System Tree for this function.

 ![screenshot: fn-mcafee-epo-find-groups ](./doc/screenshots/fn-mcafee-epo-find-groups.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `datatable_name` | `text` | No | `Name of the datatable being cleared` | - |
| `incident_id` | `number` | No | `SOAR incident id` | - |
| `mcafee_epo_search_text` | `text` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "groupId": 2,
      "groupPath": "My Organization"
    },
    {
      "groupId": 3,
      "groupPath": "My Organization\\Lost and Found"
    },
    {
      "groupId": 4,
      "groupPath": "My Organization\\Lost and Found\\ibm.com"
    },
    {
      "groupId": 5,
      "groupPath": "My Organization\\Test"
    }
  ],
  "inputs": {},
  "metrics": {
    "execution_time_ms": 1963,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 10:40:13",
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

```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.query
groupsResults = playbook.functions.results.groups
if results.get("success"):
  for groupInfo in groupsResults.get("content", {}):
    groupPath = groupInfo.get("groupPath")
    table = incident.addRow("mcafee_epo_groups")
    table["group_id"] = int(groupInfo.get("groupId"))
    table["group_path"] = groupPath
    systems = ""
    for group in results.get("content", {}):
      # EPOBranchNode.NodeTextPath2 only returns path after My Organization
      path2 = group.get("EPOBranchNode.NodeTextPath2")
      # EPOBranchNode.NodeTextPath2 returns the path, Lost and Found, as, Lost&Found,
      # so it needs to be converted in order to compare paths.
      path2 = path2.replace("Lost&Found", "Lost and Found")
      # Add, My Organization, to the beginning of the path
      path2 = "My Organization{}".format(path2[:len(path2)-1])

      if groupPath == path2:
        systems = "{}, {}".format(systems, group.get("EPOLeafNode.NodeName"))
    table["systems"] = systems[2:]
```

</p>
</details>

---
## Function - McAfee ePO Find Policies
Finds all policies that match the given search text or find all policies if no search text is given.
McAfee user requires view permission for at least one product for this function.

 ![screenshot: fn-mcafee-epo-find-policies ](./doc/screenshots/fn-mcafee-epo-find-policies.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `datatable_name` | `text` | No | `Name of the datatable being cleared` | - |
| `incident_id` | `number` | No | `SOAR incident id` | - |
| `mcafee_epo_search_text` | `text` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 4,
      "objectName": "McAfee Default",
      "objectNotes": "The McAfee Default policy is configured with settings recommended by McAfee to protect many environments",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 3,
      "typeName": "General"
    },
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 9,
      "objectName": "Large Organization Default",
      "objectNotes": "The Large Organization Default policy is configured with settings recommended by McAfee to protect large enterprise environments.",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 3,
      "typeName": "General"
    },
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 11,
      "objectName": "My Default",
      "objectNotes": "",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 3,
      "typeName": "General"
    },
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 5,
      "objectName": "McAfee Default",
      "objectNotes": "The McAfee Default policy is configured with settings recommended by McAfee to protect many environments",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 4,
      "typeName": "Repository"
    },
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 12,
      "objectName": "My Default",
      "objectNotes": "",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 4,
      "typeName": "Repository"
    },
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 6,
      "objectName": "McAfee Default",
      "objectNotes": "The McAfee Default policy is configured with settings recommended by McAfee to protect many environments",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 5,
      "typeName": "Troubleshooting"
    },
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 13,
      "objectName": "My Default",
      "objectNotes": "",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 5,
      "typeName": "Troubleshooting"
    },
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 7,
      "objectName": "McAfee Default",
      "objectNotes": "",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 6,
      "typeName": "Custom Properties"
    },
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 14,
      "objectName": "My Default",
      "objectNotes": "",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 6,
      "typeName": "Custom Properties"
    },
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 8,
      "objectName": "McAfee Default",
      "objectNotes": "The McAfee Default policy is configured with settings recommended by McAfee to protect many environments",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 7,
      "typeName": "Product Improvement Program"
    },
    {
      "featureId": "EPOAGENTMETA",
      "featureName": "McAfee Agent",
      "objectId": 15,
      "objectName": "My Default",
      "objectNotes": "",
      "productId": "EPOAGENTMETA",
      "productName": "McAfee Agent ",
      "typeId": 7,
      "typeName": "Product Improvement Program"
    }
  ],
  "inputs": {},
  "metrics": {
    "execution_time_ms": 816,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 10:40:31",
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

```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.query
policiesResults = playbook.functions.results.policies
if results.get("success"):
  for policy in policiesResults.get("content", {}):
    policyId = int(policy.get("objectId"))
    table_row = incident.addRow("mcafee_epo_policies")
    table_row["object_name"] = policy.get("objectName")
    table_row["object_id"] = policyId
    table_row["type_name"] = policy.get("typeName")
    table_row["type_id"] = int(policy.get("typeId"))
    table_row["product_id"] = policy.get("productId")
    table_row["object_notes"] = policy.get("objectNotes")
    systems = ""
    for assigned in results.get("content", {}):
      if assigned.get("EPOAssignedPolicy.PolicyObjectID") == policyId:
        systems = "{}, {}".format(systems, assigned.get("EPOAssignedPolicy.NodeName"))

    table_row["systems"] = systems[2:]
```

</p>
</details>

---
## Function - McAfee ePO Find Systems in Group
Find systems in a specified group on ePO server.
McAfee user requires access to at least one group for this function.

 ![screenshot: fn-mcafee-epo-find-systems-in-group ](./doc/screenshots/fn-mcafee-epo-find-systems-in-group.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_group_id` | `number` | No | `-` | Id for the group on the ePO server |
| `mcafee_epo_sub_group` | `text` | No | `-` | Sub group name |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "EPOBranchNode.AutoID": 5,
      "EPOComputerProperties.CPUSerialNumber": "",
      "EPOComputerProperties.CPUSpeed": 0,
      "EPOComputerProperties.CPUType": "",
      "EPOComputerProperties.ComputerDescription": null,
      "EPOComputerProperties.ComputerName": "SystemA",
      "EPOComputerProperties.DefaultLangID": "",
      "EPOComputerProperties.Description": null,
      "EPOComputerProperties.DomainName": "",
      "EPOComputerProperties.FreeDiskSpace": 0,
      "EPOComputerProperties.FreeMemory": 0,
      "EPOComputerProperties.Free_Space_of_Drive_C": 0,
      "EPOComputerProperties.IPAddress": "",
      "EPOComputerProperties.IPHostName": "",
      "EPOComputerProperties.IPSubnet": null,
      "EPOComputerProperties.IPSubnetMask": null,
      "EPOComputerProperties.IPV4x": null,
      "EPOComputerProperties.IPV6": null,
      "EPOComputerProperties.IPXAddress": "",
      "EPOComputerProperties.IsPortable": -1,
      "EPOComputerProperties.LastAgentHandler": null,
      "EPOComputerProperties.NetAddress": "",
      "EPOComputerProperties.NumOfCPU": 0,
      "EPOComputerProperties.OSBitMode": -1,
      "EPOComputerProperties.OSBuildNum": 0,
      "EPOComputerProperties.OSCsdVersion": "",
      "EPOComputerProperties.OSOEMID": "",
      "EPOComputerProperties.OSPlatform": "",
      "EPOComputerProperties.OSType": "",
      "EPOComputerProperties.OSVersion": "",
      "EPOComputerProperties.ParentID": 12,
      "EPOComputerProperties.SubnetAddress": "",
      "EPOComputerProperties.SubnetMask": "",
      "EPOComputerProperties.TimeZone": "",
      "EPOComputerProperties.TotalDiskSpace": 0,
      "EPOComputerProperties.TotalPhysicalMemory": 0,
      "EPOComputerProperties.Total_Space_of_Drive_C": 0,
      "EPOComputerProperties.UserName": "",
      "EPOComputerProperties.UserProperty1": null,
      "EPOComputerProperties.UserProperty2": null,
      "EPOComputerProperties.UserProperty3": null,
      "EPOComputerProperties.UserProperty4": null,
      "EPOComputerProperties.UserProperty5": null,
      "EPOComputerProperties.UserProperty6": null,
      "EPOComputerProperties.UserProperty7": null,
      "EPOComputerProperties.UserProperty8": null,
      "EPOComputerProperties.Vdi": -1,
      "EPOLeafNode.AgentGUID": null,
      "EPOLeafNode.AgentVersion": null,
      "EPOLeafNode.ExcludedTags": "",
      "EPOLeafNode.LastUpdate": null,
      "EPOLeafNode.ManagedState": 0,
      "EPOLeafNode.Tags": ""
    }
  ],
  "inputs": {
    "mcafee_epo_group_id": 5
  },
  "metrics": {
    "execution_time_ms": 578,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "1.1.0",
    "timestamp": "2022-08-22 11:45:56",
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
None
```

</p>
</details>

---
## Function - McAfee ePO Get All Permission sets
Get all of the permission sets on an ePO server.
McAfee user requires administrator rights for this function.

 ![screenshot: fn-mcafee-epo-get-all-permission-sets ](./doc/screenshots/fn-mcafee-epo-get-all-permission-sets.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `datatable_name` | `text` | No | `Name of the datatable being cleared` | - |
| `incident_id` | `number` | No | `SOAR incident id` | - |
| `mcafee_epo_username` | `text` | No | `-` | User name for ePO user |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "id": 4,
      "name": "Executive Reviewer"
    },
    {
      "id": 1,
      "name": "Global Reviewer"
    },
    {
      "id": 2,
      "name": "Group Admin"
    },
    {
      "id": 3,
      "name": "Group Reviewer"
    },
    {
      "id": 5,
      "name": "test"
    }
  ],
  "inputs": {},
  "metrics": {
    "execution_time_ms": 606,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 10:54:04",
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

```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.query
perm_sets = playbook.functions.results.perm_sets
if results.get("success"):
  for permset in perm_sets.get("content", {}):
    permsetName = permset.get("name")
    table_row = incident.addRow("mcafee_epo_permission_sets")
    table_row["permission_set_name"] = permsetName
    users = ""
    for perm in results.get("content", {}):
      user = perm.get("EntitlementView.PrincipalName")
      permGroup = perm.get("EntitlementView.GroupName")
      if user and permGroup and permsetName.lower() == permGroup.lower() and user not in users:
        users = "{}, {}".format(users, user)
    table_row["users"] = users[2:]
```

</p>
</details>

---
## Function - McAfee ePO Get All Users
Get all the users on a ePO server.
McAfee user requires administrator rights for this function.

 ![screenshot: fn-mcafee-epo-get-all-users ](./doc/screenshots/fn-mcafee-epo-get-all-users.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `datatable_name` | `text` | No | `Name of the datatable being cleared` | - |
| `incident_id` | `number` | No | `SOAR incident id` | - |
| `mcafee_epo_permsetname` | `text` | No | `-` | Name of the permission set to add to the ePO user |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "admin": true,
      "allowedIPs": "",
      "authDetails": "",
      "authType": "pwd",
      "disabled": false,
      "email": "",
      "fullName": "",
      "id": 1,
      "name": "admin",
      "notes": "",
      "phoneNumber": ""
    },
    {
      "admin": false,
      "allowedIPs": "",
      "authDetails": "",
      "authType": "pwd",
      "disabled": false,
      "email": "",
      "fullName": "",
      "id": 6,
      "name": "New user",
      "notes": "",
      "phoneNumber": ""
    },
    {
      "admin": false,
      "allowedIPs": "",
      "authDetails": "",
      "authType": "pwd",
      "disabled": false,
      "email": "richard@test.com",
      "fullName": "Richard Test",
      "id": 5,
      "name": "richard-test",
      "notes": "Hello",
      "phoneNumber": "7394034758"
    },
    {
      "admin": true,
      "allowedIPs": "",
      "authDetails": "",
      "authType": "pwd",
      "disabled": true,
      "email": "",
      "fullName": "",
      "id": 2,
      "name": "system",
      "notes": "",
      "phoneNumber": ""
    }
  ],
  "inputs": {
    "datatable_name": "mcafee_epo_users",
    "incident_id": 4057
  },
  "metrics": {
    "execution_time_ms": 820,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 10:55:20",
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
inputs.datatable_name = "mcafee_epo_users"
inputs.incident_id = incident.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.users
if results.get("success"):
  for user in results.get("content", {}):
    table_row = incident.addRow("mcafee_epo_users")
    table_row["user_name"] = user.get("name")
    table_row["full_name"] = user.get("fullName")
    table_row["email"] = user.get("email")
    table_row["phone_number"] = user.get("phoneNumber")
    table_row["disabled"] = bool(user.get("disabled"))
    table_row["admin"] = bool(user.get("admin"))
    table_row["notes"] = user.get("notes")
    table_row["allowed_ips"] = user.get("allowedIPs")
    table_row["user_deleted"] = False
```

</p>
</details>

---
## Function - McAfee ePO List Issues
List the issues on the ePO server.
McAfee user requires permission to view issues for this function.

 ![screenshot: fn-mcafee-epo-list-issues ](./doc/screenshots/fn-mcafee-epo-list-issues.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `datatable_name` | `text` | No | `Name of the datatable being cleared` | - |
| `incident_id` | `number` | No | `SOAR incident id` | - |
| `mcafee_epo_issue_id` | `number` | No | `-` | ID of the issue |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "activityLog": [
        {
          "date": "2023-10-09T07:39:15-07:00",
          "details": "",
          "dirty": true,
          "id": 1,
          "issueId": 1,
          "title": "Issue Created",
          "username": "admin"
        }
      ],
      "assignee": null,
      "assigneeName": "",
      "createdDate": "2023-10-09T07:39:15-07:00",
      "creatorName": "admin",
      "description": "Testing issue creation",
      "dueDate": 1698308400000,
      "id": 1,
      "name": "richard test issue",
      "priority": "LOW",
      "resolution": "NONE",
      "severity": "LOW",
      "state": "NEW",
      "subtype": null,
      "ticketId": null,
      "ticketServerName": null,
      "type": "BASIC"
    }
  ],
  "inputs": {
    "datatable_name": "mcafee_epo_issues",
    "incident_id": 4057
  },
  "metrics": {
    "execution_time_ms": 1069,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:02:47",
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
inputs.datatable_name = "mcafee_epo_issues"
inputs.incident_id = incident.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.issues
if results.get("success"):
  for c in results.get("content", {}):
    row = incident.addRow("mcafee_epo_issues")
    row["issue_name"] = c.get("name")
    row["issue_id"] = int(c.get("id"))
    row["severity"] = c.get("severity")
    row["issue_due_date"] = c.get("dueDate")
    row["issue_description"] = c.get("description")
    row["ticket_server_name"] = c.get("ticketServerName")
    row["priority"] = c.get("priority")
    row["type"] = c.get("type")
    row["resolution"] = c.get("resolution")
    row["assignee_name"] = c.get("assigneeName")
    row["issue_state"] = c.get("state")
    row["ticket_id"] = int(c.get("ticketId")) if c.get("ticketId") else None
    row["issue_deleted"] = False
```

</p>
</details>

---
## Function - McAfee ePO List Tags
Find all tags specified in ePO.
McAfee user requires Tag use permission for this function.

 ![screenshot: fn-mcafee-epo-list-tags ](./doc/screenshots/fn-mcafee-epo-list-tags.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `datatable_name` | `text` | No | `Name of the datatable being cleared` | - |
| `incident_id` | `number` | No | `SOAR incident id` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "tagId": 1,
      "tagName": "Server",
      "tagNotes": "Default tag for systems identified as a Server"
    },
    {
      "tagId": 2,
      "tagName": "Workstation",
      "tagNotes": "Default tag for systems identified as a Workstation"
    }
  ],
  "inputs": {
    "datatable_name": "mcafee_epo_tags",
    "incident_id": 4057
  },
  "metrics": {
    "execution_time_ms": 887,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:02:57",
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
inputs.datatable_name = "mcafee_epo_tags"
inputs.incident_id = incident.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.tags
if results.get("success"):
  for tag in sorted(results.get("content", {}), key = lambda i: i['tagName'].lower()):
    row = incident.addRow("mcafee_epo_tags")
    row['epo_id'] = tag.get('tagId')
    row['epo_tag'] = tag.get('tagName')
    row['epo_notes'] = tag.get('tagNotes')
```

</p>
</details>

---
## Function - McAfee ePO Remove Permission sets from user
Remove permission set(s) from an ePO user.
McAfee user requires administrator rights for this function.

 ![screenshot: fn-mcafee-epo-remove-permission-sets-from-user ](./doc/screenshots/fn-mcafee-epo-remove-permission-sets-from-user.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_permsetname` | `text` | No | `-` | Name of the permission set to add to the ePO user |
| `mcafee_epo_username` | `text` | No | `-` | User name for ePO user |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": true,
  "inputs": {
    "mcafee_epo_permsetname": "test",
    "mcafee_epo_username": "richard-test"
  },
  "metrics": {
    "execution_time_ms": 564,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:19:35",
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
inputs.mcafee_epo_permsetname = row.permission_set_name
if getattr(playbook.inputs, "epo_username", None):
  inputs.mcafee_epo_username = getattr(playbook.inputs, "epo_username")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.remove_perms
if results.get('success'):
  incident.addNote("Permissions set: {} was removed from user: {}".format(row.permission_set_name, getattr(playbook.inputs, "epo_username")))
  if row.users:
    usersList = list(row.users.split(", "))
    usersList.remove(getattr(playbook.inputs, "epo_username"))
    row.users = str(usersList).replace("[","").replace("]","").replace("'","")
```

</p>
</details>

---
## Function - McAfee ePO Remove Tag
Remove a tag associated with an ePO system(s).
McAfee user requires Tag use permission for this function.

 ![screenshot: fn-mcafee-epo-remove-tag ](./doc/screenshots/fn-mcafee-epo-remove-tag.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_systems` | `text` | No | `-` | Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO |
| `mcafee_epo_tag` | `text` | No | `-` | Tag managed on ePO |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": 1,
  "inputs": {
    "mcafee_epo_systems": "richard test1",
    "mcafee_epo_tag": "workstation"
  },
  "metrics": {
    "execution_time_ms": 555,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:07:44",
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
inputs.mcafee_epo_systems = artifact.value
if getattr(playbook.inputs, "list_of_tags", None):
  inputs.mcafee_epo_tag = str(getattr(playbook.inputs, "list_of_tags"))
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.tags_results
if not results.get("success"):
  note = "ePO system not found or tag not applied: {}".format(results.inputs.get('mcafee_epo_tag'))
else:
  note = "ePO tag(s) removed: {}".format(results.inputs.get('mcafee_epo_tag'))

if artifact.description:
  artifact.description = u"{}\n\n{}".format(artifact.description.content, note)
else:
  artifact.description = note
```

</p>
</details>

---
## Function - McAfee ePO Remove User
Delete a user from the ePO server.
McAfee user requires administrator rights for this function.

 ![screenshot: fn-mcafee-epo-remove-user ](./doc/screenshots/fn-mcafee-epo-remove-user.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_username` | `text` | No | `-` | User name for ePO user |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": true,
  "inputs": {
    "mcafee_epo_username": "New user"
  },
  "metrics": {
    "execution_time_ms": 1017,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:23:23",
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
inputs.mcafee_epo_username = row.user_name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.remove_user
if results.get("success"):
  row.user_deleted = True
  incident.addNote("User: {} removed  from ePO server".format(row.user_name))
```

</p>
</details>

---
## Function - McAfee ePO Run Client Task
Run a client task on specified system(s).
McAfee user requires edit permission for at least one product for this function.

 ![screenshot: fn-mcafee-epo-run-client-task ](./doc/screenshots/fn-mcafee-epo-run-client-task.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_abort_after_minutes` | `number` | No | `-` | Number of minutes to wait to abort a call that isn't responding |
| `mcafee_epo_product_id` | `text` | No | `-` | The product ID for the task |
| `mcafee_epo_random_minutes` | `number` | No | `-` | number of random minutes |
| `mcafee_epo_retry_attempts` | `number` | No | `-` | Number of times to retry call |
| `mcafee_epo_retry_intervals_in_seconds` | `number` | No | `-` | Number of seconds to wait between retries |
| `mcafee_epo_stop_after_minutes` | `number` | No | `-` | number of minutes to wait until stopping retry call |
| `mcafee_epo_system_name_or_id` | `text` | No | `-` | Comma separated list of systems name or system ids |
| `mcafee_epo_task_id` | `number` | No | `-` | The ID of the client task |
| `mcafee_epo_timeout_in_hours` | `number` | No | `-` | Number of hours to wait until timeout |
| `mcafee_epo_use_all_agent_handlers` | `boolean` | No | `-` | True or false to use all agent handlers |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": "Succeeded",
  "inputs": {
    "mcafee_epo_product_id": "EPOAGENTMETA",
    "mcafee_epo_system_name_or_id": "int-mcafee-tie",
    "mcafee_epo_task_id": 7
  },
  "metrics": {
    "execution_time_ms": 581,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:12:46",
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
if getattr(playbook.inputs, "epo_system_names_or_ids", None):
  inputs.mcafee_epo_system_name_or_id = getattr(playbook.inputs, "epo_system_names_or_ids")
inputs.mcafee_epo_product_id = row.product_id
inputs.mcafee_epo_task_id = int(row.task_id)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.run_task
if results.get("success"):
  incident.addNote("System(s): '{}' ran client task: '{}' successfully.".format(getattr(playbook.inputs, "epo_system_names_or_ids"), row.object_name))
```

</p>
</details>

---
## Function - McAfee ePO Update Issue
Update an issue on the ePO server.
McAfee user requires permission to edit the issue for this function.

 ![screenshot: fn-mcafee-epo-update-issue ](./doc/screenshots/fn-mcafee-epo-update-issue.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_issue_assignee` | `text` | No | `-` | Username of person assigned to the issue |
| `mcafee_epo_issue_description` | `text` | No | `-` | description of the issue  |
| `mcafee_epo_issue_due` | `datetimepicker` | No | `-` | Due date of the issue |
| `mcafee_epo_issue_id` | `number` | No | `-` | ID of the issue |
| `mcafee_epo_issue_name` | `text` | No | `-` | Name of the issue on the ePO server |
| `mcafee_epo_issue_priority` | `select` | No | `-` | The priority of the issue |
| `mcafee_epo_issue_properties` | `text` | No | `-` | Properties for the issue |
| `mcafee_epo_issue_resolution` | `select` | No | `-` | Resolution status of the issue |
| `mcafee_epo_issue_severity` | `select` | No | `-` | Severity of the issue |
| `mcafee_epo_issue_state` | `select` | No | `-` | State of the issue |
| `mcafee_epo_ticket_id` | `number` | No | `-` | ID of the ticket |
| `mcafee_epo_ticket_server_name` | `text` | No | `-` | Name of the server the issue should be on |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": 1,
  "inputs": {
    "mcafee_epo_issue_assignee": "richard-test",
    "mcafee_epo_issue_description": null,
    "mcafee_epo_issue_due": null,
    "mcafee_epo_issue_id": 1,
    "mcafee_epo_issue_name": null,
    "mcafee_epo_issue_priority": "Medium",
    "mcafee_epo_issue_properties": null,
    "mcafee_epo_issue_resolution": "None",
    "mcafee_epo_issue_severity": "Medium",
    "mcafee_epo_issue_state": null,
    "mcafee_epo_ticket_id": null,
    "mcafee_epo_ticket_server_name": null
  },
  "metrics": {
    "execution_time_ms": 491,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:14:30",
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
if getattr(playbook.inputs, "epo_issue_assignee", None):
  inputs.mcafee_epo_issue_assignee = getattr(playbook.inputs, "epo_issue_assignee")
if getattr(playbook.inputs, "epo_issue_description", None):
  inputs.mcafee_epo_issue_description = getattr(playbook.inputs, "epo_issue_description")
if getattr(playbook.inputs, "epo_issue_due", None):
  inputs.mcafee_epo_issue_due = getattr(playbook.inputs, "epo_issue_due")
inputs.mcafee_epo_issue_id = row.issue_id
if getattr(playbook.inputs, "epo_issue_name", None):
  inputs.mcafee_epo_issue_name = getattr(playbook.inputs, "epo_issue_name")
if getattr(playbook.inputs, "epo_issue_priority", None):
  inputs.mcafee_epo_issue_priority = getattr(playbook.inputs, "epo_issue_priority")
if getattr(playbook.inputs, "epo_issue_properties", None):
  inputs.mcafee_epo_issue_properties = getattr(playbook.inputs, "epo_issue_properties")
if getattr(playbook.inputs, "epo_issue_resolution", None):
  inputs.mcafee_epo_issue_resolution = getattr(playbook.inputs, "epo_issue_resolution")
if getattr(playbook.inputs, "epo_issue_severity", None):
  inputs.mcafee_epo_issue_severity = getattr(playbook.inputs, "epo_issue_severity")
if getattr(playbook.inputs, "epo_issue_state", None):
  inputs.mcafee_epo_issue_state = getattr(playbook.inputs, "epo_issue_state")
if getattr(playbook.inputs, "epo_ticket_id", None):
  inputs.mcafee_epo_ticket_id = getattr(playbook.inputs, "epo_ticket_id")
if getattr(playbook.inputs, "epo_ticket_server_name", None):
  inputs.mcafee_epo_ticket_server_name = getattr(playbook.inputs, "epo_ticket_server_name")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.issue
note = ""
if results.get("success"):
  inputs = results.get("inputs")
  if inputs.get("mcafee_epo_issue_priority"):
    row.priority = inputs.get("mcafee_epo_issue_priority")
    note += "Priority updated: {}\n".format(inputs.get("mcafee_epo_issue_priority"))
  if inputs.get("mcafee_epo_ticket_server_name"):
    row.ticket_server_name = inputs.get("mcafee_epo_ticket_server_name")
    note += "Ticket Server Name updated: {}\n".format(inputs.get("mcafee_epo_ticket_server_name"))
  if inputs.get("mcafee_epo_issue_resolution"):
    row.resolution = inputs.get("mcafee_epo_issue_resolution")
    note += "Resolution updated: {}\n".format(inputs.get("mcafee_epo_issue_resolution"))
  if inputs.get("mcafee_epo_issue_due"):
    row.issue_due_date = inputs.get("mcafee_epo_issue_due")
    note += "Due Date updated: {}\n".format(inputs.get("mcafee_epo_issue_due"))
  if inputs.get("mcafee_epo_ticket_id"):
    row.ticket_id = inputs.get("mcafee_epo_ticket_id")
    note += "Ticket ID updated: {}\n".format(inputs.get("mcafee_epo_ticket_id"))
  if inputs.get("mcafee_epo_issue_severity"):
    row.severity = inputs.get("mcafee_epo_issue_severity")
    note += "Severity updated: {}\n".format(inputs.get("mcafee_epo_issue_severity"))
  if inputs.get("mcafee_epo_issue_state"):
    row.issue_state = inputs.get("mcafee_epo_issue_state")
    note += "State updated: {}\n".format(inputs.get("mcafee_epo_issue_state"))
  if inputs.get("mcafee_epo_issue_name"):
    row.issue_name = inputs.get("mcafee_epo_issue_name")
    note += "Name updated: {}\n".format(inputs.get("mcafee_epo_issue_name"))
  if inputs.get("mcafee_epo_issue_assignee"):
    row.assignee_name = inputs.get("mcafee_epo_issue_assignee")
    note += "Assignee updated: {}\n".format(inputs.get("mcafee_epo_issue_assignee"))
  if inputs.get("mcafee_epo_issue_description"):
    row.issue_description = inputs.get("mcafee_epo_issue_description")
    note += "Description updated: {}\n".format(inputs.get("mcafee_epo_issue_description"))
  incident.addNote("Issue ID: '{}' updated \n{}".format(row.issue_id, note))
```

</p>
</details>

---
## Function - McAfee ePO Update User
Update a user on the ePO server.
McAfee user requires administrator rights for this function.

 ![screenshot: fn-mcafee-epo-update-user ](./doc/screenshots/fn-mcafee-epo-update-user.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_admin` | `boolean` | No | `-` | Should this user have admin privileges  |
| `mcafee_epo_allowed_ips` | `text` | No | `-` | A list of ips that can access the new user |
| `mcafee_epo_email` | `text` | No | `-` | Email for the new user |
| `mcafee_epo_fullname` | `text` | No | `-` | Full name for the new user |
| `mcafee_epo_new_username` | `text` | No | `-` | Change the ePO users username |
| `mcafee_epo_notes` | `text` | No | `-` | Notes to add to the new user |
| `mcafee_epo_pass` | `text` | No | `-` | Password for ePO user |
| `mcafee_epo_phone_number` | `text` | No | `-` | Phone number for the new user |
| `mcafee_epo_subjectdn` | `text` | No | `-` | Add a subject DN to the ePO users info |
| `mcafee_epo_user_disabled` | `boolean` | No | `-` | Should the new user be disabled when created? |
| `mcafee_epo_username` | `text` | No | `-` | User name for ePO user |
| `mcafee_epo_windowsdomain` | `text` | No | `-` | Add a windows domain to the ePO users info |
| `mcafee_epo_windowsusername` | `text` | No | `-` | Add a windows user name to the ePO users info |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": true,
  "inputs": {
    "mcafee_epo_admin": true,
    "mcafee_epo_allowed_ips": null,
    "mcafee_epo_email": null,
    "mcafee_epo_fullname": "Richard tester",
    "mcafee_epo_new_username": null,
    "mcafee_epo_notes": "helo world",
    "mcafee_epo_pass": null,
    "mcafee_epo_phone_number": null,
    "mcafee_epo_subjectdn": null,
    "mcafee_epo_user_disabled": null,
    "mcafee_epo_username": "richard-test",
    "mcafee_epo_windowsdomain": null,
    "mcafee_epo_windowsusername": null
  },
  "metrics": {
    "execution_time_ms": 543,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:23:02",
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
if getattr(playbook.inputs, "epo_admin", None):
  inputs.mcafee_epo_admin = getattr(playbook.inputs, "epo_admin")
if getattr(playbook.inputs, "epo_allowed_ips", None):
  inputs.mcafee_epo_allowed_ips = getattr(playbook.inputs, "epo_allowed_ips")
if getattr(playbook.inputs, "epo_email", None):
  inputs.mcafee_epo_email = getattr(playbook.inputs, "epo_email")
if getattr(playbook.inputs, "epo_full_name", None):
  inputs.mcafee_epo_fullname = getattr(playbook.inputs, "epo_full_name")
if getattr(playbook.inputs, "epo_notes", None):
  inputs.mcafee_epo_notes = getattr(playbook.inputs, "epo_notes")
if getattr(playbook.inputs, "epo_user_password", None):
  inputs.mcafee_epo_pass = getattr(playbook.inputs, "epo_user_password")
if getattr(playbook.inputs, "epo_phone_number", None):
  inputs.mcafee_epo_phone_number = getattr(playbook.inputs, "epo_phone_number")
if getattr(playbook.inputs, "epo_user_disabled", None):
  inputs.mcafee_epo_user_disabled = getattr(playbook.inputs, "epo_user_disabled")
inputs.mcafee_epo_username = row.user_name
if getattr(playbook.inputs, "epo_new_username", None):
  inputs.mcafee_epo_new_username = getattr(playbook.inputs, "epo_new_username")
if getattr(playbook.inputs, "epo_subject_dn", None):
  inputs.mcafee_epo_subjectdn = getattr(playbook.inputs, "epo_subject_dn")
if getattr(playbook.inputs, "epo_windows_domain", None):
  inputs.mcafee_epo_windowsdomain = getattr(playbook.inputs, "epo_windows_domain")
if getattr(playbook.inputs, "epo_windows_username", None):
  inputs.mcafee_epo_windowsusername = getattr(playbook.inputs, "epo_windows_username")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.user
note = ""
if results.get("success"):
  inputs = results.get("inputs")
  if inputs.get("mcafee_epo_new_username"):
    row.user_name = inputs.get("mcafee_epo_new_username")
    note += "Username updated: {}\n".format(inputs.get("mcafee_epo_new_username"))
  if inputs.get("mcafee_epo_fullname"):
    row.full_name = inputs.get("mcafee_epo_fullname")
    note += "Full name updated: {}\n".format(inputs.get("mcafee_epo_fullname"))
  if inputs.get("mcafee_epo_email"):
    row.email = inputs.get("mcafee_epo_email")
    note += "Email updated: {}\n".format(inputs.get("mcafee_epo_email"))
  if inputs.get("mcafee_epo_phone_number"):
    row.phone_number = inputs.get("mcafee_epo_phone_number")
    note += "Phone number updated: {}\n".format(inputs.get("mcafee_epo_phone_number"))
  if inputs.get("mcafee_epo_user_disabled") != None:
    row.disabled = bool(inputs.get("mcafee_epo_user_disabled"))
    note += "User disabled updated: {}\n".format(bool(inputs.get("mcafee_epo_user_disabled")))
  if inputs.get("mcafee_epo_admin") != None:
    row.admin = bool(inputs.get("mcafee_epo_admin"))
    note += "Admin updated: {}\n".format(bool(inputs.get("mcafee_epo_admin")))
  if inputs.get("mcafee_epo_notes"):
    row.notes = inputs.get("mcafee_epo_notes")
    note += "Notes updated: {}\n".format(inputs.get("mcafee_epo_notes"))
  if inputs.get("mcafee_epo_allowed_ips"):
    row.allowed_ips = inputs.get("mcafee_epo_allowed_ips")
    note += "Allowed IPs updated: {}\n".format(inputs.get("mcafee_epo_allowed_ips"))
  incident.addNote("User: {} updated \n{}".format(row.user_name, note))
```

</p>
</details>

---
## Function - McAfee ePO Wake up agent
Wake up an ePO agent.
McAfee user requires Agent wakeup permission for this function.

 ![screenshot: fn-mcafee-epo-wake-up-agent ](./doc/screenshots/fn-mcafee-epo-wake-up-agent.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_systems` | `text` | No | `-` | Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": "completed: 1\nfailed: 0\nexpired: 0",
  "inputs": {
    "mcafee_epo_systems": "int-mcafee-tie"
  },
  "metrics": {
    "execution_time_ms": 25623,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:04:58",
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
if getattr(playbook.inputs, "epo_system", None):
  inputs.mcafee_epo_systems = getattr(playbook.inputs, "epo_system")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.wake_agent
if results.get("success"):
  incident.addNote(results.get("content", {}))
```

</p>
</details>

---
## Function - McAfee Tag an ePO Asset
Applies tag to the systems in ePO. Inputs include:
- mcafee_epo_system: Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO.
- mcafee_epo_tag: A tag managed on ePO.

McAfee user requires Tag use permission for this function.

 ![screenshot: fn-mcafee-tag-an-epo-asset ](./doc/screenshots/fn-mcafee-tag-an-epo-asset.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `mcafee_epo_systems` | `text` | No | `-` | Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO |
| `mcafee_epo_tag` | `text` | No | `-` | Tag managed on ePO |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": 1,
  "inputs": {
    "mcafee_epo_systems": "int-mcafee-tie",
    "mcafee_epo_tag": "Server"
  },
  "metrics": {
    "execution_time_ms": 514,
    "host": "local",
    "package": "fn-mcafee-epo",
    "package_version": "3.0.0",
    "timestamp": "2023-10-09 13:22:08",
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
inputs.mcafee_epo_systems = artifact.value
if getattr(playbook.inputs, "list_of_tags", None):
  inputs.mcafee_epo_tag = str(getattr(playbook.inputs, "list_of_tags", None))
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.tags_results
if results.get("success"):
  note = "ePO tag(s) added: {}".format(str(getattr(playbook.inputs, "list_of_tags")))
else:
  note = "ePO system not found or tag already applied: {}".format(str(getattr(playbook.inputs, "list_of_tags")))

if artifact.description:
  artifact.description = "{}\n\n{}".format(artifact.description.content, note)
else:
  artifact.description = note
```

</p>
</details>

---


## Data Table - McAfee ePO Client Tasks

 ![screenshot: dt-mcafee-epo-client-tasks](./doc/screenshots/dt-mcafee-epo-client-tasks.png)

#### API Name:
mcafee_epo_client_tasks

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Object Name | `object_name` | `text` | Name of the client task |
| Product ID | `product_id` | `text` | ID for the product |
| Product Name | `product_name` | `text` | Name of the product associated with the client task |
| Task ID | `task_id` | `number` | ID for the task |
| Type Name | `type_name` | `text` | Type of client task |

---
## Data Table - McAfee ePO Groups

 ![screenshot: dt-mcafee-epo-groups](./doc/screenshots/dt-mcafee-epo-groups.png)

#### API Name:
mcafee_epo_groups

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Group ID | `group_id` | `number` | ID of the group |
| Group Path | `group_path` | `text` | Path to the group on the ePO server |
| Systems | `systems` | `text` | Name of the systems in the group |

---
## Data Table - McAfee ePO Issues

 ![screenshot: dt-mcafee-epo-issues](./doc/screenshots/dt-mcafee-epo-issues.png)

#### API Name:
mcafee_epo_issues

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Assignee Name | `assignee_name` | `text` | - |
| Deleted | `issue_deleted` | `boolean` | - |
| Description | `issue_description` | `text` | - |
| Due Date | `issue_due_date` | `datetimepicker` | - |
| Issue ID | `issue_id` | `number` | - |
| Issue Name | `issue_name` | `text` | - |
| Priority | `priority` | `text` | - |
| Resolution | `resolution` | `text` | - |
| Severity | `severity` | `text` | - |
| State | `issue_state` | `text` | - |
| Ticket ID | `ticket_id` | `number` | - |
| Ticket Server Name | `ticket_server_name` | `text` | - |
| Type | `type` | `text` | - |

---
## Data Table - McAfee ePO Permission sets

 ![screenshot: dt-mcafee-epo-permission-sets](./doc/screenshots/dt-mcafee-epo-permission-sets.png)

#### API Name:
mcafee_epo_permission_sets

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Permission Set Name | `permission_set_name` | `text` | - |
| Users | `users` | `text` | Users that have the permission set |

---
## Data Table - McAfee ePO Policies

 ![screenshot: dt-mcafee-epo-policies](./doc/screenshots/dt-mcafee-epo-policies.png)

#### API Name:
mcafee_epo_policies

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Object ID | `object_id` | `number` | ID of the policy |
| Object Name | `object_name` | `text` | Name of the policy |
| Object Notes | `object_notes` | `text` | Notes for the policy |
| Product ID | `product_id` | `text` | ID of the product |
| Systems | `systems` | `text` | Systems assigned to the policy |
| Type ID | `type_id` | `number` | ID of the type of policy |
| Type Name | `type_name` | `text` | Name of the type of policy |

---
## Data Table - McAfee ePO Systems

 ![screenshot: dt-mcafee-epo-systems](./doc/screenshots/dt-mcafee-epo-systems.png)

#### API Name:
mcafee_epo_systems_dt

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Agent GUID | `epo_agent_guid` | `text` | - |
| Deleted | `epo_deleted` | `boolean` | If the System is deleted or not |
| Last Communication | `epo_last_communication` | `text` | - |
| Operating System | `epo_operating_system` | `text` | - |
| System Name | `epo_system_name` | `text` | - |
| Tags | `epo_tags` | `text` | - |

---
## Data Table - McAfee ePO tags

 ![screenshot: dt-mcafee-epo-tags](./doc/screenshots/dt-mcafee-epo-tags.png)

#### API Name:
mcafee_epo_tags

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Id | `epo_id` | `number` | - |
| Notes | `epo_notes` | `text` | - |
| Tag | `epo_tag` | `text` | - |

---
## Data Table - McAfee ePO Users

 ![screenshot: dt-mcafee-epo-users](./doc/screenshots/dt-mcafee-epo-users.png)

#### API Name:
mcafee_epo_users

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Admin | `admin` | `boolean` | - |
| Allowed IPs | `allowed_ips` | `text` | - |
| Disabled | `disabled` | `boolean` | - |
| Email | `email` | `text` | - |
| Full Name | `full_name` | `text` | - |
| Notes | `notes` | `text` | - |
| Phone Number | `phone_number` | `text` | - |
| User Deleted | `user_deleted` | `boolean` | - |
| User Name | `user_name` | `text` | - |

---


## Playbooks
| Playbook Name | Description | Activation Type | Object | Status | Condition |
| ------------- | ----------- | --------------- | ------ | ------ | ---------- |
| McAfee ePO Add Permission Set to User (PB) | None | Manual | mcafee_epo_permission_sets | `enabled` | `-` |
| McAfee ePO Add System (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO Add User (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO Apply a Tag (PB) | None | Manual | mcafee_epo_tags | `enabled` | `-` |
| McAfee ePO Apply Tags (PB) | None | Manual | artifact | `enabled` | `artifact.type in ['IP Address', 'DNS Name', 'System Name', 'MAC Address']` |
| McAfee ePO Assign Policy to Group from Group (PB) | None | Manual | mcafee_epo_groups | `enabled` | `-` |
| McAfee ePO Assign Policy to Group from Policy (PB) | None | Manual | mcafee_epo_policies | `enabled` | `-` |
| McAfee ePO Assign Policy to System from System (PB) | None | Manual | mcafee_epo_systems_dt | `enabled` | `-` |
| McAfee ePO Assign Policy to Systems from Policy (PB) | None | Manual | mcafee_epo_policies | `enabled` | `-` |
| McAfee ePO Create Issue (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO Delete Issue (PB) | None | Manual | mcafee_epo_issues | `enabled` | `-` |
| McAfee ePO Delete System (PB) | None | Manual | mcafee_epo_systems_dt | `enabled` | `-` |
| McAfee ePO Find All Client Tasks (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO Find All Groups (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO Find Policies (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO Get All Permission Sets (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO Get All Systems (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO Get All Users (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO Get System Info (PB) | None | Manual | artifact | `enabled` | `artifact.type in ['IP Address', 'DNS Name', 'System Name', 'MAC Address']` |
| McAfee ePO Get System Info from Property (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO List Issues (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO List Tags (PB) | None | Manual | incident | `enabled` | `-` |
| McAfee ePO Remove Permission Set from User (PB) | None | Manual | mcafee_epo_permission_sets | `enabled` | `-` |
| McAfee ePO Remove Tags (PB) | None | Manual | artifact | `enabled` | `artifact.type in ['IP Address', 'DNS Name', 'System Name', 'MAC Address']` |
| McAfee ePO Remove User (PB) | None | Manual | mcafee_epo_users | `enabled` | `-` |
| McAfee ePO Run Client Task (PB) | None | Manual | mcafee_epo_client_tasks | `enabled` | `-` |
| McAfee ePO Run Client Task on System (PB) | None | Manual | mcafee_epo_systems_dt | `enabled` | `-` |
| McAfee ePO Update Issue (PB) | None | Manual | mcafee_epo_issues | `enabled` | `-` |
| McAfee ePO Update User (PB) | None | Manual | mcafee_epo_users | `enabled` | `-` |
| McAfee ePO Wake up Agent (PB) | None | Manual | incident | `enabled` | `-` |

---

## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.

### For Support
This is an IBM supported app. Please search [ibm.com/mysupport](https://ibm.com/mysupport) for assistance.
