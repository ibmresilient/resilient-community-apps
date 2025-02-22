#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_pipl',
    version='1.1.3',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    description="Functions to query Pipl Data API",
    long_description="This package contains one function that enriches your leads (name, email address, phone number, or social media username) with Pipl and gets their personal, professional, demographic, and contact information. The response from Pipl is saved in Pipl possible person datatable. The package also contains a script for creating an artifact from a selected row in the datatable.",
    install_requires=[
        'resilient_circuits>=50.0.0',
        'piplapis-python~=5.2.0'
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
            "PiplSearchFunctionFunctionComponent = fn_pipl.components.pipl_search_function:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_pipl.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_pipl.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_pipl.util.selftest:selftest_function"]
    }
)