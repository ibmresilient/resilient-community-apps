#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_splunk_integration',
    version='1.0.0',
    license='MIT License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_splunk_integration'",
    long_description="Update SplunkES notable event; perform Splunk/SplunkES search; add new threat intel item; delete threat intel item",
    install_requires=[
        'resilient_circuits>=30.0.0',
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
        "resilient.circuits.customize": ["customize = fn_splunk_integration.util.customize:customization_data"]
    }
)