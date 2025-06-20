<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Playbook - SOAR Utils: String to Attachment - Example (PB)

### API Name
`soar_utils_string_to_attachment_example_pb`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`artifact.type equals String`

### Object Type
`artifact`

### Description
An example playbook of creating an attachment from an input string.


---
## Function - SOAR Utilities: String to Attachment

### API Name
`soar_utils_string_to_attachment`

### Output Name
`string_to_attachment_result`

### Message Destination
`fn_soar_utils`

### Function-Input Script
```python
# Required inputs are: the string to convert, the incident id and the attachment name
inputs.soar_utils_string_to_convert_to_attachment = artifact.value
inputs.incident_id = incident.id
inputs.attachment_name = "A Test Attachment Name"
# If this is a "task attachment" then we will additionally have a task-id
if task is not None:
  inputs.task_id = task.id
```

---

## Local script - Soar Utils: Convert String to Attachment

### Description
Converting String to Attachment.

### Script Type
`Local script`

### Object Type
`artifact`

### Script Content
```python
results = playbook.functions.results.string_to_attachment_result


if results:
  note_text = f"<b>SOAR Utils: String to Attachment - Example (PB):</b> Attachment ID: <b>{results.attachment_id}</b> successfully created"
else:
  note_text = f"<b>SOAR Utils: String to Attachment - Example (PB)</b> Failed: {results.reason}"
incident.addNote(note_text)

```

---

