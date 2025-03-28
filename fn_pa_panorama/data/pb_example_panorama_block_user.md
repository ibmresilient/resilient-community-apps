<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.4.0.1351
-->

# Playbook - Panorama: Block User - Example (PB)

### API Name
`example_panorama_block_user`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`artifact.type equals User Account`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| Panorama Template | `panorama_template` | text | Name of the Panorama template to use | Always |
| panorama_label | `panorama_label` | text | Label given to the server to use. Only needed if configured in app.config. | Optional |

### Object Type
`artifact`

### Description
Given a User Account artifact, adds the user to the "Blocked_Users" group in Panorama. This only works with Panorama and does not work with PanOS.


---
## Function - Panorama Get Users in a Group

### API Name
`panorama_get_users_in_a_group`

### Output Name
`get_users_results`

### Message Destination
`palo_alto_panorama`

### Function-Input Script
```python
# Set this to the xpath of the group you are interested in
if getattr(playbook.inputs, "panorama_template", None):
  inputs.panorama_user_group_xpath = f"/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='{playbook.inputs.panorama_template}']/config/shared/local-user-database/user-group/entry[@name='Blocked_Users']"

if getattr(playbook.inputs, "panorama_label", None):
  inputs.panorama_label = getattr(playbook.inputs, "panorama_label", None)
inputs.panorama_location = "shared"
```

---
## Function - Panorama Edit Users in a Group

### API Name
`panorama_edit_users_in_a_group`

### Output Name
`edit_users_results`

### Message Destination
`palo_alto_panorama`

### Function-Input Script
```python
inputs.panorama_location = "shared"
# Set this to the name of the user group you wish to add a user to
group_name = "Blocked_Users"

# Set this to the xpath of the group you are interested in
if getattr(playbook.inputs, "panorama_template", None):
  inputs.panorama_user_group_xpath = f"/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='{playbook.inputs.panorama_template}']/config/shared/local-user-database/user-group/entry[@name='{group_name}']"

users_list = playbook.functions.results.get_users_results.get("content", {}).get("user_list", [])

blocked_users = []

if len(users_list) == 1:
  # only one user was returned
  blocked_users.append(users_list[0])
elif len(users_list) > 1:
  # multiple users returned
  for user in users_list:
    blocked_users.append(user.get("#text"))

# Add the user to the blocked list if they are not already there
if artifact.value not in blocked_users:
  blocked_users.append(artifact.value)

# Updated function creates the xml request body for you
inputs.panorama_users_list = str(blocked_users)
inputs.panorama_user_group_name = group_name
if getattr(playbook.inputs, "panorama_label", None):
  inputs.panorama_label = getattr(playbook.inputs, "panorama_label", None)

# Giving the xml request body as an input still works
# # Build xml which the function will send to Panorama
# panorama_xml = f'''
# <entry name="{str(group_name)}">
#     <user>'''

# # Add member nodes with the username to the xml string
# for user in blocked_users:
#   panorama_xml += f"\n      <member>{user}</member>"

# # Add the ending of the xml to the string
# panorama_xml += """
#     </user>
# </entry>
# """
# inputs.panorama_user_group_xml = panorama_xml
```

---
## Function - Panorama Commit

### API Name
`panorama_commit`

### Output Name
`commit_output`

### Message Destination
`palo_alto_panorama`

### Function-Input Script
```python
if getattr(playbook.inputs, "panorama_label", None):
  inputs.panorama_label = getattr(playbook.inputs, "panorama_label", None)
inputs.panorama_location = "shared"
```

---

## Local script - Panorama block user post-process

### Description


### Script Type
`Local script`

### Object Type
`artifact`

### Script Content
```python
results = playbook.functions.results.edit_users_results
if results.get("success"):
  incident.addNote(f"Panorama User account: {artifact.value} was blocked.")
else:
  if "code 12" in results.get("reason"):
    incident.addNote("Panorama Block User failed because the User you are trying to block does not exist.")
  else:
    incident.addNote(f"Panorama Block User failed with reason: {results.get('reason')}")
```

---
## Local script - commit output

### Description


### Script Type
`Local script`

### Object Type
`artifact`

### Script Content
```python
note = ""
results = playbook.functions.results.commit_output
edit_user = playbook.functions.results.edit_users_results
if edit_user.get("success"):
  note += f"Panorama User account: {artifact.value} was blocked.\n"
else:
  if "code 12" in edit_user.get("reason"):
    note += "Panorama Block User failed because the User you are trying to block does not exist.\n"
  else:
    note += f"Panorama Block User failed with reason: {edit_user.get('reason')}\n"

if results.get("success"):
  note += str(results.get("content", {}).get("result", {}).get("msg", {}).get("line"))

incident.addNote(note)
```

---

