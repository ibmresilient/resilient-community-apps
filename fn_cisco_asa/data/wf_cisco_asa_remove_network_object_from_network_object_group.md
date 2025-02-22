<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Cisco ASA Remove Network Object from Network Object Group

## Function - Cisco ASA Remove Network Object from Network Object Group

### API Name
`cisco_asa_remove_network_object_from_network_object_group`

### Output Name
`None`

### Message Destination
`fn_cisco_asa`

### Pre-Processing Script
```python
inputs.cisco_asa_firewall = row.cisco_asa_firewall
inputs.cisco_asa_network_object_group = row.cisco_asa_network_object_group
inputs.cisco_asa_network_object_kind = row.cisco_asa_network_object_kind
inputs.cisco_asa_network_object_value = row.cisco_asa_network_object_value
inputs.cisco_asa_network_object_id = row.cisco_asa_network_object_id
```

### Post-Processing Script
```python
from java.util import Date

if results.success:
  text = "Removed"
else:
  text = "NotFound"
  note = "Remove Network Object From Network Object Group Results:\n\n    {0}".format(results.content)
  incident.addNote(helper.createPlainText(note))
  
status_text = u"""<p style= "color:{color}">{status}</p>""".format(color="red", status=text)
row['cisco_asa_status'] = helper.createRichText(status_text)
row["cisco_asa_query_date"] = Date()

```

---

