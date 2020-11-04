#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_datatable_utils',
    version='1.1.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="Functions that allow you to Get, Update or Delete a single row or Get or Delete multiple rows in a Data Table",
    long_description="This package contains 5 functions that help you manipulate IBM Resilient Data Tables: Get Row, Update Row, Delete Row, Get Rows and Delete Rows.",
    install_requires=[
        'resilient_circuits>=33.0.0',
        'resilient-lib>=32.0.140',
        'cachetools'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "DtUtilsGetRowFunctionComponent = fn_datatable_utils.components.dt_utils_get_row:FunctionComponent",
            "DtUtilsUpdateRowFunctionComponent = fn_datatable_utils.components.dt_utils_update_row:FunctionComponent",
            "DtUtilsDeleteRowFunctionComponent = fn_datatable_utils.components.dt_utils_delete_row:FunctionComponent",
            "DtUtilsGetRowsFunctionComponent = fn_datatable_utils.components.dt_utils_get_rows:FunctionComponent",
            "DtUtilsDeleteRowsFunctionComponent = fn_datatable_utils.components.dt_utils_delete_rows:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_datatable_utils.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_datatable_utils.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_datatable_utils.util.selftest:selftest_function"]
    }
)