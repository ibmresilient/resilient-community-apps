<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.1.0.695
-->

# Example of searching and returning Categories

## Function - QRadar Top Events

### API Name
`qradar_top_events`

### Output Name
``

### Message Destination
`fn_qradar_enhanced_data`

### Pre-Processing Script
```python
inputs.qradar_search_param3 = incident.properties.qradar_id
inputs.qradar_query_type = "categories"
inputs.qradar_label = incident.properties.qradar_destination
inputs.soar_table_name = "qr_categories"
inputs.soar_incident_id = incident.id
```

### Post-Processing Script
```python
content = results.get("content")

if content:
  link = "<a href=\"https://" + content.get("qrhost") + "/console/ui/offenses/{0}/events?filter={1}%3B%3D%3B%3B{2}&page=1&pagesize=10\" target=\"_blank\">{3}</a>"
  offenseid = content.get("offenseid")
  for event in content.get("events"):
    categoryname = event.get("categoryname")
    qradar_event = incident.addRow("qr_categories")
    qradar_event.category_name = link.format(offenseid, "category_name", categoryname, categoryname)
    qradar_event.magnitude = link.format(offenseid, "category_name", categoryname, event.get("magnitude"))
    qradar_event.event_count = link.format(offenseid, "category_name", categoryname, event.get("eventcount"))
    qradar_event.event_time = int(event.get("eventtime"))
    qradar_event.sourceip_count = link.format(offenseid, "category_name", categoryname, event.get("sourceipcount"))
    qradar_event.destinationip_count = link.format(offenseid, "category_name", categoryname, event.get("destinationipcount"))
    qradar_event.reported_time = content.get("current_time")
```

---

## Function - QRadar Top Events

### API Name
`qradar_top_events`

### Output Name
``

### Message Destination
`fn_qradar_enhanced_data`

### Pre-Processing Script
```python
inputs.qradar_search_param3 = incident.properties.qradar_id
inputs.qradar_query_type = "categories"
inputs.qradar_label = incident.properties.qradar_destination
inputs.soar_table_name = "qr_categories"
inputs.soar_incident_id = incident.id
```

### Post-Processing Script
```python
content = results.get("content")

if content:
  link = "<a href=\"https://" + content.get("qrhost") + "/console/ui/offenses/{0}/events?filter={1}%3B%3D%3B%3B{2}&page=1&pagesize=10\" target=\"_blank\">{3}</a>"

  for event in content.get("events"):
    qradar_event = incident.addRow("qr_categories")
    qradar_event.category_name = event.get("categoryname")
    qradar_event.flow_count = event.get("flowcount")
    qradar_event.last_packet_time = int(event.get("lastpackettime"))
    qradar_event.sourceip_count = event.get("sourceipcount")
    qradar_event.destinationip_count = event.get("destinationipcount")
    qradar_event.reported_time = content.get("current_time")
```

---

