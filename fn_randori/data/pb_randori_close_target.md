<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - Randori: Automatic Close Target

### API Name
`randori_close_target`

### Status
`enabled`

### Activation Type
`Automatic`

### Activation Conditions
`incident.properties.randori_target_id has_a_value AND incident.resolution_id changed AND incident.resolution_summary not_contains Closed by Randori`

### Object Type
`incident`

### Description
Close a target in Randori if the Case is closed in SOAR.


---
## Function - Randori: Update Target Status

### API Name
`randori_update_target_status`

### Output Name
`status_data`

### Message Destination
`fn_randori`

### Function-Input Script
```python
STATUS_LOOKUP = {
  'Unresolved': "Accepted",   # Unresolved
  'Duplicate': "Accepted",   # Duplicate
  'Not an Issue': "Accepted",   # Not an Issue
  'Resolved': "Mitigated"  # Resolved
}

inputs.randori_target_id = incident.properties.randori_target_id
inputs.randori_note = incident.resolution_summary.content
inputs.randori_target_status = STATUS_LOOKUP.get(incident.resolution_id, "Accepted")
```

---

## Local script - Randori: confirm status changed.

### Description
Test if target status was successfully updated in Randori and output a note if it was not.

### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
status_data = playbook.functions.results.status_data

if not status_data.success:
  incident.addNote("ERROR: unable to update target status in Randori")
else:
  incident.properties.randori_target_status = status_data.inputs.randori_target_status
```

---

