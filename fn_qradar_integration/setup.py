#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_qradar_integration',
    version='2.0.3',
    license='MIT License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_qradar_integration'",
    long_description="fn_qradar_integration supports performing ariel search to retrieve data from QRadar. It also provide functions to find/add/delete reference set items.",
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
            "QradarFindReferenceSetsFunctionComponent = fn_qradar_integration.components.qradar_find_reference_sets:FunctionComponent",
            "QradarDeleteReferenceSetItemFunctionComponent = fn_qradar_integration.components.qradar_delete_reference_set_item:FunctionComponent",
            "QradarAddReferenceSetItemFunctionComponent = fn_qradar_integration.components.qradar_add_reference_set_item:FunctionComponent",
            "QradarFindReferenceSetItemFunctionComponent = fn_qradar_integration.components.qradar_find_reference_set_item:FunctionComponent",
            "QradarSearchFunctionComponent = fn_qradar_integration.components.qradar_search:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_qradar_integration.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_qradar_integration.util.customize:customization_data"]
    }
)