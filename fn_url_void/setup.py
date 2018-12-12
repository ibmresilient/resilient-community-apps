#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_url_void',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_url_void'",
    long_description="Resilient Circuits Components for 'fn_url_void'",
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
            "UrlVoidRetriveInformationFunctionComponent = fn_url_void.components.url_void_retrive_information:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_url_void.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_url_void.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_url_void.util.selftest:selftest_function"]
    }
)