#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_google_cloud_functions',
    version='1.0.0',
    license='MIT',
    author='Ryan',
    author_email='ryan@resilientlab.co.uk',
    description="Resilient Circuits Components used to Invoke Google Cloud Functions",
    long_description="Includes a Resilient Circuits Function to allow you to send a URL to a cloud function for sandboxing and returning a screenshot of the page",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'fn_utilities'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "GcpCloudFunctionsSandboxAndScreenshotWebpageFunctionComponent = fn_google_cloud_functions.components.gcp_cloud_functions_sandbox_and_screenshot_webpage:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_google_cloud_functions.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_google_cloud_functions.util.customize:customization_data"]
    }
)