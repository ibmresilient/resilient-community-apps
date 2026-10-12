#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

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
    name="fn_algosec",
    display_name="IBM SOAR integration for AlgoSec",
    version="2.0.0",
    license="MIT",
    author="IBM QRadar SOAR",
    author_email="resil.labs@gmail.com",
    url="https://github.com/ibmresilient/resilient-community-apps",
    description="IBM SOAR integration for AlgoSec",
    long_description="""This integration allows one to make a traffic change request, get the details of a traffic change request, or a traffic simulation query.""",
    install_requires=[
        "resilient-circuits>=51.0.0"
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
            "{}FunctionComponent = fn_algosec.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_algosec/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_algosec.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_algosec.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_algosec.util.selftest:selftest_function"]
    }
)
