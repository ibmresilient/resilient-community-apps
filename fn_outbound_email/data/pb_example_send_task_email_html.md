<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Playbook - Send Task Email HTML (PB) Example

### API Name
`example_send_task_email_html`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| CC | `mail_cc` | text | comma separated list of recipients | Optional |
| From | `mail_from` | text | default is app.config from_email_address | Optional |
| Task Attachments | `mail_attachments` | text | comma separated list of task attachment names, or '*' for all | Optional |
| To | `mail_to` | text | - | Always |

### Object Type
`task`

### Description
Send email based on a task with optional attachments



---
## Function - Outbound Email: Send Email

### API Name
`send_email`

### Output Name
`outbound_email_results`

### Message Destination
`email_outbound`

### Function-Input Script
```python
import datetime
inputs.mail_to = playbook.inputs.mail_to
inputs.mail_cc = playbook.inputs.mail_cc
inputs.mail_attachments = playbook.inputs.mail_attachments
inputs.mail_incident_id = incident.id
inputs.mail_from = playbook.inputs.mail_from
inputs.mail_subject = "[{0}] {1} Task:{2}".format(incident.id, incident.name, task.name)

creation_date = datetime.datetime.fromtimestamp(incident.create_date/1000).strftime('%Y-%m-%d %H:%M:%S')
type_ids = ", ".join(incident.incident_type_ids)
sev_code = "{}".format(incident.severity_code)
current_plan = "{}".format(incident.plan_status)

inputs.mail_body_html = """
<h2>Incident Summary</h2>
    Severity Code: {0}
<br>
    Plan Status: {1}
<br>
    Created: {2}
<br>
    Incident Type: {3}
<br>
    Incident Link: <a target='_blank' href='{{{{ template_helper.generate_incident_url({6}) }}}}'>{6}</a>
<br>
    Task: <a target='_blank' href='{{{{ template_helper.generate_task_url({6},{7}) }}}}'>{4}</a>
<br>
    Instructions: 
<br>
{5}
""".format(sev_code, current_plan, creation_date, type_ids, task.name, task.instructions.get("content") if task.instructions else '-', incident.id, task.id)

```

---

## Global script - Save Outbound Email Results

### Description
Save outbound email results in the Email Conversations datatable

### Script Type
`Global script`

### Object Type
`incident`

### Script Content
```python
import time

try:
  e_results = workflow.properties.outbound_email_results
except:
  try:
    e_results = playbook.functions.results.outbound_email_results
  except:
    helper.fail("unable to read outbound_email_results property")

if e_results:
  row = incident.addRow('email_conversations')
  row['status'] = "success" if e_results.get('success') else "failure: {}".format(e_results.get('reason'))
  
  row['date_sent'] = int(time.time()*1000)
  row['source'] = "outbound"
  row['recipients'] = helper.createRichText("To: {}<br>Cc: {}<br>Bcc: {}".format(e_results.get('inputs', {}).get('mail_to'), e_results.get('inputs', {}).get('mail_cc', ''), e_results.get('inputs', {}).get('mail_bcc', '')))
  row['from'] = e_results.get('content', {}).get('mail_from') if e_results.get('content', {}).get('mail_from') else e_results.get('inputs', {}).get('mail_from')
  row['subject'] = e_results.get('inputs', {}).get('mail_subject')
  row['body'] = e_results.get('content', {}).get('mail_body')
  row['attachments'] = e_results.get('inputs', {}).get('mail_attachments')
  row['importance'] = e_results.get('inputs', {}).get('mail_importance')
  row['in_reply_to'] = e_results.get('inputs', {}).get('mail_in_reply_to')
  row['message_id'] = e_results.get('inputs', {}).get('mail_message_id')
else:
  incident.addNote("workflow/playbook properties 'outbound_email_results' not found")
  
```

---

