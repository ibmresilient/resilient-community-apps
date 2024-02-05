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
    name="fn_network_utilities",
    display_name="Network Utilities functions for SOAR",
    version="1.1.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="Useful network related workflow/playbook functions for common automation and integration activities in the SOAR platform.",
    long_description="""This app contains useful functions that allows your workflows/playbooks to execute shell-scripts remotely and locally,
     gain information about URLs, and extract SSL certificates from URLs.""",
    install_requires=[
        'resilient-circuits',
        'pyOpenSSL',
        'cryptography',
        'pywinrm',
        'paramiko',
        'chardet'
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_network_utilities.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_network_utilities/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_network_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_network_utilities.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_network_utilities.util.selftest:selftest_function"]
    }
)