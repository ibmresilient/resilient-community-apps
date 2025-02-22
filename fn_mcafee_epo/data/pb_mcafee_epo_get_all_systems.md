<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.0.2.575
-->

# Playbook - McAfee ePO Get All Systems (PB)

### API Name
`mcafee_epo_get_all_systems`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Object Type
`incident`

### Description
None


---
## Function - McAfee ePO Execute Query

### API Name
`mcafee_epo_execute_query`

### Output Name
`query`

### Message Destination
`mcafee_epo_message_destination`

### Function-Input Script
```python
inputs.mcafee_epo_target = "EPOLeafNode"
inputs.datatable_name = "mcafee_epo_systems_dt"
inputs.incident_id = incident.id
```

---

## Local script - mcafee epo post process

### Description


### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.query
if results.get('success'):
  for system in results.get('content', {}):
    table_row = incident.addRow("mcafee_epo_systems_dt")
    table_row["epo_system_name"] = system.get("EPOLeafNode.NodeName")
    table_row["epo_agent_guid"] = system.get("EPOLeafNode.AgentGUID")
    table_row["epo_last_communication"] = system.get("EPOLeafNode.LastUpdate")
    table_row["epo_tags"] = system.get("EPOLeafNode.Tags")
    table_row["epo_operating_system"] = system.get("EPOLeafNode.os").replace("|", " | ")
    table_row["epo_deleted"] = False
```

---

