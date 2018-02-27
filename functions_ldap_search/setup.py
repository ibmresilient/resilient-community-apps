#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='functions_ldap_search',
    version='1.0.0',
    license='Resilient License',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'functions_ldap_search'",
    long_description="Resilient Circuits Components for 'functions_ldap_search'",
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
            "LdapSearchFunctionComponent = functions_ldap_search.components.ldap_search:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = functions_ldap_search.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = functions_ldap_search.util.customize:customization_data"]
    }
)