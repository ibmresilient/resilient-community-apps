<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# PagerDuty Transition Incident

## Function - PagerDuty Transition Incident

### API Name
`pagerduty_transition_incident`

### Output Name
`None`

### Message Destination
`pagerduty`

### Pre-Processing Script
```python
inputs.pd_incident_id = incident.properties.pd_incident_id
if incident.resolution_id:
  inputs.pd_status = 'resolved'
  inputs.pd_description = incident.resolution_summary.content
#else:
#  inputs.pd_status = 'acknowledged'
  
priority = { 'Low': 'p3', 'Medium': 'p2', 'High': 'p1' }
if incident.severity_code in priority:
  inputs.pd_priority = priority.get(incident.severity_code)
```

### Post-Processing Script
```python
None
```

---

