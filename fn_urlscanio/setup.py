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
    name='fn_urlscanio',
    version='1.1.0',
    license='MIT',
    author='IBM Resilient',
    url='http://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for 'fn_urlscanio'",
    long_description="Resilient Circuits Components for 'fn_urlscanio'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient_lib>32.0.0'
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
            "{}FunctionComponent = fn_urlscanio.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_urlscanio/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_urlscanio.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_urlscanio.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_urlscanio.util.selftest:selftest_function"]
    }
)