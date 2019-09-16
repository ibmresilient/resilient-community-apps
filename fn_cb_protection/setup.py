#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

from setuptools import setup, find_packages

setup(
    name='fn_cb_protection',
    version='1.0.2',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'fn_cb_protection'",
    long_description="Resilient Circuits Components for 'fn_cb_protection'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient_lib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "Bit9FileInstanceUpdateFunctionComponent = fn_cb_protection.components.bit9_file_instance_update:FunctionComponent",
            "Bit9FileInstanceQueryFunctionComponent = fn_cb_protection.components.bit9_file_instance_query:FunctionComponent",
            "Bit9FileRuleDeleteFunctionComponent = fn_cb_protection.components.bit9_file_rule_delete:FunctionComponent",
            "Bit9ApprovalRequestUpdateFunctionComponent = fn_cb_protection.components.bit9_approval_request_update:FunctionComponent",
            "Bit9FileRuleUpdateFunctionComponent = fn_cb_protection.components.bit9_file_rule_update:FunctionComponent",
            "Bit9ApprovalRequestGetFunctionComponent = fn_cb_protection.components.bit9_approval_request_get:FunctionComponent",
            "Bit9FileCatalogGetFunctionComponent = fn_cb_protection.components.bit9_file_catalog_get:FunctionComponent",
            "Bit9ApprovalRequestQueryFunctionComponent = fn_cb_protection.components.bit9_approval_request_query:FunctionComponent",
            "Bit9FileRuleGetFunctionComponent = fn_cb_protection.components.bit9_file_rule_get:FunctionComponent",
            "Bit9FileCatalogQueryFunctionComponent = fn_cb_protection.components.bit9_file_catalog_query:FunctionComponent",
            "Bit9FileRuleQueryFunctionComponent = fn_cb_protection.components.bit9_file_rule_query:FunctionComponent",
            "Bit9PollComponent = fn_cb_protection.components.bit9_poll:Bit9PollComponent",
            "Bit9FileDeleteFunctionComponent = fn_cb_protection.components.bit9_file_delete:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cb_protection.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cb_protection.util.customize:customization_data"]
    }
)
