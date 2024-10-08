<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Example: Data Table Utils: Create CSV Datatable

## Function - Data Table Utils: Create CSV Datatable

### API Name
`dt_utils_create_csv_table`

### Output Name
``

### Message Destination
`fn_datatable_utils`

### Pre-Processing Script
```python
# The ID of this incident
inputs.incident_id = incident.id
# The api name of the Data Table to update
inputs.dt_datable_name = "dt_utils_test_data_table"
# uncomment attachment_id when reading csv data from an attachmennt
inputs.attachment_id = attachment.id

# A boolean to determine if CSV headers are present
inputs.dt_has_headers = True

## The mapping format should be "csv_header":"dt_column_name"
mapping = '''{
  "hdr_number": "number",
  "hdr_text": "text",
  "hdr_boolean": "boolean",
  "hdr_datetime": "datetime",
  "hdr_select": "select",
  "hdr_multiselect": "multi_select"
}'''
# mappings of csv data without headers will be a list of data_table column names. Use null to bypass a csv data column
mapping_no_headers = '''["number","text","boolean","datetime","select","multi_select","x","y","z"]'''
inputs.dt_mapping_table = mapping
# year - %Y, month - %m, day - %d, hour - %H, minutes - %M, seconds - %S, milliseconds - %f, timezone offset - %z'
inputs.dt_date_time_format = "%m/%d/%y %H:%M"
# optional start row csv data. The first data row = 1
##inputs.dt_start_row = 0
# optional max number of csv rows to add relative to dt_start_row
##inputs.dt_max_rows = 5
```

### Post-Processing Script
```python
if results.success:
  note_text = u"""Results from Data Table Utils: Create CSV Datatable\nData Source: {}\nRows added: {}\nRows not added: {}""".format(results.content["data_source"], results.content["rows_added"], results.content["rows_with_errors"])
  incident.addNote(note_text)
else:
  incident.addNote(u"Error: Failed to add rows")
```

---

