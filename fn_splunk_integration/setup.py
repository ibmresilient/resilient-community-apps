#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_splunk_integration',
    version='1.0.3',
    license='MIT License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Add, Search and Delete artifacts to Splunk ES",
    long_description="Several functions to operate with Splunk ES intel collections, including updates to SplunkES notable events and add, search and delete operations to intel collections based on artifact type values.",
    url="https://github.com/ibmresilient/resilient-community-apps",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient_lib',
        'splunk-sdk'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "SplunkUpdateNotableFunctionComponent = fn_splunk_integration.components.splunk_update_notable:FunctionComponent",
            "SplunkDeleteThreatIntelItemFunctionComponent = fn_splunk_integration.components.splunk_delete_threat_intel_item:FunctionComponent",
            "SplunkSearchFunctionComponent = fn_splunk_integration.components.splunk_search:FunctionComponent",
            "SplunkAddIntelItemFunctionComponent = fn_splunk_integration.components.splunk_add_intel_item:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_splunk_integration.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_splunk_integration.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_splunk_integration.util.selftest:selftest_function"]
    }
)