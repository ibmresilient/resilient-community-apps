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
    name='fn_pa_panorama',
    version='1.3.0',
    license='MIT',
    author='IBM SOAR',
    description="SOAR Components to Integrate with the Panorama Platform",
    long_description="This integration contains Functions to interact with address groups, "
                     "addresses, and user groups within Palo Alto Panorama. This integration can be"
                     " configured to work with one or multiple Jira instances.",
    install_requires=[
        'resilient_circuits>=48.0.0',
        'resilient-lib>=48.0.0',
        'xmltodict>=0.12.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_pa_panorama.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_pa_panorama/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_pa_panorama.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_pa_panorama.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_pa_panorama.util.selftest:selftest_function"]
    }
)