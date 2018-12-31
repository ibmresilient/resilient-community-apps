#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_GRPC_Interface',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_GRPC_Interface'",
    long_description="Resilient Circuits Components for 'fn_GRPC_Interface'",
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
            "GrpcFunctionComponent = fn_GRPC_Interface.components.grpc:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_GRPC_Interface.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_GRPC_Interface.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_GRPC_Interface.util.selftest:selftest_function"]
    }
)