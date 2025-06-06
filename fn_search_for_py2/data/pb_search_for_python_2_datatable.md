<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
    Generated with resilient-sdk v51.0.5.0.1475
-->

# Playbook - Check for Python 2

### API Name
`search_for_python_2_datatable`

### Status
`enabled`

### Activation Type
`Manual`

### Activation Conditions
`-`

### Object Type
`search_for_py2_results`

### Description
Search for Python2 in scripts, workflows and playbooks. Python 2 will be removed in an upcoming version of SOAR.


---
## Function - Search for Python 2

### API Name
`fn_search_for_py2`

### Output Name
`search_for_py2_results`

### Message Destination
`fn_search_for_py2`

### Function-Input Script
```python
inputs.py2_item_id = row["item_id"]
inputs.py2_item_type = row["item_type"]
inputs.py2_inc_id = incident.id
```

---

## Local script - search_for_py2__datatable_results

### Description


### Script Type
`Local script`

### Object Type
`search_for_py2_results`

### Script Content
```python
from datetime import datetime

results = playbook.functions.results.search_for_py2_results

PY2_LOOKUP = {
  "PY2_UNCONVERTIBLE": "Python 2 execution found, but script complexity prevents further analysis. Please review and, in some cases, changing the setting to Python 3 is the only change needed.",
  "PY2_CONVERTIBLE": "{item_type} set to run Python 2. This {item_type} can be easily changed to use Python 3. Check function input scripts, local scripts, and scripts used in conditions. Mostly likely the only change needed is to convert all language settings to Python 3.",
  "PY2_ITERS": "Python 2 iters found. Convert to use .items(), .keys(), and .values() as appropriate",
  "PY2_JAVA_UTIL_DATE": "'import java.util.Date' found. Change to 'from datetime import datetime' and datetime functions such as 'datetime.now()'.",
  "PY2_UNICODE": "Unicode strings found ('u' string prefix). This can remain for Python 3, but it's cleaner to remove."
}

def display_db_row(now, item_type, status, attributes):
  row["date"] = now
  row["status"] = status

  msg = []
  for attr in attributes:
    if PY2_LOOKUP.get(attr):
      row[attr.lower()] = "Yes"
      msg.append(PY2_LOOKUP.get(attr).format(item_type=item_type.title()))
    else:
      msg.append(attr)
  row["notes"] = "\n".join(msg)

def display_db():
  now = int(datetime.now().timestamp()*1000)
  is_found = False
  for item_type in ["script", "playbook", "workflow"]:
    for item_id, item_info in results.content.get(item_type, []).items():
      if row["item_type"] == item_type and int(row["item_id"]) == int(item_id):
        is_found = True
        display_db_row(now, item_type, "Unconverted", item_info.get("attributes", []))
        break

  if not is_found:
    display_db_row(now, None, "Converted", [f"{row['item_type']} is converted."])

# S T A R T
if results.success:
    display_db()
else:
    incident.addNote(f"Check for Python 2 failed: {results.reason}")

```

---

