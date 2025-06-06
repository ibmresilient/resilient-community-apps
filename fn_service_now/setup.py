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
    display_name="ServiceNow",
    version="2.3.1",
    license="MIT",
    author="IBM SOAR",
    url="https://ibm.com/mysupport",
    description="Bi-directional synchronization of Incidents, Tasks, Notes, and Attachments with ServiceNow",
    long_description="""- Create an IBM SOAR Incident/Task from a ServiceNow Record in the Incident Table or Security Incident Table.<br>
        - Create a ServiceNow Record in the Incident Table or Security Incident Table from an IBM SOAR Incident/Task.<br>
        - Create child ServiceNow Records in the Incident Table or Security Response Task Table from an IBM SOAR Task.<br>
        - Sync notes between a related IBM SOAR Incident/Task and a ServiceNow Record.<br>
        - Send Attachments from an IBM SOAR Incident/Task to a related ServiceNow Record.<br>

        <ul><a target='blank' href='https://ibm.biz/res-snow-docs'>Documentation</a></ul>
        <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
        <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        "resilient_circuits>=51.0.2.0"
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
            f"{snake_to_camel(get_module_name(filename))}FunctionComponent = fn_service_now.components.{get_module_name(filename)}:FunctionComponent" for filename in glob.glob("./fn_service_now/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_service_now.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_service_now.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_service_now.util.selftest:selftest_function"]
    }
)
