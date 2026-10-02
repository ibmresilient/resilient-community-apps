#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.1.824

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
    name="fn_vmware_cbc",
    display_name="VMware Carbon Black Cloud",
    version="1.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="IBM SOAR app for VMware Carbon Black Cloud",
    long_description="""Provide bidirectional synchronization and functions for VMware Carbon Black Cloud<br>

        <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
        <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>
        <ul><a target='blank' href='https://ibmresilient.github.io/resilient-community-apps/fn_vmware_cbc/README.html'>App Documentation</a></ul>""",
    install_requires=[
        "resilient-circuits>=51.0.1.1.0"
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
            "{}FunctionComponent = fn_vmware_cbc.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_vmware_cbc/components/[a-zA-Z]*.py")
        ]
        + [
            "PollerComponent = fn_vmware_cbc.poller.poller:PollerComponent"
          ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_vmware_cbc.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_vmware_cbc.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_vmware_cbc.util.selftest:selftest_function"]
    }
)
