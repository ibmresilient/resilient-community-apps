#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mcafee_esm',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_mcafee_esm'",
    long_description="Set of functions to call different APIs in ESM",
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
            "McafeeEsmGetCaseDetailFunctionComponent = fn_mcafee_esm.components.mcafee_esm_get_case_detail:FunctionComponent",
            "McafeeEsmGetListOfCasesFunctionComponent = fn_mcafee_esm.components.mcafee_esm_get_list_of_cases:FunctionComponent",
            "McafeeEsmGetCaseEvenstsDetailFunctionComponent = fn_mcafee_esm.components.mcafee_esm_get_case_evensts_detail:FunctionComponent",
            "McafeeEsmEditCaseFunctionComponent = fn_mcafee_esm.components.mcafee_esm_edit_case:FunctionComponent",
            "McafeeEsmGetTriggeredAlarms = fn_mcafee_esm.mcafee_esm_get_triggered_alarms:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee_esm.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee_esm.util.customize:customization_data"]
    }
)