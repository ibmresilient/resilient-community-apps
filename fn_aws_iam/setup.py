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
    name='fn_aws_iam',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient Support',
    author_email='',
    url='https://ibm.com/mysupport',
    description="Amazon AWS IAM Integration for Resilient",
    long_description="Integration with Amazon AWS IAM to facilitate manual enrichment and targeted remediation actions. "
                     "Teams can investigate an attack by searching for AWS user accounts across an AWS environment, and "
                     "quickly respond to attacks by executing remediation actions, such as removing permissions or "
                     "login profiles for suspicious accounts from within the Resilient platform.",
    install_requires=[
        'resilient_circuits>=33.0.0',
        'resilient_lib>=33.0.0',
        'boto3>=1.10.6'
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
            "{}FunctionComponent = fn_aws_iam.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_aws_iam/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_aws_iam.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_aws_iam.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_aws_iam.util.selftest:selftest_function"]
    }
)