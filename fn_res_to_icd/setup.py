#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_res_to_icd',
    version='1.0.0',
    license='MIT',
    author='Sean O Gorman',
    author_email='sean.gorman@ibm.com',
    url='IBM Security',
    description="Resilient Circuits Components for 'fn_res_to_icd'",
    long_description="Resilient Circuits Components for 'fn_res_to_icd'",
    install_requires=[
        'resilient_circuits>=30.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnResToIcdFunctionComponent = fn_res_to_icd.components.fn_res_to_icd:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_res_to_icd.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_res_to_icd.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_res_to_icd.util.selftest:selftest_function"]
    }
)