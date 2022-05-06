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
    name='fn_datatable_utils',
    version='1.3.0',
    display_name="Datatable Utils",
    license='MIT',
    author='IBM SOAR',
    url='http://ibm.biz/soarcommunity',
    description="Functions manipulate data in a Datatable",
    long_description="This package contains 6 functions that help you manipulate IBM SOAR Data Tables: Get Row,  Get Rows, Update Row, Delete Row, Delete Rows and Convert CSV Data to a datatable.",
    install_requires=[
        'resilient_circuits>=41.0.0',
        'resilient-lib>=41.0.0'
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_datatable_utils.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_datatable_utils/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_datatable_utils.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_datatable_utils.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_datatable_utils.util.selftest:selftest_function"]
    }
)