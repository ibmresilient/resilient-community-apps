#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_pagerduty',
    version='1.0.0',
    url='https://github.com/ibmresilient/resilient-community-apps',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'fn_pagerduty'",
    long_description="Resilient Circuits Components for 'fn_pagerduty'. Used to create pagerducty incidents, create notes and transition incidents (acknowledged and resolved)",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'beautifulsoup4'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "PagerdutyCreateNoteFunctionComponent = fn_pagerduty.components.pd_create_note:FunctionComponent",
            "PagerdutyTransitionIncidentFunctionComponent = fn_pagerduty.components.pd_transition_incident:FunctionComponent",
            "PagerdutyCreateIncidentFunctionComponent = fn_pagerduty.components.pd_create_incident:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_pagerduty.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_pagerduty.util.customize:customization_data"]
    }
)