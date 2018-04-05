#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mcafee_atd',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_mcafee_atd'",
    long_description="Resilient Circuits Components for 'fn_mcafee_atd'",
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
            "McafeeAtdAnalyzeFileFunctionComponent = fn_mcafee_atd.components.mcafee_atd_analyze_file:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee_atd.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee_atd.util.customize:customization_data"]
    }
)