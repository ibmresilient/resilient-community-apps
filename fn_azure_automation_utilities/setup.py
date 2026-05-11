#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

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
    name="fn_azure_automation_utilities",
    display_name="Azure Automation Utilities",
    version="1.0.0",
    license="MIT",
    author="IBM QRadar SOAR",
    url="https://ibm.com/mysupport",
    description="IBM SOAR App for Azure Automation",
    long_description="""This app allows interaction with the following Azure Automation resources:\n
    - Automation Accounts
    - Activities
    - Jobs
    - Runbooks
    - Nodes
    - Credentials
    - Schedules
    - Modules
    - Agent Registration
    - Statistics""",
    install_requires=[
        "resilient-circuits>=48.0.0"
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_azure_automation_utilities.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_azure_automation_utilities/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_azure_automation_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_azure_automation_utilities.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_azure_automation_utilities.util.selftest:selftest_function"]
    }
)
