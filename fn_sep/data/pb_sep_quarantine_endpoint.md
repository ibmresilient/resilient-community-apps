<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - SEP: Quarantine Endpoint - Example (PB)

### API Name
`sep_quarantine_endpoint`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`sep_endpoint_details.computerName has_a_value AND sep_endpoint_details.endpoint_quarantine_status not_equals Quarantined AND sep_endpoint_details.group_id has_a_value AND sep_endpoint_details.hardwareKey has_a_value AND sep_endpoint_details.quarantine_command_state not_contains In progress AND sep_endpoint_details.uniqueId has_a_value`

### Object Type
`sep_endpoint_details`

### Description
Quarantine or un-quarantine an endpoint. Add or remove endpoints to or from network quarantine.


---
## Function - SEP - Quarantine Endpoints

### API Name
`fn_sep_quarantine_endpoints`

### Output Name
`quarantine_ep_results`

### Message Destination
`fn_sep`

### Function-Input Script
```python
inputs.sep_computer_ids = row.uniqueId
inputs.sep_group_ids = row.group_id
inputs.sep_hardwarekey = row.hardwareKey
# Quarantine endpoint
inputs.sep_undo = False
```

---
## Function - SEP - Get Command Status

### API Name
`fn_sep_get_command_status`

### Output Name
`get_command_status_results`

### Message Destination
`fn_sep`

### Function-Input Script
```python
quarantine_ep_content = playbook.functions.results.quarantine_ep_results.get("content", {})
inputs.sep_incident_id = incident.id
inputs.sep_commandid = quarantine_ep_content.get("commandID_computer")
inputs.sep_status_type = "quarantine"
```

---
## Function - SEP - Get Computers

### API Name
`fn_sep_get_computers`

### Output Name
`get_computers_results`

### Message Destination
`fn_sep`

### Function-Input Script
```python
inputs.sep_computername = row.computerName
```

---

## Local script - quarantine endpoints output

### Description


### Script Type
`Local script`

### Object Type
`sep_endpoint_details`

### Script Content
```python
## Symantec Endpoint Protection - fn_sep_quarantine_endpoints script ##
fn_name = "fn_sep_quarantine_endpoints"
wf_name = "Quarantine Endpoint"

results = playbook.functions.results.quarantine_ep_results
content = results.get("content", {})
inputs = results.get("inputs", {})
query_execution_date = results.get("metrics", {}).get("timestamp")

if results.get("success"):
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nExecuted with command id <b>{1}</b> for endpoint " \
              "<b>{2}</b> for SOAR function <b>{3}</b>"\
      .format(wf_name, content.get("commandID_computer", ''), row.computerName, fn_name)
  row.query_execution_date = query_execution_date
  row.quarantine_commandid = content.get("commandID_computer", '')
else:
  note_text = f"Symantec SEP Integration:\nPlaybook <b>{wf_name}</b>:\n Failed with reason: {results.get('reason', '')}"

incident.addNote(helper.createRichText(note_text))
```

---
## Local script - get command status output

### Description


### Script Type
`Local script`

### Object Type
`sep_endpoint_details`

### Script Content
```python
## Symantec Endpoint Protection - fn_sep_get_command_status script ##
FN_NAME = "fn_sep_get_command_status"
WF_NAME = "Quarantine Endpoint"
STATUS_TYPE = "quarantine"
FINAL_STATUSES = {
  0: "Not received",
  1: "Received",
  2: "In progress",
  3: "Completed",
  4: "Rejected",
  5: "Canceled",
  6: "Failed"
}

results = playbook.functions.results.get_command_status_results
C_OUTER = results.get("content", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

endpoint_quarantine_status = row.endpoint_quarantine_status
status_msg = "Un-quarantine" if endpoint_quarantine_status == "Quarantined" else "Quarantine"
note_text = ''
quarantine_command_state = C_OUTER.get("overall_command_state")

if C_OUTER and len(C_OUTER.get("content")) > 0:
  row.quarantine_command_state = quarantine_command_state
  row.query_execution_date = QUERY_EXECUTION_DATE
  computer = C_OUTER.get("content", [])[0]
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\n<b>{1}</b> command status for command id <b>{2}</b> " \
              "for computer <b>{3}</b> was <b>{4}</b> for SOAR function <b>{5}</b>"\
      .format(WF_NAME, status_msg, row.quarantine_commandid, row.computerName, FINAL_STATUSES.get(computer.get("stateId")), FN_NAME)
  if quarantine_command_state == "Completed":
    row.quarantine_command_state = FINAL_STATUSES.get(computer.get("stateId"))
  else:
    row.quarantine_command_state = quarantine_command_state

else:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> results returned for SOAR function <b>{1}</b>" \
      .format(WF_NAME, FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

---
## Local script - get computers output

### Description


### Script Type
`Local script`

### Object Type
`sep_endpoint_details`

### Script Content
```python
## Symantec Endpoint Protection - fn_sep_get_computers script ##
FN_NAME = "fn_sep_get_computers"
WF_NAME = "Quarantine Endpoint"
results = playbook.functions.results.get_computers_results
C_OUTER = results.get("content", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

note_text = ''
if C_OUTER and len(C_OUTER.get("content")) > 0:
  row.query_execution_date = QUERY_EXECUTION_DATE
  computer = C_OUTER.get("content", [])[0]
  ep_name = computer.get("computerName")
  ep_osname = computer.get("osName", "")
  if "windows" in ep_osname.lower():
    if "host integrity check passed" in computer.get("quarantineDesc").lower():
      row.endpoint_quarantine_status = "Un-Quarantined"
    elif "quarantined" in computer.get("quarantineDesc").lower():
      row.endpoint_quarantine_status = "Quarantined"
    else:
      row.endpoint_quarantine_status = None
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nQuarantine status of endpoint <b>{1}</b> is <b>{2}</b> for SOAR function <b>{3}</b>"\
    .format(WF_NAME, ep_name, row.endpoint_quarantine_status, FN_NAME)
  else:
    row.endpoint_quarantine_status = None

else:
  note_text += "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> results returned for SOAR function <b>{1}</b>"\
      .format(WF_NAME, FN_NAME)
if len(note_text) > 0:
  incident.addNote(helper.createRichText(note_text))
```

---

