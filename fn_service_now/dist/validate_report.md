

# Validation Report for ServiceNow Functions for IBM Resilient

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 43.1.2616 | 2022/01/14 14:23:42 | `cmd`: validate, `settings`: /Users/bobleckel/.resilient/.sdk_settings.json, `package`: ., `validate`: True |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | ServiceNow Functions for IBM Resilient |
| `name` | fn_service_now |
| `version` | 2.0.0 |
| `author` | IBM Resilient |
| `install_requires` | ['resilient_circuits>=43.0.0', 'beautifulsoup4>=4.6.3'] |
| `description` | Bi-directional synchronization of Incidents, Tasks, Notes and Attachments with ServiceNow |
| `long_description` | - Create an IBM Resilient Incident/Task from a ServiceNow Record in the Incident Table.<br>        - Create a ServiceNow Record in the Incident Table from an IBM Resilient Incident/Task.<br>        - Sync notes between a related IBM Resilient Incident/Task and a ServiceNow Record.<br>        - Send Attachments from an IBM Resilient Incident/Task to a related ServiceNow Record. |
| `url` | https://ibm.com/mysupport |
| `entry_points` | {'resilient.circuits.configsection': '/Users/bobleckel/soar/story/INT-4200/servicenow_close_from_soar/fn_service_now/fn_service_now/util/config.py',<br> 'resilient.circuits.customize': '/Users/bobleckel/soar/story/INT-4200/servicenow_close_from_soar/fn_service_now/fn_service_now/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/bobleckel/soar/story/INT-4200/servicenow_close_from_soar/fn_service_now/fn_service_now/util/selftest.py'} |
| `SOAR version` | 41.2.41 |
| `Proxy support` | Proxies supported if running on AppHost>=1.6 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |

<span style="color:green">Success</span>


---


## Package files validation

### `MANIFEST.in`
<span style="color:orange">WARNING</span>: `MANIFEST.in` is missing the following lines: [`include doc/*.md`, `include doc/screenshots/*`]

`MANIFEST.in` file is the list of files to be included during packaging. Be sure it is up to date


### LICENSE
<span style="color:teal">INFO</span>: `LICENSE` file is valid

It is recommended to manually validate the license. Suggested formats: MIT, Apache, and BSD


### `apikey_permissions.txt`
<span style="color:green">Pass</span>


### `Dockerfile`
<span style="color:green">Pass</span>


### `entrypoint.sh`
<span style="color:green">Pass</span>


### ``config.py``
<span style="color:green">Pass</span>


### ``customize.py``
<span style="color:green">Pass</span>


### `README.md`
<span style="color:green">Pass</span>


### `app_logo.png`
<span style="color:green">Pass</span>


### `company_logo.png`
<span style="color:green">Pass</span>


### LICENSE
<span style="color:green">Pass</span>

 
---
 

## Payload samples validation

### `payload_samples/fn_snow_helper_add_task_note`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `fn_snow_helper_add_task_note` empty

Fill in values manually or by using ```resilient-sdk codegen -p /Users/bobleckel/soar/story/INT-4200/servicenow_close_from_soar/fn_service_now --gather-samples```


### `payload_samples/fn_snow_helper_update_datatable`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `fn_snow_helper_update_datatable` empty

Fill in values manually or by using ```resilient-sdk codegen -p /Users/bobleckel/soar/story/INT-4200/servicenow_close_from_soar/fn_service_now --gather-samples```


### `payload_samples/fn_snow_add_attachment_to_record`
<span style="color:green">Pass</span>


### `payload_samples/fn_snow_add_note_to_record`
<span style="color:green">Pass</span>


### `payload_samples/fn_snow_close_record`
<span style="color:green">Pass</span>


### `payload_samples/fn_snow_create_record`
<span style="color:green">Pass</span>


### `payload_samples/fn_snow_lookup_sysid`
<span style="color:green">Pass</span>


### `payload_samples/fn_snow_update_record`
<span style="color:green">Pass</span>

 
---
 

 

 

 

 