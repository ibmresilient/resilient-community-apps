#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_utilities_strings_from_binary',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient ',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_utilities_strings_from_binary'",
    long_description="Resilient Circuits Components for 'fn_utilities_strings_from_binary'",
    install_requires=[
        'resilient_circuits>=30.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "UtilitiesStringsFromBinaryFunctionComponent = fn_utilities_strings_from_binary.components.utilities_strings_from_binary:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_utilities_strings_from_binary.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_utilities_strings_from_binary.util.customize:customization_data"]
    }
)