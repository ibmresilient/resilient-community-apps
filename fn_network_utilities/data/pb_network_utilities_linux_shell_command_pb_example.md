<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Playbook - Network Utilities Linux Shell Command (PB) Example

### API Name
`network_utilities_linux_shell_command_pb_example`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`artifact.type in ['IP Address', 'DNS Name', 'URL']`

### Object Type
`artifact`

### Description
An example running shell commands on a Linux machine


---
## Function - Network Utilities: Linux Shell Command

### API Name
`network_utilities_linux_shell_command`

### Output Name
`network_utilities_shell_result`

### Message Destination
`fn_network_utilities`

### Function-Input Script
```python
# You can set the command on the "Input" panel or dynamically
# NOTE: The administrator must configure each command before you can run it!

inputs.network_utilities_shell_params = artifact.value
inputs.network_utilities_shell_command = "remote_command_linux:remote_computer"
# inputs.network_utilities_ssh_key_auth = "ssh_key_auth"
```

---

## Global script - network_utilities_shell_results

### Description
parse and display the results from fn_network_utilities: local_shell, linux_shell and remote powershell functions

### Script Type
`Global script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.network_utilities_shell_result

# Outputs are:
#  - "commandline": the command that ran
#  - "start": timestamp, epoch milliseconds
#  - "end": timestamp, epoch milliseconds
#  - "elapsed": milliseconds
#  - "exitcode": nonzero indicates that the command failed
#  - "stdout": text output from the command
#  - "stderr": error text output from the command
#  - "stdout_json": object parsed from JSON output from the command
#  - "stderr_json": object parsed from JSON error output from the command
content = results.content
if content.get("exitcode") == 0:
  note_text = u"Command succeeded: {}\nStandard Out: {}\nStandard Error: {}".format(content.get("commandline"), content.get("stdout"), content.get("stderr"))
else:
  note_text = u"Command failed: {}\nStandard Out: {}\nStandard Error: {}".format(content.get("commandline"), content.get("stdout"), content.get("stderr"))

incident.addNote(helper.createPlainText(note_text))

```

---

