<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# McAfee ePO Run Client Task

## Function - McAfee ePO Run Client Task

### API Name
`mcafee_epo_run_client_task`

### Output Name
`None`

### Message Destination
`mcafee_epo_message_destination`

### Pre-Processing Script
```python
inputs.mcafee_epo_system_name_or_id = rule.properties.epo_system_names_or_ids
inputs.mcafee_epo_product_id = row.product_id
inputs.mcafee_epo_task_id = int(row.task_id)
```

### Post-Processing Script
```python
if results.get("success"):
  incident.addNote("System(s): '{}' ran client task: '{}' successfully.".format(rule.properties.epo_system_names_or_ids, row.object_name))
```

---

