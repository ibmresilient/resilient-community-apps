#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_utilities',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_utilities'",
    long_description="Resilient Circuits Components for 'fn_utilities'",
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
            "UtilitiesAttachmentToBase64FunctionComponent = fn_utilities.components.utilities_attachment_to_base64:FunctionComponent",
            "UtilitiesAttachmentZipExtractFunctionComponent = fn_utilities.components.utilities_attachment_zip_extract:FunctionComponent",
            "UtilitiesExpandUrlFunctionComponent = fn_utilities.components.utilities_expand_url:FunctionComponent",
            "UtilitiesExcelQueryFunctionComponent = fn_utilities.components.utilities_excel_query:FunctionComponent",
            "UtilitiesEmailParseFunctionComponent = fn_utilities.components.utilities_email_parse:FunctionComponent",
            "UtilitiesBase64ToArtifactFunctionComponent = fn_utilities.components.utilities_base64_to_artifact:FunctionComponent",
            "UtilitiesBase64ToAttachmentFunctionComponent = fn_utilities.components.utilities_base64_to_attachment:FunctionComponent",
            "UtilitiesShellCommandFunctionComponent = fn_utilities.components.utilities_shell_command:FunctionComponent",
            "UtilitiesAttachmentHashFunctionComponent = fn_utilities.components.utilities_attachment_hash:FunctionComponent",
            "UtilitiesPdfidFunctionComponent = fn_utilities.components.utilities_pdfid:FunctionComponent",
            "UtilitiesCallRestApiFunctionComponent = fn_utilities.components.utilities_call_rest_api:FunctionComponent",
            "UtilitiesDomainDistanceFunctionComponent = fn_utilities.components.utilities_domain_distance:FunctionComponent",
            "UtilitiesResilientSearchFunctionComponent = fn_utilities.components.utilities_resilient_search:FunctionComponent",
            "UtilitiesStringToAttachmentFunctionComponent = fn_utilities.components.utilities_string_to_attachment:FunctionComponent",
            "UtilitiesAttachmentZipListFunctionComponent = fn_utilities.components.utilities_attachment_zip_list:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_utilities.util.customize:customization_data"]
    }
)