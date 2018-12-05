#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_digital_shadows_search',
    version='1.0.1',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="This package contains a function that searches your Digital Shadows platform with the given query",
    long_description="The function makes use of the Digital Shadows `/search/find` API call to get information on a given query",
    install_requires=[
        'resilient_circuits>=30.0.111'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnDigitalShadowsSearchFunctionComponent = fn_digital_shadows_search.components.fn_ds_search:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_digital_shadows_search.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_digital_shadows_search.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_digital_shadows_search.util.selftest:selftest_function"]
    }
)