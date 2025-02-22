<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v52.0.0.0.927
-->

# Example: AMP get events

## Function - AMP: Get Events

### API Name
`fn_amp_get_events`

### Output Name
``

### Message Destination
`fn_cisco_amp`

### Pre-Processing Script
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

### Post-Processing Script
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

---

