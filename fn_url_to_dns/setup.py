#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_url_to_dns',
    version='1.1.0',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_url_to_dns'",
    long_description="Resilient Circuits Components for 'fn_url_to_dns'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "UrlToDnsFunctionComponent = fn_url_to_dns.components.funct_url_to_dns:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_url_to_dns.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_url_to_dns.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_url_to_dns.util.selftest:selftest_function"]
    }
)