<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - Scheduler: Remove Job (PB)

### API Name
`pb_scheduler_remove_job`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`scheduler_rules.status not_equals Deleted`

### Object Type
`scheduler_rules`

### Description
Remove a scheduled job


---
## Function - Scheduled Rule Remove

### API Name
`remove_a_scheduled_rule`

### Output Name
`output_scheduled_rule_remove`

### Message Destination
`fn_scheduler`

### Function-Input Script
```python
inputs.scheduler_label = row.schedule_label
```

---

## Local script - Write removed job to DataTable

### Description


### Script Type
`Local script`

### Object Type
`scheduler_rules`

### Script Content
```python
results = playbook.functions.results.output_scheduled_rule_remove

if results.get("success"):
  row['status'] = "Deleted"
else:
  row['status'] = row['status'] + " (Error)"

```

---

