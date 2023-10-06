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
    name='fn_bigfix',
    display_name="BigFix Integration for SOAR",
    version='1.2.0',
    license='MIT License',
    author='IBM SOAR',
    description="SOAR Components for BigFix",
    long_description="""BigFix is a systems-management platform for managing a large numbers of endpoints.
        The BigFix integration with the SOAR platform allows for the querying and updating of a BigFix deployment. 
        The integration includes a function to query for IOCs in the BigFix environment. Returned results can be used 
        to remediate issues or hits, such as a malicious path or filename,  a service or process name, or a registry 
        key. The integration can also be used to query properties of an endpoint.""",
    python_requires='>=3.6',
    install_requires=[
        'resilient_circuits>=43.0.0'
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
            "{}FunctionComponent = fn_bigfix.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_bigfix/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_bigfix.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_bigfix.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_bigfix.util.selftest:selftest_function"]
    }
)
