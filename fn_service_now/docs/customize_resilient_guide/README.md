# IBM Security QRadar SOAR Platform App for ServiceNow

## Table of Contents
- [App Config Settings](#app-config-settings-appconfig)
- [Functions](#functions)
  - [Function - SNOW: Create Record](#function---snow-create-record)
  - [Function - SNOW: Update Record](#function---snow-update-record)
    - [Sending SOAR artifacts to SNOW](#sending-soar-artifacts-to-snow)
  - [Function - SNOW: Close Record](#function---snow-close-record)
  - [Function - SNOW: Add Note to Record](#function---snow-add-note-to-record)
  - [Function - SNOW: Add Attachment to Record](#function---snow-add-attachment-to-record)
  - [Function - SNOW: Lookup sys_id](#function---snow-lookup-sys_id)
  - [Function - SNOW Helper: Update Data Table](#function---snow-helper-update-data-table)
- [Rules](#rules)
- [ServiceNow Records Data Table](#servicenow-records)
- [Security Incident Response Specific Customizations](#security-incident-response-specific-customizations)

---

# Overview:
This package contains 8 Functions, 12 Workflows, 12 Rules and 1 Data Table that, when used along side our ServiceNow App help you integrate with your ServiceNow Instance.

* [SNOW: Create Record](#function---snow-create-record) gives you the ability to create a Record in ServiceNow from a SOAR Case/Incident or Task.
* [SNOW: Update Record](#function---snow-update-record) allows you to update multiple column fields in a ServiceNow Record.
* [SNOW: Close Record](#function---snow-close-record) lets you close a related Record in ServiceNow from a SOAR Case/Incident or Task.
* [SNOW: Add Note to Record](#function---snow-add-note-to-record) allows you to send a SOAR Note to a ServiceNow Record as a `Work Note` or `Additional Comment`.
* [SNOW: Add Attachment to Record](#function---snow-add-attachment-to-record) gives you the ability to send a SOAR Attachment to a ServiceNow Record.
* [SNOW: Lookup sys_id](#function---snow-lookup-sysid) queries your ServiceNow Instance for a Record and returns the `sys_id` of that Record.
* [SNOW Helper: Update Data Table](#function---snow-helper-update-data-table) helper function that updates the ServiceNow Records Data Table status.

---

# App Config Settings (app.config):
```
[fn_service_now]
# Link to your ServiceNow Instance
sn_host=https://instance.service-now.com

# The URI to the ServiceNow App that handles the requests from SOAR
sn_api_uri=/api/x_ibmrt_resilient/api

# The name of the table in ServiceNow you want to integrate with
# as of v2.0 we support the 'incident' and 'sn_si_incident' tables
sn_table_name=incident

# Username and Password for your Administrative User in ServiceNow
sn_username=ibmresilient
sn_password=MyPassword
```

---

# Functions:

 ![screenshot](./screenshots/1.png)

## Function - SNOW: Create Record
Uses the `/create` custom endpoint in ServiceNow to create a ServiceNow Record from an IBM SOAR Case/Incident or Task.

 ![screenshot](./screenshots/2.png)


<details><summary>Inputs:</summary>

| Input Name | Type | Required | Example | Info |
| ---------- | :--: | :-------:| ------- | ---- |
| `incident_id` | `Number` | Yes | `2105` | ID of the SOAR Case/Incident |
| `task_id` | `Number` | No | `None` | ID of the SOAR Task |
| `sn_init_work_note` | `String` | No | `"This Incident originated from our Cyber Security Team using the IBM SOAR platform"` | Initial Work Note to be added to the new ServiceNow Record |
| `sn_optional_fields` | `JSON String` | No | `'{"assignment_group": "IT Security"}'` | An extensible JSON String of the field names and values to set in the new ServiceNow Record |

>**NOTE:** by default this function:
> * sets `short_description` in ServiceNow as the `incident.name` or `task.name`
> * sets `description` in ServiceNow as the `incident.description` or `task.instructions`
> * sets `work_notes` in ServiceNow as the `sn_init_work_note`
>
> **These defaults can be overwritten** by passing values from them in the `sn_optional_fields` input. To do this you would extend the example Pre-Process Script provided with the following:
> ```python
> inputs.sn_optional_fields = dict_to_json_str({
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


<details><summary>Example Pre-Processing Script:</summary>

* This example defines and uses the `dict_to_json_str` function to allow us to easily set optional_fields we want to send to ServiceNow.
* We also make use of user inputs from **Rule Activity Fields** by using: `rule.properties.sn_initial_note`.
* In the supplied example Workflow, there are 3 Functions chained together, with this Function being the third. 
  * We use the output of the first and second functions here: 
    ```python
        "assignment_group": workflow.properties.assignment_group.sys_id,
        "caller_id": workflow.properties.caller_id.sys_id
    ```

```python
#######################################
### Define pre-processing functions ###
#######################################
def dict_to_json_str(d):
  """Function that converts a dictionary into a JSON string.
     Supports types: basestring, bool, int and nested dicts.
     Does not support lists.
     If the value is None, it sets it to False."""

  json_entry = u'"{0}":{1}'
  json_entry_str = u'"{0}":"{1}"'
  entries = [] 

  for entry in d:
    key = entry
    value = d[entry]

    if value is None:
      value = False

    if isinstance(value, list):
      helper.fail('dict_to_json_str does not support Python Lists')

    if isinstance(value, basestring):
      value = value.replace(u'"', u'\\"')
      entries.append(json_entry_str.format(unicode(key), unicode(value)))
      
    elif isinstance(value, unicode):
      entries.append(json_entry.format(unicode(key), unicode(value)))
    
    elif isinstance(value, bool):
      value = 'true' if value == True else 'false'
      entries.append(json_entry.format(key, value))

    elif isinstance(value, int):
      entries.append(json_entry.format(unicode(key), value))

    elif isinstance(value, dict):
      entries.append(json_entry.format(key, dict_to_json_str(value)))

    else:
      helper.fail('dict_to_json_str does not support this type: {0}'.format(type(value)))

  return u'{0} {1} {2}'.format(u'{', ','.join(entries), u'}')

# Map IBM SOAR severity values to ServiceNow severity values
sn_severity_map = {
  "High": 1,
  "Medium": 2,
  "Low": 3
}

#####################
### Define Inputs ###
#####################

# Default text of the initial note added to the ServiceNow Record
init_snow_note_text = u"""Record created from a IBM SOAR Incident ID: {0}.
                          Severity: {1}
                          Incident Type(s): {2}""".format(incident.id, incident.severity_code, u", ".join(incident.incident_type_ids))

# If the user adds a comment when they invoke the rule, that comment gets concatenated here
if rule.properties.sn_initial_note.content is not None:
  init_snow_note_text = u"{0}\n\n{1}".format(init_snow_note_text, unicode(rule.properties.sn_initial_note.content))

# ID of this incident
inputs.incident_id = incident.id

# Initial work note to attach to created ServiceNow Record
inputs.sn_init_work_note = init_snow_note_text

# Any further information you want to send to ServiceNow. Each Key/Value pair is attached to the Request object and accessible in ServiceNow.
# ServiceNow Example:: setValue('assignment_group', request.body.data.sn_optional_fields.assignment_group)
# For SIR tables it is recommended to map "business_criticality" to sn_severity_map as that is visible in the SNOW query_builder
# (see the example commented out below)
inputs.sn_optional_fields = dict_to_json_str({
  "short_description": u"RES-{0}: {1}".format(incident.id, unicode(incident.name)),
  "severity": sn_severity_map[incident.severity_code],
  #"business_criticality": sn_severity_map[incident.severity_code],
  "assignment_group": workflow.properties.assignment_group.sys_id,
  "caller_id": workflow.properties.caller_id.sys_id
})
```

</details>

<details><summary>Example Post-Processing Script:</summary>

* This example updates two Custom Incident Fields **sn_snow_record_id** and **sn_snow_record_link** then **adds a Note to the Incident**
```python
if results.success:

  # Set incident fields sn_snow_record_id and sn_snow_record_link
  incident.sn_snow_record_id = results.sn_ref_id
  incident.sn_snow_record_link = """<a href='{0}'>Link</a>""".format(results.sn_record_link)
  
  noteText = """<br>This Incident has been created in <b>ServiceNow</b>
              <br><b>ServiceNow ID:</b>  {0}
              <br><b>ServiceNow Link:</b> <a href='{1}'>{1}</a>""".format(results.sn_ref_id, results.sn_record_link)

  incident.addNote(helper.createRichText(noteText))
```

</details>

---

## Function - SNOW: Update Record
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

<details><summary>Pre-Processing Script:</summary>

* This example uses `dict_to_json_str()` to generate a JSON String for the `sn_update_fields` input

```python
#######################################
### Define pre-processing functions ###
#######################################
def dict_to_json_str(d):
  """Function that converts a dictionary into a JSON string.
     Supports types: basestring, bool, int and nested dicts.
     Does not support lists.
     If the value is None, it sets it to False."""

  json_entry = u'"{0}":{1}'
  json_entry_str = u'"{0}":"{1}"'
  entries = [] 

  for entry in d:
    key = entry
    value = d[entry]

    if value is None:
      value = False

    if isinstance(value, list):
      helper.fail('dict_to_json_str does not support Python Lists')

    if isinstance(value, basestring):
      value = value.replace(u'"', u'\\"')
      entries.append(json_entry_str.format(unicode(key), unicode(value)))
      
    elif isinstance(value, unicode):
      entries.append(json_entry.format(unicode(key), unicode(value)))
    
    elif isinstance(value, bool):
      value = 'true' if value == True else 'false'
      entries.append(json_entry.format(key, value))

    elif isinstance(value, int):
      entries.append(json_entry.format(unicode(key), value))

    elif isinstance(value, dict):
      entries.append(json_entry.format(key, dict_to_json_str(value)))

    else:
      helper.fail('dict_to_json_str does not support this type: {0}'.format(type(value)))

  return u'{0} {1} {2}'.format(u'{', ','.join(entries), u'}')

# Map IBM SOAR severity values to ServiceNow severity values
sn_severity_map = {
  "High": 1,
  "Medium": 2,
  "Low": 3
}

#####################
### Define Inputs ###
#####################

# Get the id of this incident
inputs.incident_id = incident.id

# List all the fields you want to update in the ServiceNow Record here with the ServiceNow field_name being the key
# The default here is "severity", however if using the SIR Table we recommend switching to the business_criticality field
inputs.sn_update_fields = dict_to_json_str({
  "severity": sn_severity_map[incident.severity_code],
})
```

</details>

<details><summary>Post-Processing Script:</summary>

* This example **adds a Note to the Incident**
```python
# Add a Note to the Incident
note_text = u"The Severity of this Incident was updated to {0} in IBM SOAR".format(incident.severity_code)
incident.addNote(note_text)
```

</details>

### Sending SOAR artifacts to SNOW
You can utilize the SNOW: Update Record function to send artifact values to SNOW records. The previous example for update is set to synchronize the severity of a SOAR record to the desired field in SNOW on update. To synchronize on artifact values:

1. Using the resilient-sdk, `clone` the example workflow into a new workflow with `changetype` artifact.
    ```
    resilient-sdk clone --workflow example_snow_update_record_on_severity_change <new_workflow_name> --changetype artifact
    ```
    More information on the resilient-sdk and the `clone` command can be found [here](https://ibmresilient.github.io/resilient-python-api/pages/resilient-sdk/resilient-sdk.html#clone).
1. Modify the pre-processing script to map desired artifact values to SNOW record fields using the `sn_update_fields` parameter of the "SNOW: Update Record" function.
    ```python
    inputs.sn_update_fields = dict_to_json_str({
      "my_snow_column_name": artifact.value # When the artifact type is IP Address the value will be the IP
    })
    ```
1. Create a SOAR Rule to either manually or automatically trigger this new workflow.

---

## Function - SNOW: Close Record
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

<details><summary>Pre-Processing Script:</summary>

* This example **creates a Python Dictionary** to map the ServiceNow States to their corresponding numeric value.
> * *Note that for SIR tables, the record state options are new. If you intend to only use this with SIR or INC tables exclusively, you can remove the ones here that you don't need. These string values correspond to the Activity Field SN Record State which can be customized as well.*
```python
#######################################
### Define pre-processing functions ###
#######################################

# A Dictionary that maps Record States to their corresponding codes
# These codes are defined in ServiceNow and may be different for each ServiceNow configuration
# Codes prepended with [SIR] are specific to Security Incident Response incidents
map_sn_record_states = {
  "New": 1,
  "In Progress": 2,
  "On Hold": 3,
  "[INC] Resolved": 6,
  "[INC] Closed": 7,
  "[INC] Canceled": 8,
  "[SIR] Analysis": 16,
  "[SIR] Contain": 18,
  "[SIR] Eradicate": 19,
  "[SIR] Recover": 20,
  "[SIR] Review": 100,
  "[SIR] Closed": 3,
  "[SIR] Canceled": 7
}

#####################
### Define Inputs ###
#####################

# ID of this incident
inputs.incident_id = incident.id

# The state to change the record to
# inputs.sn_record_state = map_sn_record_states["Closed"]
inputs.sn_record_state = map_sn_record_states[rule.properties.sn_record_state]

# The resolution notes that are normally required when you close a ServiceNow record
# inputs.sn_close_notes = "This incident has been resolved in IBM SOAR. No further action required"
inputs.sn_close_notes = rule.properties.sn_close_notes

# The ServiceNow 'close_code' that you normally select when closing a ServiceNow record
# inputs.sn_close_code = "Solved (Permanently)"
inputs.sn_close_code = rule.properties.sn_close_code

# Add a Work Note to the Record in ServiceNow
inputs.sn_close_work_note = u"This record's state has been changed to {0} by IBM SOAR".format(unicode(rule.properties.sn_record_state))
```

</details>

<details><summary>Post-Processing Script:</summary>

* This example **adds a Note to the Incident** detailing why the Incident was closed or if the Workflow **fails** to close the ServiceNow Record
```python
note_text = None

if results.success:

  note_text = u"""<br>This Incident has been updated in <b>ServiceNow</b>
              <br><b>ServiceNow ID:</b> {0}
              <br><b>ServiceNow Record State:</b> {1}
              <br><b>ServiceNow Closing Notes:</b> {2}
              <br><b>ServiceNow Closing Code:</b> {3}""".format(
                                      unicode(results.sn_ref_id),
                                      unicode(results.sn_record_state),
                                      unicode(results.inputs.sn_close_notes),
                                      unicode(results.inputs.sn_close_code))

else:
  note_text = u"""<br>Failed to close this Incident in <b>ServiceNow</b>
              <br><b>Reason:</b> {0}""".format(unicode(results.reason))
  
incident.addNote(helper.createRichText(note_text))
```

</details>

---

## Function - SNOW: Add Note to Record
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

<details><summary>Pre-Processing Script:</summary>

```python
# The id of this incident
inputs.incident_id = incident.id

# If this is a task note, get the taskId
if note.type == 'task':
  # Set the task_id
  inputs.task_id = task.id

# Get the text of the note
inputs.sn_note_text = unicode(note.text.content)
```

</details>

<details><summary>Post-Processing Script:</summary>

This example prepends a timestamp to the SOAR Note to track when the Note was sent to ServiceNow.
```python
# Import Date
from java.util import Date

# Get the current time
dt_now = Date()

# Prepend message and time to the note
note.text = u"<b>Sent to ServiceNow at {0}</b><br>{1}".format(dt_now, unicode(note.text.content))
```

</details>

---

## Function - SNOW: Add Attachment to Record
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

<details><summary>Pre-Processing Script:</summary>

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
if results.success:

  noteText = u"""<br>{0} has added an attachment to <b>ServiceNow</b>
              <br><b>Attachment Name:</b>  {1}
              <br><b>ServiceNow ID:</b>  {2}""".format(unicode(principal.display_name), unicode(results.attachment_name), results.sn_ref_id)

  # If this is a task attachment, add a note to the Task
  if task:
    task.addNote(helper.createRichText(noteText))
  # Else add the note to the Incident
  else:
    incident.addNote(helper.createRichText(noteText))
```

</details>

---

## Function - SNOW: Lookup sys_id
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

<details><summary>Pre-Processing Script:</summary>

```python
# The table in ServiceNow to query
inputs.sn_table_name = "sys_user_group"

# The name of the field/table column to query
inputs.sn_query_field = "name"

# The value to equate the cell to
## Get the group name from the Rule Activity Field with:
inputs.sn_query_value = rule.properties.sn_assignment_group

## OR Set group name statically with:
# inputs.sn_query_value = "IT Securities"
```

</details>

<details><summary>Post-Processing Script:</summary>

*There is generally no Post-Process Script for this Function. Its output is normally used as an input to the **Create in ServiceNow** function.*

</details>

---

## Function - SNOW Helper: Update Data Table

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

<details><summary>Pre-Processing Script:</summary>

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

# Rules:
| Rule Name | Object Type | Activity Fields | Workflow Triggered | Conditions |
| --------- | :---------: | --------------- | ------------------ | ---------- |
| SNOW: Create Record [Incident] | `Incident` | `SN Assignment Group`, `SN Initial Note` | `Example: SNOW: Create Record [Incident]` | `SNOW Record ID` does not have a value |
| SNOW: Create Record [Task] | `Task` | `SN Assignment Group`, `SN Initial Note` | `Example: SNOW: Create Record [Task]` | None |
| SNOW: Update/Close Record [Incident] | `Incident` | `SN Record State`, `SN Close Code`, `SN Close Notes` | `Example: SNOW: Close Record [Incident]` | `SNOW Record ID` has a value |
| SNOW: Update/Close Record [Task] | `Task` | `SN Record State`, `SN Close Code`, `SN Close Notes` | `Example: SNOW: Close Record [Task]` | None |
| SNOW: Update/Close Record | `Data Table` | `SN Record State`, `SN Close Code`, `SN Close Notes` | `Example: SNOW: Close Record [Task]` | None |
| SNOW: Send as Additional Comment | `Note` | None | `Example: SNOW: Add Comment to Record` | `Note Text` does not contain "Sent to ServiceNow at" |
| SNOW: Send as Work Note | `Note` | None | `Example: SNOW: Add Work Note to Record` | `Note Text` does not contain "Sent to ServiceNow at" |
| SNOW: Add Attachment to Record | `Attachment` | None | `Example: SNOW: Add Attachment to Record` | None |
| SNOW: [INC] Update Record on Severity Change  | `Incident` | None | `Example: SNOW: Update Record on Severity Change` | `Severity` is changed AND `SNOW Record ID` has a value AND is a INC incident in SNOW |
| SNOW: [SIR] Update Record on Severity Change  | `Incident` | None | `Example: SNOW: Update Record on Severity Change` | `Severity` is changed AND `SNOW Record ID` has a value AND is a SIR Incident in SNOW |
| SNOW: Update Data Table on Status Change [Incident] | `Incident` | None | `Example: SNOW: Update Data Table on Status Change [Incident]` | `Status` is changed |
| SNOW: Update Data Table on Status Change [Task] | `Task` | None | `Example: SNOW: Update Data Table on Status Change [Task]` | `Status` is changed |

---

# Data Table:

## ServiceNow Records
 ![screenshot](./screenshots/9.png)

### API Name:
`sn_records_dt`

### Columns:
| Column Name | API Access Name | Type |
| ----------- | --------------- | -----|
| Last Updated | `sn_records_dt_time` | `DateTimePicker` |
| Name | `sn_records_dt_name` | `Text` |
| Type | `sn_records_dt_type` | `Text` |
| SOAR ID | `sn_records_dt_res_id` | `Text` |
| SNOW ID | `sn_records_dt_sn_ref_id` | `Text` |
| SOAR Status | `sn_records_dt_res_status` | `Rich Text` |
| SNOW Status | `sn_records_dt_snow_status` | `Rich Text` |
| Links | `sn_records_dt_links` | `Rich Text` |

# Security Incident Response Specific Customizations
By default the severity of a SOAR incident/case is mapped to the `severity` field in ServiceNow. 
This field is available in both the `incident` and `sn_si_incident` tables, however, Security Incident (SIR) tables have another field labeled `business_criticality`. 
It is recommend after the install to customize your workflows in SOAR and SNOW to handle `business_criticality` rather than `severity` in SNOW. 
Customize the "\[SIR\] SNOW Update Record on Severity Change" workflow and "SNOW: Create Record \[Incident\]". The "RES_WF_CreateIncident" workflow on SNOW should be customized as well. 
See the [Customize ServiceNow App Guide](../customize_snow_guide) for more details.
