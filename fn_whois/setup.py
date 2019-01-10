#!/usr/bin/env python
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_whois',
    version='1.0.0',
    license='MIT',
    author='Ryan',
    author_email='ryan@resilientlab.co.uk',
    description="Resilient Circuits Components which provide an interface for searching the WHOIS database",
    long_description="A Resilient Circuits function which takes in an input of URL/IP and then attempts to gather registrar information by sending a WHOIS query",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'python-whois'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "WhoisQueryFunctionComponent = fn_whois.components.whois_query:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_whois.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_whois.util.customize:customization_data"]
    }
)