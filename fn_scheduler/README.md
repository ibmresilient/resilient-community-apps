# Scheduler

## Table of Contents
- [Scheduler](#scheduler)
  - [Table of Contents](#table-of-contents)
  - [Release Notes](#release-notes)
    - [Migrating to v1.0.2](#migrating-to-v102)
    - [Notes regarding v2.1.0](#notes-regarding-v210)
  - [Overview](#overview)
  - [Requirements](#requirements)
    - [SOAR platform](#soar-platform)
    - [Cloud Pak for Security](#cloud-pak-for-security)
    - [Proxy Server](#proxy-server)
    - [Python Environment](#python-environment)
  - [Installation](#installation)
    - [Install](#install)
    - [App Configuration](#app-configuration)
    - [Custom Layouts](#custom-layouts)
    - [Supported Scheduled Rules/Playbooks](#supported-scheduled-rulesplaybooks)
  - [Function - Scheduled Rule Create](#function---scheduled-rule-create)
  - [Function - Scheduled Rule Modify](#function---scheduled-rule-modify)
  - [Function - Scheduled Rule List](#function---scheduled-rule-list)
  - [Function - Scheduled Rule Pause](#function---scheduled-rule-pause)
  - [Function - Scheduled Rule Remove](#function---scheduled-rule-remove)
  - [Function - Scheduled Rule Resume](#function---scheduled-rule-resume)
  - [Function - Run Scheduled Job Now](#function---run-scheduled-job-now)
  - [Data Table - Scheduler Rules](#data-table---scheduler-rules)
      - [API Name:](#api-name)
      - [Columns:](#columns)
  - [Playbooks API](#playbooks-api)
  - [Considerations](#considerations)
    - [Playbooks and Rules](#playbooks-and-rules)
    - [Artifacts](#artifacts)
    - [Datatables](#datatables)
    - [Persistence of Scheduled Playbooks/Rules](#persistence-of-scheduled-playbooksrules)
    - [Integrations](#integrations)
  - [Troubleshooting \& Support](#troubleshooting--support)
    - [For Support](#for-support)
---

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release
  notes of a previous release
-->
| Version | Date | Notes |
| ------- | ---- | ----- |
| 2.1.0   | Apr. 2023 | Migrated all workflows to playbooks |
| 2.0.0   | May  2022 | Support for Playbooks. Added support for Datatables |
| 1.1.2   | Feb. 2022 | Use ``APScheduler < 3.9`` if ``Python Version < 3.6`` |
| 1.1.1   | Aug. 2021 | remove SOAR credentials from saved rules in db |
| 1.1.0   | Apr. 2021 | app.config setting for optional note creation |
| 1.0.3   | Oct. 2020 | Conditional PostgreSQL dependency |
| 1.0.2   | Sept. 2020 | PostgreSQL support |
| 1.0.1   | May 2020 | App Host support |
| 1.0.0   | Nov. 2019 | Initial Release |

### Migrating to v1.0.2
When migrating to v1.0.2 from a previous release, add the following setting to your `[fn_scheduler]` app.config section:

```
# db url if using a postgreSQL DB. Use this with AppHost
# db_url=postgresql://username:password@host:port/database (or) db_url=postgresql+pypostgresql://username:password@host:port/database

```
Use this setting rather than the SQLite `datastore_dir` setting to persist the scheduler DB in PostgreSQL.
This is necessary in an App Host environment to retain your schedules outside the app container.

### Notes regarding v2.1.0

In v2.1, the existing rules and workflows have been replaced with playbooks.
This change is made to support the ongoing, newer capabilities of playbooks.
Each playbook has the same functionality as the previous, corresponding rule/workflow. 

If upgrading from a previous release, you'll notice that the previous release's rules/workflows remain in place. Both sets of rules and playbooks are active. For manual actions, playbooks have the same name as it's corresponding rule, but with "(PB)" added at the end.

You can continue to use the rules/workflows. 
But migrating to playbooks provides greater functionality along with future app enhancements and bug fixes. 


| SOAR Version | Capability |
| ------------ | ---------- |
| V46.0 | All scheduler Workflows and Rules have been recreated in Playbooks |

---

## Overview
<!--
  Provide a high-level description of the function itself and its remote software or application.
  The text below is parsed from the "description" and "long_description" attributes in the setup.py file
-->
**Functions to allow Playbooks/Rules to be scheduled**

This package of functions allows an enterprise to schedule a rule to run in the future associated with a incident, task, artifact, and datatable. Times to run can be specified in the following ways:

1) cron (ex. * 0 * * * for every night at midnight). For more information about cron entry syntax, see [Wikipedia](https://en.wikipedia.org/wiki/Cron)
2) interval (ex. `30s` for every 30 seconds, `10m` for every 10 minutes, `5h` for every 5 hours, `1d` for once daily)
3) date (ex. 2022/4/23 12:00:00 or 2022-4-23 12:00:00)
4) delta (ex. `30s` for 30 seconds in the future, `10m` for 10 minutes in the future, etc.)

Schedule Playbooks/Rules using `cron` and `interval` are reoccurring whereas `date` and `delta` are single event schedules. Scheduled Playbooks/Rules are persisted so that restarts of resilient-circuits will resume already scheduled Playbooks/Rules.

Functions available include:

1) Scheduling a Playbook/Rule
2) Listing scheduled Playbooks/Rules
3) Pause and resume scheduled Playbooks/Rules
5) Removing a scheduled Playbook/Rule


 ![screenshot: playbooks_support ](./doc/screenshots/main.png)

---

## Requirements
<!--
  List any Requirements
-->
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, App Host and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `46.0`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `46.0`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient_circuits>=42.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions:
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read |
  | Function | Read |

The following SOAR platform guides provide additional information:
* _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _Integration Server Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _System Administrator Guide_: provides the procedure to install, configure and deploy apps.

The above guides are available on the IBM Documentation website at [ibm.biz/soar-docs](https://ibm.biz/soar-docs). On this web page, select your SOAR platform version. On the follow-on page, you can find the _App Host Deployment Guide_ or _Integration Server Guide_ by expanding **Apps** in the Table of Contents pane. The System Administrator Guide is available by expanding **System Administrator**.

### Cloud Pak for Security
If you are deploying to IBM Cloud Pak for Security, the requirements are:
* IBM Cloud Pak for Security >= `1.10`.
* Cloud Pak is configured with an App Host.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

The following Cloud Pak guides provide additional information:
* _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. From the Table of Contents, select Case Management and Orchestration & Automation > **Orchestration and Automation Apps**.
* _System Administrator Guide_: provides information to install, configure, and deploy apps. From the IBM Cloud Pak for Security IBM Documentation table of contents, select Case Management and Orchestration & Automation > **System administrator**.

These guides are available on the IBM Documentation website at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs). From this web page, select your IBM Cloud Pak for Security version. From the version-specific IBM Documentation page, select Case Management and Orchestration & Automation.

### Proxy Server
The app **does** support a proxy server.

### Python Environment
Both Python 3.6 and Python 3.9 are supported.
Additional package dependencies may exist for each of these packages:
* APScheduler >= 3.9;python_version >= '3.6'
* python-dateutil>=2.8.1
* pytz
* resilient_circuits>=46.0
* resilient_lib>=46.0
* SQLAlchemy>=1.3.8

---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **timezone** | Yes | `utc` | *Specify the timezone (ex. America/New_York) which scheduled Playbooks/rules should follow.* |
| **thread_max** | Yes | `20` | *Number of threads which can run at the same. Typically, triggered Playbooks/rules run for a very short time to kick off a IBM SOAR rule.* |
| **datastore_dir** | No | `/path/to/sqlite_folder` | *Specify a data path for the sqlite persistent datafile (ex. /path/to/scheduler.sqlite)* |
| **db_url** | No | postgresql+pypostgresql://res_test:res_test@192.168.1.215:5432/res_test | *Specify a PostgreSQL db to retain the schedules. Uncomment and remove the setting datastore_dir.* |
| disable_notes | No | True|False | Set to True to disable creating a note when a rule is triggered. Default is False |


### Custom Layouts
<!--
  Use this section to provide guidance on where the user should add any custom fields and data tables.
  You may wish to recommend a new incident tab.
  You should save a screenshot "custom_layouts.png" in the doc/screenshots directory and reference it here
-->
A datatable is used to display scheduled Playbooks/Rules and to take actions such as pause, resume and remove a scheduled job. This datatable can be added to your incident layout by adding a new tab and by dragging the `Scheduler Rules` datatable to the new tab. Remember to save the layout change.

---

### Supported Scheduled Rules/Playbooks
Scheduled Playbooks/Rules are possible for:
* incidents
* artifacts
* tasks
* attachments (not pre-packaged)
* datatables (not pre_packaged)

When creating a rule to schedule for an attachment, set the following field in the pre-processing script:
```python
inputs.object_id = attachment.id
```

When creating a rule to schedule for a given datatable, the pre-processing script will look like this (assuming you're using rule activity fields)

```python
inputs.scheduler_type = getattr(playbook.inputs, "schedule_type", "cron")

if getattr(playbook.inputs, "schedule_type", "cron") == "date":
  # date format converted to use dashes
  inputs.scheduler_type_value = getattr(playbook.inputs, "schedule_type_value", "").replace("/", "-")
else:
  inputs.scheduler_type_value = getattr(playbook.inputs, "schedule_type_value", "")

inputs.scheduler_rule_name = getattr(playbook.inputs, "schedule_rule_name", None)
inputs.scheduler_rule_parameters = getattr(playbook.inputs, "schedule_rule_parameters", None)
inputs.scheduler_label_prefix = getattr(playbook.inputs, "schedule_label_prefix", None)
inputs.incident_id = incident.id
inputs.scheduler_is_playbook = getattr(playbook.inputs, "schedule_is_playbook", False)

```

## Function - Scheduled Rule Create
Schedule a rule or playbook to run on a schedule. This rule/playbook will be executed for a given incident, artifact, task, etc.

 ![screenshot: fn-scheduled-rule-create ](./doc/screenshots/create_scheduled_job.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | Yes | `-` | Incident Id where the rule will be executed |
| `object_id` | `number` | No | `-` | ID for task, artifact, attachment, etc. |
| `row_id` | `number` | No | `-` | row information for datatable rules |
| `scheduler_label_prefix` | `text` | Yes | `-` | Label to recall the created schedule. The incident id is appended to the name for uniqueness |
| `scheduler_rule_name` | `text` | Yes | `-` | Name of rule/playbook to schedule |
| `scheduler_rule_parameters` | `text` | No | `-` | Optional parameters for the rule/playbook in field=value format separated by semicolons. These fields should match the api name for the rule's activity or playbook's activation input fields. Ex: `rule_activity_field1=value1;rule_activity_field2=value2` |
| `scheduler_type` | `select` | Yes | `-` | type of schedule to create. cron, date, delta, or interval |
| `scheduler_type_value` | `text` | Yes | `-` | interval, date (yyyy-mm-dd hh:mm:ss) or cron value |
| `scheduler_is_playbook` | boolean | Yes | Yes | Yes if scheduling a playbook, No for a rule |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

```python
results = {
  'success': True,
  'content': {
    'args': (2219, # incident_id
    None, # object_id
    None, # row_id
    u'rule3', # Rule to execute
    u'Delete rule3', # Scheduled rule Label
    49, # rule_id
    0, # object_type_id
    None,
    None),
    'executor': 'default',
    'max_instances': 1,
    'func': 'fn_scheduler.components.create_a_scheduled_rule:triggered_job',
    'id': u'rule3',
    'next_run_time': 'Oct 03 2019 12:35PM',
    'name': 'triggered_job',
    'misfire_grace_time': 1,
    'trigger': None,
    'coalesce': False,
    'version': 1,
    'kwargs': {

    }
  }
}
```

</p>
</details>

<details><summary>Example Script: Function Pre-Process</summary>
<p>

```python
inputs.scheduler_type = getattr(playbook.inputs, "schedule_type", "cron")

if getattr(playbook.inputs, "schedule_type", "cron") == "date":
  # date format converted to use dashes
  inputs.scheduler_type_value = getattr(playbook.inputs, "schedule_type_value", "").replace("/", "-")
else:
  inputs.scheduler_type_value = getattr(playbook.inputs, "schedule_type_value", "")

inputs.scheduler_rule_name = getattr(playbook.inputs, "schedule_rule_name", None)
inputs.scheduler_rule_parameters = getattr(playbook.inputs, "schedule_rule_parameters", None)
inputs.scheduler_label_prefix = getattr(playbook.inputs, "schedule_label_prefix", None)
inputs.incident_id = incident.id
inputs.scheduler_is_playbook = getattr(playbook.inputs, "schedule_is_playbook", False)

```

</p>
</details>

<details><summary>Example Script: Write scheduled job to DataTable </summary>
<p>

```python
from datetime import datetime

results = playbook.functions.results.output_scheduled_rule_create
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # '2023-03-24 11:28:34'
TYPE_LOOKUP = {
  0: 'Incident',
  1: "Task",
  4: "Artifact",
  5: "Attachment"}

if results.get("success"):
  job = results.get("content")
  row = incident.addRow("scheduler_rules")
  row['reported_on'] = now
  row['schedule_label'] = job['id']
  row['schedule_type'] = job['type']
  row['incident_id'] = job['args'][0]
  row['schedule'] = job['value']
  row['status'] = 'Active'
  row['next_run_time'] = job['next_run_time']
  row['rule_type'] = TYPE_LOOKUP.get(job['args'][6], "Datatable")
  if job['args'][8]:
    row['rule'] = "<a href='#playbooks/designer/{}'>{}</a>".format(job['args'][5], job['args'][4])
  else:
    row['rule'] = "<a href='#customize?tab=actions&id={}'>{}</a>".format(job['args'][5], job['args'][4])
else:
  incident.addNote("Schedule a Rule/Playbook failed: {}".format(result.get("reason")))
```

</p>
</details>

---
## Function - Scheduled Rule Modify
Modify a Scheduled job associated with a rule or playbook. Settings which can be modified include the trigger criteria (cron, delta, date or interval) and the parameters passed to the rule or playbook.

 ![screenshot: modify_scheduled_job ](./doc/screenshots/modify_scheduled_job.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `scheduler_label_prefix` | `text` | Yes | `-` | Label to recall the created schedule.  |
| `modify_scheduler_type` | `select` | No | `-` | type of schedule to create. cron, date, delta, or interval |
| `modify_scheduler_type_value` | `text` | Yes | `-` | interval, date (yyyy-mm-dd hh:mm:ss) or cron value |
| `scheduler_rule_parameters` | `text` | No | `-` | Optional parameters for the rule/playbook in field=value format separated by semicolons. These fields should match the api name for the rule activity or playbook's activation input fields. Ex: `rule_activity_field1=value1;rule_activity_field2=value2` |


</p>
</details>

<details><summary>Outputs:</summary>
<p>

```python
results = {
  'success': True,
  'content': {
    'args': (2219, # incident_id
    None, # object_id
    None, # row_id
    u'rule3', # Rule to execute
    u'Delete rule3', # Scheduled rule Label
    49, # rule_id
    0, # object_type_id
    None,
    None),
    'executor': 'default',
    'max_instances': 1,
    'func': 'fn_scheduler.components.create_a_scheduled_rule:triggered_job',
    'id': u'rule3',
    'next_run_time': 'Oct 03 2019 12:35PM',
    'name': 'triggered_job',
    'misfire_grace_time': 1,
    'trigger': None,
    'coalesce': False,
    'version': 1,
    'kwargs': {

    }
  }
}
```

</p>
</details>

<details><summary>Example Script: Function Pre-Process</summary>
<p>

```python
inputs.scheduler_label = row['schedule_label']
inputs.modify_scheduler_type = getattr(playbook.inputs, "modify_schedule_type", None)
inputs.modify_scheduler_type_value = getattr(playbook.inputs, "modify_schedule_type_value", "cron")
inputs.scheduler_rule_parameters = getattr(playbook.inputs, "schedule_rule_parameters", None)

```

</p>
</details>

<details><summary>Example Script: Write modified job to DataTable</summary>
<p>

```python
from datetime import datetime

results = playbook.functions.results.output_scheduled_rule_modify
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # '2023-03-24 11:28:34'

if not results.get("success"):
  incident.addNote("Modify Scheduled Rule/Playbook failed: {}".format(results.get("reason")))

else:
  job = results.get("content")
  row['reported_on'] = now
  row['schedule_type'] = job.get('type')
  row['schedule'] = job.get('value')
  incident.addNote("Modify Scheduled Rule/Playbook succeeded for: {}".format(job.get('id')))

```

</p>
</details>

---
## Function - Scheduled Rule List
List the schedules presently defined

 ![screenshot: fn-scheduled-rule-list ](./doc/screenshots/list_scheduled_jobs.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | Yes | `-` | Incident Id to limit returned schedules. 0 or None return all |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

```python
results = {
    'success': True
    'content': [
    {
      'args': (2219, # incident_id
      None, # object_id
      None, # row_id
      u'rule3', # scheduled rule
      u'Delete rule3', # schedule rule label
      49, # rule_id
      0, # object_type_id
      None,
      None),
      'type': 'date', # schedule rule type
      'id': u'rule3', # schedule rule label
      'value': 'Oct 03 2019 12:35PM' # Schedule
    }
  ],
}
```

</p>
</details>

<details><summary>Example Script: Function Pre-Process</summary>
<p>

```python
if rule.properties.incidents_returned == "All":
  inputs.incident_id = 0
else:
  inputs.incident_id = incident.id
```

</p>
</details>

<details><summary>Example Script: Write all jobs to DataTable</summary>
<p>

```python
from datetime import datetime

results = playbook.functions.results.output_scheduled_rule_list
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # '2023-03-24 11:28:34'
date = datetime.now().strftime("%Y-%m-%d")
TYPE_LOOKUP = {
  0: 'Incident',
  1: "Task",
  4: "Artifact",
  5: "Attachment"}

if not results['content']:
  row = incident.addRow("scheduler_rules")
  row['reported_on'] = date
  row['schedule_label'] = "-- no scheduled rules --"

else:
  for job in results['content']:
    row = incident.addRow("scheduler_rules")
    row['schedule_label'] = job['id']
    row['schedule_type'] = job['type']
    row['incident_id'] = job['args'][0]
    row['schedule'] = job['value']
    row['reported_on'] = now
    row['status'] = 'Active' if job['next_run_time'] else 'Paused'
    row['next_run_time'] = job['next_run_time']
    row['rule_type'] = TYPE_LOOKUP.get(job['args'][6], "Datatable")

    if job['args'][8]:
      row['rule'] = "<a href='#playbooks/designer/{}'>{}</a>".format(job['args'][5], job['args'][4])
    else:
      row['rule'] = "<a href='#customize?tab=actions&id={}'>{}</a>".format(job['args'][5], job['args'][4])

```

</p>
</details>

---
## Function - Scheduled Rule Pause
Pause a scheduled rule

 ![screenshot: fn-scheduled-rule-pause ](./doc/screenshots/scheduled_job_actions.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `scheduler_label` | `text` | Yes | `-` | Scheduled job name for identification |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

```python
results = {
  'inputs': {
    u'scheduler_label': u'2225'
  },
  'metrics': {
    'package': 'fn-scheduler',
    'timestamp': '2019-10-08 15:38:04',
    'package_version': '1.0.0',
    'host': 'marks-mbp.cambridge.ibm.com',
    'version': '1.0',
    'execution_time_ms': 21
  },
  'success': True,
  'content': {
    'args': (2225,
    None,
    None,
    u'2225',
    u'Demo Scheduler',
    39,
    0,
    {
      u'scheduler_demo': u'yes'
    },
    None),
    'type': 'interval',
    'id': u'2225',
    'value': '2m'
  },
  'raw': '{"args": [2225, null, null, "2225", "Demo Scheduler", 39, 0, {"scheduler_demo": "yes"}, null], "type": "interval", "id": "2225", "value": "2m"}',
  'reason': None,
  'version': '1.0'
}
```

</p>
</details>

<details><summary>Example Script: Function Pre-Process</summary>
<p>

```python
inputs.scheduler_label = row.schedule_label
```

</p>
</details>

<details><summary>Example Script: Write paused job to DataTable</summary>
<p>

```python
results = playbook.functions.results.output_scheduled_rule_pause

if results.get("success"):
  row['status'] = 'Paused'
else:
  row['status'] = row['status'] + " (Error)"

```

</p>
</details>

---
## Function - Scheduled Rule Remove
Stop and remove a scheduled job


<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `scheduler_label` | `text` | Yes | `-` | Scheduled job name for identification |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

```python
results = {
    'success': True
    'content':  None
}
```

</p>
</details>

<details><summary>Example Script: Function Pre-Process</summary>
<p>

```python
inputs.scheduler_label = row.schedule_label
```

</p>
</details>

<details><summary>Example Script: Write removed job to DataTable</summary>
<p>

```python
results = playbook.functions.results.output_scheduled_rule_remove

if results.get("success"):
  row['status'] = "Deleted"
else:
  row['status'] = row['status'] + " (Error)"
```

</p>
</details>

---
## Function - Scheduled Rule Resume
Resume a scheduled job


<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `scheduler_label` | `text` | Yes | `-` | Scheduled job name for identification |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

```python
results = {
  'inputs': {
    u'scheduler_label': u'2225'
  },
  'metrics': {
    'package': 'fn-scheduler',
    'timestamp': '2019-10-08 15:38:04',
    'package_version': '1.0.0',
    'host': 'marks-mbp.cambridge.ibm.com',
    'version': '1.0',
    'execution_time_ms': 21
  },
  'success': True,
  'content': {
    'args': (2225,
    None,
    None,
    u'2225',
    u'Demo Scheduler',
    39,
    0,
    {
      u'scheduler_demo': u'yes'
    },
    None),
    'type': 'interval',
    'id': u'2225',
    'value': '2m'
  },
  'raw': '{"args": [2225, null, null, "2225", "Demo Scheduler", 39, 0, {"scheduler_demo": "yes"}, null], "type": "interval", "id": "2225", "value": "2m"}',
  'reason': None,
  'version': '1.0'
}
```

</p>
</details>

<details><summary>Example Script: Function Pre-Process</summary>
<p>

```python
inputs.scheduler_label = row.schedule_label
```

</p>
</details>

<details><summary>Example Script: Write resumed job to DataTable</summary>
<p>

```python
results = playbook.functions.results.output_scheduled_rule_resume

if results.get("success"):
  row['status'] = 'Active'
else:
  row['status'] = row['status'] + " (Error)"
```

</p>
</details>

---

## Function - Run Scheduled Job Now
Run a scheduled job immediately

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `scheduler_label` | `text` | Yes | `-` | Scheduled job name for identification |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

```python
results = {
  "version": 2.0,
  "success": true,
  "reason": null,
  "content": {
  },
  "raw": null,
  "inputs": {
    "scheduler_label": "rulex1-5713"
  },
  "metrics": {
    "version": "1.0",
    "package": "fn-scheduler",
    "package_version": "2.0.0",
    "host": "local",
    "execution_time_ms": 1609,
    "timestamp": "2022-04-28 17:39:27"
  }
}
```

</p>
</details>

<details><summary>Example Script: Function Pre-Process</summary>
<p>

```python
inputs.scheduler_label = row['schedule_label']
```

</p>
</details>

<details><summary>Example Script: Write executed job to DataTable</summary>
<p>

```python
results = playbook.functions.results.output_scheduled_rule_run

if not results.success:
  incident.addNote("Run Scheduled Job Now failed for job {}: {}".format(row['schedule_label'], results.reason))
else:
  msg = "Run Scheduled Job Now succeeded for job: {}, Rule/Playbook: {}".format(row['schedule_label'], row['rule'].content)
  incident.addNote(helper.createRichText(msg))
```

</p>
</details>

---

## Data Table - Scheduler Rules

#### API Name:
scheduler_rules

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Reported Date | `reported_on` | `text` | - |
| Schedule Label | `schedule_label` | `text` | - |
| Incident Id | `incident_id` | `text` | - |
| Rule/Playbook Type | `rule_type` | `text` | - |
| Rule/Playbook | `rule` | `text` | - |
| Schedule Type | `schedule_type` | `text` | - |
| Schedule | `schedule` | `text` | - |
| Next Run Time | `next_run_time` | `text` |
| Status | `status` | `text` | - |

---



## Playbooks API
| Playbook Name | Object | Playbook API | Function output API | Post Processing script Name |
| ------------- | ------ | ------------ | ------------------ | ---------------------- |
| Scheduler: List Jobs | `Incident` | pb_scheduler_list_jobs | output_scheduled_rule_list | Write all jobs to DataTable |
| Scheduler: Modify Job | `Datatable` | pb_scheduler_modify_job | output_scheduled_rule_modify | Write modified job to DataTable |
| Scheduler: Pause Job | `Datatable` | pb_scheduler_pause_job | output_scheduled_rule_pause | Write paused job to DataTable |
| Scheduler: Resume Job | `Datatable` | pb_scheduler_resume_job | output_scheduled_rule_resume | Write resumed job to DataTable |
| Scheduler: Run Job now | `Datatable` | pb_scheduler_run_job_now | output_scheduled_rule_run | Write executed job to DataTable |
| Scheduler: Schedule a Job | `Incident` | pb_scheduler_schedule_job | output_scheduled_rule_create | Write scheduled job to DataTable |
| Scheduler: Schedule a Job (Artifact) | `Artifact` | pb_scheduler_schedule_job_artifact | output_scheduled_rule_create | Write scheduled job to DataTable |
| Scheduler: Schedule a Job (Task) | `Incident` | pb_scheduler_schedule_job_task | output_scheduled_rule_create | Write scheduled job to DataTable |

---

## Considerations

### Playbooks and Rules
* All Rules and Workflows of the Scheduler, have now been implemented in Playbooks. This however does not affect the Scheduler's functionality to trigger Rules.
* A Playbook/Rule must be enabled to be scheduled and are again checked when the scheduled Playbook is triggered.
* Playbooks/Rules scheduled must match the invoking Playbook. For instance, to create a scheduled artifact Rule or Playbook, use the Playbook `Scheduler: Schedule a Job (Artifact)`.
* All schedules must be in the future.
* Disabled Playbooks/Rules will not execute but the scheduled Playbook will continue to trigger.
* Playbook triggered on closed incidents will not run and the scheduled Playbook will be removed.
* Incident notes are created each time a scheduled Playbook is executed documenting the Playbook invocation.
* Scheduled Playbooks will not show up under Action Status and Workflow Status. Refer instead to the incident notes.

### Artifacts
* Playbooks executed against artifacts should include at least two Activity Fields:
  * artifact_type
  * artifact_value
* Your artifact level workflow and function would then capture this information using Playbook properties such as:
  * inputs.artifact_type = playbook.inputs.artifact_type
  * inputs.artifact_value = playbook.inputs.artifact_value

### Datatables
* Datatable scheduled playbooks are not part of this package, but can be easily created for a specific Datatable.
* Datatable scheduled playbooks cannot currently reference the invoking datatable row in the pre-processing script. However, a playbooks's activity field in the Activation form can be defined to prompt for it.

### Persistence of Scheduled Playbooks/Rules
* Labels for scheduled Playbooks/Rules need to be unique. Attempting to create a duplicate will fail.
* Sqlite is used to persist scheduled Playbooks/Rules. Restarting resilient-circuits will continue with the scheduled Playbooks/Rules already defined.

### Integrations
* A function executed from a scheduled rule is free to perform any operation against IBM SOAR. Even through a scheduled Playbook/Rule runs from a specific Incident, IBM SOAR API calls can collect and operate on other incidents. For example, a scheduled rule can call a function which queries IBM SOAR for all open tasks with due dates to review any overdue.

## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.

### For Support
This is an IBM supported app. Please search [ibm.com/mysupport](https://ibm.com/mysupport) for assistance.
