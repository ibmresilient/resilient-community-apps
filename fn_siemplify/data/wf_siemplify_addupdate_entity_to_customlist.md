<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v52.0.0.0.1053
-->

# Siemplify Add/Update Entity to Custom List

## Function - Siemplify Add/Update Entity to Custom List

### API Name
`siemplify_addupdate_entity_to_customlist`

### Output Name
`None`

### Message Destination
`fn_siemplify`

### Pre-Processing Script
```python
inputs.siemplify_artifact_type = artifact.type
inputs.siemplify_artifact_value = artifact.value
inputs.siemplify_category = rule.properties.siemplify_list_category
inputs.siemplify_environment = rule.properties.siemplify_environments

```

### Post-Processing Script
```python
from datetime import datetime

current_dt = datetime.now()

if results.success:
  entity = results.content
  row = incident.addRow('siemplify_list_entries')
  row['report_date'] = current_dt
  row['list_name'] = 'Custom List'
  row['entity'] = entity['entityIdentifier']
  row['entity_type'] = entity['category']
  row['environments'] = ", ".join(entity['environments'])
  incident.addNote("Siemplify Add/Update Custom List successful for: {} ({})".format(artifact.value, artifact.type))
else:
  incident.addNote("Siemplify Add/Update Custom List Entity failed: {}".format(results.reason))

```

---

