<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Google SCC: Add Source Property

## Function - Google Cloud SCC: Update Findings

### API Name
`google_cloud_scc_update_finding`

### Output Name
`None`

### Message Destination
`fn_google_cloud_scc`

### Pre-Processing Script
```python
finding_name = incident.properties.google_scc_name.get("content")

if finding_name:
  # for this specific workflow, we want to only update the finding that
  # is associated with this incident so we pass in the finding name as the filter
  inputs.google_scc_filter = "name = \"{0}\"".format(finding_name)
  
  inputs.google_scc_update_key = rule.properties.google_scc_source_property_name
  if "source_properties." not in inputs.google_scc_update_key:
    inputs.google_scc_update_key = "source_properties." + inputs.google_scc_update_key
  inputs.google_scc_update_value = rule.properties.google_scc_update_value
else:
  log.fail("Could not find value for finding_name in Incident")
```

### Post-Processing Script
```python
if results.get("success"):
  row = incident.addRow("google_scc_finding_source_properties_dt")
  row.google_scc_source_property = results.get("inputs", {}).get("google_scc_update_key").split(".")[-1]
  row.google_scc_source_property_value = results.get("inputs", {}).get("google_scc_update_value")
```

---

