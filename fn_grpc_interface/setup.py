#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_grpc_interface',
    version='1.0.0',
    license='<<insert here>>',
    author='<<your name here>>',
    author_email='you@example.com',
    url='<<your company url>>',
    description="Resilient Circuits Components for 'fn_grpc_interface'",
    long_description="Resilient Circuits Components for 'fn_grpc_interface'",
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
            "FunctionGrpcFunctionComponent = fn_grpc_interface.components.function_grpc:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_grpc_interface.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_grpc_interface.util.customize:customization_data"]
    }
)