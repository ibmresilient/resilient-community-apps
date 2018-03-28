#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_splunk_integration',
    version='1.0.0',
    license='Resilient License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_splunk_integration'",
    long_description="Resilient Circuits Components for 'fn_splunk_integration'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'splunk-sdk',
        'requests'
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
            "SplunkSearchFunctionComponent = fn_splunk_integration.components.splunk_search:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_splunk_integration.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_splunk_integration.util.customize:customization_data"]
    }
)