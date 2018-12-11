# Resilient Integration with ClamAV
**This package contains a single function which uses ClamAV to scan a file or attachment for viruses and returns the
results of the scan.**

 ![screenshot](./screenshots/1.png)


## app.config settings:
```
[fn_clamav]
# hostname or ip address of Clamav server
host=localhost
# The TCP port Clamav listens on
port=3310
# Define socket timeout
timeout=500
```

## Function Inputs:
| Function Name | Type | Required | Example | Info |
| ------------- | :--: | :-------:| ------- | ---- |
| `base64content` | `String` | Yes | `"base64content: ..."` | Base64 encode string |
| `file_name` | `String` | Yes | `"eicar.txt"` | Attachment name|

## Function Output:
```python

results  {
    'file_name': u'eicar.txt',
    'response': {u'stream': [u'FOUND', u'Eicar-Test-Signature']}
}
```

## Pre-Process Script:
This example sets the inputs to create the Paste
```python
# The input is the base64-encoded content that was read in a previous component
# That object has properties:
#  - filename
#  - content_type
#  - size
#  - created
#  - content (the base64-encoded data)
# Only need to use the content and filenmame properties here.
inputs.base64content = workflow.properties.attachment_content.content
inputs.file_name = workflow.properties.attachment_content.filename
```

## Post-Process Script:
This example **adds a Note to the Incident** with a link to the Paste.
```python
##  CLAMAV - clamav_scan_stream script ##
# Example results:
"""
# Virus found
Result:    {
            "file_name": "eicar.txt",
            "response": {"stream": ["FOUND", "Eicar-Test-Signature"]},
           }
# No virus detected
Result:    {
            "file_name": "test.txt",
            "response": {"stream": ["OK", '']},
           }
# Got an error
Result:    {
            "file_name": "test.txt",
            "response": {"stream": ["ERROR", '<reason>']},
           }
"""
# Processing
response = results.response
file_name = results.file_name
query_execution_time = results.query_execution_time

if response is not None:
    if response.stream[0] == "FOUND":
        noteText = "ClamAV integration: A scan for attachment <b>{0}</b> detected a virus with signature <b>{1}</b>." \
                   "".format(file_name, response.stream[1])
    elif response.stream[0] == "OK":
        noteText = "ClamAV integration: A scan for attachment <b>{0}</b> did not detect any virus.".format(file_name)
    elif response.stream[0] == "ERROR":
        noteText = "ClamAV integration: A scan for attachment <b>{0}</b> threw an error".format(file_name)
incident.addNote(helper.createRichText(noteText))
```

## Rules
| Rule Name | Object Type | Workflow Triggered |
| --------- | :---------: | ------------------ |
| Example: ClamAV scan attachment | `Incident` | `Example: ClamAV scan attachment` |