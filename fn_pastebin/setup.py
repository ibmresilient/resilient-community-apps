#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_pastebin',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Function that dumps any text/code to pastebin.com and returns a link to that paste",
    long_description="This package contains one function that creates a Paste on Pastebin and returns a link to that Paste",
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