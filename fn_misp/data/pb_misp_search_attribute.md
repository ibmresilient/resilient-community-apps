<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - MISP: Search Attribute - Example (PB)

### API Name
`misp_search_attribute`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Object Type
`artifact`

### Description
Identify other MISP events with the same attribute


---
## Function - MISP Search Attribute

### API Name
`misp_search_attribute`

### Output Name
`misp_attributes`

### Message Destination
`fn_misp`

### Function-Input Script
```python
inputs.misp_attribute_value = artifact.value
```

---

## Local script - MISP post process

### Description


### Script Type
`Local script`

### Object Type
`artifact`

### Script Content
```python
results = playbook.functions.results.misp_attributes

if not results.get("success"):
  incident.addNote(f"No attributes matching {artifact.value} found")
else:
  matched = []
  for match in results.get("content", {}):
    matched.append(f"Event: {match.get('Event', {}).get('info')}, ID: {match.get('Event', {}).get('id')}")
  incident.addNote("Attribute Search Matches:\n {}".format('\n'.join(matched)))
```

---

