<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# McAfee ePO Add Permission Sets to user

## Function - McAfee ePO Add Permission sets to user

### API Name
`mcafee_epo_add_permission_sets_to_user`

### Output Name
``

### Message Destination
`mcafee_epo_message_destination`

### Pre-Processing Script
```python
inputs.mcafee_epo_username = rule.properties.epo_username
inputs.mcafee_epo_permsetname = row.permission_set_name
```

### Post-Processing Script
```python
if results['success']:
  if rule.properties.epo_username not in row.users:
    if row.users:
      row.users = "{}, {}".format(row.users, rule.properties.epo_username)
    else:
      row.users = rule.properties.epo_username
    incident.addNote("Permissions set: {} was added to user: {}".format(row.permission_set_name, rule.properties.epo_username))
  else:
    incident.addNote("User: {} already has permission set: {}".format(rule.properties.epo_username, row.permission_set_name))
```

---

