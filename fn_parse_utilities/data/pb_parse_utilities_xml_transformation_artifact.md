<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Playbook - Parse Utilities: XML Transformation (Artifact) - Example (PB)

### API Name
`parse_utilities_xml_transformation_artifact`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`artifact.type in ['Email Attachment', 'Malware Sample', 'Log File', 'Other File']`

### Object Type
`artifact`

### Description
Example playbook to transform an XML document artifact using a defined xsl transform file.


---
## Function - Parse Utilities: XML Transformation

### API Name
`parse_utilities_xml_transformation`

### Output Name
`xml_transformation`

### Message Destination
`fn_parse_utilities`

### Function-Input Script
```python
inputs.parse_utilities_artifact_id = artifact.id
inputs.parse_utilities_incident_id = incident.id
inputs.parse_utilities_xml_stylesheet = "cdcatalog.xslt"  # CHANGEME
```

---

## Local script - XML Transformation

### Description


### Script Type
`Local script`

### Object Type
`artifact`

### Script Content
```python
results = playbook.functions.results.xml_transformation

# results.content is the string representation of the transformed xml document
content = helper.createRichText("<b>Playbook 'Parse Utilities: XML Transformation (Artifact) - Example (PB)' results</b><br>{}".format(results.content))
incident.addNote(content)
```

---

