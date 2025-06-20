<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Playbook - Exchange Online Delete Messages from Query Results - Example (PB)

### API Name
`example_exchange_online_delete_messages_from_query_results`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Activation Form Elements
| Input Field Label | API Name | Element Type | Tooltip | Requirement |
| ----------------- | -------- | ------------ | ------- | ----------- |
| End date/time | `exchange_online_end_datetime` | datetimepicker | Query messages received ending at this date/time. | Optional |
| Has attachments | `exchange_online_has_attachments` | boolean | Return messages which have attachments (Yes) or do not have attachments (No) | Optional |
| Mail Folder | `exchange_online_mail_folder_id` | select | The mailfolder to search. If none is selected, all mail folders are searched. | Optional |
| Message Body | `exchange_online_message_body` | text | - | Optional |
| Message Subject | `exchange_online_message_subject` | text | Text for the message subject to query | Optional |
| Monitored Email Address | `exchange_online_email_address_list` | text | Email addresses to search: a single email address, a comma separated list of email addresses, or "ALL" to search all users | Always |
| Query results output | `exchange_online_query_results_output` | multiselect | - | Always |
| Sender Email Address | `exchange_online_sender_email_address` | text | Enter the email address of the sender | Optional |
| Start date/time | `exchange_online_start_datetime` | datetimepicker | Query messages received starting at this date/time. | Optional |

### Object Type
`incident`

### Description
This playbook calls the Query Messages function to find messages that meet user input search criteria.  The results of the query are passed to the Delete Messages From Query Function.  The list of messages is deleted and placed in the data table, an incident note and/or an incident attachment, depending on the user input for the query results output format.


---
## Function - Exchange Online: Query Messages

### API Name
`exchange_online_query_emails`

### Output Name
`exchange_online_query_results`

### Message Destination
`fn_exchange_online`

### Function-Input Script
```python


inputs.incident_id = incident.id

# Get the email address of the user whose mailbox will be queried.
inputs.exo_email_address = playbook.inputs.exchange_online_email_address_list

# Get the search criteria from the activity rules if available. 


inputs.exo_mail_folders         = playbook.inputs.exchange_online_mail_folder_id
inputs.exo_email_address_sender = playbook.inputs.exchange_online_sender_email_address
inputs.exo_message_subject      = playbook.inputs.exchange_online_message_subject
inputs.exo_message_body         = playbook.inputs.exchange_online_message_body
inputs.exo_start_date           = playbook.inputs.exchange_online_start_datetime
inputs.exo_end_date             = playbook.inputs.exchange_online_end_datetime
inputs.exo_has_attachments      = playbook.inputs.exchange_online_has_attachments

    
if hasattr(playbook.inputs, "exchange_online_query_results_output"):
    inputs.exo_query_output_format = [d for d in playbook.inputs.exchange_online_query_results_output]








```

---
## Function - Exchange Online: Delete Messages From Query Results

### API Name
`exchange_online_delete_messages_from_query_results`

### Output Name
`exchange_online_delete_messages_from_query_results`

### Message Destination
`fn_exchange_online`

### Function-Input Script
```python
inputs.exo_query_messages_results = playbook.functions.results.exchange_online_query_results['raw']

```

---

## Local script - exchange_online_delete_messages_from_query_post_process

### Description


### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
from datetime import datetime
results=playbook.functions.results.exchange_online_delete_messages_from_query_results
content = results.get("content")
output_format = content.get("exo_query_output_format")


# Write to the data table if the user requested it.
if "Exchange Online data table" in output_format:
  
  user_list = content.get("delete_results")
  # Add each email as a row in the query results data table
  for user in user_list:
    
    for email in user["deleted_list"]:
      message_row = incident.addRow("exo_message_query_results_dt")
      message_row.exo_dt_query_date = datetime.now()
      message_row.exo_dt_message_id = email.get("id", "")
      message_row.exo_dt_received_date   = email.get("receivedDateTime")
      message_row.exo_dt_email_address = user.get("email_address")
      if email.get("sender"):
        message_row.exo_dt_sender_email = email["sender"]["emailAddress"]["address"]
      else:
        message_row.exo_dt_sender_email = ""
      message_row.exo_dt_message_subject = email.get("subject")
      message_row.exo_dt_has_attachments = email.get("hasAttachments")
      message_row.exo_dt_web_link = ""
      
      text = """<p style= "color:{color}">{status} </p>""".format(color="red", status="Deleted")
      message_row.exo_dt_status = helper.createRichText(text)

```

---

