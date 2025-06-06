<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Example: MITRE Get Tactic information

## Function - MITRE Tactic Information

### API Name
`mitre_tactic_information`

### Output Name
``

### Message Destination
`fn_mitre_integration`

### Pre-Processing Script
```python
# The priority order of inputs is:
# 1. Values entered in the Activity Field pop-up
# 2. Values in the Input Fields added to the layout
# 3. Inputs in the function's workflow

activity_field_given = rule.properties.mitre_tactic_name or rule.properties.mitre_tactic_id
incident_propery_given = incident.properties.mitre_tactic_id or incident.properties.mitre_tactic_name

if activity_field_given:
  inputs.mitre_tactic_name = rule.properties.mitre_tactic_name
  inputs.mitre_tactic_id = rule.properties.mitre_tactic_id
elif incident_propery_given:
  inputs.mitre_tactic_name = incident.properties.mitre_tactic_name
  inputs.mitre_tactic_id = incident.properties.mitre_tactic_id
```

### Post-Processing Script
```python
""" Example of data returned in ResultPayload's content
{
  "mitre_tactics": [
    {
      
      "name": String,
      "id": String,
      "ref": "String",
      "collection": "String", 
      "mitre_techniques": [
        {
          "name": "String", 
          "description": "String",
          "external_references": [{"url": "String"}],
          "x_mitre_detection": "String",
          "id": "String",
          "collection": "String"
        }
      ]
    }
  ]
}
"""

tactics = results.content["mitre_tactics"]

for tactic in tactics:
  #
  # MITRE ATTACK of Incident Datatable
  #
  tactic_row = incident.addRow("mitre_attack_of_incident")
  tactic_row["collection"] = tactic["collection"]
  tactic_row["attack_tactic"] = tactic["name"]
  tactic_row["tactic_code"] = tactic["id"]
  url_html = '<a href="' + tactic["ref"] + '">' + tactic["ref"] + '</a><br>'
  tactic_row["reference"] = helper.createRichText(url_html)
  tactic_row["confidence"] = " "
  #
  # MITRE ATT&CK techniques Datatable
  #
  techs = tactic["mitre_techniques"]
  for att_tech in techs:
    tech_row = incident.addRow("mitre_attack_techniques")
    tech_row["collection"] = tactic["collection"]
    tech_row["tactic"] = tactic["name"]

    tech_row["technique_name"] = att_tech["name"]
    tech_row["technique_description"] = helper.createRichText(att_tech["description"])
    refs = att_tech["external_references"]
    ref_html = ""
    for ref in refs:
      url = ref["url"]
      
      https_str = "https://"
      http_str = "http://"

      start_pos = url.find(https_str)

      if start_pos != -1:
        start_pos = start_pos + len(https_str)
      else:
        # try http://
        start_pos = url.find(http_str)
        if start_pos != -1:
          start_pos = start_pos + len(http_str)
        else:
          start_pos = 0 

      end_pos = url.find('/', start_pos)
      if end_pos == 0:
        # We don't know how to extract
        display_str = url
      elif end_pos == -1:
        display_str = url[start_pos:]
      else:
        display_str = url[start_pos:end_pos]
      
      ref_html = ref_html + '<a href="' + ref["url"] + '">' + display_str + '</a><br>'
    tech_row["references"] = helper.createRichText(ref_html)
    tech_row["detection"] = helper.createRichText(att_tech["x_mitre_detection"])
    tech_row["technique_id"] = att_tech["id"]


```

---

