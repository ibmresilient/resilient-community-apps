#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_qradar_advisor',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_qradar_advisor'",
    long_description="Resilient Circuits Components for 'fn_qradar_advisor'",
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
            "QradarAdvisorOffenseAnalysisFunctionComponent = fn_qradar_advisor.components.qradar_advisor_offense_analysis:FunctionComponent",
            "QradarAdvisorQuickSearchFunctionComponent = fn_qradar_advisor.components.qradar_advisor_quick_search:FunctionComponent",
            "QradarAdvisorFullSearchFunctionComponent = fn_qradar_advisor.components.qradar_advisor_full_search:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_qradar_advisor.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_qradar_advisor.util.customize:customization_data"]
    }
)