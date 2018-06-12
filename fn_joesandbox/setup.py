#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_joesandbox',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_joesandbox'",
    long_description="Resilient Circuits Components for 'fn_joesandbox'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'jbxapi'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnJoesandboxFunctionComponent = fn_joesandbox.components.fn_joesandbox:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_joesandbox.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_joesandbox.util.customize:customization_data"]
    }
)