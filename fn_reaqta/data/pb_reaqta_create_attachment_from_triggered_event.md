<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v50.0.108
-->

# Playbook - QRadar EDR: Create Attachment from Triggered Event (PB)

### API Name
`reaqta_create_attachment_from_triggered_event`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`incident.properties.reaqta_endpoint_id has_a_value AND reaqta_trigger_events.program_path has_a_value`

### Object Type
`reaqta_trigger_events`

### Description
Attach a file from an endpoint.


---
## Function - QRadar EDR: Attach File

### API Name
`reaqta_attach_file`

### Output Name
`create_attach_results`

### Message Destination
`fn_reaqta`

### Function-Input Script
```python
inputs.reaqta_program_path = row['program_path']
inputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id
inputs.reaqta_incident_id = incident.id
inputs.reaqta_hive = incident.properties.reaqta_hive
```

---

## Local script - QRadar EDR: Write attachment results to note

### Description
Write attachment results to note.

### Script Type
`Local script`

### Object Type
`reaqta_trigger_events`

### Script Content
```python
results = playbook.functions.results.create_attach_results
if results.success:
  incident.addNote(u"ReaQta Attach File created: {} from program path: {}".format(results.content['name'], results.inputs['reaqta_program_path']))
else:
  incident.addNote(u"ReaQta Attach File failed: {}".format(results.reason))
```

---

