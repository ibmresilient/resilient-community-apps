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
    name='fn_resilient_ml',
    version='1.0.0',
    license='MIT License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url='https://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for 'fn_resilient_ml'",
    long_description="fn_resilient_ml supports NLP search for finding most similar incidents",
    install_requires=[
        'resilient_circuits>=30.0.0'
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
            "{}FunctionComponent = fn_resilient_ml.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_resilient_ml/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_resilient_ml.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_resilient_ml.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_resilient_ml.util.selftest:selftest_function"]
    }
)