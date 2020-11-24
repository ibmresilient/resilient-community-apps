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
    name="fn_aws_guardduty",
    version="1.0.0",
    license="MIT",
    author="IBM Resilient",
    author_email="support@resilientsystems.com",
    description="Resilient Circuits Components for 'fn_aws_guardduty'",
    long_description="""Resilient Circuits Components for 'fn_aws_guardduty'""",
    install_requires=[
        'resilient_circuits>=35.0.0',
        'resilient_lib>=35.0.0',
        'boto3>=1.16.19'
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
            "FuncAwsGuarddutyPoller = fn_aws_guardduty.components.func_aws_guardduty_poller:FuncAwsGuarddutyPoller"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_aws_guardduty.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_aws_guardduty.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_aws_guardduty.util.selftest:selftest_function"]
    }
)
