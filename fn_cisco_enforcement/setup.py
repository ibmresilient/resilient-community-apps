#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_cisco_enforcement',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_cisco_enforcement'",
    long_description="Resilient Circuits Components for 'fn_cisco_enforcement'",
    install_requires=[
        'resilient_circuits>=30.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "CiscoGetDomainsFunctionComponent = fn_cisco_enforcement.components.get_domains:FunctionComponent",
            "CiscoPostEventFunctionComponent = fn_cisco_enforcement.components.event:FunctionComponent",
            "CiscoDeleteDomainFunctionComponent = fn_cisco_enforcement.components.delete_domain:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cisco_enforcement.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cisco_enforcement.util.customize:customization_data"]
    }
)
