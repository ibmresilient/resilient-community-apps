#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_joe_sandbox_analysis',
    version='1.0.3',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Joe Sandbox Function",
    long_description="Resilient Circuits Joe Sandbox Function",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'jbxapi'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnJoeSandboxAnalysisFunctionComponent = fn_joe_sandbox_analysis.components.fn_joe_sandbox_analysis:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_joe_sandbox_analysis.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_joe_sandbox_analysis.util.customize:customization_data"]
    }
)