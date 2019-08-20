#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_bigfix',
    version='1.1.1',
    license='Resilient License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_bigfix'",
    long_description="Resilient Circuits Components for 'fn_bigfix'",
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
            "FnBigfixAssetsFunctionComponent = fn_bigfix.components.fn_bigfix_assets:FunctionComponent",
            "FnBigfixActionStatusFunctionComponent = fn_bigfix.components.fn_bigfix_action_status:FunctionComponent",
            "FnBigfixArtifactFunctionComponent = fn_bigfix.components.fn_bigfix_artifact:FunctionComponent",
            "FnBigfixRemediationFunctionComponent = fn_bigfix.components.fn_bigfix_remediation:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_bigfix.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_bigfix.util.customize:customization_data"]
    }
)