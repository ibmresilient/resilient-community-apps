<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.0.2.575
-->

# Playbook - McAfee ePO Find All Groups (PB)

### API Name
`mcafee_epo_find_all_groups`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Object Type
`incident`

### Description
None


---
## Function - McAfee ePO Find Groups

### API Name
`mcafee_epo_find_groups`

### Output Name
`groups`

### Message Destination
`mcafee_epo_message_destination`

### Function-Input Script
```python
None
```

---
## Function - McAfee ePO Execute Query

### API Name
`mcafee_epo_execute_query`

### Output Name
`query`

### Message Destination
`mcafee_epo_message_destination`

### Function-Input Script
```python
inputs.datatable_name = "mcafee_epo_groups"
inputs.incident_id = incident.id
inputs.mcafee_epo_target = "EPOLeafNode"
inputs.mcafee_epo_query_select = "EPOLeafNode.NodeName EPOBranchNode.NodeName EPOBranchNode.NodeTextPath2"
```

---

## Local script - mcafee epo post process

### Description


### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.query
groupsResults = playbook.functions.results.groups
if results.get("success"):
  for groupInfo in groupsResults.get("content", {}):
    groupPath = groupInfo.get("groupPath")
    table = incident.addRow("mcafee_epo_groups")
    table["group_id"] = int(groupInfo.get("groupId"))
    table["group_path"] = groupPath
    systems = ""
    for group in results.get("content", {}):
      # EPOBranchNode.NodeTextPath2 only returns path after My Organization
      path2 = group.get("EPOBranchNode.NodeTextPath2")
      # EPOBranchNode.NodeTextPath2 returns the path, Lost and Found, as, Lost&Found,
      # so it needs to be converted in order to compare paths.
      path2 = path2.replace("Lost&Found", "Lost and Found")
      # Add, My Organization, to the beginning of the path
      path2 = "My Organization{}".format(path2[:len(path2)-1])

      if groupPath == path2:
        systems = "{}, {}".format(systems, group.get("EPOLeafNode.NodeName"))
    table["systems"] = systems[2:]
```

---

