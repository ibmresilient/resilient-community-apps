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
    name='fn_odbc_query',
    display_name='ODBC Functions for SOAR',
    version='1.1.0',
    license='MIT',
    author='IBM QRadar SOAR',
    url="http://ibm.biz/resilientcommunity",
    description="SOAR Components for 'fn_odbc_query'",
    long_description="ODBC Functions for SOAR",
    install_requires=[
        'resilient_circuits>=43.0.0',
        'pyodbc~=4.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_odbc_query.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_odbc_query/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_odbc_query.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_odbc_query.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_odbc_query.util.selftest:selftest_function"]
    }
)
