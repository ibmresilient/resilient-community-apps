<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Example: Extrahop Reveal(x) update watchlist

## Function - Extrahop Reveal(x) update watchlist

### API Name
`funct_extrahop_rx_update_watchlist`

### Output Name
`None`

### Message Destination
`fn_extrahop`

### Pre-Processing Script
```python
dev_id = row.devs_id
action = rule.properties.extrahop_watchlist_action
if action == "add":
    inputs.extrahop_assign = str(dev_id)
elif action == "remove":
    inputs.extrahop_unassign = str(dev_id)
```

### Post-Processing Script
```python
##  ExtraHop - wf_extrahop_rx_update_watchlist post processing script ##
#  Globals
FN_NAME = "funct_extrahop_rx_update_watchlist"
WF_NAME = "Example: Extrahop Reveal(x) update watchlist"
CONTENT = results.content
INPUTS = results.inputs

# Processing
def main():
    note_text = u''
    if CONTENT:
        result = CONTENT["result"]
        if result == "success":
            workflow.addProperty("watchlist_updated", {})
            note_text = u"ExtraHop Integration: Workflow <b>{0}</b>: Successfully updated the watchlist for SOAR " \
                        u"function <b>{1}</b> with parameters <b>{2}</b> for device <b>{3}</b>."\
                .format(WF_NAME, FN_NAME, ", ".join("{}:{}".format(k, v) for k, v in INPUTS.items()), row.devs_id)
        elif result == "failed":
            note_text = u"ExtraHop Integration: Workflow <b>{0}</b>: Failed to update the watchlist for " \
                        u"SOAR function <b>{1}</b> with parameters <b>{2}</b> for device <b>{3}</b>."\
                .format(WF_NAME, FN_NAME, ", ".join("{}:{}".format(k, v) for k, v in INPUTS.items()))
        elif result == "conflict":
            note_text = u"ExtraHop Integration: Workflow <b>{0}</b>: A 409 (conflict) error was thrown while attempting  " \
                        u"to update the watchlist for SOAR function <b>{1}</b> with parameters <b>{2}</b> for device <b>{3}</b>."\
                .format(WF_NAME, FN_NAME, ", ".join("{}:{}".format(k, v) for k, v in INPUTS.items()), row.devs_id)
            note_text += u"<br>Check if the sensor is being managed from the cloud-based service."
        else:
            note_text = u"ExtraHop Integration: Workflow <b>{0}</b>: Update watchlist failed with unexpected " \
                        u"response for SOAR function <b>{1}</b> with parameters <b>{2}</b> for device <b>{3}</b>."\
                .format(WF_NAME, FN_NAME, ", ".join("{}:{}".format(k, v) for k, v in INPUTS.items()), row.devs_id)
    else:
        note_text += u"ExtraHop Integration: Workflow <b>{0}</b>: There was <b>no</b> result returned while attempting " \
                     u"to update the watchlist <b>{1}</b> with parameters <b>{2}</b> for device <b>{3}</b>."\
            .format(WF_NAME, FN_NAME, ", ".join("{}:{}".format(k, v) for k, v in INPUTS.items()), row.devs_id)

    incident.addNote(helper.createRichText(note_text))

main()

```

---

## Function - Extrahop Reveal(x) get devices

### API Name
`funct_extrahop_rx_get_devices`

### Output Name
`None`

### Message Destination
`fn_extrahop`

### Pre-Processing Script
```python
inputs.extrahop_device_id = row.devs_id
```

### Post-Processing Script
```python
##  ExtraHop - wf_extrahop_rx_get_devices post processing script ##
#  Globals
FN_NAME = "funct_extrahop_rx_get_devices"
WF_NAME = "Example: Extrahop Reveal(x) update watchlist"
CONTENT = results.content
INPUTS = results.inputs
QUERY_EXECUTION_DATE = results["metrics"]["timestamp"]
# Display subset of fields
DATA_TABLE = "extrahop_devices"
DATA_TBL_FIELDS = ["display_name", "devs_description", "default_name", "dns_name", "ipaddr4", "ipaddr6", "macaddr",
                   "role", "vendor", "devs_id", "extrahop_id", "activity", "on_watchlist", "mod_time", "user_mod_time", "discover_time", 
                   "last_seen_time"]

def process_devs(dev):
    # Process a device result.
    row.query_execution_date = QUERY_EXECUTION_DATE
    for f1 in DATA_TBL_FIELDS:
        f2 = f1
        if f1.startswith("devs_"):
            f2 = f1.split('_', 1)[1]
        if dev[f1] is None:
            row[f1] = dev[f2]
        elif isinstance(dev[f2], list):
            row[f1] = "{}".format(", ".join(dev[f2]))
        elif isinstance(dev[f2], bool):
            row[f1] = str(dev[f2])
        elif f1 in ["mod_time", "user_mod_time", "discover_time", "last_seen_time"]:
            row[f1] = long(dev[f2])
        else:
           row[f1] = "{}".format(dev[f2])

# Processing
def main():
    note_text = u''
    if CONTENT:
        dev = CONTENT.result
        note_text = u"ExtraHop Integration: Workflow <b>{0}</b>: There was a Device returned for SOAR " \
                    u"function <b>{1}</b> with parameters <b>{2}</b>.".format(WF_NAME, FN_NAME, ", ".join(
            "{}:{}".format(k, v) for k, v in INPUTS.items()))
        if dev:
            process_devs(dev)
            note_text += u"<br>The data table <b>{0}</b> has been updated".format(DATA_TABLE)

    else:
        note_text += u"ExtraHop Integration: Workflow <b>{0}</b>: There was <b>no</b> result returned while attempting " \
                     u"to get devices for SOAR function <b>{1}</b> with parameters <b>{2}</b>." \
            .format(WF_NAME, FN_NAME, ", ".join("{}:{}".format(k, v) for k, v in INPUTS.items()))

    incident.addNote(helper.createRichText(note_text))


main()

```

---

