#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_urlhaus',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_urlhaus'",
    long_description="""Resilient Circuits Components for 'fn_urlhaus'. Supported is inqueries on ip addresses, hashes and domains
              and submissions on malware distributing urls""",
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
            "UrlHausFunctionComponent = fn_urlhaus.components.func_urlhaus:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_urlhaus.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_urlhaus.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_urlhaus.util.selftest:selftest_function"]
    }
)