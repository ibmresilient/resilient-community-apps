<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.0.2.575
-->

# Playbook - McAfee ePO Run Client Task (PB)

### API Name
`mcafee_epo_run_client_task`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| ePO System Names or IDs | `epo_system_names_or_ids` | text | Comma separated list of system names or IDs | Always |

### Object Type
`mcafee_epo_client_tasks`

### Description
None


---
## Function - McAfee ePO Run Client Task

### API Name
`mcafee_epo_run_client_task`

### Output Name
`run_task`

### Message Destination
`mcafee_epo_message_destination`

### Function-Input Script
```python
if getattr(playbook.inputs, "epo_system_names_or_ids", None):
  inputs.mcafee_epo_system_name_or_id = getattr(playbook.inputs, "epo_system_names_or_ids")
inputs.mcafee_epo_product_id = row.product_id
inputs.mcafee_epo_task_id = int(row.task_id)
```

---

## Local script - mcafee epo post process

### Description


### Script Type
`Local script`

### Object Type
`mcafee_epo_client_tasks`

### Script Content
```python
results = playbook.functions.results.run_task
if results.get("success"):
  incident.addNote("System(s): '{}' ran client task: '{}' successfully.".format(getattr(playbook.inputs, "epo_system_names_or_ids"), row.object_name))
```

---

