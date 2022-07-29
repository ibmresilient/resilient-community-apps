#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_qradar_advisor',
    display_name="QRadar Advisor Functions",
    version='2.1.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='https://ibm.com/mysupport',
    description="IBM SOAR QRadar Advisor Functions",
    long_description="The QRadar Advisor integration with IBM QRadar SOAR enables SOAR users to gather Cyber "
                     "Threat Intelligence(CTI) data from IBM Watson and QRadar. In addition, the integration receives "
                     "MITRE ATT&CK information from QRadar Advisor. The integration supports QRadar Advisor quick search, "
                     "full search, map a rule, and retrieve offense insights and analysis.",
    install_requires=[
        'resilient_circuits>=44.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "QradarAdvisorMapRuleFunctionComponent = fn_qradar_advisor.components.qradar_advisor_map_rule:FunctionComponent",
            "QradarAdvisorOffenseAnalysisFunctionComponent = fn_qradar_advisor.components.qradar_advisor_offense_analysis:FunctionComponent",
            "QradarAdvisorQuickSearchFunctionComponent = fn_qradar_advisor.components.qradar_advisor_quick_search:FunctionComponent",
            "QradarAdvisorFullSearchFunctionComponent = fn_qradar_advisor.components.qradar_advisor_full_search:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_qradar_advisor.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_qradar_advisor.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_qradar_advisor.util.selftest:selftest_function"]
    }
)