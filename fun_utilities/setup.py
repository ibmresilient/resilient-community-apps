#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fun_utilities',
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
            "ArtifactEmailParseFunctionComponent = fun_utilities.components.artifact_email_parse:FunctionComponent",
            "AttachmentHashFunctionComponent = fun_utilities.components.attachment_hash:FunctionComponent",
            "AttachmentMoveToArtifactFunctionComponent = fun_utilities.components.attachment_move_to_artifact:FunctionComponent",
            "AttachmentToBase64FunctionComponent = fun_utilities.components.attachment_to_base64:FunctionComponent",
            "AttachmentZipExtractFunctionComponent = fun_utilities.components.attachment_zip_extract:FunctionComponent",
            "AttachmentZipListFunctionComponent = fun_utilities.components.attachment_zip_list:FunctionComponent",
            "Base64ToArtifactFunctionComponent = fun_utilities.components.base64_to_artifact:FunctionComponent",
            "Base64ToAttachmentFunctionComponent = fun_utilities.components.base64_to_attachment:FunctionComponent",
            "DomainDistanceFunctionComponent = fun_utilities.components.domain_distance:FunctionComponent",
            "WaitFunctionComponent = fun_utilities.components.wait:FunctionComponent",
        ],
        "resilient.circuits.configsection": ["gen_config = fun_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fun_utilities.util.customize:customization_data"]
    }
)