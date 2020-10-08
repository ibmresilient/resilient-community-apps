#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_cloud_foundry',
    version='1.0.1',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_cloud_foundry'",
    long_description="This Resilient function interacts with Cloud Foundry platforms to allow the a Resilient user to manage deployed applications, "
                     "their instances, and deploy new applications. Managing applications includes: starting/stopping, "
                     "updating, re-staging, deleting, and getting various types of information about them. "
                     "This package implements these actions in 3 functions, 3 example workflows and 3 example rules. "
                     "This package is a wrapper around Cloud Foundry’s API with possibilities to be adjusted for different platform providers.",
    install_requires=[
        'resilient_circuits>=34.0.0',
        'resilient_lib>=34.0.0'
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