<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v52.0.0.0.927
-->

# Example: AMP get computer by connector guid

## Function - AMP: Get Computer

### API Name
`fn_amp_get_computer`

### Output Name
``

### Message Destination
`fn_cisco_amp`

### Pre-Processing Script
```python
inputs.amp_conn_guid = artifact.value
```

### Post-Processing Script
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
response = results.response
input_params =  results.input_params
query_execution_time = results.query_execution_time
noteText = ''
errors = response.get("errors", None)

if response is not None and errors is None:
    data = response["data"]
    noteText = "Cisco AMP for Endpoints Integration: Result returned for computer <b>{0}</b> with connector guid " \
               "<b>{1}</b> for Resilient function <b>{2}</b>"\
        .format(data["hostname"], data["connector_guid"], "fn_amp_get_computers")
    newrow = incident.addRow("amp_computers")
    newrow.query_execution_time = query_execution_time
    for f in DATA_TBL_FIELDS:
        if f == "query_execution_time" or "policy" in f:
            continue
        if isinstance(data[f], str) or len(data[f]) == 0:
            newrow[f] = data[f]
        else:
            newrow[f] = ','.join(data[f])
    policy = data["policy"]
    if policy is not None:
        newrow.policy_name = policy["name"]
elif errors is not None and errors[0]["error_code"] == 404:
    noteText += "Cisco AMP for Endpoints Integration: Got a 404 error while attempting to get computer information for " \
                "connector guid <b>{0}</b> for function <b>{1}</b> because of a possible invalid or deleted guid."\
        .format(input_params["conn_guid"], "fn_amp_get_computers")
else:
    noteText += "Cisco AMP for Endpoints Integration: There were <b>no</b> results returned for SOAR " \
                "function <b>{0}</b>".format("fn_amp_get_computers")

incident.addNote(helper.createRichText(noteText))
```

---

