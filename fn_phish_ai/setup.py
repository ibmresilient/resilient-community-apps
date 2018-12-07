#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_phish_ai',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components for 'fn_phish_ai'",
    long_description="Resilient Circuits Components for 'fn_phish_ai'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'phish-ai-api'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "PhishAiScanUrlFunctionComponent = fn_phish_ai.components.phish_ai_scan_url:FunctionComponent",
            "PhishAiGetReportFunctionComponent = fn_phish_ai.components.phish_ai_get_report:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_phish_ai.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_phish_ai.util.customize:customization_data"]
    }
)