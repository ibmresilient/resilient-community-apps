#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_cloud_foundry',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_cloud_foundry'",
    long_description="Resilient Circuits Components for 'fn_cloud_foundry'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'requests'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnCloudFoundryManageApplicationsFunctionComponent = fn_cloud_foundry.components.fn_cloud_foundry_manage_applications:FunctionComponent",
            "FnCloudFoundryInstanceCommandFunctionComponent = fn_cloud_foundry.components.fn_cloud_foundry_instance_command:FunctionComponent",
            "FnCloudFoundryCreateAppFunctionComponent = fn_cloud_foundry.components.fn_cloud_foundry_create_app:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cloud_foundry.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cloud_foundry.util.customize:customization_data"]
    }
)