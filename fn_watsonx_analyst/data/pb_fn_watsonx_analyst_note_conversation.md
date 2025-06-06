<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.4.0.1351
-->

# Playbook - watsonx.ai Note Conversation

### API Name
`fn_watsonx_analyst_note_conversation`

### Status
`enabled`

### Activation Type
`Automatic`

### Activation Conditions
`note.text contains @watsonx AND object_added`

### Object Type
`note`

### Description
This Playbook is triggered when a user writes a note that contains "@watsonx" at the start of the note. 

A reply will be generated by IBM watsonx.ai generative AI, and added as a reply to the first note.


---
## Function - watsonx.ai Converse via Notes

### API Name
`fn_watsonx_analyst_converse_via_notes`

### Output Name
`ai_response`

### Message Destination
`fn_watsonx_analyst`

### Function-Input Script
```python

inputs.fn_watsonx_analyst_incident_id = incident.id
inputs.fn_watsonx_analyst_model_id = "ibm/granite-3-2b-instruct"
inputs.fn_watsonx_analyst_note_id = note.id

```

---

## Global script - watsonx.ai Respond to note

### Description


### Script Type
`Global script`

### Object Type
`note`

### Script Content
```python

generated_text = playbook.functions.results.ai_response["content"]["generated_text"]
tag = playbook.functions.results.ai_response["content"]["tag"]

if generated_text != "":
  note.addNote(tag + generated_text)

```

---

