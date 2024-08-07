<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# PagerDuty Create Incident

## Function - PagerDuty Create Incident

### API Name
`pagerduty_create_incident`

### Output Name
``

### Message Destination
`pagerduty`

### Pre-Processing Script
```python
inputs.incidentID = incident.id
inputs.pd_title = "Resilient: {}".format(incident.name)
inputs.pd_incident_key = 'RES-'+str(incident.id)
    
priority = { 'Low': 'p3', 'Medium': 'p2', 'High': 'p1' }
if incident.severity_code in priority:
  inputs.pd_priority = priority.get(incident.severity_code)
else:
  inputs.pd_priority = 'p4' # lowest
    
if not incident.description is None:
  inputs.pd_description = incident.description.content

```

### Post-Processing Script
```python
incident.properties.pd_incident_id  = results.pd['incident']['id']
incident.properties.pd_incident_url = "<a href='{}' target='blank'>Link</a>".format(results.pd['incident']['html_url'])
```

---

