#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

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
    name="fn_wiz",
    display_name="Wiz",
    version="1.1.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="IBM SOAR app for synchronization with Wiz issue, project, and vulnerability data",
    long_description="""Synchronize IBM SOAR cases with Wiz issues and enrich cases with project and vulnerability data.
This app creates, updates, and closes SOAR cases based on Wiz Issues. Updates Wiz issues based on changes to corresponding SOAR cases.
<br>
Links: 
<ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
<ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        "resilient-circuits>=51.0.1.0.0"
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
            "{}FunctionComponent = fn_wiz.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_wiz/components/[a-zA-Z]*.py")
        ]
        + [
            "PollerComponent = fn_wiz.poller.poller:PollerComponent"
          ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_wiz.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_wiz.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_wiz.util.selftest:selftest_function"]
    }
)
