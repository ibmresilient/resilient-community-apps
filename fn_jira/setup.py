#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_jira',
    version='2.0.0',
    license='MIT',
    author='IBM Resilient',
    url='https://ibm.com/mysupport',
    description="Provides integration with JIRA for Issue Creation, Issue Transition and Comment Creation",
    long_description="""This app allows for the tracking of Resilient Incidents and Tasks as Jira Issues. Bidirectional links are saved to allow for easy navigation between the applications.

It also allows for the transitioning of Jira issues when the corresponding incident is closed and adds comments to the Jira issue when a Note is created in Resilient.

Example rules and workflows can used used or modified to meet your business processes.
""",
    install_requires=[
        'resilient_circuits>=32.0.0',
        'resilient-lib>=38.0.0',
        'jira>=2.0.0'
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
