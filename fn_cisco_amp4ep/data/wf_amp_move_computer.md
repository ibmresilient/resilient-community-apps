<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v52.0.0.0.927
-->

# Example: AMP move computer

## Function - AMP: Get Computers

### API Name
`fn_amp_get_computers`

### Output Name
`get_computers_results`

### Message Destination
`fn_cisco_amp`

### Pre-Processing Script
```python
inputs.amp_hostname = row.hostname
inputs.amp_group_guid = None
inputs.amp_external_ip = None
inputs.amp_internal_ip = None
inputs.amp_limit = None
```

### Post-Processing Script
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
# Processing
response = results.get("response")
noteText = ''

if response is not None and response.get("metadata", {}).get("results", {}).get("total") > 0:
   pass
   # If we get here do nothing result passed on to function 'fn_amp_move_computer' as 'workflow.properties.get_computers_results'
else:
   noteText += "Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for SOAR " \
                "function <b>{0}</b>".format("fn_amp_get_computers")

   incident.addNote(helper.createRichText(noteText))
```

---

## Function - AMP: Get Groups

### API Name
`fn_amp_get_groups`

### Output Name
`get_groups_results`

### Message Destination
`fn_cisco_amp`

### Pre-Processing Script
```python
 # The inputs.amp_group_name  needs to be set to a group name.
# e.g. inputs.amp_group_name = "Int_Test_Group1"
inputs.amp_group_guid = None
inputs.amp_group_name = rule.properties.amp_group_name
inputs.amp_limit = None
```

### Post-Processing Script
```python
##  Cisco AMP for endpoints - fn_amp_get_groups script ##
#  fn_amp_get_groups  -  Event type list
# Example result:
"""
Result:         {
      "response": {
        "version": "v1.2.0",
        "data": [
          {
            "source": null,
            "guid": "abcd1234-a123-b456-c769-abcdef123456",
            "name": "Audit",
            "links": {
              "group": "https://api.amp.cisco.com/v1/groups/abcd1234-a123-b456-c769-abcdef123456"
            },
            "description": "Test Audit Group 1"
          },
          ...
        ],
        "metadata": {
          "results": {
            "index": 0,
            "total": 5,
            "items_per_page": 500,
            "current_item_count": 5
          },
          "links": {
            "self": "https://api.amp.cisco.com/v1/groups"
          }
        }
      },
      "query_execution_time": "2018-10-08 12:49:38"
    }
"""

# Processing
response = results.get("response")
input_params = results.get("input_params")
note_text = ''

if response is not None and response.get("metadata", {}).get("results", {}).get("total") > 0:
   pass
   # If we get here do nothing result passed on to function 'fn_amp_move_computer' as 'workflow.properties.get_groups_results'
else:
   note_text += "Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for group name <b>{0}</b> for SOAR function <b>{1}</b>".format(input_params.get("name",{}), "fn_amp_get_groups")
   incident.addNote(helper.createRichText(note_text))

```

---

## Function - AMP: Move Computer

### API Name
`fn_amp_move_computer`

### Output Name
`None`

### Message Destination
`fn_cisco_amp`

### Pre-Processing Script
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

### Post-Processing Script
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

---

