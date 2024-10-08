<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v52.0.0.0.927
-->

# Example: AMP get event types

## Function - AMP: Get Event Types

### API Name
`fn_amp_get_event_types`

### Output Name
``

### Message Destination
`fn_cisco_amp`

### Pre-Processing Script
```python
None
```

### Post-Processing Script
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

---

