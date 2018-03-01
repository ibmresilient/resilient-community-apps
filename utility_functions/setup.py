#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='utility_functions',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Utility Functions",
    long_description="Resilient Circuits Utility Functions",
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
            "AttachmentHashFunctionComponent = utility_functions.components.attachment_hash:FunctionComponent",
            "AttachmentMoveToArtifactFunctionComponent = utility_functions.components.attachment_move_to_artifact:FunctionComponent",
            "AttachmentZipExtractFunctionComponent = utility_functions.components.attachment_zip_extract:FunctionComponent",
            "AttachmentZipExtractToArtifactFunctionComponent = utility_functions.components.attachment_zip_extract_to_artifact:FunctionComponent",
            "AttachmentZipListFunctionComponent = utility_functions.components.attachment_zip_list:FunctionComponent",
            "WaitFunctionComponent = utility_functions.components.wait:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = utility_functions.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = utility_functions.util.customize:customization_data"]
    }
)