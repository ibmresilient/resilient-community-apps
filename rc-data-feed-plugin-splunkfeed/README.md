# Introduction
This package contains the SplunkFeed Plugin to the Data Feed extension.  This Data Feed extension allows one to maintain "replica" data for Resilient incidents, artifacts, tasks, notes, etc.  The updates are performed in near real-time.

This plugin allows this replica data to be maintained in Splunk.

Refer to the documentation on the Data Feed extension for uses cases support and configuration options. Also refer to the other Data Feed plugins which can be used in combination.

  
# License

Unless otherwise specified, contents of this repository are published under the MIT open-source
[LICENSE](LICENSE).

# Installation
  The integration package contains Python components that are called by the Resilient platform. These components run in the Resilient Circuits integration framework. The package also includes Resilient customizations that will be imported into the platform later.
  You perform these installation procedures at the Resilient integration server.
  
## Install the Python components
  Complete the following steps to install the Python components:
* Ensure that the environment is up-to-date, as follows:
```
  sudo pip install --upgrade pip
  sudo pip install --upgrade setuptools
  sudo pip install --upgrade resilient-circuits
```  
* Run the following commands to install the package:
```
  unzip rc_data_feed-plugin-splunkfeed-<version>.zip
  [sudo] pip install --upgrade rc_data_feed-plugin-splunkfeed-<version>.tar.gz
```  
* Configure Resilient-circuits

  The Resilient Circuits process runs as an unprivileged user, typically named integration. If you do not already have an integration user configured on your appliance, create it now. 
  Complete the following steps to configure and run the integration:
* Using sudo, switch to the integration user, as follows:

`  sudo su - integration`
* Use one of the following commands to create or update the resilient-circuits configuration file. Use –c for new environments or –u for existing environments.
```
  resilient-circuits config -c
  or
  resilient-circuits config –u [-l rc-data-feed-plugin-splunkfeed]
```
* Edit the resilient-circuits configuration file, as follows:
    
     - In the [resilient] section, ensure that you provide all the information required to connect to the Resilient platform.
     - In the [splunk_hec_feed] section, configure the settings for your splunkfeed environment.
     - In the [feeds] section, define the feed(s) you intend to use and create separate sections for each feed. For example:
```
  [feeds]
  feed_names=splunk_feed
  reload=True
  # feed_data is the default queue that will be listened to
  queue=feed_data
  
  [splunk_hec_feed]
  class=SplunkHECFeed
  token=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  host=splunk.host.com
  port=8088
  index=data_feeder
  # only use source_type if using one type. otherwise, the resilient object type (incident, note, artifact, etc.) is used
  #event_source_type=txt
  event_host=localhost
  event_source=resilient
  use_ssl=true
```

# SplunkHECFeed Class
The SplunkHECFeed class utilizes the Splunk HTTP Event Collector for data import. This is convenient as the data from Resilient is readily converted to JSON which can be natively consumed by Splunk.

| Key | Values | Description |
| :-- | :----- | :---------- |
| class | SplunkHECFeed | Indicates that the section is for Splunk ES. |
| token | Ex. 81e2d4bb-c008-49ac-a7a7-c0bf408c999 | API token defined for the HEC data input. |
| host | Ex. splunk.yourorg.com | 
port | Ex. 8088 | The default is 8088 |
| index | Ex data_feeder | The name of the index already defined. |
| event_host | Ex. myorg.com | Optional host name to record as the source of the events. |
| event_source | Ex. resilient | Optional source name of the events. Specifying a value improves searching
| event_source_type |  | Optional source_type if one value is used for all events. If unspecified, each object type (incident, task, note, etc.) is used as the source_type
| use_ssl | True | False | Indicate if connections to the HEC uses encryption (https) |

## Considerations
* Enable the HTTP Event Collector within Splunk ES before using this data feed. 
* Splunk events are immutable. Resilient object changes are represented as new events. No event deletion is possible. 
* Be aware that when using `reload=True`, all Resilient records will be duplicated in Splunk each time resilient-circuits is re-started.
