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
    name='fn_service_now',
    display_name="ServiceNow App",
    version="2.0.8",
    license="MIT",
    author="IBM SOAR",
    url="https://ibm.com/mysupport",
    description="Bi-directional synchronization of Incidents, Tasks, Notes and Attachments with ServiceNow",
    long_description="""- Create an IBM SOAR Incident/Task from a ServiceNow Record in the Incident Table or Security Incident Table.<br>
        - Create a ServiceNow Record in the Incident Table or Security Incident Table from an IBM SOAR Incident/Task.<br>
        - Sync notes between a related IBM SOAR Incident/Task and a ServiceNow Record.<br>
        - Send Attachments from an IBM SOAR Incident/Task to a related ServiceNow Record.""",
    install_requires=[
        "resilient_circuits>=43.0.0",
        "beautifulsoup4>=4.6.3"
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_service_now.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_service_now/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_service_now.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_service_now.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_service_now.util.selftest:selftest_function"]
    }
)
