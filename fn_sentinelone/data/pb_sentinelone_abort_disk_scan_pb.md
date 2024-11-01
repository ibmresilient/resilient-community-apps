<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v50.0.151
-->

# Playbook - SentinelOne: Abort Disk Scan (PB)

### API Name
`sentinelone_abort_disk_scan_pb`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`sentinelone_agents_dt.sentinelone_dt_is_active equals True AND sentinelone_agents_dt.sentinelone_dt_network_status equals connected`

### Object Type
`sentinelone_agents_dt`

### Description
Abort a Full Disk Scan on an agent managed by SentinelOne.


---
## Function - SentinelOne: Abort Disk Scan

### API Name
`sentinelone_abort_disk_scan`

### Output Name
`abort_scan_results`

### Message Destination
`fn_sentinelone`

### Function-Input Script
```python
inputs.sentinelone_agent_id = row.sentinelone_dt_agent_id
```

---

## Local script - SentinelOne: Write Abort Scan Results to a Note

### Description
Write abort scan function results to a note.

### Script Type
`Local script`

### Object Type
`sentinelone_agents_dt`

### Script Content
```python
results = playbook.functions.results.abort_scan_results

so_inputs = results.get("inputs")
agent_id = so_inputs.get("sentinelone_agent_id")
note = u"<b>SentinelOne: Abort Full Disk Scan </b><br>  SentinelOne Agent Id: {0}".format(agent_id)
content = results.get("content")
if content:
  data = content.get("data")
  if data:
    if int(data.get("affected")) <= 0:
      note = u"{0} Full Disk Scan was NOT aborted.".format(note)
    else:
      note = u"{0} Full Disk Scan aborted.".format(note)
  else:
    note = u"{0} Full Disk Scan was NOT aborted. No 'data' returned from function".format(note)
else:
  note = u"{0} Full Disk Scan was NOT aborted. No content returned from function".format(note)  

incident.addNote(helper.createRichText(note))
```

---

