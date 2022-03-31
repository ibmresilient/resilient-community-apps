#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import glob
import ntpath

def get_module_name(module_path):
    """
    Return the module name of the module path
    """
    return ntpath.split(module_path)[1].split(".")[0]


def snake_to_camel(word):
    """
    Convert a word from snake_case to CamelCase
    """
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

setup(
    name='fn_jira',
    display_name='Jira App for IBM SOAR',
    version='2.1.0',
    license='MIT',
    author='IBM SOAR',
    url='https://ibm.com/mysupport',
    description="Provides integration with JIRA for Issue Creation, Issue Transition and Comment Creation",
    long_description="""This app allows for the tracking of SOAR Incidents and Tasks as Jira Issues. Bidirectional links are saved to allow for easy navigation between the applications.

It also allows for the transitioning of Jira issues when the corresponding incident is closed and adds comments to the Jira issue when a Note is created in SOAR.

Example rules and workflows can used used or modified to meet your business processes.
""",
    install_requires=[
        'resilient_circuits>=44.0.0',
        'jira>=3.1; python_version>="3.0"',
        'jira>=2.0; python_version<"3.0"',
        'pyjwt~=2.3; python_version>="3.0"',
        'pyjwt~=1.7; python_version<"3.0"'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_jira.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_jira/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_jira.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_jira.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_jira.util.selftest:selftest_function"]
    }
)
