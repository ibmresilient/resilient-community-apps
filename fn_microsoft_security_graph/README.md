# Resilient Functions Integration for Microsoft Graph Security API

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release 
  notes of a previous release
-->
### v1.1.0
* Support for App Host
* Proxy support
* Readable formatting of incident notes containing Alert JSON data

**NOTE** Existing users running fn_microsoft_security_graph functions on an integrations server, should save the [fn_microsoft_security_graph] section of their app.config file to another file and delete that section from the app.config file before installing the new version, as this section has changed.  After installation get the new configuration by running:
```
  $ resilient-circuits config -u -l fn-microsoft-security-graph
  ```
Edit the required configuration setting as described in the [Integration Server](#integration-server) section below.

### v1.0.1
* Python 2 to 3 improvements
* UI version changes

## Key Features
<!--
  List the Key Features of the Integration
-->
* Alert Polling Integration that creates new incidents in the Resilient platform from Microsoft Graph Security API alerts.
* Search function to query alerts across the tenant's data using Microsoft Graph Security API.
* Function to get details of specific Microsoft Security alerts.
* Function to update details of specific Microsoft Security alerts.
* Update Microsoft Security alerts as "Resolved" when the corresponding Resilient incident is closed.

---
## Installation

### App Format

The app .zip file is in a container format and requires a Resilient platform configured with an App Host. 

The app tar.gz file is an extension format and requires a Resilient platform configured with an integration server.

### App Host
For a complete guide on how to configure App Host for Resilient and install apps, please reference the Resilient Apps [Knowledge Center](https://www.ibm.com/support/knowledgecenter/SSBRUQ).

All the components for running this integration in a container already exist when using the App Host app.

To install,

* Navigate to Administrative Settings and then the Apps tab.
* Click the Install button and select the downloaded file: app-fn_microsoft_security_graph-x.x.x.zip.
* Go to the Configuration tab and edit the app.config file, editing the tenant_id, client_id and client_secret and making any additional setting changes.

  | Config | Required | Example | Description |
  | ------ | :------: | ------- | ----------- |
  | **microsoft_graph_token_url** | Yes | `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token` | *Microsoft Graph URL endpoint for acquring access token* |
  | **microsoft_graph_url** | Yes | `https://graph.microsoft.com/v1.0` | *Microsoft Graph base URL * |
  | **tenant_id** | Yes | `xxx` | *Microsoft Azure Tenant ID* |
  | **client_id** | Yes | `xxx` | *Microsoft Azure Client ID (Application ID)* |
  | **client_secret** | Yes | `xxx` | *Microsoft Azure Client Secret* |
  | **msg_polling_intervals** | Yes | `0` | *Polling interval in seconds. Zero to turn off poller* |
  | **incident_template** | No | `` | *Path to custom jinja template. If not set, use default template* |
  | **alert_query** | No | `filter=assignedTo eq 'analyst@m365x594651.onmicrosoft.com' and severity eq 'high'` | *String query to apply to the alert polling component* |
  | **alert_time_range_sec** | No | `3600` | *Times in seconds to set the start dateTime values for the createdDateTime field when filtering alerts* |

### Integration Server

* Download the `app-fn_microsoft_security_graph-x.x.x.zip` file.
* Copy the `.zip` to your Integration Server and SSH into it.
* **Unzip** the package:
  ```
  $ unzip app-fn_microsoft_security_graph-x.x.x.zip
  ```
* **Install** the package:
  ```
  $ pip install fn_microsoft_security_graph-x.x.x.tar.gz
  ```
* Import the **configurations** into your app.config file:
  ```
  $ resilient-circuits config -u -l fn-microsoft-security-graph
  ```
* Import the fn_microsoft_security_graph **customizations** into the Resilient platform:
  ```
  $ resilient-circuits customize -y -l fn-microsoft-security-graph
  ```
* Open the config file, scroll to the bottom and edit your fn_microsoft_security_graph configurations:
  ```
  $ nano ~/.resilient/app.config
  ```
    | Config | Required | Example | Description |
  | ------ | :------: | ------- | ----------- |
  | **microsoft_graph_token_url** | Yes | `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token` | *Microsoft Graph URL endpoint for acquring access token* |
  | **microsoft_graph_url** | Yes | `https://graph.microsoft.com/v1.0` | *Microsoft Graph base URL * |
  | **tenant_id** | Yes | `xxx` | *Microsoft Azure Tenant ID* |
  | **client_id** | Yes | `xxx` | *Microsoft Azure Client ID (Application ID)* |
  | **client_secret** | Yes | `xxx` | *Microsoft Azure Client Secret* |
  | **msg_polling_intervals** | Yes | `0` | *Polling interval in seconds. Zero to turn off poller* |
  | **incident_template** | No | `` | *Path to custom jinja template. If not set, use default template* |
  | **alert_query** | No | `filter=assignedTo eq 'analyst@m365x594651.onmicrosoft.com' and severity eq 'high'` | *String query to apply to the alert polling component* |
  | **alert_time_range_sec** | No | `3600` | *Times in seconds to set the start dateTime values for the createdDateTime field when filtering alerts* |

* **Save** and **Close** the app.config file.
* [Optional]: Run selftest to test the Integration you configured:
  ```
  $ resilient-circuits selftest -l fn-microsoft-security-graph
  ```
* **Run** resilient-circuits or restart the Service on Windows/Linux:
  ```
  $ resilient-circuits run
  ```
---

#### Uninstall
* SSH into your Integration Server.
* **Uninstall** the package:
  ```
  $ pip uninstall fn-microsoft-security-graph
  ```
* Open the config file, scroll to the [fn_microsoft_security_graph] section and remove the section or prefix `#` to comment out the section.
* **Save** and **Close** the app.config file.
