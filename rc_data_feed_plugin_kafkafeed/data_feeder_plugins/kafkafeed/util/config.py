# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_data_feed"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[kafka_feed]
class=KafkaFeed
# Select the topics for each object type in Resilient format is <type>=<topic>;<type>=<topic>
topic_map=note=test;task=task;incident=incident;artifact=artifact;default=incident_data
# Connection Information - see notes on how to use in confluent docs
bootstrap.servers=localhost:9092
acks=all
message.timeout.ms=5000
# Optional for Kerberos - uncomment to use sasl_plaintext
#security.protocol=sasl_plaintext
#sasl.mechanism=GSSAPI
#sasl.kerberos.keytab=/etc/security/keytabs/kafka.keytab
#sasl.kerberos.service.name=kafka
#sasl.kerberos.principal=kafka/server.example.com

# test configuration settings
#selftest_timeout=20 # seconds before aborting connection test (defaults to 10)
"""

    return config_data

def apphost_config_section_data():
    return u"""[feeds]
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
# NOTE: attachment data sent to kafka_feed will be base64 encoded
include_attachment_data=false
# if necessary, specify the supported workspace (by label, case sensitive) and the list of feeds associated with it
# ex: 'Default Workspace': ['sqlserver_feed'], 'workspace A': ['kafka_feed', 'resilient_feed']
workspaces=
# support for parallel execution. NOTE: as of 1.1.0 kafka_feed DOES NOT support parallel execution
parallel_execution = False
"""
