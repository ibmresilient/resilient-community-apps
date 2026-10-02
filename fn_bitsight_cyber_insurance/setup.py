#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

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
    name="fn_bitsight_cyber_insurance",
    display_name="BitSight Cyber Insurance",
    version="1.0.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="https://ibm.com/mysupport",
    description="BitSight Cyber Insurance for IBM SOAR",
    long_description="""BitSight Cyber Insurance for IBM SOAR
    This integration provides the following functions:
    - Get Alerts
    - Get Company Details
    - Get Company Search
    - Get Finding Details
    - Get latest Alerts
    - Get Portfolio Details
    - Get Rapid Underwriting Assessments
    <br>
    Links:
    <ul><a target='blank' href='https://ibm.com/mysupport'>Support</a></ul>
    <ul><a target='blank' href='https://ideas.ibm.com/'>Enhancement Requests</a></ul>""",
    install_requires=[
        "resilient-circuits>=51.0.0.0.0"
    ],
    python_requires='>=3.9',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = fn_bitsight_cyber_insurance.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_bitsight_cyber_insurance/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = fn_bitsight_cyber_insurance.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_bitsight_cyber_insurance.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_bitsight_cyber_insurance.util.selftest:selftest_function"]
    }
)
