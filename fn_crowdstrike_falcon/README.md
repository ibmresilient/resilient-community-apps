# CrowdStrike Falcon Functions for IBM Resilient

## Table of Contents

---

**This package contains 2 functions that help you integrate with CrowdStrike Falcon APIs**

 ![screenshot](./screenshots/0.png)

CS Falcon: Search gives you the ability to search your CrowdStrike Falcon platform for a list of Devices, then using the CS Falcon: Device Actions function we can 'contain' or 'lift_containment' on that device

---
## app.config settings:
* At time of development, CrowdStrike Falcon are currently in the process of migrating their APIs. Therefore we are required to provide two different sets of credentials: **API Client** and **API Key**
* See their documentation here [https://falcon.crowdstrike.com/support/documentation/1/crowdstrike-api-introduction-for-developers#before_you_begin](https://falcon.crowdstrike.com/support/documentation/1/crowdstrike-api-introduction-for-developers#before_you_begin) on how to obtain your two sets of API Credentials
* Also, the `base_url` may be different depending on your environment. Below are the common `base_urls` used for each set of credentials
```
[fn_crowdstrike_falcon]

# API Client Authentication, CrowdStrike's newer standard based on OAuth2
cs_falcon_oauth2_base_url=https://api.crowdstrike.com
cs_falcon_oauth2_cid=
cs_falcon_oauth2_key=

# API Key Authentication, CrowdStrike's legacy authentication standard
cs_falcon_bauth_base_url=https://falconapi.crowdstrike.com
cs_falcon_bauth_api_uuid=
cs_falcon_bauth_api_key=
```

---
## Function - CS Falcon: Search:
Queries your CrowdStrike Falcon Hosts for a list of Devices using a Filter and/or Query. If Devices are found they are returned as a Python List

 ![screenshot](./screenshots/1.png)


### Inputs:
| Name | Type | Required | Example | Info |
| ------------- | :--: | :-------:| ------- | ---- |
| `cs_filter_string` | `String` | No | `"hostname:'{0}*'+platform_name:'{1}'".format(artifact.value, "Linux")` | See: [https://falcon.crowdstrike.com/support/documentation/2/query-api-reference#devicesearch](https://falcon.crowdstrike.com/support/documentation/2/query-api-reference#devicesearch) for filter syntax |
| `cs_query` | `String` | No | `"JohnsMacBook"` | This query searches the meta data of devices after applying the above filter. Here it would search all fields for "JohnsMacBook" |


### Output:
```python
results = {
    "success": True,
    "reason": None,
    "version": "1.0",
    "metrics": {
        "package": "fn-crowdstrike-falcon",
        "timestamp": "2019-02-11 13:23:43",
        "package_version": "1.0.0",
        "host": "localhost",
        "version": "1.0",
        "execution_time_ms": 1619
    },
    "inputs": {
        "cs_query": None,
        "cs_filter_string": "hostname:'localhost*'"
    },
    "content": [{
        "modified_timestamp": 1549891335000,
        "config_id_platform": "8",
        "system_manufacturer": "innotek GmbH",
        "meta": {
            "version": "295"
        },
        "first_seen": 1549548472000,
        "platform_id": "3",
        "local_ip": "192.168.63.3",
        "hostname": "localhost.localdomain",
        "config_id_build": "6703",
        "minor_version": "10",
        "os_version": "CentOS 7",
        "provision_status": "Provisioned",
        "mac_address": "0-0-0-0-0",
        "bios_version": "VirtualBox",
        "agent_load_flags": "0",
        "status": "normal",
        "bios_manufacturer": "innotek GmbH",
        "product_type_desc": "Server",
        "device_policies": {
            "sensor_update": {
                "applied": True,
                "applied_date": "2019-02-07T14:09:24.94667175Z",
                "settings_hash": "65994753|8|2|automatic",
                "policy_type": "sensor-update",
                "assigned_date": "2019-02-07T14:09:24.946671267Z",
                "policy_id": "4eac5ba86b27414098820732fe7876f6"
            },
            "prevention": {
                "applied": True,
                "applied_date": "2019-02-08T14:47:54.526691595Z",
                "settings_hash": "d4cbb29",
                "policy_type": "prevention",
                "assigned_date": "2019-02-08T14:47:47.25675937Z",
                "policy_id": "25291d90954c476d86c6fb2db38d7d72"
            }
        },
        "agent_local_time": 1549859544549,
        "slow_changing_modified_timestamp": "2019-02-11T13:22:15Z",
        "device_id": "606e693c6ac040107c07dcc7c7ed6785",
        "system_product_name": "VirtualBox",
        "cid": "b1e43228990c4bfe8e979969d955b800",
        "external_ip": "0.0.0.0",
        "major_version": "3",
        "platform_name": "Linux",
        "config_id_base": "65994753",
        "policies": [{
            "applied": True,
            "applied_date": "2019-02-08T14:47:54.526691595Z",
            "settings_hash": "d4cbb29",
            "policy_type": "prevention",
            "assigned_date": "2019-02-08T14:47:47.25675937Z",
            "policy_id": "25291d90954c476d86c6fb2db38d7d72"
        }],
        "agent_version": "4.21.6703.0",
        "last_seen": 1549891334000
    }]
}
```

### Pre-Process Script:
This example uses the Artifact Value to create the `cs_filter_string`
```python
# Example: "hostname:'sampleName*'+platform_name:'Windows'" ==> Searches CrowdStrike for devices who's hostname contains 'sampleName' and platform is 'Windows'
inputs.cs_filter_string = "hostname:'{0}*'".format(artifact.value)

# This query searches the meta data of devices after applying the above filter
inputs.cs_query = "JohnsMacBook"
```
### Post-Process Script:
This post-process loops each found device and adds its details to the `cs_falcon_devices_dt` Data Table
```python
# If the function found some devices
if results.success:

# For each device, add a row to the cs_falcon_devices_dt
for device in results.content:
    new_row = incident.addRow("cs_falcon_devices_dt")
    new_row.device_id = device.device_id
    new_row.hostname = device.hostname
    new_row.ip = device.local_ip
    new_row.mac = device.mac_address
    new_row.last_seen = device.last_seen
    new_row.status = device.status

else:
# Else, no devices found, add Note to Incident with reason
    incident.addNote(results.reason)
```

---

## Function - CS Falcon: Device Actions:
Function that uses the CrowdStrike Falcon '/devices/entities/devices-actions/' endpoint to Contain or Lit Containment on a Device

**Contain Device:**

 ![screenshot](./screenshots/2.png)
 
**Lift Containment:**

 ![screenshot](./screenshots/3.png)



### Inputs:
| Name | Type | Required | Example | Info |
| ------------- | :--: | :-------:| ------- | ---- |
| `cs_device_id` | `String` | Yes | `"b1e43228990c4bfe8e979969d955b800"` | This is a unique ID CrowdStrike Falcon assigns all its devices |
| `cs_action_name` | `Select` | Yes | Select Options: `contain` or `lift_containment` | The name of the action to run on the device. Currently the CrowdStrike Falcon APIs support 'contain' and 'lift_containment'. See [https://assets.falcon.crowdstrike.com/support/api/swagger.html](https://assets.falcon.crowdstrike.com/support/api/swagger.html) for more |


### Output:
```python
results = {
    "success": True,
    "reason": None,
    "version": "1.0",
    "inputs": {
        "cs_device_id": "606e693c6ac040107c07dcc7c7ed6785",
        "cs_action_name": "contain"
    },
    "metrics": {
        "package": "fn-crowdstrike-falcon",
        "timestamp": "2019-02-11 13:42:16",
        "package_version": "1.0.0",
        "host": "localhost",
        "version": "1.0",
        "execution_time_ms": 3920
    },
    "content": {
        "meta": {
            "query_time": 0.725871979,
            "trace_id": "349764c9-721f-4a90-bc48-74d793c0e151",
            "powered_by": "device-api"
        },
        "device_id": "606e693c6ac040107c07dcc7c7ed6785"
    }
}
```

### Pre-Process Script:
This example is using a Workflow with a Data Table Object Type. Therefore it can get the device_id from the row this Rule was invoked on
```python
# Set the unique CrowdStrike device_id. Taken here from the CS Falcon: Devices Data Table
inputs.cs_device_id = row.device_id

# inputs.cs_action_name is a select field and is set to "contain" in the Workflow's Input tab
```
### Post-Process Script:
This post-process adds a Note to the Incident
```python
# If the function successfully sent a "contain device" or "lift_containment" request to CrowdStrike, add a Note to the Incident
if results.success:
  note_text = """<br><b>device-action request sent to CrowdStrike</b>
                 <br><b>Action:</b> {0}
                 <br><b>Device ID:</b> {1}""".format(results.inputs.cs_action_name, results.content.device_id)

  incident.addNote(helper.createRichText(note_text))
```

---
## Rules
| Rule Name | Object Type | Conditions | Workflow Triggered |
| --------- | :---------: | ---------- | ------------------ |
| Example: CS Falcon: Search | `Artifact` | `None` | `Example: CS Falcon: Search` |
| Example: CS Falcon: Contain Device | `Data Table` | `cs_falcon_devices_dt.device_id` must have a value | `Example: CS Falcon: Contain Device` |
| Example: CS Falcon: Lift Containment | `Data Table` | `cs_falcon_devices_dt.device_id` must have a value | `Example: CS Falcon: Lift Containment` |
| Example: CS Falcon: Get Latest Device Details | `Data Table` | `cs_falcon_devices_dt.device_id` must have a value | `Example: CS Falcon: Get Latest Device Details` |

---
## Data table
### CS Falcon: Devices
 ![screenshot](./screenshots/dt_0.png)

#### API Name:
cs_falcon_devices_dt

#### Columns:
| Column Name | API Access Name | Type |
| ----------- | --------------- | -----|
| Device ID | `device_id` | `Text` |
| Hostname | `hostname` | `Text` |
| IP | `ip` | `Text` |
| MAC | `mac` | `Text` |
| Last Seen | `last_seen` | `Text` |
| Status | `status` | `Text` |


#### Display the Datatable in an Incident
* In order to **display** the Test Data Table in your Incident, you must **modify your Layout Settings**

1. Go to **Customization Settings** > **Layouts** > **Incident Tabs** > **+ Add Tab**
   
 ![screenshot](./screenshots/dt_1.png)

2. Enter **Tab Text**: `My Test Tab` and click **Add**
 
 ![screenshot](./screenshots/dt_2.png)

3. **Drag** the Data table into the middle and click **Save**
 
 ![screenshot](./screenshots/dt_3.png)

4. Create a new Incident and you will now see the **My Test Tab** with the **Test Data Table**
