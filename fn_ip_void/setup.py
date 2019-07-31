#!/usr/bin/env python
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from setuptools import setup, find_packages

setup(
    name='fn_ip_void',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="A Resilient Function to integrate with the IPVOID API",
    long_description="Integrates with IPVOID's vast range of IP Address tools to discover details about IP address helping you get enriched information about a Resilient Artifact",
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
            "FnIpVoidRequestFunctionComponent = fn_ip_void.components.fn_ip_void_request:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ip_void.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ip_void.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ip_void.util.selftest:selftest_function"]
    }
)