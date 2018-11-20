#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
from setuptools import setup, find_packages

setup(
    name='fn_xforce',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    long_description="Resilient Circuits Components for 'fn_xforce'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'requests'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "XforceGetCollectionByIdFunctionComponent = fn_xforce.components.xforce_get_collection_by_id:FunctionComponent",
            "XforceQueryCollectionFunctionComponent = fn_xforce.components.xforce_query_collection:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_xforce.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_xforce.util.customize:customization_data"]
    }
)