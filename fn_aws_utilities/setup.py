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
    name="fn_aws_utilities",
    display_name="AWS Utilities",
    version="1.1.0",
    license="MIT",
    author="IBM SOAR",
    author_email="",
    url="http://ibm.biz/soarcommunity",
    description="Resilient Circuits Components for 'fn_aws_utilities'",
    long_description="Resilient Circuits Components for 'fn_aws_utilities'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'boto3'
    ],
    # python_requires='>=3',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "{}FunctionComponent = fn_aws_utilities.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_aws_utilities/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_aws_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_aws_utilities.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_aws_utilities.util.selftest:selftest_function"]
    }
)