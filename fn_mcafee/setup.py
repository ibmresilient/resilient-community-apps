#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mcafee',
    version='1.0.0',
    license='MIT',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_mcafee'",
    long_description="Resilient Circuits Components for 'fn_mcafee'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'dxlclient',
        'dxleposervice'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "McafeeTagAnEpoAssetFunctionComponent = fn_mcafee.components.mcafee_tag_an_epo_asset:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee.util.customize:customization_data"]
    }
)