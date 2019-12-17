#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_hibp',
    version='2.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Have I Been Pwned search functions.",
    long_description="Resilient Circuits functions to search for breaches and pastes on email accounts.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib'
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
