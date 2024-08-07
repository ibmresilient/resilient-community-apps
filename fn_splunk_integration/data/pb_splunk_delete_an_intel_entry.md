<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v50.1.262
-->

# Playbook - Splunk: Delete an intel entry - Example (PB)

### API Name
`splunk_delete_an_intel_entry`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`splunk_intel_results.status equals Active`

### Object Type
`splunk_intel_results`

### Description
This is an example playbook calling the "Splunk Delete Threat Intel Item" function to delete an intel item from a Splunk collection.


---
## Function - Splunk Delete Threat Intel Item

### API Name
`splunk_delete_threat_intel_item`

### Output Name
`delete_intel_item`

### Message Destination
`splunk_es_rest`

### Function-Input Script
```python
inputs.splunk_threat_intel_type = row.intel_collection
inputs.splunk_threat_intel_key = row.intel_key
inputs.splunk_label = row.splunk_server
```

---

## Local script - post process

### Description


### Script Type
`Local script`

### Object Type
`splunk_intel_results`

### Script Content
```python
results = playbook.functions.results.delete_intel_item
results_content = results.get("content", {})

result_note = u"""<b>Artifact</b>: {}<br><br>
<b>Splunk Delete Status</b>: {}<br>
<b>Message</b>: {}""".format(row.intel_value,
                             "Successful" if results_content.get("status", False) else "Unsuccessful",
                             results_content.get("message", "None"))

incident.addNote(helper.createRichText(result_note))
if results_content.get("status"):
  row.status = "Deleted"
```

---

