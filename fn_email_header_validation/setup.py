#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_email_header_validation',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_email_header_validation'",
    long_description="Resilient Circuits Components for 'fn_email_header_validation'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'dkimpy'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "EmailHeaderValidationUsingDkimarcFunctionComponent = fn_email_header_validation.components.email_header_validation_using_dkimarc:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_email_header_validation.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_email_header_validation.util.customize:customization_data"]
    }
)