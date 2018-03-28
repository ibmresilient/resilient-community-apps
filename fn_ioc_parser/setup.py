#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
from setuptools import setup, find_packages

setup(
    name='fn_ioc_parser',
    setup_requires=['setuptools_scm'],
    use_scm_version={"root": "../", "relative_to": __file__},
    license='Resilient License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_ioc_parser'",
    long_description="Resilient Circuits Components for 'fn_ioc_parser'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'iocp',
        'pdfminer'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "IocParserFunctionComponent = fn_ioc_parser.components.ioc_parser:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_ioc_parser.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_ioc_parser.util.customize:customization_data"]
    }
)