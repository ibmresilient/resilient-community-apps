<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v50.0.151
-->

# Playbook - SentinelOne: Restart Agent Endpoint (PB)

### API Name
`sentinelone_restart_agent_pb`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`sentinelone_agents_dt.sentinelone_dt_is_active equals True AND sentinelone_agents_dt.sentinelone_dt_network_status equals connected`

### Object Type
`sentinelone_agents_dt`

### Description
Restart an agent endpoint managed by SentinelOne.


---
## Function - SentinelOne: Restart Agent

### API Name
`sentinelone_restart_agent`

### Output Name
`restart_agent_results`

### Message Destination
`fn_sentinelone`

### Function-Input Script
```python
inputs.sentinelone_agent_id = incident.properties.sentinelone_agent_id
```

---

## Local script - SentinelOne: Write restart agent results to note

### Description
Write restart agent function results to note.

### Script Type
`Local script`

### Object Type
`sentinelone_agents_dt`

### Script Content
```python
results = playbook.functions.results.restart_agent_results

so_inputs = results.get("inputs")
agent_id = so_inputs.get("sentinelone_agent_id")
note = u"<b>SentinelOne: Restart Agent</b><br>  SentinelOne Agent Id: {0}".format(agent_id)
content = results.get("content")
if content:
  data = content.get("data")
  if data:
    if int(data.get("affected")) <= 0:
      note = u"{0} was NOT restarted.".format(note)
    else:
      note = u"{0} was restarted".format(note)
  else:
    note = u"{0} was NOT restarted. No 'data' returned from function".format(note)
else:
  note = u"{0} was NOT restarted. No content returned from function".format(note)  

incident.addNote(helper.createRichText(note))
```

---

