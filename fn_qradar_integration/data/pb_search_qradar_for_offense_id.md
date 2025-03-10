<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.1.1.824
-->

# Playbook - QRadar SIEM: Get QRadar Offense Events - Example (PB)

### API Name
`search_qradar_for_offense_id`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`incident.properties.qradar_id has_a_value`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| Number of days to search back | `days_to_search_back` | text | Note when populated all results are returned for within this search back time period. | Optional |
| QRadar Query all Results | `qradar_query_all_results` | select | When all results are queried, a  predefined number of results are returned | Optional |
| QRadar Server | `qradar_server` | text | Enter the label given to the QRadar server in the app.config you wish to use | Optional |

### Object Type
`incident`

### Description
Use the qradar_id field of the incident to search qradar events, and update the data table, qradar_offense_event, with the first 5 results.


---
## Function - QRadar SIEM: QRadar Search

### API Name
`qradar_search`

### Output Name
`qradar_search_result`

### Message Destination
`fn_qradar_integration`

### Function-Input Script
```python
inputs.qradar_label = getattr(playbook.inputs, "qradar_server")


if getattr(playbook.inputs, "qradar_query_all_results"):
  inputs.qradar_query_all_results = getattr(playbook.inputs, "qradar_query_all_results")

  
inputs.qradar_query = "SELECT %param1% FROM events WHERE INOFFENSE(%param2%) LAST %param3% Days"
inputs.qradar_search_param1  = "DATEFORMAT(starttime, 'YYYY-MM-dd HH:mm') as StartTime, CATEGORYNAME(category), LOGSOURCENAME(logsourceid), PROTOCOLNAME(protocolid), RULENAME(creeventlist)"
inputs.qradar_search_param2 = incident.properties.qradar_id
if getattr(playbook.inputs, "days_to_search_back"): 
  inputs.qradar_search_param3 = getattr(playbook.inputs, "days_to_search_back")
else:
  inputs.qradar_search_param3 = '7'
inputs.qradar_query_range_start = '1'
inputs.qradar_query_range_end = '5'

```

---

## Local script - qradar_search_post_process

### Description


### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.qradar_search_result
from datetime import datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for event in results.get("events"):
  qradar_event = incident.addRow("qradar_offense_event")
  qradar_event.query_time = current_time
  qradar_event.qradar_server = results.get("inputs", {}).get("qradar_label")
  qradar_event.start_time = event.get("StartTime")
  qradar_event.category = event.get("categoryname_category")
  qradar_event.log_source = event.get("logsourcename_logsourceid")
  qradar_event.protocol = event.get("protocolname_protocolid")
  qradar_event.rule = event.get("rulename_creeventlist")
if getattr(playbook.inputs, "days_to_search_back"):
  incident.addNote("QRadar SIEM: Get QRadar Offense Events: {} events have successfully been queried for the last {} days".format(len(results.get("events")), getattr(playbook.inputs,"days_to_search_back")))
else:
  incident.addNote("QRadar SIEM: Get QRadar Offense Events: {} events have successfully been queried for the last 7 days".format(len(results.get("events"))))


```

---

