<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Example: Zip Extract

## Function - Utilities: Attachment Zip Extract

### API Name
`utilities_attachment_zip_extract`

### Output Name
`extracted_file`

### Message Destination
`fn_utilities`

### Pre-Processing Script
```python
# Required inputs are: the incident id and attachment id
inputs.incident_id = incident.id
inputs.attachment_id = attachment.id

# If this is a "task attachment" then we will additionally have a task-id
if task is not None:
  inputs.task_id = task.id

# The path within the zip that we want to extract
inputs.file_path = rule.properties.extract_file_path

# If the zipfile is password protected, specify here
# inputs.zipfile_password = 
if rule.properties.zip_password:
  inputs.zipfile_password = rule.properties.zip_password
```

### Post-Processing Script
```python
None
```

---

## Function - Utilities: Base64 to Attachment

### API Name
`utilities_base64_to_attachment`

### Output Name
`None`

### Message Destination
`fn_utilities`

### Pre-Processing Script
```python
#
inputs.base64content = workflow.properties.extracted_file.content
file_name = rule.properties.extract_file_path.split('/')[-1]

inputs.incident_id = incident.id
inputs.file_name = file_name + ".b64"
inputs.content_type = "image/jpeg"

```

### Post-Processing Script
```python
None
```

---

