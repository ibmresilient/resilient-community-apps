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
    name="fn_cisco_asa",
    #display_name="Cisco ASA Functions for IBM Security SOAR",
    version="1.0.0",
    license="MIT",
    author="Resilient Labs",
    author_email="resil.labs@gmail.com",
    url="https://github.com/ibmresilient/resilient-community-apps",
    description="Resilient Circuits Components for 'fn_cisco_asa'",
    long_description="""Resilient Circuits Components for 'fn_cisco_asa'""",
    install_requires=[
        "resilient-circuits>=31.0.0",
        "resilient-lib>=39.0.0"
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
            "{}FunctionComponent = fn_cisco_asa.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_cisco_asa/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cisco_asa.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cisco_asa.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_cisco_asa.util.selftest:selftest_function"]
    }
)
