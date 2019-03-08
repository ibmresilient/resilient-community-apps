#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_rsa_netwitness',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url='https://github.com/ibmresilient/resilient-circuits-packages',
    description="Resilient Circuits Components for 'fn_rsa_netwitness'",
    long_description="Resilient Circuits Components to query for NetWitness metadata and retrieve pcap data 'fn_rsa_netwitness'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "NetwitnessRetrievePcapFile = fn_rsa_netwitness.components.netwitness_retrieve_pcap_file:FunctionComponent",
            "NetwitnessRetrieveLogData = fn_rsa_netwitness.components.netwitness_retrieve_log_data:FunctionComponent",
            "NetwitnessQuery = fn_rsa_netwitness.components.netwitness_query:FunctionComponent",
            "NetwitnessGetMetaIdRanges = fn_rsa_netwitness.components.netwitness_get_meta_id_ranges:FunctionComponent",
            "NetwitnessGetMetaValues = fn_rsa_netwitness.components.netwitness_get_meta_values:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_rsa_netwitness.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_rsa_netwitness.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_rsa_netwitness.util.selftest:selftest_function"]
    }
)