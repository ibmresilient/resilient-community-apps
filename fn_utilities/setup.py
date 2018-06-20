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
        'openpyxl>=2.5.3'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "AttachmentHashFunctionComponent = fn_utilities.components.utilities_attachment_hash:FunctionComponent",
            "AttachmentToBase64FunctionComponent = fn_utilities.components.utilities_attachment_to_base64:FunctionComponent",
            "AttachmentZipExtractFunctionComponent = fn_utilities.components.utilities_attachment_zip_extract:FunctionComponent",
            "AttachmentZipListFunctionComponent = fn_utilities.components.utilities_attachment_zip_list:FunctionComponent",
            "Base64ToArtifactFunctionComponent = fn_utilities.components.utilities_base64_to_artifact:FunctionComponent",
            "Base64ToAttachmentFunctionComponent = fn_utilities.components.utilities_base64_to_attachment:FunctionComponent",
            "CallRestApiFunctionComponent = fn_utilities.components.utilities_call_rest_api:FunctionComponent",
            "DomainDistanceFunctionComponent = fn_utilities.components.utilities_domain_distance:FunctionComponent",
            "EmailParseFunctionComponent = fn_utilities.components.utilities_email_parse:FunctionComponent",
            "ExcelQueryComponent = fn_utilities.components.utilities_excel_query:FunctionComponent",
            "PDFidFunctionComponent = fn_utilities.components.utilities_pdfid:FunctionComponent",
            "ResilientSearchFunctionComponent = fn_utilities.components.utilities_resilient_search:FunctionComponent",
            "ShellCommandFunctionComponent = fn_utilities.components.utilities_shell_command:FunctionComponent",
            "StringToAttachmentFunctionComponent = fn_utilities.components.utilities_string_to_attachment:FunctionComponent",
            "ExpandURLFunctionComponent = fn_utilities.components.utilities_expand_url:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_utilities.util.customize:customization_data"]
    }
)
