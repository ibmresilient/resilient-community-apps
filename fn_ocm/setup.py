#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

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
    name="fn_ocm",
    display_name="On Call Manager for IBM SOAR",
    version="1.0.0",
    license='MIT',
    author='IBM SOAR',
    url='https://ibm.com/mysupport',
    description="On Call Manager for IBM SOAR",
    long_description="""This app allows the creation of Events, updating Incidents, retrieving the details of incidents and the details of events in On Call Manager from SOAR.<br>
    Links:
    <br><ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
    <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        "resilient-circuits>=51.0.0.0.0"
    ],
    python_requires='>=3.9',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_ocm.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_ocm/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_ocm.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ocm.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ocm.util.selftest:selftest_function"]
    }
)
