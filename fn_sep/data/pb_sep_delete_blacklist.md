<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - SEP: Delete Blacklist - Example (PB)

### API Name
`sep_delete_blacklist`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`sep_fingerprint_lists.list_id has_a_value`

### Object Type
`sep_fingerprint_lists`

### Description
Delete an existing blacklist fingerprint list.
Note: Also removes it from any group to which it has been assigned.


---
## Function - SEP - Delete Fingerprint List

### API Name
`fn_sep_delete_fingerprint_list`

### Output Name
`delete_fingerprintlist_results`

### Message Destination
`fn_sep`

### Function-Input Script
```python
inputs.sep_fingerprintlist_id = row.list_id
```

---

## Local script - delete fingerprintlist output

### Description


### Script Type
`Local script`

### Object Type
`sep_fingerprint_lists`

### Script Content
```python
## Symantec Endpoint Protection - fn_sep_delete_fingerprint_list ##
# Globals
FN_NAME = "fn_sep_delete_fingerprint_list"
WF_NAME = "Delete Fingerprint List"
results = playbook.functions.results.delete_fingerprintlist_results
content = results.get("content", {})
INPUTS = results.get("inputs", {})
QUERY_EXECUTION_DATE = results.get("metrics", {}).get("timestamp")

# Processing
note_text = ''
if content:
  if "errorCode" in content and int(content.get("errorCode")) == 410:
    # The finger print list doesn't exist.
    note_text = "Symantec SEP Integration:\nPlaybooks <b>{0}</b>:\nThe fingerprint list <b>{1}</b> does not exist or is invalid " \
                "for SOAR function <b>{2}</b>"\
        .format( WF_NAME, INPUTS.get("sep_fingerprintlist_name"), FN_NAME)
  else:
    note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nSuccessfully deleted fingerprint list with id " \
                "<b>{1}</b> for SOAR function <b>{2}</b>"\
        .format(WF_NAME, INPUTS.get("sep_fingerprintlist_id"), FN_NAME)
    row.list_description = "Fingerprint list deleted"
    row.hash_values = "Fingerprint list deleted"
    row.list_id = "Fingerprint list deleted"

else:
  note_text = "Symantec SEP Integration:\nPlaybook <b>{0}</b>:\nThere were <b>no</b> results returned " \
               "with fingerprint id <b>{1}</b> for SOAR function <b>{2}</b>"\
      .format(WF_NAME, INPUTS.get("sep_fingerprintlist_id"),  FN_NAME)

incident.addNote(helper.createRichText(note_text))
```

---

