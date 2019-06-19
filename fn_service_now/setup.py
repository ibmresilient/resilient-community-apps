#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_service_now',
    version='1.0.1',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url='www.resilientsystems.com',
    description="Bi-directional synchronization of Incidents, Tasks, Notes and Attachments with ServiceNow",
    long_description="""Create an IBM Resilient Incident/Task from a ServiceNow Record in the Incident Table.
        Create a ServiceNow Record in the Incident Table from an IBM Resilient Incident/Task.
        Sync notes between a related IBM Resilient Incident/Task and a ServiceNow Record.
        Send Attachments from an IBM Resilient Incident/Task to a related ServiceNow Record.""",
    install_requires=[
        'resilient_circuits>=31.0.0',
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