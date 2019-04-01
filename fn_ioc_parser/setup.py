# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_ioc_parser',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits Components for 'fn_ioc_parser'",
    long_description="Resilient Circuits Components for 'fn_ioc_parser'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'iocparser>=1.0.14',
        'resilient-lib>=32.0.126',
        'pdfminer.six >=20181108',
        'python-docx>=0.8.10'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FunctionIocParserFunctionComponent = fn_ioc_parser.components.function_ioc_parser:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ioc_parser.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ioc_parser.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_ioc_parser.util.selftest:selftest_function"]
    }
)