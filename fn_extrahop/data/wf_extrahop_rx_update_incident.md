<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-sdk codegen
-->

# Example: Extrahop Reveal(x) update incident

## Function - Extrahop Reveal(x) get detections

### API Name
`funct_extrahop_rx_get_detections`

### Output Name
`get_detections_result`

### Message Destination
`fn_extrahop`

### Pre-Processing Script
```python
inputs.extrahop_detection_id = incident.properties.extrahop_detection_id
```

### Post-Processing Script
```python
##  ExtraHop - wf_extrahop_rx_update_incident post processing script ##
#  Globals
FN_NAME = "funct_extrahop_rx_get_detections"
WF_NAME = "Example: Extrahop Reveal(x) update incident"
CONTENT = results.content
INPUTS = results.inputs
QUERY_EXECUTION_DATE = results["metrics"]["timestamp"]
DATA_TABLE = "extrahop_detections"
DATA_TBL_FIELDS = ["appliance_id", "assignee", "categories", "det_description", "end_time", "det_id", "is_user_created",
                   "mitre_tactics", "mitre_techniques", "participants", "properties", "resolution", "risk_score",
                   "start_time", "status", "ticket_id", "ticket_url", "title", "type", "update_time"]
# Read CATEGORY_MAP and TYPE_MAP dicts from workflow property.
CATEGORY_MAP = workflow.properties.category_map
TYPE_MAP = workflow.properties.type_map
LINKBACK_URL = "/extrahop/#/detections/detail/{}"

# Processing
def make_linkback_url(det_id):
    """Create a url to link back to the detection.

    Args:
        det_id (str/int): id representing the detection.

    Returns:
        str: completed url for linkback
    """
    return incident.properties.extrahop_console_url + LINKBACK_URL.format(det_id)

def addArtifact(artifact_type, artifact_value, description):
    """Add new artifacts to the incident.

    :param artifact_type: The type of the artifact.
    :param artifact_value: - The value of the artifact.
    :param description: - the description of the artifact.
    """
    incident.addArtifact(artifact_type, artifact_value, description)

# Processing
def main():
    detection_id = INPUTS["extrahop_detection_id"]
    note_text = u''
    if CONTENT:
        det = CONTENT.result
        note_text = u"ExtraHop Integration: Workflow <b>{0}</b>: A Detection was successfully returned for " \
                    u"detection ID <b>{1}</b> for SOAR function <b>{2}</b> with parameters <b>{3}</b>." \
            .format(WF_NAME, detection_id, FN_NAME, ", ".join("{}:{}".format(k, v) for k, v in INPUTS.items()))
        if det:
            detection_url = make_linkback_url(det["id"])
            detection_url_html = u'<div><b><a target="blank" href="{0}">{1}</a></b></div>' \
                         .format(detection_url, det["id"])
            newrow = incident.addRow(DATA_TABLE)
            newrow.query_execution_date = QUERY_EXECUTION_DATE
            newrow.detection_url = detection_url_html
            for f1 in DATA_TBL_FIELDS:
                f2 = f1
                if f1.startswith("det_"):
                    f2 = f1.split('_', 1)[1]
                if det[f2] is None or isinstance(det[f2], long):
                    newrow[f1] = det[f2]
                elif isinstance(det[f1], list):
                    if f1 == "categories":
                        newrow[f1] = "{}".format(", ".join(CATEGORY_MAP[c] if CATEGORY_MAP.get(c) else c for c in det[f2]))
                    elif f1 in ["participants", "mitre_tactics", "mitre_techniques"]:
                        if f1 == "participants":
                            for p in det[f2]:
                                if p["object_type"] == "ipaddr":
                                    artifact_type = "IP Address"
                                    addArtifact(artifact_type, p["object_value"],
                                                "Participant IP address in ExtraHop detection '{0}', role: '{1}'."
                                                .format(det["id"], p["role"]))
                                    if p["hostname"]:
                                        artifact_type = "DNS Name"
                                        addArtifact(artifact_type, p["hostname"],
                                                    "Participant DNS name in ExtraHop detection '{0}', role: '{1}'."
                                                    .format(det["id"], p["role"]))
                        obj_cnt = 0
                        tbl = u''
                        for i in det[f2]:
                            for k, v in i.items():
                                if k == "legacy_ids":
                                    tbl += u'<div><b>{0}:</b>{1}</div>'.format(k, ','.join(v))
                                elif k == "url":
                                    tbl += u'<div><b>{0}:<a target="blank" href="{1}">{2}</a></div>' \
                                        .format(k, v, i["id"])
                                else:
                                    tbl += u'<div><b>{0}:</b>{1}</div>'.format(k, v)
                            tbl += u"<br>"
                            obj_cnt += 1
                        newrow[f1] = tbl
                    else:
                        newrow[f1] = "{}".format(", ".join(det[f2]))
                elif isinstance(det[f2], (bool, dict)):
                    if f1 in ["properties"]:
                        tbl = u''
                        for i, j in det[f2].items():
                            if i == "suspicious_ipaddr":
                                artifact_type = "IP Address"
                                type = "Suspicious IP Addresses"
                                value = j["value"]
                                for ip in value:
                                    addArtifact(artifact_type, ip, "Suspicious IP address found by ExtraHop.")
                                tbl += u'<div><b>{0}:'.format(type)
                                tbl += u'<div><b>{0}'.format(", ".join("{}".format(i) for i in value))
                            else:
                                tbl += u'<div><b>{0}:</b>{1}</div>'.format(i, j)
                        newrow[f1] = tbl
                    else:
                        newrow[f1] = str(det[f2])
                else:
                    if f1 == "type":
                        newrow[f1] = TYPE_MAP[det[f2]] if TYPE_MAP.get(det[f2]) else det[f2]
                    elif f1 == "ticket_url":
                        newrow[f1] =  u'<div><b><a target="blank" href="{0}">{1}</a></div>'.format(det[f2], det[f2].split('/')[-1])
                    else:
                        newrow[f1] = "{}".format(det[f2])
            note_text += u"<br>The data table <b>{0}</b> has been updated".format("Extrahop Detections")
    else:
        note_text += u"ExtraHop Integration: Workflow <b>{0}</b>: There was <b>no</b> result returned while attempting " \
                     u"to get detections for detection ID <b>{1}</b> for SOAR function <b>{2}</b> ." \
                     u" with parameters <b>{3}</b>." \
            .format(WF_NAME, detection_id, FN_NAME, ", ".join("{}:{}".format(k, v) for k, v in INPUTS.items()))

    incident.addNote(helper.createRichText(note_text))


main()

```

