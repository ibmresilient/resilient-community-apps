# Introduction
This package contains the KafkaFeed Plugin to the Data Feed extension.  This Data Feed extension allows one to maintain "replica" data for SOAR incidents, artifacts, tasks, notes, etc.  The updates are performed in near real-time.

This plugin allows this replica data to be pushed to kafka topics for downstream data collection.

Refer to the documentation on the Data Feed extension for uses cases, support and configuration options. Also refer to the other Data Feed plugins which can be used in combination.

# History
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.1.0   | 01/2024 | Updated base rc_data_feed to 3.0.0 and added selftest capabilities |
| 1.0.1   | 08/2020 | App Host support |
| 1.0.0   | 12/2019 | Initial release |

# License

Unless otherwise specified, contents of this repository are published under the MIT open-source
[LICENSE](LICENSE).

# Installation
  The integration package contains Python components that are called by the SOAR platform. These components run in the Resilient Circuits integration framework. The package also includes SOAR customizations that will be imported into the platform later.
  You perform these installation procedures at the SOAR integration server.

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
  unzip rc_data_feed-plugin-kafkafeed-<version>.zip
  [sudo] pip install --upgrade rc_data_feed-plugin-kafkafeed-<version>.tar.gz
```
* Configure Resilient-circuits

  The Resilient Circuits process runs as an unprivileged user, typically named integration. If you do not already have an integration user configured on your appliance, create it now.
  Complete the following steps to configure and run the integration:
* Using sudo, switch to the integration user, as follows:
```
  sudo su - integration
```
* Use one of the following commands to create or update the resilient-circuits configuration file. Use –c for new environments or –u for existing environments.
```
  resilient-circuits config -c
  or
  resilient-circuits config –u [-l rc-data-feed-plugin-kafkafeed]
```
* Edit the resilient-circuits configuration file, as follows:

  - In the [resilient] section, ensure that you provide all the information required to connect to the SOAR platform.
  - In the [feeds] section, define the feed(s) you intend to use and create separate sections for each feed. For example:
    `feeds=kafka_feed`
  - In the [kafka_feed] section, configure the settings for your kafka environment.
```
  [feeds]
  # comma separated section names. ex. sqlserver_feed,file_feed
  feed_names=kafka_feed
  reload=False
  # use reload_types to limit the types of objects when reload=true.
  # Ex: incident,task,note,artifact,attachment,<data_table_api_name>
  reload_types=
  # set to true if ElasticSearch errors occur during reload=true
  reload_query_api_method=False

  # feed_data is the default message destination that will be listened to
  queue=feed_data

  # set to true if attachment data should be part of payload send to plugins
  # NOTE: attachment data sent to kafka will be base64 encoded
  include_attachment_data=false
  # if necessary, specify the supported workspace (by label, case sensitive) and the list of feeds associated with it
  # ex: 'Default Workspace': ['sqlserver_feed'], 'workspace A': ['kafka_feed', 'resilient_feed']
  workspaces=
  # support for parallel execution. NOTE: as of 1.1.0 kafka_feed DOES NOT support parallel execution
  parallel_execution = False

  [kafka_feed]
  class=KafkaFeed
  ## Select the topics for each object type in Resilient format is <type>=<topic>;<type>=<topic>
  topic_map=note= test; task=task; incident = incident;artifact =artifact;default=incident_data
  ## Connection Information - see notes on how to use in confluent docs
  bootstrap.servers=localhost:9092
  acks=all
  message.timeout.ms=5000
  ## Optional for Kerberos - uncomment to use sasl_plaintext
  #security.protocol=sasl_plaintext
  #sasl.mechanism=GSSAPI
  #sasl.kerberos.keytab=/etc/security/keytabs/kafka.keytab
  #sasl.kerberos.service.name=kafka
  #sasl.kerberos.principal=kafka/server.example.com

  # test configuration settings
  #selftest_timeout=20 # seconds before aborting connection test (defaults to 10)
```

# KafkaFeed Class
This class allows incident data to be submitted to a Kafka environment for processing. Multiple topics can be used by
defining datatype assignments to topics in your `app.config` section such as:
```
topic_map=note=note_topic;task=task_topic;incident=incident_topic;artifact=artifact_topic
```
Use the default topic_map reference to specify a catch-all for any Resilient datatype that isn’t explicitly defined:
```
topic_map=incident=incident_topic;default=incident_data_topic
```

Additionally, Kafka headers are used to add additional meta-data about the operation and object type sent:
```
[
  “action”: “upsert|delete”,
  “type”: “incident|artifact|attachment|datatable|milestone|note|task”
]
```
## Integration Server Requirements
The python library used, confluentKafka, relies on a system library (librdkafka) to integrate with your Kafka environment. See the README on confluentKafka for information on librdkafka installation.
