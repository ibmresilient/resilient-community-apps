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
    name='fn_slack',
    display_name='Slack Integration for SOAR',
    version='1.1.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url='https://ibm.com/mysupport',
    description="SOAR Components for 'fn_slack'",
    long_description="Function creates a Slack message based on a Resilient Incident, it's Tasks, Notes, Artifacts "
                     "and Attachments, exports conversation history from Slack channel to a text file, saves the "
                     "text file as an Attachment and archives the Slack channel.",
    install_requires=[
        'resilient_circuits>=45.0.0',
        'slackclient~=2.9.4'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_slack.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_slack/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_slack.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_slack.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_slack.util.selftest:selftest_function"]
    }
)