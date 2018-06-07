#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_odbc_query',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_odbc_query'",
    long_description="Resilient Circuits Components for 'fn_odbc_query'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'pyodbc'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnOdbcQueryFunctionComponent = fn_odbc_query.components.odbc_query:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_odbc_query.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_odbc_query.util.customize:customization_data"]
    }
)