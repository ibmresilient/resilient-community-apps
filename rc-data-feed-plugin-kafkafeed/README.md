# Introduction
This package contains the KafkaFeed Plugin to the Data Feed extension.  This Data Feed extension allows one to maintain "replica" data for Resilient incidents, artifacts, tasks, notes, etc.  The updates are performed in near real-time.

This plugin allows this replica data to be pushed to kafka topics for downstream data collection.

Refer to the documentation on the Data Feed extension for uses cases, support and configuration options. Also refer to the other Data Feed plugins which can be used in combination.
  
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
    
  - In the [resilient] section, ensure that you provide all the information required to connect to the Resilient platform.
  - In the [feeds] section, define the feed(s) you intend to use and create separate sections for each feed. For example:
    `feeds=kafka_feed`
  - In the [kafka_feed] section, configure the settings for your kafka environment.
```
  [feeds]
  feed_names=kafka_feed
  # set to true to synchronize all incidents when resilient-circuits starts.
  # care should be use when using this for every resilient-circuits restart
  reload=True
  # feed_data is the default queue that will be listened to
  queue=feed_data
  
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
