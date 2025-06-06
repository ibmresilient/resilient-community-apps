<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.0.2.575
-->

# Playbook - McAfee ePO List Issues (PB)

### API Name
`mcafee_epo_list_issues`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Object Type
`incident`

### Description
None


---
## Function - McAfee ePO List Issues

### API Name
`mcafee_epo_list_issues`

### Output Name
`issues`

### Message Destination
`mcafee_epo_message_destination`

### Function-Input Script
```python
inputs.datatable_name = "mcafee_epo_issues"
inputs.incident_id = incident.id
```

---

## Local script - mcafee epo post process

### Description


### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.issues
if results.get("success"):
  for c in results.get("content", {}):
    row = incident.addRow("mcafee_epo_issues")
    row["issue_name"] = c.get("name")
    row["issue_id"] = int(c.get("id"))
    row["severity"] = c.get("severity")
    row["issue_due_date"] = c.get("dueDate")
    row["issue_description"] = c.get("description")
    row["ticket_server_name"] = c.get("ticketServerName")
    row["priority"] = c.get("priority")
    row["type"] = c.get("type")
    row["resolution"] = c.get("resolution")
    row["assignee_name"] = c.get("assigneeName")
    row["issue_state"] = c.get("state")
    row["ticket_id"] = int(c.get("ticketId")) if c.get("ticketId") else None
    row["issue_deleted"] = False
```

---

