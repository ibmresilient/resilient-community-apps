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
    name='fn_exchange_online',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='',
    url='https://ibm.com/mysupport',
    description="Resilient Circuits Components for 'fn_exchange_online'",
    long_description="Resilient Integration with Exchange Online provides the capability to access and manipulate Microsoft Exchange Online messages from Resilient.",
    install_requires=[
        'resilient_circuits>=31.0.0',
        'resilient_lib'
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
            "{}FunctionComponent = fn_exchange_online.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_exchange_online/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_exchange_online.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_exchange_online.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_exchange_online.util.selftest:selftest_function"]
    }
)