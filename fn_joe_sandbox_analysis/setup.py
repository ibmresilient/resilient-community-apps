#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_joe_sandbox_analysis',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_joe_sandbox_analysis'",
    long_description="Resilient Circuits Components for 'fn_joe_sandbox_analysis'",
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
            "FnJoeSandboxAnalysisFunctionComponent = fn_joe_sandbox_analysis.components.fn_joe_sandbox_analysis:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_joe_sandbox_analysis.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_joe_sandbox_analysis.util.customize:customization_data"]
    }
)