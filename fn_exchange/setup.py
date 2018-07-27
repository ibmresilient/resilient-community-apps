#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_exchange',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    description="Resilient Circuits Components for 'fn_exchange'",
    long_description="Resilient Circuits Components for 'fn_exchange'",
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
            "ExchangeGetMailboxInfoFunctionComponent = fn_exchange.components.exchange_get_mailbox_info:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_exchange.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_exchange.util.customize:customization_data"]
    }
)