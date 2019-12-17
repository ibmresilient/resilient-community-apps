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
"""

    return config_data
