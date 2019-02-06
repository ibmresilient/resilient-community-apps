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
            "FnSnowAddAttachmentToRecordFunctionComponent = fn_service_now.components.fn_snow_add_attachment_to_record:FunctionComponent",
            "FnSnowAddNoteToRecordFunctionComponent = fn_service_now.components.fn_snow_add_note_to_record:FunctionComponent",
            "FnSnowCloseRecordFunctionComponent = fn_service_now.components.fn_snow_close_record:FunctionComponent",
            "FnSnowCreateRecordFunctionComponent = fn_service_now.components.fn_snow_create_record:FunctionComponent",
            "FnSnowHelperAddTaskNoteFunctionComponent = fn_service_now.components.fn_snow_helper_add_task_note:FunctionComponent",
            "FnSnowHelperUpdateDatatableFunctionComponent = fn_service_now.components.fn_snow_helper_update_datatable:FunctionComponent",
            "FnSnowLookupSysidFunctionComponent = fn_service_now.components.fn_snow_lookup_sysid:FunctionComponent",
            "FnSnowUpdateRecordFunctionComponent = fn_service_now.components.fn_snow_update_record:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_service_now.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_service_now.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_service_now.util.selftest:selftest_function"]
    }
)