#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_watson_translate',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_watson_translate'",
    long_description="Resilient Circuits Components for 'fn_watson_translate'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'watson_developer_cloud>=1.4.0',
        'bs4'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnWatsonTranslateFunctionComponent = fn_watson_translate.components.fn_watson_translate:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_watson_translate.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_watson_translate.util.customize:customization_data"]
    }
)