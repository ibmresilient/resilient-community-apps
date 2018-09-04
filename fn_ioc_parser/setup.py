#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
from setuptools import setup, find_packages

PUBLISH_VERSION = "1.0.0"


setup(
    name='fn_ioc_parser',
    version=PUBLISH_VERSION,
    url='https://github.com/ibmresilient/resilient-community-apps',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'IOC_parser' function",
    long_description="Resilient Circuits Components for 'IOC_parser' function",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'ioc_parser'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "IocParserFunctionComponent = fn_ioc_parser.components.ioc_parser:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ioc_parser.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ioc_parser.util.customize:customization_data"]
    }
)