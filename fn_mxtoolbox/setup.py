#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mxtoolbox',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_mxtoolbox'",
    long_description="Resilient Circuits Components for 'fn_mxtoolbox'",
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
            "FnMxtoolboxFunctionComponent = fn_mxtoolbox.components.fn_mxtoolbox:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mxtoolbox.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mxtoolbox.util.customize:customization_data"]
    }
)