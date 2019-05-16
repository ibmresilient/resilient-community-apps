#!/usr/bin/env python
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_falcon_sandbox',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_falcon_sandbox'",
    long_description="Resilient Circuits Components for 'fn_falcon_sandbox'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient_lib>=30.0.0',
        'requests_toolbelt>=0.9.0'

    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FalconSandboxSubmitFileFunctionComponent = fn_falcon_sandbox.components.falcon_sandbox_submit_file:FunctionComponent",
            "FalconSandboxSubmitUrlFunctionComponent = fn_falcon_sandbox.components.falcon_sandbox_submit_url:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_falcon_sandbox.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_falcon_sandbox.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_falcon_sandbox.util.selftest:selftest_function"]
    }
)