<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v50.0.151
-->

# Playbook - SentinelOne: Update Analyst Verdict and Threat Status (PB)

### API Name
`sentinelone_update_analyst_verdict_and_threat_status`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`incident.properties.sentinelone_threat_id has_a_value`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| Analyst Verdict | `sentinelone_threat_analyst_verdict` | select | Select the SentinelOne incidentStatus | Always |
| Threat Status | `sentinelone_threat_status` | select | - | Always |

### Object Type
`incident`

### Description
Update the Incident Status and Analyst Verdict of a threat in SentinelOne.  Write the results to a notes.


---
## Function - Sentinelone: Update Threat Status

### API Name
`sentinelone_update_threat_status`

### Output Name
`update_status_results`

### Message Destination
`fn_sentinelone`

### Function-Input Script
```python
inputs.sentinelone_threat_id = incident.properties.sentinelone_threat_id
inputs.sentinelone_threat_status = playbook.inputs.sentinelone_threat_status
inputs.sentinelone_threat_analyst_verdict = playbook.inputs.sentinelone_threat_analyst_verdict
```

---

## Local script - SentinelOne: Update Threat Status and Analyst Verdict results 

### Description
Write Status and Analyst Verdict results to a note.

### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.update_status_results

note = "<b>SentinelOne: Update Threat Status </b>"
if results.get("success"):
  content = results.get("content")
  threat_id = content.get("threat_id")
  success_verdict = content.get("success_verdict")
  success_status = content.get("success_status")
  status = content.get("threat_status")
  verdict = content.get("threat_analyst_verdict")
  note = "{0}><br>  SentinelOne Threat Id: {1}<br>".format(note, threat_id)
  content = results.get("content")
  if success_verdict and success_status:
    note = "{0} analystVerdict set to <b>{1}</b><br> incidentStatus set to <b>{2}</b> in SentinelOne".format(note, verdict, status)
  elif success_verdict:
    note = "{0} analystVerdict set to <b>{1}</b><br> incidentStatus was NOT set to {2} in SentinelOne".format(note, verdict, status)
  elif success_status:
    note = "{0} incidentStatus set to <b>{1}</b><br> analystVerdict was NOT set to {2} in SentinelOne".format(note, status, verdict)
  else:
    note = "{0} analystVerdict: <b>{1}</b> and incidentStatus: <b>{2}</b> were NOT set in SentinelOne".format(note, verdict, status)
else:
  note = "{0} function did not return success.".format(note)
  
incident.addNote(helper.createRichText(note))
```

---

