<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.0.974
-->

# Example: Guardium Block User Access to DB

## Function - Function Guardium block user

### API Name
`function_guardium_block_user`

### Output Name
`None`

### Message Destination
`fn_guardium`

### Pre-Processing Script
```python
inputs.guardium_username = rule.properties.grd_db_user_name
```

### Post-Processing Script
```python
message = results.get("content")
incident.addNote(str(message))
```

---

