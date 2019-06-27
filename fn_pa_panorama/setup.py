#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_pa_panorama',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url='www.resilientsystems.com',
    description="Resilient Circuits Components to Integrate with the Panorama Platform",
    long_description="Contains Functions to get and edit addresses groups, get and create addresses, and get and edit users in a group within Panorama.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>32.0.0.140',
        'xmltodict'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "PanoramaEditAddressGroupFunctionComponent = fn_pa_panorama.components.panorama_edit_address_group:FunctionComponent",
            "PanoramaGetAddressGroupsFunctionComponent = fn_pa_panorama.components.panorama_get_address_groups:FunctionComponent",
            "PanoramaGetAddressesFunctionComponent = fn_pa_panorama.components.panorama_get_addresses:FunctionComponent",
            "PanoramaCreateAddressesFunctionComponent = fn_pa_panorama.components.panorama_create_address:FunctionComponent",
            "PanoramaGetUsersInAGroupFunctionComponent = fn_pa_panorama.components.panorama_get_users_in_a_group:FunctionComponent",
            "PanoramaEditUsersInAGroupFunctionComponent = fn_pa_panorama.components.panorama_edit_users_in_a_group:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_pa_panorama.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_pa_panorama.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_pa_panorama.util.selftest:selftest_function"]
    }
)