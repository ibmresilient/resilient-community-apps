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
    name='fn_teams',
    display_name="Microsoft Teams",
    version='2.0.0',
    license='MIT License',
    author='IBM SOAR',
    author_email='',
    url='https://ibm.biz/soarcommunity',
    description="This package extends the collaboration functionality of Microsoft Teams to IBM Security QRadar SOAR Platform",
    long_description='''This package provides SOAR platform with the ability to interface with Microsoft Teams and create groups and channels.
    Included are example workflows and rules for pushing incident and task information to a Teams channel and to create a group and channel from
    within an incident or task''',
    install_requires=[
        "resilient_circuits>=45.0.0",
        "pymsteams ~= 0.2.1;python_version>='3.6'",
        "msal ~= 1.19;python_version>='3.5'"
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_teams.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_teams/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_teams.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_teams.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_teams.util.selftest:selftest_function"]
    }
)
