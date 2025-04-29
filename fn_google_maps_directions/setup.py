# (c) Copyright IBM Corp. 2018. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    display_name='Google Maps Directions',
    name='fn_google_maps_directions',
    version='1.0.1',
    url='https://ibm.biz/soarcommunity',
    license='MIT',
    author='IBM QRadar SOAR',
    author_email='resil.labs@gmail.com',
    description="IBM SOAR Components for Google Maps Directions Function",
    long_description="This package contains one function that generates a link to Google Maps which shows directions from the given origin to the destination",
    install_requires=[
        'resilient_circuits>=51.0.0'
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
        "resilient.circuits.customize": ["customize = fn_google_maps_directions.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_google_maps_directions.util.selftest:selftest_function"]
    }
)