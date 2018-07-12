#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_thug',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_thug'",
    long_description="Resilient Circuits Components for 'fn_thug'",
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
            "ThugFunctionComponent = fn_thug.components.thug:FunctionComponent",
            "Base64ToAttachmentFunctionComponent = fn_thug.components.base64_to_attachment:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_thug.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_thug.util.customize:customization_data"]
    }
)