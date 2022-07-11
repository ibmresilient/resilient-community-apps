#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

from setuptools import setup, find_packages

setup(
    name='fn_icdx',
    display_name='Symantec ICDx',
    version='1.1.0',
    license='MIT',
    author='IBM SOAR',
    description="Integration with ICDx which provides access to the ICDx Search API over AMQP",
    long_description="""The Symantec Integrated Cyber Defense Exchange (ICDx) is a central hub used \
to gather information from a number of different products in the Symantec Catalogue, normalising the \
information from these products into a schema. This establishes ICDx as an enrichment platform \
reporting on events gathered from other Symantec products""",
    install_requires=[
        'resilient_circuits>=45.0.0',
        'pika~=1.3',
        'ipaddress'
    ],
    python_requires='>=3.6',
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
        "resilient.circuits.customize": ["customize = fn_icdx.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_icdx.util.selftest:selftest_function"]

    }
)