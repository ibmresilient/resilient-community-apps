# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='fn_grpc_interface',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://github.com/ibmresilient/resilient-community-apps',
    description="This Function provides a general purpose wrapper that allows you to call gRPC services from within IBM Resilient",
    long_description="""This Function provides a general wrapper that allows you to call gRPC services from within IBM Resilient,
                    making it easier for you create distributed application and services with IBM Resilient.""",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'grpcio>=1.19.0',
        'grpcio-tools>=1.19.0'
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
