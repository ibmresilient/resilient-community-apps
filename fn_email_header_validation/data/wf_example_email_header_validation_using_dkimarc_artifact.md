<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Example: Email Header Validation Using DKIM/ARC [Artifact]

## Function - Email Header Validation Using DKIM/ARC

### API Name
`email_header_validation_using_dkimarc`

### Output Name
`None`

### Message Destination
`fn_email_header_validation`

### Pre-Processing Script
```python
inputs.incident_id = incident.id
inputs.artifact_id = artifact.id
```

### Post-Processing Script
```python
# results = {
#                 "dkim_verify": True/False,
#                 "arc_verify": True/False,
#                 "dkim_message": reason for True/False
#                 "arc_message": reason for True/False
#             }

output = f"DKIM Analysis: {str(results.dkim_verify)}. {results.dkim_message}\nARC Analysis: {str(results.arc_verify)}. {results.arc_message}"
incident.addNote(output)
```

---

