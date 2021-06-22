# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_kafka_send"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_kafka]
# comma separated list of configurations to listen on for inbound messages. 
#   Ex. 'brokerA' will refer to [fn_kafka:brokerA]
# comment out or leave unset to disable listening 
listener_brokers=
# name broker to use for selftest
selftest_broker=

[fn_kafka:brokerA]
# repeat this section to identify another broker: [fn_kafka:brokerB]
# see https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html for all the possible parameters
bootstrap_servers=127.0.0.1:9092
# listner group for consumers
#group_id=
# client identifier for producers
#client_id=
sasl_mechanism=PLAIN
security_protocol=PLAINTEXT
ssl_check_hostname=False
#ssl_cafile=
#ssl_certfile=
sasl_plain_username=
sasl_plain_password=
# comma separated list of topics which are listened on for create incident messages
topics=
# directory containing templates to convert the Kafka data into json format acceptable for the incident API call
# name the templates: <topic>_create_template.jinja and <topic>_update_template.jinja
template_dir=
"""
    return config_data