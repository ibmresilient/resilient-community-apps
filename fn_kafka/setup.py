#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_kafka',
    display_name='Kafka',
    version='1.0.2',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='https://ibm.biz/soarcommunity',
    description="Resilient Circuits Components for 'fn_kafka'",
    long_description="""Support the ability to produce and consume Kafka messages over a number of brokers.\n
Key features:
<ul>
<li>Ability to define multiple brokers for producing and consuming messages</li>
<li>Send to Kafka allows key/value or just value transmissions on a topic</li>
<li>Poller for listening on broker topics with configurable templates</li>
</ul>
Links: <ul><a target='blank' href='https://ibmresilient.github.io/resilient-community-apps/fn_kafka/README.html'>Documentation</a></ul>
<ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul><ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        'resilient_circuits>=51.0.0',
        'kafka-python-ng~=2.0',     # see: https://github.com/dpkp/kafka-python/issues/2436 & https://github.com/dpkp/kafka-python/issues/2431 
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "KafkaSendFunctionComponent = fn_kafka.components.kafka_send:FunctionComponent",
            "KafkaListenerComponent = fn_kafka.components.kafka_listener:KafkaListenerComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_kafka.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_kafka.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_kafka.util.selftest:selftest_function"]
    }
)