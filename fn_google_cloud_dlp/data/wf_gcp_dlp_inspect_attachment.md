<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v50.1.262
-->

# Example: Google Cloud DLP - Inspect Attachment for PII

## Function - Google Cloud DLP: Inspect Content

### API Name
`google_cloud_dlp_inspect_content`

### Output Name
`None`

### Message Destination
`fn_google_cloud_dlp`

### Pre-Processing Script
```python
inputs.incident_id = incident.id 

# If this workflow has the task_id available, gather it incase we need it.
if task:
  inputs.task_id = task.id
# If this workflow has the attachment_id available, gather it incase we need it.
if attachment:
  inputs.attachment_id = attachment.id

# If this workflow has the artifact_id available, gather it incase we need it.
try: 
  if artifact:
    inputs.artifact_id = artifact.id
except:
  pass
```

### Post-Processing Script
```python
if results.get("success"):
    """Print all the findings as a richtext note. This note may be very long if you run the integration on a large file with lots of PII. In these cases you may want to limit how many findings are put into the note."""
    if results.get("content", {}).get("findings") is not None:
        attachment_name = results.get("content", {}).get("attachment_name")
        note_text = """Findings were found from attachment <b>{}</b><br><br> Findings: <br>""".format(attachment_name)
        for finding in results.get("content", {}).get("findings", []):
            text_quote = finding.get("quote")
            info_type = finding.get("info_type")
            likelihood = finding.get("likelihood")
            note_text += """Text Quote: <b>{}</b>
                            <br> Information Type Suspected: <b>{}</b>
                            <br> Likelihood / Confidence: <b>{}</b><br><br>""".format(text_quote, info_type, likelihood)
        incident.addNote(helper.createRichText(note_text))

```

---

