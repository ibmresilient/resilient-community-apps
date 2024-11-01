<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.0.1.486
-->

# Playbook - Salesforce: Write Account Details to Note

### API Name
`salesforce_get_account`

### Status
`disabled`

### Activation Type
`Manual`

### Activation Conditions
`incident.properties.salesforce_case_id has_a_value`

### Object Type
`incident`

### Description
Get information on the Salesforce account associated with a case and write to a SOAR note.


---
## Function - Salesforce: Get Account

### API Name
`salesforce_get_account`

### Output Name
`account_details`

### Message Destination
`fn_salesforce`

### Function-Input Script
```python
inputs.salesforce_account_id = incident.properties.salesforce_account_id if incident.properties.salesforce_account_id else helper.fail("Error: AccountId is None")
```

---

## Local script - Salesforce: Write Account information

### Description
Write account information to a note.

### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
import json

results = playbook.functions.results.account_details

if results.success:
  content = results.get("content", {})
  account = content.get("salesforce_account", {})
  note_text = "Account Details: <br>{0}".format(json.dumps(account, indent=4))
  incident.addNote(helper.createRichText(note_text))
else:
  incident.addNote("Unable to get Account details from Salesforce.")
```

---

