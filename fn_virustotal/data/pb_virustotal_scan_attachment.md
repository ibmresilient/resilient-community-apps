<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.1.1.824
-->

# Playbook - Example: VirusTotal for Attachments (PB)

### API Name
`virustotal_scan_attachment`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Object Type
`attachment`

### Description
Perform a VirusTotal scan on an attachment.  Write the results to a note.


---
## Function - VirusTotal

### API Name
`virustotal`

### Output Name
`vt_scan_results`

### Message Destination
`fn_virustotal`

### Function-Input Script
```python
inputs.vt_type = 'file'
inputs.incident_id = incident.id
inputs.attachment_id = attachment.id
inputs.task_id = task.id if task else None
inputs.artifact_id = None
inputs.vt_data = None
```

---

## Local script - VirusTotal: Write results to an incident note

### Description
Write the results of an VirusTotal scan of an attachment to a note.

### Script Type
`Local script`

### Object Type
`attachment`

### Script Content
```python
from datetime import datetime
from json import dumps

VIRUSTOTAL_GUI_URL = "https://www.virustotal.com/gui"

results = playbook.functions.results.vt_scan_results

# Uncomment the following 2 lines to have the results json printed formatted to a note.
#pretty_results = dumps(results, indent=4, sort_keys=True)
#incident.addNote(helper.createRichText(u"<p>VirusTotal scan of attachment: {0} with attachment_id: {1}</p><div>{2}</div>".format(attachment.name, attachment.id, pretty_results)))

msg = f"<p>VirusTotal scan of Attachment: <b>{attachment.name}</b> with attachment_id: {attachment.id}</p>"
scan = results.get("content", {}).get("scan",  {})
if not scan:
  raise Exception(f"No scan data returned VirusTotal scan on attachment: {attachment.name} with attachment_id: {attachment.id}")

data = scan.get("data", {})
scan_error = scan.get("error", {})
if scan_error:
  msg = f"{msg}Error returned: {scan_error}"
  #helper.fail("Error returned from VirusTotal scan of attachment: {0}: {1}".format(attachment.name, scan_error))

stats = {}
attributes = {}
if data:
  attributes = data.get("attributes", {})
  if attributes:
    # If this a report the stats are in last_analysis_stats otherwise they are in stats
    stats = attributes.get("last_analysis_stats", {})
    if stats == {}:
	    stats = attributes.get("stats", {})

for k,v in stats.items():
  if k.lower() == "malicious":
    msg = f"{msg}{k}: <span style='color:red'>{v}</span><br>"
  else:
    msg = f"{msg}{k}: {v}<br>"

last_analysis_date = attributes.get("last_analysis_date", None)
if last_analysis_date:
  last_analysis_date_str = datetime.fromtimestamp(last_analysis_date).strftime('%Y-%b-%d %H:%M:%S')
  msg = f"{msg}<br>Last analysis date: {last_analysis_date_str}"

# Add VirusTotal Report link to the note
if data:
  vt_id = data.get("id", None)
  if vt_id:
    link_back = f"<a href='{VIRUSTOTAL_GUI_URL}/file/{vt_id}'>VirusTotal Report</a>"
    msg = f"{msg}<br>{link_back}"

if not stats:
  msg = f"{msg}No stats returned from scan attachment: {attachment.name} with attachment_id: {attachment.id}"

incident.addNote(helper.createRichText(f"<div>{msg}</div>"))

# Create artifacts from results
last_http_response_content_sha256 = attributes.get("last_http_response_content_sha256", None)
if last_http_response_content_sha256:
  incident.addArtifact('Malware SHA-256 Hash', last_http_response_content_sha256, f"Created by VirusTotal scan of attachment {attachment.name} with attachment_id: {attachment.id}")

sha256 = attributes.get("sha256", None)
if sha256:
  incident.addArtifact('Malware SHA-256 Hash', sha256, f"Created by VirusTotal scan of of attachment {attachment.name} with attachment_id: {attachment.id}")

md5 = attributes.get("md5", None)
if md5:
  incident.addArtifact('Malware MD5 Hash', md5, f"Created by VirusTotal scan of of attachment {attachment.name} with attachment_id: {attachment.id}")

sha1 = attributes.get("sha1", None)
if sha1:
  incident.addArtifact('Malware SHA-1 Hash', sha1, f"Created by VirusTotal scan of of attachment {attachment.name} with attachment_id: {attachment.id}")
```

---

