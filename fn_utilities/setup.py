#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import glob
import ntpath
import sys

PACKAGE='fn_utilities'

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
    display_name='Utility Functions for SOAR',
    version='2.1.0',
    license='MIT',
    author='IBM SOAR',
    author_email='support@resilientsystems.com',
    url="http://ibm.biz/soarcommunity",
    description="Useful workflow functions for common automation and integration activities in the SOAR platform.",
    long_description="""SOAR functions simplify development of integrations by wrapping each external activity
    into an individual workflow component. These components can be easily installed, then used and combined in SOAR
    workflows. The SOAR platform sends data to the function component that performs an activity then returns the results
    to the workflow. The results can be acted upon by scripts, rules, and workflow decision points to dynamically orchestrate
    the security incident response activities.""",
    setup_requires=['six==1.14.0'],
    install_requires=[
        'six==1.14.0',
        'resilient_circuits>=30.0.0',
        'resilient-lib>=34.0.0',
        'openpyxl>=2.5.3',
        'pyOpenSSL>=18.0.0',
        'cryptography>=2.3',
        'pywinrm>=0.3.0',
        'json2html',
        'lxml',
        'mail-parser>=3.9.3',
        'paramiko',
        'defusedxml>=0.7.1',
        'pdfid>=1.0.4',
        'chardet==4.0.0'
    ],
    packages=find_packages(),
    python_requires='>=3',
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_utilities.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_utilities/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_utilities.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_utilities.util.selftest:selftest_function"]
    }
)
