#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_sndbox_analyzer',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits SNDBOX Analyzer Functions",
    long_description="Resilient Circuits SNDBOX Analyzer Functions that submits an attached file to SNDBOX Cloud for Malware analysis and returns the results in an incident note. ",
    install_requires=[
        'resilient_circuits>=31.0.0',
        'resilient-lib>=32.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnSNDBOXSandboxAnalyzerFunctionComponent = fn_sndbox_analyzer.components.fn_sndbox_sandbox_analyzer:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_sndbox_analyzer.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_sndbox_analyzer.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_sndbox_analyzer.util.selftest:selftest_function"]
    }
)