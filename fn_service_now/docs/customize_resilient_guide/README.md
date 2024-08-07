# SOAR Customization Guide

## Overview
This package contains 8 Functions, 19 playbooks, and 1 Data Table that, when used along side our ServiceNow App help you integrate with your ServiceNow Instance.

* [SNOW: Create Record](#snow-create-record) gives you the ability to create a Record in ServiceNow from a SOAR Case/Incident or Task.
* [SNOW: Update Record](#snow-update-record) allows you to update multiple column fields in a ServiceNow Record.
* [SNOW: Close Record](#snow-close-record) lets you close a related Record in ServiceNow from a SOAR Case/Incident or Task.
* [SNOW: Add Note to Record](#snow-add-note-to-record) allows you to send a SOAR Note to a ServiceNow Record as a `Work Note` or `Additional Comment`.
* [SNOW: Add Attachment to Record](#snow-add-attachment-to-record) gives you the ability to send a SOAR Attachment to a ServiceNow Record.
* [SNOW: Lookup sys_id](#snow-lookup-sys_id) queries your ServiceNow Instance for a Record and returns the `sys_id` of that Record.
* [SNOW Helper: Update Data Table](#snow-helper-update-data-table) helper function that updates the ServiceNow Records Data Table status.

Some playbooks from the app are disabled by default. These are the automatic playbooks. Enable them after import for full app functionality.

---

## App Config Settings (app.config)
```
[fn_service_now]
sn_host=https://instance.service-now.com
sn_api_uri=/api/x_ibmrt_resilient/api

# 'sn_table_name': Name of the table in ServiceNow to create a record with.
# 'incident' table and the 'sn_si_incident' table are both supported
# (NOTE: ServiceNow Security Incident Response module is required for sn_si_incident)
# as of v2.3.0 this setting is no longer required. It is now only used in the playbooks
# labeled [DEPRECATED]
sn_table_name=incident

# Username + Password of ServiceNow Integrator user who has the the "x_ibmrt_resilient.integrator" role
sn_username=<ServiceNow Username>
sn_password=<ServiceNow Password>

# (ONLY FOR CP4S with custom endpoint) Enter the custom cases-rest prefix of your CP4S instance
# ex: if host is my-cases-rest.cp4s.ibmsecurity.com, cp4s_cases_prefix=my-cases-rest
# If you don't have a custom cases rest endpoint there is no need to use this config value
#cp4s_cases_prefix=<CP4S Cases Rest Custom Prefix>

# OPTIONAL: render notes in rich, formatted text when sent to SNOW
# only available to users who have `glide.ui.security.allow_codetag`
# enabled on their SNOW system. Set to `True` to properly render HTML notes
# render_rich_text = False
```

### A note on `sn_table_name`
Since v2.3.0, the value set in app.config for `sn_table_name` is simply used as the default table
in which to create new records in ServiceNow when sending data from SOAR. This can be overridden
by setting the table name as an input to the Create Record function.

A distinction is now also made to synchronize any record create in SOAR from ServiceNow with its
original table in ServiceNow. This means that the `sn_table_name` is no longer read in from app.config
for any synchronization functions and is rather read from the underlying data of the record in ServiceNow.
You'll notice this change in the addition of a column in the ServiceNow Records datatable in SOAR to
reflect the originating table name.

---

## Functions

 ![screenshot](./screenshots/1.png)

### SNOW: Create Record
Uses the `/create` custom endpoint in ServiceNow to create a ServiceNow Record from an IBM SOAR Case/Incident or Task.

Since version 2.3.0 `sn_table_name` was introduced as an optional input to this function. This now allows a Playbook designer to craft playbooks that create records in different tables in ServiceNow. The previous behavior (of using the table set in app.config for all record creation) is maintained by default. See the **Inputs** section for more details on how to use `sn_table_name`.

 ![screenshot](./screenshots/2.png)


<details><summary>Inputs:</summary>

| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| `incident_id` | `Number` | Yes | `2105` | ID of the SOAR Case/Incident |
| `task_id` | `Number` | No | `None` | ID of the SOAR Task |
| `sn_init_work_note` | `String` | No | `"This Incident originated from our Cyber Security Team using the IBM SOAR platform"` | Initial Work Note to be added to the new ServiceNow Record |
| `sn_optional_fields` | `JSON String` | No | `'{"assignment_group": "IT Security"}'` | An extensible JSON String of the field names and values to set in the new ServiceNow Record |
| `sn_table_name` | `String` | No | `"incident"` | Optional table in which to create this record in ServiceNow. For task creation, this is set by default to the table of the parent incident. When not set via function inputs this always defaults to the value in app.config. |

>**NOTE:** by default this function:
> * sets `short_description` in ServiceNow as the `incident.name` or `task.name`
> * sets `description` in ServiceNow as the `incident.description` or `task.instructions`
> * sets `work_notes` in ServiceNow as the `sn_init_work_note` function input
>
> **These defaults can be overwritten** by passing values from them in the `sn_optional_fields` input. To do this you would extend the example input Script provided with the following:
> ```python
> inputs.sn_optional_fields = dumps({
>     "short_description": "Custom Short Description",
>     "description": "Custom Long Description"
> })
> ```

</details>

<details><summary>Output:</summary>

```python
results = {
  "version": "1.0",
  "success": true,
  "reason": null,
  "content": {
    "success": true,
    "reason": null,
    "inputs": {
      "incident_id": 2117,
      "task_id": 103,
      "sn_init_work_note": "Record created from IBM SOAR Task ID: 103. Associated IBM SOAR Incident ID: 2117.\n\nSync task to SNOW",
      "sn_optional_fields": {
        "short_description": "RES-2117-103: Sample task",
        "assignment_group": "12a586cd0bb23200ecfd818393673a30",
        "caller_id": false
      }
    },
    "row_id": 29,
    "res_id": "RES-2117-103",
    "res_link": "https://9.30.213.40/#incidents/2117?task_id=103",
    "sn_ref_id": "SIR0010025",
    "sn_sys_id": "3294cbfa1b4d09103351ca2b234bcbfa",
    "sn_record_state": "Analysis",
    "sn_record_link": "https://xxxx.service-now.com/nav_to.do?uri=sn_si_incident.do?sysparm_query=number=SIR0010025",
    "sn_time_created": 1642522089472
  },
  "raw": "{\"success\": true, \"reason\": null, \"inputs\": {\"incident_id\": 2117, \"task_id\": 103, \"sn_init_work_note\": \"Record created from IBM SOAR Task ID: 103. Associated IBM SOAR Incident ID: 2117.\\n\\nSync task to SNOW\", \"sn_optional_fields\": {\"short_description\": \"RES-2117-103: Sample task\", \"assignment_group\": \"12a586cd0bb23200ecfd818393673a30\", \"caller_id\": false}}, \"row_id\": 29, \"res_id\": \"RES-2117-103\", \"res_link\": \"https://9.30.213.40/#incidents/2117?task_id=103\", \"sn_ref_id\": \"SIR0010025\", \"sn_sys_id\": \"3294cbfa1b4d09103351ca2b234bcbfa\", \"sn_record_state\": \"Analysis\", \"sn_record_link\": \"https://xxxx.service-now.com/nav_to.do?uri=sn_si_incident.do?sysparm_query=number=SIR0010025\", \"sn_time_created\": 1642522089472}",
  "inputs": {
    "incident_id": 2117,
    "task_id": 103,
    "sn_init_work_note": "Record created from IBM SOAR Task ID: 103. Associated IBM SOAR Incident ID: 2117.\n\nSync task to SNOW",
    "sn_optional_fields": {
      "short_description": "RES-2117-103: Sample task",
      "assignment_group": "12a586cd0bb23200ecfd818393673a30",
      "caller_id": false
    }
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-service-now",
    "package_version": "2.0.0",
    "host": "myhost",
    "execution_time_ms": 1485,
    "timestamp": "1971-01-01 00:00:00"
  },
  "row_id": 29,
  "res_id": "RES-2117-103",
  "res_link": "https://9.30.213.40/#incidents/2117?task_id=103",
  "sn_ref_id": "SIR0010025",
  "sn_sys_id": "3294cbfa1b4d09103351ca2b234bcbfa",
  "sn_record_state": "Analysis",
  "sn_record_link": "https://xxxx.service-now.com/nav_to.do?uri=sn_si_incident.do?sysparm_query=number=SIR0010025",
  "sn_time_created": 1642522089472
}
```

</details>


<details><summary>Example Input Script:</summary>

* We also make use of user inputs from **Rule Activity Fields** by using: `playbook.inputs.sn_initial_note`.
* In the supplied example playbook, there are 3 Functions chained together, with this Function being the third.
  * We use the output of the first and second functions here:
    ```python
        "assignment_group": playbooks.functions.results.assignment_group.sys_id,
        "caller_id": playbooks.functions.results.caller_id.sys_id
    ```

```python
from json import dumps
# Map IBM SOAR severity values to ServiceNow severity values
sn_severity_map = {
  "High": 1,
  "Medium": 2,
  "Low": 3
}

# Default text of the initial note added to the ServiceNow Record
init_snow_note_text = f"""Record created from a IBM SOAR Incident ID: {incident.id}.
                          Severity: {incident.severity_code}
                          Incident Type(s): {', '.join(incident.incident_type_ids)}"""

# If the user adds a comment when they invoke the rule, that comment gets concatenated here
initial_note = None
if getattr(playbook.inputs, "sn_initial_note", None):
  initial_note = getattr(playbook.inputs, "sn_initial_note", None).content
if initial_note:
  init_snow_note_text = f"{init_snow_note_text}\n\n{initial_note}"

# ID of this incident
inputs.incident_id = incident.id

# Initial work note to attach to created ServiceNow Record
inputs.sn_init_work_note = init_snow_note_text

# Parse the urgency and impact numbers value from the text input and incident severity, respectively
impact = sn_severity_map[incident.severity_code]
urgency = int(playbook.inputs.sn_urgency[0])

# Any further information you want to send to ServiceNow. Each Key/Value pair is attached to the Request object and accessible in ServiceNow.
# ServiceNow Example: setValue('assignment_group', request.body.data.sn_optional_fields.assignment_group)
inputs.sn_optional_fields = dumps({
  "short_description": f"RES-{incident.id}: {incident.name}",
  "impact": impact,
  "urgency": urgency,
  "assignment_group": playbook.functions.results.assignment_group.get("sys_id"),
  "caller_id": playbook.functions.results.caller_id.get("sys_id")
})

# This makes sure this creates this record in the "incident" table
inputs.sn_table_name = "incident"
```

</details>

<details><summary>Example Post-Processing Script:</summary>

* This example updates two Custom Incident Fields **sn_snow_record_id** and **sn_snow_record_link** then **adds a Note to the Incident**
```python
results = playbook.functions.results.create_record
if results.get("success"):
  # Set incident fields sn_snow_record_id, sn_snow_record_link, and sn_snow_table_name
  incident.sn_snow_record_id = results.get("sn_ref_id")
  incident.sn_snow_record_link = f"""<a href='{results.get('sn_record_link')}'>Link</a>"""
  incident.sn_snow_table_name = results.get("sn_table_name")

  noteText = f"""<br>This Incident has been created in <b>ServiceNow</b> with Urgency '{playbook.inputs.sn_urgency}'in the {results.get('sn_table_name')} table.
              <br><b>ServiceNow ID:</b>  {results.get('sn_ref_id')}
              <br><b>ServiceNow Link:</b> <a href='{results.get('sn_record_link')}'>{results.get('sn_record_link')}</a>"""

  incident.addNote(helper.createRichText(noteText))
```

</details>

---

### SNOW: Update Record
Uses the `/update` custom endpoint in ServiceNow to update a ServiceNow Record with a given dictionary of field name/value pairs.

 ![screenshot](./screenshots/8.png)

<details><summary>Inputs:</summary>

| Name | Type | Required | Example | Info |
| ---- | :--: | :------: | ------- | ---- |
| `incident_id` | `Number` | Yes | `1001` | ID of the SOAR Incident |
| `task_id` | `Number` | No | `20000002` or `None` | The ID of the SOAR Task |
| `sn_res_id` | `String` | No | `"RES-1001"` or `"RES-1001-20000002"` | This ID is an accumulation of the SOAR Incident and/or Task ID. It is stored in the `sn_records_dt` Data Table |
| `sn_update_fields` | `JSON String` | No | `'{"assignment_group": "IT Security"}'` | A JSON String of the ServiceNow field name and values you want to update. In our examples below we use the `dict_to_json_str(d)` Python Function to generate this JSON String. |

</details>

<details><summary>Output:</summary>

```python
results = {
  "version": "1.0",
  "success": true,
  "reason": null,
  "content": {
    "success": true,
    "inputs": {
      "incident_id": 2117,
      "task_id": null,
      "sn_res_id": null,
      "sn_update_fields": {
        "severity": 1
      }
    },
    "sn_ref_id": "SIR0010024",
    "sn_time_updated": 1642522493078
  },
  "raw": "{\"success\": true, \"inputs\": {\"incident_id\": 2117, \"task_id\": null, \"sn_res_id\": null, \"sn_update_fields\": {\"severity\": 1}}, \"sn_ref_id\": \"SIR0010024\", \"sn_time_updated\": 1642522493078}",
  "inputs": {
    "incident_id": 2117,
    "task_id": null,
    "sn_res_id": null,
    "sn_update_fields": {
      "severity": 1
    }
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-service-now",
    "package_version": "2.0.0",
    "host": "myhost",
    "execution_time_ms": 1485,
    "timestamp": "1971-01-01 00:00:00"
  },
  "sn_ref_id": "SIR0010024",
  "sn_time_updated": 1642522493078
}
```

</details>

<details><summary>Example input Script:</summary>

```python
from json import dumps
# Map IBM SOAR severity values to ServiceNow severity values
sn_severity_map = {
  "High": 1,
  "Medium": 2,
  "Low": 3
}

# Get the id of this incident
inputs.incident_id = incident.id

# List all the fields you want to update in the ServiceNow Record here with the ServiceNow field_name being the key
inputs.sn_update_fields = dumps({
  "severity": sn_severity_map[incident.severity_code],
})
```

</details>

<details><summary>Post-Processing Script:</summary>

* This example **adds a Note to the Incident**
```python
# Add a Note to the Incident
incident.addNote(f"The Severity of this Incident was updated to {incident.severity_code} in IBM SOAR")
```

</details>

#### Sending SOAR artifacts to SNOW
You can utilize the SNOW: Update Record function to send artifact values to SNOW records. The previous example for update is set to synchronize the severity of a SOAR record to the desired field in SNOW on update. To synchronize on artifact values:

1. Using the resilient-sdk, `clone` the example playbook into a new playbook with `changetype` artifact.
    ```
    resilient-sdk clone --playbook example_snow_update_record_on_severity_change <new_playbook_name> --changetype artifact
    ```
    More information on the resilient-sdk and the `clone` command can be found [here](https://ibmresilient.github.io/resilient-python-api/pages/resilient-sdk/resilient-sdk.html#clone).
1. Modify the input script to map desired artifact values to SNOW record fields using the `sn_update_fields` parameter of the "SNOW: Update Record" function.
    ```python
    inputs.sn_update_fields = dumps({
      "my_snow_column_name": artifact.value # When the artifact type is IP Address the value will be the IP
    })
    ```
1. Create a SOAR Rule to either manually or automatically trigger this new playbook.

---

### SNOW: Close Record
Uses the `/close_record` custom endpoint in ServiceNow to change the state of a ServiceNow Record and add Close Notes and a Close Code to the Record.

 ![screenshot](./screenshots/3.png)

<details><summary>Inputs:</summary>

| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| `incident_id` | `Number` | Yes | `2105` | ID of the SOAR Incident |
| `task_id` | `Number` | No | `2251401` | ID of the SOAR Task |
| `sn_record_state` | `Number` | Yes | `7` | These are defined in ServiceNow (See Note below) |
| `sn_close_notes` | `String` | Yes | `"We have closed this Incident"` | The notes required to close an Incident Record in ServiceNow |
| `sn_close_code` | `String` | Yes | `"Solved (Work Around)"` | These are defined in ServiceNow (See Note below). We use an Activity Field in the Rule to define a Select field, where we list all the possible close_codes |
| `sn_close_work_note` | `String` | Yes | `"This record's state has be changed to 'Resolved' by IBM SOAR"`  | If defined this text is added as a Work Note to the ServiceNow Record |

>**NOTE:**
> * If using the **Security Incident Response** table, the initial state of the created ServiceNow record is the ``Analysis`` state. This state must be changed to the ``Contain`` or other state to allow the ServiceNow Record to be closed otherwise this ``Close`` action will be ignored.
> * To see your record_state and close_codes value in ServiceNow go to **System Definition** > **Dictionary** > **Table Name** > **Incident** > **Column Name** > **incident state/close_code** and see their label and values.
> * It is the value that we send from SOAR to ServiceNow.
>
> **Record State:**
>![screenshot](./screenshots/4.png)
>
> **Close Code:**
> ![screenshot](./screenshots/5.png)

</details>

<details><summary>Output:</summary>

```python
results = {
  "version": "1.0",
  "success": true,
  "reason": null,
  "content": {
    "success": true,
    "reason": null,
    "inputs": {
      "incident_id": 2117,
      "task_id": null,
      "sn_res_id": "RES-2117",
      "sn_record_state": 100,
      "sn_close_notes": "Closing",
      "sn_close_code": "Threat mitigated",
      "sn_close_work_note": "This record's state has be changed to [SIR] Review by IBM SOAR"
    },
    "sn_ref_id": "SIR0010024",
    "sn_record_state": "Review"
  },
  "raw": "{\"success\": true, \"reason\": null, \"inputs\": {\"incident_id\": 2117, \"task_id\": null, \"sn_res_id\": \"RES-2117\", \"sn_record_state\": 100, \"sn_close_notes\": \"Closing\", \"sn_close_code\": \"Threat mitigated\", \"sn_close_work_note\": \"This record's state has be changed to [SIR] Review by IBM SOAR\"}, \"sn_ref_id\": \"SIR0010024\", \"sn_record_state\": \"Review\"}",
  "inputs": {
    "incident_id": 2117,
    "task_id": null,
    "sn_res_id": "RES-2117",
    "sn_record_state": 100,
    "sn_close_notes": "Closing",
    "sn_close_code": "Threat mitigated",
    "sn_close_work_note": "This record's state has be changed to [SIR] Review by IBM SOAR"
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-service-now",
    "package_version": "2.0.0",
    "host": "myhost",
    "execution_time_ms": 1485,
    "timestamp": "1971-01-01 00:00:00"
  },
  "sn_ref_id": "SIR0010024",
  "sn_record_state": "Review"
}
```

</details>

<details><summary>Example input Script:</summary>

* This example **creates a Python Dictionary** to map the ServiceNow States to their corresponding numeric value.
> * *Note that for SIR tables, the record state options are new. If you intend to only use this with SIR or INC tables exclusively, you can remove the ones here that you don't need. These string values correspond to the Activity Field SN Record State which can be customized as well.*

```python
# A Dictionary that maps Record States to their corresponding codes
# These codes are defined in ServiceNow and may be different for each ServiceNow configuration
# Codes prepended with [SIR] are specific to Security Incident Response incidents
map_sn_record_states = {
  "New": 1,
  "In Progress": 2,
  "On Hold": 3,
  "Resolved": 6,
  "Closed": 7,
  "Canceled": 8,
  "Cancelled": 8 # servicenow has inconsistent spellings of this word...
}

# ID of this incident
inputs.incident_id = incident.id

# The state to change the record to
# inputs.sn_record_state = map_sn_record_states["Closed"]
inputs.sn_record_state = map_sn_record_states[getattr(playbook.inputs, "sn_record_state", None)]

# The resolution notes that are normally required when you close a ServiceNow record
# inputs.sn_close_notes = "This incident has been resolved in IBM SOAR. No further action required"
if getattr(playbook.inputs, "sn_close_notes", None):
  inputs.sn_close_notes = getattr(playbook.inputs, "sn_close_notes", None)

# The ServiceNow 'close_code' that you normally select when closing a ServiceNow record
# inputs.sn_close_code = "Solved (Permanently)"
if getattr(playbook.inputs, "sn_close_code", None):
  inputs.sn_close_code = getattr(playbook.inputs, "sn_close_code", None)

# Add a Work Note to the Record in ServiceNow
inputs.sn_close_work_note = f"This record's state has been changed to {playbook.inputs.sn_record_state} by IBM SOAR"
```

</details>

<details><summary>Post-Processing Script:</summary>

* This example **adds a Note to the Incident** detailing why the Incident was closed or if the playbook **fails** to close the ServiceNow Record
```python
results = playbook.functions.results.close_record
if results.get("success"):
  note_text = f"""<br>This Incident has been updated in <b>ServiceNow</b>
              <br><b>ServiceNow ID:</b> {results.get('sn_ref_id')}
              <br><b>ServiceNow Record State:</b> {results.get('sn_record_state')}
              <br><b>ServiceNow Closing Notes:</b> {results.get('inputs', {}).get('sn_close_notes')}
              <br><b>ServiceNow Closing Code:</b> {results.get('inputs', {}).get('sn_close_code')}"""
else:
  note_text = f"""<br>Failed to close this Incident in <b>ServiceNow</b>
              <br><b>Reason:</b> {results.get('reason')}"""

incident.addNote(helper.createRichText(note_text))
```

</details>

---

### SNOW: Add Note to Record
Uses the `/add` custom endpoint in ServiceNow to add a SOAR Note to a ServiceNow Record as a "Work Note" or "Additional Comment".

 ![screenshot](./screenshots/6.png)

<details><summary>Inputs:</summary>

| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| `incident_id` | `Number` | Yes | `2105` | ID of the SOAR Incident |
| `task_id` | `Number` | No | `2251401` | ID of the SOAR Task |
| `sn_note_text` | `String` | Yes | `"Can your team look into this please"` | Text of the new ServiceNow Note |
| `sn_note_type` | `Select` | Yes | `"work_note"` OR `"additional_comment"` | Note type. Either `Work Note` or `Additional Comment` |

</details>

<details><summary>Output:</summary>

```python
results = {
  "version": "1.0",
  "success": true,
  "reason": null,
  "content": {
    "success": true,
    "inputs": {
      "incident_id": 2117,
      "task_id": null,
      "sn_note_text": "The Business Impact of this Incident was updated to High in IBM SOAR",
      "sn_note_type": "work_note"
    },
    "res_id": "RES-2117",
    "sn_ref_id": "SIR0010024"
  },
  "raw": "{\"success\": true, \"inputs\": {\"incident_id\": 2117, \"task_id\": null, \"sn_note_text\": \"The Business Impact of this Incident was updated to High in IBM SOAR\", \"sn_note_type\": \"work_note\"}, \"res_id\": \"RES-2117\", \"sn_ref_id\": \"SIR0010024\"}",
  "inputs": {
    "incident_id": 2117,
    "task_id": null,
    "sn_note_text": "The Business Impact of this Incident was updated to High in IBM SOAR",
    "sn_note_type": "work_note"
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-service-now",
    "package_version": "2.0.0",
    "host": "myhost",
    "execution_time_ms": 1485,
    "timestamp": "1971-01-01 00:00:00"
  },
  "res_id": "RES-2117",
  "sn_ref_id": "SIR0010024"
}
```

</details>

<details><summary>Example input Script:</summary>

```python
inputs.sn_note_type = "work_note"
# The id of this incident
inputs.incident_id = incident.id

# If this is a task note, get the taskId
if note.type == 'task':
  # Set the task_id
  inputs.task_id = task.id

# Get the text of the note
inputs.sn_note_text = note.text.content
```

</details>

<details><summary>Post-Processing Script:</summary>

This example prepends a timestamp to the SOAR Note to track when the Note was sent to ServiceNow.
```python
from datetime import datetime
note.text = f"<b>Sent to ServiceNow at {datetime.now()}</b><br>{note.text.content}"
```

</details>

---

### SNOW: Add Attachment to Record
Uses the `/add` custom endpoint in ServiceNow to add a SOAR Attachment to a ServiceNow Record.

 ![screenshot](./screenshots/7.png)

<details><summary>Inputs:</summary>

| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| `attachment_id` | `Number` | Yes | `39` | ID of the SOAR Attachment |
| `incident_id` | `Number` | Yes | `2105` | ID of the SOAR Incident |
| `task_id` | `Number` | No | `2251401` | ID of the SOAR Task |

</details>

<details><summary>Output:</summary>

```python
results = {
  "version": "1.0",
  "success": true,
  "reason": null,
  "content": {
    "success": true,
    "inputs": {
      "attachment_id": 2,
      "incident_id": 2117,
      "task_id": null
    },
    "res_id": "RES-2117",
    "sn_ref_id": "SIR0010024",
    "attachment_name": "sample_attachment.png",
    "sn_attachment_sys_id": "ef44473e1b4d09103351ca2b234bcbc6"
  },
  "raw": "{\"success\": true, \"inputs\": {\"attachment_id\": 2, \"incident_id\": 2117, \"task_id\": null}, \"res_id\": \"RES-2117\", \"sn_ref_id\": \"SIR0010024\", \"attachment_name\": \"sample_attachment.png\", \"sn_attachment_sys_id\": \"ef44473e1b4d09103351ca2b234bcbc6\"}",
  "inputs": {
    "attachment_id": 2,
    "incident_id": 2117,
    "task_id": null
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-service-now",
    "package_version": "2.0.0",
    "host": "myhost",
    "execution_time_ms": 1485,
    "timestamp": "1971-01-01 00:00:00"
  },
  "res_id": "RES-2117",
  "sn_ref_id": "SIR0010024",
  "attachment_name": "sample_attachment.png",
  "sn_attachment_sys_id": "ef44473e1b4d09103351ca2b234bcbc6"
}
```

</details>

<details><summary>Example input Script:</summary>

```python
# The id of this attachment
inputs.attachment_id = attachment.id

# The id of this incident
inputs.incident_id = incident.id

# If this is a task attachment, get the taskId
if attachment.type == 'task':
  inputs.task_id = task.id
```

</details>

<details><summary>Post-Processing Script:</summary>

* This example **adds a Note to the Incident/Task** detailing what attachment was sent to ServiceNow.
```python
results = playbook.functions.results.add_attachment
if results.get("success"):

  noteText = f"""<br>{principal.display_name} has added an attachment to <b>ServiceNow</b>
              <br><b>Attachment Name:</b>  {results.attachment_name}
              <br><b>ServiceNow ID:</b>  {results.get('sn_ref_id')}"""

  # If this is a task attachment, add a note to the Task
  if task:
    task.addNote(helper.createRichText(noteText))
  # Else add the note to the Incident
  else:
    incident.addNote(helper.createRichText(noteText))
```

</details>

---

### SNOW: Lookup sys_id
* Gets the `sys_id` of a ServiceNow Record.
* Used when creating a ServiceNow Record to get the `sys_id` of the `assignment_group` to assign the new Record to.

 ![screenshot](./screenshots/2.png)

<details><summary>Inputs:</summary>

| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| `sn_table_name` | `String` | Yes | `"sys_user_group"` | The table name in ServiceNow to query |
| `sn_query_field` | `String` | Yes | `"name"` | The column name in the table you want to query |
| `sn_query_value` | `String` | Yes | `"IT Securities"` | The cell value in the column you want to query |

</details>

<details><summary>Output:</summary>

```python
results = {
  "version": "1.0",
  "success": false,
  "reason": null,
  "content": {
    "success": false,
    "inputs": {
      "sn_query_field": "email",
      "sn_table_name": "sys_user",
      "sn_query_value": "ibmresilient"
    },
    "sys_id": null
  },
  "raw": "{\"success\": false, \"inputs\": {\"sn_query_field\": \"email\", \"sn_table_name\": \"sys_user\", \"sn_query_value\": \"ibmresilient\"}, \"sys_id\": null}",
  "inputs": {
    "sn_query_field": "email",
    "sn_table_name": "sys_user",
    "sn_query_value": "ibmresilient"
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-service-now",
    "package_version": "2.0.0",
    "host": "myhost",
    "execution_time_ms": 1485,
    "timestamp": "1971-01-01 00:00:00"
  },
  "sys_id": null
}
```

</details>

<details><summary>Example input Script:</summary>

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

</details>

<details><summary>Post-Processing Script:</summary>

*There is generally no Post-Process Script for this Function. Its output is normally used as an input to the **Create in ServiceNow** function.*

</details>

---

### SNOW Helper: Update Data Table

 ![screenshot](./screenshots/10.png)

<details><summary>Inputs:</summary>

| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| `incident_id` | `Number` | Yes | `2105` | ID of the Incident |
| `task_id` | `Number` | No | `2251401` | ID of the Task |
| `sn_resilient_status` | `String` | Yes | `"C"` | "A"=Active Incident, "O"=Open Task, "C"=Closed Incident/Task |

</details>

<details><summary>Output:</summary>

```python
results = {
  "version": "1.0",
  "success": true,
  "reason": null,
  "content": {
    "success": true,
    "inputs": {
      "incident_id": 2117,
      "task_id": null,
      "sn_resilient_status": "C"
    },
    "res_id": "RES-2117",
    "row_id": 28
  },
  "raw": "{\"success\": true, \"inputs\": {\"incident_id\": 2117, \"task_id\": null, \"sn_resilient_status\": \"C\"}, \"res_id\": \"RES-2117\", \"row_id\": 28}",
  "inputs": {
    "incident_id": 2117,
    "task_id": null,
    "sn_resilient_status": "C"
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-service-now",
    "package_version": "2.0.0",
    "host": "myhost",
    "execution_time_ms": 1485,
    "timestamp": "1971-01-01 00:00:00"
  },
  "res_id": "RES-2117",
  "row_id": 28
}
```

</details>

<details><summary>Example input Script:</summary>

```python
# Get the incident id
inputs.incident_id = incident.id

# Get the new status of the incident
inputs.sn_resilient_status = incident.plan_status
```

</details>

<details><summary>Post-Processing Script:</summary>

*There is generally no Post-Process Script for this Function.*

</details>

---

## Playbooks
Some playbooks from the app are disabled by default. These are the automatic playbooks. Enable them after import for full app functionality.

Since v2.3.0 some older playbooks have been removed:

* **[SIR] Update Record on Severity Change (PB)**

Since v2.3.0 two playbooks have been "Deprecated" and are disabled upon upgrade:

* **[DEPRECATED] SNOW: Create New Record (PB)** (formerly `SNOW: Create New Record (PB)`)
* **[DEPRECATED] SNOW: Update/Close Record [Task] (PB)** (formerly `SNOW: Update/Close Record [Task] (PB)`)

These deprecated playbooks are no longer intended for production use and should no longer be used as they are limited in their capabilities.
They rely on the deprecated `sn_table_name` config which is no longer fully supported. See [section below](#a-note-on-sn_table_name) for more information.
These deprecated playbooks might be removed completely in a future release.

| Playbook Name | Description | Activation Type | Object | Status | Condition |
| ------------- | ----------- | --------------- | ------ | ------ | --------- |
| SNOW: Add Attachment to Record (PB) | Send this attachment to the associated record in ServiceNow. | Manual | attachment | `enabled` | `incident.properties.sn_snow_record_id has_a_value` |
| SNOW: Close Incident on Datatable Value Change (PB) | Automatically closes the case/incident in SOAR when the status of the record in ServiceNow is changed to "Closed" or "Resolved." | Automatic | sn_records_dt | `disabled` | `(sn_records_dt.sn_records_dt_snow_status contains Closed OR sn_records_dt.sn_records_dt_snow_status contains Resolved) AND sn_records_dt.sn_records_dt_type equals Incident ` |
| SNOW: Create Child Incident (PB) | Create a new 'incident' record in ServiceNow based off of the linked parent incident. | Manual | task | `enabled` | `incident.properties.sn_snow_record_id has_a_value AND incident.properties.sn_snow_table_name equals incident` |
| SNOW: Create New Incident (PB) | Creates a new record in the Incident (incident) table in ServiceNow. | Manual | incident | `enabled` | `incident.properties.sn_snow_record_id not_has_a_value` |
| SNOW: Create New Security Incident (PB) | Creates a new record in the Security Incident (sn_si_incident) table in ServiceNow. Note that this option is only available if your ServiceNow instance is configured with the Security Response module. | Manual | incident | `enabled` | `incident.properties.sn_snow_record_id not_has_a_value` |
| SNOW: Create New Record from Task (PB) | NOTE: Since v2.3.0, consider using "Create Child Incident" or "Create Security Response Task" playbooks which maintain the relationship of the task to the case better than this playbook does.  Create a new record from the selected task. This will create the new record in the same ServiceNow table (incident vs sn_si_incident) that the SOAR case is associated with. If the case in SOAR isn't linked to a record in ServiceNow, the table will default to the value set by sn_table_name in the app.config. | Manual | task | `enabled` | `-` |
| SNOW: Create Security Response Task (PB) | Create a Security Response Task linked to the parent Security Incident of this task's parent incident. | Manual | task | `enabled` | `incident.properties.sn_snow_record_id has_a_value AND incident.properties.sn_snow_table_name equals sn_si_incident` |
| SNOW: Update Record on Severity Change (PB) | | Automatic | incident | `disabled` | `incident.properties.sn_snow_record_id has_a_value AND incident.severity_code changed` |
| SNOW: Send as Additional Comment (PB) | | Manual | note | `enabled` | `note.text not_contains Sent to ServiceNow at` |
| SNOW: Send as Work Note (PB) | | Manual | note | `enabled` | `note.text not_contains Sent to ServiceNow at` |
| SNOW: Update Data Table on Status Change [Incident] (PB) | | Automatic | incident | `disabled` | `incident.plan_status changed` |
| SNOW: Update Data Table on Status Change [Task] (PB) | | Automatic | task | `disabled` | `task.status changed` |
| SNOW: Update/Close Incident (PB) | Update the state of this record in the incident table in ServiceNow | Manual | incident | `enabled` | `incident.properties.sn_snow_record_id has_a_value AND incident.properties.sn_snow_table_name equals incident` |
| SNOW: Update/Close Record (PB) | Update the state of this record in the "incident" table in ServiceNow | Manual | sn_records_dt | `enabled` | `sn_records_dt.sn_records_dt_snow_table equals incident` |
| SNOW: Update/Close Response Task (PB) | Update the state of this record in the "sn_si_task" table in ServiceNow | Manual | sn_records_dt | `enabled` | `sn_records_dt.sn_records_dt_snow_table equals sn_si_task` |
| SNOW: Update/Close Security Incident (PB) | Update the state of this record in the "sn_si_incident" table in ServiceNow | Manual | sn_records_dt | `enabled` | `sn_records_dt.sn_records_dt_snow_table equals sn_si_incident` |
| SNOW: Update/Close SIR Incident (PB) | Update the state of this record in the "sn_si_incident" table in ServiceNow | Manual | incident | `enabled` | `incident.properties.sn_snow_record_id has_a_value AND incident.properties.sn_snow_table_name equals sn_si_incident` |
| [DEPRECATED] SNOW: Create New Record (PB) | Deprecated as of v2.3.0. Please use "SNOW: Create New Incident (PB)" to create "incident" records and "SNOW: Create New Security Incident (PB)" to create "sn_si_incident" records.  This playbook is used to create a new record in ServiceNow from this case in SOAR. It reads the sn_table_name config to determine the table in which to create the record. | Manual | incident | `disabled` | `incident.properties.sn_snow_record_id not_has_a_value` |
| [DEPRECATED] SNOW: Update/Close Record [Task] (PB) | Deprecated as of v2.3.0 because tasks don't contain enough information to distinguish between Security Incidents, Security Response Tasks, and Incidents. This playbook is now disabled by default. Please use the associated playbook for the record from the datatable. | Manual | task | `disabled` | `-` |

---

## Data Tables:

### ServiceNow Records
 ![screenshot](./screenshots/9.png)

#### API Name:
`sn_records_dt`

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Last Updated | `sn_records_dt_time` | `datetimepicker` | The time this row was last updated |
| Links | `sn_records_dt_links` | `textarea` | Opens the record in a new tab in either IBM SOAR or SNOW |
| Name | `sn_records_dt_name` | `text` | The name of the record |
| SNOW ID | `sn_records_dt_sn_ref_id` | `text` | ID of record in SNOW, unique to its table in SNOW |
| SNOW Parent ID | `sn_records_dt_sn_parent_ref_id` | `text` | ID of record's parent in SNOW if the record is a "child" record |
| SNOW Status | `sn_records_dt_snow_status` | `textarea` | The current status of the record in SNOW |
| SNOW Table | `sn_records_dt_snow_table` | `text` | The table in ServiceNow where this record exists |
| SOAR ID | `sn_records_dt_res_id` | `text` | Unique ID of IBM SOAR Incident or Task |
| SOAR Status | `sn_records_dt_res_status` | `textarea` | The current status of the Incident/Task in IBM SOAR |
| Type in SOAR | `sn_records_dt_type` | `text` | Type of the linked object in SOAR. Either Incident or Task |

---

## Custom Fields
| Label | API Access Name | Type | Prefix | Placeholder | Tooltip |
| ----- | --------------- | ---- | ------ | ----------- | ------- |
| ServiceNow Record | `sn_snow_record_link` | `textarea` | `properties` | - | Link to ServiceNow Record |
| ServiceNow Record ID | `sn_snow_record_id` | `text` | `properties` | - | ID of ServiceNow Record |
| ServiceNow Table Name | `sn_snow_table_name` | `text` | `properties` | incident | The name of the table in ServiceNow for the corresponding record |

---

## Links
- [IBM SOAR ServiceNow App Main Page](../../README.md)
- [Install Guide](../install_guide/README.md)
- [Customize ServiceNow App Guide](../customize_snow_guide/README.md)
