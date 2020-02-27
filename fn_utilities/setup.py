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
    name='fn_utilities',
    version='1.0.11',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url="http://ibm.biz/resilientcommunity",
    description="Useful workflow functions for common automation and integration activities in the Resilient platform.",
    long_description="""Resilient functions simplify development of integrations by wrapping each external activity
    into an individual workflow component. These components can be easily installed, then used and combined in Resilient
    workflows. The Resilient platform sends data to the function component that performs an activity then returns the results
    to the workflow. The results can be acted upon by scripts, rules, and workflow decision points to dynamically orchestrate
    the security incident response activities.""",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>=34.0.0',
        'openpyxl<=2.5.14',
        'pyOpenSSL>=18.0.0',
        'cryptography>=2.3',
        'pywinrm>=0.3.0',
        'json2html',
        'lxml',
        'mail-parser>=3.9.3'
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
            "{}FunctionComponent = fn_utilities.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_utilities/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_utilities.util.customize:customization_data"]
    }
)
