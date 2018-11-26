# Resilient Integration with ServiceNow
**This package contains six functions that help integrate with the ServiceNow Platform**

 ![screenshot](./screenshots/1.png)


## app.config settings:
```python
[fn_service_now]
# Link to your ServiceNow Instance
sn_host=https://instance.service-now.com

# The URI to the ServiceNow App that handles the requests from Resilient
sn_api_uri=/api/x_261673_resilient/api

# The name of the table in ServiceNow you want to integrate with
sn_table_name=incident

# Username and Password for your Administrative User in ServiceNow
sn_username=
sn_password=
```

# Functions:

## **1: Create in ServiceNow**

### Function Inputs:
| Function Name | Type | Required | Example |
| ------------- | :--: | :-------:| ------- |
| `incident_id` | `Number` | Yes | `1001` |
| `task_id` | `Number` | No | `20000002` |
| `sn_init_work_note` | `String` | No | `"This Incident originated from our Cyber Security Team using the IBM Resilient platform"` |
| `sn_optional_fields` | `JSON String` | No | `"""{"assignment_group": "IT Security"}"""` |


### Function Output:
```python
results = {
  success: True,

  inputs: {
    incident_id: 2105,
    task_id: None
    sn_init_work_note: "Please investigate this",
    sn_optional_fields: {
      caller_id: "c1045b20db18230044ccd426ca9619fe",
      assignment_group: "5f6441efc0a8010e0177fcb589156352"
    }
  },

  res_id: "RES-2105",
  sn_ref_id: "INC0010453",
  sn_sys_id: "a48f21c5db82230044ccd426ca96198d",
  sn_time_created: 1543245771795,
  row_id: 45,
  res_link: "https://resilient-instance/#incidents/2105",
  sn_record_link: "https://instance.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC0010453",
}
```

### Pre-Process Script:
* This example defines and uses the `dict_to_json_str` function to allow us to easily set optional_fields we want to send to ServiceNow
* We also make use of user inputs from Rule Activity Fields by using: `rule.properties.sn_initial_note`
* In the supplied example Workflow, there are 3 Functions chained together, with this Function being the third. 
We use the output of the first and second functions here: 
  ```python
    "assignment_group": workflow.properties.assignment_group.sys_id,
    "caller_id": workflow.properties.caller_id.sys_id
  ```
The example:
```python
########################
### Define Functions ###
########################
def dict_to_json_str(d):
  """Function that converts a dictionary into a JSON string.
     Supports types: basestring, bool and int. 
     Supports nested directories.
     If the value is None, it sets it to False"""

  json_str = '"{ {0} }"'
  json_entry = '"{0}":{1}'
  json_entry_str = '"{0}":"{1}"'
  entries = [] 
  
  for entry in d:
    key = entry
    value = d[entry]
    
    if value is None:
      value = False
      
    if isinstance(value, basestring):
      value = value.replace(u'"', u'\\"')
      entries.append(json_entry_str.format(key, value))
    
    elif isinstance(value, bool):
      value = 'true' if value == True else 'false'
      entries.append(json_entry.format(key, value))
    
    elif isinstance(value, dict):
      entries.append(json_entry.format(key, dict_to_json_str(value)))
    
    else:
      entries.append(json_entry.format(key, value))
  
  return '{' + ','.join(entries) + '}'

#####################
### Define Inputs ###
#####################

# ID of this incident
inputs.incident_id = incident.id

# Initial work note to attach to created ServiceNow record
if rule.properties.sn_initial_note is not None:
  inputs.sn_init_work_note = rule.properties.sn_initial_note
else:
  inputs.sn_init_work_note = "This record was created by {0} [{1}] from IBM Resilient".format(principal.display_name, principal.name)

# Any further information you want to send to ServiceNow. Each Key/Value pair is attached to the Request object and accessible in ServiceNow.
inputs.sn_optional_fields = dict_to_json_str({
  "assignment_group": workflow.properties.assignment_group.sys_id,
  "caller_id": workflow.properties.caller_id.sys_id
})
```

### Post-Process Script:
This example **adds a Note to the Incident** with a link to the ServiceNow Record.
```python
if results.success:

  noteText = """<br>This Incident has been created in <b>ServiceNow</b>
              <br><b>ServiceNow ID:</b>  {0}
              <br><b>ServiceNow Link:</b> <a href='{1}'>{1}</a>""".format(results.sn_ref_id, results.sn_record_link)

  incident.addNote(helper.createRichText(noteText))
```

# Rules:
| Rule Name | Object Type | Activity Fields | Workflow Triggered |
| --------- | :---------: | --------------- | ------------------ |
| Create Incident in ServiceNow | `Incident` | `SN Assignment Group`, `SN Initial Note` | `Example: SN Utilities: Create Incident in ServiceNow` |
| Create Task in ServiceNow | `Task` | `SN Assignment Group`, `SN Initial Note` | `Example: SN Utilities: Create Task in ServiceNow` |