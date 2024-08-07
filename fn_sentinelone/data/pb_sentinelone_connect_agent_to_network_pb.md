<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v50.0.151
-->

# Playbook - SentinelOne: Connect Agent to Network (PB)

### API Name
`sentinelone_connect_agent_to_network_pb`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`(sentinelone_agents_dt.sentinelone_dt_network_status equals disconnected OR sentinelone_agents_dt.sentinelone_dt_network_status equals disconnecting) AND sentinelone_agents_dt.sentinelone_dt_is_active equals True`

### Object Type
`sentinelone_agents_dt`

### Description
Disconnect a SentinelOne managed endpoint from the network.


---
## Function - SentinelOne: Connect to Network

### API Name
`sentinelone_connect_to_network`

### Output Name
`connect_results`

### Message Destination
`fn_sentinelone`

### Function-Input Script
```python
inputs.sentinelone_agent_id = row.sentinelone_dt_agent_id
```

---

## Local script - SentinelOne: Update data table with Connect to Network results 

### Description
Update the agent data table Network Status with results of Connect to Network function. 

### Script Type
`Local script`

### Object Type
`sentinelone_agents_dt`

### Script Content
```python
results = playbook.functions.results.connect_results

so_inputs = results.get("inputs")
agent_id = so_inputs.get("sentinelone_agent_id")
note = u"<b>SentinelOne: Connect to Network </b><br>  SentinelOne Agent Id: {0}".format(agent_id)
content = results.get("content")
if content:
  data = content.get("data")
  if data:
    if int(data.get("affected")) <= 0:
      note = u"{0} is NOT connected to network".format(note)
    else:
      networkStatus = u"""<p style= "color:{color}">{status}</p>""".format(color="green", status="connected")
      row["sentinelone_dt_network_status"] = helper.createRichText(networkStatus)
      note = u"{0} is connected to network".format(note)
  else:
    note = u"{0} no data returned from function".format(note)
else:
  note = u"{0} no content data returned from function".format(note)  

incident.addNote(helper.createRichText(note))

```

---

