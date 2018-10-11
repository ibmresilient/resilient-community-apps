#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_gcp',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'fn_gcp'",
    long_description="Resilient Circuits Components for 'fn_gcp'",
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
            "GcpUtilitiesScreenshotSandboxedWebpageFunctionComponent = fn_gcp.components.gcp_utilities_screenshot_sandboxed_webpage:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_gcp.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_gcp.util.customize:customization_data"]
    }
)