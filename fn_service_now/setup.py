#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_service_now',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_service_now'",
    long_description="Resilient Circuits Components for 'fn_service_now'",
    install_requires=[
        'resilient_circuits>=30.0.0',
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
            "SnUtilitiesGetSysIdFunctionComponent = fn_service_now.components.sn_utilities_get_sys_id:FunctionComponent",
            "SnUtilitiesAddCommentToServicenowRecordFunctionComponent = fn_service_now.components.sn_utilities_add_comment_to_servicenow_record:FunctionComponent",
            "SnUtilitiesAddAttachmentToServicenowRecordFunctionComponent = fn_service_now.components.sn_utilities_add_attachment_to_servicenow_record:FunctionComponent",
            "SnUtilitiesCreateInServicenowFunctionComponent = fn_service_now.components.sn_utilities_create_in_servicenow:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_service_now.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_service_now.util.customize:customization_data"]
    }
)