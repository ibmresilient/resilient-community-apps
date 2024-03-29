<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v50.0.108
-->

# Playbook - QRadar EDR: Kill Process (PB)

### API Name
`reaqta_kill_process`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`incident.properties.reaqta_endpoint_id has_a_value AND reaqta_process_list.pid has_a_value`

### Object Type
`reaqta_process_list`

### Description
Get the running processes on a given machine


---
## Function - QRadar EDR: Kill Process

### API Name
`reaqta_kill_process`

### Output Name
`reaqta_kill_process_result`

### Message Destination
`fn_reaqta`

### Function-Input Script
```python
inputs.reaqta_endpoint_id = incident.properties.reaqta_endpoint_id
inputs.reaqta_process_pid = row['pid']
inputs.reaqta_starttime = row['start_time']
inputs.reaqta_hive = incident.properties.reaqta_hive
```

---

## Local script - qradar_edr_kill_process_post_process

### Description


### Script Type
`Local script`

### Object Type
`reaqta_process_list`

### Script Content
```python
from datetime import datetime
now = datetime.now()
results = playbook.functions.results.reaqta_kill_process_result

if results.success:
  for process in results.content:
    row['report_date'] = now
    if process.get('killed'):
      row['status'] = 'killed'
      msg = u"Process: {} ({}) killed".format(row['process_name'], row['pid'])
    else:
      row['status'] = process.get('error')
      msg = u"Process: {} ({}) kill failed: {}".format(row['process_name'], row['pid'], process.get('error'))
    incident.addNote(msg)
    break;
else:
  incident.addNote(u"ReaQta Kill Process failed: {}".format(results.reason))
```

---

