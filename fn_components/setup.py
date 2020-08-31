# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='fn_components',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="Resilient Circuits components for single-file integrations",
    long_description="""This is a shell container for running single-file integrations which are added to the components/ directory""",
    install_requires=[
        'resilient_circuits>=37.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.configsection": ["gen_config = fn_components.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_components.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_components.util.selftest:selftest_function"]
    }
)
