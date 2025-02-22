<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v50.1.262
-->

# Example: BigFix Retrieve Resource Details

## Function - BigFix Assets

### API Name
`fn_bigfix_assets`

### Output Name
``

### Message Destination
`fn_bigfix`

### Pre-Processing Script
```python
inputs.bigfix_asset_name = row.res_bigfix_computer_name
inputs.bigfix_asset_id = row.res_bigfix_computer_id
inputs.bigfix_incident_id = incident.id

```

### Post-Processing Script
```python
result = results.get("content")
status = result.get("status")
status_note = result.get("status_note")
att_name = result.get("att_name")

if status and status == "OK":
  noteText = u"BigFix Integration: Ran query for BigFix Asset id <b>'{}'</b> and name <b>'{}'</b>. " \
             "Added as an attachment. Attachment name: <b>{}</b> "\
              .format(row.res_bigfix_computer_id, unicode(row.res_bigfix_computer_name), att_name)
else:
  noteText = u"BigFix Integration: Query unsuccessful for BigFix Asset id <b>'{}'</b> and name <b>'{}'</b>."\
              .format(row.res_bigfix_computer_id, unicode(row.res_bigfix_computer_name))

incident.addNote(helper.createRichText(noteText))
```

---

