# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
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
    description="Resilient Circuits Components for 'fn_grpc_interface'",
    long_description="""The resilient gRPC interface provides a general wrapper for the client application and can call methods on
                     a server application on a different machine as if it was a local object,making it easier for you 
                     create distributed application and services with IBM resilient.
                     In this edition we have implemented only simple RPC(Remote Procedure call) gRPC Service method.
                     for more details - https://grpc.io/docs/.
                     """,
    install_requires=[
        'resilient_circuits>=30.0.0',
        'grpcio',
        'grpcio-tools'
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