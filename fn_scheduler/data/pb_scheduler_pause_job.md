<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - Scheduler: Pause Job (PB)

### API Name
`pb_scheduler_pause_job`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`scheduler_rules.status equals Active`

### Object Type
`scheduler_rules`

### Description
Pause a scheduled job


---
## Function - Scheduled Rule Pause

### API Name
`scheduled_rule_pause`

### Output Name
`output_scheduled_rule_pause`

### Message Destination
`fn_scheduler`

### Function-Input Script
```python
inputs.scheduler_label = row.schedule_label
```

---

## Local script - Write paused job to DataTable

### Description


### Script Type
`Local script`

### Object Type
`scheduler_rules`

### Script Content
```python
results = playbook.functions.results.output_scheduled_rule_pause

if results.get("success"):
  row['status'] = 'Paused'
else:
  row['status'] = row['status'] + " (Error)"

```

---

