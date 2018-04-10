#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_pagerduty',
    version='1.0.0',
    license='MIT',
    author='Resilient',
    author_email='support@resilient.com',
    description="Resilient Circuits Components for 'fn_pagerduty'",
    long_description="Resilient Circuits Components for 'fn_pagerduty'",
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
            "PagerdutyCreateIncidentFunctionComponent = fn_pagerduty.components.pd_create_incident:FunctionComponent",
            "PagerdutyTransitionIncidentFunctionComponent = fn_pagerduty.components.pd_transition_incident:FunctionComponent",
            "PagerdutyCreateNoteFunctionComponent = fn_pagerduty.components.pd_create_note:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_pagerduty.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_pagerduty.util.customize:customization_data"]
    }
)
