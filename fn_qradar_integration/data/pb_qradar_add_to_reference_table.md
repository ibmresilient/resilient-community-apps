<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.1.1.824
-->

# Playbook - QRadar SIEM: Add to Reference Table - Example (PB)

### API Name
`qradar_add_to_reference_table`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| Inner Key | `qradar_ref_table_inner_key` | text | - | Optional |
| Outer Key | `qradar_ref_table_outer_key` | text | - | Optional |
| QRadar Server | `qradar_server` | text | Enter the label given to the QRadar server in the app.config you wish to use | Optional |
| Reference Table Name | `qradar_reference_table_name` | text | - | Optional |

### Object Type
`artifact`

### Description
Add a reference table item based on an artifact value


---
## Function - QRadar SIEM: Reference Table Add Item

### API Name
`qradar_reference_table_add_item`

### Output Name
`qradar_reference_table_add_item_result`

### Message Destination
`fn_qradar_integration`

### Function-Input Script
```python
inputs.qradar_reference_table_item_value = artifact.value
inputs.qradar_reference_table_item_inner_key = getattr(playbook.inputs, "qradar_ref_table_inner_key")
inputs.qradar_reference_table_item_outer_key = getattr(playbook.inputs, "qradar_ref_table_outer_key")
inputs.qradar_reference_table_name = getattr(playbook.inputs, "qradar_reference_table_name")
inputs.qradar_label = getattr(playbook.inputs, "qradar_server")
```

---

## Local script - qradar_add_a_reference_table_item_post_process

### Description


### Script Type
`Local script`

### Object Type
`artifact`

### Script Content
```python
results = playbook.functions.results.qradar_reference_table_add_item_result
note = u"""Outer key: {}
Inner key: {}
Entry: {}
Reference table: {}
QRadar Server: {}""".format(results.get("inputs", {}).get("qradar_reference_table_item_outer_key"),
                              results.get("inputs", {}).get("qradar_reference_table_item_inner_key"),
                              results.get("inputs", {}).get("qradar_reference_table_item_value"), 
                              results.get("inputs", {}).get("qradar_reference_table_name"),
                              results.get("inputs", {}).get("qradar_label"))
if results.get("success"):
    incident.addNote(u"Successful add\n{}".format(note))
else:
    incident.addNote(u"Failure to add item: {}\n{}".format(results.get("reason"), note))
```

---

