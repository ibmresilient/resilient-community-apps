#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
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
    name='fn_mcafee_tie',
    version="1.1.0",
    license='MIT',
    author='IBM Resilient',
    author_email='',
    url='https://ibm.com/mysupport',
    description="Resilient Circuits Components for McAfee TIE Functions",
    long_description="Provides the ability to search McAfee Threat Intelliegence Exchange (TIE) server for information on a specific file hash from Resilient",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib',
        'PySocks<1.7',
        'dxlclient',
        'dxltieclient'
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
            "{}FunctionComponent = fn_mcafee_tie.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_mcafee_tie/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee_tie.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee_tie.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_mcafee_tie.util.selftest:selftest_function"]
    }
)