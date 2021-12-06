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
    name='fn_qradar_enhanced_data',
    version='1.1.3',
    license='MIT License',
    author='IBM SOAR',
    url='https://github.com/ibmresilient/resilient-community-apps/tree/master/fn_qradar_enhanced_data',
    description="QRadar Enhanced Offense Data Migration ",
    long_description="This app fetches the data associated with the QRadar Offense and provides live links back to QRadar, thereby simplifying case management.",

    install_requires=[
        'resilient_circuits>=41.1.0'
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
            "{}FunctionComponent = fn_qradar_enhanced_data.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_qradar_enhanced_data/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_qradar_enhanced_data.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_qradar_enhanced_data.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_qradar_enhanced_data.util.selftest:selftest_function"]
    }
)