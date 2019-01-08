#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_datatable_utils',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='http://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for 'fn_datatable_utils'",
    long_description="Resilient Circuits Components for 'fn_datatable_utils'",
    install_requires=[
        'resilient_circuits>=31.0.0'
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
            "DtUtilsDeleteRowFunctionComponent = fn_datatable_utils.components.dt_utils_delete_row:FunctionComponent"

        ],
        "resilient.circuits.configsection": ["gen_config = fn_datatable_utils.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_datatable_utils.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_datatable_utils.util.selftest:selftest_function"]
    }
)