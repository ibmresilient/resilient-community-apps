#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_urlscanio',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='info@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_urlscanio'",
    long_description="Resilient Circuits Components for 'fn_urlscanio'",
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
            "UrlscanioFunctionComponent = fn_urlscanio.components.urlscanio:FunctionComponent",
        ],
        "resilient.circuits.configsection": ["gen_config = fn_urlscanio.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_urlscanio.util.customize:customization_data"]
    }
)