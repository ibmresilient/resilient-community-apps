# LDAP Utilities

## Table of Contents
- [Release Notes](#release-notes)
- [2.1.0 Changes](#210-changes)
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
  - [2.0.0 Changes](#200-changes)
- [Function - LDAP Utilities: Add](#function---ldap-utilities-add)
- [Function - LDAP Utilities: Add to Group(s)](#function---ldap-utilities-add-to-groups)
- [Function - LDAP Utilities: Remove from Group(s)](#function---ldap-utilities-remove-from-groups)
- [Function - LDAP Utilities: Search](#function---ldap-utilities-search)
- [Function - LDAP Utilities: Set Password](#function---ldap-utilities-set-password)
- [Function - LDAP Utilities: Toggle Access](#function---ldap-utilities-toggle-access)
- [Function - LDAP Utilities: Update](#function---ldap-utilities-update)
- [Script - No search results](#script---no-search-results)
  - [Custom Layouts](#custom-layouts)
- [Data Table - LDAP Query results](#data-table---ldap-query-results)
- [Custom Fields](#custom-fields)
- [Playbooks](#playbooks)
- [Troubleshooting & Support](#troubleshooting--support)

---

## Release Notes
| Version | Date | Notes |
| ------- | ---- | ----- |
| 2.1.4 | 05/2024 | Bug fix for using NTLM authentication. |
| 2.1.3 | 03/2024 | Bug fix for ldap_utilities_search.py function. |
| 2.1.2 | 08/2023 | Bug fix for set password function |
| 2.1.1 | 06/2023 | Bug fix for CP4S |
| 2.1.0 | 04/2023 | <ul><li>Update search function to perform a paged search.</li><li>Fix bug in set password function.</li><li>Convert all Rules and Workflows to Playbooks.</li></ul> |
| 2.0.1 | 07/2022 | Fix helper.py so that ldap_connect_timeout is not required in app.config |
| 2.0.0 | 04/2022 | <ul><li>Add ability to have multiple LDAP Domains</li><li>New rule to add users, groups, organizational units, etc.</li></ul>|
| 1.1.1 | 07/2021 | Support added for App Host |
| 1.1.0 | 03/2019 | <ul><li>Handle Unicode in Post-Process Scripts</li><li>Handle NTLM Authentication to Active Directory</li><li>Add functionality to allow for LDAP Wildcard queries with *</li></ul> |
| 1.0.0 | 07/2018 | Initial Release |

* For customers upgrading from a previous release to 2.0.0 or greater, the app.config file must be manually edited to add new settings required to each server configuration. See [2.0.0 Changes](#2.0.0-changes)

---
## 2.1.0 Changes
In v2.1, the existing rules and workflows have been replaced with playbooks. This change is made to support the ongoing, newer capabilities of playbooks. Each playbook has the same functionality as the previous, corresponding rule/workflow.

If upgrading from a previous release, you'll noticed that the previous release's rules/workflows remain in place. Both sets of rules and playbooks are active. For manual actions, playbooks will have the same name as it's corresponding rule, but with "(PB)" added at the end. For automatic actions, the playbooks will be disabled by default.

You can continue to use the rules/workflows. But migrating to playbooks will provide greater functionality along with future app enhancements and bug fixes.

---

## Overview
These LDAP Utility integrations allow multiple activities to be initiated from workflows in the IBM SOAR platform to an external LDAP server. Functions include: search, update, set password, toggle access, and add user.
**SOAR LDAP Utilities'**

 ![screenshot: main](./doc/screenshots/main.png)

IBM SOAR components to allow reading and manipulation of your LDAP Server'

### Key Features
* Add users, groups, organizational units to LDAP
* Add multiple users to multiple groups
* Remove multiple users from a group
* Run a person query against an LDAP server using the person's email address
* Search for a user using their email address, gets their DN and sets a new password for that user
* Enable/disable an Active Directory user account
* Update the value of a DN's attribute with the given value(s)

---

## Requirements
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, Edge Gateway (also known as App Host) and integration server.

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
  | Layout | Read, Edit |

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
The app does not support a proxy server.

### Python Environment
Python 3.6, 3.9, and 3.11 are supported.
Additional package dependencies may exist for each of these packages:
* ldap3>=2.0.0
* pycryptodome>=3.20.0
* resilient_circuits>=50.0.0

---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **ldap_server** | Yes | `xxx.xxx.xxx.xxx` | *Ip address of the LDAP Server* |
| **ldap_port** | Yes | `389` | *Port to use to connect to LDAP server* |
| **ldap_use_ssl** | Yes | `False` | *Boolean value to use ssl or not* |
| **ldap_auth** | Yes | `SIMPLE` | *Type of authentication to use* |
| **ldap_user_dn** | Yes | `CN=Username,CN=Users,DC=example,DC=com` | *DN of LDAP account* |
| **ldap_password** | Yes | `password` | *Password for the LDAP account* |
| **ldap_user_ntlm** | Yes | `Domain\User` | *Windows NTLM user* |
| **ldap_is_active_directory** | Yes | `False` | *Boolean value to determine if LDAP server is on an active directory server* |
| **ldap_connect_timeout** | Yes | `10` | *Timeout in seconds* |

#### 2.0.0 Changes
Starting in version 2.0.0, more than one LDAP instance can be configured for SOAR case data synchronization. For enterprises with only one LDAP instance, your app.config file will continue to define the LDAP instance under the `[fn_ldap_utilities]` section header.

For enterprises with more than one LDAP instance, each instance will have it;s own section header, such as `[fn_ldap_utilities:Domain1]` where `Domain1` represents any label helpful to define your LDAP environment.

Be aware that modifications to custom workflows will be needed to correctly pass this label through the `ldap_domain_name` function input field if the LDAP server/servers in the app.config have labels.

If you have existing custom workflows, see [Creating workflows when server/servers in app.config are labeled](#creating-workflows-when-serverservers-in-appconfig-are-labeled) for more information about changing them to reference the `ldap_domain_name` function input field.

## Using the example functions
Two incident fields have been added, `ldap_domain_name` and `ldap_base_dn`. If these are added to a case and given values then those values will be used when a rule is run that uses those fields. If a rule is run and the user enters a value that is different from the ones given in the incident then the user entered value will be used for that rule.

---

## Function - LDAP Utilities: Add
Add users, groups, organizational units to LDAP

 ![screenshot: fn-ldap-utilities-add ](./doc/screenshots/add.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `ldap_attribute_name_values` | `text` | No | `"attribute1": "value1", "attribute2": "value2"` | Comma separated name value pairs, each key and value must be surrounded by quotation marks like the example |
| `ldap_dn` | `text` | Yes | `CN=user1,CN=Users,DC=dev,DC=example,DC=com` | Distinguished Name of entry you want to access. |
| `ldap_domain_name` | `text` | No | `-` | The label of the LDAP server to use from the app.config |
| `ldap_multiple_group_dn` | `text` | Yes | `"['dn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']"` | List (represented as a string) of each DN of the related groups, each value in the list must have quotes around it like the example |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "description": "success",
    "dn": "",
    "message": "",
    "referrals": null,
    "result": 0,
    "type": "addResponse"
  },
  "inputs": {
    "ldap_attribute_name_values": "\"objectClass\": [\"top\",\"person\",\"organizationalPerson\",\"user\"], \"name\": \"Gary\", \"mail\": \"gary1@dev.co3sys.com\", \"sAMAccountName\": \"gary1\"",
    "ldap_dn": "cn=Gary1,cn=Users,dc=dev,dc=co3sys,dc=com",
    "ldap_domain_name": "Domain2",
    "ldap_multiple_group_dn": "[]"
  },
  "metrics": {
    "execution_time_ms": 545,
    "host": "local",
    "package": "fn-ldap-utilities",
    "package_version": "2.1.1",
    "timestamp": "2023-08-09 09:54:11",
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
# If the incident field ldap_domain_name contains a value then set ldap_domain_name to that value
if incident.properties.ldap_domain_name:
  inputs.ldap_domain_name = incident.properties.ldap_domain_name
# If a value is given by the user field then set ldap_domain_name to that value
if getattr(playbook.inputs, "ldap_domain_name", None):
  inputs.ldap_domain_name = getattr(playbook.inputs, "ldap_domain_name", None)

inputs.ldap_dn = getattr(playbook.inputs, "ldap_user_info", None)
inputs.ldap_multiple_group_dn = getattr(playbook.inputs, "ldap_groups", None) if getattr(playbook.inputs, "ldap_groups", None) else '[]'
inputs.ldap_attribute_name_values = getattr(playbook.inputs, "ldap_attribute_name_values", None)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.add_results
ldap_dn = results.get('inputs', {}).get('ldap_dn')
if results.get("success"):
  incident.addNote(f"LDAP Add operation successful for: {ldap_dn}")
else:
  incident.addNote(f"LDAP Add operation unsuccessful for: {ldap_dn}. Reason: {results.get('reason')}")
```

</p>
</details>

---
## Function - LDAP Utilities: Add to Group(s)
A function that allows adding multiple users to multiple groups.

 ![screenshot: fn-ldap-utilities-add-to-groups ](./doc/screenshots/fn-ldap-utilities-add-to-groups.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `ldap_domain_name` | `text` | No | `-` | The label of the LDAP server to use from the app.config |
| `ldap_multiple_group_dn` | `text` | Yes | `"['dn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']"` | List (represented as a string) of each DN of the related groups, each value in the list must have quotes around it like the example |
| `ldap_multiple_user_dn` | `text` | Yes | `"['dn=tom smith,dc=example,dc=com', 'dn=ted smith,dc=example,dc=com']"` | List (represented as a string) of each DN of the users, each value in the list must have quotes around it like the example |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "groups_dn": [
      "CN=Charles-3,CN=Users,DC=dev,DC=co3sys,DC=com"
    ],
    "users_dn": [
      "CN=gerry,CN=Users,DC=dev,DC=co3sys,DC=com"
    ]
  },
  "inputs": {
    "ldap_domain_name": "Domain2",
    "ldap_multiple_group_dn": "[\u0027CN=Charles-3,CN=Users,DC=dev,DC=co3sys,DC=com\u0027]",
    "ldap_multiple_user_dn": "[\u0027CN=gerry,CN=Users,DC=dev,DC=co3sys,DC=com\u0027]"
  },
  "metrics": {
    "execution_time_ms": 1081,
    "host": "local",
    "package": "fn-ldap-utilities",
    "package_version": "2.1.0",
    "timestamp": "2023-03-30 10:57:37",
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
# Both inputs must be a string representation of a List

## Example of multiple entries
# inputs.ldap_multiple_user_dn = "['dn=user1,dc=example,dc=com', 'dn=user2,dc=example,dc=com']"
# inputs.ldap_multiple_group_dn = "['dn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']"

# Both inputs must be a string representation of a List
inputs.ldap_multiple_user_dn = getattr(playbook.inputs, "ldap_multiple_user_dn", None)
inputs.ldap_multiple_group_dn = getattr(playbook.inputs, "ldap_multiple_group_dn", None)

# If the incident field ldap_domain_name contains a value then set ldap_domain_name to that value
if incident.properties.ldap_domain_name:
  inputs.ldap_domain_name = incident.properties.ldap_domain_name
# If a value is given in the rule ldap_domain_name field then set ldap_domain_name to that value
if getattr(playbook.inputs, "ldap_domain_name", None):
  inputs.ldap_domain_name = getattr(playbook.inputs, "ldap_domain_name", None)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.add_groups_results
inputs = results.get('inputs', {})
# If the function is successful in adding the users to said groups, a note is added to the incident
if results.get("success"):
  noteText = f"""<br><i style="color: #979ca3"> LDAP Utilities: Add User(s) to Group(s) <u>complete</u>:</i>
                <b>User(s):</b> {inputs.get('ldap_multiple_user_dn')}
                <b>Group(s):</b> {inputs.get('ldap_multiple_group_dn')}"""

  incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - LDAP Utilities: Remove from Group(s)
A function that allows you to remove multiple from multiple groups.

 ![screenshot: fn-ldap-utilities-remove-from-groups ](./doc/screenshots/fn-ldap-utilities-remove-from-groups.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `ldap_domain_name` | `text` | No | `Domain1` | Name of the LDAP server to use from the app.config |
| `ldap_multiple_group_dn` | `text` | Yes | `['dn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']` | List (represented as a string) of each DN of the related groups, each value in the list must have quotes around it like the example |
| `ldap_multiple_user_dn` | `text` | Yes | `['dn=tom smith,dc=example,dc=com', 'dn=ted smith,dc=example,dc=com']` | List (represented as a string) of each DN of the users, each value in the list must have quotes around it like the example |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "groups_dn": [
      "CN=Charles-3,CN=Users,DC=dev,DC=co3sys,DC=com"
    ],
    "users_dn": [
      "CN=gerry,CN=Users,DC=dev,DC=co3sys,DC=com"
    ]
  },
  "inputs": {
    "ldap_domain_name": "Domain2",
    "ldap_multiple_group_dn": "[\u0027CN=Charles-3,CN=Users,DC=dev,DC=co3sys,DC=com\u0027]",
    "ldap_multiple_user_dn": "[\u0027CN=gerry,CN=Users,DC=dev,DC=co3sys,DC=com\u0027]"
  },
  "metrics": {
    "execution_time_ms": 1093,
    "host": "local",
    "package": "fn-ldap-utilities",
    "package_version": "2.1.0",
    "timestamp": "2023-03-30 10:58:09",
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
# Both inputs must be a string representation of a List

## Example of multiple entries
# inputs.ldap_multiple_user_dn = "['dn=user1,dc=example,dc=com', 'dn=user2,dc=example,dc=com']"
# inputs.ldap_multiple_group_dn = "['dn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']"

# Both inputs must be a string representation of a List
inputs.ldap_multiple_user_dn = getattr(playbook.inputs, "ldap_multiple_user_dn", None)
inputs.ldap_multiple_group_dn = getattr(playbook.inputs, "ldap_multiple_group_dn", None)

# If the incident field ldap_domain_name contains a value then set ldap_domain_name to that value
if incident.properties.ldap_domain_name:
  inputs.ldap_domain_name = incident.properties.ldap_domain_name
# If a value is given in the rule ldap_domain_name field then set ldap_domain_name to that value
if getattr(playbook.inputs, "ldap_domain_name", None):
  inputs.ldap_domain_name = getattr(playbook.inputs, "ldap_domain_name", None)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.remove_groups_results
inputs = results.get("inputs", {})
# If the function is successful in removing the users from said groups, a note is added to the incident
if results.get("success"):
  if not results.get("content", {}).get("users_dn"):
    noteText = """<br><i style="color: #979ca3"> LDAP Utilities: Remove User from Group(s) <u>complete</u>:</i>
                  <b>No users found. Check inputted user DN's</b>"""
  else:
    noteText = f"""<br><i style="color: #979ca3"> LDAP Utilities: Remove User from Group(s) <u>complete</u>:</i>
                  <b>User(s):</b> {inputs.get('ldap_multiple_user_dn')}
                  <b>Group(s):</b> {inputs.get('ldap_multiple_group_dn')}"""

  incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - LDAP Utilities: Search
SOAR Function to do a search or query against an LDAP server.

 ![screenshot: fn-ldap-utilities-search ](./doc/screenshots/fn-ldap-utilities-search.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `ldap_domain_name` | `text` | No | `Domain1` | Name of the LDAP server to use from the app.config |
| `ldap_search_attributes` | `text` | No | `uid,cn,sn,mail,telephoneNumber or *` | A single attribute or a list of attributes to be returned by the LDAP search |
| `ldap_search_base` | `text` | Yes | `DC=dev,DC=example,DC=com` | The base of the LDAP search request. |
| `ldap_search_filter` | `textarea` | Yes | `(&(objectClass=person)(mail=*%ldap_param%))` | The filter of the LDAP search request, must be in the correct filter format for LDAP |
| `ldap_search_param` | `text` | No | `user1@example.com` | Parameter used in search filter |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "entries": [
      {
        "accountExpires": "9999-12-31 23:59:59.999999+00:00",
        "badPasswordTime": "2023-08-09 12:37:03.680271+00:00",
        "badPwdCount": 0,
        "cn": "Billy Bremner",
        "codePage": 0,
        "countryCode": 0,
        "dSCorePropagationData": [
          "2023-08-10 14:22:07+00:00",
          "2023-08-10 14:19:35+00:00",
          "1601-01-01 00:04:17+00:00"
        ],
        "displayName": "Billy Bremner",
        "distinguishedName": "CN=Billy Bremner,CN=Users,DC=dev,DC=co3sys,DC=com",
        "dn": "CN=Billy Bremner,CN=Users,DC=dev,DC=co3sys,DC=com",
        "givenName": "Billy",
        "instanceType": 4,
        "lastLogoff": "1601-01-01 00:00:00+00:00",
        "lastLogon": "2023-08-10 14:37:11.119774+00:00",
        "lastLogonTimestamp": "2023-08-10 14:37:04.349319+00:00",
        "lockoutTime": "1601-01-01 00:00:00+00:00",
        "logonCount": 15,
        "mail": "bbremner@example.com",
        "memberOf": [
          "CN=DermotGroup2,DC=dev,DC=co3sys,DC=com",
          "CN=DermotGroup,CN=Users,DC=dev,DC=co3sys,DC=com"
        ],
        "name": "Billy Bremner",
        "objectCategory": "CN=Person,CN=Schema,CN=Configuration,DC=dev,DC=co3sys,DC=com",
        "objectClass": [
          "top",
          "person",
          "organizationalPerson",
          "user"
        ],
        "objectGUID": "{af8b16cd-968a-448b-92fd-6b281d07ffde}",
        "objectSid": "S-1-5-21-1927197486-2714598076-3523470783-3118",
        "primaryGroupID": 513,
        "pwdLastSet": "2023-08-10 14:38:59.250429+00:00",
        "sAMAccountName": "bbremner",
        "sAMAccountType": 805306368,
        "sn": "Bremner",
        "uSNChanged": 1139323,
        "uSNCreated": 803064,
        "userAccountControl": 66048,
        "userPassword": [
          "abcpassword"
        ],
        "userPrincipalName": "bbremner@dev.co3sys.com",
        "whenChanged": "2023-08-10 14:38:59+00:00",
        "whenCreated": "2020-05-20 08:47:45+00:00"
      }
    ]
  },
  "inputs": {
    "ldap_domain_name": "Domain2",
    "ldap_search_base": "DC=dev,DC=co3sys,DC=com",
    "ldap_search_filter": "(\u0026(mail=%ldap_param%))",
    "ldap_search_param": "bbremner@example.com"
  },
  "metrics": {
    "execution_time_ms": 1230,
    "host": "local",
    "package": "fn-ldap-utilities",
    "package_version": "2.1.2",
    "timestamp": "2023-08-10 10:39:53",
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
# Set the ldap_search_base and ldap_search_filter
# using the ldap_param wildcard then get the email
# address the user you want to toggle access for from the artifact's value
inputs.ldap_search_filter = "(&(mail=%ldap_param%))"
inputs.ldap_search_param =  artifact.value

# If the incident field ldap_base_dn contains a value then set ldap_search_base to that value
if incident.properties.ldap_base_dn:
  inputs.ldap_search_base = incident.properties.ldap_base_dn
# If a value is given in the rule ldap_search_base field then set ldap_search_base to that value
if getattr(playbook.inputs, "ldap_search_base", None):
  inputs.ldap_search_base = getattr(playbook.inputs, "ldap_search_base", None)

# If the incident field ldap_domain_name contains a value then set ldap_domain_name to that value
if incident.properties.ldap_domain_name:
  inputs.ldap_domain_name = incident.properties.ldap_domain_name
# If a value is given in the rule ldap_domain_name field then set ldap_domain_name to that value
if getattr(playbook.inputs, "ldap_domain_name", None):
  inputs.ldap_domain_name = getattr(playbook.inputs, "ldap_domain_name", None)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.search_results
ENTRY_TO_DATATABLE_MAP = {
  "uid": "uid",
  "cn": "fullname",
  "sn": "surname",
  "mail": "email_address",
  "telephoneNumber": "telephone_number"
}

# Processing if the function is a success
if results.get("success"):
  for entry in results.get("content", {}).get("entries"):
    row = incident.addRow("ldap_query_results") # Add Row
    for k in ENTRY_TO_DATATABLE_MAP:
      # If Handle for Active Directory else Handle for OpenLdap
      row[ENTRY_TO_DATATABLE_MAP[k]] = "N/A" if not entry.get(k) else ",".join(entry.get(k)) if isinstance(entry[k], list) else entry.get(k)
```

</p>
</details>

---
## Function - LDAP Utilities: Set Password
A function that allows you to set a new password for an LDAP entry given the entry's DN. To use this you have to connect to the LDAP server using ssl.

 ![screenshot: fn-ldap-utilities-set-password ](./doc/screenshots/fn-ldap-utilities-set-password.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `ldap_dn` | `text` | Yes | `CN=user1,CN=Users,DC=dev,DC=example,DC=com` | Distinguished Name of entry you want to access. |
| `ldap_domain_name` | `text` | No | `-` | The label of the LDAP server to use from the app.config |
| `ldap_new_auto_password_len` | `number` | No | `12` | Length of password to generate. |
| `ldap_new_password` | `text` | No | `-` | The new password you want to set for the entry. |
| `ldap_return_new_password` | `boolean` | No | `-` | Either to return the new password or not. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "ldap_new_password": null,
    "user_dn": "CN=Billy Bremner,CN=Users,DC=dev,DC=co3sys,DC=com"
  },
  "inputs": {
    "ldap_dn": "CN=Billy Bremner,CN=Users,DC=dev,DC=co3sys,DC=com",
    "ldap_domain_name": "Domain2",
    "ldap_new_password": "abcpassword",
    "ldap_return_new_password": false
  },
  "metrics": {
    "execution_time_ms": 10756,
    "host": "local",
    "package": "fn-ldap-utilities",
    "package_version": "2.1.2",
    "timestamp": "2023-08-10 10:39:08",
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
results = playbook.functions.results.search_results
# Once the LDAP Utilities: Search completes, get the DN of the first entry
# which will be the DN of the account you want to set a Set a New Password for
inputs.ldap_domain_name = results.get("inputs", {}).get("ldap_domain_name")
inputs.ldap_dn = results.get("content", {}).get("entries", [])[0]["dn"]
inputs.ldap_new_password = getattr(playbook.inputs, "ldap_user_new_password", None)
pass_len = getattr(playbook.inputs, "ldap_new_auto_password_length", None)
if pass_len:
  inputs.ldap_new_auto_password_len = pass_len
inputs.ldap_return_new_password = getattr(playbook.inputs, "ldap_return_new_password", None)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.pass_results
content = results.get("content", {})
# If the function is successful in changing the users password, a note is added to the incident
if results.get("success"):
  noteText = f"""<br><i style="color: #979ca3"> LDAP MultiDomain Utilities: Set Password workflow <u>complete</u>:</i>
                A New Password has been set for:
                <b>Email:</b> <u style="color: #7fb0ff">{artifact.value}</u>
                <b>DN:</b> '{content.get('user_dn')}'
                <b>New password:</b> '{content.get('ldap_new_password')}'"""

  incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - LDAP Utilities: Toggle Access
A function that allows an LDAP user, with the correct privileges, to enable or disable another account given their DN.

 ![screenshot: fn-ldap-utilities-toggle-access ](./doc/screenshots/fn-ldap-utilities-toggle-access.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `ldap_dn` | `text` | Yes | `CN=user1,CN=Users,DC=dev,DC=example,DC=com` | Distinguished Name of entry you want to access |
| `ldap_domain_name` | `text` | No | `Domain1` | Name of the LDAP server to use from the app.config |
| `ldap_toggle_access` | `select` | Yes | `-` | Either enable or disable the user |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "user_dn": "CN=Billy Bremner,CN=Users,DC=dev,DC=co3sys,DC=com",
    "user_status": "Enable"
  },
  "inputs": {
    "ldap_dn": "CN=Billy Bremner,CN=Users,DC=dev,DC=co3sys,DC=com",
    "ldap_domain_name": "Domain2",
    "ldap_toggle_access": "Enable"
  },
  "metrics": {
    "execution_time_ms": 3714,
    "host": "local",
    "package": "fn-ldap-utilities",
    "package_version": "2.1.2",
    "timestamp": "2023-08-10 10:39:59",
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
results = playbook.functions.results.search_results
# Once the LDAP Utilities: Search completes, get the DN of the first entry
# which will be the DN of the account you want to set a Toggle Access for
inputs.ldap_domain_name = results.get("inputs", {}).get("ldap_domain_name")
inputs.ldap_dn = results.get("content", {}).get("entries", [])[0]["dn"]
inputs.ldap_toggle_access = getattr(playbook.inputs, "ldap_toggle_access", None)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.toggle_results
content = results.get("content", {})
# If the function is successful in updating users access rights, a note is added to the incident
if results.get("success"):
  color = "#45bc27" #green
  if (content.get("user_status") == "Disable"):
    color = "#ff402b" #red

  noteText = f"""<br><i style="color: #979ca3"> LDAP Utilities: Toggle Access workflow <u>complete</u>:</i>
                <b>Email:</b> <u style="color: #7fb0ff">{artifact.value}</u>
                <b>Status:</b> <b style="color: {color}">{content.get('user_status')}</b>
                <b>DN:</b> '{content.get('user_dn')}'"""

  incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - LDAP Utilities: Update
A function that updates the attribute of a DN with a new value.

 ![screenshot: fn-ldap-utilities-update ](./doc/screenshots/fn-ldap-utilities-update.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `ldap_attribute_name` | `text` | Yes | `homePhone` | The name of the LDAP attribute |
| `ldap_attribute_values` | `text` | Yes | `['value1', 'value2', 'value3']` | List (as a string representation) of the new attribute values, each value in the list must have quotes around it like the example |
| `ldap_dn` | `text` | Yes | `CN=user1,CN=Users,DC=dev,DC=example,DC=com` | Distinguished Name of entry you want to access |
| `ldap_domain_name` | `text` | No | `Domain1` | Name of the LDAP server to use from the app.config |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "attribute_name": "homePhone",
    "attribute_values": [
      "2638443927"
    ],
    "user_dn": "CN=Franky,CN=Users,DC=dev,DC=co3sys,DC=com"
  },
  "inputs": {
    "ldap_attribute_name": "homePhone",
    "ldap_attribute_values": "[\u00272638443927\u0027]",
    "ldap_dn": "CN=Franky,CN=Users,DC=dev,DC=co3sys,DC=com",
    "ldap_domain_name": "Domain2"
  },
  "metrics": {
    "execution_time_ms": 1090,
    "host": "local",
    "package": "fn-ldap-utilities",
    "package_version": "2.1.0",
    "timestamp": "2023-03-31 09:32:11",
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
results = playbook.functions.results.search_results
# Once the LDAP Utilities: Search completes, get the DN of the first entry
# which will be the DN of the account you want to update. Then set
# the name of the attribute to update and list the values
inputs.ldap_domain_name = results.get("inputs", {}).get("ldap_domain_name")
inputs.ldap_dn = results.get("content", {}).get("entries", [])[0]["dn"]
inputs.ldap_attribute_name = getattr(playbook.inputs, "ldap_update_attribute_name", None)
inputs.ldap_attribute_values = getattr(playbook.inputs, "ldap_attribute_update_value", None)
# inputs.ldap_attribute_values = "['081111111', '082222222']"
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.update_results
content = results.get("content", {})
# If the function is successful in updating the value of the attribute, a note is added to the incident
if results.get("success"):
  noteText = f"""<br><i style="color: #979ca3"> LDAP Utilities: Update workflow <u>complete</u>:</i>
                An LDAP Attribute has been updated
                <b>Attribute:</b> {content.get('attribute_name')}
                <b>New Value(s):</b> {content.get('attribute_values')}
                <b>DN:</b> '{content.get('user_dn')}'"""

  incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---

## Script - No search results


**Object:** artifact

<details><summary>Script Text:</summary>
<p>

```python
incident.addNote(f"No entries found for {artifact.value}")
```

</p>
</details>

---

## Playbooks
| Playbook Name | Description | Activation Type | Object | Status | Condition | 
| ------------- | ----------- | --------------- | ------ | ------ | --------- | 
| Example: LDAP Utilities: Add (PB) | Add users, groups, organizational units to LDAP | Manual | incident | `enabled` | `-` | 
| Example: LDAP Utilities: Add User(s) to Group(s) (PB) | add multiple users to multiple groups | Manual | artifact | `enabled` | `artifact.type equals String` | 
| Example: LDAP Utilities: Remove User(s) from Group(s) (PB) | remove multiple users from a group | Manual | artifact | `enabled` | `artifact.type equals String` | 
| Example: LDAP Utilities: Search (PB) | runs a person query against an LDAP server using the person's email address | Manual | artifact | `enabled` | `artifact.type equals Email Recipient OR artifact.type equals Email Sender OR artifact.type equals String` | 
| Example: LDAP Utilities: Set Password (PB) | searches for a user using their email address, gets their DN and sets a new password for that user | Manual | artifact | `enabled` | `artifact.type equals Email Recipient OR artifact.type equals Email Sender OR artifact.type equals String` | 
| Example: LDAP Utilities: Toggle Access (PB) | enable/disable an Active Directory user account | Manual | artifact | `enabled` | `artifact.type equals Email Recipient OR artifact.type equals Email Sender OR artifact.type equals String` | 
| Example: LDAP Utilities: Update (PB) | updates the value of a DN's attribute with the given value(s) | Manual | artifact | `enabled` | `artifact.type equals Email Recipient OR artifact.type equals Email Sender OR artifact.type equals String` | 

---



## Data Table - LDAP Query results

 ![screenshot: dt-ldap-query-results](./doc/screenshots/dt-ldap-query-results.png)

#### API Name:
ldap_query_results

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Email address | `email_address` | `text` | - |
| Fullname | `fullname` | `text` | - |
| Surname | `surname` | `text` | - |
| Telephone Number | `telephone_number` | `text` | - |
| UID | `uid` | `text` | - |

---

## Custom Fields
| Label | API Access Name | Type | Prefix | Placeholder | Tooltip |
| ----- | --------------- | ---- | ------ | ----------- | ------- |
| LDAP Base DN | `ldap_base_dn` | `text` | `properties` | DC=example,DC=com | - |
| LDAP Domain Name | `ldap_domain_name` | `text` | `properties` | - | Domain name label given to the LDAP server you wish to use |

---

## How to configure to use a single LDAP Server
To use only a single server there are two ways this can be configured
1. User the configuration used in LDAP Utilities versions prior to v2.0.0
```
[fn_ldap_utilities]
# Ip address of the LDAP Server
ldap_server=xxx.xxx.xxx.xxx
# Use port 636 if using ssl or port 389 if not using ssl
ldap_port=389
ldap_use_ssl=False
# Can be ANONYMOUS, SIMPLE or NTLM
ldap_auth=SIMPLE
# DN of LDAP account
ldap_user_dn=CN=Username,CN=Users,DC=example,DC=com
# Password for the LDAP account
ldap_password=password
# Windows NTLM user
ldap_user_ntlm=Domain\\User
ldap_is_active_directory=False
ldap_connect_timeout=10
```
2. Either keep the label, Domain1, or change it (The label does not matter when only one server is configured)
```
[fn_ldap_utilities:Domain1]
# Ip address of the LDAP Server
ldap_server=xxx.xxx.xxx.xxx
# Use port 636 if using ssl or port 389 if not using ssl
ldap_port=389
ldap_use_ssl=False
# Can be ANONYMOUS, SIMPLE or NTLM
ldap_auth=SIMPLE
# DN of LDAP account
ldap_user_dn=CN=Username,CN=Users,DC=example,DC=com
# Password for the LDAP account
ldap_password=password
# Windows NTLM user
ldap_user_ntlm=Domain\\User
ldap_is_active_directory=False
ldap_connect_timeout=10
```

## Creating playbooks when server/servers in app.config are labeled
The function input field `ldap_domain_name` is required when LDAP server/servers in the app.config are labeled. In the example playbook input scripts the input field `ldap_domain_name` is defined the following way,
```python
# If the incident field ldap_domain_name contains a value then set ldap_domain_name to that value
if incident.properties.ldap_domain_name:
  inputs.ldap_domain_name = incident.properties.ldap_domain_name
# If a value is given in the playbook ldap_domain_name activation field then set ldap_domain_name to that value
if playbook.input.ldap_domain_name:
  inputs.ldap_domain_name = playbook.input.ldap_domain_name
```

## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.
 
### For Support
This is a IBM Community provided app. Please search the Community [ibm.biz/soarcommunity](https://ibm.biz/soarcommunity) for assistance.
