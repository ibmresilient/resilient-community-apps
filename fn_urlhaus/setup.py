#!/usr/bin/env python
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_urlhaus',
    version='1.0.2',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://ibm.biz/resilientcommunity',
    description="Look up artifacts in URLhaus + sumbit malicious URLs",
    long_description="""Look up supported artifacts in URLhaus to get more enrichment information.
        Also supports submitting malicious URLs to URLhaus""",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'resilient-lib>=32.0.140'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "UrlHausFunctionComponent = fn_urlhaus.components.funct_fn_urlhaus:FunctionComponent",
            "UrlHausSubmissionFunctionComponent = fn_urlhaus.components.funct_fn_urlhaus_submission:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_urlhaus.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_urlhaus.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_urlhaus.util.selftest:selftest_function"]
    }
)