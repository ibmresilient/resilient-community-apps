#!/usr/bin/env python
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
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
    name='fn_ldap_utilities',
    version='2.0.0',
    license='MIT',
    display_name='SOAR LDAP Utilities',
    author='IBM SOAR',
    description="SOAR LDAP Utilities'",
    url='https://github.com/ibmresilient/resilient-community-apps',
    long_description="SOAR components to allow reading and manipulation of your LDAP Server'",
    install_requires=[
        'resilient_circuits>=42.0.0',
        'ldap3>=2.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_ldap_utilities.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_ldap_utilities/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ldap_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ldap_utilities.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ldap_utilities.util.selftest:selftest_function"]
    }
)
