#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_cisco_amp4ep',
    version='1.0.0',
    license='Resilient License',
    author='IBM Resilient',
    author_email='support@resilientsystems.com',
    description="Resilient Circuits Components for 'fn_cisco_amp4ep'",
    long_description="Resilient Circuits Components for 'fn_cisco_amp4ep'",
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
            "FnAmpGetComputerTrajectoryFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_computer_trajectory:FunctionComponent",
            "FnAmpGetComputersFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_computers:FunctionComponent",
            "FnAmpGetActivityFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_activity:FunctionComponent",
            "FnAmpGetComputerFunctionComponent = fn_cisco_amp4ep.components.fn_amp_get_computer:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_cisco_amp4ep.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_cisco_amp4ep.util.customize:customization_data"]
    }
)