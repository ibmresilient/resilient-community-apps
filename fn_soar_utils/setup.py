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
    name="fn_soar_utils",
    display_name="SOAR Function Utilities for SOAR",
    version="1.1.0",
    license="MIT",
    author="IBM SOAR",
    url="http://ibm.biz/soarcommunity",
    description="Useful playbook functions for common automation and integration activities in the SOAR platform.",
    long_description="""SOAR functions taken from fn_utilities to simplify development of integrations by wrapping each external activity
    into an individual playbook component. The SOAR Platform sends data from artifacts, attachments, incident data, etc. 
    to the function component and returns results to the playbook. The results can be acted upon by 
    playbook decision points to dynamically orchestrate the security incident response activities.<br>
    Link:
        <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
        <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>
        <ul><a target='blank' href='https://ibmresilient.github.io/resilient-community-apps/fn_soar_utils/README.html'>App Documentation</a></ul>""",
    install_requires=[
        "resilient-circuits>=51.0.0"
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
            f"{snake_to_camel(get_module_name(filename))}FunctionComponent = fn_soar_utils.components.{get_module_name(filename)}:FunctionComponent" for filename in glob.glob("./fn_soar_utils/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_soar_utils.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_soar_utils.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_soar_utils.util.selftest:selftest_function"]
    }
)
