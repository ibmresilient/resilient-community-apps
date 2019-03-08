#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_useragentanalysis',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_useragentanalysis'",
    long_description="Resilient Circuits Components for 'fn_useragentanalysis' to perform broswer user agent analysis",
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
            "FnUseragentanalysisFunctionComponent = fn_useragentanalysis.components.func_useragentanalysis:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_useragentanalysis.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_useragentanalysis.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_useragentanalysis.util.selftest:selftest_function"]
    }
)