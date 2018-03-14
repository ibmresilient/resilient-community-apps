#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_jira',
    version='1.0.0',
    license='See License File',
    author='Resilient',
    author_email='support@resilient.com',
    description="Resilient Circuits Components for Jira",
    long_description="Resilient Circuits Components for creating issues, transitions issues and creating comments in Jira",
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
            "JiraOpenIssueFunctionComponent = fn_jira.components.jira_open_issue:FunctionComponent",
            "JiraTransitionIssueFunctionComponent = fn_jira.components.jira_transition_issue:FunctionComponent",
            "JiraCreateCommentFunctionComponent = fn_jira.components.jira_create_comment:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_jira.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_jira.util.customize:customization_data"]
    }

)