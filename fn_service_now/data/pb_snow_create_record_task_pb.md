<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Playbook - SNOW: Create New Record from Task (PB)

### API Name
`snow_create_record_task_pb`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| Add SOAR link to ServiceNow incident | `sn_add_soar_link_on_snow` | boolean | Add SOAR incident link to ServiceNow incident in a note. Defaults to True. | Optional |
| SN Assignment Group | `sn_assignment_group` | select | The group this record will be assigned to in ServiceNow | Always |
| SN Initial Note | `sn_initial_note` | textarea | - | Optional |

### Object Type
`task`

### Description
NOTE: Since v2.3.0, consider using "Create Child Incident" or "Create Security Response Task" playbooks which maintain the relationship of the task to the case better than this playbook does.

Create a new record from the selected task. This will create the new record in the same ServiceNow table (incident vs sn_si_incident) that the SOAR case is associated with. If the case in SOAR isn't linked to a record in ServiceNow, the table will default to the value set by sn_table_name in the app.config.


---
## Function - SNOW: Lookup sys_id

### API Name
`fn_snow_lookup_sysid`

### Output Name
`assignment_group`

### Message Destination
`fn_service_now`

### Function-Input Script
```python
# The table in ServiceNow to query
inputs.sn_table_name = "sys_user_group"

# The name of the field/table column to query
inputs.sn_query_field = "name"

# The value to equate the cell to
# Get the group name from the Rule Activity Field with:
inputs.sn_query_value = getattr(playbook.inputs, "sn_assignment_group", None)

## OR Set group name statically with:
## inputs.sn_query_value = "IT Securities"
```

---
## Function - SNOW: Lookup sys_id

### API Name
`fn_snow_lookup_sysid`

### Output Name
`caller_id`

### Message Destination
`fn_service_now`

### Function-Input Script
```python
# The table in ServiceNow to query
inputs.sn_table_name = "sys_user"

# The name of the field/table column to query
inputs.sn_query_field = "user_name"

# The value to equate the cell to
inputs.sn_query_value = "ibmresilient" #our integrations user in ServiceNow
```

---
## Function - SNOW: Create Record

### API Name
`fn_snow_create_record`

### Output Name
`create_record`

### Message Destination
`fn_service_now`

### Function-Input Script
```python
from json import dumps
# Default text of the initial note added to the ServiceNow Record
init_snow_note_text = f"""Record created from IBM SOAR Task ID: {task.id}. Associated IBM SOAR Incident ID: {incident.id}."""
# This can be true or false. True will add a link to the SOAR incident in a note on the ServiceNow incident.
inputs.sn_add_soar_link_on_snow = getattr(playbook.inputs, "sn_add_soar_link_on_snow", False)

# If the user adds a comment when they invoke the playbook, that comment gets concatenated here
initial_note = None
if getattr(playbook.inputs, "sn_initial_note", None):
  initial_note = playbook.inputs.sn_initial_note.content
if initial_note:
  init_snow_note_text = f"{init_snow_note_text}\n\n{initial_note}"

# ID of this incident
inputs.incident_id = incident.id

# ID of this task
inputs.task_id = task.id

# Initial work note to attach to created ServiceNow record
inputs.sn_init_work_note = init_snow_note_text

# Any further information you want to send to ServiceNow. Each Key/Value pair is attached to the Request object and accessible in ServiceNow.
# ServiceNow Example: setValue('assignment_group', request.body.data.sn_optional_fields.assignment_group)
inputs.sn_optional_fields = dumps({
  "short_description": f"RES-{incident.id}-{task.id}: {task.name}",
  "assignment_group": playbook.functions.results.assignment_group.get("sys_id"),
  "caller_id": playbook.functions.results.caller_id.get("sys_id")
})

# if the incident for this task has already been synced,
# send this task to the same table in ServiceNow
# if not set, defaults to the value set in app.config
inputs.sn_table_name = incident.properties.sn_snow_table_name
```

---

## Local script - SNOW post-process

### Description


### Script Type
`Local script`

### Object Type
`task`

### Script Content
```python
results = playbook.functions.results.create_record
if results.get("success"):

  note_text = f"""<br>This Task has been created in <b>ServiceNow</b> in the {results.get('sn_table_name')} table.
              <br><b>ServiceNow ID:</b>  {results.get('sn_ref_id')}
              <br><b>ServiceNow Link:</b> <a href='{results.get('sn_record_link')}'>{results.get('sn_record_link')}</a>"""

  task.addNote(helper.createRichText(note_text))

elif results.get("reason"):
  task.addNote(results.get("reason"))
```

---

