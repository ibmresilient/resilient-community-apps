# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_apility',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Minimal and Simple Anti-Abuse API",
    long_description="Apility.io can be defined as Threat Intelligence SaaS for developers and product companies that want to know in realtime if their existing or potential users have been classified as 'abusers' by one or more of these lists.",
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
            "FnApilityFunctionComponent = fn_apility.components.function_apility:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_apility.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_apility.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_apility.util.selftest:selftest_function"]
    }
)