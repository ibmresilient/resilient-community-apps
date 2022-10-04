#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

from setuptools import setup, find_packages

setup(
    name='fn_mcafee_esm',
    version='1.0.2',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_mcafee_esm'",
    long_description="""The McAfee ESM integration with the Resilient platform allows for the escalation and enrichment 
        of cases between McAfee and the Resilient platform. The integration includes a poller and 6 functions. The 
        returned results can be used to make customized updates to the Resilient platform, such as updating incidents,
        data tables and so on. The integration can also be used to make updates to McAfee ESM cases.""",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib'
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
            "McafeeEsmGetCaseEvenstsDetailFunctionComponent = fn_mcafee_esm.components.mcafee_esm_get_case_events_detail:FunctionComponent",
            "McafeeEsmEditCaseFunctionComponent = fn_mcafee_esm.components.mcafee_esm_edit_case:FunctionComponent",
            "McafeeEsmGetTriggeredAlarms = fn_mcafee_esm.components.mcafee_esm_get_triggered_alarms:FunctionComponent",
            "McafeeEsmQueryLogs = fn_mcafee_esm.components.mcafee_esm_query:FunctionComponent",
            "McafeeEsmCasePolling = fn_mcafee_esm.components.mcafee_esm_case_polling:ESM_CasePolling"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee_esm.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee_esm.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_mcafee_esm.util.selftest:selftest_function"]
    }
)