<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.4.0.1351
-->

# Playbook - Example: Jira Close Issue

### API Name
`example_jira_close_issue`

### Status
`enabled`

### Activation Type
`Automatic`

### Activation Conditions
`incident.properties.jira_internal_url has_a_value AND incident.properties.jira_issue_closed_on_jira not_equals True AND incident.properties.jira_linked_to_incident equals True AND incident.resolution_summary changed`

### Object Type
`incident`

### Description
Close Jira issue when linked SOAR case is closed.


---
## Function - Jira Transition Issue

### API Name
`jira_transition_issue`

### Output Name
`output`

### Message Destination
`fn_jira`

### Function-Input Script
```python
from json import dumps

inputs.jira_label = incident.properties.jira_server
inputs.jira_issue_id = incident.properties.jira_issue_id
inputs.jira_transition_id = "Done"
inputs.jira_comment = "Closed in IBM SOAR\n\nResolution: {}\n{}".format(incident.resolution_id, incident.resolution_summary.content)

# Define JIRA fields here
inputs.jira_fields = dumps({})
```

---

## Local script - jira close issue post-process

### Description


### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
incident.properties.jira_issue_status = "Done"
```

---

