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
    name='fn_cisco_umbrella_inv',
    version='1.1.0',
    author='IBM QRadar SOAR',
    description="IBM QRadar SOAR Integration for Cisco Umbrella Investigate",
    long_description="The Cisco Umbrella Investigate integration with the SOAR platform allows for the querying of a "
                     "Cisco Umbrella Investigate deployment. The integration includes 14 functions that return results "
                     "which show security events and correlations. The results can be used to make customized updates "
                     "to the SOAR platform, such as updating incidents, data tables and so on.",
    install_requires=[
        'resilient_circuits>=51.0.0',
        'resilient-lib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_cisco_umbrella_inv.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_cisco_umbrella_inv/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cisco_umbrella_inv.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cisco_umbrella_inv.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_cisco_umbrella_inv.util.selftest:selftest_function"]
    }
)