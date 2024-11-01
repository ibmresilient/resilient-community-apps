<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v52.0.0.0.927
-->

# Playbook - VMware CBC: Update Device Row from Device

### API Name
`vmware_cbc_update_device_row_from_device`

### Status
`enabled`

### Activation Type
`Automatic`

### Activation Conditions
`vmware_cbc_device_dt.cbc_device_id has_a_value AND object_added`

### Object Type
`vmware_cbc_device_dt`

### Description
Automatic playbook to populate the columns of the CBC Device data table that from the devices endpoint. Note: Other columns of the CBC Device data table are populated from fields of the alert.


---
## Function - VMware CBC: Get Device By ID

### API Name
`vmware_cbc_get_device_by_id`

### Output Name
`get_device_by_id_results`

### Message Destination
`vmware_carbon_black_cloud`

### Function-Input Script
```python
inputs.vmware_cbc_device_id = row.cbc_device_id
```

---

## Global script - VMware CBC: Populate CBC Device Row from Device

### Description
Write the results of get device by ID function to the Device data table.

### Script Type
`Global script`

### Object Type
`vmware_cbc_device_dt`

### Script Content
```python
results = playbook.functions.results.get_device_by_id_results

if results.get("success", False):
  content = results.get("content", {})
  if content:
    device = content.get("device", None)
    if device:
      row.cbc_device_quarantined = device.get("quarantined", None)
      row.cbc_device_status = device.get("status", None)
      sensor_states =  device.get("sensor_states", None) 
      row.cbc_sensor_state = ", ".join(sensor_states) if isinstance(sensor_states, list) else None
      note_text = f"<b>VMware CBC: Populate Device Row from Device:</b> Update complete."
    else:
      note_text = f"<b>VMware CBC: Populate Device Row from Device:</b> Unable to get device data to update CBC Device data table."
  else:
    note_text = f"<b>VMware CBC: Populate Device Row from Device:</b> Unable to get device data to update CBC Device data table - no content."
else:
  reason = results.get("reason", None)
  note_text = f"<b>VMware CBC: Populate Device Row from Device:</b> Unable to get device data to update CBC Device data table.<br> reason: {reason}"
  
incident.addNote(note_text)

```

---

