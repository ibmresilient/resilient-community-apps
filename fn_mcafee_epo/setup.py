#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mcafee_epo',
    setup_requires=['setuptools_scm'],
    use_scm_version={"root": "../", "relative_to": __file__},
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for functions with McAfee ePO",
    long_description="Resilient Circuits Components for functions with McAfee ePO",
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
            "McafeeTagAnEpoAssetFunctionComponent = fn_mcafee_epo.components.mcafee_tag_an_epo_asset:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee_epo.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee_epo.util.customize:customization_data"]
    }
)