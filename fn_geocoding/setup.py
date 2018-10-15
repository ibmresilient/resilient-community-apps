#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_geocoding',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for 'fn_geocoding'",
    long_description="Resilient Circuits Components for 'fn_geocoding' implementation of Google Geocoding capabilities. Specifically,"
                     "get an address from latitude/longitude coordinates and get latitude/longitude coordinates from an address.",
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
            "GeocodingFunctionComponent = fn_geocoding.components.geocoding:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_geocoding.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_geocoding.util.customize:customization_data"]
    }
)