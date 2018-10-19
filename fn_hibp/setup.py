#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_hibp',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_hibp'",
    long_description="Resilient Circuits Components for 'fn_hibp'",
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
            "HaveIBeenPwnedGetBreachesFunctionComponent = fn_hibp.components.have_i_been_pwned_get_breaches:FunctionComponent",
            "HaveIBeenPwnedGetPastesFunctionComponent = fn_hibp.components.have_i_been_pwned_get_pastes:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_hibp.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_hibp.util.customize:customization_data"]
    }
)