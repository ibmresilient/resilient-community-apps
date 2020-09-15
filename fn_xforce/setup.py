#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
from setuptools import setup, find_packages

setup(
    name='fn_xforce',
    version='1.0.1',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    url="http://ibm.biz/resilientcommunity",
    description="Resilient Circuits Components for the IBM XForce Collections API",
    long_description="The fn_xforce integration provides the ability to query the IBM XForce Collections API. "
                     "Collections can be queried either by matching a provided search term or by Collection ID. "
                     "Additionally, it is possible to query both public and private Collections. "
                     "Information gathered from X-Force can be used for incident and artifact enrichment.",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>=34.0.0'
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
        "resilient.circuits.customize": ["customize = fn_xforce.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_xforce.util.selftest:selftest_function"]
    }
)