# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='fn_cve_search',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_cve_search'",
    long_description="Resilient Circuits Components for 'fn_cve_search'",
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
            "FunctionCveFunctionComponent = fn_cve_search.components.function_cve:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cve_search.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cve_search.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_cve_search.util.selftest:selftest_function"]
    }
)