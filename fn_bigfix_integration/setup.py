#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_bigfix_integration',
    version='1.0.0',
    license='Resilient License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_bigfix_integration'",
    long_description="Resilient Circuits Components for 'fn_bigfix_integration'",
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
            "FnBigfixAssetsFunctionComponent = fn_bigfix_integration.components.fn_bigfix_assets:FunctionComponent",
            "FnBigfixArtifactFunctionComponent = fn_bigfix_integration.components.fn_bigfix_artifact:FunctionComponent",
            "FnBigfixRemediationFunctionComponent = fn_bigfix_integration.components.fn_bigfix_remediation:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_bigfix_integration.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_bigfix_integration.util.customize:customization_data"]
    }
)