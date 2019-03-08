#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_sep',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient Support',
    author_email='support@resilientsystems.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_sep'",
    long_description="Resilient Circuits Components for 'fn_sep'",
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
            "FnSepGetFileDetailsFunctionComponent = fn_sep.components.fn_sep_get_file_details:FunctionComponent",
            "FnSepUploadFileToSepmFunctionComponent = fn_sep.components.fn_sep_upload_file_to_sepm:FunctionComponent",
            "FnSepGetFingerprintListFunctionComponent = fn_sep.components.fn_sep_get_fingerprint_list:FunctionComponent",
            "FnSepMoveClientFunctionComponent = fn_sep.components.fn_sep_move_client:FunctionComponent",
            "FnSepGetPoliciesFunctionComponent = fn_sep.components.fn_sep_get_policies:FunctionComponent",
            "FnSepGetComputersFunctionComponent = fn_sep.components.fn_sep_get_computers:FunctionComponent",
            "FnSepGetDomainsFunctionComponent = fn_sep.components.fn_sep_get_domains:FunctionComponent",
            "FnSepQuarantineEndpointsFunctionComponent = fn_sep.components.fn_sep_quarantine_endpoints:FunctionComponent",
            "FnSepAddFingerprintListFunctionComponent = fn_sep.components.fn_sep_add_fingerprint_list:FunctionComponent",
            "FnSepScanEndpointsFunctionComponent = fn_sep.components.fn_sep_scan_endpoints:FunctionComponent",
            "FnSepGetGroupsFunctionComponent = fn_sep.components.fn_sep_get_groups:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_sep.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_sep.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_sep.util.selftest:selftest_function"]
    }
)
