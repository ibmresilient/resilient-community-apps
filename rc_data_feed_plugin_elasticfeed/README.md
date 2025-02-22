# Data Feed Elasticsearch Plugin

## Introduction
This package contains the Elasticsearch Plugin to the Data Feed extension.  This Data Feed extension allows one to maintain "replica" data for IBM QRadar SOAR incidents, artifacts, tasks, notes, etc.  The updates are performed in near real-time.

This plugin allows this replica data to be maintained in Elasticsearch.

Refer to the documentation on the Data Feed extension for uses cases support and configuration options. Also refer to the other Data Feed plugins which can be used in combination.

## History
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.2.0   | 09/2024 | Support for time series data |
| 1.1.1   | 01/2024 | Updated base image rc_data_feed to 3.0.0 |
| 1.1.0   | 07/2022 | New base images and functionality for attachments |
| 1.0.1   | 08/2020 | App Host support |
| 1.0.0   | 12/2019 | Initial release |

### 1.1.0 Changes

This release modified the base portion of the Data Feeder which is controlled by the `[feed]` section within the app.config file. New parameters have been added which you need to manually add if upgrading from a previous version:

| Parameter | Value(s) | Capability |
| --------- | -------- | ---------- |
| reload_types | incident,task,note,artifact,attachment,<data_table_api_name> | use reload_types to limit the types of objects when reload=true. Leave empty to include all data. |
| workspaces | "Default Workspace": ["sqlserver_feed"], "workspace A": ["kafka_feed", "resilient_feed"] | This setting allows for the partitioning of Data Feeder execution among different workspaces. The format is to specify the workspace name with the data feeder components to associated with it: "workspace": ["app.config section_name"]. If unused, data from all workspaces is accessed. |
| include_attachment_data | true/false | set to true if attachment data should be part of the sent payload. When 'true', the attachment's byte data is saved in base64 format. |

### 1.2.0 Changes
Version 1.2.0 introduces incident timeseries data fields. These are custom select or boolean fields, as well as incident `Owner`, `Phase` and `Severity` fields, which record the duration in seconds each field contains a particular value.
For instance, how many seconds `Severity` has a value of `Low` and `Medium`, etc.

To use this capability, add the following app.config settings to the `[feeds]` configuration section. 

| Key | Values | Description |
| :-- | :----- | :---------- |
| timeseries | always \| onclose \| never | When to collect time-series data. Because of the extra API call needed to collect this data, it could be more impactful on SOAR when set to 'always'. default is 'never' |
| timeseries_fields | owner_id, phase_id, severity_code, <custom_field> | A comma separated list of time-series fields to collect. Custom select and boolean fields are also possible. Specify wildcard fields with '?' or '*'. ex. ts_* will collect all time-series fields starting with "ts_". default is all timeseries fields |

## Compatibility
SOAR Compatibilty: 51.0.0 or higher

CP4S Compatibility: 1.10 or higher


## License

Unless otherwise specified, contents of this repository are published under the MIT open-source
[LICENSE](LICENSE).

## Installation
  The integration package contains Python components that are called by the IBM SOAR platform. These components run in the Resilient Circuits integration framework. The package also includes IBM SOAR customizations that will be imported into the platform.

### App Host Installation
With App Host, all the run-time components are pre-built. Perform the following steps to install and configure:
1. Within IBM SOAR, navigate Administrative Settings and then Apps.
2. Click on the Install button and select the downloaded app-rc_data_feed_plugin_elasticfeed-x.x.x.zip file. This step will install the associated rules and message destination.
3. Once installed, navigate to the app's Configuration tab and edit the app.config file updating the `[resilient]`
section as necessary and updating the `[elastic_feed]` section to reflect the location and authentication settings for your instance of Elasticsearch.

### Integration Server Installation
#### Install the Python components
  Complete the following steps to install the Python components:
* Ensure that the environment is up-to-date, as follows:
```
  sudo pip install --upgrade pip
  sudo pip install --upgrade setuptools
  sudo pip install --upgrade resilient-circuits
```
*	Run the following commands to install the package:
```
  unzip rc_data_feed-plugin-elasticsearch-<version>.zip
  [sudo] pip install --upgrade rc_data_feed-plugin-elasticsearch-<version>.tar.gz
```
*	Configure Resilient-circuits

  The Resilient Circuits process runs as an unprivileged user, typically named integration. If you do not already have an integration user configured on your appliance, create it now.
  Complete the following steps to configure and run the integration:
*	Using sudo, switch to the integration user, as follows:

`  sudo su - integration`
*	Use one of the following commands to create or update the resilient-circuits configuration file. Use –c for new environments or –u for existing environments.
```
  resilient-circuits config -c
  or
  resilient-circuits config –u [-l rc-data-feed-plugin-elasticsearch]
```
*	Edit the resilient-circuits configuration file, as follows:

     - In the [resilient] section, ensure that you provide all the information required to connect to the IBM SOAR platform.
     - In the [feeds] section, define the feed(s) you intend to use and create separate sections for each feed. For example:
     `feed_names=elastic_feed`
     - In the [elastic_feed] section, configure the settings for your elasticsearch environment.
    ```
    [feeds]
    ## comma separated section names. ex. sqlserver_feed,file_feed
    feed_names=elastic_feed
    reload=false
    ## use reload_types to limit the types of objects when reload=true.
    ## Ex: incident,task,note,artifact,attachment,<data_table_api_name>
    reload_types=
    ## set to true if ElasticSearch errors occur during reload=true
    reload_query_api_method=false

    ## feed_data is the default message destination that will be listened to
    queue=feed_data

    ## set to true if attachment data should be part of payload send to plugins
    ## attachment data sent to elastic will be base64 encoded
    include_attachment_data=false
    ## if necessary, specify the supported workspace (by label, case sensitive) and the list of feeds associated with it
    ## ex: 'Default Workspace': ['sqlserver_feed'], 'workspace A': ['kafka_feed', 'resilient_feed']
    workspaces=
    ## support for parallel execution. Default is False
    parallel_execution = False

    [elastic_feed]
    class=ElasticFeed
    url=http://localhost
    port=9200
    ## if using multiple organizations, consider indexes such as resilient_<org_ID>
    ## each document type will append to this index as elastic 6.0 only supports one document type per index
    index_prefix=resilient_
    #auth_user=
    #auth_password=
    cafile=false
    ```

## ElasticFeed Class
This class allows you to write all incoming data to ElasticSearch. The data representation within Elastic is referenced by index, document type (incident, note, task, artifact, etc.) and document_id (incident_id, note_id, task_id, etc.).
The following configuration items are supported:

| Key | Values | Description |
| :- | :---- | :---------- |
| class | ElasticFeed | Indicates that the section is for an ElasticSearch. |
| url | | Ex. https://eliastic.yourorg.com	URL of Elastic server. Port is specified in it’s own parameter. |
| port | | Ex. 9200	Default is 9200 |
| index_prefix | resilient_ | Ex. Prefix for index. For example, an incident will be created under 'resilient_incident' if the setting is 'resilient_'. When using multiple organizations, consider indexes such as resilient_<org_ID>_.  Index values must be lower case. |
| auth_user | | User and password to authenticate to ElasticSearch. |
| auth_password	| | User and password to authenticate to ElasticSearch. |
| cafile | True | False	Specify  ‘false’ to bypass certification authentication |

### Considerations
ElasticSearch allows for the updating to and deleting of individual documents. No data duplication occurs. A recently deleted custom datatable column may also not update until circuits is re-run or until the datatable is edited in the UI.
Consult section 7.2 of the rc-data-feed documentation for datatable limitations in general.
