#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_jira',
    version='1.0.2',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url='https://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for 'fn_jira'",
    long_description="Resilient Circuits Components for 'fn_jira'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>=32.0.140',
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
            "JiraOpenIssueFunctionComponent = fn_jira.components.jira_open_issue:FunctionComponent",
            "JiraTransitionIssueFunctionComponent = fn_jira.components.jira_transition_issue:FunctionComponent",
            "JiraCreateCommentFunctionComponent = fn_jira.components.jira_create_comment:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_jira.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_jira.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_jira.util.selftest:selftest_function"]
    }
)
