#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_maas360',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_maas360'",
    long_description="Resilient Circuits Components for 'fn_maas360'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "Maas360BasicSearchFunctionComponent = fn_maas360.components.maas360_basic_search:FunctionComponent",
            "Maas360ActionFunctionComponent = fn_maas360.components.maas360_action:FunctionComponent",
            "Maas360StopAppDistFunctionComponent = fn_maas360.components.maas360_stop_app_distribution:FunctionComponent",
            "Maas360DeleteAppFunctionComponent = fn_maas360.components.maas360_delete_app:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_maas360.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_maas360.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_maas360.util.selftest:selftest_function"]
    }
)