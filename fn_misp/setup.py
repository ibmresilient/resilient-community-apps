#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_misp',
    version='1.0.1',
    license='Apache 2.0',
    author='Craig',
    author_email='craig@resilientlab.co.uk',
    url='resilientsystems.com',
    description="Resilient Circuits Components for 'fn_misp'",
    long_description="Resilient Circuits Components for 'fn_misp'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'pymisp>=2.4'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "MispCreateEventFunctionComponent = fn_misp.components.misp_create_event:FunctionComponent",
            "MispCreateSightingFunctionComponent = fn_misp.components.misp_create_sighting:FunctionComponent",
            "MispCreateAttributeFunctionComponent = fn_misp.components.misp_create_attribute:FunctionComponent",
            "MispSearchAttributeFunctionComponent = fn_misp.components.misp_search_attribute:FunctionComponent",
            "MispSightingListFunctionComponent = fn_misp.components.misp_sighting_list:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_misp.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_misp.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_misp.util.selftest:selftest_function"]
    }
)