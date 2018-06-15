#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_floss',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    description="Resilient Circuits Components for 'fn_floss'",
    long_description="Resilient Circuits Components for 'fn_floss'",
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