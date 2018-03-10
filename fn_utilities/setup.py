#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_utilities',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Utility Functions",
    long_description="Resilient Circuits Utility Functions",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'openpyxl'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "ArtifactEmailParseFunctionComponent = fn_utilities.components.artifact_email_parse:FunctionComponent",
            "AttachmentHashFunctionComponent = fn_utilities.components.attachment_hash:FunctionComponent",
            "AttachmentMoveToArtifactFunctionComponent = fn_utilities.components.attachment_move_to_artifact:FunctionComponent",
            "AttachmentToBase64FunctionComponent = fn_utilities.components.attachment_to_base64:FunctionComponent",
            "AttachmentZipExtractFunctionComponent = fn_utilities.components.attachment_zip_extract:FunctionComponent",
            "AttachmentZipListFunctionComponent = fn_utilities.components.attachment_zip_list:FunctionComponent",
            "Base64ToArtifactFunctionComponent = fn_utilities.components.base64_to_artifact:FunctionComponent",
            "Base64ToAttachmentFunctionComponent = fn_utilities.components.base64_to_attachment:FunctionComponent",
            "DomainDistanceFunctionComponent = fn_utilities.components.domain_distance:FunctionComponent",
            "SpreadsheetReadFunctionComponent = fn_utilities.components.spreadsheet_read:FunctionComponent",
            "SpreadsheetWriteFunctionComponent = fn_utilities.components.spreadsheet_write:FunctionComponent",
            "WaitFunctionComponent = fn_utilities.components.wait:FunctionComponent",
        ],
        "resilient.circuits.configsection": ["gen_config = fn_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_utilities.util.customize:customization_data"]
    }
)