<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v52.0.0.0.927
-->

# Example: AMP delete file from list

## Function - AMP: Delete File from List

### API Name
`fn_amp_delete_file_list_files`

### Output Name
`None`

### Message Destination
`fn_cisco_amp`

### Pre-Processing Script
```python
inputs.amp_file_list_guid = row.guid
inputs.amp_file_sha256 = row.sha256

```

### Post-Processing Script
```python
##  Cisco AMP for endpoints - fn_amp_delete_file_lists script ##
#  fn_amp_delete_computer_trajectory  -  Event type list
# Example result:
"""
Result:    {
             "input_params": {"file_list_guid": "e773a9eb-296c-40df-98d8-bed46322589d",
                       "file_sha256": "8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284"}
             "response": {u'version': u'v1.2.0',
                          u'data': {},
                          u'metadata': {u'links': {
                                            u'self': u'https://api.amp.cisco.com/v1/file_lists/e773a9eb-296c-40df-98d8-bed46322589d/files/8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284'}
                                       }
                          },
              "delete_execution_time": "2018-08-09 11:56:02"
            }

"""
#  Globals
# List of fields in datatable fn_amp_get_file_lists script
DATA_TBL_FIELDS = ["delete_execution_time", "status"]

# Processing
response = results.get("response")

if response is not None:
    noteText = "Cisco AMP for Endpoints Integration: Successfully deleted file with sha256 value <b>{0}</b> " \
               "from SCD list guid <b>{1}</b> for SOAR function <b>{2}</b>."\
        .format(row.sha256, row.guid, "fn_amp_delete_file_list_files")
else:
  noteText = "Cisco AMP Integration: Delete unsuccessful for file with sha256 value <b>{0}</b> " \
               "from SCD list guid <b>{1}</b> for SOAR function <b>{2}</b>."\
        .format(row.sha256, row.guid, "fn_amp_delete_file_list_files")

incident.addNote(helper.createRichText(noteText))
```

---

