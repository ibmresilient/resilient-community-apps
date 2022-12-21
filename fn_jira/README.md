# Jira App for IBM SOAR

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
  - [Multi-tenancy](#multi-tenancy)
  - [Configuring OAuth](#configuring-oauth)
  - [Custom Layouts](#custom-layouts)
- [Function - Jira Create Comment](#function---jira-create-comment)
- [Function - Jira Open Issue](#function---jira-open-issue)
- [Function - Jira Transition Issue](#function---jira-transition-issue)
- [Data Table - Jira Task References](#data-table---jira-task-references)
- [Custom Fields](#custom-fields)
- [Rules](#rules)
- [How to configure to use a single Jira Server](#how-to-configure-to-use-a-single-jira-server)
- [Creating workflows when server/servers in app.config are labeled](#creating-workflows-when-serverservers-in-appconfig-are-labeled)
- [Troubleshooting & Support](#troubleshooting--support)
---

## Release Notes
| Version | Date | Notes |
| ------- | ---- | ----- |
| 3.0.0 | 12/2022 | <ul><li>Add poller for bidirectional sync</li><li>Updated to work with Jira Cloud</li><li>Add global_settings to app.config that contains the settings for the poller</li></ul>
| 2.2.0 | 10/2022 | <ul><li>Added support for multi-tenancy</li><li>Added support for authentication with token</li><li>Removed support for python 2</li></ul> |
| 2.1.1 | 05/2022 | Updated version for pyjwt dependency |
| 2.1.0 | 04/2022 | <ul><li>Added support for authentication with OAuth</li><li>Includes new configs: `access_token`, `access_token_secret`, `consumer_key_name`, `private_rsa_key_file_path`</li><li>Added support for sending SOAR task notes to Jira -- see updated example workflow</li><li>Added support for images in notes synchronizing to Jira</li><li>Added config `jira_task_references` for custom datatables</li><li>Added option in example rule to set Jira project ID as activity field</li></ul> |
| 2.0.0 | 10/2020 | <ul><li>Added App Host support</li><li>Added proxy support</li><li>Added support for https://pypi.org/project/jira/</li><li>Changed config heading from `jira` to `fn_jira`</li><li>Added configs: `timeout`, `auth_method`, `http_proxy` and `https_proxy`</li><li>Added incident field `jira_issue_id`</li><li>Changed column name in `jira_task_references` Data Table from `jira_api_url` to `jira_issue_id_col`</li></ul> |
| 1.0.2 | 10/2019 | Improvements to data table handling and Bug fixes |
| 1.0.1 | 04/2019 | Support for versions of SOAR 31.0 and beyond |
| 1.0.0 | 12/2018 | Initial Release |

* For customers upgrading from a previous release to 2.2.0 or greater, the app.config file must be manually edited to add new settings required to each server configuration. See [2.2.0 Changes](#2.2.0-changes)

---

## Overview
**Provides integration with JIRA for Issue Creation, Issue Transition and Comment Creation**

 ![screenshot: main](./doc/screenshots/main.png)

This app allows for the tracking of SOAR Incidents and Tasks as Jira Issues. Bidirectional links are saved to allow for easy navigation between the applications.

                        It also allows for the transitioning of Jira issues when the corresponding incident is closed and adds comments to the Jira issue when a Note is created in SOAR.

                        Example rules and workflows can used used or modified to meet your business processes.

### Key Features
* Bidirectional sync between SOAR and Jira
* Issue creation
* Issue transition
* Comment creation

---

## Requirements
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, App Host and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `44.0.7585`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `44.0.7585`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient_circuits>=45.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions: 
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read |
  | Function | Read |
  | Incidents | Read |

The following SOAR platform guides provide additional information: 
* _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. 
* _Integration Server Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _System Administrator Guide_: provides the procedure to install, configure and deploy apps. 

The above guides are available on the IBM Documentation website at [ibm.biz/soar-docs](https://ibm.biz/soar-docs). On this web page, select your SOAR platform version. On the follow-on page, you can find the _App Host Deployment Guide_ or _Integration Server Guide_ by expanding **Apps** in the Table of Contents pane. The System Administrator Guide is available by expanding **System Administrator**.

### Cloud Pak for Security
If you are deploying to IBM Cloud Pak for Security, the requirements are:
* IBM Cloud Pak for Security >= 1.8.
* Cloud Pak is configured with an App Host.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

The following Cloud Pak guides provide additional information: 
* _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. From the Table of Contents, select Case Management and Orchestration & Automation > **Orchestration and Automation Apps**.
* _System Administrator Guide_: provides information to install, configure, and deploy apps. From the IBM Cloud Pak for Security IBM Documentation table of contents, select Case Management and Orchestration & Automation > **System administrator**.

These guides are available on the IBM Documentation website at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs). From this web page, select your IBM Cloud Pak for Security version. From the version-specific IBM Documentation page, select Case Management and Orchestration & Automation.

### Proxy Server
The app does support a proxy server.

### Python Environment
Both Python 3.6 and Python 3.9 are supported.
Additional package dependencies may exist for each of these packages:
* jira~=3.2
* pyjwt~=2.4
* resilient_circuits>=45.0.0

---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **auth_token** | Required for `TOKEN` | `` | Authentication token |
| **url** | Yes | `https://<jira url>` | The URL of your Jira platform. |
| **auth_method** | Yes | `AUTH` | The method of authentication to use when connecting to your Jira platform. Supported methods are `AUTH`, `BASIC`, and `OAUTH`. For more information on authentication see: https://jira.readthedocs.io/en/latest/examples.html#authentication |
| **user** | Required for `AUTH` or `BASIC` | `<jira user>` | The username of the Jira account to use with this integration. They must be a user on the Jira platform with the correct permissions. |
| **password** | Required for `AUTH` or `BASIC` | `<jira user password>` | The password or API Key for the Jira account to use with this integration. `AUTH` only supports password and `BASIC` supports both password and API Key. |
| **access_token** | Required for `OAUTH` | `<oauth access token>` | Access token created through Jira OAuth 1.0a 3LO. Details below. |
| **access_token_secret** | Required for `OAUTH` | `<oauth access secret>` | Access token secret created through Jira OAuth 1.0a 3LO. Details below. |
| **consumer_key_name** | Required for `OAUTH` | `<oauth consumer key>` | Consumer Key name created through Jira UI. Details below. |
| **private_rsa_key_file_path** | Required for `OAUTH` | `/etc/jira_privatekey.pem` | Path to file containing private RSA key associated with the public key that was uploaded in the UI. Details below. |
| **timeout** | No | `10` | The number of seconds to timeout after when making a request to the Jira platform. |
| **jira_dt_name** | No | `jira_task_references` | The datatable in which to store the data for synced SOAR tasks. Default is `jira_task_references`. If using a custom Datatable, this table *must* include the `task_id`, `jira_issue_id_col`, and `jira_link` columns. |
| **verify_cert** | No | `True` | A boolean value. Set to `True` if you want ti verify SSL certificates on each request. |
| **http_proxy** | No | `http://localhost:3128` |  Your HTTP Proxy. |
| **https_proxy** | No | `https://localhost:3128` |  Your HTTPS Proxy. |

#### Multi-tenancy
Starting in version 2.2.0, more than one Jira instance can be configured for SOAR. For enterprises with only one Jira instance, your app.config file will continue to define the Jira instance under the `[fn_jira]` section header.

For enterprises with more than one Jira instance, each instance will have it's own section header, such as `[fn_jira:jira_label1]` where `jira_label1` represents any label helpful to define you Jira environment. You cannot mix `[fn_jira]` and `[fn_jira:jira_label1]` sections headers.

Be aware that modifications to the workflows will be needed to correctly pass this label through the `jira_label` function input field if the Jira server/servers in the app.config have labels.

If you have existing custom workflows, see [Creating workflows when server/servers in app.config are labeled](#creating-workflows-when-serverservers-in-appconfig-are-labeled) for more information about changing them to reference the `jira_label` function input field.

### Configuring OAuth
OAuth authentication is supported with OAuth 1.0a protocol on Jira Server and Jira Cloud. This requires setting some configurations through the Jira UI followed by the 3 legged-dance described in the docs linked below. The main goal of this process is to generate a public and private RSA key, as well as a `access_token` and `access_token_secret`. Follow the steps at the appropriate links to setup the RSA keys and generate an access token. Then set the values as appropriate in your app.config. It is recommended to use App Host secrets to store the tokens if deploying on App Host.

Follow the instructions at the appropriate link to create a public and private key and to create an incoming link in Jira:

* [OAuth on Jira Server](https://developer.atlassian.com/server/jira/platform/oauth/#step-1--configure-jira) (only step 1)
* [OAuth 1.0a on Jira Cloud](https://developer.atlassian.com/cloud/jira/platform/jira-rest-api-oauth-authentication/#step-2--configure-the-client-application-as-an-oauth-consumer) (only step 2)

> As of v2.1.0, this app only supports OAuth 1.0a authentication to Jira.

Once you've completed the linked step above, you can continue with the rest of Jira's guide (in Java) or you can follow the Python steps below.
> Note: these steps have been verified on Python 3.6. No matter the environment that you run the app in, it is recommended to run these steps with Python 3.6.

1. Create a python environment on a machine that has internet access to your Jira server. Install `jira` in the python environment and the required associated dependencies

    ```
    $ pip install jira cryptography pyjwt IPython
    ```

    This will also install the `jirashell` utility which will be used in the next step.

1. Use the `jirashell` utility to preform the OAuth dance:

    ```
    $ jirashell -s <url_of_your_jira_server> --oauth-dance --consumer-key <name_of_consumer_key_in_jira_ui> --key-cert <path_to_private_rsa_key> --print-tokens
    ```

    This will prompt you at a point to follow a link to sign-in and authorize the OAuth tokens. Click "Allow" and return to the shell. Type `y` and hit enter. The Access Token and Access Token Secret will be printed to your terminal. You can now exit the `jirashell` prompt.

1. Use the token and secret printed to your terminal to provide access to Jira for this app. If running in App Host, it is recommended to enter the values of the tokens as secrets in the app's **Configuration** tab by clicking **Add Secret**.

1. In App Host, upload the private key as a file by clicking **New File**. Paste the contents of the private key into the file and ensure that the path to the file is the same as what you wrote in your app.config.

### Custom Layouts
* Import the Data Tables and Custom Fields like the screenshot below:

  ![screenshot: custom_layouts](./doc/screenshots/dt-jira-task-references.png)


---

## Function - Jira Create Comment
Create a Jira comment. To be used when a SOAR Note is created.
See example workflow for configuration of function pre-processor and post-processor scripts

 ![screenshot: fn-jira-create-comment ](./doc/screenshots/fn-jira-create-comment.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | No | `-` | - |
| `jira_comment` | `text` | No | `"Updated in IBM SOAR"` | The comment to add to the issue in Jira |
| `jira_issue_id` | `text` | Yes | `JRA-1000` | The ID of the issue in Jira. Also known as the issue key. E.g: "JRA-1330" |
| `jira_label` | `text` | No | `-` | Enter the label of the server you wish to use. |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "author": {
      "active": true,
      "avatarUrls": {
        "16x16": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=16",
        "24x24": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=24",
        "32x32": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=32",
        "48x48": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=48"
      },
      "displayName": "Local Admin",
      "emailAddress": "admin@ibm.com",
      "key": "JIRAUSER10000",
      "name": "admin",
      "self": "http://localhost:443/rest/api/2/user?username=admin",
      "timeZone": "Etc/UTC"
    },
    "body": "Add comment",
    "created": "2022-10-13T15:17:23.501+0000",
    "id": "10007",
    "jira_url": "\u003ca href=\"http://localhost:443/browse/JRA-5\"\u003eJRA-5\u003c/a\u003e",
    "self": "http://localhost:443/rest/api/2/issue/10004/comment/10007",
    "updateAuthor": {
      "active": true,
      "avatarUrls": {
        "16x16": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=16",
        "24x24": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=24",
        "32x32": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=32",
        "48x48": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=48"
      },
      "displayName": "Local Admin",
      "emailAddress": "admin@ibm.com",
      "key": "JIRAUSER10000",
      "name": "admin",
      "self": "http://localhost:443/rest/api/2/user?username=admin",
      "timeZone": "Etc/UTC"
    },
    "updated": "2022-10-13T15:17:23.501+0000"
  },
  "inputs": {
    "incident_id": 2106,
    "jira_comment": "\u003cdiv class=\"rte\"\u003e\u003cdiv\u003eAdd comment\u003c/div\u003e\u003c/div\u003e",
    "jira_issue_id": "",
    "jira_label": "jira_label2",
    "task_id": 120
  },
  "metrics": {
    "execution_time_ms": 289,
    "host": "local",
    "package": "fn-jira",
    "package_version": "2.2.0",
    "timestamp": "2022-10-13 11:17:23",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
# Example: Jira Create Comment pre-processing script
# If this is a task note, get the taskId
note_content = note.text.content
if note.type == 'task':
  # Set the task_id
  inputs.task_id = task.id
  inputs.jira_issue_id = "" # leave empty for tasks
else:
  inputs.jira_issue_id = incident.properties.jira_issue_id

inputs.jira_label = incident.properties.jira_server
inputs.jira_comment = note_content
inputs.incident_id = incident.id
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
None
```

</p>
</details>

---
## Function - Jira Open Issue
Create a jira issue. To be used when a SOAR Incident is created.
See example workflow for configuration of function pre-processor and post-processor scripts

 ![screenshot: fn-jira-open-issue ](./doc/screenshots/fn-jira-open-issue.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | No | `-` | - |
| `jira_fields` | `text` | No | `-` | A JSON String of the fields to set in Jira |
| `jira_label` | `text` | No | `-` | Enter the label of the server you wish to use |
| `task_id` | `number` | No | `-` | - |

### Notes
* jira_fields example:
```
{
  "project": "ENG",
  "issuetype": "BUG",
  "priority": {"name": "Low"},
  "summary": "IBM SOAR: Review artifact '1.2.3.4'",
  "description": "Created from IBM SOAR"
}
```
* If using the Rule activity fields `jira_project_id` or `jira_issue_type`, modify the select list to represent your instance of Jira's projects, and issue types, respectively. 


</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "issue": {
      "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations",
      "fields": {
        "aggregateprogress": {
          "progress": 0,
          "total": 0
        },
        "aggregatetimeestimate": null,
        "aggregatetimeoriginalestimate": null,
        "aggregatetimespent": null,
        "archivedby": null,
        "archiveddate": null,
        "assignee": null,
        "attachment": [],
        "comment": {
          "comments": [],
          "maxResults": 0,
          "startAt": 0,
          "total": 0
        },
        "components": [],
        "created": "2022-10-13T15:17:10.773+0000",
        "creator": {
          "active": true,
          "avatarUrls": {
            "16x16": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=16",
            "24x24": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=24",
            "32x32": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=32",
            "48x48": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=48"
          },
          "displayName": "Local Admin",
          "emailAddress": "admin@ibm.com",
          "key": "JIRAUSER10000",
          "name": "admin",
          "self": "http://localhost:443/rest/api/2/user?username=admin",
          "timeZone": "Etc/UTC"
        },
        "customfield_10000": "{summaryBean=com.atlassian.jira.plugin.devstatus.rest.SummaryBean@6373408b[summary={pullrequest=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@1ec67710[overall=PullRequestOverallBean{stateCount=0, state=\u0027OPEN\u0027, details=PullRequestOverallDetails{openCount=0, mergedCount=0, declinedCount=0}},byInstanceType={}], build=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@1f929cb[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BuildOverallBean@2caab013[failedBuildCount=0,successfulBuildCount=0,unknownBuildCount=0,count=0,lastUpdated=\u003cnull\u003e,lastUpdatedTimestamp=\u003cnull\u003e],byInstanceType={}], review=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@1669f223[overall=com.atlassian.jira.plugin.devstatus.summary.beans.ReviewsOverallBean@54963441[stateCount=0,state=\u003cnull\u003e,dueDate=\u003cnull\u003e,overDue=false,count=0,lastUpdated=\u003cnull\u003e,lastUpdatedTimestamp=\u003cnull\u003e],byInstanceType={}], deployment-environment=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@1c69e869[overall=com.atlassian.jira.plugin.devstatus.summary.beans.DeploymentOverallBean@65baf9df[topEnvironments=[],showProjects=false,successfulCount=0,count=0,lastUpdated=\u003cnull\u003e,lastUpdatedTimestamp=\u003cnull\u003e],byInstanceType={}], repository=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@3c1be7a1[overall=com.atlassian.jira.plugin.devstatus.summary.beans.CommitOverallBean@594ae85f[count=0,lastUpdated=\u003cnull\u003e,lastUpdatedTimestamp=\u003cnull\u003e],byInstanceType={}], branch=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@ab369bf[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BranchOverallBean@38750d37[count=0,lastUpdated=\u003cnull\u003e,lastUpdatedTimestamp=\u003cnull\u003e],byInstanceType={}]},errors=[],configErrors=[]], devSummaryJson={\"cachedValue\":{\"errors\":[],\"configErrors\":[],\"summary\":{\"pullrequest\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":\"OPEN\",\"details\":{\"openCount\":0,\"mergedCount\":0,\"declinedCount\":0,\"total\":0},\"open\":true},\"byInstanceType\":{}},\"build\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"failedBuildCount\":0,\"successfulBuildCount\":0,\"unknownBuildCount\":0},\"byInstanceType\":{}},\"review\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":null,\"dueDate\":null,\"overDue\":false,\"completed\":false},\"byInstanceType\":{}},\"deployment-environment\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"topEnvironments\":[],\"showProjects\":false,\"successfulCount\":0},\"byInstanceType\":{}},\"repository\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}},\"branch\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}}}},\"isStale\":false}}",
        "customfield_10100": null,
        "customfield_10101": null,
        "customfield_10102": null,
        "customfield_10103": null,
        "customfield_10107": null,
        "customfield_10108": null,
        "customfield_10109": null,
        "customfield_10110": "0|i0000v:",
        "customfield_10111": null,
        "description": "IBM SOAR Link: https://skirrets1.fyre.ibm.com:443/#incidents/2106?task_id=120\n\nCreated in IBM SOAR",
        "duedate": null,
        "environment": null,
        "fixVersions": [],
        "issuelinks": [],
        "issuetype": {
          "description": "Created by Jira Software - do not edit or delete. Issue type for a user story.",
          "iconUrl": "http://localhost:443/images/icons/issuetypes/story.svg",
          "id": "10001",
          "name": "Story",
          "self": "http://localhost:443/rest/api/2/issuetype/10001",
          "subtask": false
        },
        "labels": [],
        "lastViewed": null,
        "priority": {
          "iconUrl": "http://localhost:443/images/icons/priorities/low.svg",
          "id": "4",
          "name": "Low",
          "self": "http://localhost:443/rest/api/2/priority/4"
        },
        "progress": {
          "progress": 0,
          "total": 0
        },
        "project": {
          "avatarUrls": {
            "16x16": "http://localhost:443/secure/projectavatar?size=xsmall\u0026avatarId=10324",
            "24x24": "http://localhost:443/secure/projectavatar?size=small\u0026avatarId=10324",
            "32x32": "http://localhost:443/secure/projectavatar?size=medium\u0026avatarId=10324",
            "48x48": "http://localhost:443/secure/projectavatar?avatarId=10324"
          },
          "id": "10000",
          "key": "JRA",
          "name": "Test Project",
          "projectTypeKey": "software",
          "self": "http://localhost:443/rest/api/2/project/10000"
        },
        "reporter": {
          "active": true,
          "avatarUrls": {
            "16x16": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=16",
            "24x24": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=24",
            "32x32": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=32",
            "48x48": "https://www.gravatar.com/avatar/93f4834ffb88db2b17ed83c3d9281657?d=mm\u0026s=48"
          },
          "displayName": "Local Admin",
          "emailAddress": "admin@ibm.com",
          "key": "JIRAUSER10000",
          "name": "admin",
          "self": "http://localhost:443/rest/api/2/user?username=admin",
          "timeZone": "Etc/UTC"
        },
        "resolution": null,
        "resolutiondate": null,
        "status": {
          "description": "",
          "iconUrl": "http://localhost:443/",
          "id": "10000",
          "name": "Backlog",
          "self": "http://localhost:443/rest/api/2/status/10000",
          "statusCategory": {
            "colorName": "blue-gray",
            "id": 2,
            "key": "new",
            "name": "To Do",
            "self": "http://localhost:443/rest/api/2/statuscategory/2"
          }
        },
        "subtasks": [],
        "summary": "IBM SOAR: Create issue from task",
        "timeestimate": null,
        "timeoriginalestimate": null,
        "timespent": null,
        "timetracking": {},
        "updated": "2022-10-13T15:17:10.773+0000",
        "versions": [],
        "votes": {
          "hasVoted": false,
          "self": "http://localhost:443/rest/api/2/issue/JRA-5/votes",
          "votes": 0
        },
        "watches": {
          "isWatching": true,
          "self": "http://localhost:443/rest/api/2/issue/JRA-5/watchers",
          "watchCount": 1
        },
        "worklog": {
          "maxResults": 20,
          "startAt": 0,
          "total": 0,
          "worklogs": []
        },
        "workratio": -1
      },
      "id": "10004",
      "key": "JRA-5",
      "self": "http://localhost:443/rest/api/2/issue/10004"
    },
    "issue_key": "JRA-5",
    "issue_url": "http://localhost:443/browse/JRA-5",
    "issue_url_internal": "http://localhost:443/rest/api/2/issue/10004",
    "jira_dt_name": "jira_task_references"
  },
  "inputs": {
    "incident_id": 2106,
    "jira_fields": "{ \"summary\":\"IBM SOAR: Create issue from task\",\"issuetype\":\"Story\",\"project\":\"JRA\",\"description\":\"Created in IBM SOAR\",\"priority\":{ \"name\":\"Low\" } }",
    "jira_label": "jira_label2",
    "task_id": 120
  },
  "metrics": {
    "execution_time_ms": 219,
    "host": "local",
    "package": "fn-jira",
    "package_version": "2.2.0",
    "timestamp": "2022-10-13 11:17:10",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
# Example: Jira Open Issue [Incident] pre-processing script
def list_to_json_str(l):
  """
  Function that converts a list into a JSON string.
  Supports types: basestring, unicode, bool, int, list and dicts.
  If the value is None, it sets it to False.
  """
  list_as_str = ''
  json_entry = u'{0},'
  json_entry_str = u'"{0}",'

  for value in l:
    if not value:
      value = False

    if isinstance(value, list):
      list_as_str += json_entry.format(list_to_json_str(value))

    elif isinstance(value, dict):
      list_as_str += json_entry.format(dict_to_json_str(value))

    elif isinstance(value, basestring):
      value = value.replace(u'"', u'\\"').replace("\n", "\\n")
      list_as_str += json_entry_str.format(unicode(value))

    elif isinstance(value, unicode):
      list_as_str += json_entry.format(unicode(value))

    elif isinstance(value, bool):
      list_as_str += json_entry.format('true' if value else 'false')

    elif isinstance(value, int):
      list_as_str += json_entry.format(value)

    else:
      helper.fail('list_to_json_str does not support this type: {}'.format(type(value)))

  return u'{} {} {}'.format(u'[', list_as_str[:-1], u']')

def dict_to_json_str(d):
  """
  Function that converts a dictionary into a JSON string.
  Supports types: basestring, unicode, bool, int, list and nested dicts.
  If the value is None, it sets it to False.
  """

  json_entry = u'"{0}":{1}'
  json_entry_str = u'"{0}":"{1}"'
  entries = []

  for entry in d:
    key = entry
    value = d[entry] 

    if not value:
      value = False

    if isinstance(value, list):
      entries.append(json_entry.format(unicode(key), list_to_json_str(value)))

    elif isinstance(value, dict):
      entries.append(json_entry.format(key, dict_to_json_str(value)))

    elif isinstance(value, basestring):
      value = value.replace(u'"', u'\\"').replace("\n", "\\n")
      entries.append(json_entry_str.format(unicode(key), unicode(value)))

    elif isinstance(value, unicode):
      entries.append(json_entry.format(unicode(key), unicode(value)))

    elif isinstance(value, bool):
      entries.append(json_entry.format(key, 'true' if value else 'false'))

    elif isinstance(value, int):
      entries.append(json_entry.format(unicode(key), value))

    else:
      helper.fail('dict_to_json_str does not support this type: {}'.format(type(value)))

  return u'{} {} {}'.format(u'{', ','.join(entries), u'}')

if rule.properties.jira_label:
  inputs.jira_label = rule.properties.jira_label
else:
  inputs.jira_label = incident.properties.jira_label

# ID of this incident
inputs.incident_id = incident.id

# A map for JIRA priorities
priority_map = { "Low": {"name": "Low"}, "Medium": {"name": "Medium"}, "High": {"name": "High"} }
jira_priority = priority_map.get(incident.severity_code, {"name": "Low"})

# Define JIRA fields here
inputs.jira_fields = dict_to_json_str({
  "project": rule.properties.jira_project_id,
  "issuetype": rule.properties.jira_issue_type,
  "priority": jira_priority,
  "summary": u"IBM SOAR: {0}".format(incident.name),
  "description": incident.description.content if incident.get("description") else "Created in IBM SOAR"
})
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
if results.get("success"):
  results_content = results.get("content", {})
  incident.properties.jira_url = "<a href='{}' target='blank'>{}</a>".format(results_content.get("issue_url"), results_content.get("issue_key"))
  incident.properties.jira_internal_url = results_content.get("issue_url_internal")
  incident.properties.jira_issue_id = results_content.get("issue_key")
  incident.properties.jira_server = rule.properties.jira_label
```

</p>
</details>

---
## Function - Jira Transition Issue
Transition a Jira issue. This can be used when a SOAR Incident is closed or to change the Jira Issue's workflow state.
See example workflow for configuration of function pre-processor and post-processor scripts

 ![screenshot: fn-jira-transition-issue ](./doc/screenshots/fn-jira-transition-issue.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `jira_comment` | `text` | No | `"Updated in IBM SOAR"` | The comment to add to the issue in Jira |
| `jira_fields` | `text` | No | `-` | A JSON String of the fields to set in Jira |
| `jira_issue_id` | `text` | Yes | `JRA-1000` | The ID of the issue in Jira. Also known as the issue key. E.g: "JRA-1330" |
| `jira_label` | `text` | No | `-` | Enter the label of the server you wish to use |
| `jira_transition_id` | `text` | Yes | `11` | The ID to transition the Jira issue to. More information can be found in the Jira Documentation on transition_id |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": "Done",
  "inputs": {
    "jira_comment": "Closed in IBM SOAR\n\nResolution: Done\n",
    "jira_fields": "{ \"resolution\":{ \"name\":\"Done\" } }",
    "jira_issue_id": "JRA-5",
    "jira_label": "jira_label2",
    "jira_transition_id": "Done"
  },
  "metrics": {
    "execution_time_ms": 269,
    "host": "local",
    "package": "fn-jira",
    "package_version": "2.2.0",
    "timestamp": "2022-10-13 11:17:33",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
# Example: Jira Transition Issue pre-processing script
def dict_to_json_str(d):
  """Function that converts a dictionary into a JSON string.
     Supports types: basestring, unicode, bool, int and nested dicts.
     Does not support lists.
     If the value is None, it sets it to False."""

  json_entry = u'"{0}":{1}'
  json_entry_str = u'"{0}":"{1}"'
  entries = []

  for entry in d:
    key = entry
    value = d[entry]

    if not value:
      value = False

    if isinstance(value, list):
      helper.fail('dict_to_json_str does not support Python Lists')

    if isinstance(value, basestring):
      value = value.replace(u'"', u'\\"')
      entries.append(json_entry_str.format(unicode(key), unicode(value)))

    elif isinstance(value, unicode):
      entries.append(json_entry.format(unicode(key), unicode(value)))

    elif isinstance(value, bool):
      value = 'true' if value else 'false'
      entries.append(json_entry.format(key, value))

    elif isinstance(value, int):
      entries.append(json_entry.format(unicode(key), value))

    elif isinstance(value, dict):
      entries.append(json_entry.format(key, dict_to_json_str(value)))

    else:
      helper.fail('dict_to_json_str does not support this type: {0}'.format(type(value)))

  return u'{0} {1} {2}'.format(u'{', ','.join(entries), u'}')

inputs.jira_label = rule.properties.jira_label if rule.properties.jira_label else incident.properties.jira_server
inputs.jira_issue_id = incident.properties.jira_issue_id
inputs.jira_transition_id = "Done"
inputs.jira_comment = u"Closed in IBM SOAR\n\nResolution: {0}\n{1}".format(incident.resolution_id, incident.resolution_summary.content)

resolution_map = { "unresolved": "Obsolete", "duplicate": "Duplicate", "not an issue": "Won't Do", "resolved": "Done" }

# Define JIRA fields here
inputs.jira_fields = dict_to_json_str({
  "resolution": { "name": resolution_map.get(str(incident.resolution_id).lower(), "Done") }
})
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python
from java.util import Date
time_now = Date().time

if results.get("success"):
  row.date = time_now
  row.status = "Closed"
```

</p>
</details>

---


## Data Table - Jira Task References

 ![screenshot: dt-jira-task-references](./doc/screenshots/dt-jira-task-references.png)

#### API Name:
jira_task_references

#### Columns:
| Column Name | API Access Name | Type | Tooltip |
| ----------- | --------------- | ---- | ------- |
| Action Date | `date` | `datetimepicker` | - |
| Jira Issue ID | `jira_issue_id_col` | `text` | - |
| Jira Link | `jira_link` | `textarea` | - |
| Server | `server` | `text` | Label of the server being used |
| Status | `status` | `text` | - |
| Task | `task` | `textarea` | - |
| Task Id | `task_id` | `text` | - |

---

## Custom Fields
| Label | API Access Name | Type | Prefix | Placeholder | Tooltip |
| ----- | --------------- | ---- | ------ | ----------- | ------- |
| Jira Internal URL | `jira_internal_url` | `text` | `properties` | - | The REST API URL |
| Jira Issue ID | `jira_issue_id` | `text` | `properties` | JRA-1000 | The ID of the issue in Jira. E.g. JRA-1000 |
| Jira Server | `jira_server` | `text` | `properties` | - | Label of the server you wish to use |
| Jira Ticket URL | `jira_url` | `textarea` | `properties` | - | Contains URL back to the Jira issue created via the UI |

---


## Rules
| Rule Name | Object | Workflow Triggered |
| --------- | ------ | ------------------ |
| Example: Create Jira Issue | incident | `jira_open_issue` |
| Example: Create Jira Issue (Task) | task | `example_jira_open_issue_task` |
| Example: Jira Close Issue | incident | `jira_transition_issue` |
| Example: Jira Close Issue (Task) | jira_task_references | `jira_transition_issue_task` |
| Example: Jira Create Comment | note | `jira_create_comment` |
| Example: Jira Create Comment (Task) | note | `jira_create_comment` |

---

## How to configure to use a single Jira Server
To use only a single server there are two ways this can be configured
1. Use the configuration used in Jira Integration versions prior to V2.2.0
```
[fn_jira]
url=https://<jira url>
auth_method=BASIC
user=<jira username or email>
password=<jira user password or API Key>
# For TOKEN authentication
#auth_token=
# For OAUTH connections, the four parameters below are required and user/password are ignored
#access_token = <oauth access token>
#access_token_secret = <oauth access token secret>
#consumer_key_name = <oauth consumer key - from Jira incoming link settings>
#private_rsa_key_file_path = <private RSA key matched with public key on Jira>
timeout=10
# data Table name to hold data for tasks synced to Jira
jira_dt_name=jira_task_references 
# use verify_cert to disable untrusted certificate verification
verify_cert=True
#http_proxy=
#https_proxy=
```
2. Either keep the label, jira_label1, or change it
```
[fn_jira:jira_label1]
url=https://<jira url>
auth_method=BASIC
user=<jira username or email>
password=<jira user password or API Key>
# For TOKEN authentication
#auth_token=
# For OAUTH connections, the four parameters below are required and user/password are ignored
#access_token = <oauth access token>
#access_token_secret = <oauth access token secret>
#consumer_key_name = <oauth consumer key - from Jira incoming link settings>
#private_rsa_key_file_path = <private RSA key matched with public key on Jira>
timeout=10
# data Table name to hold data for tasks synced to Jira
jira_dt_name=jira_task_references 
# use verify_cert to disable untrusted certificate verification
verify_cert=True
#http_proxy=
#https_proxy=
```

## Creating workflows when server/servers in app.config are labeled
The function input field `jira_label` is required when Jira server/servers in the app.config are labeled. In the example workflows pre-process scripts the
input field `jira_label` is defined the following way,
```python
inputs.jira_label = rule.properties.jira_label
```

Example app.config server label: [fn_jira:jira_label1]
  `jira_label1` will be set to `inputs.jira_label` in the above example.

## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.

### For Support
This is an IBM supported app. Please search [ibm.com/mysupport](https://ibm.com/mysupport) for assistance.
