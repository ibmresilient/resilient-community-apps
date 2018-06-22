#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

PUBLISH_VERSION = "1.1.0"

setup(
    name='fn_mcafee_opendxl',
    version=PUBLISH_VERSION,
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for McAfee publishing to DXL Functions",
    long_description="Resilient Circuits Components for McAfee publishing to DXL Functions",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'dxlclient'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "McafeePublishToDxlFunctionComponent = fn_mcafee_opendxl.components.mcafee_publish_to_dxl:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee_opendxl.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee_opendxl.util.customize:customization_data"]
    }
)
