# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#!/usr/bin/env python

from setuptools import setup, find_packages
import glob
import ntpath


def get_module_name(module_path):
    """
    Return the module name of the module path
    """
    return ntpath.split(module_path)[1].split(".")[0]


def snake_to_camel(word):
    """
    Convert a word from snake_case to CamelCase
    """
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

setup(
    name='fn_grpc_interface',
    version='1.0.1',
    license='MIT',
    author='IBM SOAR',
    author_email='',
    url="http://ibm.biz/soarcommunity",
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
            "{}FunctionComponent = fn_grpc_interface.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./fn_grpc_interface/components/[a-zA-Z]*.py")
        ],
        "resilient.circuits.configsection": ["gen_config = fn_grpc_interface.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_grpc_interface.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_grpc_interface.util.selftest:selftest_function"]
    }
)
