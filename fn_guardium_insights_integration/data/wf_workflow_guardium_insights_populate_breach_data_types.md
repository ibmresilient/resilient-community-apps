<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.0.974
-->

# Workflow Guardium Insights populate breach data types

## Function - Function Guardium Insights populate breach data types

### API Name
`function_guardium_insights_populate_breach_data_types`

### Output Name
`None`

### Message Destination
`guardium_insights_integration`

### Pre-Processing Script
```python
inputs.incident_id = incident.id
inputs.input_field_guardium_insights_who = incident.properties.field_guardium_insights_who
inputs.input_field_guardium_insights_what = incident.properties.field_guardium_insights_what
```

### Post-Processing Script
```python
None
```

---

