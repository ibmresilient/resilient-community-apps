<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - SEP: Get Upload status - Example (PB)

### API Name
`sep_get_upload_status`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`sep_eoc_scan_results.file_upload_status contains In progress AND sep_eoc_scan_results.upload_commandid has_a_value`

### Object Type
`sep_eoc_scan_results`

### Description
Get the status of an Upload command.


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
inputs.sep_commandid = row.upload_commandid
inputs.sep_status_type = "upload"
```

---

## Local script - get command status output

### Description


### Script Type
`Local script`

### Object Type
`sep_eoc_scan_results`

### Script Content
```python
## Symantec Endpoint Protection - fn_sep_get_command_status script ##
# Globals
# List of fields in datatable fn_sep_get_command_status script
DATA_TBL_FIELDS = ["query_execution_date", "file_upload_status"]
FN_NAME = "fn_sep_get_command_status"
WF_NAME = "Get Upload status"
STATUS_TYPE = "upload"
FINAL_STATUSES = {
  0: "Initial / Not received",
  1: "Received",
  2: "In progress",
  3: "Completed".format(STATUS_TYPE.capitalize()),
  4: "Rejected".format(STATUS_TYPE.capitalize()),
  5: "Canceled".format(STATUS_TYPE.capitalize()),
  6: "Failed".format(STATUS_TYPE.capitalize())
}

# Processing
results = playbook.functions.results.get_command_status_results
C_OUTER = results.get("content", {})
INPUTS = results.get("inputs", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

upload_command_state = C_OUTER.get("overall_command_state")
note_text = ''
if C_OUTER and len(C_OUTER.get("content")) > 0:
  row.query_execution_date = QUERY_EXECUTION_DATE
  computer = C_OUTER.get("content", [])[0]
  if upload_command_state == "Completed":
    row.file_upload_status = FINAL_STATUSES.get(computer.get("stateId"))
    if computer.get("stateId") == 3:
      row.file_id = computer.get("binaryFileId")
    if FINAL_STATUSES.get(computer.get("stateId")) == "Completed":
      note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nUpload command completed with status <b>{1}</b> " \
                  "for command id <b>{2}</b> for artifact with type <b>{3}</b> and value <b>{4}</b> for SOAR function <b>{5}</b>"\
          .format(WF_NAME, FINAL_STATUSES.get(computer.get("stateId")), INPUTS.get("sep_commandid"), row.artifact_type,
          row.artifact_value, FN_NAME)
    else:
      note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nUpload command in <b>{1}</b> state for command " \
                  "id <b>{2}</b> for artifact with type <b>{3}</b> and value <b>{4}</b> for SOAR function " \
                  "<b>{5}</b>.<br>Note: Upload only supports executable file types." \
                  "<br>Please review console/logs on the Symantec SEPM server for further details if required." \
          .format(WF_NAME, FINAL_STATUSES.get(computer.get("stateId")), INPUTS.get("sep_commandid"), row.artifact_type, 
              row.artifact_value, FN_NAME)
  else:
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nUpload command in <b>{1}</b> state for command id " \
                "<b>{2}</b> for artifact with type <b>{3}</b> and value <b>{4}</b> for SOAR function <b>{5}</b>"\
        .format(WF_NAME, FINAL_STATUSES.get(computer.get("stateId")), INPUTS.get("sep_commandid"), row.artifact_type,
                row.artifact_value, FN_NAME)
    row.file_upload_status = upload_command_state
else:
  note_text += "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> results returned for SOAR function <b>{1}</b>"\
      .format(WF_NAME, FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

---

