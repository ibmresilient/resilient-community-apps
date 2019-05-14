# IBM Resilient Integration for MaaS360

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Install & Customize](#install--customize)
- [App Config Settings](#appconfig-settings)
- [Functions](#functions)

# Overview
The MaaS360 function package enables users to perform certain Mobile device management (MDM) actions. Users can perform a basic device search, get software installed for a device, locate, lock, wipe a device, cancel pending wipe, delete an app from the MaaS360 catalog and stop app distributions across different target devices.

---

# Requirements
* IBM Resilient >= `v31.0.0`
* An Integrations Server running `resilient-circuits >= v31.0.0` with `fn_maas360 >= v1.0.0` installed which you can download from our [App Exchange](xxxxxxx)

---

# Install & Customize
* You download the function package to a Resilient integration server, and from there you deploy the functions and components to a Resilient platform. These procedures are provided in the [Resilient SOAR Integration Server Guide (PDF)](https://github.com/ibmresilient/resilient-reference/blob/master/developer_guides/Integration%20Server%20Guide.pdf).
*This guide provides a description of the functions and components within the function package, any additional requirements, and a list of settings that need to be added to the Resilient Circuits app.config file.

---

# Documentation
* See the accompanying documentation Resilient Functions User Guide for MaaS360.pdf for how to use the function.

---

# App Config Settings (app.config):

```
[fn_maas360]
# Authentication settings
maas360_host_url=
maas360_billing_id=
maas360_platform_id=
maas360_app_id=
maas360_app_version=
maas360_app_access_key=
maas360_username=
maas360_password=
maas360_auth_url=/auth-apis/auth/1.0/authenticate/

# Basic Search Fn settings
maas360_basic_search_url=/device-apis/devices/2.0/search/customer/
# Limit number of devices returned at one time. Allowed page sizes: 25, 50, 100, 200, 250. Default value: 250
maas360_basic_search_page_size=25
# Optional - Match 0 (Default) indicates Partial match for Device Name, Username, Phone Number. Match 1 indicates Exact match.
#maas360_basic_search_match=0
# Optional - Sort attribute. Possible values: lastReported (Default) or installedDate
#maas360_basic_search_sort_attribute=lastReported
# Optional - Sort Order. Possible values: asc or dsc (Default)
#maas360_basic_search_sort_order=dsc

# Action Fn settings
maas360_locate_device_url=/device-apis/devices/1.0/locateDevice/
maas360_get_software_installed_url=/device-apis/devices/1.0/softwareInstalled/
maas360_lock_device_url=/device-apis/devices/1.0/lockDevice/
maas360_wipe_device_url=/device-apis/devices/1.0/wipeDevice/
# Required - Whether to notify the administrator on successful device wipe. “yes” value enables this flag
maas360_wipe_device_notify_me=Yes
# Required - Whether to notify the user on successful device wipe. “yes” value enables this flag.
maas360_wipe_device_notify_user=No
# Required - Comma separated list of other email addresses to notify on successful device wipe
maas360_wipe_device_notify_others=email1, email2
maas360_cancel_pending_wipe_url= /device-apis/devices/1.0/cancelPendingWipe/

# Stop App Distribution Fn settings
maas360_stop_app_distribution_url=/application-apis/applications/1.0/stopAppDistribution/

# Delete App Fn settings
maas360_delete_app_url=/application-apis/applications/1.0/deleteApp/

# Search Installed Apps Fn settings
maas360_search_installed_apps_url=/application-apis/installedApps/1.0/search/
# Limit number of devices returned at one time. Allowed page sizes: 25, 50, 100, 200, 250. Default value: 50
maas360_search_installed_apps_page_size=50
```
# Functions:
    
## MaaS360 Basic Search Function
Function searches for devices by Device Name, Username, Phone Number, Platform, Device Status and other Device Identifiers.

### Inputs:
| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| ` maas360_partial_device_name` | `String` | No | `Jane's iPhone` | Partial (Starts with) or full Device Name string that needs to be searched for |
| `maas360_partial_username` | `String` | No | `jane@example.com` | Partial (Starts with) or full Username string that needs to be searched for |
| ` maas360_partial_phone_no ` | `String` | No | `+16175000000` | Partial (Starts with) or full Phone Number that needs to be searched for |
| ` maas360_platform_name` | `Select` | No | `Windows,  Mac , iOS,  BlackBerry,  Android , Windows Mobile,  Symbian,  Windows Phone 7,  Others` | Platform name |
| ` maas360_device_id` | `String` | No | `ApplD8DTH6RCIH86` | Full MaaS360 Device ID string that needs to be searched for |
| ` maas360_email` | `String` | No | `jane@example.com` | Full Email address string that needs to be searched for |

### Outputs:
MaaS360 integrations uses resilient-lib Python module to generate results.

```python
{
    "content": {
        "count": 1,
        "device": {
            "appComplianceState": "In Compliance",
            "customAssetNumber": "",
            "deviceName": "dummy_device@gmail.com-STV100-1",
            "deviceOwner": "",
            "deviceStatus": "Active",
            "deviceType": "Smartphone",
            "emailAddress": "dummy_device@gmail.com",
            "encryptionStatus": "Encryption Complete",
            "firstRegisteredInEpochms": 1549629133338,
            "imeiEsn": 351623070066166,
            "installedDate": "2019-02-08T12:32:13",
            "installedDateInEpochms": 1549629133338,
            "isSupervisedDevice": False,
            "jailbreakStatus": "No",
            "lastMdmRegisteredInEpochms": 1549629133378,
            "lastRegisteredInEpochms": 1549629133338,
            "lastReported": "2019-04-23T16:11:23",
            "lastReportedInEpochms": 1556035883843,
            "maas360DeviceID": "Androiddeviceid",
            "maas360ManagedStatus": "Enrolled",
            "mailboxDeviceId": "",
            "mailboxLastReported": "",
            "mailboxLastReportedInEpochms": "",
            "mailboxManaged": "",
            "manufacturer": "blackberry",
            "mdmMailboxDeviceId": "",
            "model": "STV100-1",
            "osName": "Android 6.0.1 (MMB29M)",
            "osServicePack": "",
            "osVersion": "6.0.1",
            "ownership": "Corporate Owned",
            "passcodeCompliance": "Compliant",
            "phoneNumber": "",
            "platformName": "Android",
            "policyComplianceState": "In Compliance",
            "ruleComplianceState": "",
            "selectiveWipeStatus": "N/a",
            "sourceID": 1,
            "testDevice": False,
            "udid": "Androiddeviceid",
            "unifiedTravelerDeviceId": "Androiddeviceid",
            "userDomain": "gmail.com",
            "username": "dummy_device@gmail.com",
            "wifiMacAddress": "a4:e4:b8:73:a1:93"
        },
        "pageNumber": 1,
        "pageSize": 1
    },
    "inputs": {
        "maas360_device_id": "Androiddeviceid",
        "maas360_email": None,
        "maas360_imei_meid": None,
        "maas360_partial_device_name": None,
        "maas360_partial_phone_no": None,
        "maas360_partial_username": None,
        "maas360_platform_name": None
    },
    "metrics": {
        "execution_time_ms": 9864,
        "host": "host",
        "package": "fn-maas360",
        "package_version": "1.0.0",
        "timestamp": "2019-05-13 13:21:40",
        "version": "1.0"
    },
    "raw": "raw_json_string",
    "reason": None,
    "success": True,
    "version": "1.0"
}
```
Example of output with two or more devices found:
```
    "content": {
        "device": [{
                "maas360DeviceID": "deviceId1",
                "deviceName": "name",
                "username": "username",
                "platformName": "Android",
                "deviceType": "Smartphone",
                "lastReported": "2011-05-09T17:13:15",
                "deviceStatus": "Active",
                ...},
            {
                "maas360DeviceID": "deviceId2",
                "deviceName": "name",
                "username": "username",
                "platformName": "Android",
                "deviceType": "Smartphone",
                "lastReported": "2011-05-09T17:13:15",
                "deviceStatus": "Active",
            ...}],
        "count": 2,
        "pageNumber": 1,
        "pageSize": 1
        }
```
### Pre-Process Script:
```python
inputs.maas360_device_id = rule.properties.maas360_rule_device_id if rule.properties.maas360_rule_device_id is not None else inputs.maas360_device_id
inputs.maas360_partial_device_name = rule.properties.maas360_rule_device_name if rule.properties.maas360_rule_device_name is not None else inputs.maas360_partial_device_name
inputs.maas360_email = rule.properties.maas360_rule_email if rule.properties.maas360_rule_email is not None else inputs.maas360_email
inputs.maas360_imei_meid = rule.properties.maas360_rule_imei_meid if rule.properties.maas360_rule_imei_meid is not None else inputs.maas360_imei_meid
inputs.maas360_partial_phone_no = rule.properties.maas360_rule_phone_no if rule.properties.maas360_rule_phone_no is not None else inputs.maas360_partial_phone_no
inputs.maas360_platform_name = rule.properties.maas360_rule_platform_name if rule.properties.maas360_rule_platform_name is not None else inputs.maas360_platform_name
inputs.maas360_partial_username = rule.properties.maas360_rule_username if rule.properties.maas360_rule_username is not None else inputs.maas360_partial_username
```
### Post-Process Script
```python
from java.util import Date

def add_row(device):
  device_dt = incident.addRow("maas360_device_dt")
  device_dt.maas360_timestamp = Date()
  device_dt.maas360_deviceid = device.get("maas360DeviceID")
  device_dt.maas360_devicename = device.get("deviceName")
  device_dt.maas360_username = device.get("username")
  device_dt.maas360_platformname = device.get("platformName")
  device_dt.maas360_devicetype = device.get("deviceType")
  device_dt.maas360_lastreported = device.get("lastReported")
  device_dt.maas360_devicestatus = device.get("deviceStatus")

# Print empty string instead of None
def string_value(value):
  return value if value is not None else ""

def add_results_note(inputs, number_devices_found):
  noteText = u"""{} device/s found in MaaS360 database with search parameters: 
    - partialDeviceName: '{}' 
    - partialUsername: '{}'
    - partialPhoneNumber: '{}'
    - imeiMeid: '{}'
    - platformName: '{}'
    - maas360DeviceId: '{}'
    - email: '{}'""".format(
      number_devices_found,
      string_value(inputs.get("maas360_partial_device_name")), 
      string_value(inputs.get("maas360_partial_username")), 
      string_value(inputs.get("maas360_partial_phone_no")), 
      string_value(inputs.get("maas360_imei_meid")),
      string_value(inputs.get("maas360_platform_name").get("name")) if inputs.get("maas360_platform_name") else "",
      string_value(inputs.get("maas360_device_id")),
      string_value(inputs.get("maas360_email"))
      )
  incident.addNote(noteText)

########################
# Mainline starts here #
########################

if results and results.get("success"):
  count = 0
  content = results.get("content")
  if content:
    count = content.get("count")
    if count > 0:
      # Add a row for each Device found
      devices_list = [content.get("device")] if count == 1 else content.get("device")
      map(lambda device: add_row(device), devices_list)
  
  # Write results to a Note
  inputs = results.get("inputs")
  add_results_note(inputs, count)
```
## MaaS360 Action
MaaS360 Function performs different actions based on the chosen Menu Item Rule. 

Available actions are: 
- Locate Device
- Get Software Installed
- Lock Device 
- Wipe Device 
- Cancel Pending Wipe

### Inputs:
| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| ` maas360_device_id` | `String` | Yes | `ApplD8DTH6RCIH86` | Full MaaS360 Device ID string that needs to be searched for |
| ` maas360_action_type` | `Select` | Yes | `Get Software Installed, Locate Device, Lock Device, Wipe Device, Cancel Pending Wipe` | Action |

### MaaS360 Action - Locate Device
Function that performs a real-time lookup on Android devices or  provides Last Known location on iOS and Windows Phone devices. The results is latitude and longitude information.

### Pre-Process Script:
```python
inputs.maas360_device_id = artifact.value
```
### Post-Process Script:
```python
########################
# Mainline starts here #
########################

if results and results.get("success"):
  content = results.get("content")
  if content:
    latitude = content.get("latitude")
    longitude = content.get("longitude")
    device_id = content.get("maas360DeviceID")
    
    if latitude and longitude:
      noteText = u"Current or last know location for Device ID {} is {} latitude, {} longitude.".format(device_id, latitude, longitude)
      incident.addNote(noteText)
    else:
      noteText = u"There is no current or last know location available for Device ID {}.".format(device_id)
      incident.addNote(noteText)
```
### Outputs:
```python
{
    "content": {
        "actionStatus": 0,
        "description": "The action was executed successfully on the device.",
        "latitude": 25.005112,
        "locatedTime": "2019-05-13 17:45:12.0",
        "longitude": 121.541535,
        "maas360DeviceID": "deviceid"
    },
    "inputs": {
        "maas360_action_type": {
            "id": 202,
            "name": "Locate Device"
        },
        "maas360_device_id": "deviceid"
    },
    "metrics": {
        "execution_time_ms": 951,
        "host": "host",
        "package": "fn-maas360",
        "package_version": "1.0.0",
        "timestamp": "2019-05-13 15:18:51",
        "version": "1.0"
    },
    "raw": "raw_json_string",
    "reason": None,
    "success": True,
    "version": "1.0"
}
 ```
## MaaS360 Action - Get Software Installed
Function that gets installed software for a device.

### Pre-Process Script:
```python
inputs.maas360_device_id = artifact.value
```
### Post-Process Script:
```python
from java.util import Date

def add_row(device_id, app_Name, app_version, app_id, refresh_date):
  app_dt = incident.addRow("maas360_installed_software_datatable")
  app_dt.maas360_app_timestamp = Date()
  app_dt.maas360_app_device_id = device_id
  app_dt.maas360_app_app_name = app_Name
  app_dt.maas360_app_app_version = app_version
  app_dt.maas360_app_app_id = app_id
  app_dt.maas360_app_lastSoftwareDataRefreshDate = refresh_date
  
########################
# Mainline starts here #
########################

if results and results.get("success"):
  content = results.get("content")
  if content:
    device_id = content.get("maas360DeviceID")
    refresh_date = content.get("lastSoftwareDataRefreshDate")
    
    found_apps = False
    apps = content.get("deviceSw")
    if apps:
      for app in apps:
        if app:
          app_Name = app.get("swName")
          app_attrs = app.get("swAttrs")
          if app_Name and app_attrs:
            app_version_attr = filter(lambda att: att["key"] == 'Version', app_attrs)
            # filter returns a list [{u'type': u'string', u'key': u'Version', u'value': u'3.70.111'}]
            app_version = str(app_version_attr[0].get("value")) if app_version_attr else "N/A" 
            
            app_app_id_attr = filter(lambda att: att["key"] == 'Application ID', app_attrs)
            # filter returns a list [{u'type': u'string', u'key': u'Application ID', u'value': u'com.fiberlink.maas360forios'}]
            app_id = app_app_id_attr[0].get("value") if app_app_id_attr else "N/A" 
              
            # write results in the app datatable
            add_row(device_id, app_Name, app_version, app_id, refresh_date)
            found_apps = True
            
  if found_apps:
    noteText = u"Installed software was found for the Device ID {} and saved in the MaaS360 Installed Software datatable".format(device_id)
    incident.addNote(noteText)
  else:
    noteText = u"No installed software found for the Device ID {}".format(device_id)
    incident.addNote(noteText)
```
### Outputs:
```python
{
    "content": {
        "deviceSw": [
            {
                "swAttrs": [
                    {
                        "key": "Application ID",
                        "type": "string",
                        "value": "com.fiberlink.maas360forios"
                    },
                    {
                        "key": "Version",
                        "type": "string",
                        "value": 3.70.111
                    },
                    {
                        "key": "AppDataSize",
                        "type": "string",
                        "value": 3.79
                    },
                    {
                        "key": "File Size",
                        "type": "string",
                        "value": 175.18
                    },
                    {
                        "key": "Installed by MDM",
                        "type": "string",
                        "value": "Manage Status"
                    }
                ],
                "swName": "MaaS360"
            },
            {
                "swAttrs": [
                    {
                        "key": "Application ID",
                        "type": "string",
                        "value": "com.blackberry.ddt.bugreporter"
                    },
                    {
                        "key": "Version",
                        "type": "string",
                        "value": 1
                    },
                    {
                        "key": "AppDataSize",
                        "type": "string",
                        "value": 0
                    },
                    {
                        "key": "File Size",
                        "type": "string",
                        "value": 0
                    },
                    {
                        "key": "Install Location",
                        "type": "string",
                        "value": "Internal"
                    }
                ],
                "swName": "BlackBerry Bug Reporter"
            }
        ],
        "lastSoftwareDataRefreshDate": "2019-04-18T00:13:07",
        "maas360DeviceID": "deviceid"
    },
    "inputs": {
        "maas360_action_type": {
            "id": 201,
            "name": "Get Software Installed"
        },
        "maas360_device_id": "deviceid"
    },
    "metrics": {
        "execution_time_ms": 13019,
        "host": "host",
        "package": "fn-maas360",
        "package_version": "1.0.0",
        "timestamp": "2019-05-13 13:48:43",
        "version": "1.0"
    },
    "raw": "raw_json_string",
    "reason": None,
    "success": True,
    "version": "1.0"
}
```
### MaaS360 Action - Lock Device
Function that locks a device.

### Pre-Process Script:
```python
inputs.maas360_device_id = artifact.value
```
### Post-Process Script:
```python
########################
# Mainline starts here #
########################

if results and results.get("success"):
  content = results.get("content")
  if content:
    noteText = u"Lock Device for Device ID: {}. {}".format(content.get("maas360DeviceID"), content.get("description"))
    incident.addNote(noteText)
```
### Outputs:
```python
{
    "content": {
        "actionID": 128294549,
        "actionStatus": 0,
        "description": "The action was executed successfully on the device.",
        "maas360DeviceID": "deviceid"
    },
    "inputs": {
        "maas360_action_type": {
            "id": 203,
            "name": "Lock Device"
        },
        "maas360_device_id": "deviceid"
    },
    "metrics": {
        "execution_time_ms": 558,
        "host": "host",
        "package": "fn-maas360",
        "package_version": "1.0.0",
        "timestamp": "2019-05-13 15:27:03",
        "version": "1.0"
    },
    "raw": "raw_json_string",
    "reason": None,
    "success": True,
    "version": "1.0"
}
```
### MaaS360 Action - Wipe Device
Function that performs a remote Wipe of the device.

### Pre-Process Script:
```python
inputs.maas360_device_id = artifact.value
```
### Post-Process Script:
```python
########################
# Mainline starts here #
########################

if results and results.get("success"):
  content = results.get("content")
  if content:
    noteText = u"Wipe Device for Device ID: {}. {}".format(content.get("maas360DeviceID"), content.get("description"))
    incident.addNote(noteText)
```
### Outputs:
```python
"content": {
        "actionID": 128294785,
        "actionStatus": 0,
        "description": "The action was executed successfully on the device.",
        "maas360DeviceID": "deviceid"
    },
    "inputs": {
        "maas360_action_type": {
            "id": 204,
            "name": "Wipe Device"
        },
        "maas360_device_id": "deviceid"
    },
    "metrics": {
        "execution_time_ms": 669,
        "host": "host",
        "package": "fn-maas360",
        "package_version": "1.0.0",
        "timestamp": "2019-05-13 15:30:33",
        "version": "1.0"
    },
    "raw": "raw_json_string",
    "reason": None,
    "success": True,
    "version": "1.0"
}
```
### MaaS360 Action - Wipe Device
Function that cancels outstanding Remote Wipe sent to the device.

### Pre-Process Script:
```python
inputs.maas360_device_id = artifact.value
```
### Post-Process Script:
```python
########################
# Mainline starts here #
########################

if results and results.get("success"):
  content = results.get("content")
  if content:
    noteText = u"Cancel Pending Wipe for Device ID: {}. {}".format(content.get("maas360DeviceID"), content.get("description"))
    incident.addNote(noteText)
```
### Outputs:
```python
{
    "content": {
        "actionID": 128294800,
        "actionStatus": 0,
        "description": "The action was executed successfully on the device.",
        "maas360DeviceID": "deviceid"
    },
    "inputs": {
        "maas360_action_type": {
            "id": 205,
            "name": "Cancel Pending Wipe"
        },
        "maas360_device_id": "deviceid"
    },
    "metrics": {
        "execution_time_ms": 915,
        "host": "host",
        "package": "fn-maas360",
        "package_version": "1.0.0",
        "timestamp": "2019-05-13 15:30:52",
        "version": "1.0"
    },
    "raw": "raw_json_string",
    "reason": None,
    "success": True,
    "version": "1.0"
}
```
## MaaS360 Stop App Distribution
Function that stops a specific distribution of an app on target devices.

### Inputs:
| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| ` maas360_device_id` | `String` | Yes | `ApplD8DTH6RCIH86` | Full MaaS360 Device ID string that needs to be searched for |
| ` maas360_action_type` | `Select` | Yes | `Get Software Installed, Locate Device, Lock Device, Wipe Device, Cancel Pending Wipe` | Action |

### Outputs:

### Pre-Process Script:

### Post-Process Script:

## MaaS360 Delete App
Function that stops all distributions of the app and deletes the app.

### Inputs:
| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| ` maas360_device_id` | `String` | Yes | `ApplD8DTH6RCIH86` | Full MaaS360 Device ID string that needs to be searched for |
| ` maas360_action_type` | `Select` | Yes | `Get Software Installed, Locate Device, Lock Device, Wipe Device, Cancel Pending Wipe` | Action |

### Outputs:

### Pre-Process Script:

### Post-Process Script: