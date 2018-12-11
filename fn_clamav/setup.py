#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_clamav',
    version='1.0.0',
    license='Resilient License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_clamav'",
    long_description="Resilient Circuits Components for 'fn_clamav'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'pyclamd >= 0.4.0'

    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "ClamavScanStreamFunctionComponent = fn_clamav.components.clamav_scan_stream:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_clamav.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_clamav.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_clamav.util.selftest:selftest_function"]
    }
)