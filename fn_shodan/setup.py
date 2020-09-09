#!/usr/bin/env python
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
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
    name="fn_shodan",
    version="2.0.0",
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://ibm.biz/resilientcommunity',
    description="A function to lookup IP Addresses in Shodan",
    long_description="""This is a simple function which takes IP Address artifacts and returns the results from https://www.shodan.io/.
It will update the description of the artifact and add a note to the incident with the Vulnerabilities, Ports and more from Shodan.
You will need an API key for Shodan - https://developer.shodan.io/billing/signup
""",
    install_requires=[
        "resilient_circuits>=33.0.0",
        "resilient-lib>=37.2.215",
        "shodan>=1.23.0"
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_shodan.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_shodan/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_shodan.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_shodan.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_shodan.util.selftest:selftest_function"]
    }
)
