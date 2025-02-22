<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v52.0.0.0.927
-->

# Playbook - VMware CBC: Kill Process

### API Name
`vmware_cbc_kill_process`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`incident.properties.vmware_cbc_alert_id has_a_value`

### Object Type
`vmware_cbc_processes_dt`

### Description
Kill the specified process from the row in the Processes data table.
Write the results to a note.


---
## Function - VMware: CBC Kill Process

### API Name
`vmware_cbc_kill_process`

### Output Name
`kill_process_results`

### Message Destination
`vmware_carbon_black_cloud`

### Function-Input Script
```python
inputs.vmware_cbc_device_id = row.cbc_device_id
inputs.vmware_cbc_process_id = row.cbc_process_pid
```

---

## Local script - VMware CBC: write Kill Process results to a note

### Description
Write the results of the function to kill a process on a device to a note.

### Script Type
`Local script`

### Object Type
`vmware_cbc_processes_dt`

### Script Content
```python
results = playbook.functions.results.kill_process_results

reason = results.get("reason", None)
inputs = results.get("inputs", None)
pid = inputs.get("vmware_cbc_process_id") if inputs else None

if results.get("success"):
    content = results.get("content", None)
    if content:
        result = content.get("result", None)
        if result:
          status = result.get("status", None)
          result_code = result.get("result_code", None)
          if status == "COMPLETE" and result_code == 0:
              note_text = f"<b>VMware CBC: Kill Process:</b>  PID: {pid} was terminated:<br>{result}."
          else:
              note_text = f"<b>VMware CBC: Kill Process:</b>  ERROR: PID: {pid} was not terminated:<br>{result}<br>{reason}."
        else:
            note_text = f"<b>VMware CBC: Kill Process:</b> Failed to kill PID {pid} - no result: {reason}."
    else:
        note_text = f"<b>VMware CBC: Kill Process:</b> Failed to kill PID {pid} - no content: {reason}."
else:
    reason = results.get("reason")
    note_text = f"<b>VMware CBC: Kill Process:</b> Failed to kill PID {pid}: {reason}."
  
incident.addNote(note_text)
```

---

