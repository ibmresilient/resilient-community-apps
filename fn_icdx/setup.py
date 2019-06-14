#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

from setuptools import setup, find_packages

setup(
    name='fn_icdx',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Integration with ICDX which provides access to the ICDX Search API over AMQP",
    long_description="The Symantec Integrated Cyber Defense Exchange (ICDX) is a central hub used to gather information from a number of different products in the Symantec Catalogue, normalising the information from these products into a schema. This establishes ICDx as an enrichment platform reporting on events gathered from other Symantec products",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'pika==0.11.0',
        'ipaddress'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "IcdxFindEventsFunctionComponent = fn_icdx.components.icdx_find_events:FunctionComponent",
            "IcdxGetEventFunctionComponent = fn_icdx.components.icdx_get_event:FunctionComponent",
            "IcdxGetArchiveListFunctionComponent = fn_icdx.components.icdx_get_archive_list:FunctionComponent",
            "IcdxObserverComponent = fn_icdx.components.icdx_forwarder_observer:ICDXComponentObserver"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_icdx.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_icdx.util.customize:customization_data"]
    }
)