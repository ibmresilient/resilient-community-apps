# Cisco Secure Endpoint


## Table of Contents
- [Cisco Secure Endpoint](#cisco-secure-endpoint)
  - [Table of Contents](#table-of-contents)
  - [Release Notes](#release-notes)
  - [Overview](#overview)
    - [Key Features](#key-features)
  - [Requirements](#requirements)
    - [SOAR platform](#soar-platform)
    - [Cloud Pak for Security](#cloud-pak-for-security)
    - [Proxy Server](#proxy-server)
    - [Python Environment](#python-environment)
    - [Development Version](#development-version)
      - [Prerequisites](#prerequisites)
      - [Permissions](#permissions)
  - [Installation](#installation)
    - [Install](#install)
    - [App Configuration](#app-configuration)
  - [Function - AMP: Computer Isolation](#function---amp-computer-isolation)
  - [Function - AMP: Delete File from List](#function---amp-delete-file-from-list)
  - [Function - AMP: Get Activity](#function---amp-get-activity)
  - [Function - AMP: Get Computer](#function---amp-get-computer)
  - [Function - AMP: Get Computer Trajectory](#function---amp-get-computer-trajectory)
  - [Function - AMP: Get Computers](#function---amp-get-computers)
  - [Function - AMP: Get Event Types](#function---amp-get-event-types)
  - [Function - AMP: Get Events](#function---amp-get-events)
  - [Function - AMP: Get File Lists](#function---amp-get-file-lists)
  - [Function - AMP: Get Files from List](#function---amp-get-files-from-list)
  - [Function - AMP: Get Groups](#function---amp-get-groups)
  - [Function - AMP: Move Computer](#function---amp-move-computer)
  - [Function - AMP: Set File in List](#function---amp-set-file-in-list)
  - [Script - scr\_amp\_add\_artifact\_from\_activity](#script---scr_amp_add_artifact_from_activity)
  - [Script - scr\_amp\_add\_artifact\_from\_event](#script---scr_amp_add_artifact_from_event)
  - [Script - scr\_amp\_add\_artifact\_from\_trajectory](#script---scr_amp_add_artifact_from_trajectory)
  - [Playbooks](#playbooks)
  - [Custom Layouts](#custom-layouts)
  - [Data Table - Cisco AMP activity](#data-table---cisco-amp-activity)
      - [API Name:](#api-name)
      - [Columns:](#columns)
  - [Data Table - Cisco AMP computer trajectory](#data-table---cisco-amp-computer-trajectory)
      - [API Name:](#api-name-1)
      - [Columns:](#columns-1)
  - [Data Table - Cisco AMP computers](#data-table---cisco-amp-computers)
      - [API Name:](#api-name-2)
      - [Columns:](#columns-2)
  - [Data Table - Cisco AMP event types](#data-table---cisco-amp-event-types)
      - [API Name:](#api-name-3)
      - [Columns:](#columns-3)
  - [Data Table - Cisco AMP events](#data-table---cisco-amp-events)
      - [API Name:](#api-name-4)
      - [Columns:](#columns-4)
  - [Data Table - Cisco AMP file list files](#data-table---cisco-amp-file-list-files)
      - [API Name:](#api-name-5)
      - [Columns:](#columns-5)
  - [Data Table - Cisco AMP groups](#data-table---cisco-amp-groups)
      - [API Name:](#api-name-6)
      - [Columns:](#columns-6)
  - [Data Table - Cisco AMP Simple Custom Detections  file lists](#data-table---cisco-amp-simple-custom-detections--file-lists)
      - [API Name:](#api-name-7)
      - [Columns:](#columns-7)
  - [Rules](#rules)
  - [Troubleshooting \& Support](#troubleshooting--support)
    - [For Support](#for-support)

---

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release
  notes of a previous release
-->
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.0.0 | 04/2019 | Initial Release |
| 1.0.1 | 05/2020 | Support added for App Host |
| 1.0.2 | 11/2023 | Convert Workflow/Script to Python3 |
| 1.1.0 | 06/2024 | Add function for endpoint isolation. Bug fixes |

---

## Overview
<!--
  Provide a high-level description of the function itself and its remote software or application.
  The text below is parsed from the "description" and "long_description" attributes in the setup.py file
-->
**IBM SOAR Components for Cisco Secure Endpoint**

 ![screenshot: main](./doc/screenshots/main.png)

The Cisco Secure Endpoint (formerly, Cisco AMP for Endpoints) integration with the SOAR platform allows for the querying and updating of an AMP for Endpoints deployment. The integration includes functions that return results which show security events for endpoints in the deployment. The returned results can be used to make customized updates to the SOAR platform, such as updating incidents, artifacts, data tables and so on. The integration can also be used to make changes to a deployment including adding or removing a hash to a blacklist and moving an endpoint to a different group.

### Key Features
<!--
  List the Key Features of the Integration
-->
* Retrieve list of all computers with agents deployed on them, in a Cisco Secure Endpoint environment.
* Get information about a specific computer by guid
* Get list of all activities associated with a particular computer, search by guid.
* Search all computers for any events or activities associated with a file or network operation

---

## Requirements
<!--
  List any Requirements
-->
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, Edge Gateway (also known as App Host) and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `50.0.9097`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `50.0.9097`.
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
* IBM Cloud Pak for Security >= `1.10`.
* Cloud Pak is configured with an Edge Gateway.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

The following Cloud Pak guides provide additional information:
* _Edge Gateway Deployment Guide_ or _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. From the Table of Contents, select Case Management and Orchestration & Automation > **Orchestration and Automation Apps**.
* _System Administrator Guide_: provides information to install, configure, and deploy apps. From the IBM Cloud Pak for Security IBM Documentation table of contents, select Case Management and Orchestration & Automation > **System administrator**.

These guides are available on the IBM Documentation website at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs). From this web page, select your IBM Cloud Pak for Security version. From the version-specific IBM Documentation page, select Case Management and Orchestration & Automation.

### Proxy Server
The app **does not** support a proxy server.

### Python Environment
Python 3.9 and 3.11 are officially supported. When deployed as an app, the app runs on Python 3.11.
Additional package dependencies may exist for each of these packages:
* resilient_circuits>=51.0.0

### Development Version

This app has been implemented using:
| Product Name | API URL | API Version |
| ------------ | ------- | ----------- |
| Cisco Secure Endpoint | https://api.amp.cisco.com/ | v1 |

#### Prerequisites
<!--
List any prerequisites that are needed to use with this endpoint solution. Remove any section that is unnecessary.
-->
* An active Cisco Secure Endpoint account is required

#### Permissions
<!--
List any user permissions that are needed to use this endpoint. For example, list the API key permissions.
-->
* Client ID key and API key token with read/write permissions for Cisco Secure Endpoint are required


---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **api_token** | Yes | `<api token>` | Cisco Secure Endpoint API Token  |
| **api_version** | Yes | `v1` | Version of Cisco Secure Endpoint API to use. v0 and v1 are currently supported |
| **base_url** | Yes | `https://api.amp.cisco.com/` | Base url for Cisco Secure Endpoint API |
| **client_id** | Yes | `<client id>` | Client ID for accessing Cisco Secure Endpoint API |
| **max_retries** | Yes | `3` | Number of times to retry API requests if needed |



 ---

## Function - AMP: Computer Isolation
Isolate/de-isolate a computer by connector guid.

 ![screenshot: fn-amp-computer-isolation ](./doc/screenshots/fn-amp-computer-isolation.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_computer_isolation` | `select` | Yes | `-` | Indicate whether to isolate or de-isolate a computer or refresh isolation status |
| `amp_conn_guid` | `text` | No | `-` | Connector guid. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "response": {
      "data": {
        "available": true,
        "comment": null,
        "isolated_by": "Test User",
        "status": "isolated",
        "unlock_code": "abcdefg"
      },
      "metadata": {
        "links": {
          "self": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-0000-b1b1-bcc5-abcdefg1234/isolation"
        }
      },
      "version": "v1.2.0"
    }
  },
  "inputs": {
    "amp_comment": null,
    "amp_computer_isolation": "De-isolate",
    "amp_conn_guid": "aaaaaaaa-0000-b1b1-bcc5-abcdefg1234"
  },
  "metrics": {
    "execution_time_ms": 1287,
    "host": "my.app.host",
    "package": "fn-cisco-amp4ep",
    "package_version": "1.0.3",
    "timestamp": "2024-05-29 16:31:54",
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
inputs.amp_conn_guid = row.connector_guid
inputs.amp_computer_isolation = playbook.inputs.amp_computer_isolation
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.isolation_results

if not results.success:
  incident.addNote(f"<b>Cisco AMP for Endpoints: Computer Isolation (PB):</b> Unable to change isolation status of computer: {results.reason}")
else:
  content = results.get("content", {})
  if content:
    response = content.get("response", None)
    incident.addNote(f"<b>Cisco AMP for Endpoints: Computer Isolation (PB)</b> Response {response}")
    row.isolation_status = response.get("data", {}).get("status")
    
```

</p>
</details>

---
## Function - AMP: Delete File from List
Delete a SHA-256 from a file list by file_list_guid.

 ![screenshot: fn-amp-delete-file-from-list ](./doc/screenshots/fn-amp-delete-file-from-list.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_file_list_guid` | `text` | No | `-` | File list guid value. |
| `amp_file_sha256` | `text` | No | `-` | File sha256 value. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "input_params": {
    "file_list_guid": "aaaaaaaa-bbbb-1111-2222-cccccccccccc",
    "file_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  },
  "query_execution_time": "2024-05-31 16:12:46",
  "response": {
    "data": {},
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/file_lists/aaaaaaaa-bbbb-1111-2222-ccccccccccccd/files/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
      }
    },
    "version": "v1.2.0"
  }
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.amp_file_list_guid = row.guid
inputs.amp_file_sha256 = row.sha256

```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
##  Cisco AMP for endpoints - fn_amp_delete_file_lists script ##
#  fn_amp_delete_computer_trajectory  -  Event type list
# Example result:
"""
Result:    {
             "input_params": {"file_list_guid": "e773a9eb-296c-40df-98d8-bed46322589d",
                       "file_sha256": "8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284"}
             "response": {u'version': u'v1.2.0',
                          u'data': {},
                          u'metadata': {u'links': {
                                            u'self': u'https://api.amp.cisco.com/v1/file_lists/e773a9eb-296c-40df-98d8-bed46322589d/files/8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284'}
                                       }
                          },
              "delete_execution_time": "2018-08-09 11:56:02"
            }

"""
#  Globals
# List of fields in datatable fn_amp_get_file_lists script
DATA_TBL_FIELDS = ["delete_execution_time", "status"]

# Processing
response = results.get("response")

if response is not None:
    noteText = "Cisco AMP for Endpoints Integration: Successfully deleted file with sha256 value <b>{0}</b> " \
               "from SCD list guid <b>{1}</b> for SOAR function <b>{2}</b>."\
        .format(row.sha256, row.guid, "fn_amp_delete_file_list_files")
else:
  noteText = "Cisco AMP Integration: Delete unsuccessful for file with sha256 value <b>{0}</b> " \
               "from SCD list guid <b>{1}</b> for SOAR function <b>{2}</b>."\
        .format(row.sha256, row.guid, "fn_amp_delete_file_list_files")

incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - AMP: Get Activity
Returns list of computers from search of Cisco AMP environment for any events or activities associated with a file or network operation.

 ![screenshot: fn-amp-get-activity ](./doc/screenshots/fn-amp-get-activity.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_limit` | `number` | No | `-` | The results limit. Max value 500. Note: there is also a global limit  for the integration. |
| `amp_offset` | `number` | No | `-` | Offset to start query from. |
| `amp_q` | `text` | No | `-` | Query string can be any of type: IPv4 address, a SHA256, a filename, a URL fragment. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "input_params": {
    "limit": null,
    "offset": null,
    "q": "0.0.0.0"
  },
  "query_execution_time": "2024-06-03 16:34:53",
  "response": {
    "data": [
      {
        "active": true,
        "connector_guid": "aaaaaaa-1111-bbbb-cccc-000000000000",
        "hostname": "Demo_Zbot",
        "links": {
          "computer": "https://api.amp.cisco.com/v1/computers/aaaaaaa-1111-bbbb-cccc-000000000000",
          "group": "https://api.amp.cisco.com/v1/groups/aaaaaaa-1111-bbbb-cccc-000000000000",
          "trajectory": "https://api.amp.cisco.com/v1/computers/aaaaaaa-1111-bbbb-cccc-000000000000/trajectory?q=0.0.0.0"
        },
        "windows_processor_id": "7f42*******e63019"
      },
      {
        "active": true,
        "connector_guid": "aaaaaaa-1111-bbbb-cccc-000000000000",
        "hostname": "Demo_Stabuniq",
        "links": {
          "computer": "https://api.amp.cisco.com/v1/computers/aaaaaaa-1111-bbbb-cccc-000000000000",
          "group": "https://api.amp.cisco.com/v1/groups/aaaaaaa-1111-bbbb-cccc-000000000000",
          "trajectory": "https://api.amp.cisco.com/v1/computers/aaaaaaa-1111-bbbb-cccc-000000000000/trajectory?q=0.0.0.0"
        },
        "windows_processor_id": "ba356d0fe198472"
      },
      {
        "active": true,
        "connector_guid": "aaaaaaa-1111-bbbb-cccc-000000000000",
        "hostname": "Demo_Tinba",
        "links": {
          "computer": "https://api.amp.cisco.com/v1/computers/aaaaaaa-1111-bbbb-cccc-000000000000",
          "group": "https://api.amp.cisco.com/v1/groups/aaaaaaa-1111-bbbb-cccc-000000000000",
          "trajectory": "https://api.amp.cisco.com/v1/computers/aaaaaaa-1111-bbbb-cccc-000000000000/trajectory?q=0.0.0.0"
        },
        "windows_processor_id": "00000000000"
      },
      {
        "active": true,
        "connector_guid": "aaaaaaa-1111-bbbb-cccc-000000000000",
        "hostname": "Demo_Low_Prev_Retro",
        "links": {
          "computer": "https://api.amp.cisco.com/v1/computers/aaaaaaa-1111-bbbb-cccc-000000000000",
          "group": "https://api.amp.cisco.com/v1/groups/aaaaaaa-1111-bbbb-cccc-000000000000",
          "trajectory": "https://api.amp.cisco.com/v1/computers/aaaaaaa-1111-bbbb-cccc-000000000000/trajectory?q=0.0.0.0"
        },
        "windows_processor_id": "111111111111"
      }
    ],
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/computers/activity?q=0.0.0.0"
      },
      "results": {
        "current_item_count": 4,
        "index": 0,
        "items_per_page": 500,
        "total": 4
      }
    },
    "version": "v1.2.0"
  }
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.amp_q = artifact.value
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
##  Cisco AMP for endpoints - fn_amp_get_activity script ##
#  fn_amp_get_activity  -  Event type list
# Example result:
"""
Result: {
          "input_params": {"q": "wsymqyv90.exe", "limit": null, "offset": null},
          "response": {
            "version": "v1.2.0",
            "data": [
              {
                "active": true,
                "hostname": "Demo_Upatre",
                "connector_guid": "76edc092-9e9f-42d4-a2b5-77c094efe348",
                "links": {
                  "trajectory": "https://api.amp.cisco.com/v1/computers/76edc092-9e9f-42d4-a2b5-77c094efe348/trajectory?q=wsymqyv90.exe",
                  "computer": "https://api.amp.cisco.com/v1/computers/76edc092-9e9f-42d4-a2b5-77c094efe348",
                  "group": "https://api.amp.cisco.com/v1/groups/f31bb1cf-c986-4a56-a259-5acd56f7639e"
                }
              }
            ],
            "metadata": {
              "results": {
                "index": 0,
                "total": 1,
                "items_per_page": 500,
                "current_item_count": 1
              },
              "links": {
                "self": "https://api.amp.cisco.com/v1/computers/activity?q=wsymqyv90.exe"
              }
            }
          },
          "query_execution_time": "2018-10-18 16:42:11",
          "query": "wsymqyv90.exe",
        }
}
"""
#  Globals
# List of fields in datatable fn_amp_get_activity script
DATA_TBL_FIELDS = ["query_execution_time", "query", "active", "hostname", "connector_guid"]

# Processing
response = results.response
query_execution_time = results.query_execution_time
query =  results.input_params["q"]
if response is not None:
    r = response["metadata"]["results"]
    noteText = "Cisco AMP for Endpoints Integration: There were <b>{0}</b> results returned out of a total of <b>{1}</b> for query string <b>{2}</b> " \
               "for Resilient function <b>{3}</b>.".format(len(response["data"]), r["total"], query ,"fn_amp_get_activity")
    for data in response["data"]:
        newrow = incident.addRow("amp_activity")
        newrow.query_execution_time = query_execution_time
        newrow.query = query
        for f in DATA_TBL_FIELDS:
            if f == "query" or f == "query_execution_time":
                continue
            newrow[f] = data[f]
else:
    noteText += "Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for SOAR function <b>{0}</b>".format("fn_amp_get_activity")
incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - AMP: Get Computer
Returns information on a  computer with an agent deployed on them by connector guid.

 ![screenshot: fn-amp-get-computer ](./doc/screenshots/fn-amp-get-computer.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_conn_guid` | `text` | No | `-` | Connector guid. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "input_params": {
    "conn_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc"
  },
  "query_execution_time": "2024-05-31 16:13:53",
  "response": {
    "data": {
      "active": true,
      "connector_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
      "connector_version": "8.4.0.30201",
      "demo": true,
      "external_ip": "238.190.21.1",
      "faults": [],
      "flag": false,
      "group_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
      "groups": [
        {
          "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "name": "Protect"
        }
      ],
      "hostname": "Demo_WannaCry_Ransomware",
      "id": 71440046,
      "install_date": "2024-04-29T00:10:43Z",
      "internal_ips": [
        "222.222.222.245"
      ],
      "is_compromised": true,
      "isolation": {
        "available": true,
        "status": "not_isolated"
      },
      "last_seen": "2024-05-29T00:10:43Z",
      "links": {
        "computer": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc",
        "group": "https://api.amp.cisco.com/v1/groups/aaaaaaaa-1111-2222-bbbb-cccccccccccc",
        "trajectory": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc/trajectory"
      },
      "network_addresses": [
        {
          "ip": "226.249.214.245",
          "mac": "1e:c0:c8:7e:bf:07"
        }
      ],
      "operating_system": "Windows 10 (Build 19044.1466)",
      "orbital": {
        "status": "not_enabled"
      },
      "os_type": "WinOs",
      "os_version": "10.0.10000.4466",
      "policy": {
        "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
        "name": "Protect"
      },
      "risk_score": 100,
      "supports": {
        "device_trajectory": true,
        "events": true,
        "move_to_group": true,
        "orbital": {
          "agent_active": false,
          "agent_nil_state": false,
          "agent_supported": true,
          "is_supported": true,
          "min_supported_agent_version": "7.1.5.11111",
          "min_supported_os_version": "10.0.11111",
          "os_supported": true,
          "policy_supported": false
        },
        "request_snapshot": true,
        "scan": true
      },
      "windows_processor_id": "abcdefg1234567"
    },
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
      }
    },
    "version": "v1.2.0"
  }
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.amp_conn_guid = row.connector_guid
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
##  Cisco AMP for endpoints - fn_amp_get_computer script ##
#  fn_amp_get_computer  -  Event type list
# Example result:
"""
Result: {
                  "input_params": {"conn_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f"},
                  "response": {
                    "version": "v1.2.0",
                    "data": {
                      "operating_system": "Windows 7, SP 1.0",
                      "connector_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f",
                      "links": {
                        "trajectory": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f/trajectory",
                        "computer": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f",
                        "group": "https://api.amp.cisco.com/v1/groups/89663c44-f95e-4ee8-896d-7611744a6e9a"
                      },
                      "policy": {
                        "guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b",
                        "name": "Audit"
                      },
                      "external_ip": "145.1.91.176",
                      "group_guid": "89663c44-f95e-4ee8-896d-7611744a6e9a",
                      "hostname": "Demo_AMP",
                      "install_date": "2018-05-22T16:53:27Z",
                      "network_addresses": [
                        {
                          "ip": "255.240.221.92",
                          "mac": "a0:28:f5:c3:71:d5"
                        }
                      ],
                      "connector_version": "6.0.9.10685",
                      "internal_ips": [
                        "255.240.221.92"
                      ],
                      "faults": [],
                      "active": true,
                      "last_seen": "2018-05-22T16:53:27Z"
                    },
                    "metadata": {
                      "links": {
                        "self": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f"
                      }
                    }
                  },
                  "query_execution_time": "2018-10-22 09:28:25"
}
"""
#  Globals
# List of fields in datatable fn_amp_get_computer script
DATA_TBL_FIELDS = ["query_execution_time", "hostname", "operating_system", "connector_guid", "connector_version", "group_guid",
                   "last_seen", "external_ip", "internal_ips", "install_date", "last_seen", "policy_name"]

# Processing
response = results.get("response")
query_execution_time = results.get("query_execution_time")

if response is not None:
    data = response.get("data", {})
    noteText = "Cisco AMP for Endpoints Integration: Result returned for computer <b>{0}</b> with connector guid " \
               "<b>{1}</b> for SOAR function <b>{2}</b>"\
        .format(data.get("hostname"), data.get("connector_guid"), "fn_amp_get_computer")

    row.query_execution_time = query_execution_time
    for f in DATA_TBL_FIELDS:
        if f == "query_execution_time" or "policy" in f:
            continue
        data_field = data.get(f)
        if isinstance(data_field, str) or len(data_field) == 0:
            row[f] = data_field
        else:
            row[f] = ','.join(data_field)
    policy = data.get("policy")
    if policy is not None:
        row.policy_name = policy.get("name")

else:
    noteText += "Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for SOAR " \
                "function <b>{0}</b>".format("fn_amp_get_computer")

incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - AMP: Get Computer Trajectory
Returns a list of all activities associated with a particular computer by connector guid.

 ![screenshot: fn-amp-get-computer-trajectory ](./doc/screenshots/fn-amp-get-computer-trajectory.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_conn_guid` | `text` | No | `-` | Connector guid. |
| `amp_q` | `text` | No | `-` | Query string can be any of type: IPv4 address, a SHA256, a filename, a URL fragment. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "input_params": {
    "connector_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
    "limit": null,
    "q": null
  },
  "query_execution_time": "2024-05-31 16:13:50",
  "response": {
    "data": {
      "computer": {
        "active": true,
        "connector_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
        "connector_version": "8.4.0.30201",
        "demo": true,
        "external_ip": "238.190.21.1",
        "faults": [],
        "flag": false,
        "group_guid": "5059b918-a96b-4a2b-9b67-445f0ac1a020",
        "groups": [
          {
            "guid": "5059b918-a96b-4a2b-9b67-445f0ac1a020",
            "name": "Protect"
          }
        ],
        "hostname": "Demo_WannaCry_Ransomware",
        "id": 71440046,
        "install_date": "2024-04-29T00:10:43Z",
        "internal_ips": [
          "226.249.214.245"
        ],
        "is_compromised": true,
        "isolation": {
          "available": true,
          "status": "not_isolated"
        },
        "links": {
          "computer": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "group": "https://api.amp.cisco.com/v1/groups/5059b918-a96b-4a2b-9b67-445f0ac1a020",
          "trajectory": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc/trajectory"
        },
        "network_addresses": [
          {
            "ip": "226.249.214.245",
            "mac": "1e:c0:c8:7e:bf:07"
          }
        ],
        "operating_system": "Windows 10 (Build 19044.1466)",
        "orbital": {
          "status": "not_enabled"
        },
        "os_type": "WinOs",
        "os_version": "10.0.19044.1466",
        "policy": {
          "guid": "0280b143-7091-45c4-8502-ab250219d796",
          "name": "Protect"
        },
        "risk_score": 100,
        "supports": {
          "device_trajectory": true,
          "events": true,
          "move_to_group": true,
          "orbital": {
            "agent_active": false,
            "agent_nil_state": false,
            "agent_supported": true,
            "is_supported": true,
            "min_supported_agent_version": "7.1.5.11523",
            "min_supported_os_version": "10.0.16299",
            "os_supported": true,
            "policy_supported": false
          },
          "request_snapshot": true,
          "scan": true
        },
        "windows_processor_id": "4d136b0589a27ef"
      },
      "events": [
        {
          "date": "2024-05-29T20:31:54+00:00",
          "event_type": "Endpoint Isolation Stop Success",
          "event_type_id": 553648204,
          "group_guids": [
            "5059b918-a96b-4a2b-9b67-445f0ac1a020"
          ],
          "id": "1717014714006451188",
          "isolation": {
            "duration": 46
          },
          "timestamp": 1717014714,
          "timestamp_nanoseconds": 0
        },
        {
          "date": "2024-05-29T20:26:22+00:00",
          "event_type": "Endpoint Isolation Start Success",
          "event_type_id": 553648202,
          "group_guids": [
            "5059b918-a96b-4a2b-9b67-445f0ac1a020"
          ],
          "id": "1717014382449028169",
          "timestamp": 1717014382,
          "timestamp_nanoseconds": 0
        },
        {
          "date": "2024-05-29T17:48:52+00:00",
          "event_type": "Endpoint Isolation Stop Success",
          "event_type_id": 553648204,
          "group_guids": [
            "5059b918-a96b-4a2b-9b67-445f0ac1a020"
          ],
          "id": "1717004932523748810",
          "isolation": {
            "duration": 46
          },
          "timestamp": 1717004932,
          "timestamp_nanoseconds": 0
        }
      ]
    },
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc/trajectory"
      }
    },
    "version": "v1.2.0"
  },
  "total": 500
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
response =  workflow.properties.get_computers_results.response
if response.get("data", []):
  inputs.amp_conn_guid = response["data"][0]["connector_guid"]
inputs.amp_q = rule.properties.amp_q
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
##  Cisco AMP for endpoints - fn_amp_get_computer_trajectory script ##
#  fn_amp_get_computer_trajectory  -  Event type list
# Example result:
"""
Result: {
          "input_params": {"connector_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f", "q": null, "limit": null},
          "query_execution_time": "2018-08-09 12:34:15",
          "query": None,
          "connector_guid": None,
          "response": {
            "version": "v1.2.0",
            "data": {
              "computer": {
                "operating_system": "Windows 7, SP 1.0",
                "connector_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f",
                "links": {
                  "trajectory": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f/trajectory",
                  "computer": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f",
                  "group": "https://api.amp.cisco.com/v1/groups/9d55c259-c960-488b-9b2d-06478fa19ee4"
                },
                "external_ip": "145.1.91.176",
                "group_guid": "9d55c259-c960-488b-9b2d-06478fa19ee4",
                "hostname": "Demo_AMP",
                "install_date": "2018-05-22T16:53:27Z",
                "network_addresses": [
                  {
                    "ip": "255.240.221.92",
                    "mac": "a0:28:f5:c3:71:d5"
                  }
                ],
                "connector_version": "6.0.9.10685",
                "internal_ips": [
                  "255.240.221.92"
                ],
                "policy": {
                  "guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b",
                  "name": "Audit"
                },
                "active": true
              },
              "events": [{"timestamp": 1502989429,'
                          "timestamp_nanoseconds": 659151942,'
                          "date": "2017-08-17T17:03:49+00:00",'
                          "event_type": "NFM",'
                          "group_guids": ["b077d6bc-bbdf-42f7-8838-a06053fbd98a"],
                          "network_info": { "dirty_url": "http://www.sanjosemaristas.com/app/index.php?", "remote_ip": "188.120.225.17",
                                            "remote_port": 80, "local_ip": "192.168.1.3", "local_port": 54233,
                                            "nfm": {"direction": "Outgoing connection from", "protocol": "TCP"},
                                            "parent": {"disposition": "Clean",
                                                       "identity": {"sha256": "5ad3c37e6f2b9db3ee8b5aeedc474645de90c66e3d95f8620c48102f1eba4124"}
                                            }
                          }
                         },
                         {"timestamp": 1502989426,
                          "timestamp_nanoseconds": 155931927,
                          "date": "2017-08-17T17:03:46+00:00",
                          "event_type": "NFM",
                          "group_guids": ["b077d6bc-bbdf-42f7-8838-a06053fbd98a"],
                          "network_info": {"dirty_url": "http://www.sanjosemaristas.com/app/index.php?", "remote_ip": "188.120.225.17",
                                           "remote_port": 80, "local_ip": "192.168.1.3", "local_port": 54232,
                                           "nfm": { "direction": "Outgoing connection from","protocol": "TCP"},
                                           "parent": { "disposition": "Clean",
                                                        "identity": {"sha256": "5ad3c37e6f2b9db3ee8b5aeedc474645de90c66e3d95f8620c48102f1eba4124"}
                                        }
                          }
                         }
                        ]
            },
            "metadata": {
              "links": {
                "self": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f/trajectory"
              }
            }
          }
        }

}
"""
#  Globals
# List of fields in datatable fn_amp_get_computer_trajectory script
DATA_TBL_FIELDS = ["query_execution_time", "query", "hostname"]
DATA_TBL_FIELDS_EVNTS = ["date", "event_type", ]
DATA_TBL_FIELDS_FILE = ["file_type", "file_name", "disposition", "file_path", "sha256", "parent_sha256" ]
DATA_TBL_FIELDS_NI = ["local_port", "remote_port",  "remote_ip", "direction", "protocol", "dirty_url", "disposition"]

# Processing
response = results.get("response", {})
query_execution_time = results.get("query_execution_time")
input_params = results.get("input_params", {})
total = results.get("total")

if response is not None:
    data = response.get("data", {})
    computer = data.get("computer", {})
    connector_guid = computer.get("connector_guid", "")
    hostname = computer.get("hostname", "")
    events = data.get("events", [])
    q = input_params.get("q")

    noteText = u"Cisco AMP for Endpoints Integration: There were <b>{0}</b> results returned out of a total of <b>{1}</b>" \
               " for hostname <b>{2}</b> for query  <b>{3}</b> for Resilient function <b>{4}</b>"\
        .format(len(data["events"]), total, hostname, q, "fn_amp_get_computer_trajectory")
    for e in events:
        newrow = incident.addRow("amp_computer_trajectory")
        newrow.query_execution_time = query_execution_time
        newrow.query = q
        newrow.hostname = hostname
        for f in DATA_TBL_FIELDS_EVNTS:
            if e[f] is not None:
                newrow[f] = e[f]
            fi = e.get("file")
            if fi is not None:
                id = fi.get("identity")
                pa = fi.get("parent")
                for f2 in DATA_TBL_FIELDS_FILE:
                    if fi.get(f2) is not None:
                        newrow[f2] = fi[f2]
                    if id is not None and id.get(f2) is not None:
                        newrow[f2] = id[f2]
                    if pa is not None:
                        pi = pa.get("identity")
                        if pi is not None and pi.get(f2) is not None:
                            newrow["parent_sha256"] = pi.get("sha256")

            ni = e.get("network_info")
            if ni is not None:
                nfm = ni.get("nfm")
                pa = ni.get("parent")
                for f3 in DATA_TBL_FIELDS_NI:
                    if ni.get(f3) is not None:
                        newrow[f3] = ni[f3]
                    if nfm is not None and nfm.get(f3) is not None:
                        newrow[f3] = nfm[f3]
                    if pa is not None:
                        pi = pa.get("identity")
                        if pi is not None:
                            newrow["parent_sha256"] = pi.get("sha256")
else:
    noteText += "Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for SOAR function <b>{0}</b>"\
        .format("fn_amp_get_computer_trajectory")

incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - AMP: Get Computers
Returns a list of computers with agents deployed on them. You can use parameters to narrow the search by IP address or hostname.

 ![screenshot: fn-amp-get-computers ](./doc/screenshots/fn-amp-get-computers.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_external_ip` | `text` | No | `-` | External ip of a device used for query. |
| `amp_group_guid` | `text` | No | `-` | Group guid. |
| `amp_hostname` | `text` | No | `-` | Hostname of an endpoint. |
| `amp_internal_ip` | `text` | No | `-` | Internal ip of a device used in a query. |
| `amp_limit` | `number` | No | `-` | The results limit. Max value 500. Note: there is also a global limit  for the integration. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "input_params": {
    "external_ip": null,
    "group_guid": null,
    "hostname": "Demo_WannaCry_Ransomware",
    "internal_ip": null,
    "limit": null
  },
  "query_execution_time": "2024-05-31 16:13:47",
  "response": {
    "data": [
      {
        "active": true,
        "connector_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
        "connector_version": "8.4.0.30201",
        "demo": true,
        "external_ip": "222.222.21.1",
        "faults": [],
        "flag": false,
        "group_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
        "groups": [
          {
            "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
            "name": "Protect"
          }
        ],
        "hostname": "Demo_WannaCry_Ransomware",
        "id": 70000006,
        "install_date": "2024-04-29T00:10:43Z",
        "internal_ips": [
          "111.222.222.222"
        ],
        "is_compromised": true,
        "isolation": {
          "available": true,
          "status": "not_isolated"
        },
        "last_seen": "2024-05-29T00:10:43Z",
        "links": {
          "computer": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "group": "https://api.amp.cisco.com/v1/groups/aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "trajectory": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc/trajectory"
        },
        "network_addresses": [
          {
            "ip": "226.249.214.245",
            "mac": "1e:c0:c8:7e:bf:07"
          }
        ],
        "operating_system": "Windows 10 (Build 19044.1466)",
        "orbital": {
          "status": "not_enabled"
        },
        "os_type": "WinOs",
        "os_version": "10.0.19044.1466",
        "policy": {
          "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "name": "Protect"
        },
        "risk_score": 100,
        "supports": {
          "device_trajectory": true,
          "events": true,
          "move_to_group": true,
          "orbital": {
            "agent_active": false,
            "agent_nil_state": false,
            "agent_supported": true,
            "is_supported": true,
            "min_supported_agent_version": "7.1.5.11523",
            "min_supported_os_version": "10.0.16299",
            "os_supported": true,
            "policy_supported": false
          },
          "request_snapshot": true,
          "scan": true
        },
        "windows_processor_id": "abcdefg1234567"
      }
    ],
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/computers?hostname=Demo_WannaCry_Ransomware"
      },
      "results": {
        "current_item_count": 1,
        "index": 0,
        "items_per_page": 500,
        "total": 1
      }
    },
    "version": "v1.2.0"
  }
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.amp_hostname = artifact.value
inputs.amp_group_guid = None
inputs.amp_external_ip = None
inputs.amp_internal_ip = None
inputs.amp_limit = None
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
##  Cisco AMP for endpoints - fn_amp_get_computers script ##
#  fn_amp_get_computers  -  Event type list
# Example result:
"""
Result: {
                  "input_params": {"conn_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f"},
                  "response": {
                    "version": "v1.2.0",
                    "data": {
                      "operating_system": "Windows 7, SP 1.0",
                      "connector_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f",
                      "links": {
                        "trajectory": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f/trajectory",
                        "computer": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f",
                        "group": "https://api.amp.cisco.com/v1/groups/89663c44-f95e-4ee8-896d-7611744a6e9a"
                      },
                      "policy": {
                        "guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b",
                        "name": "Audit"
                      },
                      "external_ip": "145.1.91.176",
                      "group_guid": "89663c44-f95e-4ee8-896d-7611744a6e9a",
                      "hostname": "Demo_AMP",
                      "install_date": "2018-05-22T16:53:27Z",
                      "network_addresses": [
                        {
                          "ip": "255.240.221.92",
                          "mac": "a0:28:f5:c3:71:d5"
                        }
                      ],
                      "connector_version": "6.0.9.10685",
                      "internal_ips": [
                        "255.240.221.92"
                      ],
                      "faults": [],
                      "active": true,
                      "last_seen": "2018-05-22T16:53:27Z"
                    },
                    "metadata": {
                      "links": {
                        "self": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f"
                      }
                    }
                  },
                  "query_execution_time": "2018-10-22 09:28:25"
}
"""
#  Globals
# List of fields in datatable fn_amp_get_computers script
DATA_TBL_FIELDS = ["query_execution_time", "hostname", "operating_system", "connector_guid", "connector_version", "group_guid",
                   "last_seen", "external_ip", "internal_ips", "install_date", "last_seen", "policy_name"]

# Processing
noteText = ''
response = results.get("response")
query_execution_time = results.get("query_execution_time")
input_params = results.get("input_params")

if response is not None and response.get("metadata", {}).get("results", {}).get("total") != 0:
    noteText = u"Cisco AMP for Endpoints Integration: Result returned for computer <b>{0}</b> " \
               "for SOAR function <b>{1}</b>"\
        .format(input_params.get("hostname"), "fn_amp_get_computer")
    for data in response.get("data", []):
        newrow = incident.addRow("amp_computers")
        newrow.query_execution_time = query_execution_time
        for f in DATA_TBL_FIELDS:
            if f == "query_execution_time" or "policy" in f:
                continue
            data_fields = data.get(f)
            if isinstance(data_fields, str) or len(data_fields) == 0:
                newrow[f] = data[f]
            else:
                newrow[f] = ','.join(data_fields)
        policy = data.get("policy")
        if policy is not None:
            newrow.policy_name = policy.get("name", "")
else:
    noteText += u"Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for computer <b>{0}</b> SOAR " \
                "function <b>{1}</b>".format(input_params.get("hostname", {}), "fn_amp_get_computers")

incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - AMP: Get Event Types
Returns list of events identified and filtered by a unique ID. Provides a human readable name, and short description of each event by ID.

 ![screenshot: fn-amp-get-event-types ](./doc/screenshots/fn-amp-get-event-types.png)

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
  "query_execution_time": "2024-05-31 16:06:25",
  "response": {
    "data": [
      {
        "description": "A new agent has registered with the system.",
        "id": 50000000,
        "name": "Initial Agent Registration"
      },
      {
        "description": "An agent has been told to fetch policy.",
        "id": 50000000,
        "name": "Policy Update"
      },
      {
        "description": "An agent has started scanning.",
        "id": 50000000,
        "name": "Scan Started"
      }
    ],
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/event_types"
      },
      "results": {
        "total": 117
      }
    },
    "version": "v1.2.0"
  }
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
##  Cisco AMP for endpoints - fn_amp_get_event_types script ##
#  fn_amp_get_event_types  -  Event type list
# Example result:
"""
Result: {
          "response": {
            "version": "v1.2.0",
            "data": [
              {
                "description": "An agent has been told to fetch policy.",
                "id": 553648130,
                "name": "Policy Update"
              },
              {
                "description": "An agent has started scanning.",
                "id": 554696714,
                "name": "Scan Started"
              },
              {
                "description": "A scan has completed without detecting anything malicious.",
                "id": 554696715,
                "name": "Scan Completed, No Detections"
              },
              ...
              ...

            ],
            "metadata": {
              "results": {
                "total": 94
              },
              "links": {
                "self": "https://api.amp.cisco.com/v1/event_types"
              }
            }
          },
          "query_execution_time": "2018-10-08 16:27:32"
        }
"""
#  Globals
# List of fields in datatable fn_amp_get_event_types script - reference only
DATA_TBL_FIELDS = ["query_execution_time", "event_type_name", "event_type_id" "event_type_description"]

# Processing
response = results.response
query_execution_time = results.query_execution_time

if response is not None:
    r = response["metadata"]["results"]
    noteText = "Cisco AMP for Endpoints Integration: There were <b>{0}</b> results returned out of a total of <b>{1}</b> for Resilient function " \
               "<b>{2}</b>".format(len(response["data"]), r["total"], "fn_amp_get_event_types")
    for data in response["data"]:
        newrow = incident.addRow("amp_event_types")
        newrow.query_execution_time = query_execution_time
        newrow.event_type_name = data.get("name", "")
        newrow.event_type_id = str(data.get("id", ""))
        newrow.event_type_description = data.get("description", "")
else:
    noteText += "Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for Resilient function <b>{0}</b>".format("fn_amp_get_event_types")

incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - AMP: Get Events
Returns a  list of events.

 ![screenshot: fn-amp-get-events ](./doc/screenshots/fn-amp-get-events.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_application_sha256` | `text` | No | `-` | Application sha256 value used to query events. |
| `amp_conn_guid` | `text` | No | `-` | Connector guid. |
| `amp_detection_sha256` | `text` | No | `-` | Detection sha256 value used to query events. |
| `amp_event_type` | `text` | No | `-` | AMP event type used to query for events. |
| `amp_group_guid` | `text` | No | `-` | Group guid. |
| `amp_limit` | `number` | No | `-` | The results limit. Max value 500. Note: there is also a global limit  for the integration. |
| `amp_offset` | `number` | No | `-` | Offset to start query from. |
| `amp_severity` | `text` | No | `-` | Filter by result property. |
| `amp_start_date` | `datetimepicker` | No | `-` | Start date |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "input_params": {
    "application_sha256": null,
    "connector_guid": null,
    "detection_sha256": null,
    "event_type": null,
    "group_guid": null,
    "limit": null,
    "offset": null,
    "severity": null,
    "start_date": null
  },
  "query_execution_time": "2024-05-31 16:24:11",
  "response": {
    "data": [
      {
        "computer": {
          "active": true,
          "connector_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "external_ip": "238.190.21.1",
          "hostname": "Demo_WannaCry_Ransomware",
          "links": {
            "computer": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc",
            "group": "https://api.amp.cisco.com/v1/groups/aaaaaaaa-1111-2222-bbbb-cccccccccccc",
            "trajectory": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc/trajectory"
          },
          "network_addresses": [
            {
              "ip": "222.222.222.245",
              "mac": "1e:c0:c8:7e:bf:07"
            }
          ]
        },
        "connector_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
        "date": "2024-05-29T20:31:54+00:00",
        "event_type": "Endpoint Isolation Stop Success",
        "event_type_id": 553648204,
        "group_guids": [
          "aaaaaaaa-1111-2222-bbbb-cccccccccccc"
        ],
        "id": 17171717171717171717,
        "isolation": {
          "duration": 46
        },
        "timestamp": 1717014714,
        "timestamp_nanoseconds": 0
      },
      {
        "computer": {
          "active": true,
          "connector_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "external_ip": "222.222.21.1",
          "hostname": "Demo_WannaCry_Ransomware",
          "links": {
            "computer": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc",
            "group": "https://api.amp.cisco.com/v1/groups/aaaaaaaa-1111-2222-bbbb-cccccccccccc",
            "trajectory": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-1111-2222-bbbb-cccccccccccc/trajectory"
          },
          "network_addresses": [
            {
              "ip": "222.222.222.245",
              "mac": "1e:c0:c8:7e:bf:07"
            }
          ]
        },
        "connector_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
        "date": "2024-05-29T20:26:22+00:00",
        "event_type": "Endpoint Isolation Start Success",
        "event_type_id": 553648202,
        "group_guids": [
          "aaaaaaaa-1111-2222-bbbb-cccccccccccc0"
        ],
        "id": 17171717171717171717,
        "timestamp": 1717014382,
        "timestamp_nanoseconds": 0
      }
    ],
    "metadata": {
      "links": {
        "next": "https://api.amp.cisco.com/v1/events?offset=500",
        "self": "https://api.amp.cisco.com/v1/events"
      },
      "results": {
        "current_item_count": 500,
        "index": 0,
        "items_per_page": 500,
        "total": 1005
      }
    },
    "version": "v1.2.0"
  }
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.amp_application_sha256 = None
inputs.amp_conn_guid  = None
inputs.amp_detection_sha256  = None
inputs.amp_event_type = None
inputs.amp_group_guid  = None
inputs.amp_limit  = rule.properties.amp_limit
inputs.amp_offset  = rule.properties.amp_offset
inputs.amp_start_date  = rule.properties.amp_start_date
inputs.amp_severity = rule.properties.amp_severity

```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
##  Cisco AMP for endpoints - fn_amp_get_events script ##
#  fn_amp_get_events  -  Events list
# Example result:
"""
Result:  {
          "input_params": {"detection_sha256": null, "application_sha256": null, "connector_guid": null,
                           "group_guid": null, "start_date": null, "event_type": null, "limit": null, "offset": null},
          "response": {
            "version": "v1.2.0",
            "data": [
              {
                "id": 6455442249407791000,
                "timestamp": 1503024774,
                "severity": "High",
                "timestamp_nanoseconds": 98000000,
                "date": "2017-08-18T02:52:54+00:00",
                "event_type": "Threat Detected",
                "event_type_id": 1090519054,
                "detection": "benign_qa_testware7",
                "detection_id": "6455442249407791109",
                "group_guids": [
                  "b077d6bc-bbdf-42f7-8838-a06053fbd98a"
                ],
                "computer": {
                  "connector_guid": "af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01",
                  "hostname": "WIN-S1AC1PI6L5L",
                  "external_ip": "10.200.65.31",
                  "user": "johndoe@WIN-S1AC1PI6L5L",
                  "active": true,
                  "network_addresses": [
                    {
                      "ip": "10.0.2.15",
                      "mac": "08:00:27:85:28:61"
                    }
                  ],
                  "links": {
                    "computer": "https://api.amp.cisco.com/v1/computers/af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01",
                    "trajectory": "https://api.amp.cisco.com/v1/computers/af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01/trajectory",
                    "group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"
                  }
                },
                "file": {
                  "disposition": "Unknown",
                  "file_name": "file.zip",
                  "file_path": "\\\\?\\C:\\Users\\johndoe\\Downloads\\file.zip",
                  "identity": {
                    "sha256": "f8a6a244138cb1e2f044f63f3dc42beeb555da892bbd7a121274498cbdfc9ad5",
                    "sha1": "20eeee16345e0c1283f7b500126350cb938b8570",
                    "md5": "6853839cde69359049ae6f7bd3ae86d7"
                  },
                  "archived_file": {
                    "disposition": "Malicious",
                    "identity": {
                      "sha256": "46679a50632d05b99683a14b91a69ce908de1673fbb71e9cd325e5685fcd7e49"
                    }
                  },
                  "parent": {
                    "process_id": 3416,
                    "disposition": "Clean",
                    "file_name": "explorer.exe",
                    "identity": {
                      "sha256": "80ef843fa78c33b511394a9c7535a9cbace1deb2270e86ee4ad2faffa5b1e7d2",
                      "sha1": "ea97227d34b8526055a543ade7d18587a927f6a3",
                      "md5": "15bc38a7492befe831966adb477cf76f"
                    }
                  }
                }
              },
              ...
              ...
            ],
            "metadata": {
              "results": {
                "index": 0,
                "total": 0,
                "items_per_page": 500,
                "current_item_count": 0
              },
              "links": {
                "self": "https://api.amp.cisco.com/v1/events"
              }
            }
          },
          "query_execution_time": "2018-10-09 11:05:12"
}
"""
#  Globals
# List of fields in datatable fn_amp_get_events script - reference only
DATA_TBL_FIELDS_TOP = ["query_execution_time", "event_id", "date", "event_type", "event_type_id", "severity"]
DATA_TBL_FIELDS_COMPUTER = ["hostname", "external_ip"]
DATA_TBL_FIELDS_FILE = ["disposition", "file_name", "file_path", "sha256"]

# Processing
response = results.response
query_execution_time = results.query_execution_time

if response is not None:
    r = response["metadata"]["results"]
    noteText = "Cisco AMP for Endpoints Integration: There were <b>{0}</b> results returned out of a total of <b>{1}</b> for Resilient function " \
               "<b>{2}</b>".format(len(response["data"]), r["total"], "fn_amp_get_events")
    for d in response["data"]:
        newrow = incident.addRow("amp_events")
        newrow.query_execution_time = query_execution_time
        newrow.event_id = str(d.get("id", ""))
        newrow.event_type = d.get("event_type", "")
        newrow.severity = d.get("severity", "")
        newrow.date = d.get("date", "")
        c = d.get("computer")
        if c is not None:
            for fi in DATA_TBL_FIELDS_COMPUTER:
                comp_field = c.get(fi)
                if isinstance(comp_field, str) or len(comp_field) == 0:
                    newrow[fi] = comp_field
                else:
                    newrow[fi] = '[' + ''.join(comp_field) + ']'
        fl = d.get("file")
        if fl is not None:
            fident  =  fl.get("identity")
            if fident is not None:
                newrow.sha256 = fident.get("sha256", "")
            for fi in DATA_TBL_FIELDS_FILE:
                if fl.get(fi) is not None:
                    newrow[fi] = fl[fi]
else:
    noteText += "Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for Resilient function <b>{0}</b>".format("fn_amp_get_events")

incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - AMP: Get File Lists
Returns a list of simple custom detection file lists. You can filter this list by name.

 ![screenshot: fn-amp-get-file-lists ](./doc/screenshots/fn-amp-get-file-lists.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_limit` | `number` | No | `-` | The results limit. Max value 500. Note: there is also a global limit  for the integration. |
| `amp_offset` | `number` | No | `-` | Offset to start query from. |
| `amp_scd_name` | `text` | No | `-` | SCD (Simple custom detection) list name. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "input_params": {
    "limit": null,
    "name": null,
    "offset": null
  },
  "query_execution_time": "2024-05-31 16:19:18",
  "response": {
    "data": [
      {
        "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
        "links": {
          "file_list": "https://api.amp.cisco.com/v1/file_lists/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
        },
        "name": "Simple Custom Detection List",
        "type": "simple_custom_detections"
      }
    ],
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/file_lists/simple_custom_detections"
      },
      "results": {
        "current_item_count": 1,
        "index": 0,
        "items_per_page": 500,
        "total": 1
      }
    },
    "version": "v1.2.0"
  }
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
##  Cisco AMP for endpoints - fn_amp_get_file_lists script ##
# Example result:
"""
Result: {
          "input_params": {"name": null, "limit": null, "offset": null },
          "response": {u'version': u'v1.2.0',
                       u'data': {u'items': [],
                                 u'guid': u'9710a198-b95a-462a-b184-9e688968fd94',
                                 u'name': u'File Blacklist',
                                 u'policies': [{ u'guid': u'a98a0f97-4d54-4175-9eef-b8dee9c8e74b',
                                                 u'name': u'Audit',
                                                 u'links': {
                                                    u'policy': u'https://api.amp.cisco.com/v1/policies/a98a0f97-4d54-4175-9eef-b8dee9c8e74b'
                                                 }
                                               }, {
                                                 u'guid': u'fdf4c7f9-b0de-41bf-9d86-d0fae7aa5267',
                                                 u'name': u'Audit',
                                                 u'links': {
                                                     u'policy': u'https://api.amp.cisco.com/v1/policies/fdf4c7f9-b0de-41bf-9d86-d0fae7aa5267'
                                                 }
                                               }
                                 ]
                        },
                        u'metadata': {u'results':
                                        {u'index': 10,
                                         u'total': 1,
                                         u'items_per_page': 500,
                                         u'current_item_count': 0
                                         },
                                      u'links': {
                                          u'self': u'https://api.amp.cisco.com/v1/file_lists/e773a9eb-296c-40df-98d8-bed46322589d/files'
                                         }
                                      }
                        }
          },
          "query_execution_time": "2018-08-09 11:56:02"
    }
"""
#  Globals
# List of fields in datatable fn_amp_get_file_lists script
DATA_TBL_FIELDS = ["query_execution_time", "list_name", "guid", "type"]

# Processing
response = results.response
query_execution_time = results.query_execution_time

if response is not None:
    r = response["metadata"]["results"]
    noteText = "Cisco AMP for Endpoints Integration: There were <b>{0}</b> results returned out of a total of <b>{1}</b> for Resilient function " \
               "<b>{2}</b>".format(len(response["data"]), r["total"], "fn_amp_get_file_lists")
    for d in response["data"]:
        newrow = incident.addRow("amp_scd_file_lists")
        newrow.query_execution_time = query_execution_time
        newrow.list_name = d["name"]
        newrow.guid = d["guid"]
        newrow.type = d["type"]
else:
    noteText += "Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for Resilient function <b>{0}</b>".format("fn_amp_get_file_lists")

incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - AMP: Get Files from List
Returns a list of items for a particular file_list. You need to provide file_list_guid to retrieve these items.

 ![screenshot: fn-amp-get-files-from-list ](./doc/screenshots/fn-amp-get-files-from-list.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_file_list_guid` | `text` | No | `-` | File list guid value. |
| `amp_file_sha256` | `text` | No | `-` | File sha256 value. |
| `amp_limit` | `number` | No | `-` | The results limit. Max value 500. Note: there is also a global limit  for the integration. |
| `amp_offset` | `number` | No | `-` | Offset to start query from. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "input_params": {
    "file_list_guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
    "file_sha256": null,
    "limit": null,
    "offset": null
  },
  "query_execution_time": "2024-05-31 16:22:49",
  "response": {
    "data": {
      "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
      "items": [],
      "name": "Simple Custom Detection List",
      "policies": [
        {
          "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "links": {
            "policy": "https://api.amp.cisco.com/v1/policies/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
          },
          "name": "Audit"
        },
        {
          "guid": "0280b143-7091-45c4-8502-ab250219d796",
          "links": {
            "policy": "https://api.amp.cisco.com/v1/policies/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
          },
          "name": "Protect"
        },
        {
          "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "links": {
            "policy": "https://api.amp.cisco.com/v1/policies/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
          },
          "name": "Triage"
        },
        {
          "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "links": {
            "policy": "https://api.amp.cisco.com/v1/policies/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
          },
          "name": "Server"
        },
        {
          "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "links": {
            "policy": "https://api.amp.cisco.com/v1/policies/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
          },
          "name": "Domain Controller"
        },
        {
          "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "links": {
            "policy": "https://api.amp.cisco.com/v1/policies/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
          },
          "name": "Audit"
        },
        {
          "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "links": {
            "policy": "https://api.amp.cisco.com/v1/policies/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
          },
          "name": "Protect"
        },
        {
          "guid": "cb94c359-8eec-460b-a6c2-d7631510d34e",
          "links": {
            "policy": "https://api.amp.cisco.com/v1/policies/cb94c359-8eec-460b-a6c2-d7631510d34e"
          },
          "name": "Triage"
        },
        {
          "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "links": {
            "policy": "https://api.amp.cisco.com/v1/policies/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
          },
          "name": "Audit"
        },
        {
          "guid": "aaaaaaaa-1111-2222-bbbb-cccccccccccc",
          "links": {
            "policy": "https://api.amp.cisco.com/v1/policies/aaaaaaaa-1111-2222-bbbb-cccccccccccc"
          },
          "name": "Protect"
        }
      ]
    },
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/file_lists/aaaaaaaa-1111-2222-bbbb-cccccccccccc/files"
      },
      "results": {
        "current_item_count": 0,
        "index": 0,
        "items_per_page": 500,
        "total": 0
      }
    },
    "version": "v1.2.0"
  }
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.amp_file_list_guid = row.guid
inputs.amp_file_sha256 = None
inputs.amp_limit = None
inputs.amp_offset = None
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
##  Cisco AMP for endpoints - fn_amp_get_file_list_files script ##
#  fn_amp_get_file_list_files  -  Event type list
# Example result:
"""
Result:  {
          "input_params": {"file_list_guid": "e773a9eb-296c-40df-98d8-bed46322589d",
                           "file_sha256": "", "limit": null,
                           "offset": null},
          "response": {
            "version": "v1.2.0",
            "data": {
              "items": [
                {
                  "source": "Created by entering SHA-256 via Public api.",
                  "sha256": "c26dc4e73a335b4414d238b6b30bfd6aff693293f9e4946b5df13f9aac40af5c",
                  "description": "A test malware file. ",
                  "links": {
                    "file_list": "https://api.amp.cisco.com/v1/file_lists/9710a198-b95a-462a-b184-9e688968fd94"
                  }
                },
                {
                  "source": "Created by entering SHA-256 via Public api.",
                  "sha256": "d15766ead5d8ffe68fd96d4bda75c07378fc74f76e251ae6631f4ec8226d2bcb",
                  "description": "\"Malware test file - by JP.\"",
                  "links": {
                    "file_list": "https://api.amp.cisco.com/v1/file_lists/9710a198-b95a-462a-b184-9e688968fd94"
                  }
                }
              ],
              "guid": "9710a198-b95a-462a-b184-9e688968fd94",
              "name": "File Blacklist",
              "policies": [
                {
                  "guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b",
                  "name": "Audit",
                  "links": {
                    "policy": "https://api.amp.cisco.com/v1/policies/a98a0f97-4d54-4175-9eef-b8dee9c8e74b"
                  }
                },
                {
                  "guid": "51450374-366c-4759-9099-7baa138c499f",
                  "name": "Triage",
                  "links": {
                    "policy": "https://api.amp.cisco.com/v1/policies/51450374-366c-4759-9099-7baa138c499f"
                  }
                },
                ...
                ...
              ]
            },
            "metadata": {
              "results": {
                "index": 0,
                "total": 2,
                "items_per_page": 50,
                "current_item_count": 2
              },
              "links": {
                "self": "https://api.amp.cisco.com/v1/file_lists/9710a198-b95a-462a-b184-9e688968fd94/files?limit=50"
              }
            }
          },
          "query_execution_time": "2018-10-23 10:09:19"
}
"""
#  Globals
# List of fields in datatable fn_amp_get_file_list_files script
DATA_TBL_FIELDS = ["query_execution_time", "list_name", "guid", "file_description", "sha256", "source"]

# Processing
response = results.response
query_execution_time = results.query_execution_time
if response is not None:
    data = response["data"]
    r = response["metadata"]["results"]
    noteText = "Cisco AMP for Endpoints Integration: There were <b>{0}</b> results returned out of a total of <b>{1}</b> " \
               "for list <b>{2}</b> for Resilient function <b>{3}</b>"\
        .format(len(data["items"]), r["total"], data["name"], "fn_amp_get_file_list_files")
    if data is not None:
        items = data["items"]
        for i in items:
            newrow = incident.addRow("amp_file_list_files")
            newrow.query_execution_time = query_execution_time
            for f in DATA_TBL_FIELDS[1:]:
                if data[f] is not None:
                    newrow[f] = data[f]
                if i[f] is not None:
                    newrow[f] = i[f]
            if data.name is not None:
                newrow.list_name = data.name
            if i.description is not None:
                newrow.file_description = i.description
else:
    noteText += "Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for Resilient function <b>{0}</b>"\
        .format("fn_amp_get_file_list_files")

incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - AMP: Get Groups
Returns basic information on multiple groups or group by name. Returns more detailed information on group by guid.

 ![screenshot: fn-amp-get-groups ](./doc/screenshots/fn-amp-get-groups.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_group_guid` | `text` | No | `-` | Group guid. |
| `amp_group_name` | `text` | No | `-` | Group name. |
| `amp_limit` | `number` | No | `-` | The results limit. Max value 500. Note: there is also a global limit  for the integration. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "input_params": {
    "group_guid": null,
    "limit": null,
    "name": "Test Group2"
  },
  "query_execution_time": "2024-05-31 16:12:46",
  "response": {
    "data": [],
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/groups?name=Test+Group2"
      },
      "results": {
        "current_item_count": 0,
        "index": 0,
        "items_per_page": 500,
        "total": 0
      }
    },
    "version": "v1.2.0"
  }
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.amp_group_guid = row.group_guid
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
##  Cisco AMP for endpoints - fn_amp_get_groups script ##
#  fn_amp_get_groups
# Example result:
"""
Result: {
           "query_execution_time": "2018-11-22 12:14:28",
           "input_params": {
             "group_guid": "5931a062-19b3-46ad-9b09-d246430aba02",
             "name": null,
             "limit": null
           },
           "response": {
             "version": "v1.2.0",
             "metadata": {
               "links": {
                 "self": "https://api.amp.cisco.com/v1/groups/5931a062-19b3-46ad-9b09-d246430aba02?limit=10"
               }
             },
             "data": {
               "name": "Test Group2",
               "description": "Test group 3.",
               "guid": "5931a062-19b3-46ad-9b09-d246430aba02",
               "source": null,
               "policies": [
                 {
                   "name": "Audit",
                   "description": "This policy puts the AMP for Endpoints Connector in a mode that will only detect malicious files but not quarantine them. Malicious network traffic is also detected but not blocked.",
                   "guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b",
                   "product": "windows",
                   "default": true,
                   "serial_number": 52,
                   "links": {
                     "policy_xml": "https://api.amp.cisco.com/v1/policies/a98a0f97-4d54-4175-9eef-b8dee9c8e74b.xml",
                     "policy": "https://api.amp.cisco.com/v1/policies/a98a0f97-4d54-4175-9eef-b8dee9c8e74b"
                   },
                   "file_lists": [
                     {
                       "name": "File Blacklist",
                       "guid": "9710a198-b95a-462a-b184-9e688968fd94",
                       "type": "simple_custom_detections"
                     },
                     {
                       "name": "Execution Blacklist",
                       "guid": "3792e397-50b0-42e3-98af-35b9b7988223",
                       "type": "application_blocking"
                     },
                     {
                       "name": "File Whitelist",
                       "guid": "6b0baed2-fc8c-454d-b168-4510a89f4588",
                       "type": "application_whitelist"
                     }
                   ],
                   "ip_lists": [],
                   "exclusion_sets": [
                     {
                       "name": "Workstation Exclusions",
                       "guid": "6bc4b73c-b4be-4487-96aa-ea24520ef3d7"
                     }
                   ],
                   "used_in_groups": [
                     {
                       "name": "Audit",
                       "description": "Audit Group for Partner - IBM Security",
                       "guid": "9d55c259-c960-488b-9b2d-06478fa19ee4"
                     }
                   ],
                   "inherited": false
                 },
                 ...
                 ...
               ]
             }
           }
}
"""
#  Globals
# List of fields in datatable
DATA_TBL_FIELDS = ["group_name"]

# Processing
response = results.response

if response is not None:
   data = response["data"]
   row.group_name = data.get("name", "")
```

</p>
</details>

---
## Function - AMP: Move Computer
Move a computer by connector guid to a group by group guid.

 ![screenshot: fn-amp-move-computer ](./doc/screenshots/fn-amp-move-computer.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_conn_guid` | `text` | No | `-` | Connector guid. |
| `amp_group_guid` | `text` | No | `-` | Group guid. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "response": {
    "data": {
      "active": true,
      "connector_guid": "aaaaaaaa-bbbb-1111-2222-cccccccccccc",
      "connector_version": "99.0.99.20946",
      "csc_id": "aaaaaaaa-bbbb-1111-2222-cccccccccccc",
      "demo": true,
      "external_ip": "xxx.xxx.xxx.xxx",
      "faults": [],
      "group_guid": "aaaaaaaa-bbbb-1111-2222-cccccccccccc",
      "groups": [
        {
          "guid": "aaaaaaaa-bbbb-1111-2222-cccccccccccc",
          "name": "Protect"
        }
      ],
      "hostname": "Demo_AMP",
      "install_date": "2022-02-16T11:40:01Z",
      "internal_ips": [
        "xxx.xxx.xxx.xxx"
      ],
      "is_compromised": true,
      "isolation": {
        "available": false,
        "status": "not_isolated"
      },
      "links": {
        "computer": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-bbbb-1111-2222-cccccccccccc",
        "group": "https://api.amp.cisco.com/v1/groups/6c3c2005-4c74-4ba7-8dbb-c4d5b6bafe03",
        "trajectory": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-bbbb-1111-2222-cccccccccccc/trajectory"
      },
      "network_addresses": [
        {
          "ip": "xxx.xxx.xxx.xxx",
          "mac": "xx:xx:xx:xx:xx:xx"
        }
      ],
      "operating_system": "Windows 10",
      "orbital": {
        "status": "not_enabled"
      },
      "os_version": "10.0.19044.1466",
      "policy": {
        "guid": "aaaaaaaa-bbbb-1111-2222-cccccccccccc",
        "name": "Protect Policy"
      },
      "windows_processor_id": "195b0d8736e2af4"
    },
    "input_params": {
      "amp_conn_guid": "aaaaaaaa-bbbb-1111-2222-cccccccccccc",
      "amp_group_guid": "aaaaaaaa-bbbb-1111-2222-cccccccccccc"
    },
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/computers/aaaaaaaa-bbbb-1111-2222-cccccccccccc?group_guid=aaaaaaaa-bbbb-1111-2222-cccccccccccc"
      }
    },
    "query_execution_time": "2024-05-31 16:12:46",
    "version": "v1.2.0"
  }
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
response_groups =  workflow.properties.get_groups_results.response
input_params_groups = workflow.properties.get_groups_results.input_params
response_computers =  workflow.properties.get_computers_results.response
input_params_computers = workflow.properties.get_computers_results.input_params
if response_groups.get("metadata", {}).get("results", {}).get("total") > 0:
  inputs.amp_group_guid = response_groups["data"][0]["guid"]
else:
  raise ValueError("No results returned for group name")
if response_computers.get("metadata", {}).get("results", {}).get("total") > 0:
  inputs.amp_conn_guid = response_computers["data"][0]["connector_guid"]
else:
  raise ValueError("No results returned for computer name")
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
##  Cisco AMP for endpoints - fn_amp_move_computer script ##
#  fn_amp_move_computer  -  Event type list
# Example result:
"""
Result: {
          "input_params": {"conn_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f",
                           "group_guid": "89663c44-f95e-4ee8-896d-7611744a6e9a"},
          "response": {
            "version": "v1.2.0",
            "data": {
              "operating_system": "Windows 7, SP 1.0",
              "connector_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f",
              "links": {
                "trajectory": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f/trajectory",
                "computer": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f",
                "group": "https://api.amp.cisco.com/v1/groups/89663c44-f95e-4ee8-896d-7611744a6e9a"
              },
              "policy": {
                "guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b",
                "name": "Audit"
              },
              "external_ip": "145.1.91.176",
              "group_guid": "89663c44-f95e-4ee8-896d-7611744a6e9a",
              "hostname": "Demo_AMP",
              "install_date": "2018-05-22T16:53:27Z",
              "network_addresses": [
                {
                  "ip": "255.240.221.92",
                  "mac": "a0:28:f5:c3:71:d5"
                }
              ],
              "connector_version": "6.0.9.10685",
              "internal_ips": [
                "255.240.221.92"
              ],
              "active": true
            },
            "metadata": {
              "links": {
                "self": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f"
              }
            }
          },
          "query_execution_time": "2018-10-08 15:22:26"
        }

"""
#  Globals
# List of fields in datatable fn_amp_move_computer script
DATA_TBL_FIELDS = ["delete_execution_time", "status"]

# Processing
response = results.get("response")
query_execution_time = results.get("query_execution_time")
input_params_groups = workflow.properties.get_groups_results.input_params

if response is not None:
    resp_data = response.get("data", {})
    hostname = resp_data.get("hostname")
    row.group_guid = resp_data.get("group_guid")
    noteText = "Cisco AMP for Endpoints Integration: Successfully moved computer with hostname <b>{0}</b> " \
               "to group <b>{1}</b> for SOAR function <b>{2}</b>."\
        .format(hostname, input_params_groups.get("name"), "fn_amp_move_computer")
else:
  noteText = "Cisco AMP Integration: Move unsuccessful for computer with guid <b>{0}</b> " \
               "to group <b>{1}</b> for SOAR function <b>{2}</b>."\
        .format(hostname, input_params_groups.get("name"), "fn_amp_move_computer")

incident.addNote(helper.createRichText(noteText))
```

</p>
</details>

---
## Function - AMP: Set File in List
Add a SHA-256 to a file list by file_list_guid.

 ![screenshot: fn-amp-set-file-in-list ](./doc/screenshots/fn-amp-set-file-in-list.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `amp_file_description` | `text` | No | `-` | File description used to add file sha256 to a list. |
| `amp_file_list_guid` | `text` | No | `-` | File list guid value. |
| `amp_file_sha256` | `text` | No | `-` | File sha256 value. |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "input_params": {
    "description": "Empty description.",
    "file_list_guid": "aaaaaaaa-bbbb-1111-3333-6695009330bb",
    "file_sha256": "abcdefg123457"
  },
  "query_execution_time": "2024-06-03 16:35:14",
  "response": {
    "data": {
      "links": {
        "file_list": "https://api.amp.cisco.com/v1/file_lists/aaaaaaaa-bbbb-1111-3333-6695009330bb"
      },
      "sha256": "00fc4aba3a120ba1f6c3453ea8faa4ca7167fabd30ac297eb59905d7a879e352",
      "source": "Created by entering SHA-256 via Public api."
    },
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/file_lists/aaaaaaaa-bbbb-1111-3333-6695009330bb/files/abcdefghi01234567"
      }
    },
    "version": "v1.2.0"
  }
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
# The parameter amp_file_list_guid needs to be set to a valid file list guid.
# e.g. inputs.amp_file_list_guid = "9710a198-b95a-462a-b184-9e688968fd94"
# In the example it will be assigned from an activity field drop-down.
get_file_lists_response = workflow.properties.get_file_lists_results.response
inputs.amp_file_list_guid = get_file_lists_response["data"][0]["guid"]
inputs.amp_file_sha256 = artifact.value
if artifact.description is not None:
  inputs.amp_file_description = artifact.description.content
else:
  inputs.amp_file_description = "Empty description."
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
##  Cisco AMP for endpoints - fn_amp_set_file_list_files script ##
#  fn_amp_set_file_list_files
# Example result:
"""
Result: {
          "input_params":{"file_list_guid": "e773a9eb-296c-40df-98d8-bed46322589d",
                          "file_sha256": "8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284",
                          "description": "Sha256 description"},
          "response": {u'version': u'v1.2.0',
                                  u'data': {u'source': u'Created by entering SHA-256 via Public api.',
                                    u'sha256': u'8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284',
                                    u'description': u'Test file sha256',
                                    u'links': {u'file_list': u'https://api.amp.cisco.com/v1/file_lists/e773a9eb-296c-40df-98d8-bed46322589d'}
                                  },
                                  u'metadata': {
                                    u'links': {
                                        u'self': u'https://api.amp.cisco.com/v1/file_lists/e773a9eb-296c-40df-98d8-bed46322589d/files/8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284'}
                                    }
                                  },
          "query_execution_time": "2018-08-09 11:56:02"
}

"""
#  Globals
# List of fields in datatable fn_amp_set_file_list_files script


# Processing
response = results.get("response")
query_execution_time = results.get("query_execution_time")
input_params = results.get("input_params", {})
errors = response.get("errors")

if response is not None and errors is None:
    noteText = "Cisco AMP for Endpoints Integration: Successfully added sha256 <b>{0}</b> " \
               "to list with guid <b>{1}</b> for Resilient function <b>{2}</b>."\
        .format(input_params.get("file_sha256"), input_params.get("file_list_guid"), "fn_amp_set_file_list_files")
else:
  noteText = "Cisco AMP Integration: Unsuccessful attempt to set sha256 <b>{0}</b> to list with guid <b>{1}</b> " \
             "for Resilient function <b>{2}</b>."\
        .format(input_params.get("file_sha256"), input_params.get("file_list_guid"), "fn_amp_set_file_list_files")

incident.addNote(helper.createRichText(noteText))

```

</p>
</details>

---

## Script - scr_amp_add_artifact_from_activity
Example script to create artifacts from Cisco AMP for Endpoints activity properties. Supported artifact types are: "System Name"

**Object:** amp_activity

<details><summary>Script Text:</summary>
<p>

```python
# Create a Resilient artifact based on a drop-down which selects the corresponding data-table field.
ARTIFACT_TYPE = rule.properties.amp_artifact_type_activities
FUNCTION_NAME = "fn_amp_get_activity"
QUERY = row.query
PARAMS = {
    "System Name": row.hostname,
    "String": row.connector_guid
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
    hostname = PARAMS["System Name"]
    guid = PARAMS["String"]

    try:
      artifact_type = ARTIFACT_TYPE.split(' ')[2]
    except:
      artifact_type = ARTIFACT_TYPE
  
    validate_fields(["System Name", artifact_type], PARAMS)

    if artifact_type == "System Name":
        desc = "Hostname '{0}' was detected for query '{1}' by function '{2}' for Cisco AMP for Endpoints."\
            .format(hostname, QUERY, FUNCTION_NAME)
    elif artifact_type == "String":
        desc = "Connector guid '{0}' for hostname '{1}' was detected for query '{2}' by function '{3}' for " \
               "Cisco AMP for Endpoints.".format(guid, hostname, QUERY, FUNCTION_NAME)

    addArtifact(artifact_type, PARAMS[artifact_type], desc)

# Script execution starts here
main()
```

</p>
</details>

---
## Script - scr_amp_add_artifact_from_event
Example script to create artifacts from Cisco AMP for Endpoints event properties. Supported artifact types are: "Malware SHA-256 Hash", "System Name", "File Name", "File Path", "IP Address"

**Object:** amp_events

<details><summary>Script Text:</summary>
<p>

```python
# Create a Resilient artifact based on a drop-down which selects the corresponding data-table field.
ARTIFACT_TYPE = rule.properties.amp_artifact_type_events
FUNCTION_NAME = "fn_amp_get_events"
EVENT_ID = row.event_id
PARAMS = {
    "Malware SHA-256 Hash": row.sha256,
    "System Name": row.hostname,
    "File Name": row.file_name,
    "File Path": row.file_path,
    "IP Address": row.external_ip,
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
   hostname = PARAMS["System Name"]

   validate_fields(["System Name", ARTIFACT_TYPE], PARAMS)

   if ARTIFACT_TYPE == "Malware SHA-256 Hash":
      desc = "File sha256 hash was detected in event id '{0}' on hostname '{1}' by function '{2}' for Cisco AMP for Endpoints."\
         .format(EVENT_ID, hostname, FUNCTION_NAME)
   elif ARTIFACT_TYPE == "System Name":
      desc = "Hostname '{0}' was detected in event id '{1}' by function '{2}' for Cisco AMP for Endpoints."\
          .format(hostname, EVENT_ID, FUNCTION_NAME)
   elif ARTIFACT_TYPE == "File Name":
      desc = "File name was detected in event id '{0}' on hostname '{1}' by function '{2}' for Cisco AMP for Endpoints."\
          .format(EVENT_ID, hostname, FUNCTION_NAME)
   elif ARTIFACT_TYPE == "File Path":
      desc = "File path was detected in event id '{0}' on hostname '{1}' by function '{2}' for Cisco AMP for Endpoints."\
          .format(EVENT_ID, hostname, FUNCTION_NAME)
   elif ARTIFACT_TYPE == "IP Address":
      desc = "External IP Address was detected in event id '{0}' on hostname '{1}' by function '{2}' for Cisco AMP for Endpoints."\
          .format(EVENT_ID, hostname, FUNCTION_NAME)

   addArtifact(ARTIFACT_TYPE, PARAMS[ARTIFACT_TYPE], desc)

# Script execution starts here
main()

```

</p>
</details>

---
## Script - scr_amp_add_artifact_from_trajectory
Example script to create artifacts from Cisco AMP for Endpoints computer trajectory properties. Supported artifact types are: "Malware SHA-256 Hash", "System Name", "File Name", "File Path", "IP Address", "URL"

**Object:** amp_computer_trajectory

<details><summary>Script Text:</summary>
<p>

```python
# Create a Resilient artifact based on a dropdown which selects the corresponding data-table field.
ARTIFACT_TYPE = rule.properties.amp_artifact_type_trajectory
FUNCTION_NAME = "fn_amp_get_computer_trajectory"

PARAMS = {
    "Malware SHA-256 Hash": row.sha256,
    "System Name": row.hostname,
    "File Name": row.file_name,
    "File Path": row.file_path,
    "IP Address": row.remote_ip,
    "URL": row.dirty_url
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
    
    if ARTIFACT_TYPE == "Malware SHA-256 Hash":
        desc =  "File sha256 hash was detected on hostname '{0}' by function '{1}' for Cisco AMP for Endpoints."\
            .format(PARAMS["System Name"], FUNCTION_NAME)
    elif ARTIFACT_TYPE == "System Name":
        desc = "Hostname '{0}' was detected by function '{1}' for Cisco AMP for Endpoints."\
            .format(PARAMS["System Name"], FUNCTION_NAME)
    elif ARTIFACT_TYPE == "File Name":
        desc = "File name was detected on hostname '{0}' by function '{1}' for Cisco AMP for Endpoints."\
            .format(PARAMS["System Name"], FUNCTION_NAME)
    elif ARTIFACT_TYPE == "File Path":
        desc= "File path was detected on hostname '{0}' by function '{1}' for Cisco AMP for Endpoints."\
            .format(PARAMS["System Name"], FUNCTION_NAME)
    elif ARTIFACT_TYPE == "IP Address":
        desc = "Remote IP Address was detected on hostname '{0}' by function '{1}' for Cisco AMP for Endpoints."\
            .format(PARAMS["System Name"], FUNCTION_NAME)
    elif ARTIFACT_TYPE == "URL":
        desc = "Remote IP Address was detected on hostname '{0}' by function '{1}' for Cisco AMP for Endpoints."\
            .format(PARAMS["System Name"], FUNCTION_NAME)

    addArtifact(ARTIFACT_TYPE, PARAMS[ARTIFACT_TYPE], desc)


# Script execution starts here
main()

```

</p>
</details>

---

## Playbooks
| Playbook Name | Description | Activation Type | Object | Status | Condition | 
| ------------- | ----------- | --------------- | ------ | ------ | --------- | 
| AMP: Computer Isolation (PB) | Isolate/De-isolate computer by connector GUID | Manual | amp_computers | `enabled` | `amp_computers.connector_guid has_a_value` | 

---

## Custom Layouts
<!--
  Use this section to provide guidance on where the user should add any custom fields and data tables.
  You may wish to recommend a new incident tab.
  You should save a screenshot "custom_layouts.png" in the doc/screenshots directory and reference it here
-->
* Create a Cisco tab for an incident and add the Data Tables like the screenshot below:

  ![screenshot: custom_layouts](./doc/screenshots/custom_layouts.png)


## Data Table - Cisco AMP activity

 ![screenshot: dt-cisco-amp-activity](./doc/screenshots/dt-cisco-amp-activity.png)

#### API Name:
amp_activity

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Active | `active` | `boolean` | - |
| Connector guid | `connector_guid` | `text` | - |
| Hostname | `hostname` | `text` | - |
| Query execution time | `query_execution_time` | `text` | - |
| Query string | `query` | `text` | - |

---
## Data Table - Cisco AMP computer trajectory

 ![screenshot: dt-cisco-amp-computer-trajectory](./doc/screenshots/dt-cisco-amp-computer-trajectory.png)

#### API Name:
amp_computer_trajectory

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Direction | `direction` | `text` | - |
| Dirty url | `dirty_url` | `text` | - |
| Disposition | `disposition` | `text` | - |
| Event date | `date` | `text` | - |
| Event type | `event_type` | `text` | - |
| File name | `file_name` | `text` | - |
| File path | `file_path` | `text` | - |
| File sha256 | `sha256` | `text` | - |
| File type | `file_type` | `text` | - |
| Hostname | `hostname` | `text` | - |
| Local port | `local_port` | `text` | - |
| Parent sha256 | `parent_sha256` | `text` | - |
| Protocol | `protocol` | `text` | - |
| Query execution time | `query_execution_time` | `text` | - |
| Query string | `query` | `text` | - |
| Remote ip | `remote_ip` | `text` | - |
| Remote port | `remote_port` | `text` | - |

---
## Data Table - Cisco AMP computers

 ![screenshot: dt-cisco-amp-computers](./doc/screenshots/dt-cisco-amp-computers.png)

#### API Name:
amp_computers

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Connector guid | `connector_guid` | `text` | - |
| Connector version | `connector_version` | `text` | - |
| External ip | `external_ip` | `text` | - |
| Group guid | `group_guid` | `text` | - |
| Group name | `group_name` | `text` | - |
| Hostname | `hostname` | `text` | - |
| Install date | `install_date` | `text` | - |
| Internal ips | `internal_ips` | `text` | - |
| Isolation Status | `isolation_status` | `text` | - |
| Last seen | `last_seen` | `text` | - |
| Operating system | `operating_system` | `text` | - |
| Policy name | `policy_name` | `text` | - |
| Query execution time | `query_execution_time` | `text` | - |

---
## Data Table - Cisco AMP event types

 ![screenshot: dt-cisco-amp-event-types](./doc/screenshots/dt-cisco-amp-event-types.png)

#### API Name:
amp_event_types

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Event type description | `event_type_description` | `text` | - |
| Event type id | `event_type_id` | `text` | - |
| Event type name | `event_type_name` | `text` | - |
| Query execution time | `query_execution_time` | `text` | - |

---
## Data Table - Cisco AMP events

 ![screenshot: dt-cisco-amp-events](./doc/screenshots/dt-cisco-amp-events.png)

#### API Name:
amp_events

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Event date | `date` | `text` | - |
| Event id | `event_id` | `text` | - |
| Event type | `event_type` | `text` | - |
| External ip | `external_ip` | `text` | - |
| File disposition | `disposition` | `text` | - |
| File name | `file_name` | `text` | - |
| File path | `file_path` | `text` | - |
| File sha256 | `sha256` | `text` | - |
| Hostname | `hostname` | `text` | - |
| Query Execution time | `query_execution_time` | `text` | - |
| severity | `severity` | `text` | - |

---
## Data Table - Cisco AMP file list files

 ![screenshot: dt-cisco-amp-file-list-files](./doc/screenshots/dt-cisco-amp-file-list-files.png)

#### API Name:
amp_file_list_files

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| File Description | `file_description` | `text` | - |
| File sha256 | `sha256` | `text` | - |
| File source | `source` | `text` | - |
| List guid | `guid` | `text` | - |
| List Name | `list_name` | `text` | - |
| Query execution time | `query_execution_time` | `text` | - |

---
## Data Table - Cisco AMP groups

 ![screenshot: dt-cisco-amp-groups](./doc/screenshots/dt-cisco-amp-groups.png)

#### API Name:
amp_groups

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Description | `group_description` | `text` | - |
| Group guid | `guid` | `text` | - |
| Name | `group_name` | `text` | - |
| Query execution time | `query_execution_time` | `textarea` | - |

---
## Data Table - Cisco AMP Simple Custom Detections  file lists

 ![screenshot: dt-cisco-amp-simple-custom-detections--file-lists](./doc/screenshots/dt-cisco-amp-simple-custom-detections--file-lists.png)

#### API Name:
amp_scd_file_lists

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| List guid | `guid` | `text` | - |
| List name | `list_name` | `text` | - |
| List type | `type` | `text` | - |
| Query execution time | `query_execution_time` | `text` | - |

---



## Rules
| Rule Name | Object | Workflow Triggered | Condition |
| --------- | ------ | ------------------ | ---------- |
| Example: AMP add artifact from activity | amp_activity | `wf_amp_add_artifact_from_activity` | `amp_activity.hostname has_a_value` |
| Example: AMP add artifact from event | amp_events | `wf_amp_add_artifact_from_event` | `amp_events.file_name has_a_value OR amp_events.file_path has_a_value OR amp_events.hostname has_a_value` |
| Example: AMP add artifact from trajectory | amp_computer_trajectory | `wf_amp_add_artifact_from_trajectory` | `-` |
| Example: AMP delete file from list | amp_file_list_files | `wf_amp_delete_file_list_files` | `amp_file_list_files.guid has_a_value AND amp_file_list_files.sha256 has_a_value` |
| Example: AMP get computer (refresh) | amp_computers | `wf_amp_get_computer_refresh` | `-` |
| Example: AMP get computer by connector guid | artifact | `wf_amp_get_computer_by_guid` | `artifact.type equals String` |
| Example: AMP get computer by name | artifact | `wf_amp_get_computer_by_name` | `artifact.type equals DNS Name OR artifact.type equals System Name` |
| Example: AMP get computer trajectory | amp_computers | `wf_amp_get_computer_trajectory` | `amp_computers.hostname has_a_value` |
| Example: AMP get computer trajectory by activity | amp_activity | `wf_amp_get_computer_trajectory_by_activity` | `amp_activity.connector_guid has_a_value AND amp_activity.query has_a_value` |
| Example: AMP get computers with activity | artifact | `wf_amp_get_activity` | `artifact.type equals File Name OR artifact.type equals IP Address OR artifact.type equals Malware SHA-256 Hash OR artifact.type equals URL` |
| Example: AMP get event types | incident | `wf_amp_get_event_types` | `-` |
| Example: AMP get events | incident | `wf_amp_get_events` | `-` |
| Example: AMP get events by type | amp_event_types | `wf_amp_get_events_by_type` | `amp_event_types.event_type_id has_a_value` |
| Example: AMP get files from list | amp_scd_file_lists | `wf_amp_get_file_list_files` | `amp_scd_file_lists.guid has_a_value` |
| Example: AMP get group name by guid | amp_computers | `wf_amp_get_group_name_by_guid` | `amp_computers.hostname has_a_value AND (object_added OR amp_computers.group_guid changed)` |
| Example: AMP get groups | incident | `wf_amp_get_groups` | `-` |
| Example: AMP get SCD file lists | incident | `wf_amp_get_file_lists` | `-` |
| Example: AMP move computer | amp_computers | `wf_amp_move_computer` | `amp_computers.hostname has_a_value` |
| Example: AMP set file in list | artifact | `wf_amp_set_file_list_files` | `artifact.type equals Malware SHA-256 Hash` |

---


## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.
 
### For Support
This is an IBM supported app. Please search [ibm.com/mysupport](https://ibm.com/mysupport) for assistance.
