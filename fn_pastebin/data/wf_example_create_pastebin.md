<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Example: Create Pastebin

## Function - Create Pastebin

### API Name
`fn_create_pastebin`

### Output Name
``

### Message Destination
`fn_pastebin`

### Pre-Processing Script
```python
# This is the text that will be written inside your paste
inputs.pastebin_code = """ example code here """

# This will be the name / title of your paste
inputs.pastebin_name = "Example Name"

# This will be the syntax highlighting value. Format codes, see here: https://pastebin.com/api
inputs.pastebin_format = "python"

# This makes a paste public, unlisted or private. (Public = 0, Unlisted = 1, Private = 2)
inputs.pastebin_privacy = 2

# This sets the expiration date of your paste. Expiration codes, see here: https://pastebin.com/api
inputs.pastebin_expiration = "1H"
```

### Post-Processing Script
```python
if (results.success):
  noteText = """<br><b>Pastebin Created</b>
                <b>Name:</b> {0}
                <b>Link:</b> <a href='{1}'>{1}</a>""".format(results.inputs.get('pastebin_name'), results.get('pastebin_link'))
  incident.addNote(helper.createRichText(noteText))
```

---