---

## Function - Extrahop Reveal(x) get devices

### API Name
`funct_extrahop_rx_get_devices`

### Output Name
``

### Message Destination
`fn_extrahop`

### Pre-Processing Script
```python
None
```

### Post-Processing Script
```python
##  ExtraHop - wf_extrahop_rx_get_devices post processing script ##
#  Globals
FN_NAME = "funct_extrahop_rx_get_devices"
WF_NAME = "Example: Extrahop Reveal(x) update incident"
CONTENT = results.content
INPUTS = results.inputs
QUERY_EXECUTION_DATE = results["metrics"]["timestamp"]
# Display subset of fields
DATA_TABLE = "extrahop_devices"
DATA_TBL_FIELDS = ["display_name", "devs_description", "default_name", "dns_name", "ipaddr4", "ipaddr6", "macaddr",
                   "role", "vendor", "devs_id", "extrahop_id", "activity", "mod_time", "user_mod_time", "discover_time", 
                   "last_seen_time"]
LINKBACK_URL = "/extrahop/#/metrics/devices/{}.{}"


def make_linkback_url(dev_id):
    """Create a url to link back to the endpoint alert, case, etc.

    Args:
        dev_id (str/int): id representing the device etc.

    Returns:
        str: completed url for linkback
    """
    return incident.properties.extrahop_console_url + LINKBACK_URL.format(incident.properties.extrahop_site_uuid, dev_id)

def process_devs(dev):
    # Process a device result.
    newrow = incident.addRow(DATA_TABLE)
    newrow.query_execution_date = QUERY_EXECUTION_DATE
    for f1 in DATA_TBL_FIELDS:
        f2 = f1
        if f1.startswith("devs_"):
            f2 = f1.split('_', 1)[1]
        if dev[f1] is None:
            newrow[f1] = dev[f2]
        elif isinstance(dev[f2], list):
            newrow[f1] = "{}".format(", ".join(dev[f2]))
        elif isinstance(dev[f2], bool):
            newrow[f1] = str(dev[f2])
        elif f1 in ["mod_time", "user_mod_time", "discover_time", "last_seen_time"]:
            newrow[f1] = long(dev[f2])
        else:
            newrow[f1] = "{}".format(dev[f2])
    device_url = make_linkback_url(dev["extrahop_id"])
    device_url_html = u'<div><b><a target="blank" href="{1}">{2}</a></b></div>' \
              .format("url", device_url, dev["extrahop_id"])
    newrow.device_url = device_url_html

def get_dev_ids():
    # Get participant dev ids    
    dev_ids = []
    get_devices_content = workflow.properties.get_detections_result.content
    devs = get_devices_content["result"]
    participants = devs["participants"]
    for p in participants:
        if p["object_type"] == "device":
            dev_ids.append(p["object_id"])
    return dev_ids


# Processing
def main():
    participant_dev_ids = get_dev_ids()
    note_text = u''
    if CONTENT:
        devs = [d for d in CONTENT.result if d["id"] in participant_dev_ids]
        note_text = u"ExtraHop Integration: Workflow <b>{0}</b>: There were <b>{1}</b> Devices returned for SOAR " \
                    u"function <b>{2}</b> with parameters <b>{3}</b>.".format(WF_NAME, len(devs), FN_NAME, ", ".join(
            "{}:{}".format(k, v) for k, v in INPUTS.items()))
        if devs:
            if isinstance(devs, list):
                for dev in devs:
                    process_devs(dev)
            else:
                process_devs(devs)
            note_text += u"<br>The data table <b>{0}</b> has been updated".format(DATA_TABLE)

    else:
        note_text += u"ExtraHop Integration: Workflow <b>{0}</b>: There was <b>no</b> result returned while attempting " \
                     u"to get devices for SOAR function <b>{1}</b> with parameters <b>{2}</b>." \
            .format(WF_NAME, FN_NAME, ", ".join("{}:{}".format(k, v) for k, v in INPUTS.items()))

    incident.addNote(helper.createRichText(note_text))


main()
```

---

