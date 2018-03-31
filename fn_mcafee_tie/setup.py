#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_mcafee_tie',
    setup_requires=['setuptools_scm'],
    use_scm_version={"root": "../", "relative_to": __file__},
    url='https://github.com/ibmresilient/resilient-circuits-packages',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for McAfee TIE Functions",
    long_description="Resilient Circuits Components for McAfee TIE Functions",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'dxltieclient'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "McafeeTieSearchHashFunctionComponent = fn_mcafee_tie.components.mcafee_tie_search_hash:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_mcafee_tie.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_mcafee_tie.util.customize:customization_data"]
    }
)