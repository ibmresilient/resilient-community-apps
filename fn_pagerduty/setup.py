#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_pagerduty',
    display_name="PagerDuty App",
    version='1.1.0',
    url='https://ibm.biz/soarcommunity',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    description="IBM SOAR app for PagerDuty integration",
    long_description="An app that integrates SOAR incidents with PagerDuty incidents. Used to create pagerduty incidents from SOAR incidents, as well as automatically creating notes and transitioning incidents (acknowledged and resolved)",
    install_requires=[
        'resilient_circuits>=43.0.0',
        'beautifulsoup4~=4.11.1',
        'pdpyras~=4.5.0',
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "PagerdutyCreateNoteFunctionComponent = fn_pagerduty.components.funct_pagerduty_create_note:FunctionComponent",
            "PagerdutyTransitionIncidentFunctionComponent = fn_pagerduty.components.funct_pagerduty_transition_incident:FunctionComponent",
            "PagerdutyCreateIncidentFunctionComponent = fn_pagerduty.components.funct_pagerduty_create_incident:FunctionComponent",
            "PagerdutyListIncidentsFunctionComponent = fn_pagerduty.components.funct_pagerduty_list_incidents:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_pagerduty.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_pagerduty.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_pagerduty.util.selftest:selftest_function"]
    }
)