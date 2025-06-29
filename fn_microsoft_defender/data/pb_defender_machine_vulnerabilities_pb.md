<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.6.0.1543
-->

# Playbook - Microsoft Defender: Machine Vulnerabilities - Example (PB)

### API Name
`defender_machine_vulnerabilities_pb`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Object Type
`defender_machines`

### Description
Get Defender machine vulnerabilities


---
## Function - Defender Machine Vulnerabilities

### API Name
`defender_machine_vulnerabilities`

### Output Name
`machine_vulnerabilities`

### Message Destination
`fn_microsoft_defender`

### Function-Input Script
```python
inputs.defender_machine_id = row['machine_id']
```

---

## Local script - defender post process

### Description


### Script Type
`Local script`

### Object Type
`defender_machines`

### Script Content
```python
"""
 [
        {
            "id": "CVE-2019-1348",
            "name": "CVE-2019-1348",
            "description": "Git could allow a remote attacker to bypass security restrictions, caused by a flaw in the --export-marks option of git fast-import. By persuading a victim to import specially-crafted content, an attacker could exploit this vulnerability to overwrite arbitrary paths.",
            "severity": "Medium",
            "cvssV3": 4.3,
            "exposedMachines": 1,
            "publishedOn": "2019-12-13T00:00:00Z",
            "updatedOn": "2019-12-13T00:00:00Z",
            "publicExploit": False,
            "exploitVerified": False,
            "exploitInKit": False,
            "exploitTypes": [],
            "exploitUris": []
        },
        {
            "id": "CVE-2019-1348",
            "name": "CVE-2019-1348-2",
            "description": "Git could allow a remote attacker to bypass security restrictions, caused by a flaw in the --export-marks option of git fast-import. By persuading a victim to import specially-crafted content, an attacker could exploit this vulnerability to overwrite arbitrary paths.",
            "severity": "Medium",
            "cvssV3": 4.3,
            "exposedMachines": 1,
            "publishedOn": "2019-12-13T00:00:00Z",
            "updatedOn": "2019-12-13T00:00:00Z",
            "publicExploit": False,
            "exploitVerified": False,
            "exploitInKit": False,
            "exploitTypes": [],
            "exploitUris": []
        }
    ]
"""
results = playbook.functions.results.machine_vulnerabilities
def mk_note(list_of_notes):
    return "<br>---<br><br>".join(["<br>".join(note) for note in list_of_notes])

def format_line(k, v):
    return "<b>{}</b>: {}".format(k, v)

vulnerabilities = results.get("content", {}).get('value', [])
if results.get('success'):
  if not vulnerabilities:
    incident.addNote("Defender No machine vulnerabilities for: {}".format(row['machine_name']))
  else:
    note = []
    for risk in vulnerabilities:
      note_info = ["Defender Machine Vulnerabilities:"]
      note_info.append(format_line("Machine", row['machine_name']))
      note_info.append(format_line("Machine Id", row['machine_id']))
      note_info.append(format_line("Vulnerability", risk.get('name')))
      note_info.append(format_line("Description", risk.get('description')))
      note_info.append(format_line("Severity", risk.get('severity')))
      note_info.append(format_line("Published", risk.get('publishedOn')))
      note_info.append(format_line("Updated", risk.get('updatedOn')))

      note.append(note_info)
    incident.addNote(helper.createRichText(mk_note(note)))
else:
    incident.addNote("Defender Machine Vulnerabilities failed: {}".format(results.get("reason")))
```

---

