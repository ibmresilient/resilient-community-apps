#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

from setuptools import setup, find_packages

setup(
    name='fn_thug',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_thug'",
    long_description="Resilient Circuits Components for 'fn_thug'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'docker'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "ThugAnalysisFunctionComponent = fn_thug.components.thug_analysis:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_thug.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_thug.util.customize:customization_data"]
    }
)