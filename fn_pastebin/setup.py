#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_pastebin',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_pastebin'",
    long_description="Resilient Circuits Components for 'fn_pastebin'",
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
            "FnCreatePastebinFunctionComponent = fn_pastebin.components.fn_create_pastebin:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_pastebin.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_pastebin.util.customize:customization_data"]
    }
)