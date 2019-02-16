#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mitre_integration',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_mitre_integration'",
    long_description="Resilient Circuits Components for 'fn_mitre_integration'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'stix2',
        'taxii2client'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "MitreTechniqueInformationFunctionComponent = fn_mitre_integration.components.mitre_technique_information:FunctionComponent",
            "MitreTacticInformationFunctionComponent = fn_mitre_integration.components.mitre_tactic_information:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mitre_integration.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mitre_integration.util.customize:customization_data"]
    }
)