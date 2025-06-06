<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Playbook - ElasticSearch Query from Incident

### API Name
`elasticsearch_query_from_incident`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Object Type
`incident`

### Description
None


---
## Function - ElasticSearch Utilities: Query

### API Name
`fn_elasticsearch_query`

### Output Name
`results`

### Message Destination
`fn_elasticsearch`

### Function-Input Script
```python
None
```

---

## Local script - Elastic Search Results

### Description


### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.results
if results.success:
  msg = [f"ElasticSearch successful for Incident: {incident.id}\n"]
  for result in results.query_results:
    for k, v in result.items():
        msg.append(f"<br><b>{k}</b>: {v}")
  incident.addNote(helper.createRichText("".join(msg)))
else:
  incident.addNote(f'ElasticSearch Incident query failed:{results.reason}. Incident ID:{incident.id}')
```

---

