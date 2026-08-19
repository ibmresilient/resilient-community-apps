#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

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
    name='fn_xforce',
    version='1.1.0',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url="https://ibm.com/mysupport",
    description="IBM SOAR Components for the IBM XForce Collections API",
    long_description="The fn_xforce integration provides the ability to query the IBM XForce Collections API. "
                     "Collections can be queried either by matching a provided search term or by Collection ID. "
                     "Additionally, it is possible to query both public and private Collections. "
                     "Information gathered from X-Force can be used for incident and artifact enrichment.",
    install_requires=[
        'resilient_circuits>=45.0.0'
    ],
    python_requires='>=3.6',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_xforce.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_xforce/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_xforce.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_xforce.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_xforce.util.selftest:selftest_function"]
    }
)