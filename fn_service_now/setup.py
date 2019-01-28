#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_service_now',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url='www.resilientsystems.com',
    description="Resilient Circuits Components to Integrate with the ServiceNow Platform",
    long_description="Contains Functions to sync Incidents, Tasks, Notes and Attachments between IBM Resilient and ServiceNow",
    install_requires=[
        'resilient_circuits>=31.0.0',
        'requests',
        'beautifulsoup4>=4.6.3'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "SnUtilitiesCloseInServicenowFunctionComponent = fn_service_now.components.sn_utilities_close_in_servicenow:FunctionComponent",
            "SnUtilitiesCreateInServicenowFunctionComponent = fn_service_now.components.sn_utilities_create_in_servicenow:FunctionComponent",
            "SnUtilitiesAddNoteToServicenowRecordFunctionComponent = fn_service_now.components.sn_utilities_add_note_to_servicenow_record:FunctionComponent",
            "SnUtilitiesAddAttachmentToServicenowRecordFunctionComponent = fn_service_now.components.sn_utilities_add_attachment_to_servicenow_record:FunctionComponent",
            "SnowHelperAddTaskNoteFunctionComponent = fn_service_now.components.snow_helper_add_task_note:FunctionComponent",
            "SnUtilitiesGetSysIdFunctionComponent = fn_service_now.components.sn_utilities_get_sys_id:FunctionComponent",
            "SnUtilitiesUpdateDatatableFunctionComponent = fn_service_now.components.sn_utilities_update_datatable:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_service_now.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_service_now.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_service_now.util.selftest:selftest_function"]
    }
)