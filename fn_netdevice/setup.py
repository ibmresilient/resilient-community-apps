#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fn_netdevice',
    version='1.0.0',
    license='MIT',
    author='Resilient Labs',
    author_email='resil.labs@gmail.com',
    url='https://ibm.biz/resilientcommunity',
    description="Resilient Circuits Components for 'fn_netdevice'",
    long_description="Resilient Circuits Components for 'fn_netdevice'",
    install_requires=[
        'resilient_circuits>=30.0.0',
        'netmiko>=2.3.3'
    ],
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        "resilient.circuits.components": [
            "NetworkDeviceFunctionComponent = fn_netdevice.components.network_device:FunctionComponent"
        ],
        "resilient.circuits.configsection": ["gen_config = fn_netdevice.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = fn_netdevice.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = fn_netdevice.util.selftest:selftest_function"]
    }
)