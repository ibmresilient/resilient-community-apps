<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.2.2.1096
-->

# Playbook - MS Teams: Delete Channel (PB)

### API Name
`ms_teams_delete_channel_pb`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| Channel Name | `ms_channel_name` | text | Name of the Microsoft Teams Channel | Always |
| Group/Team ID | `ms_groupteam_id` | text | Unique ID assigned to the Group or Team object while being created | Optional |
| Group/Team Name | `ms_groupteam_name` | text | Name of the Microsoft Group or Team | Optional |
| Mail nickname | `ms_group_mail_nickname` | text | This value must be a unique value as no two MS Objects can have the same email ID. The mail address need not include the domain suffix (i.e. @example.com) | Optional |

### Object Type
`incident`

### Description
None


---
## Function - MS Teams: Delete Channel

### API Name
`ms_teams_delete_channel`

### Output Name
`delete_channel`

### Message Destination
`fn_teams`

### Function-Input Script
```python
inputs.ms_channel_name = playbook.inputs.ms_channel_name

if hasattr(playbook.inputs, "ms_groupteam_id") and playbook.inputs.ms_groupteam_id:
  inputs.ms_groupteam_id = playbook.inputs.ms_groupteam_id
if hasattr(playbook.inputs, "ms_group_mail_nickname") and playbook.inputs.ms_group_mail_nickname:
  inputs.ms_group_mail_nickname = playbook.inputs.ms_group_mail_nickname
if hasattr(playbook.inputs, "ms_groupteam_name") and playbook.inputs.ms_groupteam_name:
  inputs.ms_groupteam_name = playbook.inputs.ms_groupteam_name

```

---

## Local script - post process delete channel

### Description


### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.delete_channel
content = results.get("content", {})
channel_name = playbook.inputs.ms_channel_name

if not results.get("success"):
  text = f"Unable to delete Microsoft Channel: {channel_name}"
  fail_reason = results.get("reason")
  if fail_reason:
    text = f"{text}:\n\tFailure reason: {fail_reason}"
    text += f"\n\tInputs: {results.get('inputs')}"

else:
  text  = f"""<b>Delete Microsoft Channel: {channel_name} result</b><br />
  <br />{content.get('message')}"""

incident.addNote(helper.createRichText(text))
```

---

