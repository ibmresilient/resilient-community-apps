<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Example: Microsoft Security Graph Alert Search

## Function - Microsoft Security Graph Alert Search

### API Name
`microsoft_security_graph_alert_search`

### Output Name
``

### Message Destination
`microsoft_security_graph_message_destination`

### Pre-Processing Script
```python
from datetime import datetime

search = "filter="
conjunction = False

if rule.properties.microsoft_security_graph_query_start_datetime:
    start_ts = int(rule.properties.microsoft_security_graph_query_start_datetime) / 1000
    start = datetime.fromtimestamp(start_ts)
    start_filter = "createdDateTime%20ge%20{}".format(start.isoformat())
    search += start_filter
    conjunction = True

if rule.properties.microsoft_security_graph_query_end_datetime:
    end_ts = int(rule.properties.microsoft_security_graph_query_end_datetime) / 1000
    end = datetime.fromtimestamp(end_ts)
    end_filter = "createdDateTime%20le%20{}".format(end.isoformat())
    if conjunction: 
        search += "%20and%20"
    search += end_filter
    conjunction = True

if artifact.type == "User Account":
    artifact_filter = "userStates/any(user:%20user/accountName%20eq%20'{}')".format(artifact.value)
    if conjunction: 
        search += "%20and%20"
    search += artifact_filter
    conjunction = True

inputs.microsoft_security_graph_alert_search_query = search

```

### Post-Processing Script
```python
alerts = results.content.value
note = "Microsoft Security Graph Alert Search<br>There are <b>{}</b> alerts based on the artifact of value <b>{}</b>.".format(str(len(alerts)), artifact.value)

if len(alerts):
  note = note + "<br><b>Alert ids:</b>"
  for alert in alerts:
    note = note + "<br>- {}".format(alert.id)

incident.addNote(helper.createRichText(note))
```

---

