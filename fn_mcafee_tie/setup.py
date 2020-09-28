#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mcafee_tie',
    version="1.0.2",
    license='MIT',
    author='IBM Resilient',
    author_email='',
    url='https://ibm.com/mysupport',
    description="Resilient Circuits Components for McAfee TIE Functions",
    long_description="Resilient Circuits Components for McAfee TIE Functions",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'dxltieclient',
        'dxlclient'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "McafeeTieSearchHashFunctionComponent = fn_mcafee_tie.components.mcafee_tie_search_hash:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee_tie.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee_tie.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_mcafee_tie.util.selftest:selftest_function"]
    }
)