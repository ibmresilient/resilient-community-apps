<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v49.0.4423
-->

# Playbook - Data Table: Update Row - Example (PB)

### API Name
`example_data_utils_update_row_pb`

### Status
`enabled`

### Activation Type
`manual`

### Object Type
`dt_utils_test_data_table`

### Description
An example Playbook showing how to use the Data Table Utils: Update Row Function. It illustrates updating the current row with static values.


---
## Function - Data Table Utils: Update Row

### API Name
`dt_utils_update_row`

### Output Name
`results`

### Message Destination
`fn_datatable_utils`

### Function-Input Script
```python
from datetime import datetime

def dict_to_json_str(d):
  """Function that converts a dictionary into a JSON string.
     Supports types: basestring, bool, int, nested dicts and lists.
     If the value is None, it sets it to False."""

  json_entry = '"{0}":{1}'
  json_entry_str = '"{0}":"{1}"'
  entries = []

  for entry in d:
    key = entry
    value = d[entry]

    if not value:
      value = False

    elif isinstance(value, str):
      value = value.replace(u'"', u'\\"')
      entries.append(json_entry_str.format(key, value))

    elif isinstance(value, bool):
      value = 'true' if value else 'false'
      entries.append(json_entry.format(key, value))

    elif isinstance(value, dict):
      entries.append(json_entry.format(key, dict_to_json_str(value)))

    else:
      entries.append(json_entry.format(key, value))

  return '{0} {1} {2}'.format('{', ','.join(entries), '}')

# The ID of this incident
inputs.incident_id = incident.id

# The api name of the Data Table to update [here it is taken from previous Get Row Function]
inputs.dt_utils_datatable_api_name = "dt_utils_test_data_table"

# Refer to the existing row (value: 0)
inputs.dt_utils_row_id = 0

# The column api names and the value to update the cell to
inputs.dt_utils_cells_to_update = dict_to_json_str({"name": "Updated Example", "text": "Update from datatable", "number": 4598, "multi_select": ["b", "e", "g"], "boolean": True})
```

---

