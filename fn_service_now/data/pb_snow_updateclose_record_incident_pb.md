<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Playbook - SNOW: Update/Close Incident (PB)

### API Name
`snow_updateclose_record_incident_pb`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`incident.properties.sn_snow_record_id has_a_value AND incident.properties.sn_snow_table_name equals incident`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| SN Close Code | `sn_close_code` | select | Optional. Sets the close code only when Record State is CLOSED | Optional |
| SN Close Notes | `sn_close_notes` | text | Optional. Note to be added to record when state is CLOSED | Optional |
| SN Record State | `sn_record_state` | select | - | Always |

### Object Type
`incident`

### Description
Update the state of this record in the incident table in ServiceNow


---
## Function - SNOW: Close Record

### API Name
`fn_snow_close_record`

### Output Name
`close_record`

### Message Destination
`fn_service_now`

### Function-Input Script
```python
# A Dictionary that maps Record States to their corresponding codes
# These codes are defined in ServiceNow and may be different for each ServiceNow configuration
# Codes prepended with [SIR] are specific to Security Incident Response incidents
map_sn_record_states = {
  "New": 1,
  "In Progress": 2,
  "On Hold": 3,
  "Resolved": 6,
  "Closed": 7,
  "Canceled": 8,
  "Cancelled": 8 # servicenow has inconsistent spellings of this word...
}

# ID of this incident
inputs.incident_id = incident.id

# The state to change the record to
# inputs.sn_record_state = map_sn_record_states["Closed"]
inputs.sn_record_state = map_sn_record_states[getattr(playbook.inputs, "sn_record_state", None)]

# The resolution notes that are normally required when you close a ServiceNow record
# inputs.sn_close_notes = "This incident has been resolved in IBM SOAR. No further action required"
if getattr(playbook.inputs, "sn_close_notes", None):
  inputs.sn_close_notes = getattr(playbook.inputs, "sn_close_notes", None)

# The ServiceNow 'close_code' that you normally select when closing a ServiceNow record
# inputs.sn_close_code = "Solved (Permanently)"
if getattr(playbook.inputs, "sn_close_code", None):
  inputs.sn_close_code = getattr(playbook.inputs, "sn_close_code", None)

# Add a Work Note to the Record in ServiceNow
inputs.sn_close_work_note = f"This record's state has been changed to {playbook.inputs.sn_record_state} by IBM SOAR"

```

---

## Local script - SNOW post-process

### Description


### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.close_record
if results.get("success"):
  note_text = f"""<br>This Incident has been updated in <b>ServiceNow</b>
              <br><b>ServiceNow ID:</b> {results.get('sn_ref_id')}
              <br><b>ServiceNow Record State:</b> {results.get('sn_record_state')}
              <br><b>ServiceNow Closing Notes:</b> {results.get('inputs', {}).get('sn_close_notes')}
              <br><b>ServiceNow Closing Code:</b> {results.get('inputs', {}).get('sn_close_code')}"""
else:
  note_text = f"""<br>Failed to close this Incident in <b>ServiceNow</b>
              <br><b>Reason:</b> {results.get('reason')}"""

incident.addNote(helper.createRichText(note_text))
```

---

