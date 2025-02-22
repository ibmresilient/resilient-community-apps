<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - SEP: Get Non-Compliant Endpoints status details - Example (PB)

### API Name
`sep_get_noncompliant_endpoints_status_details`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`sep_endpoint_status_summary.non_compliant gt`

### Object Type
`sep_endpoint_status_summary`

### Description
Get further details for Endpoints with non-compliant status.


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
inputs.sep_status_details = True
```

---

## Local script - get computers output

### Description


### Script Type
`Local script`

### Object Type
`sep_endpoint_status_summary`

### Script Content
```python
## Symantec Endpoint Protection - fn_sep_get_computers script ##
# Globals
# List of fields in datatable for "Get Endpoints status" playbook.
DATA_TBL_FIELDS = ["query_execution_date", "computer_name","host_integrity_check", "onlineStatus", "readableLastScanTime",
                   "readableLastUpdateTime", "apOnOff", "avEngineOnOff", "cidsBrowserFfOnOff", "cidsBrowserIeOnOff", 
                   "cidsDrvOnOff", "daOnOff", "elamOnOff", "firewallOnOff", "pepOnOff", "ptpOnOff", "tamperOnOff"]
FN_NAME = "fn_sep_get_computers"
WF_NAME = "Get Non-Compliant Endpoints status details"
results = playbook.functions.results.get_computers_results
CONTENT = results.get("content", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

# Processing
def add_rows_non_compliant_computers(eps):
  for i in range(len(eps)):
    newrow = incident.addRow("sep_endpoints_non_compliant_details")
    newrow.query_execution_date = QUERY_EXECUTION_DATE
    for f in DATA_TBL_FIELDS:
      if f == "query_execution_date":
        continue
      newrow[f] = eps[i].get(f)

note_text = ''

if CONTENT and CONTENT.get("total", 0) > 0:
  if CONTENT.get("non_compliant", 0) > 0:
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>{1}</b> non-compliant endpoints " \
                "detected out of a total of <b>{2}</b> for SOAR function <b>{3}</b>"\
        .format(WF_NAME, CONTENT.get("non_compliant"), CONTENT.get("total"), FN_NAME)
    add_rows_non_compliant_computers(CONTENT.get("eps"))
  else:
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> non-compliant endpoints " \
                 "detected out of a total of <b>{1}</b> for SOAR function <b>{2}</b>" \
        .format(WF_NAME, CONTENT.get("total"), FN_NAME)
else:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> results returned for SOAR " \
              "function <b>{1}</b>".format(WF_NAME, FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

---

