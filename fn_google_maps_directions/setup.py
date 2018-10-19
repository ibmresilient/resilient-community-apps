# (c) Copyright IBM Corp. 2018. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_google_maps_directions',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for Google Maps Directions Function",
    long_description="This package contains one function that generates a link to Google Maps which shows directions from the given origin to the destination",
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
            "FnGoogleMapsDirectionsFunctionComponent = fn_google_maps_directions.components.fn_google_maps_directions:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_google_maps_directions.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_google_maps_directions.util.customize:customization_data"]
    }
)