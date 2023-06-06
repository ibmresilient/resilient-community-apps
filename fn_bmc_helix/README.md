# BMC Helix

## Table of Contents
- [Release Notes](#release-notes)
- [Overview](#overview)
  - [Key Features](#key-features)
- [Requirements](#requirements)
  - [SOAR platform](#soar-platform)
  - [Cloud Pak for Security](#cloud-pak-for-security)
  - [Proxy Server](#proxy-server)
  - [Python Environment](#python-environment)
- [Installation](#installation)
  - [Install](#install)
  - [App Configuration](#app-configuration)
  - [Custom Layouts](#custom-layouts)
- [Function - Helix: Close Incident](#function---helix-close-incident)
- [Function - Helix: Create Incident](#function---helix-create-incident)
- [Data Table - Helix Linked Incidents Reference Table](#data-table---helix-linked-incidents-reference-table)
- [Rules](#rules)
- [Troubleshooting & Support](#troubleshooting--support)

---

## Release Notes
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.0.0 | 06/2023 | Initial Release |

---

## Overview

**BMC Helix for IBM SOAR**

 ![screenshot: main](./doc/screenshots/main.png)

BMC Helix for IBM SOAR This integration provides the capability to create new incidents in BMC Helix from SOAR tasks via the HPD:IncidentInterface_Create form over the REST API. Once the task is complete, this integration also provides the capability to close existing BMC Helix Incidents.

### Key Features
* Send IBM SOAR Case tasks to BMC Helix as Incidents
* Close BMC Helix Incidents from IBM SOAR

---

## Requirements
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, Edge Gateway (formerly App Host) and integration server.

If deploying to a SOAR platform with an Edge Gateway, the requirements are:
* SOAR platform >= `46.0.8131`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `46.0.8131`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient-circuits>=46.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions: 
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read |
  | Function | Read |
  | Incidents |  Read |
  | Incident Notes | Write |
  | Private Tasks | Read |

The following SOAR platform guides provide additional information: 
* _Edge Gateway Deployment Guide_ or _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. 
* _Integration Server Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _System Administrator Guide_: provides the procedure to install, configure and deploy apps. 

The above guides are available on the IBM Documentation website at [ibm.biz/soar-docs](https://ibm.biz/soar-docs). On this web page, select your SOAR platform version. On the follow-on page, you can find the _Edge Gateway Deployment Guide_, _App Host Deployment Guide_, or _Integration Server Guide_ by expanding **Apps** in the Table of Contents pane. The System Administrator Guide is available by expanding **System Administrator**.

### Cloud Pak for Security
If you are deploying to IBM Cloud Pak for Security, the requirements are:
* IBM Cloud Pak for Security >= `1.8`.
* Cloud Pak is configured with an Edge Gateway.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

The following Cloud Pak guides provide additional information: 
* _Edge Gateway Deployment Guide_ or _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. From the Table of Contents, select Case Management and Orchestration & Automation > **Orchestration and Automation Apps**.
* _System Administrator Guide_: provides information to install, configure, and deploy apps. From the IBM Cloud Pak for Security IBM Documentation table of contents, select Case Management and Orchestration & Automation > **System administrator**.

These guides are available on the IBM Documentation website at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs). From this web page, select your IBM Cloud Pak for Security version. From the version-specific IBM Documentation page, select Case Management and Orchestration & Automation.

### Proxy Server
The app **does** support a proxy server.

### BMC Helix Platform
This app requires BMC Helix IT Service Management Suite 20.x or above with AR Server 9.x or above. The REST API must be enabled and exposed on any port. If the REST API is not already enabled on the BMC Helix Platform, consult their documentation on [Configuring the REST API](https://docs.bmc.com/docs/ars91/en/configuring-the-rest-api-609071434.html).

### Python Environment
Python 3.6 and Python 3.9 are supported.
Additional package dependencies may exist for each of these packages:
* resilient-circuits>=46.0.0

---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **helix_host** | Yes | `<example.domain>` | *Hostname or IP for the BMC Helix instance.* |
| **helix_user** | Yes | `<example_user>` | *Username to use to authenticate with BMC Helix.* |
| **helix_password** | Yes | `xxx` | *Password to use to authenticate with BMC Helix.* |
| **max_datatable_rows** | No | `30` | *Max number of datatable rows to return from the SOAR API when closing an Incident.* |
| **helix_port** | No | `8443` | *Port number over which the BMC Helix REST API is exposed.* |
| **verify** | No | `true|false|/path/to/certificate.crt` | *Set to `true` or `/path/to/cerficate.crt` to make verified requests to BMC Helix, else set to `false`* |
| **https_proxy** | No | `example.domain` | *https proxy for request traffic.* |

### Custom Layouts
* Import the Data Tables and Custom Fields like the screenshot below:

  ![screenshot: custom_layouts](./doc/screenshots/custom_layouts.png) <!-- ::CHANGE_ME:: -->


---

## Function - Helix: Close Incident
Close an incident ticket in BMC Helix by modifying its status. The function will make an API call to BMC Helix to retrieve the target incident form. If the status of that form is "Resolved," "Closed," or "Cancelled," no change to the incident is made. Otherwise, the status is updated to Resolved with Status Reason "No Further Action Required" and Resolution "Closed from IBM SOAR."

When a task is closed under a case, an automatic rule will trigger containing this function. If a row in the BMC Helix datatable matches the name and ID of the task just closed, the logic described above will trigger to ensure that the corresponding incident in BMC Helix is also closed.

In the event that multiple rows in the datatable match the target task (a task has been raised to BMC Helix more than once), the function will iterate over those rows to ensure that each of the corresponding incidents in BMC Helix are closed.

 ![screenshot: fn-helix-close-incident ](./doc/screenshots/fn-helix-close-incident.png) <!-- ::CHANGE_ME:: -->

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `helix_payload` | `text` | No | `-` | - |
| `incident_id` | `number` | Yes | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

<!-- ::CHANGE_ME:: -->
```python
results = {
    'version': '1.0',
    'success': True,
    'reason': None,
    'content': {'closed': [{'values': {
        'Request ID': 'INC000000000917|INC000000000917',
        'Submitter': 'Allen',
        'Submit Date': '2021-04-16T18:27:47.000+0000',
        'Assignee Login ID': 'Mary',
        'Last Modified By': 'Allen',
        'Last Modified Date': '2021-04-16T18:29:53.000+0000',
        'Status': 'Resolved',
        'Status-History': {'New': {'user': 'Allen',
                           'timestamp': '2021-04-16T18:27:47.000+0000'
                           }, 'Assigned': {'user': 'Allen',
                           'timestamp': '2021-04-16T18:27:47.000+0000'
                           }, 'Resolved': {'user': 'Allen',
                           'timestamp': '2021-04-16T18:29:53.000+0000'
                           }},
        'Assignee Groups': "1000000005;'Allen';",
        'InstanceId': 'AGGALAS1CWFC9AQROFY1QQP78CFXL9',
        'Vendor Assignee Groups': None,
        'Vendor Assignee Groups_parent': None,
        'Assignee Groups_parent': '',
        'Product Categorization Tier 1': None,
        'Product Categorization Tier 2': None,
        'Product Categorization Tier 3': None,
        'Department': 'Customer Service',
        'Site Group': 'United States',
        'Region': 'Americas',
        'Product Name': None,
        'Manufacturer': None,
        'Product Model/Version': None,
        'Site': 'Headquarters, Building 1.31',
        'SRAttachment': None,
        'Created_By': None,
        'MaxRetries': None,
        'z1D_Command': None,
        'AccessMode': None,
        'z1D_WorklogDetails': None,
        'z1D_Char02': None,
        'z1D_FormName': None,
        'AppInstanceServer': None,
        'SRInstanceID': 'NA',
        'zTmpEventGUID': None,
        'AppInterfaceForm': None,
        'Entry ID': 'INC000000000917',
        'z1D_Activity_Type': None,
        'z1D_Summary': None,
        'z1D_Details': None,
        'z1D_Secure_Log': None,
        'z1D_View_Access': None,
        'z2AF_Act_Attachment_1': None,
        'Protocol': None,
        'AppLogin': None,
        'AppPassword': None,
        'PortNumber': None,
        'SRMS Registry Instance ID': 'SR0011439CCAD4ec8UQwCkOLAQlQAA',
        'SRMSAOIGuid': None,
        'SRID': None,
        'TemplateID': None,
        'z1D_CommunicationSource': None,
        'z1D_ActivityDate_tab': None,
        'Last _Assigned_Date': None,
        'z1D_AssociationDescription': None,
        'Component_ID': None,
        'mc_ueid': None,
        'cell_name': None,
        'policy_name': None,
        'status_incident': None,
        'status_reason2': None,
        'root_component_id_list': None,
        'root_incident_id_list': None,
        'Impact_OR_Root': None,
        'bOrphanedRoot': None,
        'use_case': None,
        'ClientLocale': None,
        'ServiceCI': None,
        'HPD_CI': None,
        'ServiceCI_ReconID': None,
        'HPD_CI_ReconID': None,
        'z1D_CI_FormName': None,
        'Previous_ServiceCI_ReconID': None,
        'Previous_HPD_CI_ReconID': None,
        'z1D_SR_Instanceid': None,
        'Direct Contact Corporate ID': None,
        'KMSGUID': None,
        'HPD_CI_FormName': None,
        'z1D_InterfaceAction': None,
        'z1D_WorkInfoSubmitter': None,
        'Direct Contact Login ID': None,
        'Customer Login ID': 'Allen',
        'AttachmentSourceFormName': None,
        'AttachmentSourceGUID': None,
        'z1D_ConfirmGroup': None,
        'z1D_CreatedFromBackEndSynchWI': None,
        'InfrastructureEventType': 'None',
        'policy_type': None,
        'Chat Session ID': None,
        'Modified Chat Session ID': None,
        'Auto Open Session': None,
        'TimeOfEvent': None,
        'FirstWIPDate': None,
        'LastWIPDate': None,
        'Broker Vendor Name': None,
        'Description': 'IBM SOAR Case 2169: Investigate Exposure of Personal Information/Data'
            ,
        'Company': 'Calbro Services',
        'Country': 'United States',
        'State Province': 'New York',
        'City': 'New York',
        'Organization': 'Information Technology',
        'Assigned Support Organization': 'IT Support',
        'Last Name': 'Allbrook',
        'First Name': 'Allen',
        'Middle Initial': None,
        'Contact Client Type': 'Office-Based Employee',
        'VIP': 'No',
        'Contact Sensitivity': 'Standard',
        'Desk Location': None,
        'Mail Station': None,
        'Street': '1114 Eighth Avenue, 31st Floor',
        'Zip/Postal Code': '10036',
        'Internet E-mail': 'A.Allbrook@calbroservices.com',
        'Corporate ID': None,
        'Phone Number': '1 212 555-5454 (11)',
        'z1D Char01': None,
        'Categorization Tier 1': None,
        'Categorization Tier 2': None,
        'Categorization Tier 3': None,
        'z1D Char02': None,
        'Site ID': 'STE_SOLN0002846',
        'z1D Action': None,
        'Assigned Group ID': 'SGP000000000011',
        'Person ID': 'PPL000000000013',
        'Contact Company': 'Calbro Services',
        'Service Type': 'User Service Restoration',
        'Status_Reason': 'No Further Action Required',
        'Detailed Decription': None,
        'Resolution': 'Closed from IBM SOAR',
        'Incident Number': 'INC000000000816',
        'Urgency': '1-Critical',
        'Impact': '1-Extensive/Widespread',
        'Priority': 'Critical',
        'Priority Weight': 29,
        'Reported Source': 'Direct Input',
        'Assigned Group': 'Service Desk',
        'Assignee': 'Mary Mann',
        'Assigned Support Company': 'Calbro Services',
        'Assigned Group Shift Name': None,
        'Assigned Group Shift ID': None,
        'Owner Support Organization': 'IT Support',
        'Number of Attachments': None,
        'Vendor Name': None,
        'Owner Group': 'Service Desk',
        'Owner Support Company': 'Calbro Services',
        'Owner Group ID': 'SGP000000000011',
        'Reported Date': '2021-04-16T18:27:47.000+0000',
        'Responded Date': '2021-04-16T18:27:47.000+0000',
        'Last Acknowledged Date': None,
        'Last Resolved Date': '2021-04-16T18:29:53.000+0000',
        'Closed Date': None,
        'Vendor Ticket Number': None,
        'z1D Permission Group ID': None,
        'z1D Permission Group List': None,
        'Resolution Category': None,
        'Direct Contact Internet E-mail': None,
        'Vendor Organization': None,
        'Vendor Group': None,
        'Vendor Group ID': None,
        'Total Transfers': 1,
        'Resolution Method': None,
        'Resolution Category Tier 2': None,
        'Resolution Category Tier 3': None,
        'Closure Product Category Tier1': None,
        'Closure Product Category Tier2': None,
        'Closure Product Category Tier3': None,
        'Closure Product Name': None,
        'Closure Product Model/Version': None,
        'Closure Manufacturer': None,
        'Estimated Resolution Date': None,
        'Required Resolution DateTime': None,
        'Direct Contact Company': None,
        'Direct Contact Last Name': None,
        'Direct Contact First Name': None,
        'Direct Contact Middle Initial': None,
        'Direct Contact Phone Number': None,
        'Direct Contact Organization': None,
        'Direct Contact Department': None,
        'Direct Contact Region': None,
        'Direct Contact Site Group': None,
        'Direct Contact Site': None,
        'Direct Contact Person ID': None,
        'Direct Contact Street': None,
        'Direct Contact Country': None,
        'Direct Contact State/Province': None,
        'Direct Contact City': None,
        'Direct Contact Zip/Postal Code': None,
        'Direct Contact Time Zone': None,
        'Direct Contact Desk Location': None,
        'Direct Contact Mail Station': None,
        'Direct Contact Location Details': None,
        'Direct Contact Site ID': None,
        'Direct Contact Country Code': None,
        'Direct Contact Area Code': None,
        'Direct Contact Local Number': None,
        'Direct Contact Extension': None,
        },
            '_links': {'self': [{'href': 'https://1.1.1.1:8008/api/arsys/v1/entry/HPD:IncidentInterface/INC000000000917%7CINC000000000917'
                       }]}}], 'skipped': []},
    'raw': '{"closed": [{"values": {"Request ID": "INC000000000917|INC000000000917", "Submitter": "Allen", "Submit Date": "2021-04-16T18:27:47.000+0000", "Assignee Login ID": "Mary", "Last Modified By": "Allen", "Last Modified Date": "2021-04-16T18:29:53.000+0000", "Status": "Resolved", "Status-History": {"New": {"user": "Allen", "timestamp": "2021-04-16T18:27:47.000+0000"}, "Assigned": {"user": "Allen", "timestamp": "2021-04-16T18:27:47.000+0000"}, "Resolved": {"user": "Allen", "timestamp": "2021-04-16T18:29:53.000+0000"}}, "Assignee Groups": "1000000005;\'Allen\';", "InstanceId": "AGGALAS1CWFC9AQROFY1QQP78CFXL9", "Vendor Assignee Groups": null, "Vendor Assignee Groups_parent": null, "Assignee Groups_parent": "", "Product Categorization Tier 1": null, "Product Categorization Tier 2": null, "Product Categorization Tier 3": null, "Department": "Customer Service", "Site Group": "United States", "Region": "Americas", "Product Name": null, "Manufacturer": null, "Product Model/Version": null, "Site": "Headquarters, Building 1.31", "SRAttachment": null, "Created_By": null, "MaxRetries": null, "z1D_Command": null, "AccessMode": null, "z1D_WorklogDetails": null, "z1D_Char02": null, "z1D_FormName": null, "AppInstanceServer": null, "SRInstanceID": "NA", "zTmpEventGUID": null, "AppInterfaceForm": null, "Entry ID": "INC000000000917", "z1D_Activity_Type": null, "z1D_Summary": null, "z1D_Details": null, "z1D_Secure_Log": null, "z1D_View_Access": null, "z2AF_Act_Attachment_1": null, "Protocol": null, "AppLogin": null, "AppPassword": null, "PortNumber": null, "SRMS Registry Instance ID": "SR0011439CCAD4ec8UQwCkOLAQlQAA", "SRMSAOIGuid": null, "SRID": null, "TemplateID": null, "z1D_CommunicationSource": null, "z1D_ActivityDate_tab": null, "Last _Assigned_Date": null, "z1D_AssociationDescription": null, "Component_ID": null, "mc_ueid": null, "cell_name": null, "policy_name": null, "status_incident": null, "status_reason2": null, "root_component_id_list": null, "root_incident_id_list": null, "Impact_OR_Root": null, "bOrphanedRoot": null, "use_case": null, "ClientLocale": null, "ServiceCI": null, "HPD_CI": null, "ServiceCI_ReconID": null, "HPD_CI_ReconID": null, "z1D_CI_FormName": null, "Previous_ServiceCI_ReconID": null, "Previous_HPD_CI_ReconID": null, "z1D_SR_Instanceid": null, "Direct Contact Corporate ID": null, "KMSGUID": null, "HPD_CI_FormName": null, "z1D_InterfaceAction": null, "z1D_WorkInfoSubmitter": null, "Direct Contact Login ID": null, "Customer Login ID": "Allen", "AttachmentSourceFormName": null, "AttachmentSourceGUID": null, "z1D_ConfirmGroup": null, "z1D_CreatedFromBackEndSynchWI": null, "InfrastructureEventType": "None", "policy_type": null, "Chat Session ID": null, "Modified Chat Session ID": null, "Auto Open Session": null, "TimeOfEvent": null, "FirstWIPDate": null, "LastWIPDate": null, "Broker Vendor Name": null, "Description": "IBM SOAR Case 2169: Investigate Exposure of Personal Information/Data", "Company": "Calbro Services", "Country": "United States", "State Province": "New York", "City": "New York", "Organization": "Information Technology", "Assigned Support Organization": "IT Support", "Last Name": "Allbrook", "First Name": "Allen", "Middle Initial": null, "Contact Client Type": "Office-Based Employee", "VIP": "No", "Contact Sensitivity": "Standard", "Desk Location": null, "Mail Station": null, "Street": "1114 Eighth Avenue, 31st Floor", "Zip/Postal Code": "10036", "Internet E-mail": "A.Allbrook@calbroservices.com", "Corporate ID": null, "Phone Number": "1 212 555-5454 (11)", "z1D Char01": null, "Categorization Tier 1": null, "Categorization Tier 2": null, "Categorization Tier 3": null, "z1D Char02": null, "Site ID": "STE_SOLN0002846", "z1D Action": null, "Assigned Group ID": "SGP000000000011", "Person ID": "PPL000000000013", "Contact Company": "Calbro Services", "Service Type": "User Service Restoration", "Status_Reason": "No Further Action Required", "Detailed Decription": null, "Resolution": "Closed from IBM SOAR", "Incident Number": "INC000000000816", "Urgency": "1-Critical", "Impact": "1-Extensive/Widespread", "Priority": "Critical", "Priority Weight": 29, "Reported Source": "Direct Input", "Assigned Group": "Service Desk", "Assignee": "Mary Mann", "Assigned Support Company": "Calbro Services", "Assigned Group Shift Name": null, "Assigned Group Shift ID": null, "Owner Support Organization": "IT Support", "Number of Attachments": null, "Vendor Name": null, "Owner Group": "Service Desk", "Owner Support Company": "Calbro Services", "Owner Group ID": "SGP000000000011", "Reported Date": "2021-04-16T18:27:47.000+0000", "Responded Date": "2021-04-16T18:27:47.000+0000", "Last Acknowledged Date": null, "Last Resolved Date": "2021-04-16T18:29:53.000+0000", "Closed Date": null, "Vendor Ticket Number": null, "z1D Permission Group ID": null, "z1D Permission Group List": null, "Resolution Category": null, "Direct Contact Internet E-mail": null, "Vendor Organization": null, "Vendor Group": null, "Vendor Group ID": null, "Total Transfers": 1, "Resolution Method": null, "Resolution Category Tier 2": null, "Resolution Category Tier 3": null, "Closure Product Category Tier1": null, "Closure Product Category Tier2": null, "Closure Product Category Tier3": null, "Closure Product Name": null, "Closure Product Model/Version": null, "Closure Manufacturer": null, "Estimated Resolution Date": null, "Required Resolution DateTime": null, "Direct Contact Company": null, "Direct Contact Last Name": null, "Direct Contact First Name": null, "Direct Contact Middle Initial": null, "Direct Contact Phone Number": null, "Direct Contact Organization": null, "Direct Contact Department": null, "Direct Contact Region": null, "Direct Contact Site Group": null, "Direct Contact Site": null, "Direct Contact Person ID": null, "Direct Contact Street": null, "Direct Contact Country": null, "Direct Contact State/Province": null, "Direct Contact City": null, "Direct Contact Zip/Postal Code": null, "Direct Contact Time Zone": null, "Direct Contact Desk Location": null, "Direct Contact Mail Station": null, "Direct Contact Location Details": null, "Direct Contact Site ID": null, "Direct Contact Country Code": null, "Direct Contact Area Code": null, "Direct Contact Local Number": null, "Direct Contact Extension": null}, "_links": {"self": [{"href": "https://1.1.1.1:8008/api/arsys/v1/entry/HPD:IncidentInterface/INC000000000917%7CINC000000000917"}]}}], "skipped": []}',
    'inputs': {'incident_id': 2169,
               'helix_payload': {'format': 'text',
               'content': '{"Status_Reason": "foo"}'}, 'task_id': 380},
    'metrics': {
        'version': '1.0',
        'package': 'fn-bmc-helix',
        'package_version': '0.0.0',
        'host': 'local',
        'execution_time_ms': 2443,
        'timestamp': '2021-04-16 14:29:08',
        },
    }
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
# Python 2 compatibility for CP4S 1.6
def mk_str(value, quotes=u'"'):
    if value is None:
        return "null"
    else:
        esc_value = value.replace(u'"', u'\\"')
        if quotes:
            return u'{0}{1}{0}'.format(quotes, esc_value)
        else:
            return esc_value

inputs.task_id = task.id
inputs.incident_id = incident.id

# Use this section to add key, value pairs to send to BMC Helix
# These values will be added/updated on the target BMC Helix incident,
# so they must conform with the "HPD:IncidentInterface_Create" schema
payload = """{"Status_Reason": "foo"}"""

inputs.helix_payload = payload if payload else ''

```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
noteText = "<h5>BMC Helix Close Incident:</h5>"

if results["success"]:
    if results["content"]["closed"]:
      noteText += "<p>The following incidents were matched in BMC Helix and successfully closed:</p>"
      for item in results["content"]["closed"]:
        noteText += "<p>    Incident Number {0}, Request ID: {1}</p>".format(item["values"]["Incident Number"], item["values"]["Request ID"])
    if results["content"]["skipped"]:
      noteText += "<p>The following incidents were not able to be closed. Common reasons include that the incident has been previously closed, " \
      "the incident has been deleted, or the payload sent to Helix was incomplete according to the requirements of your specific system:</p>"
      for item in results["content"]["skipped"]:
        noteText += "<p>    Incident Number {0}, Request ID: {1}</p>".format(item["values"]["Incident Number"], item["values"]["Request ID"])
elif not results["content"]["closed"] and not results["content"]["skipped"]:
  # no sync to helix, just exit
  noteText = None
else:
  noteText += "<p>Function failed to complete. Reason: {}</p>".format(results.reason)

if noteText:
  richText = helper.createRichText(noteText)
  incident.addNote(richText)

```

</p>
</details>

---
## Function - Helix: Create Incident
Create a new incident in BMC Helix from a SOAR task.

 ![screenshot: fn-helix-create-incident ](./doc/screenshots/fn-helix-create-incident.png)

### Activity Fields

 ![screenshot: fn-helix-create-incident-activity-fields ](./doc/screenshots/fn-helix-create-incident-activity-fields.png)

BMC Helix is a highly customizable product, and this integration was designed with those customizations in mind.

Note that when creating an incident in BMC Helix via the REST API, any auto-routing that is configured in the BMC Helix platform will continue to apply as it would when creating
a new incident in the user interface. This can result in a discrepancy between the data that was submitted by the integration and the data that is present in BMC Helix once the incident object is actually created.
For example, the payload sent to BMC Helix by the integration could indicate a Status of New for an incident (either directly or via a [template](#templating).) However, when that ticket is actually
created, the auto-routing in BMC Helix could be configured to assign it to a user and update the Status to Assigned. This is expected, and the true status of the created incident
will be reflected in the [datatable](#data-table---helix-Linked-incidents-reference-table).

**Templating**

To facilitate the use of templates, none of the activity fields are required. If your BMC Helix server has a template defined that provides all required fields to create an incident, you may simply provided the template name and use this function. Note that it is necessary to manually enter the template name(s) so that they are available in the dropdown. We have provided a stock, out-of-the-box template name as an example. Other template names can be added as necessary by modifying this activity field within the Customization Settings of the platform.

**Other Common Fields**

For convenience, several activity fields have been created to handle input for commonly used fields in BMC Helix such as Status, Impact, and Urgency. These activity fields are not required, as templates can also provide those values. Note that if a template and activity field provide the same value, the activity field will take precedence over the template.

Please note that the user has the ability to customize what values appear in the dropdown menu for each activity field. This action will likely be necessary if not taking advantage of the BMC Helix's templating functionality via this integration. Activity fields can be modified within the Customization Settings of the platform.

**Additional Data**

Finally, the Additional Data activity field allows the mapping of any other values to the BMC Helix form not covered in the above activity fields, including custom defined fields. The fields must be provided as a Python-like dictionary. For example:

```python
{"Short Description": "example incident text", "my_custom_field": 1}
```

The keys provided in this dictionary string must match the API names of fields in the `HPD:IncidentInterface` form. To retrieve the schema for this form on the BMC Helix server, send an HTTPS OPTIONS request to `https://serverName/api/arsys/v1/entry/HPD:IncidentInterface_Create`. This is the endpoint used to create BMC Helix incidents over the API, and thus the response will indicate which fields are available to map and any value restrictions.

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `helix_incident_name` | `text` | No | `-` | - |
| `helix_payload` | `text` | No | `-` | - |
| `incident_id` | `number` | Yes | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

<!-- ::CHANGE_ME:: -->
```python
results = {
    # TODO: Generate an example of the Function Output within this code block.
    # To get the output of a Function:
    #   1. Run resilient-circuits in DEBUG mode: $ resilient-circuits run --loglevel=DEBUG
    #   2. Invoke the Function in SOAR
    #   3. Gather the results using: $ resilient-sdk codegen -p fn_bmc_helix --gather-results
    #   4. Run docgen again: $ resilient-sdk docgen -p fn_bmc_helix
} 
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
# Python 2 compatibility for CP4S 1.6
def mk_str(value, quotes=u'"'):
    if value is None:
        return "null"
    else:
        esc_value = value.replace(u'"', u'\\"')
        if quotes:
            return u'{0}{1}{0}'.format(quotes, esc_value)
        else:
            return esc_value


payload = u"""{{ "ApplyTemplate": {},
  "First_Name": {},
  "Last_Name": {},
  "Impact": {},
  "Urgency": {},
  "Service_Type": {},
  "Status": {},
  "Reported Source": {},
  "Description": {},
  "Assigned Support Organization": {},
  "additional_data": {}
}}""".format(mk_str(rule.properties.helix_template),
  mk_str(rule.properties.helix_first_name),
  mk_str(rule.properties.helix_last_name),
  mk_str(rule.properties.helix_impact),
  mk_str(rule.properties.helix_urgency),
  mk_str(rule.properties.helix_service_type),
  mk_str(rule.properties.helix_status),
  mk_str(rule.properties.helix_reported_source),
  mk_str(rule.properties.helix_note),
  mk_str(rule.properties.helix_support_group),
  rule.properties.helix_additional_data.content if rule.properties.helix_additional_data.content else "null"
)

# set inputs
inputs.task_id = task.id 
inputs.incident_id = incident.id
inputs.helix_incident_name = task.name
inputs.helix_payload = payload

```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
noteText = "<h5> Helix Create Incident</h5>"

task_id = task.id
task_name = task.name

if results["success"]:
  noteText += "<p>Successfully sent task {0} \"{1}\" to Helix as Incident Number {2} (UI name) and Request ID {3} (API name).</p>"\
  "".format(task_id, task_name, \
  results["content"]["values"]["Incident Number"], results["content"]["values"]["Request ID"])
else:
  noteText += "<p>Unable to send task {0} \"{1}\" to Helix</p>".format(task_id, task_name)
  noteText += "<p>Ensure the activity fields and payload you provide meet the minimum requirements in your system for incident creation and routing."

richText = helper.createRichText(noteText)
incident.addNote(richText)
```

</p>
</details>

---


## Data Table - Helix Linked Incidents Reference Table

 ![screenshot: dt-helix-linked-incidents-reference-table](./doc/screenshots/dt-helix-linked-incidents-reference-table.png) <!-- ::CHANGE_ME:: -->

#### API Name:
helix_linked_incidents_reference_table

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Extra | `extra` | `textarea` | - |
| Helix ID | `helix_id` | `text` | Request ID of the Helix form entry |
| Status | `status` | `textarea` | Last status applied to the Helix Incident |
| Task ID | `taskincident_id` | `text` | ID of the Task and its description |
| Timestamp | `timestamp` | `datetimepicker` | - |

---

### Data explanation
The BMC Helix Linked Incidents Reference Table will be updated when either the `Helix: Create Incident` or `Helix: Close Incident`
function completes.

#### Helix: Create Incident
Once an incident is posted to BMC Helix, the auto-routing feature has the potential to further alter the values of some of the fields within the BMC Helix incident 
(see [Activity Fields](#activity-fields) for more information on this). Due to this potential, the integration will fetch the incident back from the 
BMC Helix server after it has been created to ensure the datatable is updated with accurate information. Once the incident data is received from BMC Helix, relevant
fields are recorded in the datatable.

One item to note is the difference between the `Helix ID` and `Extra` columns. As noted in [columns](#columns), above, both of these columns contain some sort of ID
value relevant to the BMC Helix Incident.

The `Helix ID` column contains the "Request ID" of the form entry. Often, this value is of the form `INCxxxxxxx|INCxxxxxxx`.
Although this notation may appear to be two numbers separated by the `|` character, the entire string together is a single Request ID value.
This ID is used to refer to the incident over the API.

The `Extra` columns contains the "Incident Number" of the form entry. Often this value is of the form `INCxxxxx`, but will likely not look like either component of
the Request ID. This Incident Number is the ID that appears in the UI for the incident inside the Incident Management Console.

#### Helix: Close Incident
Once an Incident is Closed in BMC Helix, the datatable will be updated with the new status of that incident.


## Rules
| Rule Name | Object | Workflow Triggered |
| --------- | ------ | ------------------ |
| Helix Close Incident from Task | task | `close_a_helix_incident_from_task` |
| Helix Create Incident from Task | task | `create_a_helix_incident_from_task` |

---


## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.

### For Support
This is an IBM supported app. Please search [ibm.com/mysupport](https://ibm.com/mysupport) for assistance.
