#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_rsa_netwitness',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_rsa_netwitness'",
    long_description="Resilient Circuits Components for 'fn_rsa_netwitness'",
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
            "NetwitnessQueryEventSessionFunctionComponent = fn_rsa_netwitness.components.netwitness_query_event_session:FunctionComponent",
            "NetwitnessQuery = fn_rsa_netwitness.components.netwitness_query:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_rsa_netwitness.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_rsa_netwitness.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_rsa_netwitness.util.selftest:selftest_function"]
    }
)