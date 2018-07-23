#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_ldap_utilities',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_ldap_utilities'",
    long_description="Resilient Circuits Components for 'fn_ldap_utilities'",
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
            "LdapUtilitiesToggleAccessFunctionComponent = fn_ldap_utilities.components.ldap_utilities_toggle_access:FunctionComponent",
            "LdapUtilitiesUpdateFunctionComponent = fn_ldap_utilities.components.ldap_utilities_update:FunctionComponent",
            "LdapUtilitiesRemoveFromGroupsFunctionComponent = fn_ldap_utilities.components.ldap_utilities_remove_from_groups:FunctionComponent",
            "LdapUtilitiesSearchFunctionComponent = fn_ldap_utilities.components.ldap_utilities_search:FunctionComponent",
            "LdapUtilitiesAddToGroupsFunctionComponent = fn_ldap_utilities.components.ldap_utilities_add_to_groups:FunctionComponent",
            "LdapUtilitiesSetPasswordFunctionComponent = fn_ldap_utilities.components.ldap_utilities_set_password:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ldap_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ldap_utilities.util.customize:customization_data"]
    }
)