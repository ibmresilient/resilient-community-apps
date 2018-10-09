# (c) Copyright IBM Corp. 2018. All Rights Reserved.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_grr',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    description="Resilient Circuits Components GRR Search Function",
    long_description="A Resilient Circuits Function to allow you to search your GRR Agents by user, ip or host",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'grr_api_client>=2.3.4'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "GrrSearchFunctionComponent = fn_grr.components.grr_search:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_grr.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_grr.util.customize:customization_data"]
    }
)