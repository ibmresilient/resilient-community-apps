<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Example: MITRE Get Groups Using All Techniques

## Function - MITRE Get Groups Using All Given Techniques

### API Name
`mitre_groups_technique_intersection`

### Output Name
`None`

### Message Destination
`fn_mitre_integration`

### Pre-Processing Script
```python
# The priority order of inputs is:
# 1. Values entered in the Activity Field pop-up
# 2. Values in the Input Fields added to the layout
# 3. Inputs in the function's workflow

activity_field_given = rule.properties.mitre_technique_id or rule.properties.mitre_technique_name
incident_properties_given = incident.properties.mitre_technique_name or incident.properties.mitre_technique_id

if activity_field_given:
  inputs.mitre_technique_name = rule.properties.mitre_technique_name
  inputs.mitre_technique_id = rule.properties.mitre_technique_id
elif incident_properties_given:
  inputs.mitre_technique_id = incident.properties.mitre_technique_id
  inputs.mitre_technique_name = incident.properties.mitre_technique_name
```

### Post-Processing Script
```python
"""
Data returned as a part of ResultPayload:
        {
            "technique": "T0042",
            "name": "Wet Bandits",
            "id": "G0032",
            "ref": "url to MITRE",
            "description": "lorem ipsum",
            "aliases": ["name 1", "name 2"]
        }
"""
groups_mitre = results.content["mitre_groups"]

for group in groups_mitre:
  group_row = incident.addRow("mitre_attack_groups")
  group_row["groups_technique"] = group["technique"]
  
  ref = '<a href="{}">'.format(group["ref"]) +'{}</a> '
  group_row["groups_name"] = helper.createRichText(ref.format(group["name"]))
  group_row["groups_id"]   = helper.createRichText(ref.format(group["id"]))
  
  group_row["groups_aliases"] = ",".join(group["aliases"])
  group_row["groups_description"] = helper.createRichText(group["description"])
```

---

