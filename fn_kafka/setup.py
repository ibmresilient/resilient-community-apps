#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_kafka',
    version='1.0.0',
    license='MIT',
    author='Mark Scherfling',
    author_email='Resilient Labs',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_kafka'",
    long_description="""Support the ability to produce and consume Kafka messages over a nunber of brokers.
Key features:
* Ability to define multiple brokers for producing and consuming messages
* Send to Kafka allows key/value or just value transmissions on a topic
* Poller for listening on broker topics with configurable templates""",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'kafka>=1.3.5',
        'resilient-lib',
        'resilient'
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