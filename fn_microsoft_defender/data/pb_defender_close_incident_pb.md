<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.6.0.1543
-->

# Playbook - Microsoft Defender: Close Incident - Example (PB)

### API Name
`defender_close_incident_pb`

### Status
`enabled`

### Activation Type
`Automatic`

### Activation Conditions
`incident.properties.defender_incident_id has_a_value AND incident.resolution_id changed`

### Object Type
`incident`

### Description
Close the corresponding Defender incident when the SOAR incident closes


---
## Function - Defender Update Incident

### API Name
`defender_update_incident`

### Output Name
`update_incident`

### Message Destination
`fn_microsoft_defender`

### Function-Input Script
```python
LOOKUP_STATUS = {
  "7": "Resolved", # Unresolved
  "8": "Resolved", # Duplicate
  "9": "Resolved", # Not an Issue
  "10": "Resolved" # Resolved
}

inputs.defender_incident_id = incident.properties.defender_incident_id
inputs.defender_incident_status = LOOKUP_STATUS.get(incident.resolution_id, "Resolved")
inputs.defender_comment = incident.resolution_summary.content
inputs.defender_classification = incident.properties.defender_classification
inputs.defender_determination = incident.properties.defender_determination
```

---


