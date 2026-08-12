import os
from fn_microsoft_defender.lib.jinja_common import render_json, JinjaEnvironment
from resilient_circuits.template_functions import environment, render

create_incident_data_url_fix = {
  "incidentName": "",
  "incidentUri": "https://resilientsystems.com",
  "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Alerts/$entity",
  "id": "da637792709228082931_312545642",
  "incidentId": 39,
  "investigationId": "None",
  "assignedTo": "None",
  "severity": "Medium",
  "status": "New",
  "classification": "None",
  "determination": "None",
  "investigationState": "UnsupportedAlertType",
  "detectionSource": "WindowsDefenderAtp",
  "detectorId": "7f1c3609-a3ff-40e2-995b-c01770161d68",
  "category": "Execution",
  "threatFamilyName": "None",
  "title": "Suspicious PowerShell command line",
  "description": "A suspicious PowerShell activity was observed on the machine. \nThis behavior may indicate that PowerShell was used during installation, exploration, or in some cases in lateral movement activities which are used by attackers to invoke modules, download external payloads, or get more information about the system. Attackers usually use PowerShell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.",
  "createdTime": "2022-02-01T00:08:42.8083243Z",
  "alertCreationTime": "2022-02-01T00:08:42.8083243Z",
  "firstEventTime": "2022-01-31T23:46:32.8126235Z",
  "lastEventTime": "2022-01-31T23:46:32.8126235Z",
  "lastUpdateTime": "2022-02-01T21:05:48.8466667Z",
  "resolvedTime": "None",
  "machineId": "93dfc3af285816182861e0a5252624420bcc0484",
  "computerDnsName": "windowsvmos2",
  "rbacGroupName": "None",
  "aadTenantId": "50ad7d3e-b889-434d-802d-13b87c68047b",
  "threatName": "None",
  "mitreTechniques": [
    "T1059.001"
  ],
  "tags": [
    
  ],
  "alerts": [{
    "entities": [
      {
        "deviceId": "12345",
        "entityType": "Url",
        "url": "123.45.78.90",
        "evidenceCreationTime": "2017-07-06T01:25:04.9480498Z",
        "machine_comment": "some comment"
      }
    ]
  }],
  "comments": [
    
  ]
}

create_incident_data_url_ok = {
  "incidentName": "",
  "incidentUri": "https://resilientsystems.com",
  "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Alerts/$entity",
  "id": "da637792709228082931_312545642",
  "incidentId": 39,
  "investigationId": "None",
  "assignedTo": "None",
  "severity": "Medium",
  "status": "New",
  "classification": "None",
  "determination": "None",
  "investigationState": "UnsupportedAlertType",
  "detectionSource": "WindowsDefenderAtp",
  "detectorId": "7f1c3609-a3ff-40e2-995b-c01770161d68",
  "category": "Execution",
  "threatFamilyName": "None",
  "title": "Suspicious PowerShell command line",
  "description": "A suspicious PowerShell activity was observed on the machine. \nThis behavior may indicate that PowerShell was used during installation, exploration, or in some cases in lateral movement activities which are used by attackers to invoke modules, download external payloads, or get more information about the system. Attackers usually use PowerShell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.",
  "createdTime": "2022-02-01T00:08:42.8083243Z",
  "alertCreationTime": "2022-02-01T00:08:42.8083243Z",
  "firstEventTime": "2022-01-31T23:46:32.8126235Z",
  "lastEventTime": "2022-01-31T23:46:32.8126235Z",
  "lastUpdateTime": "2022-02-01T21:05:48.8466667Z",
  "resolvedTime": "None",
  "machineId": "93dfc3af285816182861e0a5252624420bcc0484",
  "computerDnsName": "windowsvmos2",
  "rbacGroupName": "None",
  "aadTenantId": "50ad7d3e-b889-434d-802d-13b87c68047b",
  "threatName": "None",
  "mitreTechniques": [
    "T1059.001"
  ],
  "tags": [
    
  ],
  "alerts": [{
    "entities": [
      {
        "deviceId": "12345",
        "entityType": "Url",
        "url": "https://123.45.78.90",
        "evidenceCreationTime": "2017-07-06T01:25:04.9480498Z",
        "machine_comment": "some comment"
      }
    ]
  }],
  "comments": [
    
  ]
}


def test_create_incident_template():
    env = JinjaEnvironment()
    create_template_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../fn_microsoft_defender/lib/data/incident_creation_template.jinja")

    template = env.get_template(create_template_file, None)
    result = render_json(template, create_incident_data_url_fix)
    assert result.get("artifacts", [])[0].get("value").startswith("https")

    result = render_json(template, create_incident_data_url_ok)
    assert result.get("artifacts", [])[0].get("value")  == "https://123.45.78.90"
