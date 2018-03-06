#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mcafee_tie_functions',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_mcafee_tie_functions'",
    long_description="Resilient Circuits Components for 'fn_mcafee_tie_functions'",
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
            "McafeeTieSearchHashFunctionComponent = fn_mcafee_tie_functions.components.mcafee_tie_search_hash:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee_tie_functions.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee_tie_functions.util.customize:customization_data"]
    }
)