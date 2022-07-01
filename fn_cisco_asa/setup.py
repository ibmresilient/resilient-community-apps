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
    display_name="Cisco ASA",
    version="1.1.0",
    license="MIT",
    author="IBM SOAR",
    url='http://ibm.biz/soarcommunity',
    description="IBM SOAR app for Cisco ASA",
    long_description="""IBM SOAR integration with Cisco ASA - Adaptive Security Appliance. Manage Cisco ASA network objects from SOAR.""",
    install_requires=[
        "resilient-circuits>=45.0.0"
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
