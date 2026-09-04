#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.

from setuptools import setup, find_packages

setup(
    name='fn_floss',
    version='1.0.0',
    url='https://github.com/ibmresilient/resilient-community-apps',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'fn_floss'",
    long_description="fn_floss package contains a function that extracts obfuscated strings from a binary. Also included are workflows that call floss on artifact and attachment files and create a note containing the extracted strings.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'vivisect>=0.0.20170525',
        'floss>=1.5.1'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnFlossFunctionComponent = fn_floss.components.function_floss:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_floss.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_floss.util.customize:customization_data"]
    }
)
