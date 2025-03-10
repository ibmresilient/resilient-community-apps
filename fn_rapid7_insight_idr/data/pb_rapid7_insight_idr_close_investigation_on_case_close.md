<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.0.2.575
-->

# Playbook - Rapid7 InsightIDR: Close Investigation On Case Close

### API Name
`rapid7_insight_idr_close_investigation_on_case_close`

### Status
`enabled`

### Activation Type
`Automatic`

### Activation Conditions
`incident.plan_status changed_to Closed AND incident.properties.rapid7_insight_idr_rrn has_a_value`

### Object Type
`incident`

### Description
Automatic playbook that updates the Status and disposition of the associated investigation in Rapid7 InsightIDR when the cases is closed in SOAR.  The SOAR case resolution summary is written as a comment to the Rapid7 InsightIDR investigation.


---
## Function - Rapid7: InsightIDR Set Status

### API Name
`rapid7_insight_idr_set_status`

### Output Name
`set_status_results`

### Message Destination
`fn_rapid7_insight_idr`

### Function-Input Script
```python
STATUS_LOOKUP = {
  "Unresolved": "CLOSED",   # Unresolved
  "Duplicate": "CLOSED",    # Duplicate
  "Not an Issue": "CLOSED", # Not an Issue
  "Resolved": "CLOSED"      # Resolved
}

inputs.rapid7_insight_idr_incident_id = incident.id
inputs.rapid7_insight_idr_rrn = incident.properties.rapid7_insight_idr_rrn
inputs.rapid7_insight_idr_status = STATUS_LOOKUP.get(incident.resolution_id, "CLOSED")

# The disposition is updated in the Close case layout dialog so pick it up from the custom field
if incident.properties.rapid7_insight_idr_disposition == "Undecided":
  helper.fail("Rapid7 InsightIDR Investigation cannot be closed with Disposition: Undecided")
else:
  inputs.rapid7_insight_idr_disposition = incident.properties.rapid7_insight_idr_disposition


```

---
## Function - Rapid7 InsightIDR: Post Comment to Rapid7 Investigation

### API Name
`rapid7_insight_idr_post_comment`

### Output Name
`post_comment_results`

### Message Destination
`fn_rapid7_insight_idr`

### Function-Input Script
```python
inputs.rapid7_insight_idr_rrn = incident.properties.rapid7_insight_idr_rrn
inputs.rapid7_insight_idr_comment_text = incident.resolution_summary.content if incident.resolution_summary.content else "Case {0} was closed in QRadar SOAR".format(incident.id)
```

---

## Local script - Rapid7 InsightIDR: Write set status results to a note

### Description
Write functions results to set the status in Rapid7 InsightIDR investigation.

### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.set_status_results

if results.get("success"):
  note_text = "<b>Rapid7 InsightIDR: Set Status on Close:</b> Closed investigation in Rapid7 InsightIDR"
else:
  note_text = "<b>Rapid7 InsightIDR: Set Status on Close:</b> Failed function to set status. Reason = {0}".format(results.get("reason"))
  
incident.addNote(note_text)
```

---
## Local script - Rapid7 InsightIDR: Write comment post error to a note

### Description
Write post comment function results to a note.

### Script Type
`Local script`

### Object Type
`incident`

### Script Content
```python
results = playbook.functions.results.post_comment_results

note_text = "Rapid7 InsightIDR Automatic playbook <b>On close from SOAR case</b> failed to post comment to Rapid7 InsightIDR: {0}".format(results.get("reason", None))

incident.addNote(note_text)
```

---

