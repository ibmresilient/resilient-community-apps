<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Example: IsItPhishing Analyze URL

## Function - IsItPhishing URL

### API Name
`isitphishing_url`

### Output Name
`None`

### Message Destination
`fn_isitphishing`

### Pre-Processing Script
```python
# Get the URL from the artifact value
inputs.isitphishing_url = artifact.value
```

### Post-Processing Script
```python
# Get the results and post to an incident note.
if results.success:
  content = 'IsItPhishing analysis of URL {0} : {1}\n'.format(results.get('inputs', {}).get('isitphishing_url'), results.get('content', {}).get('status'))
else:
  content = 'IsItPhishing analysis of URL {0} : ERROR\n'.format(results.get('inputs', {}).get('isitphishing_url'))
note = helper.createPlainText(content)
incident.addNote(note)
```

---

