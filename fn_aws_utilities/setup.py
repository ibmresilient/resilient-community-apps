#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_aws_utilities',
    version='1.0.0',
    license='MIT',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_aws_utilities'",
    long_description="Resilient Circuits Components for 'fn_aws_utilities'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'boto3',
        'fn_get_phone_numbers'  # Another resilient-circuits function required for example workflows
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "FnInvokeLambdaFunctionComponent = fn_aws_utilities.components.fn_invoke_lambda:FunctionComponent",
            "FnSendSmsViaSnsFunctionComponent = fn_aws_utilities.components.fn_send_sms_via_sns:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_aws_utilities.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_aws_utilities.util.customize:customization_data"]
    }
)