#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_qradar_advisor',
    version='2.0.0',
    license='MIT License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_qradar_advisor'",
    long_description="fn_qradar_advisor supports QRadar Advisor quick search, full search, map a rule, and retrieve offense insights and analysis",
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
            "QradarAdvisorMapRuleFunctionComponent = fn_qradar_advisor.components.qradar_advisor_map_rule:FunctionComponent",
            "QradarAdvisorOffenseAnalysisFunctionComponent = fn_qradar_advisor.components.qradar_advisor_offense_analysis:FunctionComponent",
            "QradarAdvisorQuickSearchFunctionComponent = fn_qradar_advisor.components.qradar_advisor_quick_search:FunctionComponent",
            "QradarAdvisorFullSearchFunctionComponent = fn_qradar_advisor.components.qradar_advisor_full_search:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_qradar_advisor.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_qradar_advisor.util.customize:customization_data"]
    }
)