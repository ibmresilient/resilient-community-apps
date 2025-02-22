<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.1.1.824
-->

# Playbook - Wiz: Sync Notes to Issue

### API Name
`wiz_sync_notes_to_issue`

### Status
`enabled`

### Activation Type
`Automatic`

### Activation Conditions
`incident.properties.wiz_issue_id has_a_value AND note.text not_contains Wiz:  AND object_added`

### Object Type
`note`

### Description
Add notes from SOAR Case to Wiz Issue


---
## Function - Wiz: Send SOAR Notes

### API Name
`wiz_send_soar_notes`

### Output Name
`notes_result`

### Message Destination
`fn_wiz`

### Function-Input Script
```python
inputs.wiz_issue_id = incident.properties.wiz_issue_id
inputs.wiz_soar_note = note.text.content
```

---

## Local script - Add failure note

### Description
Add note to incident if syncing notes failed

### Script Type
`Local script`

### Object Type
`note`

### Script Content
```python
results = playbook.functions.results.notes_result

if not results.success:
  incident.addNote(f"<b>Wiz: Sync Notes to Issue:</b> Failed to add note to Wiz issue: {results.reason}")
```

---

