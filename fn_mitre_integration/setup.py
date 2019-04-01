#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mitre_integration',
    version='1.0.1',
    license='MIT License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_mitre_integration'",
    long_description="fn_mitre_integration support retrieving information related to MITRE ATT&CK tactics and technique from MITRE STIX TAXII server.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'stix2',
        'taxii2-client'
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