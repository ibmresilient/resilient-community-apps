<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.0.1.486
-->

# Playbook - Salesforce: Create Salesforce Case from This SOAR Case

### API Name
`salesforce_create_salesforce_case_from_this_soar_case`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`incident.properties.salesforce_case_id not_has_a_value`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| Include SOAR Tasks | `include_soar_tasks` | boolean | - | Optional |

### Object Type
`incident`

### Description
Create a Salesforce case from the SOAR case which activated the playbook.  This playbook is only available to SOAR cases that are not associated with a Salesforce case.


---
## Function - Salesforce: Create Case in Salesforce

### API Name
`salesforce_create_case_in_salesforce`

### Output Name
`salesforce_case_results`

### Message Destination
`fn_salesforce`

### Function-Input Script
```python
import json

case_json = {}
case_json['Origin'] = "Web"
case_json['Status'] = "New"
case_json['Priority'] = incident.severity_code 
if incident.description:
  case_json['Description'] = incident.description.content
else:
  case_json['Description'] = "Case created from SOAR case {}".format(incident.id)
case_json['Subject'] = incident.name

# Need to make incident type multi-select in Salesforce to support multi-select in SOAR
# For now just take the first incident type in the list.
if incident.incident_type_ids != []:
  case_json['Type'] = incident.incident_type_ids[0]

inputs.salesforce_case_payload = json.dumps(case_json)
inputs.incident_id = incident.id
```

---
## Function - Salesforce: Sync Tasks Between Cases

### API Name
`salesforce_sync_tasks_between_cases`

### Output Name
`sync_task_results`

### Message Destination
`fn_salesforce`

### Function-Input Script
```python
inputs.incident_id = incident.id
inputs.salesforce_case_id = incident.properties.salesforce_case_id
inputs.task_sync_direction = "Salesforce"
```

---
## Function - Salesforce: Add Comment to Salesforce Case

### API Name
`salesforce_add_comment_to_salesforce_case`

### Output Name
`add_comment_results`

### Message Destination
`fn_salesforce`

### Function-Input Script
```python
inputs.salesforce_case_id = incident.properties.salesforce_case_id
results = playbook.functions.results.salesforce_case_results
inputs.salesforce_comment_text = "This Salesforce case created from SOAR case {0} URL: {1}".format(incident.id, playbook.functions.results.salesforce_case_results.content.salesforce_case.soar_case_url)
```

---

## Local script - Salesforce: Update SOAR Case with Salesforce Case Details

### Description
Salesforce: Update SOAR Case with Salesforce Case Details

### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.salesforce_case_results
content = results.get("content")
salesforce_case = content.get("salesforce_case")

if results.success:
  incident.properties.salesforce_case_id = salesforce_case.get("id")  
  incident.properties.salesforce_case_number = salesforce_case.get("CaseNumber")
  note_text = "<b>Salesforce: Created Case in Salesforce</b> created Case with CaseId: {}".format(salesforce_case.get("id", None))
  if salesforce_case.get("entity_url", None):
    note_text = note_text + "   <a target='_blank' href='{0}'>Link</a>".format(salesforce_case.get("entity_url"))
else:
  note_text = "<b>Salesforce: Create Case in Salesforce</b> failed:<br>{}".format(salesforce_case.get("error", None))
  
incident.addNote(note_text)
```

---
## Local script - Salesforce: Write sync task results to a note 

### Description
Write results of sync task function to a note.

### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.sync_task_results

if results.success:
  note_text = "<b>Salesforce: Sync Tasks</b> added:<br> {0} tasks in Salesforce<br> {1} tasks in SOAR".format(results.content.task_count_to_salesforce, results.content.task_count_to_soar)
else:
  note_text = "<b>Salesforce: Sync Tasks</b> FAILED and was unable to add tasks"

incident.addNote(note_text)
```

---

