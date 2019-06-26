#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_pa_panorama',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_pa_panorama'",
    long_description="Resilient Circuits Components for 'fn_pa_panorama'",
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