<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Example: SNOW: Update Data Table on Status Change [Incident]

## Function - SNOW Helper: Update Data Table

### API Name
`fn_snow_helper_update_datatable`

### Output Name
`None`

### Message Destination
`fn_service_now`

### Pre-Processing Script
```python
# Example: SNOW: Update Data Table on Status Change [Incident]

####################################
### Define pre-processing inputs ###
####################################

# Get the incident id
inputs.incident_id = incident.id

# Get the new status of the incident
inputs.sn_resilient_status = incident.plan_status
```

### Post-Processing Script
```python
None
```

---

