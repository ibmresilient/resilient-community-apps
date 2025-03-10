<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - MISP: Sighting List - Example (PB)

### API Name
`misp_sighting_list`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`incident.properties.misp_event_id has_a_value`

### Object Type
`incident`

### Description
Find sightings associated with a given event


---
## Function - MISP Sighting List

### API Name
`misp_sighting_list`

### Output Name
`misp_sighting`

### Message Destination
`fn_misp`

### Function-Input Script
```python
inputs.misp_event_id = incident.properties.misp_event_id
```

---

## Local script - MISP post process

### Description


### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.misp_sighting
if results.get("success"):
  incident.addNote("Sightings for associated event.\n{}".format(results.get("content", {})))
```

---

