#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_virustotal',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_virustotal'",
    long_description="Resilient Circuits Components for 'fn_virustotal'",
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
            "VirustotalFunctionComponent = fn_virustotal.components.virustotal:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_virustotal.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_virustotal.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_virustotal.util.selftest:selftest_function"]
    }
)