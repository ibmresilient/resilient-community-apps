#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
     name='fn_isitPhishing',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Function that queries isitPhishing.org API to analyze a URL or an HTML document",
    long_description="Resilient Circuits Function that queries isitPhishing.org API to analyze a URL or an HTML document",
    install_requires=[
        'resilient_circuits>=31.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "IsitphishingUrlFunctionComponent = fn_isitPhishing.components.isitphishing_url:FunctionComponent",
            "IsitphishingHtmlDocumentFunctionComponent = fn_isitPhishing.components.isitphishing_html_document:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_isitPhishing.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_isitPhishing.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_isitPhishing.util.selftest:selftest_function"]
    }
)
