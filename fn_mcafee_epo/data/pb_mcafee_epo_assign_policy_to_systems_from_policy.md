<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.0.2.575
-->

# Playbook - McAfee ePO Assign Policy to Systems from Policy (PB)

### API Name
`mcafee_epo_assign_policy_to_systems_from_policy`

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
`mcafee_epo_policies`

### Description
None


---
## Function - McAfee ePO Assign Policy to Systems

### API Name
`mcafee_epo_assign_policy_to_systems`

### Output Name
`assign_policy`

### Message Destination
`mcafee_epo_message_destination`

### Function-Input Script
```python
if getattr(playbook.inputs, "epo_system_names_or_ids", None):
  inputs.mcafee_epo_system_name_or_id = getattr(playbook.inputs, "epo_system_names_or_ids")
inputs.mcafee_epo_product_id = row.product_id
inputs.mcafee_epo_type_id = row.type_id
inputs.mcafee_epo_object_id = row.object_id
```

---

## Local script - mcafee epo post process

### Description


### Script Type
`Local script`

### Object Type
`mcafee_epo_policies`

### Script Content
```python
results = playbook.functions.results.assign_policy
if results.get("success"):
  incident.addNote("Policy: '{}' Assigned to system: '{}'".format(row.object_id, getattr(playbook.inputs, "epo_system_names_or_ids")))
```

---

